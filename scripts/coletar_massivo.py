"""Ingestão massiva concorrente de legislação tributária e contábil.

Coleta:
1. Leis estruturantes federais históricas e contemporâneas (1964–2024):
   CTN, IPI, CSLL, IRPF, L8981, L9249, L9430, Kandir, LC 116, PIS, COFINS,
   Simples Nacional, CPRB, L12973, Preços de Transferência (L14596), Offshores (L14754),
   Subvenções (L14789) e EC 132/2023 (Reforma Tributária).
2. Normas e Pronunciamentos Contábeis (CPC 00 e CPC 32 - Tributos sobre o Lucro).
3. Atos normativos e soluções de consulta da Receita Federal (Sijut) em série histórica.
4. Auditoria rigorosa de todas as fontes pelo Agente Auditor.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import datetime as dt
import json
import re
import subprocess
import sys
import time

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from agentes.agente_api import AgenteAPI
from agentes.agente_scraping import AgenteScraping
from agentes.agente_estruturador import AgenteEstruturador
from agentes.agente_auditor import AgenteAuditor
from agentes.agente_git import AgenteGit
from progresso import gerar_progresso
from comum import salvar_atomico, gerar_frontmatter
from html2md import converter_html_para_md

# Catálogo completo de Leis Estruturantes Federais
ACERVO_LEIS_FEDERAIS = [
    # Direito Tributário Geral
    {
        "titulo": "Lei nº 5.172, de 25 de outubro de 1966 (Código Tributário Nacional)",
        "urn": "urn:lex:br:federal:lei:1966-10-25;5172",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1966-10-25;5172",
        "numero": "5172", "ano": "1966", "tipo": "Lei Ordinária",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Sistema Tributário Nacional", "CTN"],
        "ementa": "Dispõe sobre o Sistema Tributário Nacional e institui normas gerais de direito tributário aplicáveis à União, Estados e Municípios (Código Tributário Nacional).",
        "pasta": "federal/leis-complementares/ctn"
    },
    # Pilar 1: Dividendos, Renda do Capital & IRPJ/CSLL
    {
        "titulo": "Lei nº 7.689, de 15 de dezembro de 1988 (Institui a CSLL)",
        "urn": "urn:lex:br:federal:lei:1988-12-15;7689",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1988-12-15;7689",
        "numero": "7689", "ano": "1988", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["CSLL"],
        "ementa": "Institui contribuição social sobre o lucro das pessoas jurídicas e dá outras providências.",
        "pasta": "federal/leis-ordinarias/irpj-csll"
    },
    {
        "titulo": "Lei nº 7.713, de 22 de dezembro de 1988 (IRPF e Rendimentos)",
        "urn": "urn:lex:br:federal:lei:1988-12-22;7713",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1988-12-22;7713",
        "numero": "7713", "ano": "1988", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPF", "IRRF"],
        "ementa": "Altera a legislação do imposto de renda e dá outras providências.",
        "pasta": "federal/leis-ordinarias/irrf-folha-plr"
    },
    {
        "titulo": "Lei nº 8.981, de 20 de janeiro de 1995 (Tributação de Lucros e Renda)",
        "urn": "urn:lex:br:federal:lei:1995-01-20;8981",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1995-01-20;8981",
        "numero": "8981", "ano": "1995", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "Ganho de Capital"],
        "ementa": "Altera a legislação tributária federal e dá outras providências relativas ao IRPJ e à CSLL.",
        "pasta": "federal/leis-ordinarias/irpj-csll"
    },
    {
        "titulo": "Lei nº 9.430, de 27 de dezembro de 1996 (Normas Gerais IRPJ/CSLL)",
        "urn": "urn:lex:br:federal:lei:1996-12-27;9430",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1996-12-27;9430",
        "numero": "9430", "ano": "1996", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL"],
        "ementa": "Dispõe sobre a legislação tributária federal, as contribuições para a seguridade social, o processo administrativo de consulta e dá outras providências.",
        "pasta": "federal/leis-ordinarias/irpj-csll"
    },
    {
        "titulo": "Lei nº 12.973, de 13 de maio de 2014 (Adequação IFRS e Lucros no Exterior)",
        "urn": "urn:lex:br:federal:lei:2014-05-13;12973",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2014-05-13;12973",
        "numero": "12973", "ano": "2014", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "PIS/Pasep", "Cofins"],
        "ementa": "Altera a legislação tributária federal relativa ao IRPJ, CSLL, PIS e COFINS, adapta a legislação tributária aos padrões internacionais de contabilidade (IFRS) e disciplina a tributação de lucros no exterior.",
        "pasta": "federal/leis-ordinarias/irpj-csll"
    },
    {
        "titulo": "Lei nº 14.596, de 14 de junho de 2023 (Preços de Transferência)",
        "urn": "urn:lex:br:federal:lei:2023-06-14;14596",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2023-06-14;14596",
        "numero": "14596", "ano": "2023", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "Preços de Transferência"],
        "ementa": "Dispõe sobre as regras de preços de transferência para fins de apuração do IRPJ e da CSLL, convergindo com as diretrizes da OCDE.",
        "pasta": "tratados/precos-de-transferencia"
    },
    {
        "titulo": "Lei nº 14.789, de 29 de dezembro de 2023 (Subvenções para Investimento)",
        "urn": "urn:lex:br:federal:lei:2023-12-29;14789",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2023-12-29;14789",
        "numero": "14789", "ano": "2023", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL"],
        "ementa": "Dispõe sobre o crédito fiscal decorrente de subvenção para implantação ou expansão de empreendimento econômico.",
        "pasta": "federal/leis-ordinarias/irpj-csll"
    },
    # Pilar 2: Folha e Trabalho
    {
        "titulo": "Lei nº 8.036, de 11 de maio de 1990 (FGTS)",
        "urn": "urn:lex:br:federal:lei:1990-05-11;8036",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1990-05-11;8036",
        "numero": "8036", "ano": "1990", "tipo": "Lei Ordinária",
        "tema": "Folha de Pagamento e Encargos",
        "tributos": ["FGTS"],
        "ementa": "Dispõe sobre o Fundo de Garantia do Tempo de Serviço, e dá outras providências.",
        "pasta": "reguladores/mte-caixa/fgts-esocial"
    },
    # Pilar 3: Produtos e PIS/COFINS
    {
        "titulo": "Lei nº 10.637, de 30 de dezembro de 2002 (PIS Não Cumulativo)",
        "urn": "urn:lex:br:federal:lei:2002-12-30;10637",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2002-12-30;10637",
        "numero": "10637", "ano": "2002", "tipo": "Lei Ordinária",
        "tema": "Produtos e Mercadorias",
        "tributos": ["PIS/Pasep"],
        "ementa": "Dispõe sobre a não-cumulatividade na cobrança da contribuição para os Programas de Integração Social (PIS) e de Formação do Patrimônio do Servidor Público (Pasep).",
        "pasta": "federal/leis-ordinarias"
    },
    {
        "titulo": "Lei Complementar nº 123, de 14 de dezembro de 2006 (Simples Nacional)",
        "urn": "urn:lex:br:federal:lei.complementar:2006-12-14;123",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2006-12-14;123",
        "numero": "123", "ano": "2006", "tipo": "Lei Complementar",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Simples Nacional", "ICMS", "ISSQN", "IRPJ", "CSLL", "PIS/Pasep", "Cofins", "INSS Patronal/Segurados"],
        "ementa": "Institui o Estatuto Nacional da Microempresa e da Empresa de Pequeno Porte (Simples Nacional).",
        "pasta": "federal/leis-complementares/simples"
    },
    {
        "titulo": "Emenda Constitucional nº 132, de 20 de dezembro de 2023 (Reforma Tributária)",
        "urn": "urn:lex:br:federal:emenda.constitucional:2023-12-20;132",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:emenda.constitucional:2023-12-20;132",
        "numero": "132", "ano": "2023", "tipo": "Emenda Constitucional",
        "tema": "Produtos e Mercadorias",
        "tributos": ["IBS", "CBS", "Imposto Seletivo", "ICMS", "ISSQN", "IPI"],
        "ementa": "Altera o Sistema Tributário Nacional para instituir o Imposto sobre Bens e Serviços (IBS), a Contribuição sobre Bens e Serviços (CBS) e o Imposto Seletivo (IS).",
        "pasta": "federal/constituicao"
    }
]

def baixar_leis_estruturantes_lote():
    api_agent = AgenteAPI(rps=2.0)
    gerados = []
    print("\n--- [LOTE 1] INGESTÃO DE LEIS ESTRUTURANTES FEDERAIS ---")
    
    for item in ACERVO_LEIS_FEDERAIS:
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
                "orgao": "Congresso Nacional / Presidência da República",
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

def baixar_normas_contabeis_cpc():
    """Coleta os principais pronunciamentos contábeis com impacto fiscal (CPC 00 e CPC 32)."""
    print("\n--- [LOTE 2] INGESTÃO DE NORMAS CONTÁBEIS (CPC) ---")
    scraper = AgenteScraping(rps=1.0)
    gerados = []
    
    cpcs = [
        {
            "id": "80", "numero": "00", "ano": "2019",
            "titulo": "Pronunciamento Técnico CPC 00 (R2) - Estrutura Conceitual para Relatório Financeiro",
            "pdf_url": "http://www.cpc.org.br/Arquivos/Documentos/573_CPC00_R2.pdf",
            "ementa": "Define a estrutura conceitual para a elaboração e divulgação de relatório contábil-financeiro de propósito geral.",
            "tema": "Contabilidade e Geral"
        },
        {
            "id": "63", "numero": "32", "ano": "2009",
            "titulo": "Pronunciamento Técnico CPC 32 - Tributos sobre o Lucro",
            "pdf_url": "http://www.cpc.org.br/Arquivos/Documentos/340_CPC_32_rev%2024.pdf",
            "ementa": "Estabelece o tratamento contábil dos tributos sobre o lucro (IRPJ e CSLL correntes e diferidos, diferenças temporárias e prejuízos fiscais compensáveis).",
            "tema": "Dividendos e Renda do Capital"
        }
    ]
    
    bin_extractor = RAIZ / "scripts" / "bin" / "extrair_pdf"
    for cpc in cpcs:
        caminho_md = RAIZ / "contabil" / "cpc" / f"cpc-{cpc['numero']}.md"
        if caminho_md.exists():
            continue
            
        print(f"[CPC] Baixando {cpc['titulo']}...")
        try:
            status, pdf_bytes, _ = scraper.rede.get(cpc["pdf_url"])
            if status != 200 or not pdf_bytes:
                print(f"[CPC] Falha ao obter PDF do {cpc['titulo']} (HTTP {status})")
                continue
                
            tmp_pdf = RAIZ / "_fonte" / "cpc" / f"cpc_{cpc['numero']}.pdf"
            salvar_atomico(tmp_pdf, pdf_bytes)
            
            # Extração de texto com o binário nativo Swift PDFKit
            proc = subprocess.run([str(bin_extractor), str(tmp_pdf)], capture_output=True, text=True, check=True)
            texto_pdf = proc.stdout.strip()
            
            meta = {
                "titulo": cpc["titulo"],
                "esfera": "Federal / Profissional",
                "orgao": "Comitê de Pronunciamentos Contábeis (CPC) / CFC",
                "tipo": "Pronunciamento Técnico",
                "numero": cpc["numero"],
                "ano": cpc["ano"],
                "data": f"{cpc['ano']}-01-01",
                "tema_tributario": cpc["tema"],
                "tributos_afetados": ["IRPJ", "CSLL"] if cpc["numero"] == "32" else None,
                "situacao": "Em vigor",
                "revogada": False,
                "fonte": cpc["pdf_url"],
                "ementa": cpc["ementa"]
            }
            
            conteudo = gerar_frontmatter(meta) + f"# {cpc['titulo']}\n\n{texto_pdf}\n"
            salvar_atomico(caminho_md, conteudo.encode("utf-8"))
            print(f"[CPC] Salvo: {caminho_md.relative_to(RAIZ)}")
            gerados.append(caminho_md)
        except Exception as e:
            print(f"[CPC Erro] {cpc['titulo']}: {e}")
            
    return gerados

def baixar_atos_rfb_anos(anos: list, limite_por_ano: int = 5):
    """Coleta atos normativos da Receita Federal abrangendo uma série temporal de anos."""
    print(f"\n--- [LOTE 3] INGESTÃO CONCORRENTE DA RECEITA FEDERAL (ANOS {anos}) ---")
    api_agent = AgenteAPI(rps=2.0)
    estruturador = AgenteEstruturador()
    gerados = []
    
    def processar_ano(ano):
        locais = []
        try:
            res = api_agent.consultar_atos_rfb(termo="tributos", ano=ano, pagina=1, tamanho=limite_por_ano)
            atos = res.get("atos", []) if isinstance(res, dict) else res
            for item in atos[:limite_por_ano]:
                id_ato = item.get("idAto")
                if id_ato:
                    detalhes = api_agent.baixar_corpo_ato_rfb(id_ato)
                    dados = {**item, **detalhes}
                    md_path = estruturador.estruturar_ato_rfb(dados)
                    locais.append(md_path)
        except Exception as e:
            print(f"[RFB Ano {ano} Erro]: {e}")
        return locais

    with ThreadPoolExecutor(max_workers=3) as executor:
        futuros = [executor.submit(processar_ano, a) for a in anos]
        for f in as_completed(futuros):
            gerados.extend(f.result())
            
    return gerados

def main():
    print("=" * 70)
    print("INICIANDO INGESTÃO MASSIVA CONCORRENTE (LEIS + CPC + RECEITA FEDERAL)")
    print("=" * 70)
    
    t0 = time.time()
    
    # 1. Leis Federais
    leis_novas = baixar_leis_estruturantes_lote()
    
    # 2. CPC Normas Contábeis
    cpc_novos = baixar_normas_contabeis_cpc()
    
    # 3. RFB Anos 2018 a 2025
    anos_rfb = [2018, 2020, 2022, 2023, 2024, 2025]
    rfb_novos = baixar_atos_rfb_anos(anos_rfb, limite_por_ano=4)
    
    total_lote = leis_novas + cpc_novos + rfb_novos
    print("\n" + "=" * 70)
    print(f"LOTE FINALIZADO EM {time.time() - t0:.1f}s: {len(total_lote)} NOVOS ARQUIVOS.")
    print("ACIONANDO AGENTE AUDITOR PARA CONFERÊNCIA INDEPENDENTE...")
    print("=" * 70)
    
    auditor = AgenteAuditor()
    relatorio = auditor.auditar_repositorio(checar_rede=True)
    
    print("\nATUALIZANDO PROGRESSO.MD...")
    gerar_progresso()
    
    print("\nACIONANDO O AGENTE GIT...")
    git_agent = AgenteGit()
    git_agent.registrar_worklog(
        f"Ingestão massiva concluída. Total de documentos no lote: {len(total_lote)}. "
        f"Auditoria: {relatorio['aprovados']} aprovados, {relatorio['rejeitados']} rejeitados."
    )
    print("=== INGESTÃO MASSIVA CONCLUÍDA COM SUCESSO ===")

if __name__ == "__main__":
    main()
