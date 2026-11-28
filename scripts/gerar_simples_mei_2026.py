"""Lote: Simples Nacional e MEI (2025-2026): LC 216/2025, LC 238/2026, Resoluções CGSN e Portaria Conjunta RFB/PGFN.
Especialistas: tributos_reforma_transicao e tributos_servicos
Documentos:
- Resoluções CGSN nº 182 e 183/2025 e nº 191, 195 e 198/2026 (Sijut/RFB, texto da alteração da Resolução CGSN nº 140/2018);
- Portaria Conjunta RFB/PGFN nº 740/2026 (remissão de créditos de MEI da LC 238/2026), Sijut/RFB;
- Lei Complementar nº 216/2025 (Programa Acredita Exportação) e Lei Complementar nº 238/2026 (limite do MEI e remissão),
  texto original (normas.leg.br).
Uso: python3 scripts/gerar_simples_mei_2026.py
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
CONGRESSO = "Congresso Nacional / Presidência da República"
ORGAO_CGSN = "Comitê Gestor do Simples Nacional (CGSN)"
ORGAO_RFB_PGFN = "Secretaria Especial da Receita Federal do Brasil / Procuradoria-Geral da Fazenda Nacional"
RES_140 = "federal/leis-complementares/simples/resolucao-cgsn-140-2018-simples-nacional.md"
LC_123 = "federal/leis-complementares/simples/lei-123-2006.md"
LC_216 = "federal/leis-complementares/simples/lei-complementar-216-2025-programa-acredita-exportacao.md"
LC_238 = "federal/leis-complementares/simples/lei-complementar-238-2026-mei-limite-e-remissao.md"
NAO_CONSOLIDADA = "Este documento traz apenas o texto da Resolução nº {n}, não a Resolução nº 140 consolidada."
def caminho_ato(id_ato: int, numero: str, data: str) -> str:
    return f"reguladores/rfb/outros-atos/{data[:4]}/ato-{id_ato}-{numero}-{data[:4]}.md"
# (idAto, tipo, numero, data da epígrafe, órgão, tema, tributos, notas)
ATOS_SIJUT = [
    (147034, "Resolução", "183", "2025-09-26", ORGAO_CGSN, "Reforma Tributária e Transição",
     ["Simples Nacional", "IBS", "CBS"],
     [f"Altera a Resolução CGSN nº 140/2018 (`{RES_140}`). " + NAO_CONSOLIDADA.format(n="183/2025") +
      " Fundamenta-se nos arts. 516 e 544, caput, inciso II, da Lei Complementar nº 214/2025 (`reforma-tributaria/lei-complementar-214-2025.md`) "
      f"e no art. 2º da Lei Complementar nº 216/2025 (`{LC_216}`). O art. 3º produz efeitos a partir de 1º de janeiro de 2026 (art. 7º, inciso I)."]),
    (146769, "Resolução", "182", "2025-09-26", ORGAO_CGSN, "Benefícios e Incentivos Fiscais",
     ["Simples Nacional", "MEI"],
     [f"Altera a tabela A do Anexo XI (ocupações permitidas ao MEI) da Resolução CGSN nº 140/2018 (`{RES_140}`). "
      + NAO_CONSOLIDADA.format(n="182/2025")]),
    (152781, "Resolução", "191", "2026-08-04", ORGAO_CGSN, "Reforma Tributária e Transição",
     ["Simples Nacional", "ISSQN"],
     [f"Altera a Resolução CGSN nº 140/2018 (`{RES_140}`) para tornar obrigatória a NFS-e de padrão nacional para as ME e EPP optantes pelo Simples Nacional. "
      + NAO_CONSOLIDADA.format(n="191/2026") +
      " Produz efeitos a partir de 1º de novembro de 2026 quanto ao art. 1º (art. 3º) e revoga a Resolução CGSN nº 189/2026, que não consta do acervo."]),
    (154194, "Resolução", "195", "2026-10-21", ORGAO_CGSN, "Reforma Tributária e Transição",
     ["Simples Nacional", "MEI"],
     [f"Altera a Resolução CGSN nº 140/2018 (`{RES_140}`) para permitir que a DASN-Simei seja usada como documento fiscal eletrônico do MEI nas vendas e serviços a consumidor final pessoa física. "
      + NAO_CONSOLIDADA.format(n="195/2026") +
      " Produz efeitos a partir de 1º de janeiro de 2027 (art. 2º)."]),
    (154765, "Resolução", "198", "2026-11-16", ORGAO_CGSN, "Benefícios e Incentivos Fiscais",
     ["Simples Nacional", "MEI"],
     [f"Altera a Resolução CGSN nº 140/2018 (`{RES_140}`) para ajustar o limite de receita bruta e o número de empregados do MEI conforme a Lei Complementar nº 238/2026 "
      f"(`{LC_238}`). " + NAO_CONSOLIDADA.format(n="198/2026") +
      " O limite anual de R$ 110.000,00 vale para o ano-calendário de 2027 (art. 2º da LC 238/2026). Produz efeitos a partir de 1º de janeiro de 2027 (art. 2º). "
      "A data do ato é a da epígrafe (16/11/2026); a publicação no DOU ocorreu em 25/11/2026."]),
    (154339, "Portaria Conjunta", "740", "2026-10-22", ORGAO_RFB_PGFN, "Benefícios e Incentivos Fiscais",
     ["Simples Nacional", "MEI", "INSS"],
     [f"Disciplina a remissão de créditos de titularidade da União de responsabilidade de MEI, prevista nos arts. 5º a 7º da Lei Complementar nº 238/2026 (`{LC_238}`). "
      "Entra em vigor em 1º de janeiro de 2027 (art. 13); na data da consulta o ato estava publicado, sem produzir efeitos."]),
]
# (urn, tipo, numero, data da epígrafe, titulo, caminho, tributos, notas)
NORMAS_LEXML = [
    ("urn:lex:br:federal:lei.complementar:2025-07-28;216", "Lei Complementar", "216", "2025-07-28",
     "Lei Complementar nº 216, de 28 de julho de 2025 (Programa Acredita Exportação; altera a LC 123/2006)",
     LC_216, ["Simples Nacional", "Imposto de Importação", "PIS/Pasep", "Cofins"],
     [f"Altera a Lei Complementar nº 123/2006 (`{LC_123}`); o documento da LC 123 no acervo não incorpora essa alteração. "
      "É citada pela Resolução CGSN nº 183/2025 (`reguladores/rfb/outros-atos/2025/ato-147034-183-2025.md`), que a aplica à Resolução CGSN nº 140/2018."]),
    ("urn:lex:br:federal:lei.complementar:2026-10-21;238", "Lei Complementar", "238", "2026-10-21",
     "Lei Complementar nº 238, de 21 de outubro de 2026 (Limite de receita e de empregados do MEI e remissão de créditos da União)",
     LC_238, ["Simples Nacional", "MEI", "INSS"],
     [f"Altera a Lei Complementar nº 123/2006 (`{LC_123}`); o documento da LC 123 no acervo não incorpora essa alteração. "
      "Produz efeitos a partir de 1º de janeiro de 2027 e, quanto às alterações do art. 18-A, §§ 1º e 2º, da LC 123, a partir de 1º de janeiro de 2028 (art. 10); "
      "para 2027 o limite anual do MEI é de R$ 110.000,00 (art. 2º). "
      "Regulamentada pela Resolução CGSN nº 198/2026 (`reguladores/rfb/outros-atos/2026/ato-154765-198-2026.md`) e pela Portaria Conjunta RFB/PGFN nº 740/2026 "
      "(`reguladores/rfb/outros-atos/2026/ato-154339-740-2026.md`)."]),
]
def documentos() -> list[tuple[str, str]]:
    docs = []
    for id_ato, tipo, numero, data, orgao, tema, tributos, notas in ATOS_SIJUT:
        doc, _ = co.documento_sijut(id_ato, None, tipo, numero, data, orgao, tributos, tema=tema, notas_extra=notas)
        docs.append((caminho_ato(id_ato, numero, data), doc))
    for urn, tipo, numero, data, titulo, destino, tributos, notas in NORMAS_LEXML:
        doc = co.documento_lexml(urn, tipo, numero, data, titulo, CONGRESSO, "Benefícios e Incentivos Fiscais", tributos, "Em vigor", notas)
        docs.append((destino, doc))
    return docs
if __name__ == "__main__":
    for destino, conteudo in documentos():
        gravado = co.gravar(destino, conteudo)
        print(f"[Simples/MEI 2026] {gravado.relative_to(co.RAIZ)} ({gravado.stat().st_size} bytes)")
