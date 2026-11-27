"""Lote: tributos subnacionais e incentivos. Lei Complementar nº 218/2025 (local de incidência do ISS sobre guincho,
guindaste e içamento), Emenda Constitucional nº 137/2025 (imunidade de IPVA para veículos com 20 anos ou mais de fabricação)
e Lei Complementar nº 222/2025 (condições e limites para incentivos fiscais ao esporte).
Especialistas: tributos_servicos, tributos_patrimonio e tributos_dividendos
Todas as normas vêm de normas.leg.br (texto original). A EC nº 137/2025 fica em `federal/leis-complementares/` porque o
plano não tem item próprio para emendas constitucionais; a nota editorial do documento registra a escolha.
Uso: python3 scripts/gerar_tributos_subnacionais_incentivos_2026.py
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
CONGRESSO = "Congresso Nacional / Presidência da República"
MESAS = "Congresso Nacional (Mesas da Câmara dos Deputados e do Senado Federal)"
LC116 = "federal/leis-complementares/iss/lei-116-2003.md"
# (urn, caminho, tipo, numero, data, titulo, orgao, tema, tributos, situacao, notas)
NORMAS = [
    ("urn:lex:br:federal:lei.complementar:2025-09-24;218",
     "federal/leis-complementares/iss/lei-complementar-218-2025-iss-guincho-obra.md",
     "Lei Complementar", "218", "2025-09-24",
     "Lei Complementar nº 218, de 24 de setembro de 2025 (Altera a LC 116/2003: ISS de guincho e içamento, local da obra)",
     CONGRESSO, "Serviços e Retenções", ["ISSQN"], "Em vigor",
     [f"Altera o art. 3º da Lei Complementar nº 116/2003 (`{LC116}`) para fixar que o ISS sobre os serviços dos subitens 7.02, "
      "7.19 e 14.14 da lista anexa é devido no local da execução da obra. O texto abaixo é o original da Lei Complementar, "
      f"sem consolidação na LC nº 116/2003, que o acervo mantém na versão de `{LC116}`."]),
    ("urn:lex:br:federal:emenda.constitucional:2025-12-09;137",
     "federal/leis-complementares/emenda-constitucional-137-2025-imunidade-ipva.md",
     "Emenda Constitucional", "137", "2025-12-09",
     "Emenda Constitucional nº 137, de 9 de dezembro de 2025 (Imunidade de IPVA para veículos que especifica; altera o art. 155 da Constituição)",
     MESAS, "Patrimônio, Herança e Veículos", ["IPVA"], "Em vigor",
     ["Acrescenta a alínea \"e\" ao inciso III do § 6º do art. 155 da Constituição Federal, que trata do IPVA. "
      "O texto abaixo é o da própria Emenda, sem consolidação na Constituição, que não integra o acervo. "
      "O documento fica em `federal/leis-complementares/` porque o plano de metas não tem pasta própria para emendas constitucionais. "
      "As leis estaduais do IPVA ficam na subpasta `leis/ipva` de cada UF em `estaduais/` e não foram alteradas por este lote."]),
    ("urn:lex:br:federal:lei.complementar:2025-11-26;222",
     "federal/beneficios-tributarios/lei-complementar-222-2025-incentivos-fiscais-esporte.md",
     "Lei Complementar", "222", "2025-11-26",
     "Lei Complementar nº 222, de 26 de novembro de 2025 (Condições e limites para incentivos fiscais ao esporte (União, Estados e Municípios))",
     CONGRESSO, "Benefícios e Incentivos Fiscais", ["IRPJ", "IRPF", "ICMS", "ISSQN"], "Em vigor",
     ["Revoga a Lei nº 11.438/2006 (Lei de Incentivo ao Esporte, art. 25) e altera a Lei nº 14.260/2021; nenhuma das duas integra o acervo. "
      "Até que Estados, Distrito Federal e Municípios editem leis para atender à Lei Complementar, ficam mantidos os limites e as condições "
      "de suas leis sobre incentivo ao esporte com base no ICMS e no ISS (art. 24), e essas leis deixam de ter eficácia em 1º de janeiro de 2033 "
      "(art. 24, parágrafo único)."]),
]
if __name__ == "__main__":
    for urn, destino_rel, tipo, numero, data, titulo, orgao, tema, tributos, situacao, notas in NORMAS:
        doc = co.documento_lexml(urn, tipo, numero, data, titulo, orgao, tema, tributos, situacao=situacao, notas=notas)
        destino = co.gravar(destino_rel, doc)
        print(f"[Subnacionais e incentivos 2025] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes)")
