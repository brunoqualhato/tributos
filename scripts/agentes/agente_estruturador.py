"""Agente Especialista em Estruturação de Documentos e Qualidade.

Responsável por converter documentos brutos em Markdown estrito (CommonMark)
com cabeçalho YAML canônico, garantindo a integridade dos textos fiscais.
"""
from pathlib import Path
import html as html_module
import json
import re
import sys

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from comum import gerar_frontmatter, salvar_atomico
from html2md import converter_html_para_md

MESES = {
    "janeiro": "01", "fevereiro": "02", "março": "03", "marco": "03",
    "abril": "04", "maio": "05", "junho": "06", "julho": "07",
    "agosto": "08", "setembro": "09", "outubro": "10", "novembro": "11",
    "dezembro": "12"
}

def classificar_tributos_e_tema(texto_completo: str):
    """Classifica automaticamente o tema tributário e lista os tributos afetados."""
    txt_clean = re.sub(r'<[^>]+>', ' ', texto_completo)
    txt = html_module.unescape(txt_clean.lower())
    tributos = []
    temas = []

    # 1. Pilar Dividendos & Renda do Capital
    if any(k in txt for k in (
        "dividendo", "juros sobre o capital próprio", "juros sobre capital próprio", "jcp",
        "distribuição de lucros", "lucro real", "lucro presumido", "offshore", "trust",
        "ganho de capital", "equivalência patrimonial", "subvenção", "subvenções", "ágio",
        "incorporação", "cisão", "fusão", "renda do capital", "imposto sobre a renda",
        "contribuição social sobre o lucro", "lucro líquido", "irpj", "csll", "irpf", "irrf",
        "14.754", "14.789", "12.973", "9.249", "1.598", "1598", "9.580", "9580", "1.700", "1700",
        "renda das pessoas jurídicas"
    )):
        temas.append("Dividendos e Renda do Capital")
        for trib in ["IRPJ", "CSLL", "IRPF", "IRRF"]:
            if trib not in tributos:
                tributos.append(trib)

    # 2. Pilar Folha & Funcionário
    if any(k in txt for k in ("folha de pagamento", "salário", "pró-labore", "pro-labore", "remuneração", "previdenciária", "inss", "rat", "fap", "fgts", "esocial", "seguridade social", "sistema s", "cprb", "desoneração da folha", "comprovante de rendimentos", "pensão alimentícia")):
        temas.append("Folha de Pagamento e Encargos")
        if "inss" in txt or "previdenciár" in txt or "seguridade" in txt:
            tributos.append("INSS Patronal/Segurados")
        if "rat" in txt or "fap" in txt:
            tributos.append("RAT/FAP")
        if "sistema s" in txt or "salário-educação" in txt or "incra" in txt:
            tributos.append("Contribuições a Terceiros (Sistema S)")
        if "fgts" in txt:
            tributos.append("FGTS")
        if "desoneração" in txt or "cprb" in txt:
            tributos.append("CPRB (Desoneração da Folha)")

    # 3. Pilar Produtos & Mercadorias
    if any(k in txt for k in ("icms", "ipi", "mercadoria", "circulação de mercadorias", "industrialização", "tipi", "importação", "substituição tributária", "imposto seletivo", "monofásic", "desembaraço aduaneiro")):
        temas.append("Produtos e Mercadorias")
        if "icms" in txt:
            tributos.append("ICMS")
        if "substituição tributária" in txt or "icms-st" in txt:
            tributos.append("ICMS-ST")
        if "ipi" in txt or "industrializados" in txt:
            tributos.append("IPI")
        if "importação" in txt or "aduaneir" in txt:
            tributos.append("Imposto de Importação")
        if "imposto seletivo" in txt:
            tributos.append("Imposto Seletivo")

    # 4. Pilar Serviços & Retenções
    if any(k in txt for k in ("issqn", "imposto sobre serviços", "lc 116", "prestação de serviços", "csrf", "retenção na fonte", "cessão de mão de obra", "serviços profissionais", "retenção", "retido na fonte", "irrf", "tomador")):
        temas.append("Serviços e Retenções")
        if "iss" in txt:
            tributos.append("ISSQN")
        if "csrf" in txt or ("retenção" in txt and ("pis" in txt or "cofins" in txt)):
            tributos.append("CSRF (Retenção 4,65%)")
        if "cessão de mão de obra" in txt or "retenção de 11%" in txt:
            tributos.append("Retenção INSS 11%")
        if "irrf" in txt or "imposto sobre a renda retido" in txt:
            tributos.append("IRRF")

    # 5. Contabilidade & Normas Técnicas
    if any(k in txt for k in ("pronunciamento técnico", "cpc ", "nbc ", "demonstrações contábeis", "escrituração contábil", "ifrs", "balanço patrimonial", "dfc", "ativo intangível", "ativo imobilizado", "depreciação")):
        temas.append("Contabilidade")
        tributos.append("Contabilidade Societária e Fiscal")

    # PIS e COFINS gerais
    if "pis" in txt and "PIS/Pasep" not in tributos:
        tributos.append("PIS/Pasep")
    if "cofins" in txt and "Cofins" not in tributos:
        tributos.append("Cofins")

    # Garante um dos 5 temas canônicos
    if temas:
        tema_principal = temas[0]
    else:
        # Fallbacks canônicos baseados em palavras-chave menores
        if "renda" in txt or "capital" in txt or "lucro" in txt:
            tema_principal = "Dividendos e Renda do Capital"
        elif "trabalho" in txt or "empreg" in txt or "benefício" in txt:
            tema_principal = "Folha de Pagamento e Encargos"
        elif "produto" in txt or "bem" in txt or "comércio" in txt:
            tema_principal = "Produtos e Mercadorias"
        elif "contábil" in txt or "contabilidade" in txt:
            tema_principal = "Contabilidade"
        else:
            tema_principal = "Serviços e Retenções"

    return tema_principal, sorted(list(set(tributos)))


