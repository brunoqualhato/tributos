"""Conversão de PDFs de atos normativos (texto nativo) para Markdown estruturado.

Usado para atos do Comitê Gestor do IBS (CGIBS) publicados apenas em PDF, como a
Resolução CGIBS nº 6/2026 (Regulamento do IBS). Requer o utilitário `pdftotext` (poppler).

Estratégia:
- corpo normativo: `pdftotext` em modo de fluxo (sem -layout), removendo sumário, números de
  página e quebras de linha artificiais, preservando uma linha lógica por dispositivo
  (artigo, parágrafo, inciso, alínea) e por título de agrupador (Livro, Título, Capítulo, Seção);
- anexos tabulares: `pdftotext -layout`, preservados em blocos de código para manter as colunas.
"""
from pathlib import Path
import re
import subprocess

INICIO_BLOCO = re.compile(
    r"^(Art\.\s|§\s?\d|Parágrafo único|[IVXLC]+\s+[-–]\s|[a-z]{1,2}\)\s|\d{1,2}\.\s|"
    r"LIVRO\b|TÍTULO\b|CAPÍTULO\b|Seção\b|Subseção\b|SEÇÃO\b|SUBSEÇÃO\b|ANEXO\b|“|\")"
)
AGRUPADOR = re.compile(r"^(LIVRO|TÍTULO|CAPÍTULO|Seção|Subseção|SEÇÃO|SUBSEÇÃO)\b")
NUMERO_PAGINA = re.compile(r"^\d{1,3}$")


def pdftotext(pdf: Path, layout: bool = False, primeira: int = None, ultima: int = None) -> str:
    cmd = ["pdftotext"]
    if layout:
        cmd.append("-layout")
    if primeira:
        cmd += ["-f", str(primeira)]
    if ultima:
        cmd += ["-l", str(ultima)]
    cmd += [str(pdf), "-"]
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def numero_paginas(pdf: Path) -> int:
    saida = subprocess.run(["pdfinfo", str(pdf)], check=True, capture_output=True, text=True).stdout
    return int(re.search(r"^Pages:\s+(\d+)", saida, re.M).group(1))


def _reflow(linhas: list[str]) -> list[str]:
    """Une linhas quebradas artificialmente, mantendo um bloco por dispositivo."""
    blocos: list[str] = []
    for bruta in linhas:
        linha = bruta.strip()
        if not linha:
            continue
        if NUMERO_PAGINA.fullmatch(linha):
            continue
        if not blocos or INICIO_BLOCO.match(linha):
            blocos.append(linha)
            continue
        anterior = blocos[-1]
        # continuação de um agrupador cujo nome ocupa mais de uma linha
        blocos[-1] = f"{anterior} {linha}"
    return blocos


CABECALHOS_ORGAO = (
    "Comitê Gestor do Imposto sobre Bens e Serviços – CGIBS",
    "COMITÊ GESTOR DO IMPOSTO SOBRE BENS E SERVIÇOS – CGIBS",
    "CONSELHO SUPERIOR",
)


def _preambulo(linhas: list[str], rx_titulo: re.Pattern) -> list[str]:
    """Epígrafe, ementa, preâmbulo e fórmula de promulgação como blocos próprios."""
    texto = " ".join(l.strip() for l in linhas if l.strip() and not NUMERO_PAGINA.fullmatch(l.strip()))
    for cab in CABECALHOS_ORGAO:
        texto = texto.replace(cab, " ")
    texto = re.sub(r"\s+", " ", texto).strip()
    m = rx_titulo.search(texto)
    if not m:
        return [texto]
    titulo = m.group(0).strip()
    resto = texto[m.end():].strip()
    m_ato = re.search(r"\bO COMITÊ GESTOR\b|\bO MINISTRO\b|\bO PRESIDENTE\b|\bO SECRETÁRIO\b", resto)
    ementa = resto[:m_ato.start()].strip() if m_ato else resto
    fundamentacao = resto[m_ato.start():].strip() if m_ato else ""
    blocos = [titulo]
    if ementa:
        blocos.append(ementa)
    if fundamentacao:
        m_res = re.search(r"\bRESOLVE:?\s*$", fundamentacao)
        if m_res:
            blocos.append(fundamentacao[:m_res.start()].strip())
            blocos.append("RESOLVE:")
        else:
            blocos.append(fundamentacao)
    return blocos


def corpo_para_markdown(texto: str, rx_titulo: re.Pattern = None) -> str:
    """Converte o texto de fluxo em blocos; o que antecede o `Art. 1º` é tratado como preâmbulo."""
    linhas = texto.split("\n")
    pre: list[str] = []
    if rx_titulo is not None:
        for i, l in enumerate(linhas):
            if re.match(r"^Art\.\s1[º°o]?\b", l.strip()):
                pre, linhas = linhas[:i], linhas[i:]
                break
    blocos = _preambulo(pre, rx_titulo) if pre else []
    return "\n".join(blocos + _reflow(linhas))


def anexos_para_markdown(pdf: Path, pagina_inicial: int, pagina_final: int) -> str:
    """Anexos tabulares em blocos de código por anexo, preservando as colunas originais."""
    texto = pdftotext(pdf, layout=True, primeira=pagina_inicial, ultima=pagina_final)
    texto = texto.replace("\f", "\n")
    linhas = []
    for linha in texto.split("\n"):
        if NUMERO_PAGINA.fullmatch(linha.strip()):
            continue
        linhas.append(linha.rstrip())
    # separa por anexo
    partes: list[tuple[str, list[str]]] = []
    for linha in linhas:
        if re.match(r"^\s*ANEXO\s+[IVXLC]+\b", linha) and (not partes or len(partes[-1][1]) > 3):
            partes.append((linha.strip(), []))
        elif partes:
            partes[-1][1].append(linha)
    saida = []
    for titulo, corpo in partes:
        while corpo and not corpo[0].strip():
            corpo.pop(0)
        # continuação do título do anexo em caixa alta (ex.: "DO REPORTO (ART. 186, ...)")
        while corpo and corpo[0].strip() and "  " not in corpo[0].strip() and re.sub(r"[ªº]", "", corpo[0].strip()).isupper():
            titulo = f"{titulo} {corpo.pop(0).strip()}"
        while corpo and not corpo[-1].strip():
            corpo.pop()
        compactado = []
        vazio = False
        for l in corpo:
            if not l.strip():
                if not vazio:
                    compactado.append("")
                vazio = True
            else:
                compactado.append(l)
                vazio = False
        saida.append(f"{titulo}\n\n```text\n" + "\n".join(compactado) + "\n```")
    return "\n\n".join(saida)


def localizar_pagina(pdf: Path, padrao: str, apos: int = 1) -> int:
    """Primeira página (>= apos) cujo texto contém o padrão (regex)."""
    total = numero_paginas(pdf)
    rx = re.compile(padrao, re.M)
    for p in range(apos, total + 1):
        if rx.search(pdftotext(pdf, primeira=p, ultima=p)):
            return p
    raise ValueError(f"Padrão não encontrado: {padrao}")
