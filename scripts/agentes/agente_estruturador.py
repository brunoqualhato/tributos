"""Agente Especialista em Estruturação de Documentos e Qualidade.

Responsável por converter documentos brutos em Markdown estrito (CommonMark)
com cabeçalho YAML canônico, garantindo a integridade dos textos fiscais.
"""
from pathlib import Path
import json
import re
import sys

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from comum import gerar_frontmatter, salvar_atomico
from html2md import converter_html_para_md

def classificar_tributos_e_tema(texto_completo: str):
    """Classifica automaticamente o tema tributário e lista os tributos afetados."""
    txt = texto_completo.lower()
    tributos = []
    temas = []

    # 1. Pilar Dividendos & Renda do Capital
    if any(k in txt for k in ("dividendo", "juros sobre o capital próprio", "juros sobre capital próprio", "jcp", "distribuição de lucros", "lucro real", "lucro presumido", "offshore", "trust", "ganho de capital", "equivalência patrimonial")):
        temas.append("Dividendos e Renda do Capital")
        if "dividendo" in txt or "distribuição de lucros" in txt:
            tributos.append("Dividendos/Lucros")
        if "juros sobre o capital próprio" in txt or "juros sobre capital próprio" in txt or "jcp" in txt:
            tributos.append("JCP")
        if "lucro real" in txt or "lucro presumido" in txt or "irpj" in txt:
            tributos.append("IRPJ")
        if "csll" in txt or "contribuição social sobre o lucro" in txt:
            tributos.append("CSLL")

    # 2. Pilar Folha & Funcionário
    if any(k in txt for k in ("folha de pagamento", "salário", "pró-labore", "pro-labore", "remuneração", "previdenciária", "inss", "rat", "fap", "fgts", "esocial", "seguridade social", "sistema s", "cprb", "desoneração da folha")):
        temas.append("Folha de Pagamento e Encargos")
        if "inss" in txt or "previdenciár" in txt:
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
    if any(k in txt for k in ("icms", "ipi", "mercadoria", "circulação de mercadorias", "industrialização", "tipi", "importação", "substituição tributária", "imposto seletivo", "monofásic")):
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
    if any(k in txt for k in ("issqn", "imposto sobre serviços", "lc 116", "prestação de serviços", "csrf", "retenção na fonte", "cessão de mão de obra", "serviços profissionais")):
        temas.append("Serviços e Retenções")
        if "iss" in txt:
            tributos.append("ISSQN")
        if "csrf" in txt or ("retenção" in txt and ("pis" in txt or "cofins" in txt)):
            tributos.append("CSRF (Retenção 4,65%)")
        if "cessão de mão de obra" in txt or "retenção de 11%" in txt:
            tributos.append("Retenção INSS 11%")

    # PIS e COFINS gerais
    if "pis" in txt and "PIS/Pasep" not in tributos:
        tributos.append("PIS/Pasep")
    if "cofins" in txt and "Cofins" not in tributos:
        tributos.append("Cofins")

    tema_principal = temas[0] if temas else "Tributário e Contábil Geral"
    return tema_principal, sorted(list(set(tributos)))


class AgenteEstruturador:
    def __init__(self):
        pass

    def estruturar_ato_rfb(self, dados_ato: dict) -> Path:
        """Converte um ato bruto da API do Sijut/RFB em arquivo Markdown."""
        id_ato = dados_ato.get("idAto")
        numero = str(dados_ato.get("numeroAto") or dados_ato.get("numero") or "")
        ano = str(dados_ato.get("anoAto") or dados_ato.get("ano") or "")
        tipo_info = dados_ato.get("tipoAto")
        tipo_nome = tipo_info.get("nomeTipoAto") if isinstance(tipo_info, dict) else (dados_ato.get("tipo") or "Instrução Normativa")
        data_pub = dados_ato.get("dataPublicacao", "")
        
        # Ementa pode vir no campo direto ou na lista de ementas
        ementa = dados_ato.get("ementa", "")
        if not ementa and dados_ato.get("ementas"):
            ementa = " ".join(e.get("textoIntegra", "") for e in dados_ato.get("ementas", []))

        # Limpeza de HTML residual da ementa
        ementa = re.sub(r'<[^>]+>', ' ', ementa)
        ementa = re.sub(r'&quot;', '"', ementa)
        ementa = re.sub(r'\s+', ' ', ementa).strip()

        # Extrai os segmentos de texto
        segmentos = sorted(dados_ato.get("outrosSegmentos", []), key=lambda x: x.get("ordemSegmentoAto", 0))
        partes_texto = []
        for seg in segmentos:
            t = seg.get("textoIntegra") or ""
            if t:
                partes_texto.append(t)
                
        texto_html = "\n\n".join(partes_texto) or (dados_ato.get("texto", "") or dados_ato.get("conteudo", ""))
        
        # Classificação semântica do tema e tributos
        texto_para_classificacao = f"{ementa} {dados_ato.get('epigrafeCompleta', '')} {texto_html[:3000]}"
        tema_tributario, tributos = classificar_tributos_e_tema(texto_para_classificacao)

        epigrafe = dados_ato.get("epigrafeCompleta") or f"{tipo_nome} RFB nº {numero}, de {ano}"
        titulo = epigrafe
        
        url_visual = dados_ato.get("urlVisualizacao") or f"https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{id_ato}"

        meta = {
            "titulo": titulo,
            "esfera": "Federal",
            "orgao": "Secretaria Especial da Receita Federal do Brasil",
            "tipo": tipo_nome,
            "numero": numero,
            "ano": ano,
            "data": data_pub[:10] if data_pub else None,
            "tema_tributario": tema_tributario,
            "tributos_afetados": tributos if tributos else None,
            "situacao": "Em vigor" if not dados_ato.get("revogado") else "Revogada",
            "revogada": bool(dados_ato.get("revogado")),
            "fonte": url_visual,
            "ementa": ementa
        }

        frontmatter = gerar_frontmatter(meta)
        corpo_md = converter_html_para_md(texto_html)
        conteudo_final = f"{frontmatter}# {titulo}\n\n{corpo_md}\n"

        # Caminho canônico: reguladores/rfb/instrucoes-normativas/AAAA/in-NUMERO-AAAA.md
        slug_tipo = "instrucoes-normativas" if "normativa" in tipo_nome.lower() else "outros-atos"
        pasta_destino = RAIZ / "reguladores" / "rfb" / slug_tipo / ano
        arquivo_destino = pasta_destino / f"ato-{id_ato}-{numero or 'sn'}-{ano}.md"

        salvar_atomico(arquivo_destino, conteudo_final.encode("utf-8"))
        print(f"[Agente Estruturador] Documento gerado: {arquivo_destino.relative_to(RAIZ)} [Tema: {tema_tributario}]")
        return arquivo_destino

    def estruturar_lei_federal(self, numero: str, ano: str, ementa: str, html: str, tipo: str = "Lei Complementar") -> Path:
        """Estrutura leis federais (como CTN, Kandir, etc.)."""
        titulo = f"{tipo} nº {numero}, de {ano}"
        meta = {
            "titulo": titulo,
            "esfera": "Federal",
            "orgao": "Congresso Nacional / Presidência da República",
            "tipo": tipo,
            "numero": numero,
            "ano": ano,
            "data": f"{ano}-01-01",
            "tributos_afetados": ["Sistema Tributário Nacional"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": "https://www.planalto.gov.br",
            "ementa": ementa
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
