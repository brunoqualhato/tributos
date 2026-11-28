"""Lote: regulamentação e acompanhamento da LC 224/2025 (benefícios fiscais) e transparência ativa de benefícios.
Especialistas: tributos_produtos e tributos_servicos
Todos os documentos vêm do Sijut/RFB (visão compilada, com anexos em PDF quando existirem).
INs seguem `reguladores/rfb/instrucoes-normativas/AAAA/`; a Portaria MF, a Portaria RFB e a Nota Cosit
seguem `reguladores/rfb/outros-atos/AAAA/`, caminhos canônicos da rotina periódica.
A Nota Cosit nº 207/2026 é documento do Receita Soluciona (não normativo): o conteúdo está em anexo PDF.
Uso: python3 scripts/gerar_beneficios_fiscais_lc224_2026.py
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
RFB = "Secretaria Especial da Receita Federal do Brasil"
MF = "Ministério da Fazenda"
COSIT = "Coordenação-Geral de Tributação (Cosit) / Secretaria Especial da Receita Federal do Brasil"
TEMA_BEN = "Benefícios e Incentivos Fiscais"
BENEF = ["IRPJ", "CSLL", "PIS/Pasep", "Cofins", "IPI", "Imposto de Importação"]
APOSTAS = ["Tributos sobre apostas de quota fixa"]
LC224 = "federal/beneficios-tributarios/lei-complementar-224-2025-reducao-beneficios-tributarios.md"
# (idAto, tipo, numero, data, orgao, tema, tributos, situacao, notas)
ATOS = [
    (151860, "Portaria", "1766", "2026-06-17", MF, TEMA_BEN, APOSTAS, "Em vigor",
     [f"Regulamenta o art. 6º da Lei Complementar nº 224/2025 (`{LC224}`), que trata da responsabilidade tributária "
      "de terceiros na exploração de apostas de quota fixa."]),
    (152704, "Nota Cosit", "207", "2026-07-14", COSIT, TEMA_BEN, BENEF, "Em vigor",
     [f"Documento do tipo Nota publicado no Sijut (Receita Soluciona), sobre a Lei Complementar nº 224/2025 (`{LC224}`) e a Zona Franca de Manaus. "
      "Não é ato normativo: expressa o entendimento da Cosit e não substitui a legislação. O conteúdo integral consta do anexo PDF `Nota Cosit nº 207-2026.pdf`, reproduzido abaixo."]),
    (152158, "Instrução Normativa", "2332", "2026-06-25", RFB, TEMA_BEN, BENEF, "Em vigor (alterada pela IN RFB nº 2341/2026)",
     [f"Critérios e procedimentos para o tratamento de irregularidades no acompanhamento da fruição de benefícios fiscais, no contexto da LC nº 224/2025 (`{LC224}`). "
      "A retificação publicada em 09/07/2026 já consta do texto compilado. Alterada pela IN RFB nº 2341/2026."]),
    (153242, "Instrução Normativa", "2341", "2026-08-31", RFB, TEMA_BEN, BENEF, "Em vigor",
     ["Altera a IN RFB nº 2332/2026 (`ato-152158-2332-2026.md`)."]),
    (154610, "Portaria", "745", "2026-10-28", RFB, TEMA_BEN, BENEF, "Em vigor",
     ["Transparência ativa de benefícios fiscais. Sucede a Portaria RFB nº 319/2023 "
      "(`reguladores/rfb/outros-atos/2023/ato-130676-319-2023.md`), revogada pela Portaria RFB nº 744/2026, "
      "de 28/10/2026, com efeitos desde 13/11/2026."]),
    (148320, "Instrução Normativa", "2297", "2025-12-11", RFB, TEMA_BEN, BENEF, "Em vigor",
     ["Altera a IN RFB nº 1.307/2012, que dispõe sobre a Declaração de Benefícios Fiscais (DBF) "
      "(`reguladores/rfb/instrucoes-normativas/2012/ato-39240-1307-2012.md`)."]),
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
        print(f"[Benefícios LC 224 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes) "
              f"pdf={dados['_anexos_pdf']} omitidos={dados['_anexos_omitidos']}")
