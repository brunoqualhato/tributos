"""Orquestrador da Esteira Multiagente Tributária e Contábil.

Coordena a atuação dos 4 agentes especialistas:
1. tax-api-collector (Coleta de APIs estruturadas)
2. tax-web-scraper (Scraping de fontes sem API)
3. tax-doc-structurer (Parsing e estruturação Markdown)
4. tax-git-workflow (Auditoria, PROGRESSO.md e Git commits/PRs)
"""
from pathlib import Path
import sys
import argparse

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from agentes.agente_api import AgenteAPI
from agentes.agente_scraping import AgenteScraping
from agentes.agente_estruturador import AgenteEstruturador
from agentes.agente_git import AgenteGit
from auditar import executar_auditoria
from progresso import gerar_progresso

def executar_ciclo_exemplo_rfb(termo: str = "imposto", limite: int = 2):
    print("=== INICIANDO CICLO MULTIAGENTE TRIBUTÁRIO ===")
    
    # 1. Agente de API
    api_agent = AgenteAPI()
    print(f"\n[Etapa 1] Agente de API consultando Receita Federal (termo='{termo}')...")
    resultado = api_agent.consultar_atos_rfb(termo=termo, pagina=1, tamanho=limite)
    
    lista_atos = resultado.get("atos", []) if isinstance(resultado, dict) else resultado
    if not lista_atos and isinstance(resultado, list):
        lista_atos = resultado

    # 2. Agente Estruturador
    estruturador = AgenteEstruturador()
    arquivos_gerados = []
    print("\n[Etapa 2] Agente Estruturador convertendo para CommonMark + YAML...")
    for item in lista_atos[:limite]:
        id_ato = item.get("idAto")
        if id_ato:
            detalhes = api_agent.baixar_corpo_ato_rfb(id_ato)
            dados_completos = {**item, **detalhes}
            md_path = estruturador.estruturar_ato_rfb(dados_completos)
            arquivos_gerados.append(md_path)

    # 3. Auditoria de Qualidade
    print("\n[Etapa 3] Auditoria de Integridade...")
    valido = executar_auditoria()

    # 4. Atualização de Progresso
    print("\n[Etapa 4] Recalculando PROGRESSO.md...")
    gerar_progresso()

    # 5. Agente Git
    print("\n[Etapa 5] Agente Git registrando histórico...")
    git_agent = AgenteGit()
    git_agent.registrar_worklog(
        f"Lote RFB ('{termo}') processado com sucesso. {len(arquivos_gerados)} documentos gerados e auditados."
    )
    print("=== CICLO MULTIAGENTE CONCLUÍDO COM SUCESSO ===")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--termo", type=str, default="imposto")
    parser.add_argument("--limite", type=int, default=2)
    args = parser.parse_args()
    executar_ciclo_exemplo_rfb(termo=args.termo, limite=args.limite)
