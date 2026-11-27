"""Utilitários de coleta de atos oficiais para os geradores de lotes do acervo.

Fontes suportadas:
- normas.leg.br (LexML/Senado): leis, leis complementares e decretos federais (texto original);
- Sijut/Receita Federal: atos da RFB e atos conjuntos RFB/CGIBS (visão compilada);
- PDFs oficiais do Comitê Gestor do IBS (cgibs.gov.br), via `pdf_regulamento`.

Todos os geradores montam o documento com o frontmatter canônico de `comum.gerar_frontmatter`
e preservam a norma sem reescrita, acrescentando apenas uma nota editorial rastreável.
"""
from pathlib import Path
import datetime as dt
import re
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from agente_api import AgenteAPI  # noqa: E402
from comum import Rede, gerar_frontmatter, salvar_atomico, yaml_str  # noqa: E402
from html2md import converter_html_para_md  # noqa: E402

DATA_CONSULTA = dt.date.today().isoformat()
DATA_CONSULTA_BR = dt.date.today().strftime("%d/%m/%Y")
CACHE_PDF = RAIZ / "_fonte" / "pdf"

_api = None


def api() -> AgenteAPI:
    global _api
    if _api is None:
        _api = AgenteAPI(rps=1.0)
        _api.rede.timeout = 120
    return _api


def lexml_para_md(urn: str) -> str:
    """Texto original de uma norma federal em normas.leg.br convertido para Markdown."""
    r = api().baixar_norma_lexml(urn)
    if not r["html"].strip():
        raise RuntimeError(f"normas.leg.br não retornou texto para {urn}")
    return limpar_corpo(converter_html_para_md(r["html"]))


def sijut_para_md(id_ato: int) -> tuple[str, dict]:
    """Corpo compilado (texto vigente) de um ato do Sijut convertido para Markdown."""
    dados = api().baixar_corpo_ato_rfb(id_ato)
    segmentos = [s for s in dados.get("outrosSegmentos", []) if s.get("compilado")]
    segmentos.sort(key=lambda s: s.get("ordemSegmentoAto", 0))
    html = "\n\n".join(s.get("textoIntegra") or "" for s in segmentos)
    if not html.strip():
        raise RuntimeError(f"Sijut não retornou texto compilado para o ato {id_ato}")
    return limpar_corpo(converter_html_para_md(html)), dados


def baixar_pdf(url: str, nome: str) -> Path:
    """Baixa um PDF oficial para o cache local (`_fonte/pdf`, ignorado pelo git)."""
    destino = CACHE_PDF / nome
    if destino.exists() and destino.stat().st_size > 0:
        return destino
    rede = Rede(rps=1.0, timeout=180)
    status, bruto, _ = rede.get(url)
    if status != 200 or not bruto.startswith(b"%PDF"):
        raise RuntimeError(f"Falha ao baixar PDF oficial ({status}): {url}")
    salvar_atomico(destino, bruto)
    return destino


def limpar_corpo(md: str) -> str:
    """Normalizações mínimas que não alteram o texto normativo."""
    md = md.replace("\u00a0", " ").replace("&nbsp;", " ")
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def montar_documento(meta: dict, corpo: str, notas: list[str] = None, extras: dict = None) -> str:
    """Frontmatter canônico + H1 + nota editorial opcional + corpo."""
    cabecalho = gerar_frontmatter(meta).rstrip("\n")
    if extras:
        linhas = cabecalho.split("\n")
        fim = len(linhas) - 1  # linha de fechamento '---'
        for chave, valor in extras.items():
            linhas.insert(fim, f"{chave}: {yaml_str(str(valor))}")
            fim += 1
        cabecalho = "\n".join(linhas)
    partes = [cabecalho, "", f"# {meta['titulo']}", ""]
    if notas:
        for nota in notas:
            partes.append(f"> **Nota editorial.** {nota}")
            partes.append(">")
        partes.pop()
        partes.append("")
    partes.append(corpo.strip())
    return "\n".join(partes) + "\n"


def gravar(caminho_relativo: str, conteudo: str) -> Path:
    destino = RAIZ / caminho_relativo
    salvar_atomico(destino, conteudo.encode("utf-8"))
    return destino


def _texto_simples(html: str) -> str:
    import html as html_module
    return re.sub(r"\s+", " ", html_module.unescape(re.sub(r"<[^>]+>", " ", html or ""))).strip()


def documento_sijut(id_ato: int, titulo: str, tipo: str, numero: str, data: str, orgao: str,
                    tributos: list[str], tema: str = "Reforma Tributária e Transição",
                    notas_extra: list[str] = None, situacao: str = "Em vigor") -> tuple[str, dict]:
    """Monta o documento de um ato do Sijut/RFB (texto compilado) com metadados verificados."""
    corpo, dados = sijut_para_md(id_ato)
    ementa = _texto_simples(" ".join(e.get("textoIntegra") or "" for e in dados.get("ementas", [])))
    meta = {
        "titulo": titulo, "esfera": "Federal", "orgao": orgao, "tipo": tipo, "numero": numero,
        "data": data, "ano": data[:4], "tema_tributario": tema, "tributos_afetados": tributos,
        "situacao": situacao, "revogada": False, "fonte": url_sijut(id_ato), "ementa": ementa,
    }
    historico = [_texto_simples(h.get("texto")) for h in dados.get("historico", []) if h.get("texto")]
    notas = [f"Texto compilado obtido do Sijut/RFB em {DATA_CONSULTA_BR}. {dados.get('dadosPublicacao', '').strip()}."]
    if historico:
        notas.append("Histórico registrado no Sijut: " + "; ".join(historico) + ". O texto abaixo já incorpora essas alterações.")
    notas += notas_extra or []
    extras = {"data_consulta": DATA_CONSULTA, "versao_texto": "Compilado (Sijut/RFB)"}
    return montar_documento(meta, corpo, notas, extras), dados


def url_normas_leg(urn: str) -> str:
    return f"https://normas.leg.br/?urn={urn}"


def url_sijut(id_ato: int) -> str:
    return f"https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{id_ato}"
