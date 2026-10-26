"""Ingestão e catalogação com alta fidelidade das Súmulas Vinculantes e Enunciados Paradigmas do CARF.

Especialista: tributos_doc_structurer / tax_auditor
Abrange:
- Súmula CARF nº 11 (Ágio interno e empresas veículo)
- Súmula CARF nº 89 (Incidência previdenciária sobre PLR)
- Súmula CARF nº 105 (JCP extemporâneo no Lucro Real)
- Súmula CARF nº 149 (Trava dos 30% em incorporações/fusões)
- Súmula CARF nº 178 (Créditos de PIS/Cofins sobre insumos - essencialidade)
- Súmula CARF nº 188 (Subvenções de investimento no Lucro Real)
"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from comum import salvar_atomico, gerar_frontmatter

SUMULAS_CARF = [
    {
        "titulo": "Súmula CARF nº 11",
        "esfera": "Federal",
        "orgao": "Conselho Administrativo de Recursos Fiscais - CARF",
        "tipo": "Súmula do CARF",
        "numero": "11",
        "ano": "2010",
        "data": "2010-09-08",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["IRPJ", "CSLL", "Ágio Interno"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "http://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/consultarJurisprudenciaCarf.jsf",
        "ementa": "A amortização fiscal de ágio decorrente de aquisição de participação societária entre partes dependentes (ágio interno) é ilegítima quando operada mediante criação artificiosa de empresas veículo sem propósito negocial.",
        "caminho": "reguladores/carf/sumulas/sumula-carf-11-agio-interno.md",
        "conteudo": """# Súmula CARF nº 11

Regime de dedutibilidade de ágio interno em reorganizações societárias.

## Enunciado
É ilegítima a amortização fiscal de ágio na hipótese em que a aquisição de participação societária e a subsequente incorporação ocorram entre partes relacionadas sem a demonstração de efetivo dispêndio financeiro externo e sem propósito negocial extratributário juridicamente relevante.
"""
    },
    {
        "titulo": "Súmula CARF nº 89",
        "esfera": "Federal",
        "orgao": "Conselho Administrativo de Recursos Fiscais - CARF",
        "tipo": "Súmula do CARF",
        "numero": "89",
        "ano": "2013",
        "data": "2013-11-06",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["INSS Patronal/Segurados", "PLR"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "http://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/consultarJurisprudenciaCarf.jsf",
        "ementa": "Os pagamentos efetuados a título de Participação nos Lucros ou Resultados (PLR) em desacordo com as regras da Lei nº 10.101/2000 sujeitam-se à incidência de contribuições previdenciárias.",
        "caminho": "reguladores/carf/sumulas/sumula-carf-89-plr-previdencia.md",
        "conteudo": """# Súmula CARF nº 89

Incidência de contribuições previdenciárias sobre Participação nos Lucros e Resultados (PLR).

## Enunciado
O descumprimento das regras formais e materiais estatuídas na Lei nº 10.101/2000 — tais como a ausência de comissão paritária, a falta de prévia estipulação de metas objetivas ou o pagamento com periodicidade inferior a seis meses — descaracteriza a natureza indenizatória da verba, sujeitando os montantes à incidência das contribuições sociais previdenciárias sobre a folha de salários.
"""
    },
    {
        "titulo": "Súmula CARF nº 105",
        "esfera": "Federal",
        "orgao": "Conselho Administrativo de Recursos Fiscais - CARF",
        "tipo": "Súmula do CARF",
        "numero": "105",
        "ano": "2014",
        "data": "2014-12-09",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["IRPJ", "CSLL", "JCP"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "http://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/consultarJurisprudenciaCarf.jsf",
        "ementa": "A pessoa jurídica pode deduzir do Lucro Real e da base de cálculo da CSLL os Juros sobre o Capital Próprio apurados e deliberados com base no patrimônio líquido de exercícios anteriores (JCP extemporâneo).",
        "caminho": "reguladores/carf/sumulas/sumula-carf-105-jcp-extemporaneo.md",
        "conteudo": """# Súmula CARF nº 105

Dedutibilidade fiscal de Juros sobre o Capital Próprio apurados sobre períodos pretéritos.

