"""Lote: Atos Conjuntos RFB/CGIBS e atos da RFB/MF sobre a CBS (2025-2026).
Especialista: tributos_reforma_transicao

Todos os documentos vêm do Sijut/RFB (visão compilada) e seguem o caminho canônico
`reguladores/rfb/outros-atos/AAAA/ato-<idAto>-<numero>-<ano>.md`, o mesmo usado pela rotina
periódica, o que evita duplicidade em coletas futuras.

Uso: python3 scripts/gerar_reforma_atos_rfb_2026.py
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co

RFB_CGIBS = "Secretaria Especial da Receita Federal do Brasil / Comitê Gestor do Imposto sobre Bens e Serviços"
RFB = "Secretaria Especial da Receita Federal do Brasil"
MF = "Ministério da Fazenda"

# (idAto, titulo, tipo, numero, data do ato, orgao, tributos, situacao, notas extras)
ATOS = [
    (148477, "Ato Conjunto RFB / CGIBS nº 1, de 22 de dezembro de 2025", "Ato Conjunto", "1", "2025-12-22",
     RFB_CGIBS, ["IBS", "CBS"], "Em vigor",
     ["Disciplina as obrigações acessórias do IBS e da CBS em 2026, incluindo o período sem penalidades por falta de "
      "registro dos campos do IBS e da CBS nos documentos fiscais. A retificação publicada no DOU de 24/12/2025 "
      "(Sijut, idAto 148512) corrige a remissão do inciso I do art. 3º (de art. 1º para art. 2º, §§ 1º e 2º) e já está "
      "incorporada ao texto abaixo."]),
    (151582, "Ato Conjunto RFB / CGIBS nº 2, de 27 de maio de 2026", "Ato Conjunto", "2", "2026-05-27",
     RFB_CGIBS, ["IBS", "CBS", "Split Payment"], "Em vigor", []),
    (151927, "Ato Conjunto RFB / CGIBS nº 3, de 19 de junho de 2026", "Ato Conjunto", "3", "2026-06-19",
     RFB_CGIBS, ["IBS", "CBS"], "Em vigor", []),
    (152616, "Ato Conjunto RFB / CGIBS nº 4, de 30 de julho de 2026", "Ato Conjunto", "4", "2026-07-30",
     RFB_CGIBS, ["IBS", "CBS"], "Em vigor (alterado pelo Ato Conjunto RFB/CGIBS nº 7/2026)",
     ["Fixa as datas de início da obrigatoriedade de emissão dos documentos fiscais eletrônicos do art. 112 dos "
      "regulamentos. As datas foram alteradas pelo Ato Conjunto RFB/CGIBS nº 7, de 11 de novembro de 2026 "
      "(`ato-154548-7-2026.md`); o texto abaixo é o compilado vigente. O resumo da Receita está em "
      "`reforma-tributaria/publicacoes/2026/rfb-cronograma-documentos-fiscais.md`."]),
    (152862, "Ato Conjunto RFB / CGIBS nº 5, de 12 de agosto de 2026", "Ato Conjunto", "5", "2026-08-12",
     RFB_CGIBS, ["IBS", "CBS"], "Em vigor", []),
    (153216, "Ato Conjunto RFB / CGIBS nº 6, de 28 de agosto de 2026", "Ato Conjunto", "6", "2026-08-28",
     RFB_CGIBS, ["IBS", "CBS"], "Em vigor", []),
    (154548, "Ato Conjunto RFB / CGIBS nº 7, de 11 de novembro de 2026", "Ato Conjunto", "7", "2026-11-11",
     RFB_CGIBS, ["IBS", "CBS"], "Em vigor",
     ["Altera o Ato Conjunto RFB/CGIBS nº 4/2026 (`ato-152616-4-2026.md`)."]),
    (154689, "Ato Conjunto RFB / CGIBS nº 8, de 13 de novembro de 2026", "Ato Conjunto", "8", "2026-11-13",
     RFB_CGIBS, ["IBS", "CBS"], "Em vigor", []),
    (154060, "Portaria MF nº 3.074, de 9 de outubro de 2026", "Portaria", "3074", "2026-10-09",
     MF, ["CBS"], "Em vigor", []),
    (154673, "Portaria RFB nº 763, de 19 de novembro de 2026", "Portaria", "763", "2026-11-19",
     RFB, ["CBS"], "Em vigor",
     ["Dispõe sobre o Piloto RTC-CBS. A Portaria RFB nº 549/2025, que instituiu o piloto inicial, consta no Sijut como "
      "não vigente e não foi incorporada."]),
]


def caminho(id_ato: int, numero: str, data: str) -> str:
    ano = data[:4]
    return f"reguladores/rfb/outros-atos/{ano}/ato-{id_ato}-{numero}-{ano}.md"


if __name__ == "__main__":
    for id_ato, titulo, tipo, numero, data, orgao, tributos, situacao, notas in ATOS:
        doc, _ = co.documento_sijut(id_ato, titulo, tipo, numero, data, orgao, tributos,
                                    notas_extra=notas, situacao=situacao)
        destino = co.gravar(caminho(id_ato, numero, data), doc)
        print(f"[Atos RFB 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes)")
