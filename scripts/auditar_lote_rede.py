"""Auditoria de esquema e de rede (`--rede`) restrita a um lote de documentos.

Uso: python3 scripts/auditar_lote_rede.py caminho1.md caminho2.md ...
Retorna código de saída 1 se algum documento for rejeitado. Útil para lotes pequenos,
evitando a verificação de rede dos mais de mil documentos do acervo.
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))
from agente_auditor import AgenteAuditor  # noqa: E402

if __name__ == "__main__":
    auditor = AgenteAuditor(rps=1.0)
    reprovados = 0
    for caminho in sys.argv[1:]:
        ok, erros = auditor.auditar_documento(RAIZ / caminho, checar_rede=True)
        print(("APROVADO " if ok else "REJEITADO"), caminho, "" if ok else erros)
        reprovados += 0 if ok else 1
    print(f"{len(sys.argv) - 1 - reprovados} aprovados, {reprovados} rejeitados")
    sys.exit(1 if reprovados else 0)
