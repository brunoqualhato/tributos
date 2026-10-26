"""Agente Especialista em Web Scraping Tributário e Contábil.

Responsável pela captura em portais oficiais sem API REST:
- CONFAZ (Convênios ICMS e Ajustes SINIEF)
- CFC (Conselho Federal de Contabilidade - NBC TG)
- CPC (Comitê de Pronunciamentos Contábeis)
- Planalto (CF/88, CTN, Leis Complementares, Decretos)

Regras Operacionais:
1. Respeitar limites de requisições por segundo (rate limit de 1 a 3 rps por domínio).
2. Salvar sempre o conteúdo original bruto compactado em `_fonte/scraping/<orgao>/<hash>.html.gz` ou `.pdf.gz`.
3. Garantir idempotência: verificar o cache local antes de disparar requisições HTTP redundantes.
4. Converter PDFs em texto limpo com o utilitário nativo compilado `scripts/bin/extrair_pdf`.
"""
from pathlib import Path
import datetime as dt
import hashlib
import gzip
import re
import subprocess
import sys
import time

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from comum import Rede, salvar_atomico, gerar_frontmatter
from html2md import converter_html_para_md

# =====================================================================
# METADADOS DE NORMAS DO CPC (Comitê de Pronunciamentos Contábeis)
# =====================================================================
NORMAS_CPC = [
    {
        "num": "00",
        "ano": "2019",
        "data": "2019-11-21",
        "titulo": "Pronunciamento Técnico CPC 00 (R2) - Estrutura Conceitual para Relatório Financeiro",
        "url": "http://www.cpc.org.br/Arquivos/Documentos/573_CPC00(R2).pdf",
        "ementa": "Define a Estrutura Conceitual para Relatório Financeiro (Conceptual Framework), estabelecendo os conceitos fundamentais para a elaboração e apresentação das demonstrações contábeis.",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Contabilidade Societária e Fiscal"],
    },
    {
        "num": "02",
        "ano": "2010",
        "data": "2010-09-03",
        "titulo": "Pronunciamento Técnico CPC 02 (R2) - Efeitos das Mudanças nas Taxas de Câmbio e Conversão de Demonstrações Contábeis",
        "url": "http://www.cpc.org.br/Arquivos/Documentos/62_CPC_02_R2_rev%2027_ComAVISO.pdf",
        "ementa": "Prescreve como incluir transações em moeda estrangeira e operações no exterior nas demonstrações contábeis e como converter demonstrações para moeda de apresentação.",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "Variação Cambial"],
    },
    {
        "num": "03",
        "ano": "2010",
        "data": "2010-09-03",
        "titulo": "Pronunciamento Técnico CPC 03 (R2) - Demonstração dos Fluxos de Caixa (DFC)",
        "url": "http://www.cpc.org.br/Arquivos/Documentos/183_CPC_03_R2_rev%2024.pdf",
        "ementa": "Requer o fornecimento de informações sobre as alterações históricas de caixa e equivalentes de caixa da entidade por meio de Demonstração dos Fluxos de Caixa (DFC).",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Contabilidade Societária e Fiscal"],
    },
    {
        "num": "04",
        "ano": "2010",
        "data": "2010-10-01",
        "titulo": "Pronunciamento Técnico CPC 04 (R1) - Ativo Intangível",
        "url": "http://www.cpc.org.br/Arquivos/Documentos/187_CPC_04_R1_rev%2021.pdf",
        "ementa": "Define o tratamento contábil de ativos intangíveis, incluindo critérios de reconhecimento, mensuração, amortização e apuração de ágio por rentabilidade futura (goodwill).",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "Ágio"],
    },
    {
        "num": "06",
        "ano": "2018",
        "data": "2018-12-21",
        "titulo": "Pronunciamento Técnico CPC 06 (R2) - Operações de Arrendamento Mercantil (IFRS 16)",
        "url": "http://www.cpc.org.br/Arquivos/Documentos/533_CPC_06_R2_rev%2023.pdf",
        "ementa": "Estabelece os princípios para o reconhecimento, mensuração, apresentação e divulgação de arrendamentos mercantis (leasing) para locatários e locadores.",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["PIS/Pasep", "Cofins", "IRPJ", "CSLL"],
    },
    {
        "num": "16",
        "ano": "2009",
        "data": "2009-05-29",
        "titulo": "Pronunciamento Técnico CPC 16 (R1) - Estoques",
        "url": "http://www.cpc.org.br/Arquivos/Documentos/243_CPC_16_R1_rev%2013_ComAVISO.pdf",
        "ementa": "Estabelece o tratamento contábil para estoques, determinando os critérios de valoração, custo de aquisição e dedução de tributos recuperáveis (ICMS, IPI, PIS/COFINS).",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "IPI", "PIS/Pasep", "Cofins"],
    },
    {
        "num": "18",
        "ano": "2012",
        "data": "2012-12-07",
        "titulo": "Pronunciamento Técnico CPC 18 (R3) - Investimento em Coligada, em Controlada e em Empreendimento Controlado em Conjunto",
        "url": "http://www.cpc.org.br/Arquivos/Documentos/650_CPC_18R3.pdf",
        "ementa": "Prescreve a aplicação do Método de Equivalência Patrimonial (MEP) na contabilização de investimentos em entidades coligadas e controladas e seus reflexos fiscais.",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "Equivalência Patrimonial"],
    },
    {
        "num": "20",
        "ano": "2011",
        "data": "2011-12-02",
        "titulo": "Pronunciamento Técnico CPC 20 (R1) - Custos de Empréstimos",
        "url": "http://www.cpc.org.br/Arquivos/Documentos/281_CPC_20_R1_rev%2022.pdf",
        "ementa": "Estabelece o tratamento contábil aplicável aos custos de empréstimos e financiamentos diretamente atribuíveis à aquisição, construção ou produção de ativo qualificável.",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "Juros sobre Capital"],
    },
    {
        "num": "25",
        "ano": "2009",
        "data": "2009-10-30",
        "titulo": "Pronunciamento Técnico CPC 25 - Provisões, Passivos Contingentes e Ativos Contingentes",
        "url": "http://www.cpc.org.br/Arquivos/Documentos/304_CPC_25_rev%2019.pdf",
        "ementa": "Define critérios de reconhecimento e bases de mensuração para provisões contábeis, passivos contingentes e contingências fiscais e judiciais.",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["IRPJ", "CSLL", "Provisões Fiscais"],
    },
    {
        "num": "27",
        "ano": "2009",
        "data": "2009-07-28",
        "titulo": "Pronunciamento Técnico CPC 27 - Ativo Imobilizado",
        "url": "http://www.cpc.org.br/Arquivos/Documentos/316_CPC_27_rev%2022.pdf",
        "ementa": "Estabelece o tratamento contábil para ativos imobilizados, incluindo taxas de depreciação, vida útil econômica e conciliação com a depreciação fiscal do RIR.",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["IRPJ", "CSLL", "Depreciação Acelerada"],
    },
    {
        "num": "47",
        "ano": "2016",
        "data": "2016-11-04",
        "titulo": "Pronunciamento Técnico CPC 47 - Receita de Contrato com Cliente (IFRS 15)",
        "url": "http://www.cpc.org.br/Arquivos/Documentos/527_CPC_47_Rev%2021.pdf",
        "ementa": "Estabelece o modelo de cinco etapas para reconhecimento de receita proveniente de contratos com clientes e sua correlação com a apuração de PIS, COFINS e ISS.",
        "tema": "Serviços e Retenções",
        "tributos": ["PIS/Pasep", "Cofins", "ISS"],
    },
    {
        "num": "48",
        "ano": "2016",
        "data": "2016-12-09",
        "titulo": "Pronunciamento Técnico CPC 48 - Instrumentos Financeiros (IFRS 9)",
        "url": "http://www.cpc.org.br/Arquivos/Documentos/530_CPC_48_rev_19.pdf",
        "ementa": "Estabelece princípios para o reconhecimento, classificação, mensuração e perdas esperadas de instrumentos financeiros e operações de hedge contábil.",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRRF", "IOF", "IRPJ", "CSLL"],
    },
]

