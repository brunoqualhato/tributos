"""Lote: PIS/Cofins, IPI, comércio exterior e combustíveis. Lei Complementar nº 228/2026 (PIS/Pasep e Cofins na indústria
química e petroquímica), Leis nº 15.394/2026 (créditos de PIS/Pasep e Cofins), nº 15.502/2026 (remessas postais
internacionais) e nº 15.504/2026 (Redata), Decretos nº 12.549 e nº 12.665/2025 (TIPI), nº 12.922/2026 (RIPI, tabagismo),
nº 13.116, nº 13.134 e nº 13.159/2026 (PIS/Cofins e Cide sobre gasolina e etanol hidratado) e IN RFB nº 2.324/2026
(suspensão do IPI).
Especialistas: tributos_produtos, tributos_combustiveis
A IN vem do Sijut/RFB (visão compilada, com o anexo em PDF) e segue `reguladores/rfb/instrucoes-normativas/AAAA/`,
caminho canônico da rotina periódica. As demais normas vêm de normas.leg.br (texto original).
Uso: python3 scripts/gerar_pis_cofins_ipi_combustiveis_2026.py
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
RFB = "Secretaria Especial da Receita Federal do Brasil"
CONGRESSO = "Congresso Nacional / Presidência da República"
PRESIDENCIA = "Presidência da República"
TEMA_PRODUTOS = "Produtos e Mercadorias"
TEMA_COMBUSTIVEIS = "Combustíveis e Energia"
TEMA_BENEFICIOS = "Benefícios e Incentivos Fiscais"
TIPI = "federal/regulamentos/ripi/decreto-11158-2022-tipi.md"
RIPI = "federal/regulamentos/ripi/decreto-7212-2010.md"
LEI_11196 = "federal/leis-ordinarias/lei-11196-2005.md"
LEI_14902 = "federal/regulamentos/aduana/lei-14902-2024-programa-remessa-conforme-importacao.md"
DECRETO_5060 = "federal/leis-ordinarias/combustiveis/decreto-5060-2004-aliquotas-cide.md"
LC_235 = "federal/beneficios-tributarios/lei-complementar-235-2026-renuncias-choque-energia.md"
LC_237 = "federal/beneficios-tributarios/lei-complementar-237-2026-altera-lc-229.md"
# (idAto, tipo, numero, data, orgao, tema, tributos, situacao, notas)
ATOS = [
    (150886, "Instrução Normativa", "2324", "2026-04-24", RFB, TEMA_PRODUTOS, ["IPI"], "Em vigor",
     ["Trata da suspensão do IPI prevista no art. 5º da Lei nº 9.826/1999 e no art. 29 da Lei nº 10.637/2002; "
      "o Anexo Único (PDF) tem camada de texto e foi preservado em bloco de texto."]),
]
# (urn, caminho, tipo, numero, data, titulo, orgao, tema, tributos, situacao, notas)
NORMAS = [
    ("urn:lex:br:federal:decreto:2025-07-10;12549",
     "federal/regulamentos/ripi/decreto-12549-2025-altera-tipi.md",
     "Decreto", "12549", "2025-07-10",
     "Decreto nº 12.549, de 10 de julho de 2025 (Altera a TIPI)",
     PRESIDENCIA, TEMA_PRODUTOS, ["IPI"], "Em vigor",
     [f"Altera a Tabela de Incidência do IPI (TIPI), aprovada pelo Decreto nº 11.158/2022 (`{TIPI}`), nas posições 87.03 e 87.04, "
      f"em conexão com a Lei nº 14.902/2024 (`{LEI_14902}`). O documento reproduz o texto da alteração, não a TIPI consolidada. "
      "Os Anexos I a V (alíquotas, notas complementares e parâmetros) não constam do texto obtido de normas.leg.br e devem ser "
      "consultados no DOU."]),
    ("urn:lex:br:federal:decreto:2025-10-10;12665",
     "federal/regulamentos/ripi/decreto-12665-2025-altera-tipi.md",
     "Decreto", "12665", "2025-10-10",
     "Decreto nº 12.665, de 10 de outubro de 2025 (Altera a TIPI)",
     PRESIDENCIA, TEMA_PRODUTOS, ["IPI"], "Em vigor",
     [f"Institui Ex-Tarifários e as respectivas alíquotas na TIPI, aprovada pelo Decreto nº 11.158/2022 (`{TIPI}`); "
      "os efeitos começam no primeiro dia do quarto mês subsequente ao da publicação (art. 2º). "
      "Os Ex-Tarifários constam do Anexo, que não consta do texto obtido de normas.leg.br e deve ser consultado no DOU."]),
    ("urn:lex:br:federal:decreto:2026-04-07;12922",
     "federal/regulamentos/ripi/decreto-12922-2026-altera-ripi-tabagismo.md",
     "Decreto", "12922", "2026-04-07",
     "Decreto nº 12.922, de 7 de abril de 2026 (Altera o RIPI (tabagismo) e o Decreto 12.226/2025 (jurisdições de tributação favorecida))",
     PRESIDENCIA, TEMA_PRODUTOS, ["IPI", "IRPJ", "IRRF"], "Em vigor",
     [f"Altera o Regulamento do IPI, Decreto nº 7.212/2010 (`{RIPI}`), nos arts. 212-B e 220-A (alíquotas específicas e valor por vintena "
      "do cigarro), e o Decreto nº 12.226/2024 (jurisdições de tributação favorecida e regimes fiscais privilegiados), e revoga o "
      "Decreto nº 12.127/2024. O documento reproduz o texto da alteração, não o regulamento consolidado."]),
    ("urn:lex:br:federal:lei.complementar:2026-03-19;228",
     "federal/leis-complementares/lei-complementar-228-2026-pis-cofins-industria-quimica.md",
     "Lei Complementar", "228", "2026-03-19",
     "Lei Complementar nº 228, de 19 de março de 2026 (Redução de PIS/Pasep e Cofins na indústria química e petroquímica)",
     CONGRESSO, TEMA_PRODUTOS, ["PIS/Pasep", "Cofins"], "Em vigor",
     ["Altera as Leis nº 11.196/2005 (Regime Especial da Indústria Química, REIQ) e nº 10.865/2004 e limita em R$ 2,0 bilhões e "
      "R$ 1,1 bilhão a renúncia de 2026 (art. 3º). O texto abaixo é o original da Lei Complementar, sem consolidação nas leis alteradas."]),
    ("urn:lex:br:federal:lei:2026-04-22;15394",
     "federal/leis-ordinarias/lei-15394-2026-creditos-pis-cofins.md",
     "Lei Ordinária", "15394", "2026-04-22",
     "Lei nº 15.394, de 22 de abril de 2026 (Créditos de PIS/Pasep e Cofins; altera a Lei 11.196/2005)",
     CONGRESSO, TEMA_PRODUTOS, ["PIS/Pasep", "Cofins"], "Em vigor",
     [f"Altera os arts. 47 e 48 da Lei nº 11.196/2005 (`{LEI_11196}`) para autorizar o crédito de PIS/Pasep e Cofins na aquisição de "
      "desperdícios, resíduos e aparas e isentar a respectiva venda. O texto abaixo é o original da Lei nº 15.394/2026, "
      "sem consolidação na lei alterada."]),
    ("urn:lex:br:federal:lei:2026-09-15;15504",
     "federal/beneficios-tributarios/lei-15504-2026-redata-datacenter.md",
     "Lei Ordinária", "15504", "2026-09-15",
     "Lei nº 15.504, de 15 de setembro de 2026 (Redata (regime especial de tributação para datacenter); altera a Lei 11.196/2005)",
     CONGRESSO, TEMA_BENEFICIOS, ["PIS/Pasep", "Cofins", "IPI", "Imposto de Importação"], "Em vigor",
     [f"Institui o Regime Especial de Tributação para Serviços de Datacenter (Redata) na Lei nº 11.196/2005 (`{LEI_11196}`) e altera a "
      f"Lei nº 15.211/2025 (Estatuto Digital da Criança e do Adolescente). Complementa a Lei Complementar nº 237/2026 (`{LC_237}`). "
      "O tema é o mesmo da Medida Provisória nº 1.318/2025, que não integra o acervo. O texto abaixo é o original, sem consolidação "
      "nas leis alteradas."]),
    ("urn:lex:br:federal:lei:2026-09-10;15502",
     "federal/regulamentos/aduana/lei-15502-2026-remessas-postais-internacionais.md",
     "Lei Ordinária", "15502", "2026-09-10",
     "Lei nº 15.502, de 10 de setembro de 2026 (Remessas postais internacionais; altera o Decreto-Lei 1.804/1980)",
     CONGRESSO, TEMA_PRODUTOS, ["Imposto de Importação"], "Em vigor",
     [f"Altera o Decreto-Lei nº 1.804/1980 (tributação simplificada das remessas postais internacionais) e converte em lei o tema da "
      f"Medida Provisória nº 1.357/2026. Relaciona-se à Lei nº 14.902/2024 (`{LEI_14902}`) e à Portaria MF nº 612/2023. "
      "O texto abaixo é o original da Lei, sem consolidação no Decreto-Lei."]),
    ("urn:lex:br:federal:decreto:2026-09-09;13116",
     "federal/leis-ordinarias/combustiveis/decreto-13116-2026-reduz-pis-cofins-gasolina-etanol.md",
     "Decreto", "13116", "2026-09-09",
     "Decreto nº 13.116, de 9 de setembro de 2026 (Reduz PIS/Cofins sobre gasolina e etanol hidratado (10/09 a 09/10/2026))",
     PRESIDENCIA, TEMA_COMBUSTIVEIS, ["PIS/Pasep Combustíveis", "Cofins Combustíveis"],
     "Em vigor (alterado pelo Decreto nº 13.134/2026)",
     ["Reduz as alíquotas de PIS/Pasep e Cofins sobre gasolina e etanol hidratado combustível e altera o Decreto nº 5.059/2004, "
      "que não integra o acervo. Efeitos temporais: a redução vale de 10 de setembro a 9 de outubro de 2026 (coeficiente de 0,7981 "
      "para a gasolina e de um inteiro para o etanol hidratado). O Decreto nº 13.134/2026 alterou o regime a partir de 10 de outubro "
      "de 2026."]),
    ("urn:lex:br:federal:decreto:2026-10-09;13134",
     "federal/leis-ordinarias/combustiveis/decreto-13134-2026-reduz-pis-cofins-cide-gasolina-etanol.md",
     "Decreto", "13134", "2026-10-09",
     "Decreto nº 13.134, de 9 de outubro de 2026 (Reduz PIS/Cofins sobre gasolina e etanol hidratado e a Cide-Combustíveis (LC 235/2026))",
     PRESIDENCIA, TEMA_COMBUSTIVEIS, ["PIS/Pasep Combustíveis", "Cofins Combustíveis", "CIDE-Combustíveis"],
     "Em vigor (alterado pelo Decreto nº 13.159/2026)",
     [f"Reduz a zero PIS/Pasep, Cofins e Cide-Combustíveis sobre a gasolina e PIS/Pasep e Cofins sobre o etanol hidratado de 10 de "
      f"outubro a 9 de novembro de 2026, com fundamento no art. 2º da Lei Complementar nº 235/2026 (`{LC_235}`). Altera os Decretos "
      f"nº 5.059/2004 (fora do acervo), nº 5.060/2004 (`{DECRETO_5060}`) e nº 13.119/2026 (subvenção ao etanol, fora do acervo). "
      "O Decreto nº 13.159/2026 prorrogou o prazo até 9 de dezembro de 2026."]),
    ("urn:lex:br:federal:decreto:2026-11-09;13159",
     "federal/leis-ordinarias/combustiveis/decreto-13159-2026-prorroga-reducoes-gasolina-etanol.md",
     "Decreto", "13159", "2026-11-09",
     "Decreto nº 13.159, de 9 de novembro de 2026 (Prorroga até 09/12/2026 as reduções de PIS/Cofins e Cide sobre gasolina e etanol hidratado)",
     PRESIDENCIA, TEMA_COMBUSTIVEIS, ["PIS/Pasep Combustíveis", "Cofins Combustíveis", "CIDE-Combustíveis"], "Em vigor",
     [f"Prorroga até 9 de dezembro de 2026 as reduções de PIS/Pasep, Cofins e Cide-Combustíveis sobre a gasolina e de PIS/Pasep e "
      f"Cofins sobre o etanol hidratado. Altera os Decretos nº 5.059/2004 (fora do acervo), nº 5.060/2004 (`{DECRETO_5060}`), "
      f"nº 13.119/2026 (fora do acervo) e nº 13.134/2026, com fundamento no art. 2º da Lei Complementar nº 235/2026 (`{LC_235}`). "
      "Vigente até 9 de dezembro de 2026 na data de consulta."]),
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
        print(f"[PIS/Cofins, IPI e combustíveis 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes) "
              f"pdf={dados['_anexos_pdf']} omitidos={dados['_anexos_omitidos']}")
    for urn, destino_rel, tipo, numero, data, titulo, orgao, tema, tributos, situacao, notas in NORMAS:
        doc = co.documento_lexml(urn, tipo, numero, data, titulo, orgao, tema, tributos, situacao=situacao, notas=notas)
        destino = co.gravar(destino_rel, doc)
        print(f"[PIS/Cofins, IPI e combustíveis 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes)")
