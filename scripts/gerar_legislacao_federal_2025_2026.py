"""Lote: legislação federal de 2025-2026 posterior à EC 132/2023 e ausente do acervo.
Especialistas: tributos_dividendos, tributos_produtos e tributos_servicos

Documentos (texto original em normas.leg.br):
- Redução de benefícios tributários: LC 224/2025, Decreto 12.808/2025, LC 229/2026, LC 235/2026 e LC 237/2026;
- Processo e direitos do contribuinte: LC 225/2026 (Código de Defesa do Contribuinte) e LC 236/2026 (CTN);
- Renda: Lei 15.270/2025 (redução do IR de baixa renda, tributação mínima e IRRF sobre dividendos).

Uso: python3 scripts/gerar_legislacao_federal_2025_2026.py
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co

CONGRESSO = "Congresso Nacional / Presidência da República"
PRESIDENCIA = "Presidência da República"

# (urn, caminho, tipo, numero, data, titulo, orgao, tema, tributos, ementa, notas)
NORMAS = [
    ("urn:lex:br:federal:lei.complementar:2025-12-26;224",
     "federal/beneficios-tributarios/lei-complementar-224-2025-reducao-beneficios-tributarios.md",
     "Lei Complementar", "224", "2025-12-26",
     "Lei Complementar nº 224, de 26 de dezembro de 2025 (Redução de Incentivos e Benefícios Tributários da União)",
     CONGRESSO, "Benefícios e Incentivos Fiscais",
     ["IRPJ", "CSLL", "PIS/Pasep", "Cofins", "IPI", "Imposto de Importação"],
     "Dispõe sobre a redução e os critérios de concessão de incentivos e benefícios de natureza tributária, financeira ou creditícia concedidos exclusivamente no âmbito da União; estabelece a responsabilidade solidária de terceiros pelo recolhimento de tributos incidentes sobre a exploração de apostas de quota fixa; e altera as Leis Complementares nºs 101/2000, 105/2001 e 215/2025 e as Leis nºs 7.689/1988, 9.249/1995, 13.756/2018 e 8.137/1990.",
     ["Regulamentada pelo Decreto nº 12.808/2025 (`decreto-12808-2025-reducao-beneficios-tributarios.md`) e pela IN RFB nº 2.305/2025 "
      "(`ato-148694-2305-2025.md`, em `reguladores/rfb/instrucoes-normativas/2025/`). "
      "Segundo a ementa, a LC nº 239/2026 a alterou; essa alteração não foi incorporada ao texto abaixo."]),
    ("urn:lex:br:federal:decreto:2025-12-29;12808",
     "federal/beneficios-tributarios/decreto-12808-2025-reducao-beneficios-tributarios.md",
     "Decreto", "12808", "2025-12-29",
     "Decreto nº 12.808, de 29 de dezembro de 2025 (Redução de Benefícios Tributários - LC 224/2025)",
     PRESIDENCIA, "Benefícios e Incentivos Fiscais",
     ["IRPJ", "CSLL", "PIS/Pasep", "Cofins", "IPI", "Imposto de Importação"],
     "Dispõe sobre a redução dos incentivos e dos benefícios de natureza tributária concedidos no âmbito da União e sobre a responsabilidade solidária de terceiros pelo recolhimento de tributos incidentes sobre a exploração de apostas de quota fixa.",
     ["Regulamenta a Lei Complementar nº 224/2025 (`lei-complementar-224-2025-reducao-beneficios-tributarios.md`)."]),
    ("urn:lex:br:federal:lei.complementar:2026-03-30;229",
     "federal/beneficios-tributarios/lei-complementar-229-2026-beneficios-tributarios-2026.md",
     "Lei Complementar", "229", "2026-03-30",
     "Lei Complementar nº 229, de 30 de março de 2026 (Benefícios Tributários e Despesas Obrigatórias em 2026)",
     CONGRESSO, "Benefícios e Incentivos Fiscais", ["PIS/Pasep", "Cofins"],
     "Dispõe sobre regras relativas a benefícios tributários e despesas obrigatórias no exercício de 2026.",
     ["Alterada pela Lei Complementar nº 237/2026 (`lei-complementar-237-2026-altera-lc-229.md`); o texto abaixo é o original."]),
    ("urn:lex:br:federal:lei.complementar:2026-08-27;235",
     "federal/beneficios-tributarios/lei-complementar-235-2026-renuncias-choque-energia.md",
     "Lei Complementar", "235", "2026-08-27",
     "Lei Complementar nº 235, de 27 de agosto de 2026 (Renúncias de Receita e Choque no Mercado de Energia)",
     CONGRESSO, "Benefícios e Incentivos Fiscais", ["PIS/Pasep", "Cofins"],
     "Dispõe sobre regras para renúncias de receita com o objetivo de mitigar os impactos econômicos causados pelo choque no mercado internacional de energia decorrente do conflito no Oriente Médio e excepcionaliza os benefícios tributários destinados à Política Nacional de Minerais Críticos e Estratégicos, ao Programa de Desenvolvimento da Indústria de Fertilizantes e à realização da Copa do Mundo Feminina, e dá outras providências.",
     ["O art. 5º permite às produtoras de etanol utilizar saldos credores de PIS/Pasep e Cofins, regulamentado pela IN RFB nº 2.344/2026 "
      "(fora deste lote). Segundo a ementa, a LC nº 239/2026 a alterou; essa alteração não foi incorporada ao texto abaixo."]),
    ("urn:lex:br:federal:lei.complementar:2026-09-15;237",
     "federal/beneficios-tributarios/lei-complementar-237-2026-altera-lc-229.md",
     "Lei Complementar", "237", "2026-09-15",
     "Lei Complementar nº 237, de 15 de setembro de 2026 (Altera a LC 229/2026: Datacenter, Resseguradoras e Programas Federais)",
     CONGRESSO, "Benefícios e Incentivos Fiscais", ["IRPJ", "CSLL"],
     "Altera a Lei Complementar nº 229, de 30 de março de 2026, para incluir o regime especial de tributação para serviços de datacenter, os programas federais de financiamento de ações de apoio às pessoas com câncer e às pessoas com deficiência e a desoneração do IRPJ e da CSLL das sociedades resseguradoras locais entre as exceções às regras de concessão de benefícios tributários; e altera a Lei Complementar nº 101/2000 (LRF).",
     ["Altera a Lei Complementar nº 229/2026 (`lei-complementar-229-2026-beneficios-tributarios-2026.md`)."]),
    ("urn:lex:br:federal:lei.complementar:2026-01-08;225",
     "federal/leis-complementares/lei-complementar-225-2026-codigo-defesa-contribuinte.md",
     "Lei Complementar", "225", "2026-01-08",
     "Lei Complementar nº 225, de 8 de janeiro de 2026 (Código de Defesa do Contribuinte)",
     CONGRESSO, "Processo Tributário e Fiscal",
     ["Direitos do Contribuinte", "Devedor Contumaz", "Programas de Conformidade"],
     "Institui o Código de Defesa do Contribuinte.",
     ["Os programas de conformidade tributária e aduaneira previstos nesta Lei Complementar foram regulamentados por instruções normativas da "
      "Receita Federal publicadas em março de 2026 (fora deste lote)."]),
    ("urn:lex:br:federal:lei.complementar:2026-09-04;236",
     "federal/leis-complementares/lei-complementar-236-2026-solucao-controversias-ctn.md",
     "Lei Complementar", "236", "2026-09-04",
     "Lei Complementar nº 236, de 4 de setembro de 2026 (Solução de Controvérsias, Consensualidade e Processo Administrativo Tributário - CTN)",
     CONGRESSO, "Processo Tributário e Fiscal",
     ["CTN", "Processo Administrativo Tributário", "Consensualidade"],
     "Altera a Lei nº 5.172, de 25 de outubro de 1966 (Código Tributário Nacional), para dispor sobre normas gerais para solução de controvérsias, consensualidade e processo administrativo em matéria tributária e aduaneira, e revoga dispositivo da Lei nº 9.430, de 27 de dezembro de 1996.",
     ["O acervo mantém o Código Tributário Nacional em `federal/leis-complementares/ctn/lei-5172-1966.md`; este documento traz apenas o texto "
      "da Lei Complementar nº 236/2026, não o CTN consolidado."]),
    ("urn:lex:br:federal:lei:2025-11-26;15270",
     "federal/leis-ordinarias/dividendos-jcp/lei-15270-2025-irpf-altas-rendas-dividendos.md",
     "Lei Ordinária", "15270", "2025-11-26",
     "Lei nº 15.270, de 26 de novembro de 2025 (Redução do IRPF, Tributação Mínima de Altas Rendas e IRRF sobre Dividendos)",
     CONGRESSO, "Dividendos e Renda do Capital", ["IRPF", "IRRF"],
     "Altera a Lei nº 9.250, de 26 de dezembro de 1995, e a Lei nº 9.249, de 26 de dezembro de 1995, para instituir a redução do imposto sobre a renda devido nas bases de cálculo mensal e anual e a tributação mínima para as pessoas físicas que auferem altas rendas; e dá outras providências.",
     ["Altera as Leis nº 9.249/1995 (`federal/leis-ordinarias/dividendos-jcp/lei-9249-1995.md`) e nº 9.250/1995. As tabelas de redução foram "
      "convertidas para Markdown conforme o texto original. A IN RFB nº 2.299/2025 (no acervo) atualiza as normas gerais do IRPF."]),
]


def construir(urn, tipo, numero, data, titulo, orgao, tema, tributos, ementa, notas):
    r = co.api().baixar_norma_lexml(urn)
    publicacao = r["metadados"].get("datePublished") or data
    dia = f"{publicacao[8:10]}/{publicacao[5:7]}/{publicacao[:4]}"
    meta = {
        "titulo": titulo, "esfera": "Federal", "orgao": orgao, "tipo": tipo, "numero": numero,
        "data": data, "ano": data[:4], "tema_tributario": tema, "tributos_afetados": tributos,
        "situacao": "Em vigor", "revogada": False, "fonte": co.url_normas_leg(urn), "ementa": ementa,
    }
    notas_doc = [f"Texto original publicado em {dia} (DOU), obtido em normas.leg.br em {co.DATA_CONSULTA_BR}."] + notas
    extras = {"data_consulta": co.DATA_CONSULTA, "versao_texto": f"Original (DOU de {dia})"}
    return co.montar_documento(meta, co.lexml_para_md(urn), notas_doc, extras)


if __name__ == "__main__":
    for urn, caminho, tipo, numero, data, titulo, orgao, tema, tributos, ementa, notas in NORMAS:
        doc = construir(urn, tipo, numero, data, titulo, orgao, tema, tributos, ementa, notas)
        destino = co.gravar(caminho, doc)
        print(f"[Legislação 2025-2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes)")
