"""O plano do acervo tributário e contábil: fontes, escopo e metas de integridade.

Este arquivo é a fonte única da verdade para a medição de progresso e cobertura,
estruturado nos 10 pilares essenciais do Sistema Tributário e Contábil Nacional:
1. Legislação Estruturante & Códigos (CTN, Simples Nacional, PAF, Decretos-Leis)
2. Dividendos, Renda do Capital & IRPJ/CSLL (Lucro Real/Presumido, Offshores, RIR)
3. Folha de Pagamento & Encargos Previdenciários (Custeio, RPS, CPRB, FGTS Digital, RAT/FAP)
4. Produtos, Mercadorias & Indústria (Kandir, CONFAZ, RIPI, PIS/COFINS, Aduana, RICMS 27 UFs)
5. Serviços & Retenções na Fonte (ISSQN LC 116, CSRF 4,65%, IRRF 1,5%, CTMs Capitais)
6. Patrimônio, Herança e Veículos (ITCMD 27 UFs, IPVA 27 UFs, ITR, ITBI, IPTU)
7. Combustíveis e Energia (CIDE, Petróleo, RenovaBio, ICMS Monofásico ad rem LC 192, ANP)
8. Tributação Financeira e IOF (RIOF, Leis 5.143/8.894, Câmbio, Renda Fixa/Variável/Cripto)
9. Reforma Tributária e Transição (EC 132/23, LC 214/25, LC 227/26, Split Payment, Comitê Gestor)
10. Normas Contábeis (CFC NBC TG, CPC 00-48), Jurisprudência e Atos da RFB
"""
from collections import namedtuple
from pathlib import Path
import glob

RAIZ = Path(__file__).resolve().parent.parent

ItemPlano = namedtuple("ItemPlano", "setor pilar nome caminho meta fase fonte")

FASES = {
    1: ("Fase 1 — Legislação Estruturante & Códigos", "CF/88, CTN, Leis Complementares, Ordinárias e Regulamentos Federais"),
    2: ("Fase 2 — Normativos Federais e Regulamentação", "Receita Federal (Sijut), CONFAZ, CFC, CPC, ANP e CGSN"),
    3: ("Fase 3 — Legislação Estadual das 27 UFs", "Regulamentos do ICMS (RICMS), Leis de IPVA e ITCMD das 27 UFs"),
    4: ("Fase 4 — Legislação Municipal", "Códigos Tributários Municipais e Regulamentos do ISS/IPTU/ITBI das Capitais"),
    5: ("Fase 5 — Reforma Tributária & Jurisprudência", "EC 132/23, LC 214/25, LC 227/26, Split Payment, STF/STJ Vinculantes e CARF"),
}

