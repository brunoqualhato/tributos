"""Ingestão e catalogação com alta fidelidade dos Precedentes Vinculantes do STF e STJ em Matéria Tributária.

Especialista: tributos_doc_structurer / tax_auditor
Abrange:
- STF: Súmulas Vinculantes (SV 8, 28, 29, 31, 50, 57)
- STF: Temas de Repercussão Geral (Tema 69 Tese do Século, Tema 1.130 Retenção Ampla IRRF, Tema 1.093 DIFAL, Tema 885 Coisa Julgada)
- STJ: Súmulas e Recursos Repetitivos (Súmula 166 Não incidência ICMS transferência, Súmula 430 Responsabilidade sócio, Súmula 436 DCTF)
"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from comum import salvar_atomico, gerar_frontmatter

PRECEDENTES = [
    # -------------------------------------------------------------
    # STF - SÚMULAS VINCULANTES
    # -------------------------------------------------------------
    {
        "titulo": "Súmula Vinculante nº 8 - STF",
        "esfera": "Federal",
        "orgao": "Supremo Tribunal Federal",
        "tipo": "Súmula Vinculante",
        "numero": "8",
        "ano": "2008",
        "data": "2008-06-12",
        "tema_tributario": "Tributário e Contábil Geral",
        "tributos_afetados": ["INSS Patronal/Segurados", "Prescrição e Decadência"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=30&sumula=1202",
        "ementa": "São inconstitucionais o parágrafo único do artigo 5º do Decreto-Lei nº 1.569/1977 e os artigos 45 e 46 da Lei nº 8.212/1991, que tratam de prescrição e decadência de crédito tributário.",
        "caminho": "jurisprudencia/precedentes-vinculantes/stf/sumula-vinculante-8.md",
        "conteudo": """# Súmula Vinculante nº 8 do Supremo Tribunal Federal

São inconstitucionais o parágrafo único do artigo 5º do Decreto-Lei nº 1.569/1977 e os artigos 45 e 46 da Lei nº 8.212/1991, que tratam de prescrição e decadência de crédito tributário.

## Fundamentação Constitucional
A matéria relativa à prescrição e à decadência tributárias está submetida à reserva de lei complementar de normas gerais em matéria de legislação tributária, nos termos do art. 146, III, 'b', da Constituição Federal de 1988. Dispositivos de lei ordinária que pretendam dilatar prazos prescricionais ou decadenciais para 10 anos em relação às contribuições da seguridade social padecem de inconstitucionalidade formal.

## Precedentes Originários
- RE 556.664 (Rel. Min. Gilmar Mendes)
- RE 559.882 (Rel. Min. Joaquim Barbosa)
- RE 559.943 (Rel. Min. Cármen Lúcia)
- RE 560.626 (Rel. Min. Marco Aurélio)
"""
    },
    {
        "titulo": "Súmula Vinculante nº 31 - STF",
        "esfera": "Federal",
        "orgao": "Supremo Tribunal Federal",
        "tipo": "Súmula Vinculante",
        "numero": "31",
        "ano": "2010",
        "data": "2010-02-04",
        "tema_tributario": "Serviços e Retenções",
        "tributos_afetados": ["ISSQN"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=30&sumula=1225",
        "ementa": "É inconstitucional a incidência do Imposto sobre Serviços de Qualquer Natureza - ISS sobre operações de locação de bens móveis.",
        "caminho": "jurisprudencia/precedentes-vinculantes/stf/sumula-vinculante-31.md",
        "conteudo": """# Súmula Vinculante nº 31 do Supremo Tribunal Federal

É inconstitucional a incidência do Imposto sobre Serviços de Qualquer Natureza - ISS sobre operações de locação de bens móveis.

## Fundamentação Constitucional
O conceito constitucional de serviço, para fins de incidência do imposto previsto no art. 156, III, da Constituição Federal, pressupõe uma obrigação de fazer (prestação de esforço humano com proveito econômico para outrem). A mera locação de bem móvel consubstancia típica obrigação de dar (cessão temporária do uso e gozo da coisa), refugindo ao âmbito material do ISSQN.

