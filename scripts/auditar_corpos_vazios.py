from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

ignored_names = {'README.md', 'PROGRESSO.md', 'PLANO.md', 'WORKLOG.md', 'COBERTURA.md', 'AGENT.md', 'ACERVO.md'}
ignored_dirs = {'_auditoria', '_fonte', 'wiki'}

docs = [p for p in RAIZ.glob('**/*.md') if not any(part.startswith('.') for part in p.parts) and p.name not in ignored_names and not any(part in ignored_dirs for part in p.parts)]

empty_bodies = []
tiny_bodies = []

for p in sorted(docs):
    text = p.read_text(encoding='utf-8', errors='replace')
    parts = text.split('---', 2)
    if len(parts) < 3:
        empty_bodies.append((str(p.relative_to(RAIZ)), "Sem frontmatter"))
        continue
    body = parts[2].strip()
    body_lines = [l for l in body.splitlines() if l.strip() and not l.startswith('# ')]
    body_text = '\n'.join(body_lines).strip()
    if len(body_text) == 0:
        empty_bodies.append((str(p.relative_to(RAIZ)), "Corpo completamente vazio"))
    elif len(body_lines) < 3 or len(body_text) < 50:
        tiny_bodies.append((str(p.relative_to(RAIZ)), len(body_lines), len(body_text)))

print(f"Total documentos analisados: {len(docs)}")
print(f"Documentos com corpo vazio: {len(empty_bodies)}")
for item in empty_bodies:
    print(f"  {item[0]}: {item[1]}")

print(f"\nDocumentos com corpo minusculo (<3 linhas úteis ou <50 chars): {len(tiny_bodies)}")
for item in tiny_bodies[:30]:
    print(f"  {item[0]} ({item[1]} linhas, {item[2]} chars)")
