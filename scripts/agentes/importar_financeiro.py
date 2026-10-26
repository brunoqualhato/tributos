"""Script de Ingestão de Legislação de Tributação Financeira, IOF e Criptoativos.

Coleta e formata em CommonMark estrito com metadados YAML canônicos:
1. Decreto nº 6.306/2007 (Regulamento do IOF - RIOF)
2. Lei nº 5.143/1966 (Cria o IOF)
3. Lei nº 8.894/1994 (IOF sobre Títulos, Valores Mobiliários e Câmbio)
4. Instrução Normativa RFB nº 1.888/2019 (Criptoativos)
"""
from pathlib import Path
import re
import sys

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from agente_api import AgenteAPI
from comum import gerar_frontmatter, salvar_atomico
from html2md import converter_html_para_md


def importar_financeiro():
    api = AgenteAPI()
    gerados = []

    # 1. Decreto nº 6.306/2007 (RIOF)
    print("[Financeiro] Ingerindo Decreto nº 6.306/2007 (RIOF)...")
    res1 = api.baixar_norma_lexml("urn:lex:br:federal:decreto:2007-12-14;6306")
    md1 = converter_html_para_md(res1["html"])
    md1 = md1.replace("\ufeff", "").replace("<<ANEXO>>", "[ANEXO]").strip()

    meta1 = {
        "titulo": "Decreto nº 6.306, de 14 de dezembro de 2007 (Regulamento do IOF - RIOF)",
        "esfera": "Federal",
        "orgao": "Presidência da República / Congresso Nacional",
        "tipo": "Decreto",
        "numero": "6306",
        "data": "2007-12-14",
        "ano": "2007",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IOF", "IRRF Financeiro"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:2007-12-14;6306",
        "ementa": "Regulamenta o Imposto sobre Operações de Crédito, Câmbio e Seguro, ou relativas a Títulos ou Valores Mobiliários - IOF (Regulamento do IOF - RIOF)."
    }
    conteudo1 = gerar_frontmatter(meta1) + f"# {meta1['titulo']}\n\n{md1}\n"
    dest1 = RAIZ / "federal" / "regulamentos" / "iof" / "decreto-6306-2007.md"
    salvar_atomico(dest1, conteudo1.encode("utf-8"))
    gerados.append(dest1)
    print(f"Salvo: {dest1.relative_to(RAIZ)}")

    # 2. Lei nº 5.143/1966
    print("[Financeiro] Ingerindo Lei nº 5.143/1966...")
    res2 = api.baixar_norma_lexml("urn:lex:br:federal:lei:1966-10-20;5143")
    md2 = converter_html_para_md(res2["html"])
    md2 = md2.replace("\ufeff", "").strip()

    meta2 = {
        "titulo": "Lei nº 5.143, de 20 de outubro de 1966 (Cria o IOF)",
        "esfera": "Federal",
        "orgao": "Presidência da República / Congresso Nacional",
        "tipo": "Lei Ordinária",
        "numero": "5143",
        "data": "1966-10-20",
        "ano": "1966",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IOF", "IRRF Financeiro"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1966-10-20;5143",
        "ementa": "Institui o Imposto sobre Operações Financeiras, regula a respectiva cobrança, dispõe sobre a aplicação das reservas monetárias oriundas de sua receita, e dá outras providências."
    }
    conteudo2 = gerar_frontmatter(meta2) + f"# {meta2['titulo']}\n\n{md2}\n"
    dest2 = RAIZ / "federal" / "leis-ordinarias" / "iof" / "lei-5143-1966.md"
    salvar_atomico(dest2, conteudo2.encode("utf-8"))
    gerados.append(dest2)
    print(f"Salvo: {dest2.relative_to(RAIZ)}")

    # 3. Lei nº 8.894/1994
    print("[Financeiro] Ingerindo Lei nº 8.894/1994...")
    res3 = api.baixar_norma_lexml("urn:lex:br:federal:lei:1994-06-21;8894")
    md3 = converter_html_para_md(res3["html"])
    md3 = md3.replace("\ufeff", "").strip()

    meta3 = {
        "titulo": "Lei nº 8.894, de 21 de junho de 1994 (IOF sobre Títulos e Câmbio)",
        "esfera": "Federal",
        "orgao": "Presidência da República / Congresso Nacional",
        "tipo": "Lei Ordinária",
        "numero": "8894",
        "data": "1994-06-21",
        "ano": "1994",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IOF", "IRRF Financeiro"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1994-06-21;8894",
        "ementa": "Dispõe sobre o Imposto sobre Operações de Crédito, Câmbio e Seguro, ou relativas a Títulos e Valores Mobiliários, e dá outras providências."
    }
    conteudo3 = gerar_frontmatter(meta3) + f"# {meta3['titulo']}\n\n{md3}\n"
    dest3 = RAIZ / "federal" / "leis-ordinarias" / "iof" / "lei-8894-1994.md"
    salvar_atomico(dest3, conteudo3.encode("utf-8"))
    gerados.append(dest3)
    print(f"Salvo: {dest3.relative_to(RAIZ)}")

    # 4. IN RFB nº 1.888/2019 (Criptoativos)
    print("[Financeiro] Ingerindo IN RFB nº 1.888/2019 (Criptoativos)...")
    corpo4 = api.baixar_corpo_ato_rfb(100592)
    segs4 = sorted(corpo4.get("outrosSegmentos", []), key=lambda x: x.get("ordemSegmentoAto", 0))
    partes4 = [s.get("textoIntegra", "") for s in segs4 if s.get("textoIntegra")]
    texto_html4 = "\n\n".join(partes4)
    md4 = converter_html_para_md(texto_html4)
    md4 = md4.replace("\ufeff", "").strip()
    ementa4 = "Institui e disciplina a obrigatoriedade de prestação de informações relativas às operações realizadas com criptoativos à Secretaria Especial da Receita Federal do Brasil (RFB)."

    meta4 = {
        "titulo": "Instrução Normativa RFB nº 1888, de 3 de maio de 2019",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil",
        "tipo": "Instrução Normativa",
        "numero": "1888",
        "data": "2019-05-07",
        "ano": "2019",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IOF", "IRRF Financeiro", "Criptoativos"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/100592",
        "ementa": ementa4
    }
    corpo_final4 = f"## Ementa\n\n{ementa4}\n\n{md4}"
    conteudo4 = gerar_frontmatter(meta4) + f"# {meta4['titulo']}\n\n{corpo_final4}\n"
    dest4 = RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2019" / "ato-100592-1888-2019.md"
    salvar_atomico(dest4, conteudo4.encode("utf-8"))
    gerados.append(dest4)
    print(f"Salvo: {dest4.relative_to(RAIZ)}")

    return gerados


if __name__ == "__main__":
    importar_financeiro()
