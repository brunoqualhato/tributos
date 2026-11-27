"""Lote: Regulamentos da CBS e do IBS (Reforma Tributária do Consumo), 2026.
Especialista: tributos_reforma_transicao

Documentos:
- Decreto nº 12.955/2026 (Regulamento da CBS), texto original (normas.leg.br);
- Decreto nº 13.075/2026 (altera o Regulamento da CBS), texto original (normas.leg.br);
- Resolução CGIBS nº 6/2026 (Regulamento do IBS), PDF oficial do CGIBS;
- Resolução CGIBS nº 13/2026 (altera o Regulamento do IBS), PDF oficial do CGIBS;
- Portaria Conjunta MF/CGIBS nº 7/2026 (disposições comuns CBS/IBS), Sijut/RFB.

Uso: python3 scripts/gerar_reforma_regulamentos_2026.py
"""
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
import pdf_regulamento as pdfr

CGIBS = "https://www.cgibs.gov.br/upload/arquivos"
PDF_RES6 = f"{CGIBS}/202604/30084927-res-cgibs-n-6-30-abr-2026-regulamenta-o-ibs.pdf"
PDF_RES13 = f"{CGIBS}/202607/22121010-resolucao-cgibs-n-13-de-22-de-julho-de-2026.pdf"

ORGAO_CGIBS = "Comitê Gestor do Imposto sobre Bens e Serviços (CGIBS)"
RX_TITULO_RES = re.compile(r"RESOLUÇÃO CGIBS Nº \d+, DE \d+ DE [A-ZÇÃÕ]+ DE \d{4}")


def decreto_12955() -> str:
    urn = "urn:lex:br:federal:decreto:2026-04-29;12955"
    meta = {
        "titulo": "Decreto nº 12.955, de 29 de abril de 2026 (Regulamento da Contribuição sobre Bens e Serviços - CBS)",
        "esfera": "Federal", "orgao": "Presidência da República", "tipo": "Decreto", "numero": "12955",
        "data": "2026-04-29", "ano": "2026", "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": ["CBS", "IBS", "PIS/Pasep", "Cofins"],
        "situacao": "Em vigor (alterado pelo Decreto nº 13.075/2026)", "revogada": False,
        "fonte": co.url_normas_leg(urn),
        "ementa": "Regulamenta a Contribuição Social sobre Bens e Serviços - CBS e dá outras providências.",
    }
    notas = [
        "Texto original publicado no Diário Oficial da União de 30/04/2026, obtido em normas.leg.br em "
        f"{co.DATA_CONSULTA_BR}. Os arts. 105, 115 e 619 foram alterados pelo Decreto nº 13.075, de 21 de julho de 2026, "
        "incorporado ao acervo em documento próprio (`decreto-13075-2026-altera-regulamento-cbs.md`).",
        "Os anexos do próprio Decreto (por exemplo, o Anexo I de taxas de depreciação e as tabelas do Anexo IV, citados "
        "nos arts. 47 e seguintes) não constam do texto estruturado disponibilizado em normas.leg.br e não foram "
        "incorporados. Para esses anexos, consultar a publicação no DOU. Os anexos do Regulamento do IBS constam do "
        "documento da Resolução CGIBS nº 6/2026.",
    ]
    extras = {"data_consulta": co.DATA_CONSULTA, "versao_texto": "Original (DOU de 30/04/2026)"}
    return co.montar_documento(meta, co.lexml_para_md(urn), notas, extras)


def decreto_13075() -> str:
    urn = "urn:lex:br:federal:decreto:2026-07-21;13075"
    meta = {
        "titulo": "Decreto nº 13.075, de 21 de julho de 2026 (Altera o Regulamento da CBS)",
        "esfera": "Federal", "orgao": "Presidência da República", "tipo": "Decreto", "numero": "13075",
        "data": "2026-07-21", "ano": "2026", "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": ["CBS", "IBS"], "situacao": "Em vigor", "revogada": False,
        "fonte": co.url_normas_leg(urn),
        "ementa": "Altera o Decreto nº 12.955, de 29 de abril de 2026, que regulamenta a Contribuição Social sobre Bens e Serviços - CBS.",
    }
    notas = [
        "Texto original publicado no Diário Oficial da União de 22/07/2026, obtido em normas.leg.br em "
        f"{co.DATA_CONSULTA_BR}. Altera os arts. 105, 115 e 619 do Regulamento da CBS "
        "(`decreto-12955-2026-regulamento-cbs.md`), fixando 1º de janeiro de 2027 para a inscrição no CNPJ e a emissão de "
        "documentos fiscais por pessoas físicas contribuintes ou responsáveis e por produtores rurais pessoas físicas.",
    ]
    extras = {"data_consulta": co.DATA_CONSULTA, "versao_texto": "Original (DOU de 22/07/2026)"}
    return co.montar_documento(meta, co.lexml_para_md(urn), notas, extras)


