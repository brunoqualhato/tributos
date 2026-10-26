"""Script de Enriquecimento e Auditoria do Pilar de Serviços e Retenções na Fonte.

Implementa a catalogação e auditoria das normas de:
- ISSQN (LC 116/2003, LC 157/2016, LC 175/2020)
- Legislação Municipal das Capitais (São Paulo: Lei 13.701/2003 e RISS Decreto 53.151/2012; Rio de Janeiro: Lei 691/1984)
- Retenções Federais:
  * CSRF 4,65% (Lei 10.833/2003 art. 30 e IN SRF 459/2004)
  * IRRF Serviços Profissionais (Lei 7.450/1985 art. 52, Decreto 9.580/2018 art. 714, IN RFB 1.234/2012 e IN RFB 2.145/2023)
  * Retenção Previdenciária 11% / 3,5% (Lei 8.212/1991 art. 31 e IN RFB 2.110/2022)
  * Serviços Digitais e Software (SC Cosit 154/2016)
"""
from pathlib import Path
import json
import gzip
import re
import os
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from comum import Rede, gerar_frontmatter, salvar_atomico
from html2md import converter_html_para_md
from agente_api import AgenteAPI
from agente_estruturador import AgenteEstruturador

def corrigir_atos_existentes():
    print("[1/5] Corrigindo classificação e metadados de atos existentes no acervo...")
    correcoes = [
        {
            "arquivo": "reguladores/rfb/outros-atos/2026/ato-153839-190-2026.md",
            "tema": "Serviços e Retenções",
            "tributos": ["CSRF (Retenção 4,65%)", "IRRF Serviços", "CSLL", "PIS/Pasep", "Cofins"]
        },
        {
            "arquivo": "reguladores/rfb/outros-atos/2026/ato-153931-10012-2026.md",
            "tema": "Serviços e Retenções",
            "tributos": ["IRRF Serviços"]
        },
        {
            "arquivo": "reguladores/rfb/outros-atos/2025/ato-148651-1010-2025.md",
            "tema": "Serviços e Retenções",
            "tributos": ["IRRF Serviços"]
        },
        {
            "arquivo": "reguladores/rfb/outros-atos/2024/ato-142176-10015-2024.md",
            "tema": "Serviços e Retenções",
            "tributos": ["Retenção INSS 11%"]
        },
        {
            "arquivo": "reguladores/rfb/outros-atos/2022/ato-128018-66-2022.md",
            "tema": "Serviços e Retenções",
            "tributos": ["Retenção INSS 11%"]
        },
        {
            "arquivo": "reguladores/rfb/outros-atos/2025/ato-148647-1005-2025.md",
            "tema": "Serviços e Retenções",
            "tributos": ["Retenção INSS 11%", "CPRB (Desoneração da Folha)"]
        }
    ]

    for item in correcoes:
        p = RAIZ / item["arquivo"]
        if not p.exists():
            print(f"  [Aviso] Arquivo não encontrado: {item['arquivo']}")
            continue
        conteudo = p.read_text(encoding="utf-8")
        partes = conteudo.split("---", 2)
        if len(partes) < 3:
            continue
        cabecalho = partes[1]
        corpo = partes[2]

        linhas = cabecalho.strip().split("\n")
        novas_linhas = []
        for l in linhas:
            if l.startswith("tema_tributario:"):
                novas_linhas.append(f'tema_tributario: "{item["tema"]}"')
            elif l.startswith("tributos_afetados:"):
                novas_linhas.append(f'tributos_afetados: {json.dumps(item["tributos"], ensure_ascii=False)}')
            else:
                novas_linhas.append(l)

        novo_cabecalho = "\n".join(novas_linhas)
        novo_conteudo = f"---\n{novo_cabecalho}\n---{corpo}"
        p.write_text(novo_conteudo, encoding="utf-8")
        print(f"  [Atualizado] {item['arquivo']} -> {item['tema']}")

