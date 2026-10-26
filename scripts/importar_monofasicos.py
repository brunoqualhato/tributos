"""Importa leis e atos de PIS/Cofins Monofásicos."""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from agente_api import AgenteAPI
from html2md import converter_html_para_md
from comum import gerar_frontmatter, salvar_atomico
from agente_auditor import AgenteAuditor

def main():
    api = AgenteAPI()
    auditor = AgenteAuditor()

    leis_monofasico = [
        {
            "titulo": "Lei nº 10.147, de 21 de dezembro de 2000 (PIS/Cofins Monofásico - Farmacêuticos e Cosméticos)",
            "urn": "urn:lex:br:federal:lei:2000-12-21;10147",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2000-12-21;10147",
            "numero": "10147", "ano": "2000", "data": "2000-12-21",
            "tributos": ["PIS/Pasep", "Cofins"],
            "ementa": "Dispõe sobre a incidência da contribuição para o PIS/Pasep e da Cofins nas operações de venda dos produtos farmacêuticos, de perfumaria, de toucador ou de higiene pessoal.",
            "slug": "lei-10147-2000"
        },
        {
            "titulo": "Lei nº 10.485, de 3 de julho de 2002 (PIS/Cofins Monofásico - Autopeças e Veículos)",
            "urn": "urn:lex:br:federal:lei:2002-07-03;10485",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2002-07-03;10485",
            "numero": "10485", "ano": "2002", "data": "2002-07-03",
            "tributos": ["PIS/Pasep", "Cofins"],
            "ementa": "Dispõe sobre a incidência das contribuições para o PIS/Pasep e da Cofins devidas pelas pessoas jurídicas que procedam à industrialização ou à importação de autopeças e veículos automotores.",
            "slug": "lei-10485-2002"
        },
        {
            "titulo": "Lei nº 10.560, de 13 de novembro de 2002 (PIS/Cofins Monofásico - Combustíveis)",
            "urn": "urn:lex:br:federal:lei:2002-11-13;10560",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2002-11-13;10560",
            "numero": "10560", "ano": "2002", "data": "2002-11-13",
            "tributos": ["PIS/Pasep", "Cofins"],
            "ementa": "Dispõe sobre a incidência do PIS/Pasep e da Cofins nas operações de venda de querosene de aviação e derivados de petróleo.",
            "slug": "lei-10560-2002"
        },
        {
            "titulo": "Lei nº 13.097, de 19 de janeiro de 2015 (PIS/Cofins - Bebidas Frias)",
            "urn": "urn:lex:br:federal:lei:2015-01-19;13097",
            "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2015-01-19;13097",
            "numero": "13097", "ano": "2015", "data": "2015-01-19",
            "tributos": ["PIS/Pasep", "Cofins", "IPI"],
            "ementa": "Disciplina a tributação concentrada e especial de PIS/Pasep, Cofins e IPI para o setor de bebidas frias (cervejas, refrigerantes, águas e isotônicos).",
            "slug": "lei-13097-2015"
        }
    ]

    for item in leis_monofasico:
        res = api.baixar_norma_lexml(item["urn"])
        html = res.get("html", "")
        md = converter_html_para_md(html)
        
        meta = {
            "titulo": item["titulo"],
            "esfera": "Federal",
            "orgao": "Presidência da República / Congresso Nacional",
            "tipo": "Lei Ordinária",
            "numero": item["numero"],
            "data": item["data"],
            "ano": item["ano"],
            "tema_tributario": "Produtos e Mercadorias",
            "tributos_afetados": item["tributos"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": item["url"],
            "ementa": item["ementa"]
        }
        
        titulo_doc = item["titulo"]
        conteudo = f"{gerar_frontmatter(meta)}# {titulo_doc}\n\n{md}\n"
        
        p1 = RAIZ / "federal" / "leis-ordinarias" / "pis-cofins-monofasico" / f"{item['slug']}.md"
        salvar_atomico(p1, conteudo.encode("utf-8"))
        
        p2 = RAIZ / "reguladores" / "rfb" / "pis-cofins-monofasico" / f"{item['slug']}.md"
        salvar_atomico(p2, conteudo.encode("utf-8"))
        
        val1, err1 = auditor.auditar_documento(p1, checar_rede=True)
        val2, err2 = auditor.auditar_documento(p2, checar_rede=True)
        print(f"Salvo {item['slug']}: p1 valid={val1} err={err1}, p2 valid={val2} err={err2}")

if __name__ == "__main__":
    main()
