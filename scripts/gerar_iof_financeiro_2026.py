"""Lote: IOF e tributação financeira. Decreto nº 12.499/2025 (altera o RIOF) e IN RFB nº 2.278/2025 (e-Financeira de
instituições de pagamento e participantes de arranjos de pagamento).
Especialista: tributos_financeiro
O Decreto nº 12.499/2025 vem de normas.leg.br (texto original). A IN vem do Sijut/RFB (visão compilada) e segue
`reguladores/rfb/instrucoes-normativas/AAAA/`, caminho canônico da rotina periódica.
Ficaram fora do lote os Decretos nº 12.466 e nº 12.467/2025: o art. 2º do Decreto nº 12.499/2025 os revoga integralmente
e o Decreto Legislativo nº 176/2025 também os sustou.
Uso: python3 scripts/gerar_iof_financeiro_2026.py
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
RFB = "Secretaria Especial da Receita Federal do Brasil"
PRESIDENCIA = "Presidência da República"
TEMA_IOF = "Tributação Financeira e IOF"
RIOF = "federal/regulamentos/iof/decreto-6306-2007.md"
SITUACAO_12499 = ("Em vigor (com ressalva: DLG 176/2025 e decisão do STF de 16/07/2025, exceto risco sacado)")
# (idAto, tipo, numero, data, orgao, tema, tributos, situacao, notas)
ATOS = [
    (145940, "Instrução Normativa", "2278", "2025-08-28", RFB, TEMA_IOF,
     ["Fiscalização Tributária", "Sigilo Bancário", "e-Financeira"], "Em vigor",
     ["Estende às instituições de pagamento e aos participantes de arranjos de pagamento a obrigação de apresentar a e-Financeira, "
      "instituída pela IN RFB nº 1.571/2015 (fora do acervo), com base na Lei nº 12.865/2013. O texto abaixo é o da própria IN, "
      "sem consolidação no ato que ela estende."]),
]
# (urn, caminho, tipo, numero, data, titulo, orgao, tema, tributos, situacao, notas)
NORMAS = [
    ("urn:lex:br:federal:decreto:2025-06-11;12499",
     "federal/regulamentos/iof/decreto-12499-2025-altera-riof.md",
     "Decreto", "12499", "2025-06-11",
     "Decreto nº 12.499, de 11 de junho de 2025 (Altera o RIOF)",
     PRESIDENCIA, TEMA_IOF, ["IOF"], SITUACAO_12499,
     [f"Altera o Regulamento do IOF, Decreto nº 6.306/2007 (`{RIOF}`), e revoga o art. 15-C desse regulamento e os Decretos "
      "nº 12.466 e nº 12.467/2025 (art. 2º), que ficaram fora do acervo. O texto abaixo é o original do Decreto, sem consolidação "
      "no RIOF.",
      "Ressalva de vigência: o Decreto Legislativo nº 176/2025 (26/06/2025) sustou os Decretos nº 12.466, nº 12.467 e nº 12.499/2025 "
      "e restabeleceu a redação anterior do RIOF. Segundo o Supremo Tribunal Federal (ADI 7827, ADI 7839 e ADC 96, relator "
      "ministro Alexandre de Moraes), os efeitos do decreto legislativo e dos decretos foram suspensos em liminar do início de "
      "julho de 2025. Em 16/07/2025, a decisão conjunta restabeleceu a eficácia do Decreto nº 12.499/2025 desde a edição, em "
      "11/06/2025, mantendo a suspensão apenas quanto às operações de \"risco sacado\" (art. 7º, § 23 e § 24, do RIOF, na redação do "
      "decreto). A liminar será analisada pelo Plenário do STF. A Receita Federal orienta observar o RIOF com a redação do "
      "Decreto nº 12.499/2025 a partir dessa decisão e dispensa a cobrança retroativa do IOF no período de suspensão.",
      "Esta ressalva vem de fontes institucionais (noticias.stf.jus.br e nota da Receita Federal publicada em gov.br/fazenda em "
      "17/07/2025) e não do metadado de normas.leg.br, que não registra situação para a norma. Não faz parte do texto do Decreto. "
      "Confira o andamento das ações no STF antes de aplicar o texto."]),
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
        print(f"[IOF e tributação financeira 2025] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes) "
              f"pdf={dados['_anexos_pdf']} omitidos={dados['_anexos_omitidos']}")
    for urn, destino_rel, tipo, numero, data, titulo, orgao, tema, tributos, situacao, notas in NORMAS:
        doc = co.documento_lexml(urn, tipo, numero, data, titulo, orgao, tema, tributos, situacao=situacao, notas=notas)
        destino = co.gravar(destino_rel, doc)
        print(f"[IOF e tributação financeira 2025] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes)")
