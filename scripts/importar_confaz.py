"""Importador de Atos Estruturantes do CONFAZ (Convênios ICMS e Ajustes SINIEF)."""
from pathlib import Path
import re
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from comum import Rede, gerar_frontmatter, salvar_atomico
from html2md import converter_html_para_md
from agente_auditor import AgenteAuditor

CONFAZ_ATOS = [
    {
        "titulo": "Convênio ICMS nº 142, de 14 de dezembro de 2018 (ICMS Substituição Tributária)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2018/CV142_18",
        "tipo": "Convênio ICMS",
        "numero": "142",
        "ano": "2018",
        "data": "2018-12-14",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "ICMS-ST"],
        "ementa": "Dispõe sobre os regimes de substituição tributária e de antecipação de recolhimento do Imposto sobre Operações relativas à Circulação de Mercadorias e sobre Prestações de Serviço de Transporte Interestadual e de Comunicação (ICMS) com encerramento de tributação, relativos ao imposto devido pelas operações subsequentes.",
        "pasta": "reguladores/confaz/convenios",
        "slug": "convenio-icms-142-2018"
    },
    {
        "titulo": "Convênio ICMS nº 52, de 26 de setembro de 1991 (Máquinas e Equipamentos)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/convenios/1991/cv052_91",
        "tipo": "Convênio ICMS",
        "numero": "52",
        "ano": "1991",
        "data": "1991-09-26",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS"],
        "ementa": "Concede redução da base de cálculo do ICMS nas operações com equipamentos industriais e implementos agrícolas.",
        "pasta": "reguladores/confaz/convenios",
        "slug": "convenio-icms-52-1991"
    },
    {
        "titulo": "Ajuste SINIEF nº 7, de 30 de setembro de 2005 (Nota Fiscal Eletrônica - NF-e)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ_007_05",
        "tipo": "Ajuste SINIEF",
        "numero": "7",
        "ano": "2005",
        "data": "2005-09-30",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "IPI"],
        "ementa": "Institui a Nota Fiscal Eletrônica e o Documento Auxiliar da Nota Fiscal Eletrônica (DANFE).",
        "pasta": "reguladores/confaz/ajustes-sinief",
        "slug": "ajuste-sinief-07-2005"
    },
    {
        "titulo": "Ajuste SINIEF nº 21, de 10 de dezembro de 2010 (Manifesto Eletrônico de Documentos Fiscais - MDF-e)",
        "url": "https://www.confaz.fazenda.gov.br/legislacao/ajustes/2010/aj_021_10",
        "tipo": "Ajuste SINIEF",
        "numero": "21",
        "ano": "2010",
        "data": "2010-12-10",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS"],
        "ementa": "Institui o Manifesto Eletrônico de Documentos Fiscais - MDF-e.",
        "pasta": "reguladores/confaz/ajustes-sinief",
        "slug": "ajuste-sinief-21-2010"
    }
]

def main():
    rede = Rede(rps=2.0)
    auditor = AgenteAuditor()

    for item in CONFAZ_ATOS:
        print(f"[CONFAZ] Baixando {item['titulo']}...")
        st, body, _ = rede.get(item["url"])
        if st != 200 or not body:
            print(f"[ERRO] Falha ao obter {item['url']}: HTTP {st}")
            continue

        html = body.decode("utf-8", errors="replace")
        m = re.search(r"<div id=\"content-core\">(.*?)</div>\s*</article>", html, re.DOTALL)
        if not m:
            m = re.search(r"<div id=\"content\">(.*?)<div id=\"viewlet-below-content\">", html, re.DOTALL)
        sub_html = m.group(1) if m else html
        corpo_md = converter_html_para_md(sub_html)

        meta = {
            "titulo": item["titulo"],
            "esfera": "Estadual / CONFAZ",
            "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
            "tipo": item["tipo"],
            "numero": item["numero"],
            "ano": item["ano"],
            "data": item["data"],
            "tema_tributario": item["tema"],
            "tributos_afetados": item["tributos"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": item["url"],
            "ementa": item["ementa"]
        }

        titulo_md = item["titulo"]
        conteudo = f"{gerar_frontmatter(meta)}# {titulo_md}\n\n{corpo_md}\n"
        caminho = RAIZ / item["pasta"] / f"{item['slug']}.md"
        salvar_atomico(caminho, conteudo.encode("utf-8"))

        valido, erros = auditor.auditar_documento(caminho, checar_rede=True)
        print(f"[CONFAZ] Salvo: {caminho.relative_to(RAIZ)} | Válido: {valido} | Erros: {erros}")

if __name__ == "__main__":
    main()
