"""Importador de Normas Estruturantes de Combustíveis e Energia.

Coleta e formata:
1. Lei nº 10.336/2001 (CIDE-Combustíveis)
2. Decreto nº 5.060/2004 (Alíquotas da CIDE-Combustíveis)
3. Lei Complementar nº 192/2022 (ICMS Monofásico Combustíveis)
4. Convênio ICMS 199/2022 (ICMS Monofásico - Diesel, Biodiesel e GLP)
5. Convênio ICMS 15/2023 (ICMS Monofásico - Gasolina e Etanol Anidro)
6. Lei nº 10.560/2002 (PIS/Cofins Combustíveis e Querosene de Aviação)
"""
from pathlib import Path
import re
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from agente_api import AgenteAPI
from agente_auditor import AgenteAuditor
from comum import Rede, gerar_frontmatter, salvar_atomico
from html2md import converter_html_para_md

TRIBUTOS_COMBUSTIVEIS = [
    "CIDE-Combustíveis",
    "ICMS Monofásico",
    "PIS/Pasep Combustíveis",
    "Cofins Combustíveis",
]
TEMA = "Combustíveis e Energia"


def limpar_markdown_norma(md: str) -> str:
    """Limpa cabeçalhos repetidos e ruídos específicos de LexML/CONFAZ mantendo fidelidade jurídica."""
    # Remove marcação LexML tipo ###LEI-010336...@@@
    md = re.sub(r"###[A-Z0-9\-_]+@@@", "", md)
    # Remove marcas de BOM
    md = md.replace("\ufeff", "")
    # Remove botões residuais do CONFAZ como "Tweet" e "Imprimir"
    md = re.sub(r"\n\s*Tweet\s*\n", "\n\n", md)
    md = re.sub(r"\n\s*Imprimir\s*\n", "\n\n", md)
    # Compacta linhas em branco excessivas
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def importar_normas_federais(api: AgenteAPI, auditor: AgenteAuditor):
    normas = [
        {
            "titulo": "Lei nº 10.336, de 19 de dezembro de 2001 (CIDE-Combustíveis)",
            "urn": "urn:lex:br:federal:lei:2001-12-19;10336",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2001-12-19;10336",
            "tipo": "Lei Ordinária",
            "numero": "10336",
            "ano": "2001",
            "data": "2001-12-19",
            "orgao": "Presidência da República / Congresso Nacional",
            "ementa": "Institui Contribuição de Intervenção no Domínio Econômico incidente sobre a importação e a comercialização de petróleo e seus derivados, gás natural e seus derivados, e álcool etílico combustível (Cide), e dá outras providências.",
            "pasta": "federal/leis-ordinarias/combustiveis",
            "slug": "lei-10336-2001",
        },
        {
            "titulo": "Decreto nº 5.060, de 30 de abril de 2004 (Alíquotas da CIDE-Combustíveis)",
            "urn": "urn:lex:br:federal:decreto:2004-04-30;5060",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:2004-04-30;5060",
            "tipo": "Decreto",
            "numero": "5060",
            "ano": "2004",
            "data": "2004-04-30",
            "orgao": "Presidência da República",
            "ementa": "Reduz as alíquotas da Contribuição de Intervenção no Domínio Econômico incidente sobre a importação e a comercialização de petróleo e seus derivados, gás natural e seus derivados, e álcool etílico combustível (CIDE), instituída pela Lei nº 10.336, de 19 de dezembro de 2001, e dá outras providências.",
            "pasta": "federal/regulamentos/cide",
            "slug": "decreto-5060-2004",
        },
        {
            "titulo": "Lei Complementar nº 192, de 11 de março de 2022 (ICMS Monofásico Combustíveis)",
            "urn": "urn:lex:br:federal:lei.complementar:2022-03-11;192",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2022-03-11;192",
            "tipo": "Lei Complementar",
            "numero": "192",
            "ano": "2022",
            "data": "2022-03-11",
            "orgao": "Presidência da República / Congresso Nacional",
            "ementa": "Define os combustíveis sobre os quais incidirá uma única vez o Imposto sobre Operações Relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação (ICMS), ainda que as operações se iniciem no exterior; e dá outras providências.",
            "pasta": "federal/leis-complementares/combustiveis",
            "slug": "lei-complementar-192-2022",
        },
        {
            "titulo": "Lei nº 10.560, de 13 de novembro de 2002 (PIS/Cofins Monofásico - Combustíveis e Querosene)",
            "urn": "urn:lex:br:federal:lei:2002-11-13;10560",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2002-11-13;10560",
            "tipo": "Lei Ordinária",
            "numero": "10560",
            "ano": "2002",
            "data": "2002-11-13",
            "orgao": "Presidência da República / Congresso Nacional",
            "ementa": "Dispõe sobre o tratamento tributário dispensado às empresas de transporte aéreo e a incidência do PIS/Pasep e da Cofins nas operações de venda de combustíveis e querosene de aviação.",
            "pasta": "federal/leis-ordinarias/combustiveis",
            "slug": "lei-10560-2002",
        },
    ]

    for item in normas:
        print(f"[Federal] Baixando {item['titulo']} via LexML...")
        res = api.baixar_norma_lexml(item["urn"])
        html = res.get("html", "")
        corpo = converter_html_para_md(html)
        corpo = limpar_markdown_norma(corpo)

        meta = {
            "titulo": item["titulo"],
            "esfera": "Federal",
            "orgao": item["orgao"],
            "tipo": item["tipo"],
            "numero": item["numero"],
            "data": item["data"],
            "ano": item["ano"],
            "tema_tributario": TEMA,
            "tributos_afetados": TRIBUTOS_COMBUSTIVEIS,
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": item["url"],
            "ementa": item["ementa"],
        }

        doc = f"{gerar_frontmatter(meta)}# {item['titulo']}\n\n{corpo}\n"
        destino = RAIZ / item["pasta"] / f"{item['slug']}.md"
        salvar_atomico(destino, doc.encode("utf-8"))

        valido, erros = auditor.auditar_documento(destino, checar_rede=True)
        print(f"-> Salvo: {destino.relative_to(RAIZ)} | Válido: {valido} | Erros: {erros}")


