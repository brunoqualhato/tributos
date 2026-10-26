"""O plano do acervo tributário e contábil: fontes, escopo e metas de integridade.

Este arquivo é a fonte única da verdade para a medição de progresso e cobertura,
estruturado nos 9 pilares essenciais do Sistema Tributário Nacional:
1. Dividendos, Renda do Capital & IRPJ/CSLL
2. Folha de Pagamento & Encargos Previdenciários
3. Produtos, Mercadorias & Indústria (ICMS, IPI, PIS/COFINS Monofásico)
4. Serviços & Retenções na Fonte (ISSQN, CSRF 4,65%, IRRF 1,5%)
5. Patrimônio, Herança e Veículos (ITCMD, IPVA, ITR, ITBI, IPTU)
6. Combustíveis e Energia (CIDE, Petróleo, RenovaBio, ICMS Monofásico ad rem)
7. Tributação Financeira e IOF (RIOF, Renda Fixa/Variável, Cripto, Fundos)
8. Reforma Tributária e Transição (IBS, CBS, Imposto Seletivo, Split Payment)
9. Normas Contábeis (CPC e CFC) e Atos Regulatórios da RFB
"""
from collections import namedtuple

ItemPlano = namedtuple("ItemPlano", "setor pilar nome caminho meta fase fonte")

FASES = {
    1: ("Fase 1 — Legislação Estruturante & Códigos", "CF/88, CTN, Leis Complementares e Regulamentos Federais"),
    2: ("Fase 2 — Normativos Federais e Regulamentação", "Receita Federal (Sijut), CONFAZ, CFC, CPC, ANP e CGSN"),
    3: ("Fase 3 — Legislação Estadual das 27 UFs", "Regulamentos do ICMS (RICMS), Leis de IPVA e ITCMD das 27 UFs"),
    4: ("Fase 4 — Legislação Municipal", "Códigos Tributários Municipais e Regulamentos do ISS/IPTU/ITBI das Capitais"),
    5: ("Fase 5 — Reforma Tributária & Transição", "EC 132/23, PLP 68/24, PLP 108/24, Split Payment e Comitê Gestor"),
}

