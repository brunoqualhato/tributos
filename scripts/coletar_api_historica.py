"""Coletor Especialista em APIs Oficiais (Sijut/Receita Federal e LexML).

Responsável pela ingestão em série histórica ampla (2000-2025):
1. Leis e Decretos Federais Estruturantes via LexML (normas.leg.br)
2. Instruções Normativas Estruturantes da RFB via Sijut
3. Atos Declaratórios Interpretativos (ADI) da RFB (2000-2025)
4. Portarias Conjuntas RFB/PGFN (2000-2025)
"""
from pathlib import Path
import json
import gzip
import time
import sys
import html

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from agentes.agente_api import AgenteAPI
from agentes.agente_estruturador import AgenteEstruturador
from comum import salvar_atomico, gerar_frontmatter
from html2md import converter_html_para_md

# =====================================================================
# 1. LEIS E DECRETOS FEDERAIS ESTRUTURANTES (LexML 2000-2025)
# =====================================================================
LEIS_LEXML_2000_2025 = [
    {
        "titulo": "Lei Complementar nº 104, de 10 de janeiro de 2001 (Norma Geral Antielisão e CTN)",
        "urn": "urn:lex:br:federal:lei.complementar:2001-01-10;104",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2001-01-10;104",
        "numero": "104", "ano": "2001", "tipo": "Lei Complementar",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Sistema Tributário Nacional", "CTN", "Planejamento Tributário"],
        "ementa": "Altera dispositivos da Lei nº 5.172, de 25 de outubro de 1966 - Código Tributário Nacional (introduz a norma antielisão no art. 116 e novas hipóteses de suspensão e extinção).",
        "pasta": "federal/leis-complementares/ctn"
    },
    {
        "titulo": "Lei Complementar nº 105, de 10 de janeiro de 2001 (Sigilo Bancário e Fiscalização Tributária)",
        "urn": "urn:lex:br:federal:lei.complementar:2001-01-10;105",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2001-01-10;105",
        "numero": "105", "ano": "2001", "tipo": "Lei Complementar",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Fiscalização Tributária", "Sigilo Bancário", "e-Financeira"],
        "ementa": "Dispõe sobre o sigilo das operações de instituições financeiras e dá outras providências (permite o acesso da administração tributária a dados bancários).",
        "pasta": "federal/leis-complementares"
    },
    {
        "titulo": "Lei Complementar nº 118, de 9 de fevereiro de 2005 (Prescrição e Repetição de Indébito Tributário)",
        "urn": "urn:lex:br:federal:lei.complementar:2005-02-09;118",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2005-02-09;118",
        "numero": "118", "ano": "2005", "tipo": "Lei Complementar",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Repetição de Indébito", "Crédito Tributário", "Falência"],
        "ementa": "Altera e acrescenta dispositivos à Lei nº 5.172, de 25 de outubro de 1966 - Código Tributário Nacional, e dispõe sobre a prescrição da ação de repetição de indébito tributário.",
        "pasta": "federal/leis-complementares"
    },
    {
        "titulo": "Lei Complementar nº 160, de 7 de agosto de 2017 (Convalidação de Benefícios Fiscais de ICMS)",
        "urn": "urn:lex:br:federal:lei.complementar:2017-08-07;160",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2017-08-07;160",
        "numero": "160", "ano": "2017", "tipo": "Lei Complementar",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "Subvenções para Investimento", "Guerra Fiscal"],
        "ementa": "Dispõe sobre convênio que permite a remissão de créditos tributários e a reinstituição de isenções, incentivos e benefícios fiscais de ICMS (disciplina a convalidação da Guerra Fiscal).",
        "pasta": "federal/leis-complementares"
    },
    {
        "titulo": "Lei Complementar nº 190, de 4 de janeiro de 2022 (DIFAL ICMS Não Contribuinte)",
        "urn": "urn:lex:br:federal:lei.complementar:2022-01-04;190",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2022-01-04;190",
        "numero": "190", "ano": "2022", "tipo": "Lei Complementar",
        "tema": "Produtos e Mercadorias",
        "tributos": ["ICMS", "DIFAL"],
        "ementa": "Altera a Lei Complementar nº 87/1996 (Lei Kandir), para regulamentar a cobrança do Diferencial de Alíquota (DIFAL) do ICMS nas operações e prestações interestaduais a consumidor final.",
        "pasta": "federal/leis-complementares/kandir"
    },
    {
        "titulo": "Lei nº 13.988, de 14 de abril de 2020 (Lei da Transação Tributária Federal)",
        "urn": "urn:lex:br:federal:lei:2020-04-14;13988",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2020-04-14;13988",
        "numero": "13988", "ano": "2020", "tipo": "Lei Ordinária",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Transação Tributária", "PGFN", "Crédito Tributário"],
        "ementa": "Dispõe sobre a transação tributária resolutiva de litígios fiscais no âmbito da Procuradoria-Geral da Fazenda Nacional e da Receita Federal do Brasil.",
        "pasta": "federal/leis-ordinarias"
    },
    {
        "titulo": "Lei nº 14.195, de 26 de agosto de 2021 (Ambiente de Negócios e Prescrição Intercorrente Fiscal)",
        "urn": "urn:lex:br:federal:lei:2021-08-26;14195",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2021-08-26;14195",
        "numero": "14195", "ano": "2021", "tipo": "Lei Ordinária",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Execução Fiscal", "Prescrição Intercorrente"],
        "ementa": "Facilita a abertura de empresas e aprimora as execuções fiscais e a cobrança do crédito público.",
        "pasta": "federal/leis-ordinarias"
    },
    {
        "titulo": "Lei nº 14.375, de 21 de junho de 2022 (Aperfeiçoamento da Transação Tributária)",
        "urn": "urn:lex:br:federal:lei:2022-06-21;14375",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2022-06-21;14375",
        "numero": "14375", "ano": "2022", "tipo": "Lei Ordinária",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Transação Tributária", "Prejuízo Fiscal", "Base Negativa CSLL"],
        "ementa": "Amplia os descontos de transação tributária para até 70% e autoriza a utilização de créditos de prejuízo fiscal e base de cálculo negativa da CSLL.",
        "pasta": "federal/leis-ordinarias"
    },
    {
        "titulo": "Lei nº 14.596, de 14 de junho de 2023 (Preços de Transferência / Transfer Pricing)",
        "urn": "urn:lex:br:federal:lei:2023-06-14;14596",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2023-06-14;14596",
        "numero": "14596", "ano": "2023", "tipo": "Lei Ordinária",
        "tema": "Dividendos e Renda do Capital",
        "tributos": ["IRPJ", "CSLL", "Preços de Transferência", "Arm's Length"],
        "ementa": "Dispõe sobre as regras de preços de transferência para transações com partes relacionadas no exterior alinhadas às diretrizes da OCDE.",
        "pasta": "federal/leis-ordinarias"
    },
    {
        "titulo": "Lei nº 14.689, de 20 de setembro de 2023 (CARF Voto de Qualidade e Transação Específica)",
        "urn": "urn:lex:br:federal:lei:2023-09-20;14689",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2023-09-20;14689",
        "numero": "14689", "ano": "2023", "tipo": "Lei Ordinária",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["CARF", "Multas Tributárias", "Transação"],
        "ementa": "Disciplina a proclamação de resultados de julgamentos no CARF na hipótese de empate (voto de qualidade) e prevê a exclusão de multas e juros.",
        "pasta": "federal/leis-ordinarias"
    },
    {
        "titulo": "Decreto nº 7.574, de 29 de setembro de 2011 (Processo de Consulta Tributária Federal)",
        "urn": "urn:lex:br:federal:decreto:2011-09-29;7574",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:2011-09-29;7574",
        "numero": "7574", "ano": "2011", "tipo": "Decreto",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Processo de Consulta", "COSIT", "Segurança Jurídica"],
        "ementa": "Regulamenta o processo de determinação e exigência de créditos tributários da União e o processo de consulta sobre a interpretação da legislação tributária.",
        "pasta": "federal/regulamentos/consulta"
    }
]