PLANO = [
    # =========================================================================
    # PILAR 1: LEGISLAÇÃO ESTRUTURANTE & CÓDIGOS
    # =========================================================================
    ItemPlano("1. Legislação Estruturante & Códigos", "Código Tributário Nacional",
              "CTN integral (Lei 5.172/1966) e LC 104/2001",
              "federal/leis-complementares/ctn", 2, 1, "normas.leg.br"),
    ItemPlano("1. Legislação Estruturante & Códigos", "Simples Nacional e MEI",
              "Estatuto da Microempresa (LC 123/2006) e Resolução CGSN 140/2018",
              "federal/leis-complementares/simples", 2, 1, "normas.leg.br"),
    ItemPlano("1. Legislação Estruturante & Códigos", "Leis Complementares Gerais",
              "Sigilo Bancário (LC 105), Prescrição (LC 118), MEI (LC 128), Convalidação (LC 160) e Protesto (LC 208)",
              "federal/leis-complementares-gerais", 5, 1, "normas.leg.br"),
    ItemPlano("1. Legislação Estruturante & Códigos", "Decretos-Leis Estruturantes",
              "Delimitação ITR/IPTU (DL 57/66) e Zona Franca de Manaus (DL 288/67)",
              "federal/decretos-leis", 2, 1, "normas.leg.br"),
    ItemPlano("1. Legislação Estruturante & Códigos", "Processo Fiscal, Consulta e CIDE",
              "Processo Administrativo Fiscal (Dec. 70.235/72), Consulta (Dec. 7.574/11) e CIDE (Dec. 5.060/04)",
              "federal/regulamentos/paf_consulta_cide", 3, 1, "normas.leg.br"),

    # =========================================================================
    # PILAR 2: DIVIDENDOS, RENDA DO CAPITAL & IRPJ/CSLL
    # =========================================================================
    ItemPlano("2. Dividendos & Renda do Capital", "Dividendos e JCP",
              "Isenção de Dividendos e JCP (Lei 9.249/95 e Lei das S/A)",
              "federal/leis-ordinarias/dividendos-jcp", 5, 1, "normas.leg.br"),
    ItemPlano("2. Dividendos & Renda do Capital", "Lucro Real e Presumido",
              "Norma Matriz do Lucro Real, IRPJ/CSLL (DL 1.598/77, Leis 7.689/88, 8.981/95, 12.973/14)",
              "federal/leis-ordinarias/irpj-csll", 10, 1, "normas.leg.br"),
    ItemPlano("2. Dividendos & Renda do Capital", "Offshores e Trusts",
              "Tributação de Renda e Controladas no Exterior (Lei 14.754/2023)",
              "federal/leis-ordinarias/offshores", 5, 1, "normas.leg.br"),
    ItemPlano("2. Dividendos & Renda do Capital", "Regulamento do IRPJ (RIR)",
              "Regulamento do Imposto sobre a Renda - RIR/2018 integral (Decreto 9.580/2018)",
              "federal/regulamentos/rir", 1, 1, "normas.leg.br"),

    # =========================================================================
    # PILAR 3: FOLHA DE PAGAMENTO & ENCARGOS PREVIDENCIÁRIOS
    # =========================================================================
    ItemPlano("3. Folha & Encargos", "Custeio da Seguridade",
              "Plano de Custeio da Previdência Social e Benefícios (Leis 8.212/91 e 8.213/91)",
              "federal/leis-ordinarias/previdencia-custeio", 8, 1, "normas.leg.br"),
    ItemPlano("3. Folha & Encargos", "Regulamento da Previdência (RPS)",
              "Regulamento da Previdência Social - RPS (Decreto 3.048/1999)",
              "federal/regulamentos/rps", 1, 1, "normas.leg.br"),
    ItemPlano("3. Folha & Encargos", "IRRF Folha e PLR",
              "Retenção na Fonte sobre Salários, Rescisões e PLR (Lei 10.101/2000 e Tabela Progressiva)",
              "federal/leis-ordinarias/irrf-folha-plr", 5, 1, "normas.leg.br"),
    ItemPlano("3. Folha & Encargos", "Desoneração da Folha (CPRB)",
              "Contribuição Previdenciária sobre a Receita Bruta - CPRB (Lei 12.546/11 e Lei 14.973/24)",
              "federal/leis-ordinarias/cprb", 5, 1, "normas.leg.br"),
    ItemPlano("3. Folha & Encargos", "FGTS e eSocial",
              "Normas do FGTS (Lei 8.036/1990) e Obrigações Trabalhistas",
              "federal/leis-ordinarias/fgts", 3, 1, "normas.leg.br"),
    ItemPlano("3. Folha & Encargos", "FGTS Digital e Operação",
              "Manuais e Portarias do FGTS Digital (Portaria MTE 240/2024) e eSocial",
              "reguladores/mte-caixa/fgts-esocial", 5, 2, "Caixa / MTE"),
    ItemPlano("3. Folha & Encargos", "RAT, FAP e Sistema S",
              "Normas de Riscos Ambientais, FAP e Contribuições a Terceiros",
              "reguladores/rfb/rat-fap-terceiros", 5, 2, "RFB / MPS"),

    # =========================================================================
    # PILAR 4: PRODUTOS, MERCADORIAS & INDÚSTRIA (ICMS, IPI, PIS/COFINS)
    # =========================================================================
    ItemPlano("4. Produtos & Mercadorias", "ICMS e DIFAL",
              "Lei Kandir (LC 87/1996) e Regulamentação do DIFAL (LC 190/2022)",
              "federal/leis-complementares/kandir", 6, 1, "normas.leg.br"),
    ItemPlano("4. Produtos & Mercadorias", "Alíquotas Interestaduais do ICMS",
              "Resoluções do Senado Federal nº 22/1989, 95/1996 e 13/2012",
              "federal/resolucoes-senado/icms", 3, 1, "normas.leg.br"),
    ItemPlano("4. Produtos & Mercadorias", "CONFAZ e ICMS-ST",
              "Convênios ICMS de Substituição Tributária (Convênio 142/18) e Ajustes SINIEF",
              "estaduais/confaz", 61, 2, "confaz.fazenda.gov.br"),
    ItemPlano("4. Produtos & Mercadorias", "IPI e TIPI",
              "Lei do IPI (Lei 4.502/1964), RIPI/2010 integral (Decreto 7.212/2010) e Tabela TIPI",
              "federal/regulamentos/ripi", 5, 1, "normas.leg.br"),
    ItemPlano("4. Produtos & Mercadorias", "PIS/COFINS Monofásico",
              "Regimes Monofásicos de Bebidas, Fármacos e Autopeças (Leis 10.147/00 e 10.485/02)",
              "federal/leis-ordinarias/pis-cofins-monofasico", 5, 1, "normas.leg.br"),
    ItemPlano("4. Produtos & Mercadorias", "Leis Federais Estruturantes",
              "PIS/COFINS Geral (Leis 10.637, 10.833, 9.718), Preços de Transferência (14.596) e Transação (13.988)",
              "federal/leis-ordinarias-estruturantes", 14, 1, "normas.leg.br"),
    ItemPlano("4. Produtos & Mercadorias", "Comércio Exterior e Aduana",
              "Regulamento Aduaneiro consolidado (Decreto 6.759/2009) e Imposto de Importação",
              "federal/regulamentos/aduana", 3, 1, "normas.leg.br"),
    ItemPlano("4. Produtos & Mercadorias", "RICMS Estaduais",
              "Regulamentos do ICMS das 27 Unidades Federativas (Todas as 27 UFs)",
              "estaduais/*/ricms", 36, 3, "Secretarias de Fazenda Estaduais"),

    # =========================================================================
    # PILAR 5: SERVIÇOS & RETENÇÕES NA FONTE (ISSQN, CSRF, IRRF)
    # =========================================================================
    ItemPlano("5. Serviços & Retenções", "ISSQN Geral",
              "Lei Complementar nº 116/2003, LC 157/2016 e LC 175/2020",
              "federal/leis-complementares/iss", 5, 1, "normas.leg.br"),
    ItemPlano("5. Serviços & Retenções", "Retenções Federais na Fonte",
              "Retenção de Serviços e CSRF (Lei 10.833/03)",
              "federal/leis-ordinarias/irrf-servicos", 5, 1, "normas.leg.br"),
    ItemPlano("5. Serviços & Retenções", "CTM e RISS das Capitais",
              "Códigos Tributários Municipais e Regulamentos do ISS (SP, RJ, BH)",
              "municipais/*/servicos-iss", 7, 4, "Câmaras e Prefeituras Municipais"),

    # =========================================================================
    # PILAR 6: PATRIMÔNIO, HERANÇA E VEÍCULOS (ITCMD, IPVA, ITR, ITBI, IPTU)
    # =========================================================================
    ItemPlano("6. Patrimônio & Herança", "ITCMD Federal e Delimitação",
              "Resolução Senado 9/92 (Teto 8%) e Delimitação ITR x IPTU (Decreto-Lei 57/66)",
              "federal/resolucoes-senado/itcmd", 2, 1, "normas.leg.br"),
    ItemPlano("6. Patrimônio & Herança", "ITR Federal",
              "Lei do ITR (Lei 9.393/1996) e Regulamento do ITR (Decreto 4.382/2002)",
              "federal/regulamentos/itr", 3, 1, "normas.leg.br"),
    ItemPlano("6. Patrimônio & Herança", "ITCMD Estadual",
              "Leis Estaduais do ITCMD das 27 Unidades Federativas (Todas as 27 UFs)",
              "estaduais/*/leis/itcmd", 27, 3, "Assembleias Legislativas"),
    ItemPlano("6. Patrimônio & Herança", "IPVA Estadual",
              "Leis Estaduais do IPVA das 27 Unidades Federativas (Todas as 27 UFs)",
              "estaduais/*/leis/ipva", 27, 3, "Assembleias Legislativas"),
    ItemPlano("6. Patrimônio & Herança", "ITBI Municipal",
              "Leis Municipais do ITBI das Capitais (SP, RJ, BH)",
              "municipais/*/leis/itbi", 3, 4, "Câmaras Municipais"),
    ItemPlano("6. Patrimônio & Herança", "IPTU Municipal",
              "Leis do IPTU e Plantas Genéricas de Valores das Capitais (SP, RJ, BH)",
              "municipais/*/leis/iptu", 3, 4, "Câmaras Municipais"),

    # =========================================================================
    # PILAR 7: COMBUSTÍVEIS E ENERGIA
    # =========================================================================
    ItemPlano("7. Combustíveis e Energia", "CIDE e Lei do Petróleo",
              "CIDE-Combustíveis (Lei 10.336/01, Dec. 5.060/04), Petróleo (Lei 9.478/97) e Combustíveis do Futuro",
              "federal/leis-ordinarias/combustiveis", 8, 1, "normas.leg.br"),
    ItemPlano("7. Combustíveis e Energia", "ICMS Monofásico ad rem",
              "Regime Monofásico Uniforme Nacional de Combustíveis (LC 192/2022)",
              "federal/leis-complementares/combustiveis", 2, 1, "normas.leg.br"),
    ItemPlano("7. Combustíveis e Energia", "Regulação ANP e Setorial",
              "Resoluções da Agência Nacional do Petróleo sobre Controle Fiscal (Res. 795, 858 e 948)",
              "reguladores/anp/resolucoes", 3, 2, "atosoficiais.com.br/anp"),

    # =========================================================================
    # PILAR 8: TRIBUTAÇÃO FINANCEIRA E IOF
    # =========================================================================
    ItemPlano("8. Financeiro e IOF", "Regulamento do IOF (RIOF)",
              "Regulamento do IOF - RIOF integral (Decreto 6.306/2007)",
              "federal/regulamentos/iof", 1, 1, "normas.leg.br"),
    ItemPlano("8. Financeiro e IOF", "Leis Matrizes do IOF",
              "Leis do IOF sobre Crédito, Câmbio e Títulos (Leis 5.143/66 e 8.894/94)",
              "federal/leis-ordinarias/iof", 2, 1, "normas.leg.br"),
    ItemPlano("8. Financeiro e IOF", "IOF-Câmbio e OCDE",
              "Portaria MF nº 204/2022 (Cronograma de redução das alíquotas do IOF-Câmbio)",
              "federal/portarias/mf", 3, 1, "normas.leg.br"),
    ItemPlano("8. Financeiro e IOF", "Mercados Financeiro e de Capitais",
              "Tributação de Renda Fixa, Renda Variável, Derivativos e Criptoativos",
              "reguladores/rfb/instrucoes-normativas/financeiro", 5, 2, "normas.receita.fazenda.gov.br"),

    # =========================================================================
    # PILAR 9: REFORMA TRIBUTÁRIA E TRANSIÇÃO
    # =========================================================================
    ItemPlano("9. Reforma Tributária", "Marco Constitucional e Leis Complementares",
              "Emenda Constitucional nº 132/2023, LC 214/2025, LC 227/2026, PLP 68, PLP 108 e Split Payment",
              "reforma-tributaria", 8, 5, "Congresso Nacional / LexML"),

    # =========================================================================
    # PILAR 10: NORMAS CONTÁBEIS (CPC E CFC) E ATOS REGULATÓRIOS DA RFB
    # =========================================================================
    ItemPlano("10. Contabilidade e Precedentes", "Normas Brasileiras de Contabilidade (CFC)",
              "Resoluções e Normas Técnicas Gerais do CFC (NBC TG 01 a 48, 1000, ITG 19 e Estrutura Conceitual)",
              "contabil/cfc", 48, 2, "cfc.org.br"),
    ItemPlano("10. Contabilidade e Precedentes", "Pronunciamentos Técnicos CPC",
              "Pronunciamentos Técnicos do Comitê de Pronunciamentos Contábeis (CPC 00 a 48)",
              "contabil/cpc", 48, 2, "cpc.org.br"),
    ItemPlano("10. Contabilidade e Precedentes", "Precedentes Vinculantes STF / STJ",
              "Súmulas Vinculantes, Temas de Repercussão Geral e Recursos Repetitivos (SV 8, 29, 31, 48, 50, 57, Temas STF/STJ)",
              "jurisprudencia/precedentes-vinculantes", 19, 5, "STF / STJ"),
    ItemPlano("10. Contabilidade e Precedentes", "Súmulas do CARF",
              "Súmulas e Enunciados Vinculantes do Conselho Administrativo de Recursos Fiscais",
              "reguladores/carf/sumulas", 10, 2, "carf.fazenda.gov.br"),
    ItemPlano("10. Contabilidade e Precedentes", "Instruções Normativas da RFB (Gerais)",
              "Instruções Normativas vigentes estruturantes da Receita Federal (exceto financeiro)",
              "reguladores/rfb/instrucoes-normativas-gerais", 94, 2, "normas.receita.fazenda.gov.br"),
    ItemPlano("10. Contabilidade e Precedentes", "Atos Executivos e Soluções de Consulta",
              "Soluções de Consulta COSIT/DISIT, Portarias e Atos Declaratórios da RFB",
              "reguladores/rfb/outros-atos", 613, 2, "normas.receita.fazenda.gov.br"),
]

