"""Saneia todos os links quebrados identificados na auditoria exaustiva."""
from pathlib import Path
import re

RAIZ = Path(__file__).resolve().parent.parent

PORTAIS_UF = {
    "ac": ("Assembleia Legislativa do Estado do Acre", "https://www.al.ac.leg.br/leis"),
    "al": ("Secretaria da Fazenda do Estado de Alagoas", "https://sefaz.al.gov.br/legislacao"),
    "am": ("Secretaria de Estado da Fazenda do Amazonas", "https://sistemas.sefaz.am.gov.br/legislacao"),
    "ap": ("Assembleia Legislativa do Estado do Amapá", "https://www.al.ap.leg.br"),
    "ba": ("Secretaria da Fazenda do Estado da Bahia", "https://www.sefaz.ba.gov.br"),
    "ce": ("Secretaria da Fazenda do Estado do Ceará", "https://www.sefaz.ce.gov.br"),
    "df": ("Sistema Integrado de Normas Jurídicas do DF (SINJ-DF)", "https://www.sinj.df.gov.br/sinj/Norma"),
    "es": ("Assembleia Legislativa do Estado do Espírito Santo", "https://www.al.es.leg.br"),
    "go": ("Secretaria de Estado da Economia de Goiás / Casa Civil-GO", "https://legisla.casacivil.go.gov.br"),
    "ma": ("Assembleia Legislativa do Estado do Maranhão", "https://www.al.ma.leg.br"),
    "mg": ("Assembleia Legislativa do Estado de Minas Gerais", "https://www.almg.gov.br"),
    "ms": ("Secretaria de Estado de Fazenda de Mato Grosso do Sul", "https://www.sefaz.ms.gov.br/legislacao"),
    "mt": ("Secretaria de Estado de Fazenda de Mato Grosso", "https://www.sefaz.mt.gov.br/legislacao"),
    "pa": ("Secretaria de Estado da Fazenda do Pará", "https://www.sefa.pa.gov.br/legislacao"),
    "pb": ("Secretaria de Estado da Fazenda da Paraíba", "https://www.sefaz.pb.gov.br/legislacao"),
    "pe": ("Secretaria da Fazenda do Estado de Pernambuco", "https://www.sefaz.pe.gov.br/Legislacao/Tributaria"),
    "pi": ("Assembleia Legislativa do Estado do Piauí", "https://www.al.pi.leg.br"),
    "pr": ("Secretaria de Estado da Fazenda do Paraná", "https://www.fazenda.pr.gov.br"),
    "rj": ("Assembleia Legislativa do Estado do Rio de Janeiro", "http://alerjln1.alerj.rj.gov.br"),
    "rn": ("Assembleia Legislativa do Estado do Rio Grande do Norte", "https://www.al.rn.leg.br"),
    "ro": ("Assembleia Legislativa do Estado de Rondônia", "https://www.al.ro.leg.br"),
    "rr": ("Assembleia Legislativa do Estado de Roraima", "https://al.rr.leg.br/legislacao"),
    "rs": ("Assembleia Legislativa do Estado do Rio Grande do Sul", "https://ww3.al.rs.gov.br/filerepository/replegiscomp"),
    "sc": ("Secretaria de Estado da Fazenda de Santa Catarina", "https://legislacao.sef.sc.gov.br"),
    "se": ("Assembleia Legislativa de Sergipe", "https://al.se.leg.br"),
    "sp": ("Secretaria da Fazenda e Planejamento do Estado de São Paulo", "https://legislacao.fazenda.sp.gov.br"),
    "to": ("Assembleia Legislativa do Estado do Tocantins", "https://www.al.to.leg.br"),
}

CORRECOES_PONTUAIS = {
    "estaduais/confaz/convenios-icms/1970/convenio-sinief-sn-1970.md": "https://www.confaz.fazenda.gov.br/legislacao/ajustes/sinief/cvsn_70",
    "municipais/mg/servicos-iss/lei-8725-2003.md": "https://www.cmbh.mg.gov.br/atividade-legislativa/pesquisar-legislacao/lei/8725/2003",
    "municipais/rj/servicos-iss/lei-691-1984.md": "https://www0.rio.rj.gov.br/patrimonio/pastas/legislacao/lei691_84.pdf",
    "estaduais/rj/leis/ipva/lei-2877-1997.md": "http://alerjln1.alerj.rj.gov.br",
    "estaduais/rj/leis/itcmd/lei-7174-2015.md": "http://alerjln1.alerj.rj.gov.br",
    "federal/portarias/mf/portaria-mf-204-2022.md": "https://www.gov.br/fazenda/pt-br",
    "reforma-tributaria/cbs-receita-federal/portaria-mf-34-2024.md": "https://www.gov.br/fazenda/pt-br",
    "reguladores/rfb/rat-fap-terceiros/portaria-interministerial-mps-mf-2-2024-fap.md": "https://www.gov.br/previdencia/pt-br",
    "reguladores/mte-caixa/fgts-esocial/portaria-conjunta-mte-rfb-33-2023.md": "https://www.gov.br/trabalho-e-emprego/pt-br",
    "reguladores/rfb/instrucoes-normativas/financeiro/ato-in-2141-2023.md": "https://www.gov.br/receitafederal/pt-br",
}

def sanear():
    corrigidos = 0

    # 1. Correções pontuais
    for rel_path, nova_url in CORRECOES_PONTUAIS.items():
        p = RAIZ / rel_path
        if not p.exists():
            continue
        content = p.read_text(encoding="utf-8")
        novo = re.sub(r'fonte:\s*["\'][^"\r\n\']+["\']', f'fonte: "{nova_url}"', content)
        if novo != content:
            p.write_text(novo, encoding="utf-8")
            corrigidos += 1
            print(f"[PONTUAL] {rel_path} -> {nova_url}")

    # 2. Correções estaduais nos arquivos que falharam
    import json
    rel_auditoria = RAIZ / "_auditoria" / "auditoria_links_detalhada.json"
    if rel_auditoria.exists():
        data = json.load(open(rel_auditoria, encoding="utf-8"))
        falhas = [d["arquivo"] for d in data.get("documentos", []) if not d.get("acessivel", False)]
        for f in falhas:
            if f.startswith("estaduais/") and "/confaz/" not in f:
                partes = f.split("/")
                uf = partes[1]
                if uf in PORTAIS_UF:
                    _, portal_url = PORTAIS_UF[uf]
                    p = RAIZ / f
                    if p.exists():
                        content = p.read_text(encoding="utf-8")
                        novo = re.sub(r'fonte:\s*["\'][^"\r\n\']+["\']', f'fonte: "{portal_url}"', content)
                        if novo != content:
                            p.write_text(novo, encoding="utf-8")
                            corrigidos += 1
                            print(f"[ESTADUAL] {f} -> {portal_url}")

    print(f"\nTotal de arquivos saneados: {corrigidos}")

if __name__ == "__main__":
    sanear()
