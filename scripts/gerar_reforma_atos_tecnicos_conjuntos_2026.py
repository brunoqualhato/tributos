"""Lote: Atos Técnicos Conjuntos RFB/CGIBS (documentação técnica dos DF-e, da DeRE, do Split Payment e dos
sistemas aduaneiros), 2026.
Especialista: tributos_reforma_transicao
Todos os documentos vêm do Sijut/RFB (visão compilada) e seguem o caminho canônico
`reguladores/rfb/outros-atos/AAAA/ato-<idAto>-<numero>-<ano>.md`, o mesmo usado pela rotina
periódica, o que evita duplicidade em coletas futuras. As Notas Técnicas citadas nas notas
editoriais são identificadas só pelo número (os documentos delas entram em outro lote).
Uso: python3 scripts/gerar_reforma_atos_tecnicos_conjuntos_2026.py
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co

RFB_CGIBS = "Secretaria Especial da Receita Federal do Brasil / Comitê Gestor do Imposto sobre Bens e Serviços"
TIPO = "Ato Técnico Conjunto"
DECRETO = "reforma-tributaria/regulamentos/decreto-12955-2026-regulamento-cbs.md"
RES6 = "reforma-tributaria/regulamentos/resolucao-cgibs-6-2026-regulamento-ibs.md"
BASE = (f"Aprovado com fundamento no Decreto nº 12.955/2026 (`{DECRETO}`) e na Resolução CGIBS nº 6/2026 "
        f"(`{RES6}`), com competência atribuída pela Resolução CGIBS nº 17/2026 (fora do acervo nesta etapa).")
DFE = ("As Notas Técnicas e os Informes Técnicos citados no texto são identificados pelo número e pela versão; os "
       "documentos deles não integram este lote. O Ato Conjunto RFB/CGIBS nº 4/2026 (`ato-152616-4-2026.md`) fixa "
       "as datas de obrigatoriedade dos documentos fiscais eletrônicos.")

# (idAto, titulo, numero, data da epígrafe, tributos, notas extras)
ATOS = [
    (152654, "Ato Técnico Conjunto RFB / CGIBS nº 1, de 31 de julho de 2026", "1", "2026-07-31",
     ["IBS", "CBS"],
     [BASE, "Aprova as versões vigentes das Notas Técnicas 2026.002, 2025.002 e 2026.007 (NF-e, NFC-e, CT-e, CT-e OS, "
      "GTV-e, BP-e, NF3e e NFCom) e ratifica as versões anteriores da documentação, inclusive as de NFGas e NFAg. " + DFE]),
    (153091, "Ato Técnico Conjunto Sufis / CGIBS nº 2, de 21 de agosto de 2026", "2", "2026-08-21",
     ["IBS", "CBS"],
     [BASE, "Aprova as Notas Técnicas 2026.006 e 2026.002 (versão 1.10a) e os Informes Técnicos 2023.002, 2025.004 e "
      "2026.001 da NF-e e da NFC-e, a Nota Técnica 2025.002 (BP-e TA) e os Manuais de Orientação ao Contribuinte da NFAg, "
      "da NFGas e da NF-e de Alienação de Bens Imóveis (NF-e ABI). " + DFE]),
    (153349, "Ato Técnico Conjunto Sufis / CGIBS nº 3, de 2 de setembro de 2026", "3", "2026-09-02",
     ["IBS", "CBS", "Imposto Seletivo"],
     [BASE, "Aprova a documentação técnica da Declaração de Regimes Específicos (DeRE) na versão 1.2.0 e ratifica a "
      "Nota Orientativa DeRE nº 2026.001. Sucede a publicação da versão 1.1.0 feita pelo Ato Conjunto RFB/CGIBS nº 3/2026 "
      "(`ato-151927-3-2026.md`) e é sucedida pelo Ato Técnico Conjunto Sufis/CGIBS nº 6/2026 (versão 1.3)."]),
    (153354, "Ato Técnico Conjunto Suara / CGIBS nº 4, de 28 de agosto de 2026", "4", "2026-08-28",
     ["IBS", "CBS", "Split Payment"],
     [BASE, "Aprova o Manual de Habilitação de Participantes e o Manual de Redes (versão 1.0.0) da Plataforma Pública do "
      "Split Payment. O Ato Técnico Conjunto Suara/CGIBS nº 5/2026 autoriza versões sequenciais do Manual de Habilitação. "
      "Sobre o modelo operacional, ver `reforma-tributaria/split-payment/split-payment-modelo-operacional.md`."]),
    (153687, "Ato Técnico Conjunto Suara / CGIBS nº 5, de 22 de setembro de 2026", "5", "2026-09-22",
     ["IBS", "CBS", "Split Payment"],
     [BASE, "Aprova os Manuais de Operações, de Integração, de Tempos, de Redes e de Segurança e o documento openAPI da "
      "Plataforma Pública do Split Payment, ratifica as versões 1.0.0 dos Manuais de Operações e de Tempos, antes "
      "disponibilizadas em minuta, e autoriza versões sequenciais (X.Y.Z) só para correção de erros materiais e "
      "ajustes redacionais. Complementa o Ato Técnico Conjunto Suara/CGIBS nº 4/2026 e o Ato Conjunto RFB/CGIBS nº 2/2026 "
      "(`ato-151582-2-2026.md`)."]),
    (153885, "Ato Técnico Conjunto Sufis / CGIBS nº 6, de 28 de setembro de 2026", "6", "2026-09-28",
     ["IBS", "CBS"],
     [BASE, "Aprova a documentação técnica da Declaração de Regimes Específicos (DeRE) na versão 1.3 (Manual de "
      "Orientação do Usuário, Leiautes, Tabelas, Regras de Validação e XSD). Sucede a versão 1.2.0 aprovada pelo Ato "
      "Técnico Conjunto Sufis/CGIBS nº 3/2026."]),
    (153886, "Ato Técnico Conjunto Sufis / CGIBS nº 8, de 29 de setembro de 2026", "8", "2026-09-29",
     ["IBS", "CBS"],
     [BASE, "Aprova as Notas Técnicas 2025.002 (versão 1.52), 2026.002 (versão 1.11), 2026.007 (versão 1.10), 2026.008, "
      "2026.010 e 2026.004 e o Informe Técnico 2025.002 (versão 1.70) para NF-e, NFC-e, CT-e, NFCom, BP-e, NF3e, NFAg "
      "e NFGas. " + DFE]),
    (153887, "Ato Técnico Conjunto Sufis / CGIBS nº 7, de 28 de setembro de 2026", "7", "2026-09-28",
     ["IBS", "CBS"],
     [BASE, "Aprova a documentação técnica da NFS-e (Nota Técnica SE/CGNFS-e nº 009, com os Anexos VI e VII) e da NFS-e "
      "de Exploração de Via (Nota Técnica SE/CGNFS-e nº 010 e Manual de Emissão). Sobre a NFS-e nacional, ver "
      "`reforma-tributaria/cbs-receita-federal/nota-tecnica-nfse-nacional-ibs-cbs.md`."]),
    (154246, "Ato Técnico Conjunto RFB / CGIBS nº 9, de 20 de outubro de 2026", "9", "2026-10-20",
     ["IBS", "CBS"],
     ["Não aprova documentação técnica: disciplina a organização e o funcionamento dos trabalhos conjuntos da Receita "
      "Federal e da Diretoria Executiva do CGIBS para implementar a reforma tributária sobre o consumo (Coordenações "
      "Normativa e Operacional e Grupos de Trabalho Integrados), com efeitos até 31 de março de 2027 (art. 17). "
      "Fundamenta-se na Resolução CGIBS nº 17/2026 (fora do acervo nesta etapa) e na Lei Complementar nº 227/2026 "
      "(`reforma-tributaria/lei-complementar-227-2026.md`). Os Anexos I e II (composição das instâncias) vinham como "
      "arquivos PDF no Sijut."]),
    (154369, "Ato Técnico Conjunto Sufis / CGIBS nº 10, de 28 de outubro de 2026", "10", "2026-10-28",
     ["IBS", "CBS", "Simples Nacional"],
     [BASE, "Aprova as Notas Técnicas 2025.002 (versão 1.53), 2026.004 (versão 1.01), 2026.005 (Simples Nacional), 2026.006, "
      "2026.007 e 2026.008 e a documentação da NF-e ABI, entre outras. " + DFE]),
    (154555, "Ato Técnico Conjunto Suana / CGIBS nº 11, de 10 de novembro de 2026", "11", "2026-11-10",
     ["IBS", "CBS"],
     [BASE, "Aprova a documentação técnica da Declaração Única de Importação (Duimp): layout versão 77.0.0 e Nota "
      "Copad/Coana/Suana/RFB nº 77/2026 com o Anexo I, e ratifica as versões 75.0.0 e 75.1.0 do layout. O layout e as "
      "Notas ficam nos portais da Receita Federal e do Portal Único Siscomex indicados no texto e não integram o acervo."]),
    (154556, "Ato Técnico Conjunto Suana / CGIBS nº 12, de 10 de novembro de 2026", "12", "2026-11-10",
     ["IBS", "CBS"],
     [BASE, "Aprova a documentação técnica da Declaração de Importação de Remessa (DIR): layout versão 1.0 e Nota "
      "Copad/Coana/Suana/RFB nº 78/2026 com o Anexo I. O layout e as Notas ficam nos portais indicados no texto e não "
      "integram o acervo."]),
]


def caminho(id_ato: int, numero: str, data: str) -> str:
    ano = data[:4]
    return f"reguladores/rfb/outros-atos/{ano}/ato-{id_ato}-{numero}-{ano}.md"


if __name__ == "__main__":
    for id_ato, titulo, numero, data, tributos, notas in ATOS:
        doc, _ = co.documento_sijut(id_ato, titulo, TIPO, numero, data, RFB_CGIBS, tributos,
                                    notas_extra=notas, situacao="Em vigor")
        destino = co.gravar(caminho(id_ato, numero, data), doc)
        print(f"[ATC RFB/CGIBS 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes)")