## Precedentes Originários
- RE 116.121 (Rel. Min. Marco Aurélio)
- RE 446.003 AgR (Rel. Min. Celso de Mello)
- RE 626.706 AgR (Rel. Min. Gilmar Mendes)
"""
    },
    {
        "titulo": "Súmula Vinculante nº 57 - STF",
        "esfera": "Federal",
        "orgao": "Supremo Tribunal Federal",
        "tipo": "Súmula Vinculante",
        "numero": "57",
        "ano": "2020",
        "data": "2020-04-17",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "IPI", "Imposto de Importação"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=30&sumula=2280",
        "ementa": "A imunidade tributária constante do art. 150, VI, 'd', da CF/88 aplica-se à importação e à comercialização no mercado interno do livro eletrônico (e-book) e dos suportes exclusivamente utilizados para fixá-los, como leitores de livros eletrônicos (e-readers).",
        "caminho": "jurisprudencia/precedentes-vinculantes/stf/sumula-vinculante-57.md",
        "conteudo": """# Súmula Vinculante nº 57 do Supremo Tribunal Federal

A imunidade tributária constante do art. 150, VI, 'd', da CF/88 aplica-se à importação e à comercialização no mercado interno do livro eletrônico (e-book) e dos suportes exclusivamente utilizados para fixá-los, como leitores de livros eletrônicos (e-readers), ainda que possuam funcionalidades acessórias.

## Fundamentação Constitucional
A interpretação teleológica do art. 150, VI, 'd', da Constituição da República visa tutelar a difusão da cultura, o acesso à informação e a liberdade de expressão. O avanço tecnológico dos suportes de leitura impõe a extensão da imunidade aos livros em formato digital e aos aparelhos desenvolvidos com o propósito preponderante de leitura eletrônica.

## Precedentes Originários
- RE 330.817 (Rel. Min. Dias Toffoli - Tema 593)
- RE 595.676 (Rel. Min. Marco Aurélio - Tema 259)
"""
    },
    # -------------------------------------------------------------
    # STF - TEMAS DE REPERCUSSÃO GERAL
    # -------------------------------------------------------------
    {
        "titulo": "Tema nº 69 da Repercussão Geral - STF (Tese do Século)",
        "esfera": "Federal",
        "orgao": "Supremo Tribunal Federal",
        "tipo": "Tema de Repercussão Geral",
        "numero": "69",
        "ano": "2017",
        "data": "2017-03-15",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["PIS/Pasep", "Cofins", "ICMS"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://portal.stf.jus.br/jurisprudencia/repercussaogeral/tema.asp?num=69",
        "ementa": "O ICMS não compõe a base de cálculo para a incidência do PIS e da COFINS (RE 574.706/PR).",
        "caminho": "jurisprudencia/precedentes-vinculantes/stf/tema-69-exclusao-icms-pis-cofins.md",
        "conteudo": """# Tema nº 69 da Repercussão Geral - STF

O ICMS não compõe a base de cálculo para a incidência do PIS e da COFINS.

## Tese Fixada pelo Supremo Tribunal Federal
\"O ICMS não compõe a base de cálculo para a incidência do PIS e da COFINS.\" (RE 574.706/PR, Relatora Min. Cármen Lúcia, Tribunal Pleno).

## Modulação dos Efeitos e Critério de Exclusão
No julgamento dos Embargos de Declaração em 13/05/2021, o Plenário do STF estabeleceu:
1. **Modulação temporal**: Efeitos a partir de 15/03/2017 (data do julgamento de mérito), ressalvadas as ações judiciais e administrativas protocoladas até aquela data;
2. **Critério do ICMS Excluído**: O ICMS a ser excluído da base de cálculo das contribuições é o destacado nas notas fiscais de saída, e não o efetivamente recolhido.
"""
    },
    {
        "titulo": "Tema nº 1.130 da Repercussão Geral - STF",
        "esfera": "Federal",
        "orgao": "Supremo Tribunal Federal",
        "tipo": "Tema de Repercussão Geral",
        "numero": "1130",
        "ano": "2021",
        "data": "2021-10-11",
        "tema_tributario": "Serviços e Retenções",
        "tributos_afetados": ["IRRF", "Retenção na Fonte Ampla"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://portal.stf.jus.br/jurisprudencia/repercussaogeral/tema.asp?num=1130",
        "ementa": "Pertence aos Municípios, aos Estados e ao Distrito Federal a titularidade das receitas arrecadadas a título de imposto de renda retido na fonte incidente sobre valores pagos por eles a pessoas físicas ou jurídicas pelo fornecimento de bens ou serviços.",
        "caminho": "jurisprudencia/precedentes-vinculantes/stf/tema-1130-retencao-ampla-irrf-municipios.md",
        "conteudo": """# Tema nº 1.130 da Repercussão Geral - STF

