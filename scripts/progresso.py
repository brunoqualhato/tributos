"""Calcula a cobertura atual do acervo contra o scripts/plano.py e gera o PROGRESSO.md."""
from pathlib import Path
import sys
import datetime as dt

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from plano import PLANO, contar_documentos

def gerar_progresso():
    linhas = [
        "# Progresso do Acervo Tributário e Contábil",
        "",
        f"Gerado em: {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}. Escopo definido em `scripts/plano.py`.",
        "",
        "| Pilar / Subtema | Documentos | Meta | Cobertura | Pasta | Fonte Principal |",
        "| :--- | ---: | ---: | :---: | :--- | :--- |"
    ]

    total_docs = 0
    total_meta = 0
    setor_atual = None

    for item in PLANO:
        if item.setor != setor_atual:
            setor_atual = item.setor
            linhas.append(f"| **### {setor_atual}** | | | | | |")
            
        qtd = contar_documentos(item.caminho)
        total_docs += qtd
        total_meta += item.meta
        perc = f"{(qtd / item.meta * 100):.1f}%" if item.meta > 0 else "-"
        status = "✅" if qtd >= item.meta else ("🟦" if qtd > 0 else "⬜️")
        linhas.append(f"| {status} **{item.pilar}**: {item.nome} | {qtd} | {item.meta} | {perc} | `{item.caminho}` | {item.fonte} |")

    linhas.insert(4, f"**Total de Documentos no Acervo:** {total_docs} / {total_meta} ({((total_docs/total_meta*100) if total_meta else 0):.1f}%)")
    linhas.insert(5, "")

    progresso_md = RAIZ / "PROGRESSO.md"
    progresso_md.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"PROGRESSO.md atualizado: {total_docs} de {total_meta} documentos mapeados.")

if __name__ == "__main__":
    gerar_progresso()