# =====================================================================
# METADADOS DE NORMAS DO CFC (Conselho Federal de Contabilidade - NBC TG)
# =====================================================================
NORMAS_CFC = [
    {
        "num": "EC",
        "ano": "2019",
        "data": "2019-11-21",
        "codigo_cfc": "NBC TG ESTRUTURA CONCEITUAL",
        "titulo": "NBC TG ESTRUTURA CONCEITUAL - Estrutura Conceitual para Relatório Financeiro",
        "url": "https://www1.cfc.org.br/sisweb/SRE/docs/NBCTGEC.pdf",
        "ementa": "Dá nova redação à NBC TG ESTRUTURA CONCEITUAL, que dispõe sobre a estrutura conceitual para relatório financeiro elaborada pelo Conselho Federal de Contabilidade.",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Contabilidade Societária e Fiscal"],
    },
    {
        "num": "01",
        "ano": "2017",
        "data": "2017-12-22",
        "codigo_cfc": "NBC TG 01 (R4)",
        "titulo": "NBC TG 01 (R4) - Redução ao Valor Recuperável de Ativos (Impairment)",
        "url": "https://www1.cfc.org.br/sisweb/SRE/docs/NBCTG01(R4).pdf",
        "ementa": "Estabelece procedimentos para garantir que os ativos de uma entidade não estejam registrados por valor superior ao recuperável (impairment test).",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Contabilidade Societária e Fiscal"],
    },
    {
        "num": "02",
        "ano": "2017",
        "data": "2017-12-22",
        "codigo_cfc": "NBC TG 02 (R3)",
        "titulo": "NBC TG 02 (R3) - Efeitos das Mudanças nas Taxas de Câmbio e Conversão de Demonstrações Contábeis",
        "url": "https://www1.cfc.org.br/sisweb/SRE/docs/NBCTG02(R3).pdf",
        "ementa": "Prescreve o tratamento contábil de transações em moeda estrangeira e a conversão de demonstrações contábeis para moeda funcional e de apresentação.",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "Variação Cambial"],
    },
    {
        "num": "03",
        "ano": "2016",
        "data": "2016-12-09",
        "codigo_cfc": "NBC TG 03 (R3)",
        "titulo": "NBC TG 03 (R3) - Demonstração dos Fluxos de Caixa (DFC)",
        "url": "https://www1.cfc.org.br/sisweb/SRE/docs/NBCTG03(R3).pdf",
        "ementa": "Dispõe sobre a apresentação das informações relativas aos fluxos de caixa operacionais, de investimento e de financiamento.",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Contabilidade Societária e Fiscal"],
    },
    {
        "num": "04",
        "ano": "2017",
        "data": "2017-12-22",
        "codigo_cfc": "NBC TG 04 (R4)",
        "titulo": "NBC TG 04 (R4) - Ativo Intangível",
        "url": "https://www1.cfc.org.br/sisweb/SRE/docs/NBCTG04(R4).pdf",
        "ementa": "Estabelece critérios contábeis para o reconhecimento e mensuração de ativos intangíveis e tratamento do ágio por expectativa de rentabilidade futura (goodwill).",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "Ágio"],
    },
    {
        "num": "06",
        "ano": "2017",
        "data": "2017-12-22",
        "codigo_cfc": "NBC TG 06 (R3)",
        "titulo": "NBC TG 06 (R3) - Operações de Arrendamento Mercantil (IFRS 16)",
        "url": "https://www1.cfc.org.br/sisweb/SRE/docs/NBCTG06(R3).pdf",
        "ementa": "Dispõe sobre o tratamento contábil dos contratos de arrendamento mercantil (leasing) sob a ótica do ativo de direito de uso e passivo de arrendamento.",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["PIS/Pasep", "Cofins", "IRPJ", "CSLL"],
    },
    {
        "num": "16",
        "ano": "2017",
        "data": "2017-12-22",
        "codigo_cfc": "NBC TG 16 (R2)",
        "titulo": "NBC TG 16 (R2) - Estoques",
        "url": "https://www1.cfc.org.br/sisweb/SRE/docs/NBCTG16(R2).pdf",
        "ementa": "Estabelece os critérios de mensuração e reconhecimento de estoques ao menor valor entre o custo e o valor realizável líquido.",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "IPI", "PIS/Pasep", "Cofins"],
    },
    {
        "num": "18",
        "ano": "2024",
        "data": "2024-11-21",
        "codigo_cfc": "NBC TG 18 (R4)",
        "titulo": "NBC TG 18 (R4) - Investimento em Coligada, em Controlada e em Empreendimento Controlado em Conjunto",
        "url": "https://www1.cfc.org.br/sisweb/SRE/docs/NBCTG18(R4).pdf",
        "ementa": "Dispõe sobre os requisitos para aplicação do método de equivalência patrimonial em investimentos societários coligados e controlados.",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "Equivalência Patrimonial"],
    },
    {
        "num": "20",
        "ano": "2017",
        "data": "2017-12-22",
        "codigo_cfc": "NBC TG 20 (R2)",
        "titulo": "NBC TG 20 (R2) - Custos de Empréstimos",
        "url": "https://www1.cfc.org.br/sisweb/SRE/docs/NBCTG20(R2).pdf",
        "ementa": "Estabelece o tratamento contábil e as condições de capitalização dos encargos financeiros decorrentes de empréstimos em ativos qualificáveis.",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL"],
    },
    {
        "num": "25",
        "ano": "2017",
        "data": "2017-12-22",
        "codigo_cfc": "NBC TG 25 (R2)",
        "titulo": "NBC TG 25 (R2) - Provisões, Passivos Contingentes e Ativos Contingentes",
        "url": "https://www1.cfc.org.br/sisweb/SRE/docs/NBCTG25(R2).pdf",
        "ementa": "Define regras para o reconhecimento e quantificação de provisões financeiras e divulgação de contingências tributárias, trabalhistas e cíveis.",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["IRPJ", "CSLL", "Provisões Fiscais"],
    },
    {
        "num": "27",
        "ano": "2017",
        "data": "2017-12-22",
        "codigo_cfc": "NBC TG 27 (R4)",
        "titulo": "NBC TG 27 (R4) - Ativo Imobilizado",
        "url": "https://www1.cfc.org.br/sisweb/SRE/docs/NBCTG27(R4)_rev18.pdf",
        "ementa": "Prescreve o tratamento contábil dos itens que compõem o ativo imobilizado, critérios de depreciação, valor residual e baixa patrimonial.",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["IRPJ", "CSLL", "Depreciação"],
    },
]

