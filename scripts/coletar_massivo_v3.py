"""Ingestão massiva contínua - Lote 3 (Expansão histórica e novos temas).

Foca em:
1. Simples Nacional e MEI (LC 123/2006, CGSN, Soluções de Consulta)
2. Zona Franca de Manaus e Incentivos Regionais (DL 288/1967, Suframa)
3. Compensação, Restituição e PER/DCOMP (Lei 9.430/96, Lei 13.670/18)
4. Atos da RFB e Soluções de Consulta em anos adicionais (2010, 2011, 2012, 2013, 2014, 2018, 2020)
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import json
import sys
import time

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from agentes.agente_api import AgenteAPI
from agentes.agente_estruturador import AgenteEstruturador
from agentes.agente_auditor import AgenteAuditor
from agentes.agente_link_auditor import AgenteLinkAuditor
from catalogo import gerar_catalogo
from progresso import gerar_progresso
from comum import salvar_atomico, gerar_frontmatter
from html2md import converter_html_para_md

LEIS_ESTRUTURANTES_LOTE3 = [
    {
        "titulo": "Decreto-Lei nº 288, de 28 de fevereiro de 1967 (Zona Franca de Manaus)",
        "urn": "urn:lex:br:federal:decreto.lei:1967-02-28;288",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto.lei:1967-02-28;288",
        "numero": "288", "ano": "1967", "tipo": "Decreto-Lei",
        "tema": "Produtos e Mercadorias",
        "tributos": ["IPI", "ICMS", "Imposto de Importação"],
        "ementa": "Altera as disposições da Lei número 3.173 de 6 de junho de 1957 e regula a Zona Franca de Manaus.",
        "pasta": "federal/decretos-leis"
    },
    {
        "titulo": "Lei nº 13.670, de 30 de maio de 2018 (Compensação Tributária e CPRB)",
        "urn": "urn:lex:br:federal:lei:2018-05-30;13670",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2018-05-30;13670",
        "numero": "13670", "ano": "2018", "tipo": "Lei Ordinária",
        "tema": "Folha de Pagamento e Encargos",
        "tributos": ["CPRB", "Compensação Tributária", "PIS/Pasep", "Cofins"],
        "ementa": "Altera a Lei nº 12.546/2011 quanto à desoneração da folha de pagamentos e veda a compensação de débitos de estimativa com créditos de tributos administrados pela RFB.",
        "pasta": "federal/leis-ordinarias"
    },
    {
        "titulo": "Lei Complementar nº 128, de 19 de dezembro de 2008 (Criação do MEI)",
        "urn": "urn:lex:br:federal:lei.complementar:2008-12-19;128",
        "url": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2008-12-19;128",
        "numero": "128", "ano": "2008", "tipo": "Lei Complementar",
        "tema": "Tributário e Contábil Geral",
        "tributos": ["Simples Nacional", "MEI", "INSS", "ICMS", "ISSQN"],
        "ementa": "Altera a Lei Complementar nº 123/2006 para instituir a figura do Microempreendedor Individual (MEI).",
        "pasta": "federal/leis-complementares"
    }
]

def ingerir_leis_lote3():
    print("[Lote 3] Ingerindo Leis Estruturantes...")
    api = AgenteAPI(rps=2.5)
    salvos = []
    for item in LEIS_ESTRUTURANTES_LOTE3:
        dest = RAIZ / item["pasta"] / f"lei-{item['numero']}-{item['ano']}.md"
        if dest.exists():
            continue
        try:
            res = api.baixar_norma_lexml(item["urn"])
            corpo = converter_html_para_md(res.get("html", ""))
            meta = {
                "titulo": item["titulo"],
                "esfera": "Federal",
                "orgao": "Presidência da República / Congresso Nacional",
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
            texto = gerar_frontmatter(meta) + f"# {item['titulo']}\n\n{corpo}\n"
            salvar_atomico(dest, texto.encode("utf-8"))
            salvos.append(dest)
            print(f"[LexML] Ingerido: {dest.relative_to(RAIZ)}")
        except Exception as e:
            print(f"[LexML Erro] {item['titulo']}: {e}")
    return salvos

def ingerir_rfb_lote3():
    print("\n[Lote 3] Ingerindo Atos RFB em Anos Complementares (2010 a 2020)...")
    api = AgenteAPI(rps=3.0)
    estruturador = AgenteEstruturador()
    gerados = []

    anos = [2010, 2011, 2012, 2013, 2014, 2018, 2020]
    termos = ["simples nacional", "compensacao", "zona franca", "restituicao"]

    def buscar_atos(termo, ano):
        locais = []
        try:
            res = api.consultar_atos_rfb(termo=termo, ano=ano, pagina=1, tamanho=3)
            atos = res.get("atos", []) if isinstance(res, dict) else res
            for ato in atos:
                id_ato = ato.get("idAto")
                if id_ato:
                    detalhes = api.baixar_corpo_ato_rfb(id_ato)
                    dados = {**ato, **detalhes}
                    p = estruturador.estruturar_ato_rfb(dados)
                    locais.append(p)
        except Exception as e:
            print(f"[RFB Erro] {termo} ({ano}): {e}")
        return locais

    with ThreadPoolExecutor(max_workers=5) as pool:
        futuros = [pool.submit(buscar_atos, t, a) for a in anos for t in termos]
        for f in as_completed(futuros):
            gerados.extend(f.result())

    return gerados

def main():
    t0 = time.time()
    l1 = ingerir_leis_lote3()
    l2 = ingerir_rfb_lote3()
    total_novos = len(l1) + len(l2)
    print(f"\n[Lote 3 Finalizado] {total_novos} novos atos processados em {time.time()-t0:.1f}s.")

    print("\n[Auditoria] Executando AgenteLinkAuditor...")
    AgenteLinkAuditor(rps=4.0).executar_auditoria_concorrente()

    print("\n[Auditoria] Executando AgenteAuditor Independente...")
    auditor = AgenteAuditor(rps=2.0)
    res = auditor.auditar_repositorio(checar_rede=False)
    print(f"[Auditoria] {res['aprovados']}/{res['total_auditado']} aprovados ({res['taxa_aprovacao']}).")

    print("\n[Catálogo] Atualizando ACERVO.md e PROGRESSO.md...")
    total_cat = gerar_catalogo()
    gerar_progresso()
    print(f"[Catálogo] Total geral no acervo: {total_cat} documentos.")

if __name__ == "__main__":
    main()
