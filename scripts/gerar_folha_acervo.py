"""Ingestão e catalogação com alta fidelidade das normas estruturantes de Folha de Pagamento e Encargos.

Especialista: tributos_folha
Abrange:
- IN RFB nº 2.110/2022 (Consolidação Previdenciária)
- IN RFB nº 2.053/2021 (CPRB)
- IN RFB nº 2.237/2024 (DCTFWeb)
- Lei nº 14.973/2024 (Reoneração Gradual CPRB)
- Lei nº 14.784/2023 (Prorrogação Desoneração CPRB)
- Lei nº 8.213/1991 (Benefícios e Riscos RAT/NTEP)
- Lei nº 10.666/2003 (Criação do FAP art. 10)
- Decreto-Lei nº 2.318/1986 (Teto de 20 SM Sistema S)
- Lei nº 11.457/2007 (Super Receita / Terceiros Sistema S)
"""
from pathlib import Path
import json
import re
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from agentes.agente_api import AgenteAPI
from comum import salvar_atomico, gerar_frontmatter
from html2md import converter_html_para_md

api = AgenteAPI(rps=1.5)

# -------------------------------------------------------------
# 1. ATOS DA RECEITA FEDERAL (SIJUT)
# -------------------------------------------------------------
ATOS_RFB = [
    {
        "idAto": 126687,
        "titulo": "Instrução Normativa RFB nº 2.110, de 17 de outubro de 2022",
        "tipo": "Instrução Normativa",
        "numero": "2110",
        "ano": "2022",
        "data": "2022-10-17",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["INSS Patronal", "INSS Segurados", "RAT/FAP", "Sistema S"],
        "ementa": "Dispõe sobre normas gerais de tributação previdenciária e de arrecadação das contribuições sociais destinadas à Previdência Social e das contribuições devidas a outras entidades ou fundos (terceiros), administradas pela Secretaria Especial da Receita Federal do Brasil (RFB).",
        "caminho": "reguladores/rfb/instrucoes-normativas/folha/ato-126687-2110-2022.md"
    },
    {
        "idAto": 122005,
        "titulo": "Instrução Normativa RFB nº 2.053, de 6 de dezembro de 2021",
        "tipo": "Instrução Normativa",
        "numero": "2053",
        "ano": "2021",
        "data": "2021-12-06",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["CPRB", "INSS Patronal"],
        "ementa": "Dispõe sobre a Contribuição Previdenciária sobre a Receita Bruta (CPRB), destinada ao Regime Geral de Previdência Social (RGPS), de que tratam os arts. 7º a 9º da Lei nº 12.546, de 14 de dezembro de 2011.",
        "caminho": "reguladores/rfb/instrucoes-normativas/folha/ato-122005-2053-2021.md"
    },
    {
        "idAto": 141910,
        "titulo": "Instrução Normativa RFB nº 2.237, de 4 de dezembro de 2024",
        "tipo": "Instrução Normativa",
        "numero": "2237",
        "ano": "2024",
        "data": "2024-12-04",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["INSS Patronal", "INSS Segurados", "RAT/FAP", "Sistema S", "IRRF Folha", "CPRB"],
        "ementa": "Dispõe sobre a Declaração de Débitos e Créditos Tributários Federais Previdenciários e de Outras Entidades e Fundos (DCTFWeb).",
        "caminho": "reguladores/rfb/instrucoes-normativas/folha/ato-141910-2237-2024.md"
    }
]

