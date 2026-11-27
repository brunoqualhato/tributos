"""Lote: folha e previdência. INs RFB nº 2.289/2025 e 2.321/2026 (alteram a IN RFB 2.110/2022), Lei nº 15.371/2026
(licença-paternidade e salário-paternidade) e Decreto nº 13.054/2026 (altera o Regulamento da Previdência Social).
Especialistas: tributos_folha
As INs vêm do Sijut/RFB (visão compilada, com anexos em PDF e HTML quando existirem) e seguem
`reguladores/rfb/instrucoes-normativas/AAAA/`, caminho canônico da rotina periódica. A Lei e o Decreto vêm de
normas.leg.br (texto original).
Uso: python3 scripts/gerar_folha_previdencia_2026.py
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
RFB = "Secretaria Especial da Receita Federal do Brasil"
CONGRESSO = "Congresso Nacional / Presidência da República"
PRESIDENCIA = "Presidência da República"
TEMA_FOLHA = "Folha de Pagamento e Encargos"
IN_2110 = "reguladores/rfb/instrucoes-normativas/2022/ato-126687-2110-2022.md"
LEI_8212 = "federal/leis-ordinarias/previdencia-custeio/lei-8212-1991.md"
LEI_8213 = "federal/leis-ordinarias/previdencia-custeio/lei-8213-1991.md"
RPS = "federal/regulamentos/rps/decreto-3048-1999.md"
# (idAto, tipo, numero, data, orgao, tema, tributos, situacao, notas)
ATOS = [
    (147671, "Instrução Normativa", "2289", "2025-10-30", RFB, TEMA_FOLHA, ["INSS Patronal/Segurados"], "Em vigor",
     [f"Altera a IN RFB nº 2110/2022 (`{IN_2110}`), que dispõe sobre normas gerais de tributação previdenciária. "
      "O texto abaixo é o da própria alteração; a IN nº 2110/2022 do acervo é a versão compilada do Sijut."]),
    (150565, "Instrução Normativa", "2321", "2026-04-06", RFB, TEMA_FOLHA, ["INSS Patronal/Segurados"], "Em vigor",
     [f"Altera a IN RFB nº 2110/2022 (`{IN_2110}`), que dispõe sobre normas gerais de tributação previdenciária. "
      "O texto abaixo é o da própria alteração; a IN nº 2110/2022 do acervo é a versão compilada do Sijut."]),
]
# (urn, caminho, tipo, numero, data, titulo, orgao, tema, tributos, notas)
NORMAS = [
    ("urn:lex:br:federal:lei:2026-03-31;15371",
     "federal/leis-ordinarias/previdencia-custeio/lei-15371-2026-licenca-e-salario-paternidade.md",
     "Lei Ordinária", "15371", "2026-03-31",
     "Lei nº 15.371, de 31 de março de 2026 (Licença-paternidade e salário-paternidade; altera as Leis 8.212/1991 e 8.213/1991)",
     CONGRESSO, TEMA_FOLHA, ["INSS Patronal/Segurados"],
     [f"Altera a Lei nº 8.212/1991 (`{LEI_8212}`) e a Lei nº 8.213/1991 (`{LEI_8213}`), além da CLT e da Lei nº 11.770/2008. "
      "O texto abaixo é o original da Lei nº 15.371/2026, sem consolidação nas leis alteradas."]),
    ("urn:lex:br:federal:decreto:2026-07-03;13054",
     "federal/regulamentos/rps/decreto-13054-2026-altera-rps-segurado-especial-cooperativas.md",
     "Decreto", "13054", "2026-07-03",
     "Decreto nº 13.054, de 3 de julho de 2026 (Altera o Regulamento da Previdência Social (segurado especial em cooperativas))",
     PRESIDENCIA, TEMA_FOLHA, ["INSS Patronal/Segurados"],
     [f"Altera o Regulamento da Previdência Social, Decreto nº 3.048/1999 (`{RPS}`). O documento reproduz o texto da alteração, "
      "não o regulamento consolidado."]),
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
        print(f"[Folha/previdência 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes) "
              f"pdf={dados['_anexos_pdf']} omitidos={dados['_anexos_omitidos']}")
    for urn, destino_rel, tipo, numero, data, titulo, orgao, tema, tributos, notas in NORMAS:
        doc = co.documento_lexml(urn, tipo, numero, data, titulo, orgao, tema, tributos, notas=notas)
        destino = co.gravar(destino_rel, doc)
        print(f"[Folha/previdência 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes)")