def resolucao_cgibs_6() -> str:
    pdf = co.baixar_pdf(PDF_RES6, "resolucao-cgibs-6-2026.pdf")
    total = pdfr.numero_paginas(pdf)
    p_ini = pdfr.localizar_pagina(pdf, r"^RESOLUÇÃO CGIBS Nº 6, DE 30 DE ABRIL DE 2026\s*\nRegulamenta")
    p_anexos = pdfr.localizar_pagina(pdf, r"^ANEXO I - TAXAS ANUAIS DE DEPRECIAÇÃO \(ART\. 48, § 1º\)\s*\nITEM")
    corpo = pdfr.corpo_para_markdown(pdfr.pdftotext(pdf, primeira=p_ini, ultima=p_anexos - 1), RX_TITULO_RES)
    numeros = [int(m.group(1)) for m in re.finditer(r"^Art\.\s(\d+)[º°o]?\.?\s", corpo, re.M)]
    if numeros != list(range(1, 618)):
        raise RuntimeError("Sequência de artigos da Resolução CGIBS nº 6/2026 incompleta ou fora de ordem")
    anexos = pdfr.anexos_para_markdown(pdf, p_anexos, total)
    meta = {
        "titulo": "Resolução CGIBS nº 6, de 30 de abril de 2026 (Regulamento do Imposto sobre Bens e Serviços - IBS)",
        "esfera": "Federal", "orgao": ORGAO_CGIBS, "tipo": "Resolução", "numero": "6",
        "data": "2026-04-30", "ano": "2026", "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": ["IBS", "CBS", "Split Payment"],
        "situacao": "Em vigor (art. 617 alterado pela Resolução CGIBS nº 13/2026)", "revogada": False,
        "fonte": PDF_RES6,
        "ementa": "Regulamenta o Imposto sobre Bens e Serviços (IBS) e dá outras providências.",
    }
    notas = [
        "Texto extraído da camada de texto do PDF oficial divulgado no portal do CGIBS em 30/04/2026 "
        f"({total} páginas), consultado em {co.DATA_CONSULTA_BR}. Foram removidos o sumário e a numeração de página; a "
        "sequência dos 617 artigos foi conferida. Sinais gráficos como travessões podem diferir do original; "
        "em caso de dúvida, prevalece o PDF.",
        "O art. 617 foi alterado pela Resolução CGIBS nº 13, de 22 de julho de 2026 "
        "(`resolucao-cgibs-13-2026-altera-regulamento-ibs.md`). Os Anexos I a V são tabelas e foram preservados em blocos "
        "de texto que mantêm as colunas do PDF.",
    ]
    extras = {"data_consulta": co.DATA_CONSULTA, "versao_texto": "Original (portal do CGIBS, 30/04/2026)"}
    return co.montar_documento(meta, corpo + "\n\n## Anexos\n\n" + anexos, notas, extras)


def resolucao_cgibs_13() -> str:
    pdf = co.baixar_pdf(PDF_RES13, "resolucao-cgibs-13-2026.pdf")
    corpo = pdfr.corpo_para_markdown(pdfr.pdftotext(pdf), RX_TITULO_RES)
    meta = {
        "titulo": "Resolução CGIBS nº 13, de 22 de julho de 2026 (Altera o Regulamento do IBS)",
        "esfera": "Federal", "orgao": ORGAO_CGIBS, "tipo": "Resolução", "numero": "13",
        "data": "2026-07-22", "ano": "2026", "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": ["IBS"], "situacao": "Em vigor", "revogada": False,
        "fonte": PDF_RES13,
        "ementa": "Altera o Regulamento do Imposto sobre Bens e Serviços (IBS), divulgado pela Resolução CGIBS nº 6, de 30 de abril de 2026.",
    }
    notas = [
        "Texto extraído do PDF oficial divulgado no portal do CGIBS em 22/07/2026, consultado em "
        f"{co.DATA_CONSULTA_BR}. A ementa oficial usa a redação \"Altera o Regulamenta o Imposto sobre Bens e Serviços (IBS) "
        "e dá outras providências\", reproduzida no corpo abaixo; a ementa do cabeçalho foi normalizada.",
    ]
    extras = {"data_consulta": co.DATA_CONSULTA, "versao_texto": "Original (portal do CGIBS, 22/07/2026)"}
    return co.montar_documento(meta, corpo, notas, extras)


def portaria_conjunta_7() -> str:
    doc, _ = co.documento_sijut(
        150871, "Portaria Conjunta MF / CGIBS nº 7, de 30 de abril de 2026", "Portaria Conjunta", "7", "2026-04-30",
        "Ministério da Fazenda / Comitê Gestor do Imposto sobre Bens e Serviços", ["CBS", "IBS"])
    return doc


LOTE = [
    ("reforma-tributaria/regulamentos/decreto-12955-2026-regulamento-cbs.md", decreto_12955),
    ("reforma-tributaria/regulamentos/decreto-13075-2026-altera-regulamento-cbs.md", decreto_13075),
    ("reforma-tributaria/regulamentos/resolucao-cgibs-6-2026-regulamento-ibs.md", resolucao_cgibs_6),
    ("reforma-tributaria/regulamentos/resolucao-cgibs-13-2026-altera-regulamento-ibs.md", resolucao_cgibs_13),
    ("reguladores/rfb/outros-atos/2026/ato-150871-7-2026.md", portaria_conjunta_7),
]

if __name__ == "__main__":
    for caminho, construtor in LOTE:
        destino = co.gravar(caminho, construtor())
        print(f"[Reforma 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes)")
