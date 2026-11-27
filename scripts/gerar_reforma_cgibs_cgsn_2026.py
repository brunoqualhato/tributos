"""Lote: Simples Nacional na Reforma Tributária (Resoluções CGSN) e atos de governança do CGIBS (2026).
Especialista: tributos_reforma_transicao

Documentos:
- Resoluções CGSN nº 186, 190, 192, 194 e 196/2026 (Sijut/RFB, visão compilada);
- Resoluções CGIBS nº 4, 5, 9, 14 e 20/2026 (PDFs oficiais do portal do CGIBS).

Uso: python3 scripts/gerar_reforma_cgibs_cgsn_2026.py
"""
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
import pdf_regulamento as pdfr

CGIBS = "https://www.cgibs.gov.br/upload/arquivos"
ORGAO_CGIBS = "Comitê Gestor do Imposto sobre Bens e Serviços (CGIBS)"
ORGAO_CGSN = "Comitê Gestor do Simples Nacional (CGSN)"
RX_TITULO_RES = re.compile(r"RESOLUÇÃO CG-?IBS Nº \d+, DE \d+ DE [A-ZÇÃÕ]+ DE \d{4}")

# (idAto, titulo, numero, data, tributos, notas)
CGSN = [
    (150653, "Resolução CGSN nº 186, de 9 de abril de 2026", "186", "2026-04-09", ["Simples Nacional", "IBS", "CBS"],
     ["Dispõe sobre o exercício da opção pelo Simples Nacional e, para os optantes, pelo regime regular do IBS e da CBS em 2027. "
      "Alterada pela Resolução CGSN nº 194/2026 (`ato-153801-194-2026.md`)."]),
    (152832, "Resolução CGSN nº 190, de 4 de agosto de 2026", "190", "2026-08-04", ["Simples Nacional", "IBS", "CBS"],
     ["Altera a Resolução CGSN nº 140/2018 (`federal/leis-complementares/simples/resolucao-cgsn-140-2018-simples-nacional.md`), "
      "Este documento traz apenas o texto da Resolução nº 190/2026, não a Resolução nº 140 consolidada. Alterada pela Resolução CGSN nº 196/2026 (`ato-154694-196-2026.md`)."]),
    (152805, "Resolução CGSN nº 192, de 4 de agosto de 2026", "192", "2026-08-04", ["Simples Nacional", "IBS"],
     ["Altera a Resolução CGSN nº 11/2007, sobre a arrecadação do Regime Especial Unificado de Arrecadação de Tributos e Contribuições."]),
    (153801, "Resolução CGSN nº 194, de 25 de setembro de 2026", "194", "2026-09-25", ["Simples Nacional", "IBS", "CBS"],
     ["Altera a Resolução CGSN nº 186/2026 (`ato-150653-186-2026.md`)."]),
    (154694, "Resolução CGSN nº 196, de 16 de novembro de 2026", "196", "2026-11-16", ["Simples Nacional", "IBS", "CBS"],
     ["Altera as Resoluções CGSN nº 140/2018 e nº 190/2026 (`ato-152832-190-2026.md`)."]),
]

