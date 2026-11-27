"""Lote: IRPJ e CSLL. Alterações da IN RFB 1.700/2017 e da IN RFB 2.228/2024 (regras GloBE), ADIs sobre JCP em convenções
e tributo pago no exterior, e Lei 15.525/2026 (CSLL e adicional de IRPJ das resseguradoras locais).
Especialistas: tributos_dividendos
Os atos da RFB vêm do Sijut/RFB (visão compilada, com anexos em PDF e HTML quando existirem). INs seguem
`reguladores/rfb/instrucoes-normativas/AAAA/` e os Atos Declaratórios Interpretativos `reguladores/rfb/outros-atos/AAAA/`,
caminhos canônicos da rotina periódica. A Lei nº 15.525/2026 vem de normas.leg.br (texto original).
Uso: python3 scripts/gerar_irpj_csll_2026.py
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
RFB = "Secretaria Especial da Receita Federal do Brasil"
CONGRESSO = "Congresso Nacional / Presidência da República"
TEMA = "Dividendos e Renda do Capital"
IRPJ_CSLL = ["IRPJ", "CSLL"]
IN_1700 = "reguladores/rfb/instrucoes-normativas/2017/ato-81268-1700-2017.md"
IN_2228 = "reguladores/rfb/instrucoes-normativas/2024/ato-140884-2228-2024.md"
IN_2237 = "reguladores/rfb/instrucoes-normativas/2024/ato-141910-2237-2024.md"
# (idAto, tipo, numero, data, orgao, tema, tributos, situacao, notas)
ATOS = [
    (148102, "Instrução Normativa", "2296", "2025-12-03", RFB, TEMA, IRPJ_CSLL, "Em vigor",
     [f"Altera a IN RFB nº 1700/2017 (`{IN_1700}`), em matéria de perdas no recebimento de créditos de instituições financeiras."]),
    (146523, "Instrução Normativa", "2281", "2025-09-15", RFB, TEMA, IRPJ_CSLL, "Em vigor",
     [f"Altera a IN RFB nº 1700/2017 (`{IN_1700}`), em matéria de perdas no recebimento de créditos."]),
    (150037, "Instrução Normativa", "2315", "2026-03-18", RFB, TEMA, IRPJ_CSLL, "Em vigor",
     [f"Altera a IN RFB nº 1700/2017 (`{IN_1700}`), em matéria de alíquotas da CSLL a partir de 01/04/2026."]),
    (153616, "Instrução Normativa", "2343", "2026-09-17", RFB, TEMA, IRPJ_CSLL, "Em vigor",
     [f"Altera a IN RFB nº 1700/2017 (`{IN_1700}`), em matéria de serviços hospitalares e perdas em créditos."]),
    (143464, "Instrução Normativa", "2259", "2025-03-24", RFB, TEMA, ["CSLL"], "Em vigor",
     [f"Altera a IN RFB nº 2228/2024 (`{IN_2228}`), que trata da CSLL e das regras GloBE (Lei nº 15.079/2024, "
      "`federal/leis-ordinarias/irpj-csll/lei-15079-2024-adicional-csll-pilar-2-ocde-qdmtt.md`)."]),
    (150345, "Instrução Normativa", "2319", "2026-03-30", RFB, TEMA, ["CSLL"], "Em vigor",
     [f"Altera a IN RFB nº 2228/2024 (`{IN_2228}`) e a IN RFB nº 2237/2024 (`{IN_2237}`)."]),
    (151902, "Instrução Normativa", "2329", "2026-06-18", RFB, TEMA, ["CSLL"], "Em vigor",
     [f"Altera a IN RFB nº 2228/2024 (`{IN_2228}`)."]),
    (153622, "Instrução Normativa", "2342", "2026-09-15", RFB, TEMA, ["CSLL"], "Em vigor",
     [f"Altera a IN RFB nº 2228/2024 (`{IN_2228}`)."]),
    (154660, "Instrução Normativa", "2351", "2026-11-17", RFB, TEMA, ["CSLL"], "Em vigor",
     [f"Altera a IN RFB nº 2228/2024 (`{IN_2228}`). A data do ato é a da epígrafe (17/11/2026)."]),
    (148965, "Ato Declaratório Interpretativo", "1", "2026-01-22", RFB, TEMA, IRPJ_CSLL, "Em vigor",
     ["Trata da dedução, na apuração do IRPJ e da CSLL, do tributo pago no exterior por controlada ou coligada."]),
    (149849, "Ato Declaratório Interpretativo", "3", "2026-03-09", RFB, TEMA, ["IRRF", "JCP"], "Em vigor",
     ["Trata dos juros sobre o capital próprio (JCP) na convenção para evitar a dupla tributação entre Brasil e Espanha."]),
    (150769, "Ato Declaratório Interpretativo", "5", "2026-04-22", RFB, TEMA, ["IRRF", "JCP"], "Em vigor",
     ["Trata dos juros sobre o capital próprio (JCP) na convenção para evitar a dupla tributação entre Brasil e Países Baixos."]),
]
# (urn, caminho, tipo, numero, data, titulo, orgao, tema, tributos, notas)
NORMAS = [
    ("urn:lex:br:federal:lei:2026-09-28;15525",
     "federal/leis-ordinarias/irpj-csll/lei-15525-2026-csll-irpj-resseguradoras-locais.md",
     "Lei Ordinária", "15525", "2026-09-28",
     "Lei nº 15.525, de 28 de setembro de 2026 (CSLL e adicional de IRPJ das resseguradoras locais)",
     CONGRESSO, TEMA, IRPJ_CSLL,
     ["Altera as Leis nº 7.689/1988 (`federal/leis-ordinarias/irpj-csll/lei-7689-1988.md`), nº 9.249/1995 "
      "(`federal/leis-ordinarias/dividendos-jcp/lei-9249-1995.md`) e nº 9.430/1996 (`federal/leis-ordinarias/irpj-csll/lei-9430-1996.md`). "
      "Relaciona-se à desoneração tratada na LC nº 237/2026 (`federal/beneficios-tributarios/lei-complementar-237-2026-altera-lc-229.md`)."]),
]
def caminho(id_ato: int, tipo: str, numero: str, data: str) -> str:
    pasta = "instrucoes-normativas" if tipo == "Instrução Normativa" else "outros-atos"
    ano = data[:4]
    return f"reguladores/rfb/{pasta}/{ano}/ato-{id_ato}-{numero}-{ano}.md"
if __name__ == "__main__":
    for id_ato, tipo, numero, data, orgao, tema, tributos, situacao, notas in ATOS:
        doc, dados = co.documento_sijut(id_ato, None, tipo, numero, data, orgao, tributos, tema=tema,
                                        notas_extra=notas, situacao=situacao)
        destino = co.gravar(caminho(id_ato, tipo, numero, data), doc)
        print(f"[IRPJ/CSLL 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes) "
              f"pdf={dados['_anexos_pdf']} omitidos={dados['_anexos_omitidos']}")
    for urn, destino_rel, tipo, numero, data, titulo, orgao, tema, tributos, notas in NORMAS:
        doc = co.documento_lexml(urn, tipo, numero, data, titulo, orgao, tema, tributos, notas=notas)
        destino = co.gravar(destino_rel, doc)
        print(f"[IRPJ/CSLL 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes)")
