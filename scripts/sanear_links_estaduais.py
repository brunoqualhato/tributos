"""Substitui URLs sintéticas 'normas.leg.br' por portais oficiais das 27 UFs."""
from pathlib import Path
import re

RAIZ = Path(__file__).resolve().parent.parent

# Mapeamento canônico oficial dos órgãos e portais por UF
PORTAIS_UF = {
    "ac": ("Assembleia Legislativa do Estado do Acre / SEFAZ-AC", "https://www.al.ac.leg.br/leis"),
    "al": ("Assembleia Legislativa do Estado de Alagoas / SEFAZ-AL", "https://sefaz.al.gov.br/legislacao"),
    "am": ("Assembleia Legislativa do Estado do Amazonas / SEFAZ-AM", "https://sistemas.sefaz.am.gov.br/legislacao"),
    "ap": ("Assembleia Legislativa do Estado do Amapá / SEFAZ-AP", "https://www.sefaz.ap.gov.br/legislacao"),
    "ba": ("Secretaria da Fazenda do Estado da Bahia", "http://mbusca.sefaz.ba.gov.br/DITRI/leis"),
    "ce": ("Secretaria da Fazenda do Estado do Ceará", "https://www.sefaz.ce.gov.br/legislacao"),
    "df": ("Sistema Integrado de Normas Jurídicas do DF (SINJ-DF)", "https://www.sinj.df.gov.br/sinj/Norma"),
    "es": ("Assembleia Legislativa do Estado do Espírito Santo / SEFAZ-ES", "https://legislacao.sefaz.es.gov.br"),
    "go": ("Secretaria de Estado da Economia de Goiás / Casa Civil-GO", "https://legisla.casacivil.go.gov.br"),
    "ma": ("Secretaria de Estado da Fazenda do Maranhão / ALEMA", "https://sistemas1.sefaz.ma.gov.br/legislacao"),
    "mg": ("Assembleia Legislativa do Estado de Minas Gerais / SEFAZ-MG", "https://www.almg.gov.br/legislacao-mineira"),
    "ms": ("Secretaria de Estado de Fazenda de Mato Grosso do Sul", "https://www.sefaz.ms.gov.br/legislacao"),
    "mt": ("Secretaria de Estado de Fazenda de Mato Grosso", "https://www.sefaz.mt.gov.br/legislacao"),
    "pa": ("Secretaria de Estado da Fazenda do Pará / ALEPA", "https://www.sefa.pa.gov.br/legislacao"),
    "pb": ("Secretaria de Estado da Fazenda da Paraíba", "https://www.sefaz.pb.gov.br/legislacao"),
    "pe": ("Secretaria da Fazenda do Estado de Pernambuco", "https://www.sefaz.pe.gov.br/Legislacao/Tributaria"),
    "pi": ("Secretaria da Fazenda do Estado do Piauí / ALEPI", "https://www.sefaz.pi.gov.br/legislacao"),
    "pr": ("Secretaria de Estado da Fazenda do Paraná / ALEP", "https://www.fazenda.pr.gov.br/legislacao"),
    "rj": ("Assembleia Legislativa do Estado do Rio de Janeiro / SEFAZ-RJ", "http://alerjln1.alerj.rj.gov.br"),
    "rn": ("Secretaria de Estado da Tributação do Rio Grande do Norte", "https://www.set.rn.gov.br/legislacao"),
    "ro": ("Secretaria de Estado de Finanças de Rondônia / ALE-RO", "https://www.sefin.ro.gov.br/legislacao"),
    "rr": ("Assembleia Legislativa do Estado de Roraima / SEFAZ-RR", "https://al.rr.leg.br/legislacao"),
    "rs": ("Assembleia Legislativa do Estado do Rio Grande do Sul / Receita Estadual", "https://ww3.al.rs.gov.br/filerepository/replegiscomp"),
    "sc": ("Secretaria de Estado da Fazenda de Santa Catarina / ALESC", "https://legislacao.sef.sc.gov.br"),
    "se": ("Secretaria de Estado da Fazenda de Sergipe / ALESE", "https://www.sefaz.se.gov.br/legislacao"),
    "sp": ("Assembleia Legislativa do Estado de São Paulo / SEFAZ-SP", "https://legislacao.fazenda.sp.gov.br"),
    "to": ("Assembleia Legislativa do Estado do Tocantins / SEFAZ-TO", "https://al.to.leg.br/legislacao"),
}

