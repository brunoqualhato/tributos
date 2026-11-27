"""Lote: CBS sobre combustíveis, Imposto Seletivo de 2027 e competências do CGIBS (2026).
Especialistas: tributos_reforma_transicao e tributos_produtos
Documentos:
- Decreto nº 13.133/2026 (delega ao Ministro da Fazenda a divulgação das alíquotas da CBS sobre combustíveis),
  texto original (normas.leg.br);
- Medida Provisória nº 1.399/2026 (alíquotas e normas do Imposto Seletivo para 2027), texto original (normas.leg.br);
- Resoluções CGIBS nº 16 e 17/2026 (competências do Presidente do Conselho Superior e da Diretoria Executiva),
  PDFs oficiais do portal do CGIBS.
Uso: python3 scripts/gerar_reforma_cbs_is_cgibs_2026.py
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
import gerar_reforma_cgibs_cgsn_2026 as cgibs
PRESIDENCIA = "Presidência da República"
TEMA = "Reforma Tributária e Transição"
def caminho(subpasta: str, arquivo: str) -> str:
    return f"reforma-tributaria/{subpasta}/{arquivo}" if subpasta else f"reforma-tributaria/{arquivo}"
# (urn, caminho, tipo, numero, data da epígrafe, titulo, tributos, situacao, notas)
NORMAS_LEXML = [
    ("urn:lex:br:federal:decreto:2026-10-09;13133",
     caminho("regulamentos", "decreto-13133-2026-delega-aliquotas-cbs-combustiveis.md"),
     "Decreto", "13133", "2026-10-09",
     "Decreto nº 13.133, de 9 de outubro de 2026 (Delega ao Ministro da Fazenda a divulgação das alíquotas da CBS sobre combustíveis)",
     ["CBS"], "Em vigor",
     ["Altera o art. 471 (inciso III) e o art. 476 e revoga o art. 477 do Regulamento da CBS "
      "(`reforma-tributaria/regulamentos/decreto-12955-2026-regulamento-cbs.md`, Decreto nº 12.955/2026); "
      "o documento do Regulamento no acervo traz o texto original, sem essas alterações. "
      "A competência delegada foi exercida pela Portaria MF nº 3.074, de 9 de outubro de 2026 "
      "(`reguladores/rfb/outros-atos/2026/ato-154060-3074-2026.md`), que cita este Decreto. "
      "O Decreto se apoia nos arts. 174 e 175 da Lei Complementar nº 214/2025 "
      "(`reforma-tributaria/lei-complementar-214-2025.md`)."]),
    ("urn:lex:br:federal:medida.provisoria:2026-11-04;1399",
     caminho("", "medida-provisoria-1399-2026-aliquotas-imposto-seletivo-2027.md"),
     "Medida Provisória", "1399", "2026-11-04",
     "Medida Provisória nº 1.399, de 4 de novembro de 2026 (Alíquotas e normas do Imposto Seletivo para 2027)",
     ["Imposto Seletivo", "CBS", "IPI"], "Em vigor (medida provisória; conversão em lei pendente)",
     ["Medida provisória em vigor desde a publicação, com efeitos a partir de 2 de fevereiro de 2027 (art. 19). "
      "Na consulta ao normas.leg.br não havia lei de conversão, rejeição ou revogação registrada; a situação deve ser "
      "reavaliada quando o Congresso Nacional deliberar. O art. 15 prevê projeto de lei com as alíquotas do Imposto "
      "Seletivo a partir de 1º de janeiro de 2028, e a medida provisória permanece em vigor até o início da produção "
      "de efeitos dessa lei (art. 19). Regulamenta o Imposto Seletivo da Lei Complementar nº 214/2025 "
      "(`reforma-tributaria/lei-complementar-214-2025.md`) e adota a TIPI aprovada pelo Decreto nº 11.158/2022 "
      "(`federal/regulamentos/ripi/decreto-11158-2022-tipi.md`). "
      "Os Anexos I a V citados no texto (alíquota-base e critérios de sustentabilidade dos veículos e fatores de conversão) "
      "não constam do texto estruturado disponibilizado em normas.leg.br e não foram incorporados; para esses anexos, "
      "consultar a publicação no DOU."]),
]
# (chave do cache, caminho do PDF, caminho do documento, titulo, numero, data, tributos, ementa, situacao, notas)
CGIBS_RES = [
    ("resolucao-cgibs-16-2026", "202607/29175824-doc-20260729-wa0035-260729-175811.pdf",
     caminho("cgibs", "resolucao-cgibs-16-2026-competencia-presidente-obrigatoriedade-dfe.md"),
     "Resolução CGIBS nº 16, de 29 de julho de 2026 (Competência do Presidente do Conselho Superior para o ato conjunto de obrigatoriedade dos DF-e)",
     "16", "2026-07-29", ["IBS"],
     "Atribui competência provisória ao Presidente do Conselho Superior para decidir sobre o teor e os limites do ato conjunto da RFB e do CGIBS relativo à obrigatoriedade de emissão de documentos fiscais eletrônicos.",
     "Em vigor",
     ["Trata do ato conjunto referido no art. 112 do Regulamento do IBS (`reforma-tributaria/regulamentos/resolucao-cgibs-6-2026-regulamento-ibs.md`). "
      "As datas de início da obrigatoriedade fixadas nesse ato não podem passar de 1º de janeiro de 2027 (art. 1º, parágrafo único). "
      "O ato conjunto de obrigatoriedade dos documentos fiscais é o Ato Conjunto RFB/CGIBS nº 4, de 30 de julho de 2026, "
      "alterado pelo Ato Conjunto nº 7/2026 (`reguladores/rfb/outros-atos/2026/ato-152616-4-2026.md`)."]),
    ("resolucao-cgibs-17-2026", "202607/30184100-doc-20260730-wa0034-260730-183903.pdf",
     caminho("cgibs", "resolucao-cgibs-17-2026-competencia-direx-atos-tecnicos.md"),
     "Resolução CGIBS nº 17, de 30 de julho de 2026 (Competência da Diretoria Executiva para atos técnicos)",
     "17", "2026-07-30", ["IBS"],
     "Atribui competências à Diretoria Executiva e às suas Diretorias para a aprovação de atos técnicos de natureza operacional relativos aos sistemas e às plataformas digitais administrados pelo Comitê Gestor do IBS.",
     "Em vigor (efeitos até a entrada em vigor do regimento interno estrutural)",
     ["O art. 6º limita os efeitos desta Resolução à entrada em vigor do regimento interno estrutural do CGIBS, que deve dispor sobre o tema. "
      "É o fundamento de competência citado nos Atos Técnicos Conjuntos RFB/CGIBS, por exemplo o Ato Técnico Conjunto RFB/CGIBS nº 1/2026 "
      "(`reguladores/rfb/outros-atos/2026/ato-152654-1-2026.md`), e a Resolução CGIBS nº 20/2026 "
      "(`reforma-tributaria/cgibs/resolucao-cgibs-20-2026-tipologia-dos-atos.md`) remete a ela. "
      "A epígrafe do PDF omite a preposição \"de\" antes do dia (\"Nº 17, 30 DE JULHO DE 2026\"). "
      "A extração de texto do PDF embaralhava a ordem das palavras do inciso VI do art. 2º; "
      "a ordem foi restabelecida conforme a imagem do PDF (\"especificações de APIs, protocolos, interfaces e padrões de interoperabilidade\")."]),
]
# Correções de ordem de palavras da extração do PDF, por chave: (trecho extraído, trecho conforme o PDF)
AJUSTES_PDF = {
    "resolucao-cgibs-17-2026": [
        ("VI – especificações interoperabilidade; de APIs, protocolos, interfaces e padrões de",
         "VI – especificações de APIs, protocolos, interfaces e padrões de interoperabilidade;"),
    ],
}
def documento_resolucao(chave, pdf_rel, destino, titulo, numero, data, tributos, ementa, situacao, notas):
    _, doc = cgibs.documento_cgibs(chave, pdf_rel, destino, titulo, numero, data, tributos, ementa, situacao, notas)
    for errado, certo in AJUSTES_PDF.get(chave, []):
        if doc.count(errado) != 1:
            raise RuntimeError(f"Trecho a ajustar não encontrado em {chave}: {errado!r}")
        doc = doc.replace(errado, certo)
    return destino, doc
if __name__ == "__main__":
    docs = []
    for urn, destino, tipo, numero, data, titulo, tributos, situacao, notas in NORMAS_LEXML:
        docs.append((destino, co.documento_lexml(urn, tipo, numero, data, titulo, PRESIDENCIA, TEMA, tributos, situacao, notas)))
    docs += [documento_resolucao(*r) for r in CGIBS_RES]
    for destino, conteudo in docs:
        gravado = co.gravar(destino, conteudo)
        print(f"[CBS/IS/CGIBS 2026] {gravado.relative_to(co.RAIZ)} ({gravado.stat().st_size} bytes)")