# =====================================================================
# METADADOS DE NORMAS DO CONFAZ (Convênios ICMS e Ajustes SINIEF)
# =====================================================================
NORMAS_CONFAZ = [
    {
        "tipo": "Convênio ICMS",
        "subpasta": "convenios-icms",
        "prefixo_arquivo": "convenio-icms",
        "num": "142",
        "ano": "2018",
        "data": "2018-12-14",
        "titulo": "Convênio ICMS nº 142, de 14 de dezembro de 2018 (ICMS Substituição Tributária)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2018/CV142_18",
        "ementa": "Dispõe sobre os regimes de substituição tributária e de antecipação de recolhimento do ICMS com encerramento de tributação relativos às operações subsequentes.",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "ICMS-ST", "MVA"],
    },
    {
        "tipo": "Convênio ICMS",
        "subpasta": "convenios-icms",
        "prefixo_arquivo": "convenio-icms",
        "num": "190",
        "ano": "2017",
        "data": "2017-12-15",
        "titulo": "Convênio ICMS nº 190, de 15 de dezembro de 2017 (Incentivos Fiscais e Guerra Fiscal)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2017/CV190_17",
        "ementa": "Dispõe sobre a remissão e anistia dos créditos tributários decorrentes de isenções e incentivos fiscais e revalidação de normas concessivas nos termos da LC 160/2017.",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "Benefícios Fiscais"],
    },
    {
        "tipo": "Convênio ICMS",
        "subpasta": "convenios-icms",
        "prefixo_arquivo": "convenio-icms",
        "num": "52",
        "ano": "1991",
        "data": "1991-09-26",
        "titulo": "Convênio ICMS nº 52, de 26 de setembro de 1991 (Máquinas e Implementos Agrícolas)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/convenios/1991/CV052_91",
        "ementa": "Concede redução da base de cálculo do ICMS nas operações com equipamentos industriais e implementos agrícolas.",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS"],
    },
    {
        "tipo": "Convênio ICMS",
        "subpasta": "convenios-icms",
        "prefixo_arquivo": "convenio-icms",
        "num": "100",
        "ano": "1997",
        "data": "1997-11-04",
        "titulo": "Convênio ICMS nº 100, de 4 de novembro de 1997 (Insumos Agropecuários)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/convenios/1997/CV100_97",
        "ementa": "Reduz a base de cálculo do ICMS nas saídas dos insumos agropecuários que especifica.",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "Agronegócio"],
    },
    {
        "tipo": "Convênio ICMS",
        "subpasta": "convenios-icms",
        "prefixo_arquivo": "convenio-icms",
        "num": "236",
        "ano": "2021",
        "data": "2021-12-27",
        "titulo": "Convênio ICMS nº 236, de 27 de dezembro de 2021 (DIFAL a Não Contribuinte)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2021/CV236_21",
        "ementa": "Dispõe sobre os procedimentos a serem observados nas operações e prestações interestaduais que destinem mercadorias e serviços a consumidor final não contribuinte (DIFAL).",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "DIFAL"],
    },
    {
        "tipo": "Ajuste SINIEF",
        "subpasta": "ajustes-sinief",
        "prefixo_arquivo": "ajuste-sinief",
        "num": "07",
        "ano": "2005",
        "data": "2005-09-30",
        "titulo": "Ajuste SINIEF nº 07, de 30 de setembro de 2005 (Nota Fiscal Eletrônica - NF-e e DANFE)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/ajustes-sinief/2005/AJ_007_05",
        "ementa": "Institui a Nota Fiscal Eletrônica e o Documento Auxiliar da Nota Fiscal Eletrônica - DANFE.",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "IPI", "NF-e"],
    },
    {
        "tipo": "Ajuste SINIEF",
        "subpasta": "ajustes-sinief",
        "prefixo_arquivo": "ajuste-sinief",
        "num": "09",
        "ano": "2007",
        "data": "2007-10-25",
        "titulo": "Ajuste SINIEF nº 09, de 25 de outubro de 2007 (Conhecimento de Transporte Eletrônico - CT-e e DACTE)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/ajustes-sinief/2007/AJ_009_07",
        "ementa": "Institui o Conhecimento de Transporte Eletrônico e o Documento Auxiliar do Conhecimento de Transporte Eletrônico - DACTE.",
        "tema": "Serviços e Retenções",
        "tributos": ["ICMS", "Transporte", "CT-e"],
    },
    {
        "tipo": "Ajuste SINIEF",
        "subpasta": "ajustes-sinief",
        "prefixo_arquivo": "ajuste-sinief",
        "num": "02",
        "ano": "2009",
        "data": "2009-04-03",
        "titulo": "Ajuste SINIEF nº 02, de 3 de abril de 2009 (Escrituração Fiscal Digital - EFD SPED Fiscal)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/ajustes-sinief/2009/AJ_002_09",
        "ementa": "Dispõe sobre a Escrituração Fiscal Digital - EFD para fins de apuração e fiscalização do ICMS e do IPI.",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "IPI", "SPED Fiscal", "EFD"],
    },
    {
        "tipo": "Ajuste SINIEF",
        "subpasta": "ajustes-sinief",
        "prefixo_arquivo": "ajuste-sinief",
        "num": "01",
        "ano": "2019",
        "data": "2019-04-05",
        "titulo": "Ajuste SINIEF nº 01, de 5 de abril de 2019 (Guia Nacional de Recolhimento - GNRE On-Line)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/ajustes/2019/AJ001_19",
        "ementa": "Institui a Guia Nacional de Recolhimento de Tributos Estaduais On-Line - GNRE On-Line e estabelece regras de arrecadação interestadual.",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "GNRE", "Arrecadação Estadual"],
    },
]


