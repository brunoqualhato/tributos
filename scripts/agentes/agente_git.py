"""Agente Especialista em Git, Pull Requests e Issues.

Responsável por:
- Criar branches temáticas de coletas
- Montar commits semânticos com signatários e datas históricas
- Abrir e atualizar Pull Requests e Issues no GitHub via `gh` CLI
- Registrar marcos no WORKLOG.md e atualizar o PROGRESSO.md
"""
from pathlib import Path
import subprocess
import datetime as dt
import sys

RAIZ = Path(__file__).resolve().parent.parent.parent

class AgenteGit:
    def __init__(self):
        pass

    def executar(self, cmd: list, check: bool = True) -> str:
        res = subprocess.run(cmd, cwd=str(RAIZ), capture_output=True, text=True)
        if check and res.returncode != 0:
            raise RuntimeError(f"Erro no comando {' '.join(cmd)}: {res.stderr}")
        return res.stdout.strip()

    def criar_branch(self, nome_branch: str):
        """Cria e comuta para uma nova branch de lote."""
        print(f"[Agente Git] Criando branch: {nome_branch}")
        self.executar(["git", "checkout", "-b", nome_branch])

    def comitar_lote(self, mensagem: str, arquivos: list = None, autor: str = "TributosBot <bot@tributos.org>"):
        """Adiciona arquivos e gera o commit."""
        if arquivos:
            for arq in arquivos:
                self.executar(["git", "add", str(arq)])
        else:
            self.executar(["git", "add", "."])

        print(f"[Agente Git] Gerando commit: {mensagem}")
        self.executar(["git", "commit", "--author", autor, "-m", mensagem])

    def abrir_pr(self, titulo: str, corpo: str, base: str = "main") -> str:
        """Abre Pull Request no GitHub usando a gh CLI."""
        print(f"[Agente Git] Abrindo PR: {titulo}")
        try:
            saida = self.executar(["gh", "pr", "create", "--base", base, "--title", titulo, "--body", corpo])
            print(f"[Agente Git] PR criada: {saida}")
            return saida
        except Exception as e:
            print(f"[Agente Git] Aviso: Não foi possível abrir PR via gh CLI: {e}")
            return ""

    def abrir_issue(self, titulo: str, corpo: str, labels: list = None) -> str:
        """Abre uma Issue no GitHub para rastreamento de lote ou pendência de integridade."""
        print(f"[Agente Git] Abrindo Issue: {titulo}")
        cmd = ["gh", "issue", "create", "--title", titulo, "--body", corpo]
        if labels:
            cmd.extend(["--label", ",".join(labels)])
        try:
            saida = self.executar(cmd)
            print(f"[Agente Git] Issue criada: {saida}")
            return saida
        except Exception as e:
            print(f"[Agente Git] Aviso: Não foi possível abrir Issue via gh CLI: {e}")
            return ""

    def registrar_worklog(self, entrada: str):
        """Acrescenta um registro auditável ao WORKLOG.md."""
        worklog = RAIZ / "WORKLOG.md"
        data_str = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        bloco = f"\n## {data_str}\n\n{entrada.strip()}\n"
        if worklog.exists():
            conteudo = worklog.read_text(encoding="utf-8") + bloco
        else:
            conteudo = "# Histórico de Execuções e Auditoria (WORKLOG)\n" + bloco
        worklog.write_text(conteudo, encoding="utf-8")
        print("[Agente Git] WORKLOG.md atualizado.")

if __name__ == "__main__":
    agente = AgenteGit()
    agente.registrar_worklog("Inicialização do repositório de Tributos e Contabilidade com 4 agentes especialistas.")