# -------------------------------------------------------------
# 2. LEIS E DECRETOS FEDERAIS (LEXML)
# -------------------------------------------------------------
ATOS_LEXML = [
    {
        "urn": "urn:lex:br:federal:lei:2024-09-16;14973",
        "titulo": "Lei nº 14.973, de 16 de setembro de 2024",
        "tipo": "Lei Ordinária",
        "numero": "14973",
        "ano": "2024",
        "data": "2024-09-16",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["CPRB", "INSS Patronal"],
        "ementa": "Estabelece regime de transição para a desoneração da folha de pagamentos e a reoneração gradual da Contribuição Previdenciária sobre a Receita Bruta (CPRB) no período de 2025 a 2027, e dá outras providências.",
        "caminho": "federal/leis-ordinarias/cprb/lei-14973-2024.md"
    },
    {
        "urn": "urn:lex:br:federal:lei:2023-12-27;14784",
        "titulo": "Lei nº 14.784, de 27 de dezembro de 2023",
        "tipo": "Lei Ordinária",
        "numero": "14784",
        "ano": "2023",
        "data": "2023-12-27",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["CPRB", "INSS Patronal"],
        "ementa": "Prorroga o prazo da desoneração da folha de pagamentos (CPRB) até 31 de dezembro de 2027 e altera as alíquotas da contribuição previdenciária sobre a receita bruta.",
        "caminho": "federal/leis-ordinarias/cprb/lei-14784-2023.md"
    },
    {
        "urn": "urn:lex:br:federal:lei:1991-07-24;8213",
        "titulo": "Lei nº 8.213, de 24 de julho de 1991",
        "tipo": "Lei Ordinária",
        "numero": "8213",
        "ano": "1991",
        "data": "1991-07-24",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["RAT/FAP", "INSS Patronal"],
        "ementa": "Dispõe sobre os Planos de Benefícios da Previdência Social e estabelece critérios fundamentais para os Riscos Ambientais do Trabalho (RAT) e Nexo Técnico Epidemiológico Previdenciário (NTEP).",
        "caminho": "federal/leis-ordinarias/previdencia-custeio/lei-8213-1991.md"
    },
    {
        "urn": "urn:lex:br:federal:lei:2003-05-08;10666",
        "titulo": "Lei nº 10.666, de 8 de maio de 2003",
        "tipo": "Lei Ordinária",
        "numero": "10666",
        "ano": "2003",
        "data": "2003-05-08",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["RAT/FAP", "INSS Patronal"],
        "ementa": "Dispõe sobre a concessão da aposentadoria especial ao cooperado de cooperativa de produção ou de trabalho e serviço e institui em seu art. 10 o Fator Acidentário de Prevenção (FAP).",
        "caminho": "federal/leis-ordinarias/previdencia-custeio/lei-10666-2003.md"
    },
    {
        "urn": "urn:lex:br:federal:decreto.lei:1986-12-30;2318",
        "titulo": "Decreto-Lei nº 2.318, de 30 de dezembro de 1986",
        "tipo": "Decreto-Lei",
        "numero": "2318",
        "ano": "1986",
        "data": "1986-12-30",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["Sistema S", "INSS Patronal"],
        "ementa": "Dispõe sobre fontes de custeio da Previdência Social e revoga o teto limite de vinte vezes o maior salário mínimo para apuração da base de cálculo das contribuições previdenciárias e ao Sistema S.",
        "caminho": "reguladores/rfb/rat-fap-terceiros/lei-2318-1986.md"
    },
    {
        "urn": "urn:lex:br:federal:lei:2007-03-16;11457",
        "titulo": "Lei nº 11.457, de 16 de março de 2007",
        "tipo": "Lei Ordinária",
        "numero": "11457",
        "ano": "2007",
        "data": "2007-03-16",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["Sistema S", "INSS Patronal", "INSS Segurados"],
        "ementa": "Dispõe sobre a Administração Tributária Federal; cria a Secretaria da Receita Federal do Brasil (Super Receita) e disciplina a arrecadação e fiscalização das contribuições previdenciárias e de terceiros (Sistema S).",
        "caminho": "reguladores/rfb/rat-fap-terceiros/lei-11457-2007.md"
    }
]

def processar_atos_rfb():
    for item in ATOS_RFB:
        print(f"[RFB] Baixando ato {item['idAto']}: {item['titulo']}...")
        dados = api.baixar_corpo_ato_rfb(item["idAto"])
        
        # Segmentos de texto
        segs = sorted(dados.get("outrosSegmentos", []), key=lambda x: x.get("ordemSegmentoAto", 0))
        partes = [s.get("textoIntegra") for s in segs if s.get("textoIntegra")]
        raw_html = "\n\n".join(partes) or (dados.get("texto") or "")
        
        corpo_md = converter_html_para_md(raw_html)
        
        meta = {
            "titulo": item["titulo"],
            "esfera": "Federal",
            "orgao": "Secretaria Especial da Receita Federal do Brasil",
            "tipo": item["tipo"],
            "numero": item["numero"],
            "ano": item["ano"],
            "data": item["data"],
            "tema_tributario": item["tema_tributario"],
            "tributos_afetados": item["tributos_afetados"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": f"https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{item['idAto']}",
            "ementa": item["ementa"]
        }
        
        conteudo = f"{gerar_frontmatter(meta)}# {item['titulo']}\n\n{corpo_md}\n"
        destino = RAIZ / item["caminho"]
        salvar_atomico(destino, conteudo.encode("utf-8"))
        print(f"[RFB] Salvo com sucesso: {destino.relative_to(RAIZ)} ({len(conteudo)} bytes)")

def processar_atos_lexml():
    for item in ATOS_LEXML:
        print(f"[LEXML] Baixando norma {item['urn']}: {item['titulo']}...")
        dados = api.baixar_norma_lexml(item["urn"])
        raw_html = dados.get("html", "")
        
        corpo_md = converter_html_para_md(raw_html)
        
        meta = {
            "titulo": item["titulo"],
            "esfera": "Federal",
            "orgao": "Presidência da República / Congresso Nacional" if "Decreto" not in item["tipo"] else "Presidência da República",
            "tipo": item["tipo"],
            "numero": item["numero"],
            "ano": item["ano"],
            "data": item["data"],
            "tema_tributario": item["tema_tributario"],
            "tributos_afetados": item["tributos_afetados"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": f"https://normas.leg.br/?urn={item['urn']}",
            "ementa": item["ementa"]
        }
        
        conteudo = f"{gerar_frontmatter(meta)}# {item['titulo']}\n\n{corpo_md}\n"
        destino = RAIZ / item["caminho"]
        salvar_atomico(destino, conteudo.encode("utf-8"))
        print(f"[LEXML] Salvo com sucesso: {destino.relative_to(RAIZ)} ({len(conteudo)} bytes)")

if __name__ == "__main__":
    processar_atos_rfb()
    processar_atos_lexml()
    print("Processamento concluído com sucesso!")