class AgenteScraping:
    """Agente de Web Scraping especializado em portais governamentais fiscais e contábeis."""

    def __init__(self, rps: float = 2.0):
        self.rede = Rede(rps=rps)
        self.cache_dir = RAIZ / "_fonte" / "scraping"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.bin_extrair_pdf = RAIZ / "scripts" / "bin" / "extrair_pdf"

    def raspar_pagina(self, url: str, rotulo: str = "geral") -> str:
        """Baixa página HTML com cache compactado e controle estrito de vazão."""
        chave = hashlib.sha256(url.encode()).hexdigest()
        cache_file = self.cache_dir / rotulo / f"{chave}.html.gz"

        if cache_file.exists():
            return gzip.decompress(cache_file.read_bytes()).decode("utf-8", errors="replace")

        print(f"[Agente Scraping] Raspando HTML ({rotulo}): {url}")
        status, dados, _ = self.rede.get(url)
        if status != 200 or not dados:
            raise RuntimeError(f"Erro ao raspar HTML {url}: HTTP {status}")

        salvar_atomico(cache_file, gzip.compress(dados))
        return dados.decode("utf-8", errors="replace")

    def raspar_binario(self, url: str, rotulo: str = "geral", extensao: str = "pdf") -> bytes:
        """Baixa arquivo binário (PDF) com cache compactado e controle de vazão."""
        chave = hashlib.sha256(url.encode()).hexdigest()
        cache_file = self.cache_dir / rotulo / f"{chave}.{extensao}.gz"

        if cache_file.exists():
            return gzip.decompress(cache_file.read_bytes())

        print(f"[Agente Scraping] Baixando binário ({rotulo}): {url}")
        status, dados, _ = self.rede.get(url)
        if status != 200 or not dados:
            raise RuntimeError(f"Erro ao baixar binário {url}: HTTP {status}")

        salvar_atomico(cache_file, gzip.compress(dados))
        return dados

    def extrair_texto_pdf(self, pdf_bytes: bytes, rotulo: str = "temp") -> str:
        """Utiliza o utilitário nativo compilado Swift extrair_pdf para extrair texto limpo."""
        if not self.bin_extrair_pdf.exists():
            raise FileNotFoundError(f"Utilitário de extração de PDF não encontrado em: {self.bin_extrair_pdf}")

        temp_pdf = RAIZ / "_fonte" / "temp" / f"{rotulo}_{time.time_ns()}.pdf"
        salvar_atomico(temp_pdf, pdf_bytes)

        try:
            res = subprocess.run(
                [str(self.bin_extrair_pdf), str(temp_pdf)],
                capture_output=True,
                text=True,
                check=True
            )
            return res.stdout.strip()
        finally:
            if temp_pdf.exists():
                temp_pdf.unlink()

    def coletar_cpcs(self, lista_cpcs: list[dict] = None) -> list[Path]:
        """Coleta e estrutura pronunciamentos contábeis do CPC."""
        itens = lista_cpcs or NORMAS_CPC
        salvos = []
        pasta_cpc = RAIZ / "contabil" / "cpc"
        pasta_cpc.mkdir(parents=True, exist_ok=True)
        pasta_fonte = RAIZ / "_fonte" / "cpc"
        pasta_fonte.mkdir(parents=True, exist_ok=True)

        for cpc in itens:
            caminho_md = pasta_cpc / f"cpc-{cpc['num']}.md"
            if caminho_md.exists():
                print(f"[CPC] Documento já existente: {caminho_md.name} (ignorado)")
                salvos.append(caminho_md)
                continue

            print(f"[CPC] Processando {cpc['titulo']}...")
            try:
                pdf_bytes = self.raspar_binario(cpc["url"], rotulo="cpc", extensao="pdf")
                
                # Salva cópia bruta para inspeção local
                caminho_bruto_pdf = pasta_fonte / f"cpc_{cpc['num']}.pdf"
                salvar_atomico(caminho_bruto_pdf, pdf_bytes)

                texto = self.extrair_texto_pdf(pdf_bytes, rotulo=f"cpc_{cpc['num']}")

                meta = {
                    "titulo": cpc["titulo"],
                    "esfera": "Federal / Profissional",
                    "orgao": "Comitê de Pronunciamentos Contábeis (CPC) / CFC",
                    "tipo": "Pronunciamento Técnico",
                    "numero": str(cpc["num"]),
                    "data": cpc.get("data", f"{cpc['ano']}-01-01"),
                    "ano": str(cpc["ano"]),
                    "tema_tributario": cpc["tema"],
                    "tributos_afetados": cpc["tributos"],
                    "situacao": "Em vigor",
                    "revogada": False,
                    "fonte": cpc["url"],
                    "ementa": cpc["ementa"],
                }

                conteudo = gerar_frontmatter(meta) + f"# {cpc['titulo']}\n\n{texto}\n"
                salvar_atomico(caminho_md, conteudo.encode("utf-8"))
                print(f"[CPC] Salvo com sucesso: {caminho_md.relative_to(RAIZ)}")
                salvos.append(caminho_md)
            except Exception as e:
                print(f"[CPC Erro] Falha ao processar {cpc['titulo']}: {e}")

        return salvos

    def coletar_cfcs(self, lista_cfcs: list[dict] = None) -> list[Path]:
        """Coleta e estrutura Normas Brasileiras de Contabilidade (NBC TG) do CFC."""
        itens = lista_cfcs or NORMAS_CFC
        salvos = []
        pasta_cfc = RAIZ / "contabil" / "cfc"
        pasta_cfc.mkdir(parents=True, exist_ok=True)
        pasta_fonte = RAIZ / "_fonte" / "cfc"
        pasta_fonte.mkdir(parents=True, exist_ok=True)

        for cfc in itens:
            nome_arq = f"nbc-tg-{cfc['num'].lower()}.md"
            caminho_md = pasta_cfc / nome_arq
            if caminho_md.exists():
                print(f"[CFC] Documento já existente: {caminho_md.name} (ignorado)")
                salvos.append(caminho_md)
                continue

            print(f"[CFC] Processando {cfc['titulo']}...")
            try:
                pdf_bytes = self.raspar_binario(cfc["url"], rotulo="cfc", extensao="pdf")

                # Salva cópia bruta para inspeção local
                caminho_bruto_pdf = pasta_fonte / f"nbc_tg_{cfc['num'].lower()}.pdf"
                salvar_atomico(caminho_bruto_pdf, pdf_bytes)

                texto = self.extrair_texto_pdf(pdf_bytes, rotulo=f"cfc_{cfc['num']}")

                meta = {
                    "titulo": cfc["titulo"],
                    "esfera": "Federal / Profissional",
                    "orgao": "Conselho Federal de Contabilidade (CFC)",
                    "tipo": "Norma Brasileira de Contabilidade",
                    "numero": str(cfc["num"]),
                    "data": cfc.get("data", f"{cfc['ano']}-01-01"),
                    "ano": str(cfc["ano"]),
                    "tema_tributario": cfc["tema"],
                    "tributos_afetados": cfc["tributos"],
                    "situacao": "Em vigor",
                    "revogada": False,
                    "fonte": cfc["url"],
                    "ementa": cfc["ementa"],
                }

                conteudo = gerar_frontmatter(meta) + f"# {cfc['titulo']}\n\n{texto}\n"
                salvar_atomico(caminho_md, conteudo.encode("utf-8"))
                print(f"[CFC] Salvo com sucesso: {caminho_md.relative_to(RAIZ)}")
                salvos.append(caminho_md)
            except Exception as e:
                print(f"[CFC Erro] Falha ao processar {cfc['titulo']}: {e}")

        return salvos

    def coletar_confaz(self, lista_confaz: list[dict] = None) -> list[Path]:
        """Coleta e estrutura Convênios ICMS e Ajustes SINIEF do CONFAZ."""
        itens = lista_confaz or NORMAS_CONFAZ
        salvos = []
        pasta_fonte = RAIZ / "_fonte" / "confaz"
        pasta_fonte.mkdir(parents=True, exist_ok=True)

        for item in itens:
            pasta_destino = RAIZ / "reguladores" / "confaz" / item["subpasta"]
            pasta_destino.mkdir(parents=True, exist_ok=True)
            caminho_md = pasta_destino / f"{item['prefixo_arquivo']}-{item['num']}-{item['ano']}.md"

            if caminho_md.exists():
                print(f"[CONFAZ] Documento já existente: {caminho_md.name} (ignorado)")
                salvos.append(caminho_md)
                continue

            print(f"[CONFAZ] Processando {item['titulo']}...")
            try:
                html_raw = self.raspar_pagina(item["url"], rotulo="confaz")

                # Salva cópia bruta para inspeção
                caminho_bruto_html = pasta_fonte / f"{item['prefixo_arquivo']}_{item['num']}_{item['ano']}.html"
                salvar_atomico(caminho_bruto_html, html_raw.encode("utf-8"))

                # Extrai bloco de conteúdo central do portal CONFAZ
                m = re.search(r'<div id=\"parent-fieldname-text\"[^>]*>(.*?)</div>\s*</div>', html_raw, re.S)
                if not m:
                    m = re.search(r'<div id=\"content-core\"[^>]*>(.*?)</div>\s*</div>', html_raw, re.S)

                trecho_html = m.group(1) if m else html_raw
                corpo_md = converter_html_para_md(trecho_html)

                meta = {
                    "titulo": item["titulo"],
                    "esfera": "Estadual / CONFAZ",
                    "orgao": "Conselho Nacional de Política Fazendária (CONFAZ)",
                    "tipo": item["tipo"],
                    "numero": str(item["num"]),
                    "data": item.get("data", f"{item['ano']}-01-01"),
                    "ano": str(item["ano"]),
                    "tema_tributario": item["tema"],
                    "tributos_afetados": item["tributos"],
                    "situacao": "Em vigor",
                    "revogada": False,
                    "fonte": item["url"],
                    "ementa": item["ementa"],
                }

                conteudo = gerar_frontmatter(meta) + f"# {item['titulo']}\n\n{corpo_md}\n"
                salvar_atomico(caminho_md, conteudo.encode("utf-8"))
                print(f"[CONFAZ] Salvo com sucesso: {caminho_md.relative_to(RAIZ)}")
                salvos.append(caminho_md)
            except Exception as e:
                print(f"[CONFAZ Erro] Falha ao processar {item['titulo']}: {e}")

        return salvos

    def executar_coleta_completa(self) -> dict:
        """Executa a rotina completa de scraping fiscal/contábil (CONFAZ, CFC, CPC)."""
        print("=" * 70)
        print("INICIANDO ROTINA DE SCRAPING OFICIAL TRIBUTÁRIO E CONTÁBIL")
        print("=" * 70)

        t0 = time.time()
        cpcs = self.coletar_cpcs()
        cfcs = self.coletar_cfcs()
        confaz = self.coletar_confaz()

        duracao = time.time() - t0
        resumo = {
            "cpcs": len(cpcs),
            "cfcs": len(cfcs),
            "confaz": len(confaz),
            "total": len(cpcs) + len(cfcs) + len(confaz),
            "tempo_s": round(duracao, 2),
        }

        print("=" * 70)
        print(f"SCRAPING CONCLUÍDO EM {duracao:.2f}s: {resumo['total']} documentos gerados/verificados.")
        print("=" * 70)
        return resumo


if __name__ == "__main__":
    agente = AgenteScraping(rps=2.0)
    agente.executar_coleta_completa()