# =====================================================================
# 2. INSTRUÇÕES NORMATIVAS ESTRUTURANTES DA RECEITA FEDERAL (Sijut)
# =====================================================================
INS_ESTRUTURANTES_RFB = [
    {
        "idAto": 126687, "num": "2110", "ano": "2022",
        "titulo": "Instrução Normativa RFB nº 2110, de 17 de outubro de 2022 (Consolidação Previdenciária)",
        "pasta": RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "folha",
        "tema": "Folha de Pagamento e Encargos"
    },
    {
        "idAto": 127905, "num": "2121", "ano": "2022",
        "titulo": "Instrução Normativa RFB nº 2121, de 15 de dezembro de 2022 (Consolidação de PIS/COFINS)",
        "pasta": RAIZ / "reguladores" / "rfb" / "pis-cofins-monofasico",
        "tema": "Produtos e Mercadorias"
    },
    {
        "idAto": 81268, "num": "1700", "ano": "2017",
        "titulo": "Instrução Normativa RFB nº 1700, de 14 de março de 2017 (Consolidação do IRPJ e da CSLL)",
        "pasta": RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2017",
        "tema": "Dividendos e Renda do Capital"
    },
    {
        "idAto": 37200, "num": "1234", "ano": "2012",
        "titulo": "Instrução Normativa RFB nº 1234, de 11 de janeiro de 2012 (Retenção de Tributos Órgãos Públicos)",
        "pasta": RAIZ / "reguladores" / "rfb" / "retencoes-servicos",
        "tema": "Serviços e Retenções"
    },
    {
        "idAto": 131582, "num": "2145", "ano": "2023",
        "titulo": "Instrução Normativa RFB nº 2145, de 26 de junho de 2023 (Retenção Ampla de IRRF por Estados e Municípios)",
        "pasta": RAIZ / "reguladores" / "rfb" / "retencoes-servicos",
        "tema": "Serviços e Retenções"
    },
    {
        "idAto": 122107, "num": "2058", "ano": "2021",
        "titulo": "Instrução Normativa RFB nº 2058, de 9 de dezembro de 2021 (Processo de Consulta Tributária RFB)",
        "pasta": RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2021",
        "tema": "Tributário e Contábil Geral"
    },
    {
        "idAto": 135577, "num": "2169", "ano": "2023",
        "titulo": "Instrução Normativa RFB nº 2169, de 29 de dezembro de 2023 (Preços de Transferência / TP)",
        "pasta": RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2023",
        "tema": "Dividendos e Renda do Capital"
    },
    {
        "idAto": 136603, "num": "2180", "ano": "2024",
        "titulo": "Instrução Normativa RFB nº 2180, de 13 de março de 2024 (Regulamentação de Offshores e Trusts)",
        "pasta": RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2024",
        "tema": "Dividendos e Renda do Capital"
    },
    {
        "idAto": 58336, "num": "1500", "ano": "2014",
        "titulo": "Instrução Normativa RFB nº 1500, de 29 de outubro de 2014 (Tributação do IRPF e Retenção na Fonte)",
        "pasta": RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2014",
        "tema": "Folha de Pagamento e Encargos"
    },
    {
        "idAto": 114965, "num": "2003", "ano": "2021",
        "titulo": "Instrução Normativa RFB nº 2003, de 18 de janeiro de 2021 (Escrituração Contábil Digital - ECD)",
        "pasta": RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2021",
        "tema": "Contabilidade e Geral"
    },
    {
        "idAto": 114966, "num": "2004", "ano": "2021",
        "titulo": "Instrução Normativa RFB nº 2004, de 18 de janeiro de 2021 (Escrituração Contábil Fiscal - ECF)",
        "pasta": RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2021",
        "tema": "Dividendos e Renda do Capital"
    },
    {
        "idAto": 119859, "num": "2043", "ano": "2021",
        "titulo": "Instrução Normativa RFB nº 2043, de 12 de agosto de 2021 (EFD-Reinf)",
        "pasta": RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2021",
        "tema": "Serviços e Retenções"
    },
    {
        "idAto": 115131, "num": "2005", "ano": "2021",
        "titulo": "Instrução Normativa RFB nº 2005, de 29 de janeiro de 2021 (DCTFWeb)",
        "pasta": RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2021",
        "tema": "Folha de Pagamento e Encargos"
    },
    {
        "idAto": 127821, "num": "2119", "ano": "2022",
        "titulo": "Instrução Normativa RFB nº 2119, de 6 de dezembro de 2022 (Cadastro Nacional da Pessoa Jurídica - CNPJ)",
        "pasta": RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2022",
        "tema": "Tributário e Contábil Geral"
    },
    {
        "idAto": 122077, "num": "2055", "ano": "2021",
        "titulo": "Instrução Normativa RFB nº 2055, de 6 de dezembro de 2021 (Compensação e Restituição PER/DCOMP)",
        "pasta": RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2021",
        "tema": "Tributário e Contábil Geral"
    }
]

