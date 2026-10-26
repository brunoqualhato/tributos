"""O plano do acervo tributário e contábil: fontes, escopo e metas de integridade.

Este arquivo é a fonte única da verdade para a medição de progresso e cobertura.
"""
from collections import namedtuple

ItemPlano = namedtuple("ItemPlano", "setor nome caminho meta fase fonte")

FASES = {
    1: ("Fase 1 — Sistema Tributário Nacional & Federal", "CF/88, CTN, Leis Complementares, Decretos e Regulamentos Federais"),
    2: ("Fase 2 — Normativos Federais e Contabilidade", "Receita Federal (Sijut), CONFAZ, CFC, CPC, CARF, PGFN e CGSN"),
    3: ("Fase 3 — Legislação Estadual dos 27 Estados", "Regulamentos do ICMS (RICMS), Leis de IPVA e ITCMD das 27 UFs"),
    4: ("Fase 4 — Legislação Municipal", "Códigos Tributários Municipais e Regulamentos do ISS das Capitais e Grandes Polos"),
    5: ("Fase 5 — Precedentes Vinculantes & Tratados", "STF, STJ, Súmulas CARF e Acordos Internacionais de Bitributação"),
}

PLANO = [
    # Fase 1: Federal Estruturante
    ItemPlano("Constituição Federal", "Sistema Tributário Nacional (arts. 145-162 + EC 132/23)",
              "federal/constituicao", 1, 1, "https://www.planalto.gov.br"),
    ItemPlano("Leis Complementares", "Código Tributário Nacional (Lei 5.172/1966)",
              "federal/leis-complementares/ctn", 1, 1, "https://www.planalto.gov.br"),
    ItemPlano("Leis Complementares", "Lei Kandir (LC 87/1996 - ICMS)",
              "federal/leis-complementares/kandir", 1, 1, "https://www.planalto.gov.br"),
    ItemPlano("Leis Complementares", "Lei do ISSQN (LC 116/2003)",
              "federal/leis-complementares/iss", 1, 1, "https://www.planalto.gov.br"),
    ItemPlano("Leis Complementares", "Estatuto Nacional da ME e EPP - Simples Nacional (LC 123/2006)",
              "federal/leis-complementares/simples", 1, 1, "https://www.planalto.gov.br"),
    ItemPlano("Leis Ordinárias Federais", "Legislação do IRPJ, CSLL, PIS/COFINS, IPI, IOF",
              "federal/leis-ordinarias", 150, 1, "normas.leg.br + Planalto"),
    ItemPlano("Regulamentos Federais", "RIR/2018, RIPI/2010, Regulamento Aduaneiro, RPS",
              "federal/regulamentos", 4, 1, "https://www.planalto.gov.br"),

    # Fase 2: Reguladores Federais e Contabilidade
    ItemPlano("Receita Federal", "Instruções Normativas da RFB (vigentes e históricas)",
              "reguladores/rfb/instrucoes-normativas", 3000, 2, "normas.receita.fazenda.gov.br"),
    ItemPlano("Receita Federal", "Portarias e demais atos normativos da RFB",
              "reguladores/rfb/outros-atos", 5000, 2, "normas.receita.fazenda.gov.br"),
    ItemPlano("Receita Federal", "Soluções de Consulta COSIT e DISIT",
              "reguladores/rfb/solucoes-consulta", 25000, 2, "normas.receita.fazenda.gov.br"),
    ItemPlano("CONFAZ", "Convênios ICMS, Protocolos ICMS e Ajustes SINIEF",
              "reguladores/confaz", 6000, 2, "confaz.fazenda.gov.br / DOU"),
    ItemPlano("Simples Nacional", "Resoluções CGSN e CGSIM",
              "reguladores/cgsn", 200, 2, "gov.br/receitafederal/simplesnacional"),
    ItemPlano("CARF", "Súmulas e Acórdãos Paradigmas do CARF",
              "reguladores/carf", 300, 2, "carf.fazenda.gov.br"),
    ItemPlano("PGFN", "Pareceres Vinculantes e Portarias de Transação Fiscal",
              "reguladores/pgfn", 500, 2, "pgfn.gov.br"),
    ItemPlano("Normas Contábeis (CFC)", "Normas Brasileiras de Contabilidade (NBC TG, TSP, PG, PA, PP)",
              "contabil/cfc", 180, 2, "cfc.org.br"),
    ItemPlano("Pronunciamentos Contábeis (CPC)", "Pronunciamentos CPC (00 a 50+), Orientações e Interpretações",
              "contabil/cpc", 90, 2, "cpc.org.br"),

    # Fase 3: Estadual
    ItemPlano("ICMS Estadual", "Regulamentos do ICMS (RICMS) dos 26 Estados e DF",
              "estaduais/*/ricms", 27, 3, "Secretarias de Fazenda Estaduais (SEFAZ)"),
    ItemPlano("IPVA e ITCMD", "Leis ordinárias e regulamentos do IPVA e ITCMD das 27 UFs",
              "estaduais/*/outros-tributos", 150, 3, "Assembleias Legislativas e SEFAZ"),

    # Fase 4: Municipal
    ItemPlano("Direito Municipal", "Códigos Tributários Municipais (CTM) das 27 Capitais",
              "municipais/*/ctm", 27, 4, "Câmaras e Prefeituras das Capitais"),
    ItemPlano("Direito Municipal", "Regulamentos do ISS (RISS) das 27 Capitais",
              "municipais/*/riss", 27, 4, "Câmaras e Prefeituras das Capitais"),

    # Fase 5: Precedentes e Tratados
    ItemPlano("Tratados Internacionais", "Acordos para Evitar Dupla Tributação (Convenções Modelo)",
              "tratados/bitributacao", 45, 5, "MRE / Receita Federal"),
    ItemPlano("Jurisprudência Vinculante", "Súmulas Vinculantes e Temas Tributários de Repercussão Geral (STF)",
              "jurisprudencia/stf", 500, 5, "stf.jus.br / CNJ Pangea"),
    ItemPlano("Jurisprudência Vinculante", "Súmulas e Temas Repetitivos Tributários (STJ)",
              "jurisprudencia/stj", 400, 5, "stj.jus.br / CNJ Pangea"),
]
