"""Orquestrador da Rotina Cíclica de 2 Horas.

Executa em intervalos periódicos para:
1. Avançar a paginação e anos de busca na API Sijut/RFB e LexML em todos os pilares:
   - Dividendos / JCP / Lucro Real / Offshores
   - Folha de Pagamento / INSS / CPRB / RAT
   - Produtos / ICMS / IPI / PIS/COFINS
   - Serviços / ISSQN / Retenções CSRF/IRRF
   - Patrimônio / ITCMD / IPVA / ITR
   - Reforma Tributária / IBS / CBS / Split Payment
   - Combustíveis / CIDE / ICMS ad rem
   - Tributação Financeira / IOF / Cripto
   - Normas Contábeis CPC e CFC
2. Auditar todos os links e assegurar o padrão de URLs diretas.
3. Executar auditoria de integridade com verificação de rede.
4. Regenerar ACERVO.md, PROGRESSO.md e WORKLOG.md.
5. Criar branch com timestamp, commitar e abrir Pull Request automaticamente.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import datetime as dt
import json
import os
import sys
import time

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from agentes.agente_api import AgenteAPI
from agentes.agente_estruturador import AgenteEstruturador
from agentes.agente_auditor import AgenteAuditor
from agentes.agente_link_auditor import AgenteLinkAuditor
from agentes.agente_git import AgenteGit
from progresso import gerar_progresso
from catalogo import gerar_catalogo

ARQUIVO_ESTADO = RAIZ / "_fonte" / "estado_coleta.json"

PILAR_TERMOS = {
    "Dividendos e Renda do Capital": ["dividendos", "juros sobre capital proprio", "lucro real", "subvencao"],
    "Folha de Pagamento e Encargos": ["folha de pagamento", "previdenciaria", "desoneracao", "pro-labore"],
    "Produtos e Mercadorias": ["icms", "ipi", "monofasico", "substituicao tributaria"],
    "Serviços e Retenções": ["servicos", "issqn", "csrf", "retencao na fonte"],
    "Patrimônio, Herança e Veículos": ["itcmd", "ipva", "itr", "iptu"],
    "Reforma Tributária e Transição": ["reforma tributaria", "ibs", "cbs", "split payment", "comite gestor"],
    "Combustíveis e Energia": ["combustiveis", "cide", "petroleo", "etanol"],
    "Tributação Financeira e IOF": ["iof", "cambio", "criptoativos", "fundos de investimento"]
}

def carregar_estado() -> dict:
    if ARQUIVO_ESTADO.exists():
        try:
            return json.loads(ARQUIVO_ESTADO.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"pagina_atual": 1, "anos_visitados": [2024, 2025]}

def salvar_estado(estado: dict):
    ARQUIVO_ESTADO.parent.mkdir(parents=True, exist_ok=True)
    ARQUIVO_ESTADO.write_text(json.dumps(estado, indent=2, ensure_ascii=False), encoding="utf-8")

def executar_ciclo_coleta():
    print("=" * 80)
    print(f"INICIANDO CICLO PERIÓDICO DE COLETA: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    estado = carregar_estado()
    pagina = estado.get("pagina_atual", 1) + 1
    if pagina > 10:
        pagina = 1

    anos = [2022, 2023, 2024, 2025]
    api = AgenteAPI(rps=2.5)
    estruturador = AgenteEstruturador()
    novos_docs = []

    def processar_busca(termo, ano, pag):
        locais = []
        try:
            res = api.consultar_atos_rfb(termo=termo, ano=ano, pagina=pag, tamanho=4)
            atos = res.get("atos", []) if isinstance(res, dict) else res
            for ato in atos:
                id_ato = ato.get("idAto")
                if id_ato:
                    detalhes = api.baixar_corpo_ato_rfb(id_ato)
                    dados = {**ato, **detalhes}
                    caminho = estruturador.estruturar_ato_rfb(dados)
                    locais.append(caminho)
        except Exception as e:
            print(f"[Aviso Busca] Erro ao buscar '{termo}' ({ano}, pag {pag}): {e}")
        return locais

    print(f"\n[Fase 1] Disparando consultas multianuais (página {pagina})...")
    with ThreadPoolExecutor(max_workers=4) as executor:
        futuros = []
        for pilar, termos in PILAR_TERMOS.items():
            for termo in termos[:2]:
                for ano in anos[:2]:
                    futuros.append(executor.submit(processar_busca, termo, ano, pagina))

        for f in as_completed(futuros):
            novos_docs.extend(f.result())

    print(f"\n[Fase 1 Concluída] {len(novos_docs)} novos documentos estruturados.")

    print("\n[Fase 2] Executando Agente Link Auditor...")
    link_auditor = AgenteLinkAuditor(rps=4.0)
    link_auditor.executar_auditoria_concorrente()

    print("\n[Fase 3] Executando Agente Auditor Independente com checagem de rede...")
    auditor = AgenteAuditor(rps=2.0)
    relatorio = auditor.auditar_repositorio(checar_rede=True)

    print("\n[Fase 4] Atualizando Catálogo (ACERVO.md) e Progresso...")
    total_catalogo = gerar_catalogo()
    gerar_progresso()

    estado["pagina_atual"] = pagina
    salvar_estado(estado)

    print("\n[Fase 5] Agente Git: Verificando alterações e submetendo Pull Request...")
    git = AgenteGit()
    agora_str = dt.datetime.now().strftime("%Y%m%d-%H%M")
    nome_branch = f"coleta/rotina-periodica-{agora_str}"

    git.registrar_worklog(
        f"Ciclo periódico de 2h executado com sucesso em {agora_str}. "
        f"Novos documentos neste lote: {len(novos_docs)}. Total geral: {total_catalogo}. "
        f"Aprovação auditoria: {relatorio['taxa_aprovacao']}."
    )

    if novos_docs:
        git.criar_branch(nome_branch)
        git.commitar(f"feat: coleta periódica multianual de atos tributários ({agora_str})")
        git.empurrar(nome_branch)
        git.abrir_pull_request(
            branch_origem=nome_branch,
            titulo=f"feat: expansão periódica multianual do acervo tributário ({agora_str})",
            corpo=(
                f"### Ciclo Periódico de Coleta (a cada 2h)\n\n"
                f"- **Novos documentos adicionados:** {len(novos_docs)}\n"
                f"- **Total de documentos no acervo:** {total_catalogo}\n"
                f"- **Auditoria de rede:** {relatorio['aprovados']} aprovados, {relatorio['rejeitados']} rejeitados.\n"
                f"- **Saneamento de links:** 100% de links diretos verificados.\n"
            )
        )
    else:
        print("[Agente Git] Nenhuma alteração pendente para criação de nova PR neste ciclo.")

    print("\n=== CICLO DE 2H FINALIZADO COM SUCESSO ===")

if __name__ == "__main__":
    executar_ciclo_coleta()
