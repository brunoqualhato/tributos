"""Lote: atos da RFB e da PGFN que regulamentam as LC 225/2026 (conformidade), LC 224/2025 e LC 235/2026.
Especialistas: tributos_servicos e tributos_produtos

Todos os documentos vêm do Sijut/RFB (visão compilada, com anexos em PDF e HTML quando existirem).
INs seguem `reguladores/rfb/instrucoes-normativas/AAAA/` e a portaria conjunta
`reguladores/rfb/outros-atos/AAAA/`, caminhos canônicos da rotina periódica.

Uso: python3 scripts/gerar_conformidade_beneficios_rfb_2026.py
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co

RFB = "Secretaria Especial da Receita Federal do Brasil"
RFB_PGFN = "Procuradoria-Geral da Fazenda Nacional / Secretaria Especial da Receita Federal do Brasil"
TEMA_PROC = "Processo Tributário e Fiscal"
TEMA_BEN = "Benefícios e Incentivos Fiscais"
CONF = ["Programas de Conformidade", "Direitos do Contribuinte"]
BENEF = ["IRPJ", "CSLL", "PIS/Pasep", "Cofins", "IPI", "Imposto de Importação"]

# (idAto, tipo, numero, data, orgao, tema, tributos, situacao, notas)
ATOS = [
    (148173, "Instrução Normativa", "2295", "2025-12-03", RFB, TEMA_PROC, CONF + ["Confia"],
     "Em vigor (alterada pelas INs RFB nº 2317 e nº 2328/2026)",
     ["Programa de Conformidade Cooperativa Fiscal (Confia). Alterada pelas INs RFB nº 2317/2026 (`ato-150220-2317-2026.md`) e "
      "nº 2328/2026 (`ato-151846-2328-2026.md`)."]),
    (150220, "Instrução Normativa", "2317", "2026-03-25", RFB, TEMA_PROC, CONF + ["Confia"], "Em vigor (alterada pela IN RFB nº 2328/2026)",
     ["Altera a IN RFB nº 2295/2025 (`ato-148173-2295-2025.md`)."]),
    (151846, "Instrução Normativa", "2328", "2026-06-17", RFB, TEMA_PROC, CONF + ["Confia"], "Em vigor",
     ["Altera a IN RFB nº 2295/2025 (`ato-148173-2295-2025.md`)."]),
    (150221, "Instrução Normativa", "2316", "2026-03-25", RFB, TEMA_PROC, CONF + ["Sintonia"],
     "Em vigor (alterada pela IN RFB nº 2339/2026)",
     ["Programa de Estímulo à Conformidade Tributária (Sintonia), previsto na LC nº 225/2026 "
      "(`federal/leis-complementares/lei-complementar-225-2026-codigo-defesa-contribuinte.md`). Alterada pela IN RFB nº 2339/2026 "
      "(`ato-153174-2339-2026.md`)."]),
    (153174, "Instrução Normativa", "2339", "2026-08-21", RFB, TEMA_PROC, CONF + ["Sintonia"], "Em vigor",
     ["Altera a IN RFB nº 2316/2026 (`ato-150221-2316-2026.md`)."]),
    (150228, "Instrução Normativa", "2318", "2026-03-26", RFB, TEMA_PROC, CONF + ["Operador Econômico Autorizado"], "Em vigor",
     ["Programa Brasileiro de Operador Econômico Autorizado (OEA), um dos programas de conformidade da LC nº 225/2026."]),
    (150207, "Portaria Conjunta", "6", "2026-03-26", RFB_PGFN, TEMA_PROC, ["Devedor Contumaz", "Direitos do Contribuinte"], "Em vigor",
     ["Trata do devedor contumaz de que cuida a LC nº 225/2026 (`federal/leis-complementares/lei-complementar-225-2026-codigo-defesa-contribuinte.md`). "
      "A retificação de 1º/04/2026 já consta do texto compilado."]),
    (148959, "Instrução Normativa", "2306", "2026-01-22", RFB, TEMA_BEN, BENEF, "Em vigor",
     ["Altera a IN RFB nº 2305/2025 (`ato-148694-2305-2025.md`), que regulamenta a redução linear de benefícios da LC nº 224/2025."]),
    (149398, "Instrução Normativa", "2307", "2026-02-20", RFB, TEMA_BEN, BENEF, "Em vigor",
     ["Substitui o Anexo Único da IN RFB nº 2305/2025 (`ato-148694-2305-2025.md`). O documento da IN nº 2305/2025 no acervo traz "
      "apenas o título do Anexo Único, sem o conteúdo; a lista vigente dos gastos tributários não alcançados pela redução linear está neste documento."]),
    (153636, "Instrução Normativa", "2344", "2026-09-18", RFB, TEMA_BEN, ["PIS/Pasep", "Cofins"], "Em vigor",
     ["Regulamenta o art. 5º da LC nº 235/2026 (`federal/beneficios-tributarios/lei-complementar-235-2026-renuncias-choque-energia.md`): "
      "uso de saldos credores de PIS/Pasep e Cofins na compensação com débitos próprios."]),
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
        print(f"[Conformidade/benefícios 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes) "
              f"pdf={dados['_anexos_pdf']} omitidos={dados['_anexos_omitidos']}")
