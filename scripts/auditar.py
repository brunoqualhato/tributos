"""Ponto de entrada para a auditoria de integridade do acervo."""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from agente_auditor import AgenteAuditor

if __name__ == "__main__":
    auditor = AgenteAuditor()
    checar_rede = "--rede" in sys.argv
    resultado = auditor.auditar_repositorio(checar_rede=checar_rede)
    sys.exit(0 if resultado["rejeitados"] == 0 else 1)
