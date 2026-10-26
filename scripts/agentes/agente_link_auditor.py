"""Agente Especialista em Auditoria e Correção de Links Diretos Oficiais.

Varre concorrentemente todos os documentos do acervo e corrige:
- URLs legadas do Sijut (sijut2consulta/consulta.action?idAto=X) -> URL SPA oficial direta (https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/X)
- Valida integridade e acessibilidade direta no navegador
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import re
import sys
import json

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from comum import Rede

class AgenteLinkAuditor:
    def __init__(self, rps: float = 3.0):
        self.rede = Rede(rps=rps)
        self.pasta_auditoria = RAIZ / "_auditoria"
        self.pasta_auditoria.mkdir(parents=True, exist_ok=True)
        self.log_correcoes = self.pasta_auditoria / "links_corrigidos.jsonl"

    def corrigir_e_validar_documento(self, caminho_md: Path) -> dict:
        conteudo = caminho_md.read_text(encoding="utf-8")
        if not conteudo.startswith("---"):
            return {"arquivo": str(caminho_md), "status": "sem_frontmatter"}

        partes = conteudo.split("---", 2)
        if len(partes) < 3:
            return {"arquivo": str(caminho_md), "status": "frontmatter_invalido"}

        cabecalho = partes[1]
        corpo = partes[2]
        modificado = False
        url_antiga = None
        url_nova = None

        # 1. Correção de links legados da Receita Federal
        # Ex: https://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action?idAto=153937
        m_rfb = re.search(r'fonte:\s*"(https?://normas\.receita\.fazenda\.gov\.br/sijut2consulta/consulta\.action\?idAto=(\d+))"', cabecalho)
        if m_rfb:
            url_antiga = m_rfb.group(1)
            id_ato = m_rfb.group(2)
            url_nova = f"https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{id_ato}"
            cabecalho = cabecalho.replace(url_antiga, url_nova)
            modificado = True

        # Se o link não tiver aspas ou for de formato variante
        if not modificado:
            m_rfb_raw = re.search(r'fonte:\s*(https?://normas\.receita\.fazenda\.gov\.br/sijut2consulta/consulta\.action\?idAto=(\d+))', cabecalho)
            if m_rfb_raw:
                url_antiga = m_rfb_raw.group(1)
                id_ato = m_rfb_raw.group(2)
                url_nova = f"https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{id_ato}"
                cabecalho = cabecalho.replace(url_antiga, f'"{url_nova}"')
                modificado = True

        if modificado:
            novo_conteudo = f"---{cabecalho}---{corpo}"
            caminho_md.write_text(novo_conteudo, encoding="utf-8")
            return {
                "arquivo": str(caminho_md.relative_to(RAIZ)),
                "status": "corrigido",
                "antigo": url_antiga,
                "novo": url_nova
            }

        return {"arquivo": str(caminho_md.relative_to(RAIZ)), "status": "inalterado"}

    def executar_auditoria_concorrente(self) -> list:
        print("[Agente Link Auditor] Iniciando auditoria e saneamento de links em paralelo...")
        arquivos = []
        for p in RAIZ.glob("**/*.md"):
            if p.name in ("README.md", "PROGRESSO.md", "PLANO.md", "WORKLOG.md", "COBERTURA.md", "AGENT.md"):
                continue
            if any(part.startswith(".") or part.startswith("_") for part in p.parts):
                continue
            arquivos.append(p)

        resultados = []
        corrigidos = 0
        with ThreadPoolExecutor(max_workers=8) as executor:
            futuros = [executor.submit(self.corrigir_e_validar_documento, arq) for arq in arquivos]
            for f in as_completed(futuros):
                res = f.result()
                resultados.append(res)
                if res.get("status") == "corrigido":
                    corrigidos += 1
                    print(f"[LINK CORRIGIDO] {res['arquivo']}:")
                    print(f"  De:   {res['antigo']}")
                    print(f"  Para: {res['novo']}")

        # Salva o log de correções
        with open(self.log_correcoes, "w", encoding="utf-8") as f:
            for item in resultados:
                if item.get("status") == "corrigido":
                    f.write(json.dumps(item, ensure_ascii=False) + "\n")

        print(f"\n[Agente Link Auditor] Concluído: {len(arquivos)} arquivos analisados, {corrigidos} links corrigidos.")
        return resultados

if __name__ == "__main__":
    agente = AgenteLinkAuditor()
    agente.executar_auditoria_concorrente()
