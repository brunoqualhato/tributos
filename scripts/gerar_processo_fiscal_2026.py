"""Lote: processo fiscal, prazos (LC 227/2026), consensualidade (LC 225/2026 e LC 236/2026), autorregularização,
restituição e compensação (IN RFB 2.055/2021), beneficiário final (IN RFB 2.119/2022) e súmulas do CARF.
Especialistas: tributos_servicos e tributos_produtos
Todos os documentos vêm do Sijut/RFB (visão compilada, com anexos em PDF e HTML quando existirem).
INs seguem `reguladores/rfb/instrucoes-normativas/AAAA/` e as demais espécies
`reguladores/rfb/outros-atos/AAAA/`, caminhos canônicos da rotina periódica.
Uso: python3 scripts/gerar_processo_fiscal_2026.py
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
RFB = "Secretaria Especial da Receita Federal do Brasil"
MF = "Ministério da Fazenda"
TEMA_PROC = "Processo Tributário e Fiscal"
PRAZOS = ["Processo Administrativo Fiscal", "Direitos do Contribuinte"]
RESTITUICAO = ["Compensação Tributária", "Processo Administrativo Fiscal"]
# (idAto, tipo, numero, data, orgao, tema, tributos, situacao, notas)
ATOS = [
    (149140, "Ato Declaratório Interpretativo", "2", "2026-02-03", RFB, TEMA_PROC, PRAZOS, "Em vigor",
     ["Aplica o art. 173 da LC nº 227/2026 aos prazos do Decreto nº 70.235/1972 até 31/03/2026. Os efeitos práticos se exauriram "
      "naquele prazo; o ato permanece como norma interpretativa de referência."]),
    (151067, "Instrução Normativa", "2325", "2026-05-12", RFB, TEMA_PROC, PRAZOS + ["DCTFWeb"], "Em vigor",
     ["Altera a IN RFB nº 958/2009 e a IN RFB nº 2237/2024 (`reguladores/rfb/instrucoes-normativas/2024/ato-141910-2237-2024.md`), "
      "em matéria de prazos processuais (art. 173 da LC nº 227/2026 e Decreto nº 70.235/1972). A IN RFB nº 958/2009 não consta do acervo."]),
    (152863, "Portaria", "715", "2026-08-11", RFB, TEMA_PROC, ["Consensualidade", "Direitos do Contribuinte"], "Em vigor",
     ["Receita de Consenso (Procedimento de Consensualidade Fiscal), com base na LC nº 225/2026, art. 3º, II, e art. 24, I "
      "(`federal/leis-complementares/lei-complementar-225-2026-codigo-defesa-contribuinte.md`), e na LC nº 236/2026."]),
    (154367, "Instrução Normativa", "2346", "2026-10-13", RFB, TEMA_PROC, ["Programas de Conformidade", "Direitos do Contribuinte", "Confia", "Sintonia"], "Em vigor",
     ["Autorregularização para os detentores dos Selos Confia e Sintonia. Relaciona-se às INs RFB nº 2295/2025 "
      "(`reguladores/rfb/instrucoes-normativas/2025/ato-148173-2295-2025.md`) e nº 2316/2026 "
      "(`reguladores/rfb/instrucoes-normativas/2026/ato-150221-2316-2026.md`)."]),
    (151979, "Portaria", "1785", "2026-06-19", MF, TEMA_PROC, ["CARF", "Processo Administrativo Fiscal"], "Em vigor",
     ["Atribui efeito vinculante a súmulas do Conselho Administrativo de Recursos Fiscais (CARF)."]),
    (145172, "Instrução Normativa", "2272", "2025-07-17", RFB, TEMA_PROC, RESTITUICAO, "Em vigor",
     ["Altera a IN RFB nº 2055/2021 (`reguladores/rfb/instrucoes-normativas/2021/ato-122077-2055-2021.md`), que trata de restituição, compensação, "
      "ressarcimento e reembolso."]),
    (147567, "Instrução Normativa", "2288", "2025-10-30", RFB, TEMA_PROC, RESTITUICAO, "Em vigor",
     ["Altera a IN RFB nº 2055/2021 (`reguladores/rfb/instrucoes-normativas/2021/ato-122077-2055-2021.md`)."]),
    (150017, "Instrução Normativa", "2314", "2026-03-18", RFB, TEMA_PROC, RESTITUICAO, "Em vigor",
     ["Altera a IN RFB nº 2055/2021 (`reguladores/rfb/instrucoes-normativas/2021/ato-122077-2055-2021.md`)."]),
    (147406, "Instrução Normativa", "2290", "2025-10-30", RFB, TEMA_PROC, ["CNPJ", "Beneficiário Final"], "Em vigor",
     ["Altera a IN RFB nº 2119/2022 (`reguladores/rfb/instrucoes-normativas/2022/ato-127567-2119-2022.md`) para tratar dos beneficiários finais e da e-BEF."]),
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
        print(f"[Processo fiscal 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes) "
              f"pdf={dados['_anexos_pdf']} omitidos={dados['_anexos_omitidos']}")
