"""Script de Enriquecimento e Auditoria de Normas: Dividendos e Renda do Capital.

Executado pelo Agente Especialista `tributos_dividendos` para preencher lacunas cruciais
do acervo em conformidade com as diretrizes normativas.
"""
from pathlib import Path
import json
import re
import ssl
import sys
import urllib.request

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from comum import Rede, gerar_frontmatter, salvar_atomico
from html2md import converter_html_para_md
from agente_api import AgenteAPI
from agente_estruturador import AgenteEstruturador


def atualizar_rir_2018():
    """Baixa e converte o Regulamento do Imposto de Renda 2018 (RIR/2018 - Decreto 9.580/2018) na íntegra com seu Anexo."""
    print("\n--- [1/5] Atualizando Regulamento do Imposto de Renda (RIR/2018) ---")
    url = "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    )
    print("Baixando texto oficial integral do Planalto...")
    with urllib.request.urlopen(req, context=ctx) as resp:
        bruto = resp.read()

    try:
        html = bruto.decode("windows-1252")
    except Exception:
        html = bruto.decode("utf-8", "ignore")

    print(f"HTML baixado ({len(bruto)} bytes). Convertendo para Markdown...")
    corpo_md = converter_html_para_md(html)
    
    meta = {
        "titulo": "Decreto nº 9.580, de 22 de novembro de 2018 (Regulamento do Imposto de Renda - RIR/2018)",
        "esfera": "Federal",
        "orgao": "Presidência da República / Congresso Nacional",
        "tipo": "Decreto",
        "numero": "9580",
        "data": "2018-11-22",
        "ano": "2018",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["IRPJ", "CSLL", "IRPF", "IRRF"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": url,
        "ementa": "Regulamenta a tributação, a fiscalização, a arrecadação e a administração do Imposto sobre a Renda e Proventos de Qualquer Natureza (RIR/2018)."
    }

    frontmatter = gerar_frontmatter(meta)
    conteudo = f"{frontmatter}# {meta['titulo']}\n\n{corpo_md}\n"
    destino = RAIZ / "federal" / "regulamentos" / "rir" / "lei-9580-2018.md"
    salvar_atomico(destino, conteudo.encode("utf-8"))
    print(f"RIR/2018 salvo com sucesso em: {destino} ({len(conteudo.splitlines())} linhas)")


def adicionar_dl_1598_1977(api: AgenteAPI):
    """Baixa e estrutura o Decreto-Lei nº 1.598/1977 (Norma Matriz do Lucro Real, ágio, subvenções e DDL)."""
    print("\n--- [2/5] Coletando Decreto-Lei nº 1.598/1977 (Lucro Real & DDL) ---")
    urn = "urn:lex:br:federal:decreto.lei:1977-12-26;1598"
    norma = api.baixar_norma_lexml(urn)
    html = norma.get("html", "")
    if not html:
        raise RuntimeError("Não foi possível obter HTML do DL 1.598/1977 no LexML")

    corpo_md = converter_html_para_md(html)
    meta = {
        "titulo": "Decreto-Lei nº 1.598, de 26 de dezembro de 1977 (Norma Matriz do Lucro Real e IRPJ/CSLL)",
        "esfera": "Federal",
        "orgao": "Presidência da República / Congresso Nacional",
        "tipo": "Decreto-Lei",
        "numero": "1598",
        "data": "1977-12-26",
        "ano": "1977",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["IRPJ", "CSLL", "IRPF", "IRRF"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": f"https://normas.leg.br/?urn={urn}",
        "ementa": "Altera a legislação do imposto sobre a renda das pessoas jurídicas, define o conceito e apuração do Lucro Real, disciplina o ágio, subvenções para investimento e a distribuição disfarçada de lucros (DDL)."
    }

    frontmatter = gerar_frontmatter(meta)
    conteudo = f"{frontmatter}# {meta['titulo']}\n\n{corpo_md}\n"
    destino = RAIZ / "federal" / "leis-ordinarias" / "irpj-csll" / "lei-1598-1977.md"
    salvar_atomico(destino, conteudo.encode("utf-8"))
    print(f"DL 1.598/1977 salvo com sucesso em: {destino} ({len(conteudo.splitlines())} linhas)")


def padronizar_leis_federais():
    """Valida e padroniza o frontmatter canônico das leis federais do tema Dividendos e Renda do Capital."""
    print("\n--- [3/5] Padronizando Frontmatters de Leis Federais Chave ---")
    alvos = [
        RAIZ / "federal" / "leis-ordinarias" / "dividendos-jcp" / "lei-9249-1995.md",
        RAIZ / "federal" / "leis-ordinarias" / "offshores" / "lei-14754-2023.md",
        RAIZ / "federal" / "leis-ordinarias" / "irpj-csll" / "lei-14789-2023.md",
        RAIZ / "federal" / "leis-ordinarias" / "irpj-csll" / "lei-12973-2014.md",
        RAIZ / "federal" / "leis-ordinarias" / "irpj-csll" / "lei-8981-1995.md",
        RAIZ / "federal" / "leis-ordinarias" / "irpj-csll" / "lei-9430-1996.md",
        RAIZ / "federal" / "leis-ordinarias" / "irpj-csll" / "lei-7689-1988.md",
    ]

    for p in alvos:
        if not p.exists():
            continue
        conteudo = p.read_text(encoding="utf-8")
        if not conteudo.startswith("---"):
            continue
        partes = conteudo.split("---", 2)
        if len(partes) < 3:
            continue
        cabecalho = partes[1]
        corpo = partes[2]

        cabecalho = re.sub(r'tema_tributario:\s*".*?"', 'tema_tributario: "Dividendos e Renda do Capital"', cabecalho)
        cabecalho = re.sub(r'tributos_afetados:\s*\[.*?\]', 'tributos_afetados: ["IRPJ", "CSLL", "IRPF", "IRRF"]', cabecalho)

        novo_conteudo = f"---{cabecalho}---{corpo}"
        salvar_atomico(p, novo_conteudo.encode("utf-8"))
        print(f"Frontmatter padronizado: {p.relative_to(RAIZ)}")


def coletar_ins_essenciais(api: AgenteAPI, estruturador: AgenteEstruturador):
    """Coleta e estrutura Instruções Normativas prioritárias da RFB para Dividendos, JCP, Offshores e Subvenções."""
    print("\n--- [4/5] Coletando Instruções Normativas Paradigmáticas da RFB ---")
    ins_alvo = [
        (81268, "IN RFB nº 1.700/2017 (Regulamento IRPJ/CSLL, JCP e Lucro Real/Presumido)"),
        (136603, "IN RFB nº 2.180/2024 (Offshores, Trusts e Investimentos no Exterior)"),
        (135536, "IN RFB nº 2.170/2023 (Subvenções para Investimento - Lei 14.789/2023)"),
        (135339, "IN RFB nº 2.166/2023 (Fundos de Investimento e Atualização de Bens no Exterior)"),
    ]

    for id_ato, desc in ins_alvo:
        print(f"Baixando {desc} [ID Sijut: {id_ato}]...")
        dados = api.baixar_corpo_ato_rfb(id_ato)
        caminho = estruturador.estruturar_ato_rfb(dados)
        print(f"Salvo: {caminho.relative_to(RAIZ)}")


def coletar_cosits_essenciais(api: AgenteAPI, estruturador: AgenteEstruturador):
    """Coleta e estrutura Soluções de Consulta COSIT paradigmáticas."""
    print("\n--- [5/5] Coletando Soluções de Consulta COSIT Paradigmáticas ---")
    cosits_alvo = [
        (152773, "SC COSIT nº 134/2026 (JCP base de cálculo & Subvenções Lei 14.789/2023)"),
        (138337, "SC COSIT nº 138/2024 (JCP dedutibilidade & Lucro da Exploração)"),
        (152838, "SC COSIT nº 138/2026 (Offshores & Trusts - Dedução de JCP e Dividendos Lei 14.754/2023)"),
        (149052, "SC COSIT nº 6/2026 (Subvenção governamental de investimento Lei 14.789/2023)"),
        (108040, "SC COSIT nº 13/2020 (Ágio interno por rentabilidade futura e incorporação Lei 12.973/2014)"),
        (134391, "SC COSIT nº 228/2023 (Pró-labore vs Distribuição Desproporcional de Lucros Lei 9.249/1995)"),
        (71323, "SC COSIT nº 3/2016 (Ágio na aquisição de participação societária)"),
        (151272, "SC COSIT nº 81/2026 (Subvenção para investimento e aproveitamento de prejuízo fiscal)"),
    ]

    for id_ato, desc in cosits_alvo:
        print(f"Baixando {desc} [ID Sijut: {id_ato}]...")
        dados = api.baixar_corpo_ato_rfb(id_ato)
        caminho = estruturador.estruturar_ato_rfb(dados)
        print(f"Salvo: {caminho.relative_to(RAIZ)}")


def main():
    api = AgenteAPI()
    estruturador = AgenteEstruturador()

    atualizar_rir_2018()
    adicionar_dl_1598_1977(api)
    padronizar_leis_federais()
    coletar_ins_essenciais(api, estruturador)
    coletar_cosits_essenciais(api, estruturador)
    print("\n[Sucesso] Enriquecimento de Dividendos e Renda do Capital finalizado!")


if __name__ == "__main__":
    main()