# (chave do cache, caminho do PDF, caminho do documento, titulo, numero, data, tributos, ementa, situacao, notas)
CGIBS_RES = [
    ("resolucao-cgibs-4-2026", "202604/13174441-resolucao-cgibs-n-4-de-8-de-abril-de-2026-regimento-interno-procedimental.pdf",
     "reforma-tributaria/cgibs/resolucao-cgibs-4-2026-regimento-interno-procedimental.md",
     "Resolução CGIBS nº 4, de 8 de abril de 2026 (Regimento Interno Procedimental do CGIBS)", "4", "2026-04-08", ["IBS"],
     "Aprova o Regimento Interno Procedimental do Comitê Gestor do Imposto sobre Bens e Serviços.",
     "Em vigor (alterada pelas Resoluções CGIBS nº 5 e nº 9/2026)",
     ["Alterada pelas Resoluções CGIBS nº 5/2026 (`resolucao-cgibs-5-2026-altera-regimento-interno.md`) e nº 9/2026 "
      "(`resolucao-cgibs-9-2026-altera-regimento-procedimental.md`); o texto abaixo é o original. A epígrafe do PDF usa a grafia \"CG-IBS\"."]),
    ("resolucao-cgibs-5-2026", "202604/30221158-resolucao-cgibs-n-5-de-30-de-abril-de-2026.pdf",
     "reforma-tributaria/cgibs/resolucao-cgibs-5-2026-altera-regimento-interno.md",
     "Resolução CGIBS nº 5, de 30 de abril de 2026 (Altera o Regimento Interno Procedimental)", "5", "2026-04-30", ["IBS"],
     "Altera a Resolução CGIBS nº 4, de 8 de abril de 2026, para dispor sobre a estrutura organizacional mínima do CGIBS e sobre a eleição e o provimento do cargo de Diretor Executivo.",
     "Em vigor", []),
    ("resolucao-cgibs-9-2026", "202606/17170454-resolucao-cgibs-n-9-de-10-de-junho-de-2026-altera-o-regimento-procedimental-1.pdf",
     "reforma-tributaria/cgibs/resolucao-cgibs-9-2026-altera-regimento-procedimental.md",
     "Resolução CGIBS nº 9, de 10 de junho de 2026 (Altera o Regimento Procedimental)", "9", "2026-06-10", ["IBS"],
     "Altera as Resoluções CGIBS nº 1, de 23 de fevereiro de 2026, que institui Comissões de Trabalho de caráter transitório, e nº 4, de 8 de abril de 2026, que aprova o Regimento Interno Procedimental.",
     "Em vigor", []),
    ("resolucao-cgibs-14-2026", "202607/31144942-resoluc-ao-cgibs-n-14-de-29-de-julho-de-2026-proposta-percentual-ibs-cgibs-2027.pdf",
     "reforma-tributaria/cgibs/resolucao-cgibs-14-2026-percentual-ibs-financiamento-cgibs-2027.md",
     "Resolução CGIBS nº 14, de 29 de julho de 2026 (Percentual do IBS para o Financiamento do CGIBS e Estimativa de Arrecadação em 2027)",
     "14", "2026-07-29", ["IBS"],
     "Publica a proposta do percentual do produto da arrecadação do IBS de cada ente federativo destinado ao financiamento do Comitê Gestor do Imposto sobre Bens e Serviços (CGIBS) no exercício financeiro de 2027 e a estimativa de arrecadação do IBS para o exercício financeiro de 2027.",
     "Em vigor",
     ["É uma proposta submetida aos Poderes Legislativos dos entes, nos termos do art. 47 da LC 227/2026. O Anexo (nota técnica com quadros) "
      "foi preservado em bloco de texto que mantém as colunas do PDF."]),
    ("resolucao-cgibs-20-2026", "202611/17165820-resoluc-a-o-cgibs-n-20-de-17-de-novembro-de-2026.pdf",
     "reforma-tributaria/cgibs/resolucao-cgibs-20-2026-tipologia-dos-atos.md",
     "Resolução CGIBS nº 20, de 17 de novembro de 2026 (Tipologia dos Atos e Instrumentos Formais do CGIBS)", "20", "2026-11-17", ["IBS"],
     "Dispõe sobre a tipologia, a finalidade, a competência, a elaboração, a aprovação, a expedição, o registro e a publicidade dos atos e instrumentos formais no âmbito do Comitê Gestor do Imposto sobre Bens e Serviços - CGIBS.",
     "Em vigor", []),
]


def documento_cgsn(id_ato, titulo, numero, data, tributos, notas):
    doc, _ = co.documento_sijut(id_ato, titulo, "Resolução", numero, data, ORGAO_CGSN, tributos, notas_extra=notas)
    return f"reguladores/rfb/outros-atos/{data[:4]}/ato-{id_ato}-{numero}-{data[:4]}.md", doc


def documento_cgibs(chave, pdf_rel, caminho, titulo, numero, data, tributos, ementa, situacao, notas):
    url = f"{CGIBS}/{pdf_rel}"
    pdf = co.baixar_pdf(url, f"{chave}.pdf")
    total = pdfr.numero_paginas(pdf)
    try:
        p_anexo = pdfr.localizar_pagina(pdf, r"^ANEXO À RESOLUÇÃO")
    except ValueError:
        p_anexo = None
    ultima_corpo = (p_anexo - 1) if p_anexo else total
    corpo = pdfr.corpo_para_markdown(pdfr.pdftotext(pdf, primeira=1, ultima=ultima_corpo), RX_TITULO_RES)
    if p_anexo:
        layout = pdfr.pdftotext(pdf, layout=True, primeira=p_anexo, ultima=total).replace("\f", "\n")
        linhas = [l.rstrip() for l in layout.split("\n") if not re.fullmatch(r"\s*\d{1,3}\s*", l)]
        anexo = re.sub(r"\n{3,}", "\n\n", "\n".join(linhas)).strip("\n")
        corpo += f"\n\n## Anexo\n\n```text\n{anexo}\n```"
    meta = {
        "titulo": titulo, "esfera": "Federal", "orgao": ORGAO_CGIBS, "tipo": "Resolução", "numero": numero,
        "data": data, "ano": data[:4], "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": tributos, "situacao": situacao, "revogada": False, "fonte": url, "ementa": ementa,
    }
    base = (f"Texto extraído do PDF oficial divulgado no portal do CGIBS ({total} página(s)), consultado em {co.DATA_CONSULTA_BR}. "
            "Foram removidos cabeçalhos de órgão e numeração de página.")
    extras = {"data_consulta": co.DATA_CONSULTA, "versao_texto": "Original (portal do CGIBS)"}
    return caminho, co.montar_documento(meta, corpo, [base] + notas, extras)


if __name__ == "__main__":
    docs = [documento_cgsn(*c) for c in CGSN] + [documento_cgibs(*r) for r in CGIBS_RES]
    for caminho, conteudo in docs:
        destino = co.gravar(caminho, conteudo)
        print(f"[CGSN/CGIBS 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes)")
