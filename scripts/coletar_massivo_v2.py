"""Ingestão massiva de grande escala para o acervo tributário e contábil.

Executa em paralelo:
1. Decretos e Leis Federais Fundamentais (RIR/2018, RPS/1999, RIPI/2010, Aduana, PAF, LSA, Lei do Bem, etc.)
2. Série de Pronunciamentos Contábeis do CPC (CPC 01, 03, 04, 06, 16, 25, 27, 47)
3. Atos Normativos e Soluções de Consulta da Receita Federal em Série Histórica (2015–2025)
   abrangendo os 4 pilares: Dividendos/JCP, Folha/Previdência, Produtos/ICMS/IPI e Serviços/ISS/CSRF.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import datetime as dt
import json
import re
import subprocess
import sys
import time
import urllib.parse

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from agentes.agente_api import AgenteAPI
from agentes.agente_scraping import AgenteScraping
from agentes.agente_estruturador import AgenteEstruturador
from agentes.agente_auditor import AgenteAuditor
from agentes.agente_link_auditor import AgenteLinkAuditor
from agentes.agente_git import AgenteGit
from progresso import gerar_progresso
from catalogo import gerar_catalogo
from comum import salvar_atomico, gerar_frontmatter
from html2md import converter_html_para_md

# =====================================================================
# LOTE DE LEIS E DECRETOS FEDERAIS ESTRUTURANTES ADICIONAIS
# =====================================================================
DECRETOS_E_LEIS_ADICIONAIS = [
    {
        "titulo": "Decreto nº 9.580, de 22 de novembro de 2018 (Regulamento do Imposto de Renda - RIR/2018)",
        "urn": "urn:lex:br:federal:decreto:2018-11-22;9580",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:2018-11-22;9580",
        "numero": "9580", "ano": "2018", "tipo": "Decreto",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "IRPF", "IRRF", "CSLL"],
        "ementa": "Regulamenta a tributação, a fiscalização, a arrecadação e a administração do Imposto sobre a Renda e Proventos de Qualquer Natureza (RIR/2018).",
        "pasta": "federal/regulamentos/rir"
    },
    {
        "titulo": "Decreto nº 3.048, de 6 de maio de 1999 (Regulamento da Previdência Social - RPS)",
        "urn": "urn:lex:br:federal:decreto:1999-05-06;3048",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:1999-05-06;3048",
        "numero": "3048", "ano": "1999", "tipo": "Decreto",
        "tema": "Folha de Pagamento e Encargos",
        "tributos": ["INSS Patronal/Segurados", "RAT/FAP", "Contribuições Previdenciárias"],
        "ementa": "Aprova o Regulamento da Previdência Social, e dá outras providências.",
        "pasta": "federal/regulamentos/rps"
    },
    {
        "titulo": "Decreto nº 7.212, de 15 de junho de 2010 (Regulamento do IPI - RIPI/2010)",
        "urn": "urn:lex:br:federal:decreto:2010-07-26;7212",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:2010-07-26;7212",
        "numero": "7212", "ano": "2010", "tipo": "Decreto",
        "tema": "Produtos e Mercadorias",
        "tributos": ["IPI"],
        "ementa": "Regulamenta a cobrança, fiscalização, arrecadação e administração do Imposto sobre Produtos Industrializados - IPI (RIPI/2010).",
        "pasta": "federal/regulamentos/ripi"
    },
    {
        "titulo": "Decreto nº 6.759, de 5 de fevereiro de 2009 (Regulamento Aduaneiro)",
        "urn": "urn:lex:br:federal:decreto:2009-02-05;6759",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:2009-02-05;6759",
        "numero": "6759", "ano": "2009", "tipo": "Decreto",
        "tema": "Produtos e Mercadorias",
        "tributos": ["Imposto de Importação", "IPI", "PIS/Pasep", "Cofins"],
        "ementa": "Regulamenta a administração das atividades aduaneiras, e a fiscalização, o controle e a tributação das operações de comércio exterior (Regulamento Aduaneiro).",
        "pasta": "federal/regulamentos/aduana"
    },
    {
        "titulo": "Decreto nº 70.235, de 6 de março de 1972 (Processo Administrativo Fiscal - PAF)",
        "urn": "urn:lex:br:federal:decreto:1972-03-06;70235",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:1972-03-06;70235",
        "numero": "70235", "ano": "1972", "tipo": "Decreto",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Processo Administrativo Fiscal", "CARF"],
        "ementa": "Dispõe sobre o Processo Administrativo Fiscal (PAF) e regula a determinação e exigência dos créditos tributários da União.",
        "pasta": "federal/regulamentos/paf"
    },
    {
        "titulo": "Lei nº 6.404, de 15 de dezembro de 1976 (Lei das Sociedades por Ações - Demonstrações e Lucros)",
        "urn": "urn:lex:br:federal:lei:1976-12-15;6404",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1976-12-15;6404",
        "numero": "6404", "ano": "1976", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["Dividendos/Lucros", "Demonstrações Financeiras"],
        "ementa": "Dispõe sobre as Sociedades por Ações, disciplina a escrituração contábil, demonstrações financeiras e a distribuição de dividendos obrigatórios.",
        "pasta": "federal/leis-ordinarias/dividendos-jcp"
    },
    {
        "titulo": "Lei nº 9.718, de 27 de novembro de 1998 (PIS e COFINS no Faturamento)",
        "urn": "urn:lex:br:federal:lei:1998-11-27;9718",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1998-11-27;9718",
        "numero": "9718", "ano": "1998", "tipo": "Lei Ordinária",
        "tema": "Produtos e Mercadorias",
        "tributos": ["PIS/Pasep", "Cofins"],
        "ementa": "Altera a Legislação Tributária Federal, disciplina a cobrança de PIS e COFINS sobre a receita bruta e faturamento.",
        "pasta": "federal/leis-ordinarias"
    },
    {
        "titulo": "Lei nº 10.865, de 30 de abril de 2004 (PIS e COFINS Importação)",
        "urn": "urn:lex:br:federal:lei:2004-04-30;10865",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2004-04-30;10865",
        "numero": "10865", "ano": "2004", "tipo": "Lei Ordinária",
        "tema": "Produtos e Mercadorias",
        "tributos": ["PIS/Pasep", "Cofins", "Imposto de Importação"],
        "ementa": "Dispõe sobre a Contribuição para os Programas de Integração Social e de Formação do Patrimônio do Servidor Público incidente sobre a Importação de Produtos Estrangeiros ou Serviços (PIS/PASEP-Importação) e da COFINS-Importação.",
        "pasta": "federal/leis-ordinarias"
    },
    {
        "titulo": "Lei nº 11.033, de 21 de dezembro de 2004 (Mercado Financeiro e REIDI)",
        "urn": "urn:lex:br:federal:lei:2004-12-21;11033",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2004-12-21;11033",
        "numero": "11033", "ano": "2004", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRRF", "REIDI", "Mercado Financeiro"],
        "ementa": "Altera a tributação do mercado financeiro e de capitais; institui o Regime Especial de Incentivos para o Desenvolvimento da Infra-Estrutura - REIDI.",
        "pasta": "federal/leis-ordinarias"
    },
    {
        "titulo": "Lei nº 11.196, de 21 de novembro de 2005 (Lei do Bem - Incentivos Fiscais)",
        "urn": "urn:lex:br:federal:lei:2005-11-21;11196",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2005-11-21;11196",
        "numero": "11196", "ano": "2005", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "Lei do Bem"],
        "ementa": "Institui incentivos fiscais para a inovação tecnológica (Lei do Bem), altera a legislação do IRPJ e da CSLL.",
        "pasta": "federal/leis-ordinarias"
    },
    {
        "titulo": "Lei nº 11.941, de 27 de maio de 2009 (Extinção do RTT e Parcelamento)",
        "urn": "urn:lex:br:federal:lei:2009-05-27;11941",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2009-05-27;11941",
        "numero": "11941", "ano": "2009", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "PIS/Pasep", "Cofins"],
        "ementa": "Institui o Regime Tributário de Transição - RTT e disciplina o parcelamento de débitos tributários federais.",
        "pasta": "federal/leis-ordinarias"
    },
    {
        "titulo": "Lei nº 13.043, de 2 de outubro de 2014 (Desonerações e Mercado de Capitais)",
        "urn": "urn:lex:br:federal:lei:2014-10-02;13043",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2014-10-02;13043",
        "numero": "13043", "ano": "2014", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRRF", "IRPJ", "Mercado de Capitais"],
        "ementa": "Dispõe sobre a isenção de imposto sobre a renda na alienação de debêntures e incentivos ao mercado de capitais.",
        "pasta": "federal/leis-ordinarias"
    }
]

# =====================================================================
# SÉRIE DE PRONUNCIAMENTOS CONTÁBEIS (CPC)
# =====================================================================
CPCS_PARA_COLETA = [
    {"num": "01", "ano": "2010", "titulo": "Pronunciamento Técnico CPC 01 (R1) - Redução ao Valor Recuperável de Ativos (Impairment)", "url_cpc": "http://www.cpc.org.br/Arquivos/Documentos/27_CPC_01_R1_rev%2021_ComAVISO.pdf", "ementa": "Define os procedimentos para assegurar que os ativos não estejam registrados contabilmente por valor superior àquele passível de ser recuperado por uso ou venda.", "tema": "Contabilidade e Geral"},
    {"num": "03", "ano": "2010", "titulo": "Pronunciamento Técnico CPC 03 (R2) - Demonstração dos Fluxos de Caixa (DFC)", "url_cpc": "http://www.cpc.org.br/Arquivos/Documentos/147_CPC03_R2.pdf", "ementa": "Requer o fornecimento de informações sobre as alterações históricas de caixa e equivalentes de caixa da entidade por meio de DFC.", "tema": "Contabilidade e Geral"},
    {"num": "04", "ano": "2010", "titulo": "Pronunciamento Técnico CPC 04 (R1) - Ativo Intangível", "url_cpc": "http://www.cpc.org.br/Arquivos/Documentos/155_CPC_04_R1_rev%2022.pdf", "ementa": "Define o tratamento contábil de ativos intangíveis (incluindo ágio/goodwill e critérios de amortização contábil e fiscal).", "tema": "Dividendos e Renda do Capital"},
    {"num": "06", "ano": "2018", "titulo": "Pronunciamento Técnico CPC 06 (R2) - Operações de Arrendamento Mercantil (IFRS 16)", "url_cpc": "http://www.cpc.org.br/Arquivos/Documentos/532_CPC%2006%20(R2).pdf", "ementa": "Estabelece os princípios para o reconhecimento, mensuração, apresentação e divulgação de arrendamentos (leasing) para locatários e locadores.", "tema": "Contabilidade e Geral"},
    {"num": "16", "ano": "2009", "titulo": "Pronunciamento Técnico CPC 16 (R1) - Estoques", "url_cpc": "http://www.cpc.org.br/Arquivos/Documentos/255_CPC%2016%20R1.pdf", "ementa": "Estabelece o tratamento contábil para estoques, determinando o valor de custo de aquisição deduzido de tributos recuperáveis (ICMS/PIS/COFINS).", "tema": "Produtos e Mercadorias"},
    {"num": "25", "ano": "2009", "titulo": "Pronunciamento Técnico CPC 25 - Provisões, Passivos Contingentes e Ativos Contingentes", "url_cpc": "http://www.cpc.org.br/Arquivos/Documentos/303_CPC_25_rev%2014.pdf", "ementa": "Define critérios para reconhecimento e bases apropriadas de mensuração para provisões fiscais/tributárias e contingências judiciais.", "tema": "Tributário e Contábil Geral"},
    {"num": "27", "ano": "2009", "titulo": "Pronunciamento Técnico CPC 27 - Ativo Imobilizado", "url_cpc": "http://www.cpc.org.br/Arquivos/Documentos/313_CPC_27_rev%2022.pdf", "ementa": "Estabelece o tratamento contábil para ativos imobilizados, incluindo taxas de depreciação, vida útil econômica e conciliação com a depreciação fiscal do RIR.", "tema": "Contabilidade e Geral"},
    {"num": "47", "ano": "2016", "titulo": "Pronunciamento Técnico CPC 47 - Receita de Contrato com Cliente (IFRS 15)", "url_cpc": "http://www.cpc.org.br/Arquivos/Documentos/522_CPC_47_rev%2023.pdf", "ementa": "Estabelece os princípios que a entidade deve aplicar para relatar informações úteis sobre a natureza, valor, época e incerteza de receitas e fluxos de caixa de contrato com cliente.", "tema": "Serviços e Retenções"}
]

def coletar_leis_federais():
    print("\n[Worker 1] Coletando Decretos e Leis Federais Estruturantes...")
    api_agent = AgenteAPI(rps=2.0)
    gerados = []
    
    for item in DECRETOS_E_LEIS_ADICIONAIS:
        caminho = RAIZ / item["pasta"] / f"lei-{item['numero']}-{item['ano']}.md"
        if caminho.exists():
            continue
            
        print(f"[LexML] Ingerindo {item['titulo']}...")
        try:
            res = api_agent.baixar_norma_lexml(item["urn"])
            html = res.get("html", "")
            corpo_md = converter_html_para_md(html)
            
            meta = {
                "titulo": item["titulo"],
                "esfera": "Federal",
                "orgao": "Presidência da República / Congresso Nacional",
                "tipo": item["tipo"],
                "numero": item["numero"],
                "ano": item["ano"],
                "data": f"{item['ano']}-01-01",
                "tema_tributario": item["tema"],
                "tributos_afetados": item["tributos"],
                "situacao": "Em vigor",
                "revogada": False,
                "fonte": item["url"],
                "ementa": item["ementa"]
            }
            
            conteudo = gerar_frontmatter(meta) + f"# {item['titulo']}\n\n{corpo_md}\n"
            salvar_atomico(caminho, conteudo.encode("utf-8"))
            print(f"[LexML] Salvo: {caminho.relative_to(RAIZ)}")
            gerados.append(caminho)
        except Exception as e:
            print(f"[LexML Erro] {item['titulo']}: {e}")
            
    return gerados

def coletar_normas_cpc():
    print("\n[Worker 2] Coletando Pronunciamentos Contábeis CPC...")
    scraper = AgenteScraping(rps=1.0)
    bin_extractor = RAIZ / "scripts" / "bin" / "extrair_pdf"
    gerados = []
    
    for cpc in CPCS_PARA_COLETA:
        caminho_md = RAIZ / "contabil" / "cpc" / f"cpc-{cpc['num']}.md"
        if caminho_md.exists():
            continue
            
        print(f"[CPC] Ingerindo {cpc['titulo']}...")
        try:
            status, pdf_bytes, _ = scraper.rede.get(cpc["url_cpc"])
            if status != 200 or not pdf_bytes:
                print(f"[CPC] Erro HTTP {status} ao baixar PDF: {cpc['url_cpc']}")
                continue
                
            tmp_pdf = RAIZ / "_fonte" / "cpc" / f"cpc_{cpc['num']}.pdf"
            salvar_atomico(tmp_pdf, pdf_bytes)
            
            proc = subprocess.run([str(bin_extractor), str(tmp_pdf)], capture_output=True, text=True, check=True)
            texto_pdf = proc.stdout.strip()
            
            meta = {
                "titulo": cpc["titulo"],
                "esfera": "Federal / Profissional",
                "orgao": "Comitê de Pronunciamentos Contábeis (CPC) / CFC",
                "tipo": "Pronunciamento Técnico",
                "numero": cpc["num"],
                "ano": cpc["ano"],
                "data": f"{cpc['ano']}-01-01",
                "tema_tributario": cpc["tema"],
                "tributos_afetados": ["Contabilidade Societária e Fiscal"],
                "situacao": "Em vigor",
                "revogada": False,
                "fonte": cpc["url_cpc"],
                "ementa": cpc["ementa"]
            }
            
            conteudo = gerar_frontmatter(meta) + f"# {cpc['titulo']}\n\n{texto_pdf}\n"
            salvar_atomico(caminho_md, conteudo.encode("utf-8"))
            print(f"[CPC] Salvo: {caminho_md.relative_to(RAIZ)}")
            gerados.append(caminho_md)
        except Exception as e:
            print(f"[CPC Erro] {cpc['titulo']}: {e}")
            
    return gerados

def coletar_rfb_multianual():
    print("\n[Worker 3] Coletando Atos da Receita Federal em Série Histórica (2015–2025)...")
    api_agent = AgenteAPI(rps=2.0)
    estruturador = AgenteEstruturador()
    gerados = []
    
    anos = [2015, 2016, 2017, 2019, 2021, 2022, 2023, 2024, 2025]
    termos = ["imposto", "previdenciaria", "icms", "retencao"]
    
    def processar_ano_termo(ano, termo):
        locais = []
        try:
            res = api_agent.consultar_atos_rfb(termo=termo, ano=ano, pagina=1, tamanho=3)
            atos = res.get("atos", []) if isinstance(res, dict) else res
            for item in atos[:3]:
                id_ato = item.get("idAto")
                if id_ato:
                    detalhes = api_agent.baixar_corpo_ato_rfb(id_ato)
                    dados = {**item, **detalhes}
                    md_path = estruturador.estruturar_ato_rfb(dados)
                    locais.append(md_path)
        except Exception as e:
            print(f"[RFB Ano {ano} / Termo '{termo}' Erro]: {e}")
        return locais

    with ThreadPoolExecutor(max_workers=4) as executor:
        futuros = []
        for ano in anos:
            for termo in termos:
                futuros.append(executor.submit(processar_ano_termo, ano, termo))
                
        for f in as_completed(futuros):
            gerados.extend(f.result())
            
    return gerados

def main():
    print("=" * 75)
    print("INICIANDO INGESTÃO DE GRANDE ESCALA CONCORRENTE MULTIDOMÍNIO")
    print("=" * 75)
    
    t0 = time.time()
    todos = []
    
    with ThreadPoolExecutor(max_workers=3) as pool:
        f_leis = pool.submit(coletar_leis_federais)
        f_cpc = pool.submit(coletar_normas_cpc)
        f_rfb = pool.submit(coletar_rfb_multianual)
        
        todos.extend(f_leis.result())
        todos.extend(f_cpc.result())
        todos.extend(f_rfb.result())
        
    print("\n" + "=" * 75)
    print(f"INGESTÃO CONCLUÍDA EM {time.time() - t0:.1f}s: {len(todos)} DOCUMENTOS PROCESSADOS.")
    print("ACIONANDO AGENTE LINK AUDITOR PARA SANEAMENTO CONCORRENTE DE LINKS...")
    print("=" * 75)
    
    link_auditor = AgenteLinkAuditor(rps=4.0)
    link_auditor.executar_auditoria_concorrente()
    
    print("\nACIONANDO O AGENTE AUDITOR PARA CONFERÊNCIA RIGOROSA...")
    auditor = AgenteAuditor()
    relatorio = auditor.auditar_repositorio(checar_rede=True)
    
    print("\nATUALIZANDO ACERVO.MD (CATÁLOGO GERAL)...")
    total_docs = gerar_catalogo()
    
    print("\nATUALIZANDO PROGRESSO.MD...")
    gerar_progresso()
    
    print("\nREGISTRANDO HISTÓRICO NO WORKLOG.MD...")
    git_agent = AgenteGit()
    git_agent.registrar_worklog(
        f"Ingestão de grande escala concluída com sucesso. "
        f"Lote processou {len(todos)} novos documentos. Total no acervo: {total_docs}. "
        f"Auditoria independente de rede: {relatorio['aprovados']} aprovados, {relatorio['rejeitados']} rejeitados (Taxa: {relatorio['taxa_aprovacao']})."
    )
    print("\n=== PIPELINE DE INGESTÃO MASSIVA V2 FINALIZADO COM SUCESSO ===")

if __name__ == "__main__":
    main()
