#!/usr/bin/env python3
"""Auditoria de Integridade Total do Acervo Tributário.

Realiza a varredura e inspeção profunda de todos os documentos Markdown do acervo:
1. Validade do Schema (cabeçalho frontmatter, campos obrigatórios, tipos e coerência)
2. Autenticidade da Fonte (domínios oficiais, URLs diretas vs legadas)
3. Tamanho e Profundidade Textual (micro-resumos, normas vazias, distribuição)
4. Duplicidade de Conteúdo e Fragmentação Artificial (ex: PLP 68 fatiado em 5 arquivos)
5. Situação de Vigência (normas revogadas marcadas como em vigor e vice-versa, ex: CPC 08, 17, 30, 38)
6. Qualidade Formal do Corpo (HTML residual, caracteres corrompidos, mojibake, scraping junk, tabelas quebradas)
"""

import json
import re
import sys
import urllib.parse
from collections import defaultdict, Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

DOMINIOS_OFICIAIS_PERMITIDOS = {
    "gov.br",
    "leg.br",
    "jus.br",
    "cfc.org.br",
    "cpc.org.br",
    "leismunicipais.com.br",
    "atosoficiais.com.br"
}

IGNORED_NAMES = {
    "README.md", "PROGRESSO.md", "PLANO.md", "WORKLOG.md",
    "COBERTURA.md", "AGENT.md", "ACERVO.md"
}
IGNORED_DIRS = {"_auditoria", "_fonte", "wiki", ".git", ".gemini", "node_modules"}

REQUIRED_FIELDS = [
    "titulo", "esfera", "orgao", "tipo", "numero",
    "ano", "data", "tema_tributario", "situacao", "fonte", "ementa"
]

HTML_TAG_REGEX = re.compile(
    r"</?(?:script|style|div|span|p|br|table|tr|td|th|tbody|thead|a|b|i|font|iframe|strong|em|img|hr)[\s/>]",
    re.IGNORECASE
)

MOJIBAKE_REGEX = re.compile(r"(?:Ã§|Ã£|Ã©|Ã¡|Ã³|Ãº|â€|Â§|Âº|Âª|Â\s|Ã‚|Ãµ|Ãª|Ã­)")
HTML_ENTITY_REGEX = re.compile(r"&(?:nbsp|amp|quot|lt|gt|#\d+|#[xX][0-9a-fA-F]+);")

def extrair_frontmatter_e_corpo(conteudo: str):
    if not conteudo.startswith("---"):
        return {}, conteudo, "Frontmatter ausente (arquivo não inicia com ---)"
    partes = conteudo.split("---", 2)
    if len(partes) < 3:
        return {}, conteudo, "Frontmatter malformado (delimitador --- de fechamento não encontrado)"
    
    cabecalho = partes[1]
    corpo = partes[2].strip()
    
    meta = {}
    linhas = cabecalho.strip().splitlines()
    for l in linhas:
        m = re.match(r"^([a-zA-Z0-9_]+):\s*(.*)$", l)
        if m:
            k = m.group(1).strip()
            v = m.group(2).strip()
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1].replace('\\"', '"')
            elif v.startswith("'") and v.endswith("'"):
                v = v[1:-1].replace("\\'", "'")
            elif v.startswith("[") and v.endswith("]"):
                # Simples lista de strings
                itens = [i.strip(' "\'') for i in v[1:-1].split(",") if i.strip()]
                v = itens
            elif v.lower() == "true":
                v = True
            elif v.lower() == "false":
                v = False
            elif v.lower() == "null" or v == "":
                v = None
            meta[k] = v
            
    return meta, corpo, None

