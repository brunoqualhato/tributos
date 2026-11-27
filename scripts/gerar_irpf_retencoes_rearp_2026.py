"""Lote: IRPF, retenções na fonte e Rearp. Leis nº 15.191/2025 (tabela progressiva mensal do IRPF) e nº 15.265/2025
(Rearp, empréstimo de títulos e hedge) e INs RFB nº 2.253, 2.257, 2.265, 2.301/2025 e 2.331/2026.
Especialistas: tributos_dividendos, tributos_folha, tributos_servicos
Os atos da RFB vêm do Sijut/RFB (visão compilada, com anexos em PDF e HTML quando existirem) e seguem
`reguladores/rfb/instrucoes-normativas/AAAA/`, caminho canônico da rotina periódica. As Leis vêm de normas.leg.br
(texto original).
Uso: python3 scripts/gerar_irpf_retencoes_rearp_2026.py
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
RFB = "Secretaria Especial da Receita Federal do Brasil"
CONGRESSO = "Congresso Nacional / Presidência da República"
TEMA_RETENCOES = "Serviços e Retenções"
TEMA_CAPITAL = "Dividendos e Renda do Capital"
TEMA_FOLHA = "Folha de Pagamento e Encargos"
IN_1234 = "reguladores/rfb/instrucoes-normativas/2012/ato-37200-1234-2012.md"
IN_2166 = "reguladores/rfb/instrucoes-normativas/2023/ato-135339-2166-2023.md"
LEI_14754 = "federal/leis-ordinarias/offshores/lei-14754-2023.md"
LEI_15265 = "federal/leis-ordinarias/offshores/lei-15265-2025-rearp-emprestimo-titulos-hedge.md"
LEI_11482 = "federal/leis-ordinarias/irrf-folha-plr/lei-11482-2007-tabela-progressiva-irpf.md"
# (idAto, tipo, numero, data, orgao, tema, tributos, situacao, notas)
ATOS = [
    (152155, "Instrução Normativa", "2331", "2026-06-23", RFB, TEMA_RETENCOES, ["IRRF", "IRPF", "IRPJ"], "Em vigor",
     ["Trata do imposto sobre a renda retido na fonte (IRRF) incidente sobre comissões e remunerações pagas a plataformas digitais."]),
    (143374, "Instrução Normativa", "2257", "2025-03-18", RFB, TEMA_RETENCOES, ["IRRF", "IRPF", "IRPJ"], "Em vigor",
     [f"Altera a IN RFB nº 1234/2012 (`{IN_1234}`), em matéria de aluguel pago a fundo de investimento imobiliário (FII)."]),
    (144202, "Instrução Normativa", "2265", "2025-05-09", RFB, TEMA_CAPITAL, ["IRPF", "IRPJ", "IRRF"], "Em vigor",
     ["Exclui os Emirados Árabes Unidos e o regime austríaco das listas de jurisdições com tributação favorecida e de regimes "
      "fiscais privilegiados. Altera a IN RFB nº 1037/2010, que não consta do acervo: o texto compilado do ato permite a leitura "
      "isolada, mas a consulta à IN RFB nº 1037/2010 completa as listas."]),
    (143007, "Instrução Normativa", "2253", "2025-02-21", RFB, TEMA_CAPITAL, ["IRPF", "IRPJ", "IRRF"], "Em vigor",
     [f"Altera a IN RFB nº 2166/2023 (`{IN_2166}`), que dispõe sobre o imposto sobre a renda em fundos de investimento "
      f"(Lei nº 14.754/2023, `{LEI_14754}`)."]),
    (148510, "Instrução Normativa", "2301", "2025-12-23", RFB, TEMA_CAPITAL, ["IRPF", "IRPJ"], "Em vigor",
     [f"Regulamenta o Regime Especial de Regularização Cambial e Tributária (Rearp Regularização) da Lei nº 15.265/2025 "
      f"(`{LEI_15265}`)."]),
]
# (urn, caminho, tipo, numero, data, titulo, orgao, tema, tributos, notas)
NORMAS = [
    ("urn:lex:br:federal:lei:2025-08-11;15191",
     "federal/leis-ordinarias/irrf-folha-plr/lei-15191-2025-tabela-progressiva-irpf-mensal.md",
     "Lei Ordinária", "15191", "2025-08-11",
     "Lei nº 15.191, de 11 de agosto de 2025 (Tabela progressiva mensal do IRPF; altera a Lei 11.482/2007)",
     CONGRESSO, TEMA_FOLHA, ["IRPF", "IRRF"],
     [f"Altera a Lei nº 11.482/2007 (`{LEI_11482}`) e revoga a Medida Provisória nº 1.294/2025. "
      "As tabelas foram convertidas para Markdown conforme o texto original."]),
    ("urn:lex:br:federal:lei:2025-11-21;15265",
     "federal/leis-ordinarias/offshores/lei-15265-2025-rearp-emprestimo-titulos-hedge.md",
     "Lei Ordinária", "15265", "2025-11-21",
     "Lei nº 15.265, de 21 de novembro de 2025 (Rearp, empréstimo de títulos e hedge)",
     CONGRESSO, TEMA_CAPITAL, ["IRPF", "IRPJ", "IRRF"],
     ["Regulamentada pela IN RFB nº 2301/2025 (`reguladores/rfb/instrucoes-normativas/2025/ato-148510-2301-2025.md`). "
      f"Relaciona-se à Lei nº 14.754/2023 (`{LEI_14754}`)."]),
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
        print(f"[IRPF/Rearp 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes) "
              f"pdf={dados['_anexos_pdf']} omitidos={dados['_anexos_omitidos']}")
    for urn, destino_rel, tipo, numero, data, titulo, orgao, tema, tributos, notas in NORMAS:
        doc = co.documento_lexml(urn, tipo, numero, data, titulo, orgao, tema, tributos, notas=notas)
        destino = co.gravar(destino_rel, doc)
        print(f"[IRPF/Rearp 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes)")
