"""Agente Auditor Independente.

Verifica a autenticidade, integridade de schema e acessibilidade do link de referência
(fonte oficial) para cada arquivo Markdown gerado no repositório.
"""
from pathlib import Path
import json
import re
import sys
import urllib.parse
import urllib.request

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from comum import Rede

DOMINIOS_OFICIAIS_PERMITIDOS = {
    "planalto.gov.br",
    "receita.fazenda.gov.br",
    "fazenda.gov.br",
    "normas.leg.br",
    "senado.leg.br",
    "camara.leg.br",
    "stf.jus.br",
    "stj.jus.br",
    "carf.fazenda.gov.br",
    "pgfn.gov.br",
    "cfc.org.br",
    "cpc.org.br",
    "in.gov.br",
    "mre.gov.br",
    "sp.gov.br",
    "rj.gov.br",
    "mg.gov.br",
    "leismunicipais.com.br"
}

class AgenteAuditor:
    def __init__(self, rps: float = 2.0):
        self.rede = Rede(rps=rps, timeout=20)
        self.pasta_auditoria = RAIZ / "_auditoria"
        self.pasta_auditoria.mkdir(parents=True, exist_ok=True)
        self.arquivo_falhas = self.pasta_auditoria / "falhas_auditoria.jsonl"
        self.arquivo_relatorio = self.pasta_auditoria / "auditoria_relatorio.json"

    def extrair_metadados(self, conteudo: str) -> tuple[dict, str]:
        if not conteudo.startswith("---"):
            return {}, ""
        partes = conteudo.split("---", 2)
        if len(partes) < 3:
            return {}, ""
        
        cabecalho = partes[1]
        corpo = partes[2].strip()
        
        meta = {}
        for linha in cabecalho.strip().split("\n"):
            m = re.match(r"^(\w+):\s*(.*)$", linha)
            if m:
                k, v = m.group(1), m.group(2).strip()
                if v.startswith('"') and v.endswith('"'):
                    v = v[1:-1].replace('\\"', '"')
                meta[k] = v
        return meta, corpo

    def checar_link_fonte(self, url: str) -> tuple[bool, str]:
        """Valida se a URL é de um órgão oficial confiável e se está acessível."""
        if not url or url == '""' or url == "null":
            return False, "Campo 'fonte' vazio ou nulo"

        # Bloqueio de URL legada da RFB que não carrega o documento direto
        if "sijut2consulta/consulta.action" in url:
            return False, "Link legado da RFB detectado. Deve usar a URL direta: https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{idAto}"

        try:
            parsed = urllib.parse.urlparse(url)
            dominio = parsed.netloc.lower()
            if ":" in dominio:
                dominio = dominio.split(":")[0]
                
            # Verifica se pertence a um domínio oficial permitido
            confiavel = any(dominio == dom or dominio.endswith("." + dom) for dom in DOMINIOS_OFICIAIS_PERMITIDOS)
            if not confiavel:
                return False, f"Domínio não reconhecido na whitelist oficial: {dominio}"
        except Exception as e:
            return False, f"URL de fonte inválida: {url} ({e})"

        # Verificação HTTP HEAD/GET (remove fragmento client-side se houver)
        url_verificacao = url.split("#")[0] if "#" in url else url
        try:
            status, bruto, _ = self.rede.get(url_verificacao, max_tentativas=2)
            if status in (200, 301, 302, 307, 308):
                return True, f"HTTP {status}"
            else:
                return False, f"Fonte respondeu com HTTP {status}"
        except Exception as e:
            return False, f"Falha de conexão com a fonte oficial: {e}"

    def auditar_documento(self, caminho_md: Path, checar_rede: bool = True) -> tuple[bool, list[str]]:
        erros = []
        conteudo = caminho_md.read_text(encoding="utf-8")
        meta, corpo = self.extrair_metadados(conteudo)

        if not meta:
            erros.append("Frontmatter YAML ausente ou corrompido")
            return False, erros

        # 1. Campos obrigatórios
        obrigatorios = ["titulo", "esfera", "orgao", "tipo", "numero", "ano", "situacao", "fonte", "ementa"]
        for campo in obrigatorios:
            if campo not in meta or not meta[campo]:
                erros.append(f"Campo essencial ausente no cabeçalho: '{campo}'")

        # 2. Verificação de tema tributário
        if "tema_tributario" not in meta:
            erros.append("Campo 'tema_tributario' não informado no frontmatter")

        # 3. Verificação do corpo Markdown
        if not corpo:
            erros.append("Corpo do documento vazio após frontmatter")
        elif not corpo.startswith("# "):
            erros.append("O texto deve iniciar com título de nível 1 ('# Título')")

        # 4. Verificação de tags HTML brutas residuais
        tags_proibidas = re.findall(r"<(?:script|style|div|span|p|br|table|tr|td)[\s/>]", corpo, re.I)
        if tags_proibidas:
            erros.append(f"Detectadas {len(tags_proibidas)} tags HTML residuais não convertidas no corpo")

        # 5. Verificação da fonte de referência
        if checar_rede and "fonte" in meta:
            valido, msg = self.checar_link_fonte(meta["fonte"])
            if not valido:
                erros.append(f"Falha na verificação da fonte de referência: {msg}")

        return (len(erros) == 0), erros

    def auditar_repositorio(self, checar_rede: bool = False) -> dict:
        """Audita todos os arquivos Markdown do acervo."""
        total = 0
        aprovados = 0
        rejeitados = 0
        falhas_registro = []

        print(f"[Agente Auditor] Iniciando auditoria do acervo (checar_rede={checar_rede})...")
        for md_path in RAIZ.glob("**/*.md"):
            if md_path.name in ("README.md", "PROGRESSO.md", "PLANO.md", "WORKLOG.md", "COBERTURA.md", "AGENT.md", "ACERVO.md"):
                continue
            if any(part.startswith(".") or part.startswith("_") for part in md_path.parts):
                continue

            total += 1
            sucesso, erros = self.auditar_documento(md_path, checar_rede=checar_rede)
            if sucesso:
                aprovados += 1
            else:
                rejeitados += 1
                registro = {
                    "arquivo": str(md_path.relative_to(RAIZ)),
                    "erros": erros
                }
                falhas_registro.append(registro)
                print(f"[REJEITADO] {md_path.relative_to(RAIZ)}:")
                for e in erros:
                    print(f"  - {e}")

        # Registra log de auditoria
        relatorio = {
            "total_auditado": total,
            "aprovados": aprovados,
            "rejeitados": rejeitados,
            "taxa_aprovacao": f"{(aprovados / total * 100):.1f}%" if total > 0 else "100%"
        }
        self.arquivo_relatorio.write_text(json.dumps(relatorio, indent=2, ensure_ascii=False), encoding="utf-8")
        
        with open(self.arquivo_falhas, "w", encoding="utf-8") as f:
            for item in falhas_registro:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")

        print(f"[Agente Auditor] Concluído: {total} documentos, {aprovados} aprovados, {rejeitados} rejeitados.")
        return relatorio

if __name__ == "__main__":
    auditor = AgenteAuditor()
    checar = "--rede" in sys.argv
    res = auditor.auditar_repositorio(checar_rede=checar)
    sys.exit(0 if res["rejeitados"] == 0 else 1)
