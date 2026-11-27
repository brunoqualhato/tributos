#!/usr/bin/env python3
"""Recupera o conteúdo dos anexos vazios de 36 documentos do acervo a partir do Sijut/RFB.

O corpo de cada documento já é o texto compilado do ato; aqui só entra o que falta: o anexo, tirado sempre do
arquivo marcado `compilado: true` no Sijut (que já incorpora as alterações posteriores do ato), logo abaixo do
título do anexo, e uma `> **Nota editorial.**` após o H1 com os anexos recuperados e os não recuperados.
A alteração é estritamente aditiva: o script aborta se alguma linha original for removida ou alterada.

Como cada anexo é casado: pelo numeral do título do segmento no Sijut (ou do título de anexo que o antecede no ato;
o nome do arquivo só vale na falta de ambos, p.ex. `Anexo XXVIII.pdf` do idAto 123666 é o Anexo XVIII). Se o numeral
aparece em mais de um bloco do corpo, ou em mais de um arquivo do Sijut, o anexo não é alterado e fica registrado.
PDF sem camada de texto, DOC (OLE), DOCX e imagens não têm conversor reprodutível e ficam só na nota editorial.
Blocos de anexo que já têm conteúdo no corpo nunca são tocados.

Uso (a partir da raiz do repositório):
    python3 scripts/atualizar_anexos_sijut_2026.py --dry-run     # mostra o que seria feito
    python3 scripts/atualizar_anexos_sijut_2026.py               # grava os documentos e o relatório em _auditoria/
    python3 scripts/atualizar_anexos_sijut_2026.py --so 148694   # só um idAto
Rodar de novo não altera nada: documentos que já têm a nota editorial deste script são pulados.
"""
from pathlib import Path
import argparse
import collections
import difflib
import re
import sys
import unicodedata

sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co  # noqa: E402

RAIZ = co.RAIZ
MARCA_NOTA = "> **Nota editorial.** Anexos recuperados do Sijut/RFB"
TAGS_HTML = re.compile(r"<(?:script|style|div|span|p|br|table|tr|td)[\s/>]", re.I)
RELATORIO = f"_auditoria/auditoria_anexos_sijut_{co.DATA_CONSULTA}.md"
# Frase extra da nota editorial por idAto. IN RFB 2.305/2025: o arquivo compilado do Anexo Único é a redação dada pela IN 2.307/2026.
NOTAS_EXTRA = {
    148694: "O Anexo Único está na redação dada pela IN RFB nº 2307/2026 (`ato-149398-2307-2026.md`), que o substituiu.",
}

