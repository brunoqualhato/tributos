"""O plano do acervo tributário e contábil: fontes, escopo e metas de integridade.

Este arquivo é a fonte única da verdade para a medição de progresso e cobertura,
estruturado nos 4 pilares essenciais da tributação brasileira + normas contábeis:
1. Dividendos, Renda do Capital & IRPJ/IRPF
2. Folha de Pagamento, Funcionário & Encargos Previdenciários
3. Produtos, Mercadorias & Indústria (ICMS, IPI, PIS/COFINS Monofásico)
4. Serviços, ISS & Retenções na Fonte
5. Contabilidade (CFC / CPC) e Jurisprudência Vinculante
"""
from collections import namedtuple

ItemPlano = namedtuple("ItemPlano", "setor pilar nome caminho meta fase fonte")

FASES = {
    1: ("Fase 1 — Legislação Estruturante & Códigos", "CF/88, CTN, Leis Complementares e Regulamentos Federais"),
    2: ("Fase 2 — Normativos Federais e Regulamentação", "Receita Federal (Sijut), CONFAZ, CFC, CPC, CARF, PGFN e CGSN"),
    3: ("Fase 3 — Legislação Estadual das 27 UFs", "Regulamentos do ICMS (RICMS), Leis de IPVA e ITCMD das 27 UFs"),
    4: ("Fase 4 — Legislação Municipal", "Códigos Tributários Municipais e Regulamentos do ISS das Capitais e Grandes Polos"),
    5: ("Fase 5 — Precedentes Vinculantes & Tratados", "STF, STJ, Súmulas CARF e Acordos Internacionais de Bitributação"),
}