def coletar_lexml(api: AgenteAPI):
    print("\n" + "=" * 70)
    print("ETAPA 1: COLETANDO LEIS E DECRETOS FEDERAIS VIA LEXML (2000-2025)")
    print("=" * 70)
    gerados = []
    for item in LEIS_LEXML_2000_2025:
        caminho = RAIZ / item["pasta"] / f"lei-{item['numero']}-{item['ano']}.md"
        if caminho.exists():
            print(f"[LexML Cache] Já existe: {caminho.relative_to(RAIZ)}")
            gerados.append(caminho)
            continue

        print(f"[LexML] Consultando {item['titulo']}...")
        try:
            res = api.baixar_norma_lexml(item["urn"])
            html_texto = res.get("html", "")
            corpo_md = converter_html_para_md(html_texto)

            meta = {
                "titulo": item["titulo"],
                "esfera": "Federal",
                "orgao": "Congresso Nacional / Presidência da República",
                "tipo": item["tipo"],
                "numero": item["numero"],
                "ano": item["ano"],
                "data": f"{item['ano']}-01-01",
                "tema_tributario": item["tema"],
                "tributos_afetados": item["tributos"],
                "situacao": "Em vigor",
                "revogada": False,
                "fonte": item["url"],
                "ementa": item["ementa"]
            }

            conteudo = gerar_frontmatter(meta) + f"# {item['titulo']}\n\n{corpo_md}\n"
            salvar_atomico(caminho, conteudo.encode("utf-8"))
            print(f"[LexML] Salvo com sucesso: {caminho.relative_to(RAIZ)}")
            gerados.append(caminho)
        except Exception as e:
            print(f"[LexML ERRO] {item['titulo']}: {e}")

    return gerados

