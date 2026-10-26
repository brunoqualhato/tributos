"""Enriquece o corpo dos atos da RFB que ficaram apenas com a linha de assinatura."""
from pathlib import Path
import re

RAIZ = Path(__file__).resolve().parent.parent

corrigidos = 0
for p in sorted(RAIZ.glob("reguladores/rfb/outros-atos/**/*.md")):
    text = p.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        continue
    
    fm = parts[1]
    body = parts[2].strip()
    
    # Extrair título e ementa do frontmatter
    m_tit = re.search(r'titulo:\s*["\']?([^"\r\n\']+)["\']?', fm)
    m_em = re.search(r'ementa:\s*["\']?(.*?)["\']?\n(?:\w+:|---|\Z)', fm, re.DOTALL)
    
    if not m_tit or not m_em:
        continue
        
    titulo = m_tit.group(1).strip()
    ementa = m_em.group(1).strip().strip('"').strip("'")
    
    # Verificar se o corpo útil é minúsculo
    body_lines = [l for l in body.splitlines() if l.strip() and not l.startswith("# ")]
    body_text = "\n".join(body_lines).strip()
    
    if len(body_text) < 150 and len(ementa) > 150:
        novo_corpo = f"""# {titulo}

## Ementa Oficial

{ementa}

## Autoridade e Conclusão

{body_text if body_text not in ('a', '.', 'a\n.') else 'Publicado pela Secretaria Especial da Receita Federal do Brasil.'}
"""
        p.write_text(f"---{fm}---\n\n{novo_corpo}", encoding="utf-8")
        corrigidos += 1
        print(f"[ENRIQUECIDO] {p.name} (Ementa: {len(ementa)} chars)")

print(f"\nTotal de atos RFB enriquecidos: {corrigidos}")
