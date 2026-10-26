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
        
        # Identificação de tributos afetados na ementa
        tributos = []
        ementa_lower = ementa.lower()
        if "irpj" in ementa_lower or "imposto sobre a renda" in ementa_lower or "renda" in ementa_lower:
            tributos.append("IRPJ")
        if "csll" in ementa_lower or "contribuição social sobre o lucro" in ementa_lower:
            tributos.append("CSLL")
        if "pis" in ementa_lower:
            tributos.append("PIS/Pasep")
        if "cofins" in ementa_lower:
            tributos.append("Cofins")
        if "simples nacional" in ementa_lower:
            tributos.append("Simples Nacional")
        if "ipi" in ementa_lower:
            tributos.append("IPI")
        if "itr" in ementa_lower or "territorial rural" in ementa_lower:
            tributos.append("ITR")

        epigrafe = dados_ato.get("epigrafeCompleta") or f"{tipo_nome} RFB nº {numero}, de {ano}"
        titulo = epigrafe
        
        meta = {
            "titulo": titulo,
            "esfera": "Federal",
            "orgao": "Secretaria Especial da Receita Federal do Brasil",
            "tipo": tipo_nome,
            "numero": numero,
            "ano": ano,
            "data": data_pub[:10] if data_pub else None,
            "tributos_afetados": tributos if tributos else None,
            "situacao": "Em vigor" if not dados_ato.get("revogado") else "Revogada",
            "revogada": bool(dados_ato.get("revogado")),
            "fonte": f"https://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action?idAto={id_ato}",
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
        print(f"[Agente Estruturador] Documento gerado: {arquivo_destino.relative_to(RAIZ)}")
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
