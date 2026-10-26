"""Gera o catálogo auditado de todos os documentos presentes no acervo (ACERVO.md).

Varre os arquivos Markdown do repositório, extrai os metadados do frontmatter YAML
e organiza um índice estruturado, pesquisável e categorizado pelos pilares tributários.
"""
from pathlib import Path
import json
import re
import sys
import datetime as dt

RAIZ = Path(__file__).resolve().parent.parent

def extrair_metadados(conteudo: str) -> dict:
    if not conteudo.startswith("---"):
        return {}
    partes = conteudo.split("---", 2)
    if len(partes) < 3:
        return {}
    
    cabecalho = partes[1]
    meta = {}
    for linha in cabecalho.strip().split("\n"):
        m = re.match(r"^(\w+):\s*(.*)$", linha)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1].replace('\\"', '"')
            elif v.startswith("[") and v.endswith("]"):
                itens = [i.strip().strip('"') for i in v[1:-1].split(",") if i.strip()]
                v = itens
            elif v.lower() == "true":
                v = True
            elif v.lower() == "false":
                v = False
            elif v.lower() == "null":
                v = None
            meta[k] = v
    return meta

def gerar_catalogo():
    documentos = []
    
    for p in sorted(RAIZ.glob("**/*.md")):
        if p.name in ("README.md", "PROGRESSO.md", "PLANO.md", "WORKLOG.md", "COBERTURA.md", "AGENT.md", "ACERVO.md"):
            continue
        if any(part.startswith(".") or part.startswith("_") or part == "wiki" for part in p.parts):
            continue
            
        conteudo = p.read_text(encoding="utf-8")
        meta = extrair_metadados(conteudo)
        if meta and "titulo" in meta:
            meta["_caminho"] = str(p.relative_to(RAIZ))
            documentos.append(meta)

    # Ordenação por ano e título
    documentos.sort(key=lambda x: (str(x.get("ano", "0")), str(x.get("numero", "0")), x.get("titulo", "")))

    linhas = [
        "# Catálogo Geral do Acervo Tributário e Contábil (ACERVO.md)",
        "",
        f"Documento gerado automaticamente em **{dt.datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}**.",
        "",
        f"**Total de Documentos Catalogados e Auditados:** `{len(documentos)}`",
        "",
        "---",
        "",
        "## Sumário Executivo por Pilar",
        ""
    ]

    # Agrupamento por tema_tributario
    grupos = {}
    for doc in documentos:
        tema = doc.get("tema_tributario") or "Tributário e Contábil Geral"
        grupos.setdefault(tema, []).append(doc)

    for tema, docs in sorted(grupos.items()):
        linhas.append(f"- **{tema}:** `{len(docs)}` documentos")
    linhas.append("")
    linhas.append("---")
    linhas.append("")

    # Tabelas detalhadas por Pilar
    for tema, docs in sorted(grupos.items()):
        linhas.append(f"## {tema} ({len(docs)} documentos)")
        linhas.append("")
        linhas.append("| Norma / Título | Ano | Órgão | Tributos Afetados | Situação | Link Direto Oficial | Arquivo Local |")
        linhas.append("| :--- | :---: | :--- | :--- | :---: | :---: | :--- |")
        
        for d in docs:
            titulo = d.get("titulo", "")
            ano = d.get("ano", "-")
            orgao = d.get("orgao", "-")
            tribs = d.get("tributos_afetados")
            if isinstance(tribs, list):
                tribs_str = ", ".join(tribs)
            elif tribs:
                tribs_str = str(tribs)
            else:
                tribs_str = "-"
                
            situacao = d.get("situacao", "Em vigor")
            fonte = d.get("fonte", "")
            link_md = f"[Visualizar na Fonte Oficial]({fonte})" if fonte else "-"
            caminho_md = f"[`{d['_caminho']}`]({d['_caminho']})"
            
            linhas.append(f"| **{titulo}** | {ano} | {orgao} | {tribs_str} | {situacao} | {link_md} | {caminho_md} |")
        linhas.append("")

    saida_md = RAIZ / "ACERVO.md"
    saida_md.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"[Catálogo] ACERVO.md gerado com sucesso! {len(documentos)} normas documentadas.")
    return len(documentos)

if __name__ == "__main__":
    gerar_catalogo()