def auditar_tudo():
    docs = sorted([
        p for p in RAIZ.glob("**/*.md")
        if not any(part.startswith(".") for part in p.parts)
        and p.name not in IGNORED_NAMES
        and not any(part in IGNORED_DIRS for part in p.parts)
    ])
    
    total_docs = len(docs)
    print(f"[Auditor] Iniciando auditoria total de {total_docs} documentos...")

    # Estruturas de diagnóstico
    diagnostico = {
        "resumo": {
            "total_documentos": total_docs,
            "taxa_conformidade_schema": "0%",
            "documentos_com_inconformidades": 0,
            "distribuicao_linhas": Counter(),
            "distribuicao_esferas": Counter(),
            "distribuicao_temas": Counter(),
        },
        "schema_inconformidades": defaultdict(list),
        "fontes_inconformidades": defaultdict(list),
        "profundidade_textual": {
            "vazios_sem_corpo": [],
            "micro_resumos_criticos": [],  # Normas de grande porte < 50 linhas
            "stubs_sinteticos_estaduais": [], # Leis estaduais resumidas
            "estatisticas_linhas": {}
        },
        "duplicidade_e_fragmentacao": {
            "normas_fatiadas": {},
            "duplicidades_exatas": {},
            "duplicidades_normativas": {} # Mesmo tipo, numero e ano
        },
        "vigencia_inconsistencias": {
            "revogadas_marcadas_em_vigor": [],
            "em_vigor_marcadas_revogadas": [],
            "inconsistencias_flag_revogada": []
        },
        "qualidade_corpo": {
            "html_residual": [],
            "mojibake_e_caracteres_corrompidos": [],
            "html_entities_residuais": [],
            "marcadores_raspagem_lexml": [],
            "scraping_boilerplate": [],
            "tabelas_quebradas": [],
            "ausencia_titulo_h1": [],
            "inconsistencias_nomenclatura_arquivo": []
        },
        "detalhes_por_arquivo": {}
    }

    normas_por_chave = defaultdict(list)
    normas_por_titulo = defaultdict(list)
    plp68_files = []

    for p in docs:
        rel = str(p.relative_to(RAIZ))
        conteudo = p.read_text(encoding="utf-8", errors="replace")
        linhas = conteudo.splitlines()
        n_linhas = len(linhas)
        n_chars = len(conteudo)
        
        meta, corpo, erro_fm = extrair_frontmatter_e_corpo(conteudo)
        
        erros_arquivo = []
        avisos_arquivo = []
        
        # 1. Contagem de linhas
        if n_linhas < 50:
            diagnostico["resumo"]["distribuicao_linhas"]["<50"] += 1
        elif n_linhas <= 100:
            diagnostico["resumo"]["distribuicao_linhas"]["50-100"] += 1
        elif n_linhas <= 300:
            diagnostico["resumo"]["distribuicao_linhas"]["101-300"] += 1
        elif n_linhas <= 1000:
            diagnostico["resumo"]["distribuicao_linhas"]["301-1000"] += 1
        else:
            diagnostico["resumo"]["distribuicao_linhas"][">1000"] += 1

        # 2. Schema Check
        if erro_fm:
            erros_arquivo.append(erro_fm)
            diagnostico["schema_inconformidades"]["frontmatter_invalido"].append({"arquivo": rel, "erro": erro_fm})
        else:
            for campo in REQUIRED_FIELDS:
                if campo not in meta:
                    erros_arquivo.append(f"Campo obrigatório ausente: '{campo}'")
                    diagnostico["schema_inconformidades"][f"ausente_{campo}"].append(rel)
                elif meta[campo] is None or str(meta[campo]).strip() in ("", "null", "N/A", "TODO"):
                    erros_arquivo.append(f"Campo obrigatório vazio/placeholder: '{campo}'")
                    diagnostico["schema_inconformidades"][f"vazio_{campo}"].append(rel)

            esfera = meta.get("esfera", "Indefinida")
            tema = meta.get("tema_tributario", "Indefinido")
            diagnostico["resumo"]["distribuicao_esferas"][str(esfera)] += 1
            diagnostico["resumo"]["distribuicao_temas"][str(tema)] += 1

        # 3. Fonte Check
        fonte = meta.get("fonte", "")
        if not fonte or str(fonte).strip() in ("", "null", "N/A"):
            erros_arquivo.append("Campo 'fonte' vazio ou nulo")
            diagnostico["fontes_inconformidades"]["fonte_vazia"].append(rel)
        else:
            fonte_str = str(fonte).strip()
            if "sijut2consulta/consulta.action" in fonte_str:
                erros_arquivo.append("Fonte usa URL legada sijut2consulta que não abre o ato diretamente")
                diagnostico["fontes_inconformidades"]["url_legada_rfb"].append({"arquivo": rel, "fonte": fonte_str})
            try:
                parsed = urllib.parse.urlparse(fonte_str)
                dom = parsed.netloc.lower().split(":")[0]
                confiavel = any(dom == d or dom.endswith("." + d) for d in DOMINIOS_OFICIAIS_PERMITIDOS)
                if not confiavel:
                    erros_arquivo.append(f"Fonte em domínio não-oficial ({dom})")
                    diagnostico["fontes_inconformidades"]["dominio_nao_oficial"].append({"arquivo": rel, "fonte": fonte_str, "dominio": dom})
            except Exception as e:
                erros_arquivo.append(f"URL de fonte inválida: {fonte_str} ({e})")
                diagnostico["fontes_inconformidades"]["url_invalida"].append({"arquivo": rel, "fonte": fonte_str, "erro": str(e)})

        # 4. Profundidade Textual e Micro-resumos
        # Separar linhas de corpo após H1
        linhas_corpo = [l.strip() for l in corpo.splitlines() if l.strip() and not l.startswith("# ")]
        texto_corpo = "\n".join(linhas_corpo).strip()
        tipo_ato = str(meta.get("tipo", ""))
        titulo_ato = str(meta.get("titulo", ""))
        numero_ato = str(meta.get("numero", ""))
        ano_ato = str(meta.get("ano", ""))

        if len(texto_corpo) == 0:
            erros_arquivo.append("Documento com corpo textual COMPLETAMENTE VAZIO após título H1")
            diagnostico["profundidade_textual"]["vazios_sem_corpo"].append({
                "arquivo": rel,
                "titulo": titulo_ato,
                "tipo": tipo_ato,
                "linhas": n_linhas
            })
        elif n_linhas < 50:
            # Identifica normas de alto escalão que deveriam ser completas
            alto_escalao = any(k in tipo_ato.lower() for k in ["emenda", "lei", "decreto", "resolução", "regulamento", "projeto"])
            if alto_escalao:
                if "estaduais/" in rel and ("/ipva/" in rel or "/itcmd/" in rel):
                    diagnostico["profundidade_textual"]["stubs_sinteticos_estaduais"].append({
                        "arquivo": rel,
                        "titulo": titulo_ato,
                        "linhas": n_linhas,
                        "motivo": "Lei estadual sintetizada estruturalmente em 40-48 linhas gerada por template/script"
                    })
                    avisos_arquivo.append(f"Norma estadual sintetizada em esboço ({n_linhas} linhas)")
                else:
                    diagnostico["profundidade_textual"]["micro_resumos_criticos"].append({
                        "arquivo": rel,
                        "titulo": titulo_ato,
                        "tipo": tipo_ato,
                        "linhas": n_linhas,
                        "caracteres": n_chars,
                        "motivo": "Norma federal/geral de grande porte representada apenas por resumo conciso (< 50 linhas)"
                    })
                    avisos_arquivo.append(f"Norma primária de alta complexidade em micro-resumo ({n_linhas} linhas)")

        # 5. Duplicidade e Fatiamento de Normas
        # PLP 68
        if rel in (
            "reforma-tributaria/plp-68-2024.md",
            "reforma-tributaria/split-payment/arquitetura-split-payment-plp68.md",
            "reforma-tributaria/split-payment/split-payment-modelo-operacional.md",
            "reforma-tributaria/imposto-seletivo/incidencia-e-aliquotas-plp68.md",
            "reforma-tributaria/regimes-especificos/regimes-diferenciados-plp68.md"
        ):
            plp68_files.append(rel)

        chave_norma = f"{tipo_ato} {numero_ato}/{ano_ato}".strip()
        if tipo_ato and numero_ato and ano_ato and numero_ato != "0":
            normas_por_chave[chave_norma].append(rel)
        if titulo_ato:
            normas_por_titulo[titulo_ato].append(rel)

        # Inconsistência de nomenclatura de arquivo vs tipo
        nome_arquivo = Path(rel).name
        if nome_arquivo.startswith("lei-") and "decreto-lei" in tipo_ato.lower():
            diagnostico["qualidade_corpo"]["inconsistencias_nomenclatura_arquivo"].append({
                "arquivo": rel, "nome": nome_arquivo, "tipo": tipo_ato,
                "problema": "Arquivo nomeado com prefixo 'lei-' mas o tipo é Decreto-Lei"
            })
            avisos_arquivo.append(f"Inconsistência de nomenclatura: arquivo '{nome_arquivo}' vs tipo '{tipo_ato}'")
        elif nome_arquivo.startswith("lei-") and tipo_ato.lower() == "decreto":
            diagnostico["qualidade_corpo"]["inconsistencias_nomenclatura_arquivo"].append({
                "arquivo": rel, "nome": nome_arquivo, "tipo": tipo_ato,
                "problema": "Arquivo nomeado com prefixo 'lei-' mas o tipo é Decreto regulamentar"
            })
            avisos_arquivo.append(f"Inconsistência de nomenclatura: arquivo '{nome_arquivo}' vs tipo '{tipo_ato}'")

        # 6. Situação de Vigência
        situacao = str(meta.get("situacao", "")).strip()
        flag_revogada = meta.get("revogada", None)
        
        # Inconsistência entre flag_revogada e campo situacao
        if flag_revogada is True and "vigor" in situacao.lower():
            erros_arquivo.append(f"Incoerência: flag revogada=true mas situacao='{situacao}'")
            diagnostico["vigencia_inconsistencias"]["inconsistencias_flag_revogada"].append({
                "arquivo": rel, "situacao": situacao, "revogada": flag_revogada
            })
        elif flag_revogada is False and "revogad" in situacao.lower():
            erros_arquivo.append(f"Incoerência: flag revogada=false mas situacao='{situacao}'")
            diagnostico["vigencia_inconsistencias"]["inconsistencias_flag_revogada"].append({
                "arquivo": rel, "situacao": situacao, "revogada": flag_revogada
            })

        # Casos especiais conhecidos: CPC 08, 17, 30, 38
        if "cpc-08.md" in rel and "revogad" in situacao.lower():
            # CPC 08 está marcado como Revogada no frontmatter, mas CPC 08 (R1) está EM VIGOR
            diagnostico["vigencia_inconsistencias"]["em_vigor_marcadas_revogadas"].append({
                "arquivo": rel,
                "norma": "CPC 08 (R1)",
                "situacao_atual": situacao,
                "diagnostico_vigencia": "CPC 08 (R1) está plenamente EM VIGOR (CVM 649/2010, NBC TG 08). Foi erroneamente marcado como Revogada no acervo."
            })
            erros_arquivo.append("CPC 08 está EM VIGOR (R1), mas foi marcado erroneamente como 'Revogada'")

        if any(c in rel for c in ["cpc-17.md", "cpc-30.md", "cpc-38.md"]):
            # CPCs 17, 30 e 38 foram revogados em 01/01/2018 (pelo CPC 47 e CPC 48).
            if "revogad" not in situacao.lower():
                erros_arquivo.append(f"{rel} foi revogado pelo CPC 47/48 em 2018 mas não está com situação 'Revogada'")
                diagnostico["vigencia_inconsistencias"]["revogadas_marcadas_em_vigor"].append({
                    "arquivo": rel, "situacao": situacao, "motivo": "Revogado pelo CPC 47/48 em 01/01/2018"
                })

        # Verificação do Decreto Municipal nº 53.151/2012 (antigo RISS/SP)
        if rel == "municipais/sp/servicos-iss/decreto-53151-2012.md" and "vigor" in situacao.lower():
            erros_arquivo.append("Decreto 53.151/2012 (antigo RISS/SP) foi REVOGADO pelo Decreto nº 58.701/2019, mas consta como 'Em vigor'")
            diagnostico["vigencia_inconsistencias"]["revogadas_marcadas_em_vigor"].append({
                "arquivo": rel,
                "norma": "Decreto nº 53.151/2012 (RISS/SP)",
                "situacao_atual": situacao,
                "diagnostico_vigencia": "Revogado expressamente pelo Decreto Municipal nº 58.701/2019 (art. 177). Deve ser marcado como 'Revogada'."
            })

        # Verificação textual de revogação no corpo
        # Detectar se o ato foi expressamente revogado mas consta como "Em vigor"
        if "vigor" in situacao.lower() and rel != "municipais/sp/servicos-iss/decreto-53151-2012.md":
            m_rev = re.search(r"(?:este\s+regulamento\s+foi\s+revogado|ficam?\s+revogad[ao]s?\s+integralmente|revogad[ao]\s+pel[ao]\s+Decreto\s+n[ºo°]\s*58\.701)", corpo, re.IGNORECASE)
            if m_rev:
                erros_arquivo.append(f"Texto indica revogação expressa ('{m_rev.group(0)}'), mas situação consta como '{situacao}'")
                diagnostico["vigencia_inconsistencias"]["revogadas_marcadas_em_vigor"].append({
                    "arquivo": rel, "situacao": situacao, "trecho": m_rev.group(0)
                })

        # 7. Qualidade do Corpo
        if not corpo.startswith("# "):
            erros_arquivo.append("Corpo textual não inicia com '# Título' (Heading 1)")
            diagnostico["qualidade_corpo"]["ausencia_titulo_h1"].append(rel)

        # Marcadores brutos de controle LexML / Senado
        lexml_markers = re.findall(r"###[A-Z0-9_-]+@@@", corpo)
        if lexml_markers:
            unicos = sorted(list(set(lexml_markers)))
            avisos_arquivo.append(f"Marcadores brutos de controle LexML/Senado detectados ({len(lexml_markers)}x): {unicos[:3]}")
            diagnostico["qualidade_corpo"]["marcadores_raspagem_lexml"].append({
                "arquivo": rel, "contagem": len(lexml_markers), "marcadores": unicos
            })

        # Tags HTML
        tags_encontradas = HTML_TAG_REGEX.findall(corpo)
        if tags_encontradas:
            tags_unicas = sorted(list(set(tags_encontradas)))
            erros_arquivo.append(f"HTML residual detectado ({len(tags_encontradas)} ocorrências): {tags_unicas[:5]}")
            diagnostico["qualidade_corpo"]["html_residual"].append({
                "arquivo": rel,
                "contagem": len(tags_encontradas),
                "tags": tags_unicas
            })

        # Mojibake / caracteres corrompidos
        if "\x00" in conteudo or "\ufffd" in conteudo:
            erros_arquivo.append("Caracteres nulos (\\x00) ou marcador de substituição Unicode (\\ufffd) detectados")
            diagnostico["qualidade_corpo"]["mojibake_e_caracteres_corrompidos"].append({
                "arquivo": rel, "tipo": "caractere_nulo_ou_ufffd"
            })
        
        mojibake_match = MOJIBAKE_REGEX.findall(conteudo)
        if mojibake_match:
            mojibakes = sorted(list(set(mojibake_match)))
            avisos_arquivo.append(f"Possível mojibake / encoding corrompido: {mojibakes[:5]}")
            diagnostico["qualidade_corpo"]["mojibake_e_caracteres_corrompidos"].append({
                "arquivo": rel, "tipo": "mojibake", "amostra": mojibakes
            })

        # HTML Entities
        entities = HTML_ENTITY_REGEX.findall(corpo)
        if entities:
            ent_unicas = sorted(list(set(entities)))
            avisos_arquivo.append(f"Entidades HTML não convertidas: {ent_unicas[:5]}")
            diagnostico["qualidade_corpo"]["html_entities_residuais"].append({
                "arquivo": rel, "contagem": len(entities), "entidades": ent_unicas
            })

        # Scraping junk (artefatos de interface de portais de prefeituras/tribunais)
        junk_patterns = [
            "Aguarde...", "Transparência São Paulo", "Consultar Processos",
            "Acessibilidade", "CASA CIVIL DO GABINETE DO PREFEITO", "Página principal",
            "Buscar no portal", "Voltar ao topo", "Imprimir esta página"
        ]
        junk_achado = [j for j in junk_patterns if j in corpo[:1500]]
        if junk_achado:
            erros_arquivo.append(f"Boilerplate de scraping residual detectado no cabeçalho textual: {junk_achado}")
            diagnostico["qualidade_corpo"]["scraping_boilerplate"].append({
                "arquivo": rel, "artefatos": junk_achado
            })

        # Tabelas Markdown quebradas (linhas com | sem separador |---| ou colunas desbalanceadas)
        linhas_tab = [l for l in corpo.splitlines() if "|" in l]
        if linhas_tab:
            tem_separador = any(re.match(r"^\s*\|?\s*:?-+:?\s*\|", l) for l in linhas_tab)
            if len(linhas_tab) >= 3 and not tem_separador:
                avisos_arquivo.append("Possível tabela Markdown quebrada (faltando separador |---|)")
                diagnostico["qualidade_corpo"]["tabelas_quebradas"].append({
                    "arquivo": rel, "motivo": "Linhas com pipes sem linha delimitadora de cabeçalho"
                })

        # Registro por arquivo
        diagnostico["detalhes_por_arquivo"][rel] = {
            "linhas": n_linhas,
            "caracteres": n_chars,
            "tipo": tipo_ato,
            "titulo": titulo_ato,
            "situacao": situacao,
            "erros": erros_arquivo,
            "avisos": avisos_arquivo,
            "conforme": len(erros_arquivo) == 0
        }

    # Análise de Duplicidades e Fatiamentos Globais
    diagnostico["duplicidade_e_fragmentacao"]["normas_fatiadas"]["PLP_68_2024"] = {
        "descricao": "PLP 68/2024 fragmentado artificialmente em 5 arquivos no acervo",
        "arquivos": sorted(list(set(plp68_files)))
    }

    # Duplicidades normativas (mesmo tipo, numero e ano)
    for k, v in normas_por_chave.items():
        if len(v) > 1:
            diagnostico["duplicidade_e_fragmentacao"]["duplicidades_normativas"][k] = v

    # Duplicidades exatas de título
    for k, v in normas_por_titulo.items():
        if len(v) > 1:
            diagnostico["duplicidade_e_fragmentacao"]["duplicidades_exatas"][k] = v

    # Totalizações e consolidação
    docs_com_erros = sum(1 for v in diagnostico["detalhes_por_arquivo"].values() if not v["conforme"])
    aprovados = total_docs - docs_com_erros
    diagnostico["resumo"]["documentos_com_inconformidades"] = docs_com_erros
    diagnostico["resumo"]["documentos_aprovados"] = aprovados
    taxa_conf = (aprovados / total_docs * 100) if total_docs > 0 else 0
    diagnostico["resumo"]["taxa_conformidade_schema"] = f"{taxa_conf:.2f}%"

    # Converter defaultdict e Counter para dict puro para serialização JSON
    def converter_json(obj):
        if isinstance(obj, (defaultdict, Counter)):
            return dict(obj)
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    caminho_out = RAIZ / "_auditoria" / "auditoria_integridade_total.json"
    caminho_out.parent.mkdir(parents=True, exist_ok=True)
    caminho_out.write_text(json.dumps(diagnostico, indent=2, ensure_ascii=False, default=converter_json), encoding="utf-8")
    print(f"[Auditor] Relatório gravado com sucesso em: {caminho_out}")

    # Atualizar falhas_auditoria.jsonl
    caminho_falhas = RAIZ / "_auditoria" / "falhas_auditoria.jsonl"
    with open(caminho_falhas, "w", encoding="utf-8") as f:
        for rel, d in sorted(diagnostico["detalhes_por_arquivo"].items()):
            if not d["conforme"] or d["avisos"]:
                reg = {
                    "arquivo": rel,
                    "erros": d["erros"],
                    "avisos": d["avisos"]
                }
                f.write(json.dumps(reg, ensure_ascii=False) + "\n")
    print(f"[Auditor] Arquivo de falhas gravado em: {caminho_falhas}")

    return diagnostico

if __name__ == "__main__":
    auditar_tudo()