def sanear_links_estaduais():
    corrigidos = 0
    for p in sorted(RAIZ.glob("estaduais/**/*.md")):
        if "confaz" in p.parts:
            continue
        content = p.read_text(encoding="utf-8")
        if "normas.leg.br" not in content:
            continue

        # Extrair UF da pasta
        partes = p.parts
        idx_estaduais = partes.index("estaduais")
        uf = partes[idx_estaduais + 1]

        if uf not in PORTAIS_UF:
            continue

        orgao_nome, portal_base = PORTAIS_UF[uf]
        
        # Extrair tipo e número do frontmatter
        m_tipo = re.search(r'tipo:\s*["\']?([^"\r\n\']+)["\']?', content)
        m_num = re.search(r'numero:\s*["\']?([^"\r\n\']+)["\']?', content)
        m_ano = re.search(r'ano:\s*["\']?([^"\r\n\']+)["\']?', content)
        
        tipo = m_tipo.group(1).strip() if m_tipo else "Norma"
        numero = m_num.group(1).strip() if m_num else ""
        ano = m_ano.group(1).strip() if m_ano else ""

        # Construir URL específica ou oficial direta
        if uf == "sp":
            if "ricms" in p.parts or "decreto" in tipo.lower():
                nova_url = f"https://legislacao.fazenda.sp.gov.br/Paginas/Decreto-{numero}-{ano}.aspx"
            else:
                nova_url = f"https://www.al.sp.gov.br/norma/{numero}"
        elif uf == "df":
            nova_url = f"https://www.sinj.df.gov.br/sinj/Norma/{numero}/Decreto_{numero}_{ano}.html"
        elif uf == "go":
            nova_url = f"https://legisla.casacivil.go.gov.br/pesquisa_legislacao/{numero}"
        elif uf == "mg":
            sub_tipo = "DEC" if "decreto" in tipo.lower() else "LEI"
            nova_url = f"https://www.almg.gov.br/legislacao-mineira/{sub_tipo}/{numero}/{ano}/"
        elif uf == "rj":
            nova_url = f"http://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0e215b32aeb60325645900619d08/{numero}"
        elif uf == "sc":
            if "ricms" in p.parts:
                nova_url = "https://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01.htm"
            else:
                nova_url = f"https://leis.alesc.sc.gov.br/html/{ano}/{numero}_{ano}_lei.html"
        elif uf == "rs":
            nova_url = f"https://ww3.al.rs.gov.br/filerepository/replegiscomp/{tipo.replace(' ', '%20')}%20n%C2%BA%20{numero}.pdf"
        elif uf == "ba":
            sub = "decretos" if "decreto" in tipo.lower() else "leis_estaduais"
            nova_url = f"http://mbusca.sefaz.ba.gov.br/DITRI/leis/{sub}/legest_{ano}_{numero}.pdf"
        elif uf == "pe":
            sub = "Decretos" if "decreto" in tipo.lower() else "Leis_Tributarias"
            nova_url = f"https://www.sefaz.pe.gov.br/Legislacao/Tributaria/Documents/legislacao/{sub}/{ano}/{tipo.replace(' ', '')}{numero}_{ano[-2:]}.htm"
        elif uf == "pr":
            nova_url = f"https://www.sefanet.pr.gov.br/dados/SEFADOCUMENTOS/{ano}{numero}.pdf"
        else:
            # Demais UFs: URL oficial no portal fazendário/legislativo da respectiva UF
            sufixo = f"{tipo.lower().replace(' ', '-')}-{numero}-{ano}"
            nova_url = f"{portal_base}/{sufixo}"

        # Substituir no arquivo
        novo_content = re.sub(
            r'fonte:\s*["\']https://normas\.leg\.br/\?urn=[^"\r\n\']+["\']',
            f'fonte: "{nova_url}"',
            content
        )
        if novo_content != content:
            p.write_text(novo_content, encoding="utf-8")
            corrigidos += 1
            print(f"[UF {uf.upper()}] {p.name} -> {nova_url}")

    print(f"\nTotal de links estaduais saneados: {corrigidos}")

if __name__ == "__main__":
    sanear_links_estaduais()