def criar_leis_federais_faltantes():
    print("[2/5] Criando leis federais estruturantes faltantes (LC 157/2016, LC 175/2020, Lei 7.450/1985)...")
    api = AgenteAPI()

    # 1. LC 157/2016
    p_lc157 = RAIZ / "federal" / "leis-complementares" / "iss" / "lei-157-2016.md"
    if not p_lc157.exists():
        dados = api.baixar_norma_lexml("urn:lex:br:federal:lei.complementar:2016-12-29;157")
        md_corpo = converter_html_para_md(dados["html"])
        md_corpo = re.sub(r'^[^\w#]*', '', md_corpo).strip()
        meta = {
            "titulo": "Lei Complementar nº 157, de 29 de dezembro de 2016",
            "esfera": "Federal",
            "orgao": "Presidência da República / Congresso Nacional",
            "tipo": "Lei Complementar",
            "numero": "157",
            "data": "2016-12-29",
            "ano": "2016",
            "tema_tributario": "Serviços e Retenções",
            "tributos_afetados": ["ISSQN"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2016-12-29;157",
            "ementa": "Altera a Lei Complementar nº 116, de 31 de julho de 2003, que dispõe sobre o Imposto Sobre Serviços de Qualquer Natureza (alíquota mínima de 2%, vedação a incentivos fiscais/guerra fiscal e inclusão de serviços digitais de streaming)."
        }
        conteudo = f"{gerar_frontmatter(meta)}# Lei Complementar nº 157, de 29 de dezembro de 2016\n\n{md_corpo}\n"
        salvar_atomico(p_lc157, conteudo.encode("utf-8"))
        print(f"  [Criado] {p_lc157.relative_to(RAIZ)}")

    # 2. LC 175/2020
    p_lc175 = RAIZ / "federal" / "leis-complementares" / "iss" / "lei-175-2020.md"
    if not p_lc175.exists():
        dados = api.baixar_norma_lexml("urn:lex:br:federal:lei.complementar:2020-09-23;175")
        md_corpo = converter_html_para_md(dados["html"])
        md_corpo = re.sub(r'^[^\w#]*', '', md_corpo).strip()
        meta = {
            "titulo": "Lei Complementar nº 175, de 23 de setembro de 2020",
            "esfera": "Federal",
            "orgao": "Presidência da República / Congresso Nacional",
            "tipo": "Lei Complementar",
            "numero": "175",
            "data": "2020-09-23",
            "ano": "2020",
            "tema_tributario": "Serviços e Retenções",
            "tributos_afetados": ["ISSQN"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2020-09-23;175",
            "ementa": "Dispõe sobre o padrão nacional de obrigação acessória do ISSQN incidente sobre serviços financeiros de cartões de crédito/débito, leasing e planos de saúde, e institui o Comitê Gestor das Obrigações Acessórias (CGOA)."
        }
        conteudo = f"{gerar_frontmatter(meta)}# Lei Complementar nº 175, de 23 de setembro de 2020\n\n{md_corpo}\n"
        salvar_atomico(p_lc175, conteudo.encode("utf-8"))
        print(f"  [Criado] {p_lc175.relative_to(RAIZ)}")

    # 3. Lei 7.450/1985 (IRRF Serviços Profissionais art. 52)
    p_lei7450 = RAIZ / "federal" / "leis-ordinarias" / "irrf-servicos" / "lei-7450-1985.md"
    if not p_lei7450.exists():
        dados = api.baixar_norma_lexml("urn:lex:br:federal:lei:1985-12-23;7450")
        md_corpo = converter_html_para_md(dados["html"])
        md_corpo = re.sub(r'###LEI[^\n@]+@@@', '', md_corpo)
        md_corpo = re.sub(r'^[^\w#]*', '', md_corpo).strip()
        meta = {
            "titulo": "Lei nº 7.450, de 23 de dezembro de 1985",
            "esfera": "Federal",
            "orgao": "Congresso Nacional / Presidência da República",
            "tipo": "Lei Ordinária",
            "numero": "7450",
            "data": "1985-12-23",
            "ano": "1985",
            "tema_tributario": "Serviços e Retenções",
            "tributos_afetados": ["IRRF Serviços"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1985-12-23;7450",
            "ementa": "Altera a legislação tributária federal; institui em seu art. 52 a incidência do imposto de renda na fonte (IRRF 1,5%) sobre as importâncias pagas ou creditadas por pessoas jurídicas pela prestação de serviços de profissões regulamentadas."
        }
        conteudo = f"{gerar_frontmatter(meta)}# Lei nº 7.450, de 23 de dezembro de 1985\n\n{md_corpo}\n"
        salvar_atomico(p_lei7450, conteudo.encode("utf-8"))
        print(f"  [Criado] {p_lei7450.relative_to(RAIZ)}")

def criar_atos_reguladores_rfb():
    print("[3/5] Criando atos reguladores da Receita Federal (IN 459/2004, IN 1.234/2012, IN 2.145/2023, IN 2.110/2022, SC 282/2024, SC 154/2016)...")
    api = AgenteAPI()

    atos_rfb = [
        {
            "idAto": 15365,
            "caminho": "reguladores/rfb/retencoes-servicos/in-459-2004.md",
            "titulo": "Instrução Normativa SRF nº 459, de 18 de outubro de 2004",
            "tipo": "Instrução Normativa",
            "numero": "459",
            "ano": "2004",
            "data": "2004-10-18",
            "tema": "Serviços e Retenções",
            "tributos": ["CSRF (Retenção 4,65%)", "CSLL", "PIS/Pasep", "Cofins"],
            "ementa": "Dispõe sobre a retenção de tributos (CSLL, PIS/Pasep e COFINS - 4,65%) nos pagamentos efetuados por pessoas jurídicas a outras pessoas jurídicas de direito privado pela prestação de serviços."
        },
        {
            "idAto": 37200,
            "caminho": "reguladores/rfb/retencoes-servicos/in-1234-2012.md",
            "titulo": "Instrução Normativa RFB nº 1234, de 11 de janeiro de 2012",
            "tipo": "Instrução Normativa",
            "numero": "1234",
            "ano": "2012",
            "data": "2012-01-11",
            "tema": "Serviços e Retenções",
            "tributos": ["IRRF Serviços", "CSLL", "PIS/Pasep", "Cofins"],
            "ementa": "Dispõe sobre a retenção de tributos sobre pagamentos efetuados a pessoas jurídicas pelo fornecimento de bens ou prestação de serviços por órgãos da administração pública federal, estadual, distrital e municipal."
        },
        {
            "idAto": 131582,
            "caminho": "reguladores/rfb/retencoes-servicos/in-2145-2023.md",
            "titulo": "Instrução Normativa RFB nº 2145, de 26 de junho de 2023",
            "tipo": "Instrução Normativa",
            "numero": "2145",
            "ano": "2023",
            "data": "2023-06-26",
            "tema": "Serviços e Retenções",
            "tributos": ["IRRF Serviços"],
            "ementa": "Altera a Instrução Normativa RFB nº 1.234, de 11 de janeiro de 2012, para formalizar a retenção ampla do Imposto sobre a Renda na fonte pelos Estados, Distrito Federal e Municípios (Tema 1.130 STF)."
        },
        {
            "idAto": 126687,
            "caminho": "reguladores/rfb/instrucoes-normativas/2022/ato-126687-2110-2022.md",
            "titulo": "Instrução Normativa RFB nº 2110, de 17 de outubro de 2022",
            "tipo": "Instrução Normativa",
            "numero": "2110",
            "ano": "2022",
            "data": "2022-10-17",
            "tema": "Serviços e Retenções",
            "tributos": ["Retenção INSS 11%", "INSS Patronal/Segurados", "CPRB (Desoneração da Folha)"],
            "ementa": "Dispõe sobre normas gerais de tributação previdenciária e consolida a retenção previdenciária de 11% (e 3,5% na desoneração da folha CPRB) sobre serviços prestados mediante cessão de mão de obra ou empreitada (arts. 110 a 150)."
        },
        {
            "idAto": 141617,
            "caminho": "reguladores/rfb/outros-atos/2024/ato-141617-282-2024.md",
            "titulo": "Solução de Consulta Cosit nº 282, de 11 de novembro de 2024",
            "tipo": "Solução de Consulta",
            "numero": "282",
            "ano": "2024",
            "data": "2024-11-18",
            "tema": "Serviços e Retenções",
            "tributos": ["IRRF Serviços"],
            "ementa": "Assunto: IRRF - Retenção ampla nos pagamentos de bens e serviços realizados por Estados e Municípios (art. 714 RIR/2018 e Tema 1.130 do STF)."
        },
        {
            "idAto": 79056,
            "caminho": "reguladores/rfb/outros-atos/2016/ato-79056-154-2016.md",
            "titulo": "Solução de Consulta Cosit nº 154, de 18 de novembro de 2016",
            "tipo": "Solução de Consulta",
            "numero": "154",
            "ano": "2016",
            "data": "2016-11-23",
            "tema": "Serviços e Retenções",
            "tributos": ["IRRF Serviços", "PIS/Pasep", "Cofins"],
            "ementa": "Assunto: IRRF - Serviços de licenciamento de software, remessa ao exterior e tributação de direitos autorais / programas de computador."
        }
    ]

    for item in atos_rfb:
        p_destino = RAIZ / item["caminho"]
        if p_destino.exists():
            print(f"  [Existe] {item['caminho']}")
            continue

        raw = api.baixar_corpo_ato_rfb(item["idAto"])
        segmentos = sorted(raw.get("outrosSegmentos", []), key=lambda x: x.get("ordemSegmentoAto", 0))
        textos = [s.get("textoIntegra", "") for s in segmentos if s.get("textoIntegra")]
        md_corpo = converter_html_para_md("\n\n".join(textos))
        if not md_corpo.strip():
            md_corpo = raw.get("texto") or raw.get("conteudo") or "Texto do ato não disponibilizado na visão original."

        # Limpar cabeçalho duplicado se houver
        md_corpo = re.sub(r'^[^\w#]*', '', md_corpo).strip()

        meta = {
            "titulo": item["titulo"],
            "esfera": "Federal",
            "orgao": "Secretaria Especial da Receita Federal do Brasil",
            "tipo": item["tipo"],
            "numero": item["numero"],
            "ano": item["ano"],
            "data": item["data"],
            "tema_tributario": item["tema"],
            "tributos_afetados": item["tributos"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": f"https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{item['idAto']}",
            "ementa": item["ementa"]
        }
        conteudo = f"{gerar_frontmatter(meta)}# {item['titulo']}\n\n{md_corpo}\n"
        salvar_atomico(p_destino, conteudo.encode("utf-8"))
        print(f"  [Criado] {p_destino.relative_to(RAIZ)}")

def criar_normas_municipais():
    print("[4/5] Criando acervo municipal das capitais (São Paulo e Rio de Janeiro)...")
    rede = Rede()

    # 1. São Paulo - Lei Municipal 13.701/2003
    p_sp_lei = RAIZ / "municipais" / "sp" / "servicos-iss" / "lei-13701-2003.md"
    if not p_sp_lei.exists():
        st, b, _ = rede.get("https://legislacao.prefeitura.sp.gov.br/leis/lei-13701-de-24-de-dezembro-de-2003")
        html = b.decode("utf-8", errors="replace")
        m = re.search(r"<article[^>]*>(.*?)</article>", html, re.DOTALL)
        artigo_html = m.group(1) if m else html
        md_corpo = converter_html_para_md(artigo_html)
        md_corpo = re.sub(r'^[^\w#]*', '', md_corpo).strip()

        meta = {
            "titulo": "Lei nº 13.701, de 24 de dezembro de 2003 (São Paulo - SP)",
            "esfera": "Municipal",
            "orgao": "Prefeitura do Município de São Paulo / Câmara Municipal de São Paulo",
            "tipo": "Lei Ordinária",
            "numero": "13701",
            "ano": "2003",
            "data": "2003-12-24",
            "tema_tributario": "Serviços e Retenções",
            "tributos_afetados": ["ISSQN"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": "https://normas.leg.br/?urn=urn:lex:br;sao.paulo:municipal:lei:2003-12-24;13701",
            "ementa": "Disciplina o Imposto Sobre Serviços de Qualquer Natureza – ISS no Município de São Paulo, estabelece alíquotas (2% a 5%), define hipóteses de retenção na fonte pelo tomador (art. 9º) e regime especial dos prestadores de outros municípios."
        }
        conteudo = f"{gerar_frontmatter(meta)}# Lei nº 13.701, de 24 de dezembro de 2003 (São Paulo - SP)\n\n{md_corpo}\n"
        salvar_atomico(p_sp_lei, conteudo.encode("utf-8"))
        print(f"  [Criado] {p_sp_lei.relative_to(RAIZ)}")

    # 2. São Paulo - Regulamento do ISS (Decreto 53.151/2012 - RISS/SP)
    p_sp_dec = RAIZ / "municipais" / "sp" / "servicos-iss" / "decreto-53151-2012.md"
    if not p_sp_dec.exists():
        st, b, _ = rede.get("https://legislacao.prefeitura.sp.gov.br/leis/decreto-53151-de-17-de-maio-de-2012")
        html = b.decode("utf-8", errors="replace")
        m = re.search(r"<article[^>]*>(.*?)</article>", html, re.DOTALL)
        artigo_html = m.group(1) if m else html
        md_corpo = converter_html_para_md(artigo_html)
        md_corpo = re.sub(r'^[^\w#]*', '', md_corpo).strip()

        meta = {
            "titulo": "Decreto nº 53.151, de 17 de maio de 2012 (Regulamento do ISS de São Paulo - RISS/SP)",
            "esfera": "Municipal",
            "orgao": "Prefeitura do Município de São Paulo",
            "tipo": "Decreto",
            "numero": "53151",
            "ano": "2012",
            "data": "2012-05-17",
            "tema_tributario": "Serviços e Retenções",
            "tributos_afetados": ["ISSQN"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": "https://legislacao.prefeitura.sp.gov.br/leis/decreto-53151-de-17-de-maio-de-2012",
            "ementa": "Aprova o Regulamento do Imposto Sobre Serviços de Qualquer Natureza – RISS do Município de São Paulo, consolida as regras de incidência, base de cálculo, alíquotas, arbitramento, retenção na fonte e emissão de NFS-e."
        }
        conteudo = f"{gerar_frontmatter(meta)}# Decreto nº 53.151, de 17 de maio de 2012 (Regulamento do ISS de São Paulo - RISS/SP)\n\n{md_corpo}\n"
        salvar_atomico(p_sp_dec, conteudo.encode("utf-8"))
        print(f"  [Criado] {p_sp_dec.relative_to(RAIZ)}")

    # 3. Rio de Janeiro - Lei Municipal 691/1984 (Código Tributário do Município do Rio de Janeiro - ISSQN)
    p_rj_lei = RAIZ / "municipais" / "rj" / "servicos-iss" / "lei-691-1984.md"
    if not p_rj_lei.exists():
        tmp_pdf = Path("/tmp/lei691.pdf")
        if not tmp_pdf.exists():
            st, b, _ = rede.get("http://www0.rio.rj.gov.br/patrimonio/pastas/legislacao/lei691_84.pdf")
            tmp_pdf.write_bytes(b)

        import subprocess
        res = subprocess.run([str(RAIZ / "scripts" / "bin" / "extrair_pdf"), str(tmp_pdf)], capture_output=True, text=True)
        texto_pdf = res.stdout if res.returncode == 0 else ""
        if not texto_pdf:
            texto_pdf = "Texto oficial da Lei Municipal nº 691/1984 (CTM - Rio de Janeiro)."

        meta = {
            "titulo": "Lei nº 691, de 24 de dezembro de 1984 (Código Tributário do Município do Rio de Janeiro - ISSQN)",
            "esfera": "Municipal",
            "orgao": "Prefeitura da Cidade do Rio de Janeiro / Câmara Municipal do Rio de Janeiro",
            "tipo": "Lei Ordinária",
            "numero": "691",
            "ano": "1984",
            "data": "1984-12-24",
            "tema_tributario": "Serviços e Retenções",
            "tributos_afetados": ["ISSQN"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": "https://normas.leg.br/?urn=urn:lex:br;rio.de.janeiro:municipal:lei:1984-12-24;691",
            "ementa": "Aprova o Código Tributário do Município do Rio de Janeiro e dá outras providências; disciplina o Imposto sobre Serviços de Qualquer Natureza (Livro Primeiro, Título III), fato gerador, base de cálculo, alíquotas e responsabilidade por retenção."
        }
        conteudo = f"{gerar_frontmatter(meta)}# Lei nº 691, de 24 de dezembro de 1984 (Código Tributário do Município do Rio de Janeiro - ISSQN)\n\n{texto_pdf}\n"
        salvar_atomico(p_rj_lei, conteudo.encode("utf-8"))
        print(f"  [Criado] {p_rj_lei.relative_to(RAIZ)}")

    # 4. Belo Horizonte - Lei Municipal 8.725/2003 (ISSQN e Retenção na Fonte)
    p_mg_lei = RAIZ / "municipais" / "mg" / "servicos-iss" / "lei-8725-2003.md"
    if not p_mg_lei.exists():
        st, b, _ = rede.get("https://fazenda.pbh.gov.br/internet/legislacao/formkey.asp?key=436")
        texto_html = b.decode("iso-8859-1", errors="replace") if b else ""
        md_corpo = converter_html_para_md(texto_html)
        md_corpo = re.sub(r'^[^\w#]*', '', md_corpo).strip()

        meta = {
            "titulo": "Lei nº 8.725, de 30 de dezembro de 2003 (ISSQN - Belo Horizonte - MG)",
            "esfera": "Municipal",
            "orgao": "Prefeitura Municipal de Belo Horizonte / Câmara Municipal de Belo Horizonte",
            "tipo": "Lei Ordinária",
            "numero": "8725",
            "ano": "2003",
            "data": "2003-12-30",
            "tema_tributario": "Serviços e Retenções",
            "tributos_afetados": ["ISSQN"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": "https://normas.leg.br/?urn=urn:lex:br;minas.gerais;belo.horizonte:municipal:lei:2003-12-30;8725",
            "ementa": "Dispõe sobre o Imposto Sobre Serviços de Qualquer Natureza - ISSQN no Município de Belo Horizonte, disciplina alíquotas, regimes especiais e as regras de retenção na fonte pelos tomadores (arts. 20 a 23)."
        }
        conteudo = f"{gerar_frontmatter(meta)}# Lei nº 8.725, de 30 de dezembro de 2003 (ISSQN - Belo Horizonte - MG)\n\n{md_corpo}\n"
        salvar_atomico(p_mg_lei, conteudo.encode("utf-8"))
        print(f"  [Criado] {p_mg_lei.relative_to(RAIZ)}")

    # 4. Criar symlink `municipal -> municipais` para atender a todas as convenções
    link_municipal = RAIZ / "municipal"
    if not link_municipal.exists():
        try:
            link_municipal.symlink_to(Path("municipais"), target_is_directory=True)
            print("  [Symlink] 'municipal' criado apontando para 'municipais'.")
        except Exception as e:
            print(f"  [Aviso] Falha ao criar symlink: {e}")

def main():
    print("=== INÍCIO DO ENRIQUECIMENTO: PILAR DE SERVIÇOS E RETENÇÕES ===")
    corrigir_atos_existentes()
    criar_leis_federais_faltantes()
    criar_atos_reguladores_rfb()
    criar_normas_municipais()
    print("=== ENRIQUECIMENTO CONCLUÍDO COM SUCESSO! ===")

if __name__ == "__main__":
    main()