def coletar_ins_estruturantes(api: AgenteAPI, estruturador: AgenteEstruturador):
    print("\n" + "=" * 70)
    print("ETAPA 2: COLETANDO INSTRUÇÕES NORMATIVAS ESTRUTURANTES (RFB/SIJUT)")
    print("=" * 70)
    gerados = []
    for item in INS_ESTRUTURANTES_RFB:
        id_ato = item["idAto"]
        destino_esperado = item["pasta"] / f"ato-{id_ato}-{item['num']}-{item['ano']}.md"
        if destino_esperado.exists():
            print(f"[RFB IN Cache] Já existe: {destino_esperado.relative_to(RAIZ)}")
            gerados.append(destino_esperado)
            continue

        print(f"[RFB IN] Baixando corpo oficial: {item['titulo']} (idAto={id_ato})...")
        try:
            detalhes = api.baixar_corpo_ato_rfb(id_ato)
            dados_item = {
                "idAto": id_ato,
                "numeroAto": item["num"],
                "anoAto": item["ano"],
                "tipoAto": {"nomeTipoAto": "Instrução Normativa", "siglaTipoAto": "IN"},
                "dataPublicacao": f"{item['ano']}-01-01"
            }
            dados = {**dados_item, **detalhes}
            md_path = estruturador.estruturar_ato_rfb(dados, pasta_customizada=item["pasta"])
            gerados.append(md_path)
        except Exception as e:
            print(f"[RFB IN ERRO] {item['titulo']}: {e}")

    return gerados

def coletar_adis_historicas(api: AgenteAPI, estruturador: AgenteEstruturador, max_atos: int = 50):
    print("\n" + "=" * 70)
    print("ETAPA 3: COLETANDO ATOS DECLARATÓRIOS INTERPRETATIVOS (ADI 2000-2025)")
    print("=" * 70)
    gerados = []
    todos_atos = []

    # 1. Busca todas as páginas de ADIs de 2000 a 2025 (total 296)
    print("[ADI] Mapeando metadados de ADIs entre 2000 e 2025 no Sijut...")
    for pagina in range(1, 4):
        try:
            res = api.consultar_atos_rfb(
                tipo_sigla="ADI",
                data_inicio="01/01/2000",
                data_fim="31/12/2025",
                pagina=pagina,
                tamanho=100
            )
            atos = res.get("atos", [])
            todos_atos.extend(atos)
            print(f"[ADI] Página {pagina}: {len(atos)} ADIs mapeadas. Total acumulado: {len(todos_atos)}")
        except Exception as e:
            print(f"[ADI ERRO Busca pág {pagina}]: {e}")

    # Prioriza os ADIs mais impactantes cobrindo a série 2000-2025
    # Seleciona todos os recentes (2020-2025) e uma amostragem qualificada dos anos anteriores
    atos_selecionados = []
    anos_cobertos = set()
    for a in todos_atos:
        ano = int(a.get("anoAto") or 0)
        ementa = a.get("ementa", "").lower()
        if "retifica" in ementa[:30]:
            continue
        # Inclui todos de 2020 a 2025
        if ano >= 2020:
            atos_selecionados.append(a)
            anos_cobertos.add(ano)
        elif ano not in anos_cobertos or len(atos_selecionados) < max_atos:
            atos_selecionados.append(a)
            anos_cobertos.add(ano)

    print(f"[ADI] Selecionados {len(atos_selecionados)} ADIs prioritários abrangendo os anos {sorted(list(anos_cobertos))[:10]}...")

    for a in atos_selecionados:
        id_ato = a.get("idAto")
        numero = a.get("numeroAto")
        ano = a.get("anoAto")
        arquivo_esperado = RAIZ / "reguladores" / "rfb" / "outros-atos" / str(ano) / f"ato-{id_ato}-{numero}-{ano}.md"
        if arquivo_esperado.exists():
            gerados.append(arquivo_esperado)
            continue

        try:
            detalhes = api.baixar_corpo_ato_rfb(id_ato)
            dados = {**a, **detalhes}
            md_path = estruturador.estruturar_ato_rfb(dados)
            gerados.append(md_path)
        except Exception as e:
            print(f"[ADI ERRO idAto={id_ato}]: {e}")

    return gerados