PLANO = [
    # =========================================================================
    # PILAR 1: DIVIDENDOS, RENDA DO CAPITAL & IRPJ/CSLL
    # =========================================================================
    ItemPlano("1. Dividendos & Renda do Capital", "Dividendos e JCP",
              "Isenção de Dividendos e Juros sobre Capital Próprio (Lei 9.249/95 e LSA)",
              "federal/leis-ordinarias/dividendos-jcp", 5, 1, "normas.leg.br"),
    ItemPlano("1. Dividendos & Renda do Capital", "Lucro Real e Presumido",
              "Norma Matriz do Lucro Real, IRPJ/CSLL (DL 1.598/77, Leis 7.689/88, 8.981/95, 12.973/14)",
              "federal/leis-ordinarias/irpj-csll", 10, 1, "normas.leg.br"),
    ItemPlano("1. Dividendos & Renda do Capital", "Offshores e Trusts",
              "Tributação de Renda e Controladas no Exterior (Lei 14.754/2023)",
              "federal/leis-ordinarias/offshores", 5, 1, "normas.leg.br"),
    ItemPlano("1. Dividendos & Renda do Capital", "Regulamento do IRPJ (RIR)",
              "Regulamento do Imposto sobre a Renda - RIR/2018 integral (Decreto 9.580/2018)",
              "federal/regulamentos/rir", 1, 1, "normas.leg.br"),

    # =========================================================================
    # PILAR 2: FOLHA DE PAGAMENTO & ENCARGOS PREVIDENCIÁRIOS
    # =========================================================================
    ItemPlano("2. Folha & Encargos", "Custeio da Seguridade",
              "Plano de Custeio da Previdência Social e Benefícios (Leis 8.212/91 e 8.213/91)",
              "federal/leis-ordinarias/previdencia-custeio", 8, 1, "normas.leg.br"),
    ItemPlano("2. Folha & Encargos", "Regulamento da Previdência (RPS)",
              "Regulamento da Previdência Social - RPS (Decreto 3.048/1999)",
              "federal/regulamentos/rps", 1, 1, "normas.leg.br"),
    ItemPlano("2. Folha & Encargos", "IRRF Folha e PLR",
              "Retenção na Fonte sobre Salários, Rescisões e PLR (Lei 10.101/2000 e Tabela Progressiva)",
              "federal/leis-ordinarias/irrf-folha-plr", 5, 1, "normas.leg.br"),
    ItemPlano("2. Folha & Encargos", "Desoneração da Folha (CPRB)",
              "Contribuição Previdenciária sobre a Receita Bruta - CPRB (Lei 12.546/11 e Lei 14.973/24)",
              "federal/leis-ordinarias/cprb", 5, 1, "normas.leg.br"),
    ItemPlano("2. Folha & Encargos", "FGTS e eSocial",
              "Normas do FGTS (Lei 8.036/1990) e Obrigações Trabalhistas",
              "federal/leis-ordinarias/fgts", 3, 1, "normas.leg.br"),
    ItemPlano("2. Folha & Encargos", "FGTS Digital e Operação",
              "Manuais e Circulares do FGTS Digital e eSocial",
              "reguladores/mte-caixa/fgts-esocial", 5, 2, "Caixa / MTE"),
    ItemPlano("2. Folha & Encargos", "RAT, FAP e Sistema S",
              "Normas de Riscos Ambientais, FAP e Contribuições a Terceiros",
              "reguladores/rfb/rat-fap-terceiros", 5, 2, "RFB / MPS"),

    # =========================================================================
    # PILAR 3: PRODUTOS, MERCADORIAS & INDÚSTRIA (ICMS, IPI, PIS/COFINS)
    # =========================================================================
    ItemPlano("3. Produtos & Mercadorias", "ICMS e DIFAL",
              "Lei Kandir (LC 87/1996) e Regulamentação do DIFAL (LC 190/2022)",
              "federal/leis-complementares/kandir", 3, 1, "normas.leg.br"),
    ItemPlano("3. Produtos & Mercadorias", "CONFAZ e ICMS-ST",
              "Convênios ICMS de Substituição Tributária (Convênio 142/18) e Ajustes SINIEF",
              "estaduais/confaz", 30, 2, "confaz.fazenda.gov.br"),
    ItemPlano("3. Produtos & Mercadorias", "IPI e TIPI",
              "Lei do IPI (Lei 4.502/1964), RIPI/2010 integral (Decreto 7.212/2010) e Tabela TIPI",
              "federal/regulamentos/ripi", 5, 1, "normas.leg.br"),
    ItemPlano("3. Produtos & Mercadorias", "PIS/COFINS Monofásico",
              "Regimes Monofásicos de Bebidas, Fármacos e Autopeças (Leis 10.147/00 e 10.485/02)",
              "federal/leis-ordinarias/pis-cofins-monofasico", 5, 1, "normas.leg.br"),
    ItemPlano("3. Produtos & Mercadorias", "Comércio Exterior e Aduana",
              "Regulamento Aduaneiro consolidado (Decreto 6.759/2009) e Imposto de Importação",
              "federal/regulamentos/aduana", 3, 1, "normas.leg.br"),
    ItemPlano("3. Produtos & Mercadorias", "RICMS Estaduais",
              "Regulamentos do ICMS das 27 Unidades Federativas (Todas as 27 UFs)",
              "estaduais/*/ricms", 27, 3, "Secretarias de Fazenda Estaduais"),

    # =========================================================================
    # PILAR 4: SERVIÇOS & RETENÇÕES NA FONTE (ISSQN, CSRF 4,65%, IRRF)
    # =========================================================================
    ItemPlano("4. Serviços & Retenções", "ISSQN Geral",
              "Lei Complementar nº 116/2003, LC 157/2016 e LC 175/2020",
              "federal/leis-complementares/iss", 5, 1, "normas.leg.br"),
    ItemPlano("4. Serviços & Retenções", "Retenções Federais na Fonte",
              "Retenção de Serviços e CSRF (Lei 10.833/03)",
              "federal/leis-ordinarias/irrf-servicos", 5, 1, "normas.leg.br"),
    ItemPlano("4. Serviços & Retenções", "CTM e RISS das Capitais",
              "Códigos Tributários Municipais e Regulamentos do ISS (SP, RJ, BH)",
              "municipais/*/servicos-iss", 15, 4, "Câmaras e Prefeituras Municipais"),

    # =========================================================================
    # PILAR 5: PATRIMÔNIO, HERANÇA E VEÍCULOS (ITCMD, IPVA, ITR, ITBI, IPTU)
    # =========================================================================
    ItemPlano("5. Patrimônio & Herança", "ITCMD Federal e Delimitação",
              "Resolução Senado 9/92 (Teto 8%) e Delimitação ITR x IPTU (Decreto-Lei 57/66)",
              "federal/resolucoes-senado/itcmd", 2, 1, "normas.leg.br"),
    ItemPlano("5. Patrimônio & Herança", "ITR Federal",
              "Lei do ITR (Lei 9.393/1996) e Regulamento do ITR (Decreto 4.382/2002)",
              "federal/regulamentos/itr", 2, 1, "normas.leg.br"),
    ItemPlano("5. Patrimônio & Herança", "ITCMD Estadual",
              "Leis Estaduais do ITCMD das 27 Unidades Federativas (Todas as 27 UFs)",
              "estaduais/*/leis/itcmd", 27, 3, "Assembleias Legislativas"),
    ItemPlano("5. Patrimônio & Herança", "IPVA Estadual",
              "Leis Estaduais do IPVA das 27 Unidades Federativas (Todas as 27 UFs)",
              "estaduais/*/leis/ipva", 27, 3, "Assembleias Legislativas"),
    ItemPlano("5. Patrimônio & Herança", "ITBI Municipal",
              "Leis Municipais do ITBI das Capitais (SP, RJ, BH)",
              "municipais/*/leis/itbi", 8, 4, "Câmaras Municipais"),
    ItemPlano("5. Patrimônio & Herança", "IPTU Municipal",
              "Leis do IPTU e Plantas Genéricas de Valores das Capitais",
              "municipais/*/leis/iptu", 5, 4, "Câmaras Municipais"),

    # =========================================================================
    # PILAR 6: COMBUSTÍVEIS E ENERGIA
    # =========================================================================
    ItemPlano("6. Combustíveis e Energia", "CIDE e Lei do Petróleo",
              "CIDE-Combustíveis (Lei 10.336/01 e Dec. 5.060/04) e Lei do Petróleo (Lei 9.478/97)",
              "federal/leis-ordinarias/combustiveis", 8, 1, "normas.leg.br"),
    ItemPlano("6. Combustíveis e Energia", "ICMS Monofásico ad rem",
              "Regime Monofásico Uniforme Nacional de Combustíveis (LC 192/2022)",
              "federal/leis-complementares/combustiveis", 2, 1, "normas.leg.br"),
    ItemPlano("6. Combustíveis e Energia", "Regulação ANP e Setorial",
              "Resoluções da Agência Nacional do Petróleo sobre Controle Fiscal",
              "reguladores/anp/resolucoes", 3, 2, "anp.gov.br"),

    # =========================================================================
    # PILAR 7: TRIBUTAÇÃO FINANCEIRA E IOF
    # =========================================================================
    ItemPlano("7. Financeiro e IOF", "Regulamento do IOF (RIOF)",
              "Regulamento do IOF - RIOF integral (Decreto 6.306/2007)",
              "federal/regulamentos/iof", 1, 1, "normas.leg.br"),
    ItemPlano("7. Financeiro e IOF", "Leis Matrizes do IOF",
              "Leis do IOF sobre Crédito, Câmbio e Títulos (Leis 5.143/66 e 8.894/94)",
              "federal/leis-ordinarias/iof", 2, 1, "normas.leg.br"),
    ItemPlano("7. Financeiro e IOF", "IOF-Câmbio e OCDE",
              "Portaria MF nº 204/2022 (Cronograma de redução das alíquotas do IOF-Câmbio)",
              "federal/portarias/mf", 3, 1, "normas.leg.br"),
    ItemPlano("7. Financeiro e IOF", "Mercados Financeiro e de Capitais",
              "Tributação de Renda Fixa, Renda Variável, Derivativos e Criptoativos",
              "reguladores/rfb/instrucoes-normativas/financeiro", 5, 2, "normas.receita.fazenda.gov.br"),

    # =========================================================================
    # PILAR 8: REFORMA TRIBUTÁRIA E TRANSIÇÃO
    # =========================================================================
    ItemPlano("8. Reforma Tributária", "Marco Constitucional e Leis Complementares",
              "Emenda Constitucional nº 132/2023, PLP 68/2024 e PLP 108/2024",
              "reforma-tributaria", 8, 5, "Congresso Nacional"),

    # =========================================================================
    # PILAR 9: NORMAS CONTÁBEIS (CPC E CFC) E ATOS REGULATÓRIOS DA RFB
    # =========================================================================
    ItemPlano("9. Contabilidade e Precedentes", "Normas Brasileiras de Contabilidade (CFC)",
              "Resoluções e Normas Técnicas Gerais do CFC (NBC TG)",
              "contabil/cfc", 20, 2, "cfc.org.br"),
    ItemPlano("9. Contabilidade e Precedentes", "Pronunciamentos Técnicos CPC",
              "Pronunciamentos Técnicos do Comitê de Pronunciamentos Contábeis (CPC 00 a 48)",
              "contabil/cpc", 25, 2, "cpc.org.br"),
    ItemPlano("9. Contabilidade e Precedentes", "Precedentes Vinculantes STF / STJ",
              "Súmulas Vinculantes, Temas de Repercussão Geral e Recursos Repetitivos",
              "jurisprudencia/precedentes-vinculantes", 10, 5, "STF / STJ"),
    ItemPlano("9. Contabilidade e Precedentes", "Súmulas do CARF",
              "Súmulas e Enunciados Vinculantes do Conselho Administrativo de Recursos Fiscais",
              "reguladores/carf/sumulas", 10, 2, "carf.fazenda.gov.br"),
    ItemPlano("9. Contabilidade e Precedentes", "Instruções Normativas da RFB",
              "Instruções Normativas vigentes estruturantes da Receita Federal",
              "reguladores/rfb/instrucoes-normativas", 90, 2, "normas.receita.fazenda.gov.br"),
    ItemPlano("9. Contabilidade e Precedentes", "Atos Executivos e Soluções de Consulta",
              "Soluções de Consulta COSIT/DISIT, Portarias e Atos Declaratórios",
              "reguladores/rfb/outros-atos", 500, 2, "normas.receita.fazenda.gov.br"),
]