PLANO = [
    # =========================================================================
    # PILAR 1: DIVIDENDOS, RENDA DO CAPITAL & IRPJ/IRPF
    # =========================================================================
    ItemPlano("Dividendos & Renda do Capital", "Dividendos",
              "Isenção de Dividendos e Juros sobre Capital Próprio - JCP (Lei 9.249/95 e RIR/2018)",
              "federal/leis-ordinarias/dividendos-jcp", 25, 1, "Planalto / normas.leg.br"),
    ItemPlano("Dividendos & Renda do Capital", "Lucro Real e Presumido",
              "Tributação de Lucros, Equivalência Patrimonial e IRPJ/CSLL (Leis 8.981/95, 9.430/96, 12.973/14)",
              "federal/leis-ordinarias/irpj-csll", 60, 1, "Planalto / normas.leg.br"),
    ItemPlano("Dividendos & Renda do Capital", "Offshores e Trusts",
              "Tributação de Renda e Fundos no Exterior (Lei 14.754/2023 e INs)",
              "federal/leis-ordinarias/offshores", 15, 1, "Planalto / RFB"),
    ItemPlano("Dividendos & Renda do Capital", "Regulamento do IRPJ",
              "Regulamento do Imposto de Renda - RIR/2018 (Decreto 9.580/2018)",
              "federal/regulamentos/rir", 1, 1, "Planalto"),
    ItemPlano("Dividendos & Renda do Capital", "Soluções de Consulta RFB",
              "Soluções de Consulta COSIT sobre Dividendos, JCP, Ágio e Reorganizações Societárias",
              "reguladores/rfb/solucoes-consulta/dividendos", 2500, 2, "normas.receita.fazenda.gov.br"),

    # =========================================================================
    # PILAR 2: FOLHA DE PAGAMENTO, FUNCIONÁRIO & ENCARGOS PREVIDENCIÁRIOS
    # =========================================================================
    ItemPlano("Folha & Encargos Trabalhistas", "Previdência e Custeio",
              "Plano de Custeio da Previdência Social (Lei 8.212/1991 e Lei 8.213/1991)",
              "federal/leis-ordinarias/previdencia-custeio", 10, 1, "Planalto"),
    ItemPlano("Folha & Encargos Trabalhistas", "Regulamento da Previdência",
              "Regulamento da Previdência Social - RPS (Decreto 3.048/1999)",
              "federal/regulamentos/rps", 1, 1, "Planalto"),
    ItemPlano("Folha & Encargos Trabalhistas", "Norma Geral Previdenciária RFB",
              "Instrução Normativa RFB nº 2.110/2022 (Consolidação Previdenciária e Retenções)",
              "reguladores/rfb/instrucoes-normativas/folha", 50, 2, "normas.receita.fazenda.gov.br"),
    ItemPlano("Folha & Encargos Trabalhistas", "RAT / FAP e Riscos",
              "Regulamentação de RAT, FAP e Contribuições a Terceiros / Sistema S",
              "reguladores/rfb/rat-fap-terceiros", 120, 2, "RFB / MPS"),
    ItemPlano("Folha & Encargos Trabalhistas", "IRRF Folha e PLR",
              "Retenção na Fonte sobre Salários, Rescisões e PLR (Lei 10.101/2000 e Tabela Progressiva)",
              "federal/leis-ordinarias/irrf-folha-plr", 35, 1, "Planalto / RFB"),
    ItemPlano("Folha & Encargos Trabalhistas", "FGTS e eSocial",
              "Normas do FGTS (Lei 8.036/1990), FGTS Digital, eSocial e DCTFWeb",
              "reguladores/mte-caixa/fgts-esocial", 80, 2, "Caixa / MTE"),
    ItemPlano("Folha & Encargos Trabalhistas", "Desoneração da Folha",
              "Contribuição Previdenciária sobre a Receita Bruta - CPRB (Lei 12.546/2011)",
              "federal/leis-ordinarias/cprb", 20, 1, "Planalto"),

    # =========================================================================
    # PILAR 3: PRODUTOS, MERCADORIAS & INDÚSTRIA
    # =========================================================================
    ItemPlano("Produtos & Mercadorias", "ICMS Geral e DIFAL",
              "Lei Kandir (LC 87/1996) e DIFAL (LC 190/2022)",
              "federal/leis-complementares/kandir", 5, 1, "Planalto"),
    ItemPlano("Produtos & Mercadorias", "CONFAZ e ICMS-ST",
              "Convênios ICMS (Substituição Tributária - Convênio 142/2018), Protocolos e Ajustes SINIEF",
              "reguladores/confaz", 6000, 2, "confaz.fazenda.gov.br"),
    ItemPlano("Produtos & Mercadorias", "IPI e TIPI",
              "Lei do IPI (Lei 4.502/1964), RIPI/2010 (Decreto 7.212/2010) e Tabela TIPI",
              "federal/regulamentos/ripi", 15, 1, "Planalto / RFB"),
    ItemPlano("Produtos & Mercadorias", "PIS/COFINS Monofásico",
              "Regimes Monofásicos de Combustíveis, Bebidas, Fármacos e Autopeças",
              "reguladores/rfb/pis-cofins-monofasico", 150, 2, "normas.receita.fazenda.gov.br"),
    ItemPlano("Produtos & Mercadorias", "Comércio Exterior e Aduana",
              "Imposto de Importação e Regulamento Aduaneiro (Decreto 6.759/2009)",
              "federal/regulamentos/aduana", 10, 1, "Planalto"),
    ItemPlano("Produtos & Mercadorias", "Reforma - Imposto Seletivo",
              "Imposto Seletivo e CBS/IBS sobre Bens (EC 132/2023 e Leis Complementares)",
              "federal/reforma-tributaria/produtos-seletivo", 20, 1, "Planalto"),
    ItemPlano("Produtos & Mercadorias", "RICMS das 27 UFs",
              "Regulamentos do ICMS dos 26 Estados e Distrito Federal",
              "estaduais/*/ricms", 27, 3, "Secretarias de Fazenda Estaduais"),

    # =========================================================================
    # PILAR 4: SERVIÇOS, ISS & RETENÇÕES NA FONTE
    # =========================================================================
    ItemPlano("Serviços & Retenções", "ISSQN Geral",
              "Lei do ISSQN (Lei Complementar 116/2003 e lista anexa de serviços)",
              "federal/leis-complementares/iss", 5, 1, "Planalto"),
    ItemPlano("Serviços & Retenções", "Retenções na Fonte de Serviços",
              "CSRF 4,65% (Lei 10.833/03 art. 30), IRRF 1,5% e Retenção INSS 11%",
              "reguladores/rfb/retencoes-servicos", 150, 2, "normas.receita.fazenda.gov.br"),
    ItemPlano("Serviços & Retenções", "CTM e RISS das Capitais",
              "Códigos Tributários e Regulamentos do ISS das 27 Capitais",
              "municipais/*/servicos-iss", 54, 4, "Câmaras e Prefeituras das Capitais"),
    ItemPlano("Serviços & Retenções", "Reforma - IBS/CBS Serviços",
              "Transição do ISS para o IBS/CBS na prestação de serviços",
              "federal/reforma-tributaria/servicos", 20, 1, "Planalto"),

    # =========================================================================
    # PILAR 5: CONTABILIDADE (CFC / CPC) & PRECEDENTES VINCULANTES
    # =========================================================================
    ItemPlano("Contabilidade & Precedentes", "Normas CFC",
              "Normas Brasileiras de Contabilidade (NBC TG, TSP, PG, PA, PP)",
              "contabil/cfc", 180, 2, "cfc.org.br"),
    ItemPlano("Contabilidade & Precedentes", "Pronunciamentos CPC",
              "Pronunciamentos Técnicos CPC (00 a 50+), OCPC e ICPC",
              "contabil/cpc", 90, 2, "cpc.org.br"),
    ItemPlano("Contabilidade & Precedentes", "Precedentes STF / STJ",
              "Súmulas Vinculantes, Temas de Repercussão Geral e Recursos Repetitivos Fiscais",
              "jurisprudencia/precedentes-vinculantes", 900, 5, "STF / STJ / CNJ"),
    ItemPlano("Contabilidade & Precedentes", "CARF",
              "Súmulas e Acórdãos Paradigmas do CARF",
              "reguladores/carf", 300, 2, "carf.fazenda.gov.br"),
    ItemPlano("Contabilidade & Precedentes", "Atos Gerais e Resoluções RFB",
              "Portarias, Instruções Normativas e Atos Gerais da RFB",
              "reguladores/rfb/outros-atos", 5000, 2, "normas.receita.fazenda.gov.br"),
]