class AgenteEstruturador:
    def __init__(self):
        pass

    def estruturar_ato_rfb(self, dados_ato: dict, pasta_customizada: Path = None) -> Path:
        """Converte um ato bruto da API do Sijut/RFB em arquivo Markdown."""
        id_ato = str(dados_ato.get("idAto"))
        epigrafe_completa = dados_ato.get("epigrafeCompleta") or ""
        epigrafe_dict = dados_ato.get("epigrafe") if isinstance(dados_ato.get("epigrafe"), dict) else {}
        
        numero = str(dados_ato.get("numeroAto") or dados_ato.get("numero") or epigrafe_dict.get("numeroAto") or "")
        data_ato = epigrafe_dict.get("dataAto") or dados_ato.get("dataPublicacao") or ""
        ano = str(dados_ato.get("anoAto") or dados_ato.get("ano") or (data_ato[:4] if len(data_ato) >= 4 else ""))
        
        tipo_info = dados_ato.get("tipoAto") or epigrafe_dict.get("tipoAto")
        tipo_nome = tipo_info.get("nomeTipoAto") if isinstance(tipo_info, dict) else (dados_ato.get("tipo") or "")
        data_pub = dados_ato.get("dataPublicacao", "")

        # Se numero, ano ou tipo_nome faltarem, extrai via regex de epigrafeCompleta
        if not numero or not ano or not tipo_nome or numero == "None" or ano == "None":
            m = re.match(r"^(.*?)\s+n[º°\.]?\s*([0-9\.\-/]+)(?:.*?de\s+(\d{1,2})\s+de\s+([a-zA-Zç]+)\s+de\s+(\d{4}))?", epigrafe_completa, re.I)
            if m:
                if not tipo_nome or tipo_nome == "None":
                    tipo_nome = m.group(1).strip()
                if not numero or numero == "None":
                    numero = m.group(2).replace(".", "").strip()
                if (not ano or ano == "None") and m.group(5):
                    ano = m.group(5).strip()
                if not data_pub and m.group(3) and m.group(4) and m.group(5):
                    dia = m.group(3).zfill(2)
                    mes = MESES.get(m.group(4).lower(), "01")
                    ano_match = m.group(5)
                    data_pub = f"{ano_match}-{mes}-{dia}"

        if not tipo_nome:
            tipo_nome = "Instrução Normativa" if "normativa" in epigrafe_completa.lower() else "Solução de Consulta"
        if not ano and data_pub:
            ano = data_pub[:4]

        # Ementa pode vir no campo direto ou na lista de ementas
        ementa = dados_ato.get("ementa", "")
        if not ementa and dados_ato.get("ementas"):
            ementa = " ".join(e.get("textoIntegra", "") for e in dados_ato.get("ementas", []))

        # Limpeza e decodificação rigorosa da ementa
        ementa = html_module.unescape(ementa)
        ementa = re.sub(r'<[^>]+>', ' ', ementa)
        ementa = re.sub(r'\s+', ' ', ementa).strip()

        # Extrai os segmentos de texto
        segmentos = sorted(dados_ato.get("outrosSegmentos", []), key=lambda x: x.get("ordemSegmentoAto", 0))
        partes_texto = []
        for seg in segmentos:
            t = seg.get("textoIntegra") or ""
            if t and t.strip():
                partes_texto.append(t)
                
        texto_html = "\n\n".join(partes_texto) or (dados_ato.get("texto", "") or dados_ato.get("conteudo", ""))
        
        # Se os segmentos de texto forem vazios (caso comum em Soluções de Consulta), utiliza a ementa
        if not texto_html.strip() and ementa:
            texto_html = f"<p>{ementa}</p>"

        # Classificação semântica do tema e tributos
        texto_para_classificacao = f"{ementa} {epigrafe_completa} {texto_html[:4000]}"
        tema_tributario, tributos = classificar_tributos_e_tema(texto_para_classificacao)

        titulo = epigrafe_completa or f"{tipo_nome} RFB nº {numero}, de {ano}"
        url_visual = dados_ato.get("urlVisualizacao") or f"https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{id_ato}"

        meta = {
            "titulo": titulo,
            "esfera": "Federal",
            "orgao": "Secretaria Especial da Receita Federal do Brasil",
            "tipo": tipo_nome,
            "numero": numero or "sn",
            "ano": ano,
            "data": data_pub[:10] if data_pub else f"{ano}-01-01",
            "tema_tributario": tema_tributario,
            "tributos_afetados": tributos if tributos else None,
            "situacao": "Em vigor" if not dados_ato.get("revogado") else "Revogada",
            "revogada": bool(dados_ato.get("revogado")),
            "fonte": url_visual,
            "ementa": ementa or titulo
        }

        frontmatter = gerar_frontmatter(meta)
        corpo_md = converter_html_para_md(texto_html)
        
        if not corpo_md.strip():
            corpo_md = f"## Ementa e Fundamentação Legal\n\n{ementa}\n"
        elif ementa and not corpo_md.strip().startswith(ementa[:50]):
            corpo_md = f"## Ementa\n\n{ementa}\n\n{corpo_md}"

        conteudo_final = f"{frontmatter}# {titulo}\n\n{corpo_md}\n"

        if pasta_customizada:
            pasta_destino = pasta_customizada
        else:
            # Caminho canônico: reguladores/rfb/instrucoes-normativas/AAAA/ato-ID-NUM-ANO.md
            slug_tipo = "instrucoes-normativas" if "normativa" in tipo_nome.lower() else "outros-atos"
            pasta_destino = RAIZ / "reguladores" / "rfb" / slug_tipo / ano
        arquivo_destino = pasta_destino / f"ato-{id_ato}-{numero or 'sn'}-{ano}.md"

        ja_existia = arquivo_destino.exists()
        salvar_atomico(arquivo_destino, conteudo_final.encode("utf-8"))
        if not ja_existia:
            print(f"[Agente Estruturador] Novo documento gerado: {arquivo_destino.relative_to(RAIZ)} [Tema: {tema_tributario}]")
            return arquivo_destino
        return None

    def estruturar_lei_federal(self, numero: str, ano: str, ementa: str, html: str, tipo: str = "Lei Complementar") -> Path:
        """Estrutura leis federais (como CTN, Kandir, etc.)."""
        titulo = f"{tipo} nº {numero}, de {ano}"
        tema_tributario, tributos = classificar_tributos_e_tema(f"{ementa} {html[:4000]}")
        meta = {
            "titulo": titulo,
            "esfera": "Federal",
            "orgao": "Congresso Nacional / Presidência da República",
            "tipo": tipo,
            "numero": numero,
            "ano": ano,
            "data": f"{ano}-01-01",
            "tema_tributario": tema_tributario,
            "tributos_afetados": tributos if tributos else ["Sistema Tributário Nacional"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": "https://www.planalto.gov.br",
            "ementa": html_module.unescape(ementa).strip()
        }
        frontmatter = gerar_frontmatter(meta)
        corpo_md = converter_html_para_md(html)
        conteudo_final = f"{frontmatter}# {titulo}\n\n{corpo_md}\n"

        destino = RAIZ / "federal" / "leis-complementares" / f"lei-{numero}-{ano}.md"
        salvar_atomico(destino, conteudo_final.encode("utf-8"))
        print(f"[Agente Estruturador] Lei estruturada: {destino.relative_to(RAIZ)}")
        return destino

if __name__ == "__main__":
    estruturador = AgenteEstruturador()
    print("[Agente Estruturador] Pronto para processamento de lote.")
