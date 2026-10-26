"""Publica o conteúdo da pasta wiki/ no repositório oficial da GitHub Wiki (tributos.wiki.git)."""
from pathlib import Path
import os
import re
import subprocess

RAIZ = Path(__file__).resolve().parent.parent
WIKI_DIR = RAIZ / "wiki"
DESTINO = Path("/tmp/tributos_wiki")

def adaptar_conteudo_para_github_wiki(texto: str) -> str:
    # 1. Links relativos para o repositório principal de código
    # Ex: (../federal/...) -> (https://github.com/brunoqualhato/tributos/blob/main/federal/...)
    texto = re.sub(
        r'\(\.\./([^\)]+)\)',
        r'(https://github.com/brunoqualhato/tributos/blob/main/\1)',
        texto
    )
    # 2. Links entre páginas da própria Wiki (.md removido para URL nativa da wiki)
    # Ex: (Pilar-1-Dividendos-e-Renda-do-Capital.md) -> (Pilar-1-Dividendos-e-Renda-do-Capital)
    texto = re.sub(
        r'\(([a-zA-Z0-9_\-]+)\.md\)',
        r'(\1)',
        texto
    )
    return texto

def gerar_sidebar() -> str:
    return """### 📚 [Home](Home)

---

### Os 9 Pilares Tributários
1. 💰 [1. Dividendos e JCP](Pilar-1-Dividendos-e-Renda-do-Capital)
2. 👥 [2. Folha e Encargos](Pilar-2-Folha-de-Pagamento-e-Encargos)
3. 📦 [3. Produtos e ICMS](Pilar-3-Produtos-Mercadorias-e-ICMS)
4. 🛠️ [4. Serviços e ISS](Pilar-4-Servicos-e-Retencoes)
5. 🏰 [5. Patrimônio e Veículos](Pilar-5-Patrimonio-Heranca-e-Veiculos)
6. ⛽ [6. Combustíveis e CIDE](Pilar-6-Combustiveis-e-Energia)
7. 📈 [7. Financeiro e IOF](Pilar-7-Tributacao-Financeira-e-IOF)
8. 🚀 [8. Reforma & Split Payment](Pilar-8-Reforma-Tributaria-e-Split-Payment)
9. 📊 [9. Contabilidade (CPC/CFC)](Pilar-9-Normas-Contabeis-CPC-e-CFC)

---

### Governança e Automação
- 🤖 [Arquitetura dos Agentes](Arquitetura-dos-Agentes-e-Automacao)
- 📖 [Catálogo do Acervo](https://github.com/brunoqualhato/tributos/blob/main/ACERVO.md)
- 📊 [Quadro de Progresso](https://github.com/brunoqualhato/tributos/blob/main/PROGRESSO.md)
- 📝 [Worklog Auditável](https://github.com/brunoqualhato/tributos/blob/main/WORKLOG.md)
"""

def main():
    if not DESTINO.exists():
        print(f"Erro: diretório {DESTINO} não encontrado. Clone o tributos.wiki.git primeiro.")
        return

    # Processa cada arquivo da wiki
    for md_file in WIKI_DIR.glob("*.md"):
        conteudo = md_file.read_text(encoding="utf-8")
        conteudo_adaptado = adaptar_conteudo_para_github_wiki(conteudo)
        dest_file = DESTINO / md_file.name
        dest_file.write_text(conteudo_adaptado, encoding="utf-8")
        print(f"[Wiki] Processado: {md_file.name} -> {dest_file}")

    # Cria _Sidebar.md
    sidebar_file = DESTINO / "_Sidebar.md"
    sidebar_file.write_text(gerar_sidebar(), encoding="utf-8")
    print("[Wiki] Criado: _Sidebar.md")

    # Git commit e push no tributos.wiki.git
    subprocess.run(["git", "config", "user.name", "Bruno Qualhato"], cwd=DESTINO, check=True)
    subprocess.run(["git", "config", "user.email", "brunoqualhato@users.noreply.github.com"], cwd=DESTINO, check=True)
    subprocess.run(["git", "add", "."], cwd=DESTINO, check=True)
    
    status = subprocess.run(["git", "status", "--porcelain"], cwd=DESTINO, capture_output=True, text=True)
    if status.stdout.strip():
        subprocess.run(["git", "commit", "-m", "docs: publica os 10 guias dos 9 pilares e sidebar na GitHub Wiki"], cwd=DESTINO, check=True)
        subprocess.run(["git", "push", "origin", "master"], cwd=DESTINO, check=True)
        print("\n✅ GitHub Wiki atualizada com sucesso no servidor do GitHub!")
    else:
        print("\nNenhuma alteração pendente na GitHub Wiki.")

if __name__ == "__main__":
    main()