def coletar_portarias_conjuntas(api: AgenteAPI, estruturador: AgenteEstruturador, max_atos: int = 40):
    print("\n" + "=" * 70)
    print("ETAPA 4: COLETANDO PORTARIAS CONJUNTAS RFB/PGFN (2000-2025)")
    print("=" * 70)
    gerados = []
    todos_atos = []

    print("[Portaria Conjunta] Mapeando metadados de Portarias Conjuntas no Sijut...")
    for pagina in range(1, 5):
        try:
            res = api.consultar_atos_rfb(
                tipo_sigla="PORTARIA_CONJUNTA",
                data_inicio="01/01/2000",
                data_fim="31/12/2025",
                pagina=pagina,
                tamanho=100
            )
            atos = res.get("atos", [])
            todos_atos.extend(atos)
            print(f"[Portaria Conjunta] Página {pagina}: {len(atos)} atos mapeados. Total acumulado: {len(todos_atos)}")
        except Exception as e:
            print(f"[Portaria Conjunta ERRO Busca pág {pagina}]: {e}")

    # Prioriza portarias conjuntas tributárias (transação, litígio zero, parcelamento, certidão negativa, eSocial)
    palavras_chave = ["transa", "litigio", "parcel", "certid", "esocial", "judicial", "regularidade", "debito"]
    atos_prioritarios = []
    for a in todos_atos:
        em = (a.get("ementa") or "").lower()
        if any(k in em for k in palavras_chave) or int(a.get("anoAto") or 0) >= 2023:
            if not em.startswith("retifica"):
                atos_prioritarios.append(a)

    print(f"[Portaria Conjunta] {len(atos_prioritarios)} portarias prioritárias identificadas.")

    for a in atos_prioritarios[:max_atos]:
        id_ato = a.get("idAto")
        numero = a.get("numeroAto")
        ano = a.get("anoAto")
        arquivo_esperado = RAIZ / "reguladores" / "rfb" / "outros-atos" / str(ano) / f"ato-{id_ato}-{numero}-{ano}.md"
        if arquivo_esperado.exists():
            gerados.append(arquivo_esperado)
            continue

        try:
            detalhes = api.baixar_corpo_ato_rfb(id_ato)
            dados = {**a, **detalhes}
            md_path = estruturador.estruturar_ato_rfb(dados)
            gerados.append(md_path)
        except Exception as e:
            print(f"[Portaria Conjunta ERRO idAto={id_ato}]: {e}")

    return gerados

def main():
    api = AgenteAPI(rps=3.0)
    estruturador = AgenteEstruturador()

    t0 = time.time()
    docs_lexml = coletar_lexml(api)
    docs_ins = coletar_ins_estruturantes(api, estruturador)
    docs_adis = coletar_adis_historicas(api, estruturador, max_atos=50)
    docs_port_conj = coletar_portarias_conjuntas(api, estruturador, max_atos=35)

    total_coletados = len(docs_lexml) + len(docs_ins) + len(docs_adis) + len(docs_port_conj)
    print("\n" + "=" * 70)
    print(f"COLETA CONCLUÍDA EM {time.time() - t0:.1f}s!")
    print(f"- Leis/Decretos LexML: {len(docs_lexml)}")
    print(f"- INs Estruturantes RFB: {len(docs_ins)}")
    print(f"- ADIs (Atos Declaratórios Interpretativos): {len(docs_adis)}")
    print(f"- Portarias Conjuntas RFB/PGFN: {len(docs_port_conj)}")
    print(f"Total de Documentos no Lote: {total_coletados}")
    print("=" * 70)

if __name__ == "__main__":
    main()
