"""Auditoria de integridade dos arquivos Markdown do repositório."""
from pathlib import Path
import re
import sys

RAIZ = Path(__file__).resolve().parent.parent

def auditar_arquivo(caminho: Path) -> list:
    erros = []
    conteudo = caminho.read_text(encoding="utf-8")
    
    if not conteudo.startswith("---"):
        erros.append("Ausência de abertura de frontmatter (---)")
        return erros
        
    partes = conteudo.split("---", 2)
    if len(partes) < 3:
        erros.append("Frontmatter malformado (não fecha com ---)")
        return erros
        
    cabecalho = partes[1]
    corpo = partes[2].strip()
    
    # Validação de campos obrigatórios
    campos_obrigatorios = ["titulo:", "esfera:", "tipo:", "numero:", "ementa:"]
    for campo in campos_obrigatorios:
        if campo not in cabecalho:
            erros.append(f"Campo obrigatório ausente no cabeçalho: {campo}")
            
    if not corpo:
        erros.append("Corpo do documento vazio após o cabeçalho")
    elif not corpo.startswith("# "):
        erros.append("O corpo do documento deve iniciar com título em '# '")
        
    return erros

def executar_auditoria():
    total_docs = 0
    erros_encontrados = 0
    
    for ext in ("*.md",):
        for path in RAIZ.glob(f"**/{ext}"):
            if path.name in ("README.md", "PROGRESSO.md", "PLANO.md", "WORKLOG.md", "COBERTURA.md"):
                continue
            if "_fonte" in path.parts:
                continue
            total_docs += 1
            falhas = auditar_arquivo(path)
            if falhas:
                erros_encontrados += 1
                print(f"[FALHA] {path.relative_to(RAIZ)}:")
                for f in falhas:
                    print(f"  - {f}")
                    
    print(f"\nAuditoria concluída: {total_docs} documentos verificados, {erros_encontrados} falhas encontradas.")
    return erros_encontrados == 0

if __name__ == "__main__":
    sucesso = executar_auditoria()
    sys.exit(0 if sucesso else 1)
