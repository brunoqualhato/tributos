"""Pipeline de importação paralela de normas tributárias nos 4 pilares:
1. Dividendos, Renda do Capital & JCP
2. Folha de Pagamento & Encargos Previdenciários
3. Produtos & Mercadorias (ICMS, IPI, Monofásicos)
4. Serviços & Retenções (ISSQN, CSRF 4,65%)

Executa a coleta concorrente utilizando os agentes especializados,
passa pelo Agente Estruturador, aciona o Agente Auditor para conferência
contra o link oficial e atualiza o PROGRESSO.md.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import datetime as dt
import json
import re
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

# =====================================================================
# LEIS ESTRUTURANTES FEDERAIS PARA COLETA
# =====================================================================
LEIS_ESTRUTURANTES = {
    "dividendos": [
        {
            "titulo": "Lei nº 9.249, de 26 de dezembro de 1995",
            "urn": "urn:lex:br:federal:lei:1995-12-26;9249",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1995-12-26;9249",
            "numero": "9249",
            "ano": "1995",
            "tipo": "Lei Ordinária",
            "tema": "Dividendos e Renda do Capital",
            "tributos": ["Dividendos/Lucros", "JCP", "IRPJ", "CSLL"],
            "ementa": "Altera a legislação do imposto de renda das pessoas jurídicas, bem como da contribuição social sobre o lucro líquido, estabelece a isenção de dividendos e cria os Juros sobre o Capital Próprio (JCP).",
            "pasta": "federal/leis-ordinarias/dividendos-jcp"
        },
        {
            "titulo": "Lei nº 14.754, de 12 de dezembro de 2023",
            "urn": "urn:lex:br:federal:lei:2023-12-12;14754",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2023-12-12;14754",
            "numero": "14754",
            "ano": "2023",
            "tipo": "Lei Ordinária",
            "tema": "Dividendos e Renda do Capital",
            "tributos": ["IRPF", "IRPJ", "Offshores e Trusts"],
            "ementa": "Dispõe sobre a tributação de renda auferida por pessoas físicas residentes no País em aplicações financeiras no exterior, entidades controladas e trusts no exterior.",
            "pasta": "federal/leis-ordinarias/offshores"
        }
    ],
    "folha": [
        {
            "titulo": "Lei nº 8.212, de 24 de julho de 1991",
            "urn": "urn:lex:br:federal:lei:1991-07-24;8212",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1991-07-24;8212",
            "numero": "8212",
            "ano": "1991",
            "tipo": "Lei Ordinária",
            "tema": "Folha de Pagamento e Encargos",
            "tributos": ["INSS Patronal/Segurados", "Contribuições Previdenciárias"],
            "ementa": "Dispõe sobre a organização da Seguridade Social, institui Plano de Custeio, e dá outras providências.",
            "pasta": "federal/leis-ordinarias/previdencia-custeio"
        },
        {
            "titulo": "Lei nº 12.546, de 14 de dezembro de 2011",
            "urn": "urn:lex:br:federal:lei:2011-12-14;12546",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2011-12-14;12546",
            "numero": "12546",
            "ano": "2011",
            "tipo": "Lei Ordinária",
            "tema": "Folha de Pagamento e Encargos",
            "tributos": ["CPRB (Desoneração da Folha)", "INSS Patronal/Segurados"],
            "ementa": "Institui o Regime Especial de Reintegração de Valores Tributários para as Empresas Exportadoras (Reintegra); dispõe sobre a desoneração da folha de pagamento (CPRB).",
            "pasta": "federal/leis-ordinarias/cprb"
        },
        {
            "titulo": "Lei nº 10.101, de 19 de dezembro de 2000",
            "urn": "urn:lex:br:federal:lei:2000-12-19;10101",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2000-12-19;10101",
            "numero": "10101",
            "ano": "2000",
            "tipo": "Lei Ordinária",
            "tema": "Folha de Pagamento e Encargos",
            "tributos": ["IRRF Folha", "PLR"],
            "ementa": "Regulamenta a participação dos trabalhadores nos lucros ou resultados da empresa e estabelece regras de tributação exclusiva na fonte.",
            "pasta": "federal/leis-ordinarias/irrf-folha-plr"
        }
    ],
    "produtos": [
        {
            "titulo": "Lei Complementar nº 87, de 13 de setembro de 1996",
            "urn": "urn:lex:br:federal:lei.complementar:1996-09-13;87",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:1996-09-13;87",
            "numero": "87",
            "ano": "1996",
            "tipo": "Lei Complementar",
            "tema": "Produtos e Mercadorias",
            "tributos": ["ICMS", "ICMS-ST"],
            "ementa": "Dispõe sobre o imposto dos Estados e do Distrito Federal sobre operações relativas à circulação de mercadorias e sobre prestações de serviços de transporte interestadual e intermunicipal e de comunicação, e dá outras providências (Lei Kandir).",
            "pasta": "federal/leis-complementares/kandir"
        },
        {
            "titulo": "Lei nº 4.502, de 30 de novembro de 1964",
            "urn": "urn:lex:br:federal:lei:1964-11-30;4502",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1964-11-30;4502",
            "numero": "4502",
            "ano": "1964",
            "tipo": "Lei Ordinária",
            "tema": "Produtos e Mercadorias",
            "tributos": ["IPI"],
            "ementa": "Dispõe sôbre o Imposto de Consumo e reorganiza a legislação sobre produtos industrializados (IPI).",
            "pasta": "federal/regulamentos/ripi"
        }
    ],
    "servicos": [
        {
            "titulo": "Lei Complementar nº 116, de 31 de julho de 2003",
            "urn": "urn:lex:br:federal:lei.complementar:2003-07-31;116",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2003-07-31;116",
            "numero": "116",
            "ano": "2003",
            "tipo": "Lei Complementar",
            "tema": "Serviços e Retenções",
            "tributos": ["ISSQN"],
            "ementa": "Dispõe sobre o Imposto Sobre Serviços de Qualquer Natureza, de competência dos Municípios e do Distrito Federal, e dá outras providências.",
            "pasta": "federal/leis-complementares/iss"
        },
        {
            "titulo": "Lei nº 10.833, de 29 de dezembro de 2003",
            "urn": "urn:lex:br:federal:lei:2003-12-29;10833",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2003-12-29;10833",
            "numero": "10833",
            "ano": "2003",
            "tipo": "Lei Ordinária",
            "tema": "Serviços e Retenções",
            "tributos": ["CSRF (Retenção 4,65%)", "PIS/Pasep", "Cofins"],
            "ementa": "Altera a Legislação Tributária Federal e institui a retenção na fonte da CSLL, do PIS e da COFINS sobre pagamentos efetuados por pessoas jurídicas a outras pessoas jurídicas pela prestação de serviços (CSRF 4,65%).",
            "pasta": "reguladores/rfb/retencoes-servicos"
        }
    ]
}

def importar_leis_estruturantes(pilar: str, itens: list) -> list:
    """Importa e estrutura leis federais de referência via API do Senado/LexML."""
    api_agent = AgenteAPI(rps=1.5)
    arquivos = []
    
    for item in itens:
        print(f"[{pilar.upper()}] Consultando LexML oficial: {item['titulo']} ({item['urn']})...")
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
            caminho = RAIZ / item["pasta"] / f"lei-{item['numero']}-{item['ano']}.md"
            salvar_atomico(caminho, conteudo.encode("utf-8"))
            print(f"[{pilar.upper()}] Salvo com sucesso: {caminho.relative_to(RAIZ)}")
            arquivos.append(caminho)
        except Exception as e:
            print(f"[{pilar.upper()}] Erro ao importar {item['titulo']}: {e}")
            
    return arquivos

def importar_atos_rfb_pilar(pilar: str, termo: str, limite: int = 2) -> list:
    """Coleta e estrutura atos regulamentares e soluções de consulta da RFB por tema."""
    api_agent = AgenteAPI(rps=1.5)
    estruturador = AgenteEstruturador()
    arquivos = []
    
    print(f"[{pilar.upper()}] Consultando API da RFB para termo '{termo}'...")
    try:
        resultado = api_agent.consultar_atos_rfb(termo=termo, pagina=1, tamanho=limite)
        atos = resultado.get("atos", []) if isinstance(resultado, dict) else resultado
        for item in atos[:limite]:
            id_ato = item.get("idAto")
            if id_ato:
                detalhes = api_agent.baixar_corpo_ato_rfb(id_ato)
                dados_completos = {**item, **detalhes}
                md_path = estruturador.estruturar_ato_rfb(dados_completos)
                arquivos.append(md_path)
    except Exception as e:
        print(f"[{pilar.upper()}] Erro ao buscar atos da RFB: {e}")
        
    return arquivos

def tarefa_pilar(pilar: str, termo_rfb: str, leis: list) -> list:
    """Tarefa completa de um pilar executada em thread separada."""
    print(f"\n>>> INICIANDO TRABALHO DO PILAR: {pilar.upper()} <<<")
    docs_estruturantes = importar_leis_estruturantes(pilar, leis)
    docs_rfb = importar_atos_rfb_pilar(pilar, termo_rfb, limite=2)
    total_pilar = docs_estruturantes + docs_rfb
    print(f">>> PILAR {pilar.upper()} FINALIZADO: {len(total_pilar)} DOCUMENTOS GERADOS <<<\n")
    return total_pilar

def main():
    print("=" * 65)
    print("INICIANDO IMPORTAÇÃO PARALELA MULTIAGENTE NOS 4 PILARES")
    print("=" * 65)
    
    tarefas = [
        ("dividendos", "juros sobre o capital próprio", LEIS_ESTRUTURANTES["dividendos"]),
        ("folha", "contribuições previdenciárias folha", LEIS_ESTRUTURANTES["folha"]),
        ("produtos", "icms substituição tributária", LEIS_ESTRUTURANTES["produtos"]),
        ("servicos", "retenção na fonte prestação de serviços", LEIS_ESTRUTURANTES["servicos"])
    ]
    
    todos_arquivos = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        futuros = {
            executor.submit(tarefa_pilar, pilar, termo, leis): pilar
            for pilar, termo, leis in tarefas
        }
        for fut in as_completed(futuros):
            pilar = futuros[fut]
            try:
                gerados = fut.result()
                todos_arquivos.extend(gerados)
            except Exception as e:
                print(f"[ERRO NO PILAR {pilar}]: {e}")
                
    print("\n" + "=" * 65)
    print(f"IMPORTAÇÃO CONCLUÍDA: {len(todos_arquivos)} DOCUMENTOS NOVOS/ATUALIZADOS.")
    print("ACIONANDO O AGENTE AUDITOR PARA CONFERÊNCIA INDEPENDENTE...")
    print("=" * 65)
    
    auditor = AgenteAuditor()
    relatorio = auditor.auditar_repositorio(checar_rede=True)
    
    print("\nATUALIZANDO PROGRESSO.MD...")
    gerar_progresso()
    
    print("\nACIONANDO O AGENTE GIT...")
    git_agent = AgenteGit()
    git_agent.registrar_worklog(
        f"Importação paralela concluída nos 4 pilares (Dividendos, Folha, Produtos, Serviços). "
        f"Total de arquivos gerados/revisados: {len(todos_arquivos)}. "
        f"Auditoria independente: {relatorio['aprovados']} aprovados, {relatorio['rejeitados']} rejeitados."
    )
    print("\n=== PIPELINE MULTIAGENTE PARALELO FINALIZADO COM SUCESSO ===")

if __name__ == "__main__":
    main()