def resolver_arquivos(caminho_relativo: str) -> set[Path]:
    """Resolve os arquivos Markdown correspondentes ao caminho do plano com precisão e sem sobreposições."""
    if caminho_relativo == "reguladores/rfb/instrucoes-normativas-gerais":
        todos = set(Path(f).resolve() for f in glob.glob(str(RAIZ / "reguladores/rfb/instrucoes-normativas/**/*.md"), recursive=True))
        fin = set(Path(f).resolve() for f in glob.glob(str(RAIZ / "reguladores/rfb/instrucoes-normativas/financeiro/**/*.md"), recursive=True))
        return todos - fin
    elif caminho_relativo == "federal/leis-ordinarias-estruturantes":
        return set(Path(f).resolve() for f in (RAIZ / "federal" / "leis-ordinarias").glob("*.md"))
    elif caminho_relativo == "federal/leis-complementares-gerais":
        return set(Path(f).resolve() for f in (RAIZ / "federal" / "leis-complementares").glob("*.md"))
    elif caminho_relativo == "federal/regulamentos/paf_consulta_cide":
        paf = set(Path(f).resolve() for f in glob.glob(str(RAIZ / "federal/regulamentos/paf/**/*.md"), recursive=True))
        consulta = set(Path(f).resolve() for f in glob.glob(str(RAIZ / "federal/regulamentos/consulta/**/*.md"), recursive=True))
        cide = set(Path(f).resolve() for f in glob.glob(str(RAIZ / "federal/regulamentos/cide/**/*.md"), recursive=True))
        return paf | consulta | cide
    elif caminho_relativo == "federal/regulamentos/itr":
        reg_itr = set(Path(f).resolve() for f in glob.glob(str(RAIZ / "federal/regulamentos/itr/**/*.md"), recursive=True))
        lei_itr = set(Path(f).resolve() for f in glob.glob(str(RAIZ / "federal/leis-ordinarias/itr/**/*.md"), recursive=True))
        return reg_itr | lei_itr
    elif "*" in caminho_relativo:
        return set(Path(f).resolve() for f in glob.glob(str(RAIZ / caminho_relativo / "**/*.md"), recursive=True))
    else:
        p = RAIZ / caminho_relativo
        if p.is_file() and p.suffix == ".md":
            return {p.resolve()}
        return set(Path(f).resolve() for f in glob.glob(str(p / "**/*.md"), recursive=True))

def contar_documentos(caminho_relativo: str) -> int:
    """Retorna o número de documentos resolvidos para o item."""
    return len(resolver_arquivos(caminho_relativo))