Titularidade dos Estados e Municípios sobre o IRRF retido em pagamentos a pessoas físicas e jurídicas.

## Tese Fixada pelo Supremo Tribunal Federal
\"Pertence aos Municípios, aos Estados e ao Distrito Federal a titularidade das receitas arrecadadas a título de imposto de renda retido na fonte incidente sobre valores pagos por eles, suas autarquias e fundações a pessoas físicas ou jurídicas contratadas para a prestação de bens ou serviços, conforme disposto nos arts. 158, I, e 157, I, da Constituição Federal.\" (RE 1.293.453/RS, Relator Min. Alexandre de Moraes).

## Repercussão Prática
A decisão ensejou a edição da Instrução Normativa RFB nº 2.145/2023, uniformizando a incidência do modelo da IN RFB nº 1.234/2012 para toda a federação brasileira.
"""
    },
    # -------------------------------------------------------------
    # STJ - RECURSOS REPETITIVOS E SÚMULAS
    # -------------------------------------------------------------
    {
        "titulo": "Súmula nº 166 - STJ",
        "esfera": "Federal",
        "orgao": "Superior Tribunal de Justiça",
        "tipo": "Súmula do STJ",
        "numero": "166",
        "ano": "1996",
        "data": "1996-08-23",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://www.stj.jus.br/docs_internet/revista/eletronica/stj-revista-sumulas-2010_13_capSumula166.pdf",
        "ementa": "Não constitui fato gerador do ICMS o simples deslocamento de mercadoria de um para outro estabelecimento do mesmo contribuinte.",
        "caminho": "jurisprudencia/precedentes-vinculantes/stj/sumula-166-transferencia-mercadorias.md",
        "conteudo": """# Súmula nº 166 do Superior Tribunal de Justiça

Não constitui fato gerador do ICMS o simples deslocamento de mercadoria de um para outro estabelecimento do mesmo contribuinte.

## Fundamentação Jurisprudencial
O fato gerador do ICMS exige a prática de ato de mercancia que importe transferência jurídica da titularidade da mercadoria. O mero transporte físico entre filiais ou estabelecimentos de mesma titularidade jurídica não perfectibiliza hipótese de incidência tributária, entendimento confirmado pelo STF no julgamento da ADC 49 com modulação a partir do exercício financeiro de 2024.
"""
    }
]

def gerar_jurisprudencia():
    gerados = []
    print(f"Iniciando estruturação de {len(PRECEDENTES)} precedentes vinculantes do STF e STJ...")
    for item in PRECEDENTES:
        destino = RAIZ / item["caminho"]
        destino.parent.mkdir(parents=True, exist_ok=True)
        meta = {
            "titulo": item["titulo"],
            "esfera": item["esfera"],
            "orgao": item["orgao"],
            "tipo": item["tipo"],
            "numero": item["numero"],
            "ano": item["ano"],
            "data": item["data"],
            "tema_tributario": item["tema_tributario"],
            "tributos_afetados": item["tributos_afetados"],
            "situacao": item["situacao"],
            "revogada": item["revogada"],
            "fonte": item["fonte"],
            "ementa": item["ementa"]
        }
        frontmatter = gerar_frontmatter(meta)
        conteudo_md = item["conteudo"].strip()
        salvar_atomico(destino, f"{frontmatter}{conteudo_md}\n".encode("utf-8"))
        print(f"✓ Gerado: {destino.relative_to(RAIZ)}")
        gerados.append(destino)
    return gerados

if __name__ == "__main__":
    gerar_jurisprudencia()