# (caminho, idAto, numerais dos anexos vazios segundo o plano). Ordem: vigentes por idAto, depois os revogados.
DOCUMENTOS = [
    ('reguladores/rfb/outros-atos/2011/ato-37116-95-2011.md', 37116, ('UNICO',)),
    ('reguladores/rfb/instrucoes-normativas/2012/ato-37200-1234-2012.md', 37200, ('I', 'II', 'III', 'IV', 'V')),
    ('reguladores/rfb/instrucoes-normativas/2013/ato-48865-1432-2013.md', 48865, ('I', 'II', 'III', 'IV', 'V')),
    ('reguladores/rfb/instrucoes-normativas/2016/ato-79115-1677-2016.md', 79115, ('UNICO',)),
    ('reguladores/rfb/instrucoes-normativas/2017/ato-81268-1700-2017.md', 81268, ('I', 'II', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI')),
    ('reguladores/rfb/outros-atos/2018/ato-97787-2131-2018.md', 97787, ('I', 'II')),
    ('reguladores/rfb/instrucoes-normativas/2020/ato-114672-2002-2020.md', 114672, ('I', 'II')),
    ('reguladores/rfb/instrucoes-normativas/2021/ato-122005-2053-2021.md', 122005, ('III', 'IV', 'V')),
    ('reguladores/rfb/instrucoes-normativas/2022/ato-122718-2063-2022.md', 122718, ('I', 'II', 'III', 'IV', 'V')),
    ('reguladores/rfb/outros-atos/2022/ato-123666-167-2022.md', 123666, ('I', 'UNICO', 'II')),
    ('reguladores/rfb/outros-atos/2022/ato-125063-200-2022.md', 125063, ('UNICO',)),
    ('reguladores/rfb/instrucoes-normativas/2022/ato-125102-2097-2022.md', 125102, ('I', 'II')),
    ('reguladores/rfb/outros-atos/2022/ato-125873-7913-2022.md', 125873, ('I',)),
    ('reguladores/rfb/instrucoes-normativas/2022/ato-126687-2110-2022.md', 126687, ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')),
    ('reguladores/rfb/instrucoes-normativas/2022/ato-127411-2117-2022.md', 127411, ('I', 'II')),
    ('reguladores/rfb/instrucoes-normativas/2022/ato-127567-2119-2022.md', 127567, ('II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI')),
    ('reguladores/rfb/instrucoes-normativas/2022/ato-127905-2121-2022.md', 127905, ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX')),
    ('reguladores/rfb/outros-atos/2023/ato-129873-309-2023.md', 129873, ('UNICO',)),
    ('reguladores/rfb/outros-atos/2023/ato-131461-328-2023.md', 131461, ('UNICO',)),
    ('reguladores/rfb/outros-atos/2023/ato-132287-130-2023.md', 132287, ('I', 'II')),
    ('reguladores/rfb/outros-atos/2024/ato-138114-187-2024.md', 138114, ('I', 'II')),
    ('reguladores/rfb/instrucoes-normativas/2024/ato-138735-2198-2024.md', 138735, ('UNICO',)),
    ('reguladores/rfb/instrucoes-normativas/2024/ato-142276-2241-2024.md', 142276, ('UNICO',)),
    ('reguladores/rfb/instrucoes-normativas/2025/ato-144058-2264-2025.md', 144058, ('I', 'II', 'III', 'IV')),
    ('reguladores/rfb/instrucoes-normativas/2025/ato-148316-2294-2025.md', 148316, ('UNICO',)),
    ('reguladores/rfb/instrucoes-normativas/2025/ato-148383-2299-2025.md', 148383, ('I', 'II')),
    ('reguladores/rfb/instrucoes-normativas/2025/ato-148694-2305-2025.md', 148694, ('UNICO',)),
    ('reguladores/rfb/instrucoes-normativas/2015/ato-69971-1597-2015.md', 69971, ('I', 'II')),
    ('reguladores/rfb/outros-atos/2017/ato-89021-6447-2017.md', 89021, ('I', 'II')),
    ('reguladores/rfb/outros-atos/2022/ato-124717-81-2022.md', 124717, ('UNICO',)),
    ('reguladores/rfb/outros-atos/2022/ato-126900-242-2022.md', 126900, ('I',)),
    ('reguladores/rfb/outros-atos/2022/ato-127965-66-2022.md', 127965, ('UNICO',)),
    ('reguladores/rfb/outros-atos/2023/ato-130676-319-2023.md', 130676, ('I', 'I-A', 'II', 'VI')),
    ('reguladores/rfb/outros-atos/2023/ato-132670-133-2023.md', 132670, ('I', 'II', 'III')),
    ('reguladores/rfb/outros-atos/2023/ato-134080-368-2023.md', 134080, ('UNICO',)),
    ('reguladores/rfb/outros-atos/2024/ato-141278-477-2024.md', 141278, ('II',)),
]

# Documentos com anexo vazio que ficam fora desta rodada (caminho, idAto, anexos, motivo).
NAO_TRATADOS = [
    ('reguladores/rfb/instrucoes-normativas/2011/ato-36692-1208-2011.md', 36692, 'UNICO (1 DOC (OLE))', 'só DOC (OLE), sem conversor reprodutível; revogado.'),
    ('reguladores/rfb/instrucoes-normativas/2011/ato-36794-1211-2011.md', 36794, 'I, II, III, IV, V, VI, VII, VIII, IX (9 DOC (OLE))', 'só DOC (OLE), sem conversor reprodutível; revogado.'),
    ('reguladores/rfb/instrucoes-normativas/2011/ato-37095-1224-2011.md', 37095, 'UNICO (1 DOC (OLE))', 'só DOC (OLE), sem conversor reprodutível; revogado.'),
    ('reguladores/rfb/instrucoes-normativas/2011/ato-37097-1226-2011.md', 37097, 'I, II, III (3 DOC (OLE))', 'só DOC (OLE), sem conversor reprodutível; revogado.'),
    ('reguladores/rfb/instrucoes-normativas/2011/ato-37127-1229-2011.md', 37127, 'UNICO (1 DOC (OLE))', 'só DOC (OLE), sem conversor reprodutível; revogado.'),
    ('reguladores/rfb/instrucoes-normativas/2012/ato-39257-1312-2012.md', 39257, 'I, II, III (3 DOC (OLE))', 'só DOC (OLE), sem conversor reprodutível; revogado.'),
    ('reguladores/rfb/outros-atos/2010/ato-30584-2466-2010.md', 30584, 'III, II, IV, V, VI (6 DOC (OLE))', 'só DOC (OLE), sem conversor reprodutível; revogado.'),
    ('reguladores/rfb/outros-atos/2022/ato-125876-1-2022.md', 125876, 'I, II (2 DOCX)', 'só DOCX, sem conversor no repositório.'),
    ('reguladores/rfb/outros-atos/2022/ato-125877-2-2022.md', 125877, 'I, II (2 DOCX)', 'só DOCX, sem conversor no repositório.'),
    ('reguladores/rfb/instrucoes-normativas/2022/ato-123983-2081-2022.md', 123983, 'UNICO (1 PDF sem texto)', 'ambígua: IN RFB 2.081/2022: anexo único em PDF sem camada de texto (formulário); exigiria OCR.'),
    ('reguladores/rfb/instrucoes-normativas/2022/ato-125241-2099-2022.md', 125241, 'UNICO (1 PDF sem texto)', 'ambígua: IN RFB 2.099/2022: PDF sem camada de texto; exigiria OCR.'),
    ('reguladores/rfb/instrucoes-normativas/2023/ato-135339-2166-2023.md', 135339, 'UNICO (1 JPG inline)', 'ambígua: IN RFB 2.166/2023: o único anexo é `Imagem.jpg`; exigiria OCR ou descrição manual.'),
    ('reguladores/rfb/outros-atos/2022/ato-122738-1-2022.md', 122738, 'I, II, III, IV (4 PDF sem texto)', 'ambígua: Portaria IRF/SLS 1/2022 (revogada): 4 PDFs sem camada de texto.'),
    ('reguladores/rfb/outros-atos/2022/ato-126230-220-2022.md', 126230, 'I, II ()', 'ambígua: Portaria RFB 220/2022: o Sijut não traz arquivo compilado próprio; os anexos remetem aos da Portaria RFB 167/2022.'),
    ('reguladores/rfb/outros-atos/2025/ato-148683-632-2025.md', 148683, 'I, II (2 PDF sem texto)', 'ambígua: Portaria RFB 632/2025: 2 PDFs sem camada de texto.'),
]

# Classe B: tabelas HTML ausentes e anexos em arquivo sem título detectável no corpo. Sem âncora para inserir
# sem conferência manual do corpo (caminho, idAto, arquivos).
CLASSE_B_HTML = [
    ('reguladores/rfb/instrucoes-normativas/2022/ato-124633-2090-2022.md', 124633, 'Anexo da Nota Explicativa 7.1.jpg, Tabela 1.html, Tabela 2.html …'),
    ('reguladores/rfb/instrucoes-normativas/2022/ato-126228-2104-2022.md', 126228, 'A7.html'),
    ('reguladores/rfb/instrucoes-normativas/2024/ato-140884-2228-2024.md', 140884, 'I2.jpg, I6.jpg'),
    ('reguladores/rfb/outros-atos/2015/ato-70675-50-2015.md', 70675, 'Anexo .html'),
    ('reguladores/rfb/outros-atos/2017/ato-89069-4-2017.md', 89069, 'Anexo .html, Anexo .html'),
    ('reguladores/rfb/outros-atos/2021/ato-122443-37-2021.md', 122443, 'tabela.html'),
    ('reguladores/rfb/outros-atos/2022/ato-123828-9-2022.md', 123828, 'Tabela.html, Tabela.html'),
    ('reguladores/rfb/outros-atos/2022/ato-127946-6-2022.md', 127946, 'Anexo I.html, Anexo II.html'),
    ('reguladores/rfb/outros-atos/2022/ato-128020-30-2022.md', 128020, 'Tabela.htm'),
    ('reguladores/rfb/outros-atos/2023/ato-131987-138-2023.md', 131987, 'Tabela.htm'),
    ('reguladores/rfb/outros-atos/2023/ato-132331-168-2023.md', 132331, 'Tabela.htm'),
    ('reguladores/rfb/outros-atos/2023/ato-134654-656-2023.md', 134654, 'Tabela.htm'),
    ('reguladores/rfb/outros-atos/2023/ato-134785-688-2023.md', 134785, 'Tabela.htm'),
    ('reguladores/rfb/outros-atos/2023/ato-134809-28-2023.md', 134809, 'Tabela.htm'),
    ('reguladores/rfb/outros-atos/2023/ato-134817-693-2023.md', 134817, 'Tabela.htm'),
    ('reguladores/rfb/outros-atos/2023/ato-134861-699-2023.md', 134861, 'Tabela.htm'),
    ('reguladores/rfb/outros-atos/2023/ato-135046-734-2023.md', 135046, 'tab1.html'),
    ('reguladores/rfb/outros-atos/2023/ato-135147-46-2023.md', 135147, 'Tabela.htm, Tabela.htm'),
    ('reguladores/rfb/outros-atos/2023/ato-135201-47-2023.md', 135201, 'Tabela.htm, Tabela.htm'),
    ('reguladores/rfb/outros-atos/2023/ato-135335-48-2023.md', 135335, 'Tabela.htm, Tabela.htm'),
    ('reguladores/rfb/outros-atos/2024/ato-137967-6-2024.md', 137967, '140418467484464.html'),
]
CLASSE_B_ARQUIVO = [
    ('federal/leis-complementares/simples/resolucao-cgsn-140-2018-simples-nacional.md', 92278, 'Anexo I  .pdf, Anexo II .pdf, Anexo III .pdf, Anexo IV .pdf, Anexo V.pdf'),
    ('federal/leis-ordinarias/offshores/in-rfb-2180-2024-offshores-trusts.md', 136675, 'SC Cosit nº 27-2024.pdf'),
    ('reguladores/rfb/instrucoes-normativas/2004/ato-15365-459-2004.md', 15365, 'Anexo I.doc'),
    ('reguladores/rfb/instrucoes-normativas/2016/ato-79445-1682-2016.md', 79445, 'Anexo I.pdf, Anexo II.pdf'),
    ('reguladores/rfb/instrucoes-normativas/2021/ato-122077-2055-2021.md', 122077, 'Anexo II.pdf, Anexo III.pdf, Anexo IV.pdf, Anexo V.pdf'),
    ('reguladores/rfb/instrucoes-normativas/2023/ato-135577-2169-2023.md', 135577, 'Anexo Único.pdf'),
    ('reguladores/rfb/instrucoes-normativas/2024/ato-135610-2171-2024.md', 135610, 'Anexo Único.pdf'),
    ('reguladores/rfb/instrucoes-normativas/2024/ato-140316-2216-2024.md', 140316, 'Anexo Único.pdf'),
    ('reguladores/rfb/instrucoes-normativas/2025/ato-148173-2295-2025.md', 148173, 'Anexo I.pdf, Anexo II.pdf, Anexo III.pdf, Anexo IV.htm'),
    ('reguladores/rfb/instrucoes-normativas/2026/ato-151846-2328-2026.md', 151846, 'Anexo II.pdf, Anexo III.pdf'),
    ('reguladores/rfb/outros-atos/2010/ato-5446-96-2010.md', 5446, 'AgeJan11-2010.doc'),
    ('reguladores/rfb/outros-atos/2019/ato-105880-2246-2019.md', 105880, 'Anexo I.pdf, Anexo II.pdf, Anexo III.pdf'),
    ('reguladores/rfb/outros-atos/2022/ato-125066-72-2022.md', 125066, 'Anexo.pdf'),
    ('reguladores/rfb/outros-atos/2022/ato-126671-95-2022.md', 126671, 'Anexo Único.pdf'),
    ('reguladores/rfb/outros-atos/2022/ato-126901-85-2022.md', 126901, 'Anexos.pdf'),
    ('reguladores/rfb/outros-atos/2022/ato-128016-277-2022.md', 128016, '(sem nome), (sem nome), Anexo I (íntegra).docx, Anexo II.docx'),
    ('reguladores/rfb/outros-atos/2023/ato-133034-346-2023.md', 133034, 'Anexo Único.pdf'),
    ('reguladores/rfb/outros-atos/2026/ato-152832-190-2026.md', 152832, 'Anexo Único.pdf'),
    ('reguladores/rfb/outros-atos/2026/ato-154694-196-2026.md', 154694, 'Anexo I.pdf, Anexo II.pdf, Anexo III.pdf, Anexo IV.pdf, Anexo V.pdf'),
    ('reguladores/rfb/rat-fap-terceiros/portaria-conjunta-rfb-inss-1-2021-ntep.md', 112340, 'ANEXO IN SRF  Nº 14 de 02.12.1'),
]


# ----------------------------------------------------------------------------------------------------------------
# Detecção dos blocos de título de anexo (lógica de detect_anexos.py, agora com a posição de cada linha)
# ----------------------------------------------------------------------------------------------------------------
def separar(texto: str) -> tuple[list[str], int]:
    """Linhas do arquivo e índice da primeira linha depois do frontmatter."""
    linhas = texto.split("\n")
    if linhas[0] != "---":
        raise RuntimeError("frontmatter ausente")
    return linhas, linhas.index("---", 1) + 1


def classificar(bloco: dict) -> str:
    """'vazio', 'so_subtitulo' (até 3 linhas e menos de 250 caracteres, sem tabela nem cerca de código) ou 'ok'."""
    c = [l for _, l in bloco["cont"]]
    if not c:
        return "vazio"
    if any(l.lstrip().startswith(("|", "```")) for l in c):
        return "ok"
    if len(" ".join(c)) < 250 and len(c) <= 3:
        return "so_subtitulo"
    return "ok"


def blocos_de_anexo(linhas: list[str], inicio: int) -> list[dict]:
    """Blocos [título(s) + conteúdo até o próximo título], com títulos consecutivos do mesmo numeral mesclados.
    `fim` é o índice da última linha não vazia do bloco (onde entra o anexo)."""
    nb = [(i, l) for i, l in enumerate(linhas) if i >= inicio and l.strip()]
    ts = [co.numeral_anexo(l) for _, l in nb]
    brutos, i = [], 0
    while i < len(nb):
        if ts[i] is None:
            i += 1
            continue
        num, j = ts[i], i
        titulos = [nb[i]]
        while j + 1 < len(nb) and ts[j + 1] == num:
            j += 1
            titulos.append(nb[j])
        k = j + 1
        while k < len(nb) and ts[k] is None:
            k += 1
        brutos.append({"num": num, "titulos": titulos, "cont": nb[j + 1:k]})
        i = k
    blocos = []
    for b in brutos:
        if blocos and blocos[-1]["num"] == b["num"]:
            blocos[-1]["titulos"] += b["titulos"]
            blocos[-1]["cont"] += b["cont"]
        else:
            blocos.append({"num": b["num"], "titulos": list(b["titulos"]), "cont": list(b["cont"])})
    for b in blocos:
        b["classe"] = classificar(b)
        ultimo_cont = b["cont"][-1][0] if b["cont"] else -1
        b["fim"] = max(ultimo_cont, b["titulos"][-1][0])
    return blocos


# ----------------------------------------------------------------------------------------------------------------
# Planejamento: casa cada bloco vazio com o anexo compilado do Sijut
# ----------------------------------------------------------------------------------------------------------------
def planejar(caminho: str, id_ato: int, esperados: tuple) -> dict:
    texto = (RAIZ / caminho).read_bytes().decode("utf-8")  # sem tradução de quebras de linha: há \r solto em um documento
    plano = {"caminho": caminho, "id_ato": id_ato, "esperados": esperados, "texto": texto,
             "ja_processado": MARCA_NOTA in texto, "recuperados": [], "nao_recuperados": [], "com_conteudo": [],
             "so_sijut": [], "vazios_detectados": []}
    if plano["ja_processado"]:
        return plano
    linhas, inicio = separar(texto)
    plano["linhas"], plano["inicio"] = linhas, inicio
    blocos = blocos_de_anexo(linhas, inicio)
    plano["ordem_corpo"] = [b["num"] for b in blocos]
    vazios = [b for b in blocos if b["classe"] != "ok"]
    plano["vazios_detectados"] = [b["num"] for b in vazios]
    por_numeral = collections.Counter(b["num"] for b in blocos)
    segmentos = co.anexos_sijut(id_ato, numerais=set())
    plano["ordem_sijut"] = [s["numeral"] for s in segmentos if s["numeral"]]
    candidatos = collections.defaultdict(list)
    for s in segmentos:
        if s["numeral"]:
            candidatos[s["numeral"]].append(s)
    escolhidos = []
    for b in vazios:
        n = b["num"]
        if por_numeral[n] > 1:
            plano["nao_recuperados"].append((n, f"o título do Anexo {rot(n)} aparece em {por_numeral[n]} blocos do corpo e não há como saber em qual entra o anexo"))
        elif not candidatos[n]:
            motivo = "o Sijut não traz arquivo compilado com esse título" if segmentos else "o Sijut não traz arquivo compilado para os anexos"
            plano["nao_recuperados"].append((n, motivo))
        elif len(candidatos[n]) > 1:
            plano["nao_recuperados"].append((n, f"o Sijut traz {len(candidatos[n])} arquivos compilados com o título do Anexo {rot(n)}"))
        else:
            escolhidos.append((b, candidatos[n][0]))
    if escolhidos:
        convertidos = {s["id_arquivo"]: s for s in co.anexos_sijut(id_ato, numerais={s["numeral"] for _, s in escolhidos})}
        for b, s in escolhidos:
            c = convertidos[s["id_arquivo"]]
            if c["omissao"]:
                detalhe = ("PDF sem camada de texto (formulário ou imagem digitalizada)" if c["omissao"] == "PDF sem camada de texto"
                           else f"arquivo {c['tipo'].upper()}, formato sem conversor no repositório")
                plano["nao_recuperados"].append((b["num"], detalhe))
            elif not c["md"].strip():
                plano["nao_recuperados"].append((b["num"], "o arquivo compilado não tem conteúdo convertível"))
            else:
                plano["recuperados"].append({"bloco": b, "seg": c})
    nums_corpo = {b["num"] for b in blocos}
    plano["com_conteudo"] = [b["num"] for b in blocos if b["classe"] == "ok" and candidatos.get(b["num"])]
    plano["so_sijut"] = [s["numeral"] for s in segmentos if s["numeral"] and s["numeral"] not in nums_corpo]
    return plano


# ----------------------------------------------------------------------------------------------------------------
# Nota editorial
# ----------------------------------------------------------------------------------------------------------------
def rot(numeral: str) -> str:
    return "Único" if numeral == "UNICO" else numeral


def juntar(partes: list[str]) -> str:
    return partes[0] if len(partes) == 1 else ", ".join(partes[:-1]) + " e " + partes[-1]


def rotulo_anexos(numerais: list[str], referencia: list[str]) -> str:
    """'Anexo I', 'Anexos I e II', 'Anexos III a XXV' (sequência de 3 ou mais na ordem de referência)."""
    pos = {n: i for i, n in enumerate(referencia)}
    ns = sorted(set(numerais), key=lambda n: pos.get(n, 10 ** 6))
    partes, i = [], 0
    while i < len(ns):
        j = i
        while j + 1 < len(ns) and pos.get(ns[j + 1], -9) == pos.get(ns[j], -99) + 1:
            j += 1
        sufixo = any("-" in n for n in ns[i:j + 1])  # 'I-A' não entra em 'I a II'
        partes += [f"{rot(ns[i])} a {rot(ns[j])}"] if j - i >= 2 and not sufixo else [rot(n) for n in ns[i:j + 1]]
        i = j + 1
    return ("Anexo " if len(ns) == 1 else "Anexos ") + juntar(partes)


def referencia(plano: dict) -> list[str]:
    ref = []
    for n in plano["ordem_corpo"] + plano["ordem_sijut"]:
        if n not in ref:
            ref.append(n)
    return ref


def nao_recuperados_agrupados(plano: dict) -> list[str]:
    """['Anexos I a III e V: motivo', ...] com os anexos vazios que continuam vazios, agrupados por motivo."""
    ref = referencia(plano)
    por_motivo = collections.OrderedDict()
    for n, motivo in plano["nao_recuperados"]:
        por_motivo.setdefault(motivo, []).append(n)
    return [f"{rotulo_anexos(ns, ref)}: {motivo}" for motivo, ns in por_motivo.items()]


def nota_editorial(plano: dict) -> str:
    ref = referencia(plano)
    rec = plano["recuperados"]
    if len(rec) <= 4:
        lista = juntar([f"Anexo {rot(r['bloco']['num'])} (`{r['seg']['nome']}`)" for r in rec])
    else:
        lista = rotulo_anexos([r["bloco"]["num"] for r in rec], ref) + f" ({len(rec)} arquivos)"
    frases = [f"Anexos recuperados do Sijut/RFB em {co.DATA_CONSULTA_BR}, sempre do arquivo marcado como compilado "
              f"(que já incorpora as alterações posteriores do ato): {lista}."]
    tipos = {r["seg"]["tipo"] for r in rec}
    if "pdf" in tipos:
        frases.append("Os PDFs foram extraídos com `pdftotext -layout` e ficam em blocos de texto que mantêm as colunas, "
                      "sem a formatação visual do original.")
    if "html" in tipos:
        frases.append("Os anexos em HTML foram convertidos para Markdown, com as tabelas.")
    if any(co.numeral_anexo(r["seg"]["nome"], estrito=False) not in (None, r["bloco"]["num"]) for r in rec):
        frases.append("O nome de alguns arquivos no Sijut não coincide com o numeral do anexo; vale o título do segmento.")
    if plano["nao_recuperados"]:
        frases.append("Não recuperados: " + "; ".join(nao_recuperados_agrupados(plano)) + ".")
    if plano["so_sijut"]:
        frases.append(f"O Sijut traz ainda {rotulo_anexos(plano['so_sijut'], ref)}, sem título correspondente no corpo; "
                      "não foram incorporados.")
    if plano["id_ato"] in NOTAS_EXTRA:
        frases.append(NOTAS_EXTRA[plano["id_ato"]])
    frases.append("O restante do documento não foi alterado; cada anexo foi acrescentado logo abaixo do respectivo título.")
    return MARCA_NOTA[:len("> **Nota editorial.** ")] + " ".join(frases)


# ----------------------------------------------------------------------------------------------------------------
# Aplicação e verificação
# ----------------------------------------------------------------------------------------------------------------
def aplicar(plano: dict) -> str:
    linhas = list(plano["linhas"])
    for r in sorted(plano["recuperados"], key=lambda r: r["bloco"]["fim"], reverse=True):
        fim = r["bloco"]["fim"]
        novo = ["", *r["seg"]["md"].strip("\n").split("\n")]
        if fim + 1 < len(linhas) and linhas[fim + 1].strip():
            novo.append("")
        linhas[fim + 1:fim + 1] = novo
    h1 = next(i for i in range(plano["inicio"], len(linhas)) if linhas[i].startswith("# "))
    nota = ["", nota_editorial(plano)]
    if h1 + 1 < len(linhas) and linhas[h1 + 1].strip():
        nota.append("")
    linhas[h1 + 1:h1 + 1] = nota
    return "\n".join(linhas)


def verificar_aditivo(plano: dict, novo: str) -> None:
    """Aborta se alguma linha original foi removida/alterada ou se entrou tag HTML que o auditor rejeita."""
    antes, depois = plano["texto"].split("\n"), novo.split("\n")
    ops = difflib.SequenceMatcher(None, antes, depois, autojunk=False).get_opcodes()
    ruins = [(t, i1, i2) for t, i1, i2, _, _ in ops if t in ("delete", "replace")]
    if ruins:
        raise SystemExit(f"ERRO {plano['caminho']}: linhas originais removidas ou alteradas: {ruins[:3]}")
    inseridas = "\n".join("\n".join(depois[j1:j2]) for t, _, _, j1, j2 in ops if t == "insert")
    achadas = TAGS_HTML.findall(inseridas)
    if achadas:
        raise SystemExit(f"ERRO {plano['caminho']}: {len(achadas)} tag(s) HTML no conteúdo inserido: {achadas[:3]}")


# ----------------------------------------------------------------------------------------------------------------
# Mensagem de commit sugerida
# ----------------------------------------------------------------------------------------------------------------
def sem_acentos(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")


def nome_curto(titulo: str) -> str:
    m = re.match(r"^(?P<tipo>.+?)\s+n[ºo°]\s*(?P<num>[\d.]+)\s*(?:/\s*\w+)?\s*,\s*de\s+.*?(?P<ano>\d{4})\s*$", titulo)
    if not m:
        return sem_acentos(titulo)
    tipo = m["tipo"]
    for longo, curto in (("Instrução Normativa", "IN"), ("Ato Declaratório Executivo", "ADE"),
                         ("Ato Declaratório Interpretativo", "ADI"), (" / ", "/")):
        tipo = tipo.replace(longo, curto)
    numero = f"{int(m['num'].replace('.', '')):,}".replace(",", ".")
    return sem_acentos(f"{tipo} {numero}/{m['ano']}")


def mensagem_commit(plano: dict) -> str:
    titulo = re.search(r'^titulo: "(.*)"$', plano["texto"], re.M).group(1)
    curto = nome_curto(titulo)
    artigo = "do" if curto.startswith(("ADE", "ADI")) else "da"
    return f"fix(anexos): recupera anexos {artigo} {curto} (Sijut {plano['id_ato']})"


# ----------------------------------------------------------------------------------------------------------------
# Relatório
# ----------------------------------------------------------------------------------------------------------------
def escapar(s: str) -> str:
    return s.replace("|", "\\|")


def relatorio(planos: list[dict]) -> str:
    alterados = [p for p in planos if p["recuperados"]]
    n_rec = sum(len(p["recuperados"]) for p in alterados)
    n_nao = sum(len({n for n, _ in p["nao_recuperados"]}) for p in planos)
    L = [f"# Auditoria dos anexos recuperados do Sijut/RFB ({co.DATA_CONSULTA_BR})", "",
         f"Consulta ao Sijut em {co.DATA_CONSULTA_BR}, por `python3 scripts/atualizar_anexos_sijut_2026.py`. "
         "Cada anexo vem do arquivo marcado `compilado: true` no segmento de anexo do ato (o corpo do acervo já é o texto "
         "compilado, e o anexo compilado incorpora as alterações posteriores). A alteração é aditiva: o anexo entra logo "
         "abaixo do título e uma `> **Nota editorial.**` após o H1 lista o que foi recuperado e o que não foi; "
         "nenhuma linha original foi removida.", "",
         "## Resumo", "",
         f"- Documentos alterados: {len(alterados)} de {len(planos)}.",
         f"- Anexos recuperados: {n_rec}.",
         f"- Anexos vazios que continuam vazios: {n_nao} (motivo na tabela abaixo).",
         f"- Documentos fora desta rodada: {len(NAO_TRATADOS)} (DOC, DOCX, imagem ou PDF sem texto).",
         f"- Pendências de conferência manual (classe B): {len(CLASSE_B_HTML) + len(CLASSE_B_ARQUIVO)} atos.", "",
         "Regras de casamento: o numeral do título do segmento no Sijut (ou do título de anexo que o antecede no ato) é "
         "comparado ao numeral do bloco vazio no corpo. Numeral repetido em mais de um bloco do corpo, ou em mais de um "
         "arquivo do Sijut, não é alterado. PDF sem camada de texto (menos de 200 caracteres úteis), DOC (OLE), DOCX e "
         "imagem não têm conversor reprodutível no repositório. Anexos que já têm conteúdo no corpo não são tocados.", "",
         "## Documentos alterados", "",
         "| # | Documento | idAto | Anexos recuperados | Anexos que continuam vazios (motivo) |", "|---|---|---|---|---|"]
    for k, p in enumerate(planos, 1):
        if not p["recuperados"]:
            continue
        ref = referencia(p)
        rec = rotulo_anexos([r["bloco"]["num"] for r in p["recuperados"]], ref) + " (" + ", ".join(
            sorted({r["seg"]["tipo"].upper() for r in p["recuperados"]})) + ")"
        nao = "; ".join(nao_recuperados_agrupados(p)) or "nenhum"
        L.append(f"| {k} | `{p['caminho']}` | {p['id_ato']} | {rec} | {escapar(nao)} |")
    sem = [p for p in planos if not p["recuperados"]]
    if sem:
        L += ["", "## Documentos da lista sem alteração", "", "| Documento | idAto | Motivo |", "|---|---|---|"]
        for p in sem:
            motivo = "já processado (nota editorial presente)" if p["ja_processado"] else "; ".join(
                f"Anexo {rot(n)}: {m}" for n, m in p["nao_recuperados"]) or "nenhum anexo vazio detectado"
            L.append(f"| `{p['caminho']}` | {p['id_ato']} | {escapar(motivo)} |")
    sem_titulo = [p for p in planos if p["so_sijut"]]
    if sem_titulo:
        L += ["", "## Anexos do Sijut sem título correspondente no corpo (não incorporados)", "",
              "| Documento | idAto | Anexos |", "|---|---|---|"]
        for p in sem_titulo:
            L.append(f"| `{p['caminho']}` | {p['id_ato']} | {rotulo_anexos(p['so_sijut'], referencia(p))} |")
    parciais = [(p, p["com_conteudo"]) for p in planos if p["com_conteudo"]]
    if parciais:
        L += ["", "## Anexos com conteúdo no corpo e arquivo compilado no Sijut (não alterados)", "",
              "Só relato: o corpo já tem algum conteúdo sob o título, então o script não toca. A cobertura pode ser parcial "
              "(p.ex. o `tabela.html` do Anexo III da IN RFB 1.700/2017 aparece em cerca de 13% no corpo).", "",
              "| Documento | idAto | Anexos |", "|---|---|---|"]
        for p, ns in parciais:
            L.append(f"| `{p['caminho']}` | {p['id_ato']} | {rotulo_anexos(ns, referencia(p))} |")
    L += ["", "## Documentos não tratados nesta rodada", "",
          "| Documento | idAto | Anexos | Motivo |", "|---|---|---|---|"]
    for caminho, id_ato, anexos, motivo in NAO_TRATADOS:
        L.append(f"| `{caminho}` | {id_ato} | {escapar(anexos)} | {escapar(motivo)} |")
    L += ["", "## Pendências (classe B, conferência manual do corpo)", "",
          "Sem título de anexo detectável no corpo para ancorar o conteúdo; ficam fora desta rodada.", "",
          f"### Tabelas HTML do Sijut ausentes no corpo ({len(CLASSE_B_HTML)} atos, quase todos individuais)", "",
          "| Documento | idAto | Arquivos |", "|---|---|---|"]
    for caminho, id_ato, arquivos in CLASSE_B_HTML:
        L.append(f"| `{caminho}` | {id_ato} | {escapar(arquivos)} |")
    L += ["", f"### Anexos em arquivo (PDF, DOC, DOCX ou imagem) sem título correspondente no corpo ({len(CLASSE_B_ARQUIVO)} atos)", "",
          "| Documento | idAto | Arquivos |", "|---|---|---|"]
    for caminho, id_ato, arquivos in CLASSE_B_ARQUIVO:
        L.append(f"| `{caminho}` | {id_ato} | {escapar(arquivos)} |")
    return "\n".join(L) + "\n"


# ----------------------------------------------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true", help="não grava nada; lista o que seria feito")
    ap.add_argument("--so", type=int, metavar="ID_ATO", help="processa só este idAto")
    args = ap.parse_args()
    selecionados = [d for d in DOCUMENTOS if args.so in (None, d[1])]
    if not selecionados:
        raise SystemExit(f"idAto {args.so} não está na lista de documentos")
    planos, divergencias = [], []
    for k, (caminho, id_ato, esperados) in enumerate(selecionados, 1):
        plano = planejar(caminho, id_ato, esperados)
        planos.append(plano)
        nome = Path(caminho).name
        if plano["ja_processado"]:
            print(f"[{k:02d}] {nome}: já processado (nota editorial presente)")
            continue
        if set(plano["vazios_detectados"]) != set(esperados):
            divergencias.append((nome, plano["vazios_detectados"], esperados))
        rec = [r["bloco"]["num"] for r in plano["recuperados"]]
        print(f"[{k:02d}] {nome} ({id_ato}): recupera {rec or '-'}; não recupera "
              f"{[(n, m[:48]) for n, m in plano['nao_recuperados']] or '-'}")
        if plano["recuperados"] and not args.dry_run:
            novo = aplicar(plano)
            verificar_aditivo(plano, novo)
            co.gravar(caminho, novo)
            plano["commit"] = mensagem_commit(plano)
    for nome, achados, esperados in divergencias:
        print(f"DIVERGE DO PLANO {nome}: vazios detectados {achados} / plano {list(esperados)}")
    if args.dry_run:
        print(f"\nDry-run: {sum(1 for p in planos if p['recuperados'])} documentos seriam alterados, "
              f"{sum(len(p['recuperados']) for p in planos)} anexos recuperados, "
              f"{sum(1 for p in planos if p['ja_processado'])} já processados.")
        return 0
    alterados = [p for p in planos if p.get("commit")]
    if alterados and args.so is None:
        co.gravar(RELATORIO, relatorio(planos))
        print(f"\nRelatório: {RELATORIO}")
    print(f"\n{len(alterados)} documentos alterados." + (" Mensagens de commit sugeridas (arquivo<TAB>mensagem):" if alterados else ""))
    for p in alterados:
        print(f"{p['caminho']}\t{p['commit']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
