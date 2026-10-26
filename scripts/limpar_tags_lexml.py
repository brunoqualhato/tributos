"""Remove marcadores brutos de controle LexML (ex: ###LEI-005172-251066@@@) dos arquivos."""
from pathlib import Path
import re

RAIZ = Path(__file__).resolve().parent.parent

padrao_tag = re.compile(r'###[A-Z0-9_-]+@@@')

corrigidos = 0
for p in sorted(RAIZ.glob("**/*.md")):
    if p.name in ("README.md", "PROGRESSO.md", "PLANO.md", "WORKLOG.md", "COBERTURA.md", "AGENT.md", "ACERVO.md"):
        continue
    if any(part.startswith(".") or part.startswith("_") or part == "wiki" for part in p.parts):
        continue
    
    content = p.read_text(encoding="utf-8")
    if padrao_tag.search(content):
        novo_content = padrao_tag.sub("", content)
        # Limpar quebras de linha duplas desnecessárias deixadas pelas tags
        novo_content = re.sub(r'\n{3,}', '\n\n', novo_content)
        p.write_text(novo_content, encoding="utf-8")
        corrigidos += 1
        print(f"[TAG LEXML LIMPA] {p.relative_to(RAIZ)}")

print(f"\nTotal de arquivos limpos: {corrigidos}")