def importar_convenios_confaz(rede: Rede, auditor: AgenteAuditor):
    convenios = [
        {
            "titulo": "Convênio ICMS nº 199, de 22 de dezembro de 2022 (ICMS Monofásico - Diesel, Biodiesel e GLP)",
            "url": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2022/CV199_22",
            "tipo": "Convênio ICMS",
            "numero": "199",
            "ano": "2022",
            "data": "2022-12-22",
            "ementa": "Dispõe sobre o regime de tributação monofásica do ICMS a ser aplicado nas operações com combustíveis nos termos da Lei Complementar nº 192, de 11 de março de 2022, e estabelece procedimentos para o controle, apuração, repasse e dedução do imposto.",
            "pasta": "estadual/confaz/convenios-icms",
            "slug": "convenio-icms-199-2022",
        },
        {
            "titulo": "Convênio ICMS nº 15, de 31 de março de 2023 (ICMS Monofásico - Gasolina e Etanol Anidro)",
            "url": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2023/CV015_23",
            "tipo": "Convênio ICMS",
            "numero": "15",
            "ano": "2023",
            "data": "2023-03-31",
            "ementa": "Dispõe sobre o regime de tributação monofásica do ICMS a ser aplicado nas operações com gasolina e etanol anidro combustível, nos termos da Lei Complementar nº 192, de 11 de março de 2022, e estabelece procedimentos para o controle, apuração, repasse e dedução do imposto.",
            "pasta": "estadual/confaz/convenios-icms",
            "slug": "convenio-icms-15-2023",
        },
    ]

    for item in convenios:
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
        corpo = converter_html_para_md(sub_html)
        corpo = limpar_markdown_norma(corpo)

        meta = {
            "titulo": item["titulo"],
            "esfera": "Estadual / CONFAZ",
            "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
            "tipo": item["tipo"],
            "numero": item["numero"],
            "ano": item["ano"],
            "data": item["data"],
            "tema_tributario": TEMA,
            "tributos_afetados": TRIBUTOS_COMBUSTIVEIS,
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": item["url"],
            "ementa": item["ementa"],
        }

        doc = f"{gerar_frontmatter(meta)}# {item['titulo']}\n\n{corpo}\n"
        destino = RAIZ / item["pasta"] / f"{item['slug']}.md"
        salvar_atomico(destino, doc.encode("utf-8"))

        valido, erros = auditor.auditar_documento(destino, checar_rede=True)
        print(f"-> Salvo: {destino.relative_to(RAIZ)} | Válido: {valido} | Erros: {erros}")


def main():
    api = AgenteAPI()
    rede = Rede(rps=2.0)
    auditor = AgenteAuditor()

    print("=== Ingestão de Legislação Estruturante de Combustíveis e Energia ===")
    importar_normas_federais(api, auditor)
    importar_convenios_confaz(rede, auditor)
    print("=== Ingestão Concluída com Sucesso ===")


if __name__ == "__main__":
    main()
