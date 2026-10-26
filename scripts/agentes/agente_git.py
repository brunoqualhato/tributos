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
import os

RAIZ = Path(__file__).resolve().parent.parent.parent

class AgenteGit:
    def __init__(self):
        pass

    def _obter_env(self):
        env = os.environ.copy()
        if "GH_TOKEN" not in env:
            try:
                proc = subprocess.run(
                    ["git", "credential", "fill"],
                    input="protocol=https\nhost=github.com\n",
                    text=True,
                    capture_output=True,
                    check=False
                )
                for line in proc.stdout.splitlines():
                    if line.startswith("password="):
                        env["GH_TOKEN"] = line.split("=", 1)[1]
                        break
            except Exception:
                pass
        return env

    def executar(self, cmd: list, check: bool = True) -> str:
        env = self._obter_env()
        res = subprocess.run(cmd, cwd=str(RAIZ), capture_output=True, text=True, env=env)
        if check and res.returncode != 0:
            raise RuntimeError(f"Erro no comando {' '.join(cmd)}: {res.stderr}")
        return res.stdout.strip()

    def criar_branch(self, nome_branch: str):
        """Cria e comuta para uma nova branch de lote."""
        print(f"[Agente Git] Criando branch: {nome_branch}")
        self.executar(["git", "checkout", "-b", nome_branch])

    def commitar(self, mensagem: str, arquivos: list = None, autor: str = "TributosBot <bot@tributos.org>"):
        """Adiciona arquivos especificados (ou todos se None) e gera o commit semântico/atômico."""
        if arquivos:
            for arq in arquivos:
                try:
                    self.executar(["git", "add", str(arq)])
                except Exception as e:
                    if "ignorado" in str(e).lower() or "ignored" in str(e).lower():
                        continue
                    raise
        else:
            self.executar(["git", "add", "."])

        # Verifica se há algo staged antes de commitar
        staged = self.executar(["git", "diff", "--cached", "--name-only"])
        if not staged.strip():
            print(f"[Agente Git] Nada para commitar no stage. Pulando commit: {mensagem}")
            return

        print(f"[Agente Git] Gerando commit: {mensagem}")
        self.executar(["git", "commit", "--author", autor, "-m", mensagem])

    def comitar_lote(self, mensagem: str, arquivos: list = None, autor: str = "TributosBot <bot@tributos.org>"):
        """Alias para commitar."""
        self.commitar(mensagem, arquivos, autor)

    def empurrar(self, nome_branch: str = None):
        """Faz push da branch atual ou especificada para origin."""
        cmd = ["git", "push", "-u", "origin"]
        if nome_branch:
            cmd.append(nome_branch)
        else:
            cmd.append("HEAD")
        print(f"[Agente Git] Fazendo push: {' '.join(cmd)}")
        return self.executar(cmd)

    def abrir_pull_request(self, branch_origem: str = None, titulo: str = "", corpo: str = "", base: str = "main") -> str:
        """Abre Pull Request no GitHub usando a gh CLI."""
        print(f"[Agente Git] Abrindo PR: {titulo}")
        cmd = ["gh", "pr", "create", "--base", base, "--title", titulo, "--body", corpo]
        if branch_origem:
            cmd.extend(["--head", branch_origem])
        try:
            saida = self.executar(cmd)
            print(f"[Agente Git] PR criada: {saida}")
            return saida
        except Exception as e:
            print(f"[Agente Git] Aviso: Não foi possível abrir PR via gh CLI: {e}")
            return ""

    def abrir_pr(self, titulo: str, corpo: str, base: str = "main") -> str:
        """Alias de compatibilidade para abrir_pull_request."""
        return self.abrir_pull_request(titulo=titulo, corpo=corpo, base=base)

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