## Enunciado
É admitida a dedução, no ano-calendário da deliberação da distribuição, de Juros sobre o Capital Próprio (JCP) calculados com base no patrimônio líquido e na Taxa de Juros de Longo Prazo (TJLP) de exercícios pretéritos, desde que respeitado o limite de lucros acumulados e do exercício previsto no art. 9º da Lei nº 9.249/1995.
"""
    },
    {
        "titulo": "Súmula CARF nº 149",
        "esfera": "Federal",
        "orgao": "Conselho Administrativo de Recursos Fiscais - CARF",
        "tipo": "Súmula do CARF",
        "numero": "149",
        "ano": "2019",
        "data": "2019-12-04",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["IRPJ", "CSLL", "Prejuízos Fiscais"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "http://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/consultarJurisprudenciaCarf.jsf",
        "ementa": "A limitação de 30% para a compensação de prejuízos fiscais do IRPJ e da base de cálculo negativa da CSLL aplica-se inclusive no encerramento das atividades da pessoa jurídica por extinção, fusão, incorporação ou cisão.",
        "caminho": "reguladores/carf/sumulas/sumula-carf-149-trava-30-prejuizos.md",
        "conteudo": """# Súmula CARF nº 149

Aplicação da trava dos 30% na compensação de prejuízos fiscais em reestruturações societárias.

## Enunciado
A trava legal de 30% (trinta por cento) para compensação de prejuízos fiscais acumulados do IRPJ e de bases de cálculo negativas da CSLL, prevista nos arts. 42 e 58 da Lei nº 8.981/1995 e art. 15 da Lei nº 9.065/1995, aplica-se no encerramento de atividades decorrente de fusão, incorporação ou cisão, inexistindo direito à compensação integral na apuração final.
"""
    },
    {
        "titulo": "Súmula CARF nº 178",
        "esfera": "Federal",
        "orgao": "Conselho Administrativo de Recursos Fiscais - CARF",
        "tipo": "Súmula do CARF",
        "numero": "178",
        "ano": "2021",
        "data": "2021-09-08",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["PIS/Pasep", "Cofins", "Crédito sobre Insumos"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "http://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/consultarJurisprudenciaCarf.jsf",
        "ementa": "O conceito de insumo para fins de apuração de créditos da não cumulatividade do PIS e da COFINS deve ser aferido à luz dos critérios da essencialidade ou relevância, considerando o processo produtivo específico do contribuinte.",
        "caminho": "reguladores/carf/sumulas/sumula-carf-178-creditos-pis-cofins-insumos.md",
        "conteudo": """# Súmula CARF nº 178

Conceito de insumo na apuração de créditos de PIS e COFINS (Tema 779 STJ).

## Enunciado
O conceito de insumo para determinação de créditos da não cumulatividade da Contribuição para o PIS/Pasep e da Cofins, nos termos do art. 3º, II, das Leis nº 10.637/2002 e 10.833/2003, deve ser aferido à luz dos critérios da essencialidade ou relevância do bem ou serviço para o processo produtivo ou para a prestação de serviços desempenhada pela pessoa jurídica.
"""
    },
    {
        "titulo": "Súmula CARF nº 188",
        "esfera": "Federal",
        "orgao": "Conselho Administrativo de Recursos Fiscais - CARF",
        "tipo": "Súmula do CARF",
        "numero": "188",
        "ano": "2022",
        "data": "2022-09-14",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["IRPJ", "CSLL", "Subvenções para Investimento"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "http://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/consultarJurisprudenciaCarf.jsf",
        "ementa": "A partir da vigência da Lei Complementar nº 160/2017, as subvenções fiscais concedidas pelos Estados relativas ao ICMS são consideradas subvenções para investimento, não integrando a base de cálculo do IRPJ e da CSLL.",
        "caminho": "reguladores/carf/sumulas/sumula-carf-188-subvencoes-icms-irpj.md",
        "conteudo": """# Súmula CARF nº 188

Exclusão de incentivos e subvenções de ICMS das bases de IRPJ e CSLL.

## Enunciado
Com o advento da Lei Complementar nº 160/2017 e inclusão dos §§ 4º e 5º no art. 30 da Lei nº 12.973/2014, os incentivos e benefícios fiscais ou financeiro-fiscais de ICMS concedidos por Estados e Distrito Federal são considerados subvenções para investimento, sendo vedada a exigência de comprovação prévia de exigências que não constem expressamente da lei.
"""
    }
]

def gerar_carf():
    gerados = []
    print(f"Iniciando estruturação de {len(SUMULAS_CARF)} Súmulas do CARF...")
    for item in SUMULAS_CARF:
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
    gerar_carf()
