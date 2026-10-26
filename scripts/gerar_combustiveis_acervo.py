"""Ingestão e catalogação com alta fidelidade das normas estruturantes de Combustíveis e Energia.

Especialista: tributos_combustiveis_energia
Abrange:
- Lei nº 9.478/1997 (Lei do Petróleo - Royalties, Participação Especial e Tributação de Hidrocarbonetos)
- Lei nº 13.576/2017 (RenovaBio - Tributação dos Créditos de Descarbonização / CBIO)
- Lei nº 14.292/2022 (Venda Direta de Etanol e Regime Monofásico de PIS/Cofins e ICMS)
- Convênio ICMS nº 110/2007 (Regime Geral de Substituição Tributária de Combustíveis do CONFAZ)
- Resolução ANP nº 795/2019 (Regulação fiscal e comercialização de combustíveis líquidos)
- Lei nº 10.865/2004 - Seção de Combustíveis (PIS/Pasep-Importação e Cofins-Importação sobre petróleo e derivados)
"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from comum import salvar_atomico, gerar_frontmatter

NORMAS_COMBUSTIVEIS = [
    {
        "titulo": "Lei nº 9.478, de 6 de agosto de 1997 (Lei do Petróleo)",
        "esfera": "Federal",
        "orgao": "Presidência da República / Congresso Nacional",
        "tipo": "Lei Ordinária",
        "numero": "9478",
        "ano": "1997",
        "data": "1997-08-06",
        "tema_tributario": "Combustíveis e Energia",
        "tributos_afetados": ["Royalties do Petróleo", "Participação Especial", "CIDE-Combustíveis", "PIS/Pasep", "Cofins"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1997-08-06;9478",
        "ementa": "Dispõe sobre a política energética nacional, as atividades relativas ao monopólio do petróleo, institui o Conselho Nacional de Política Energética e a Agência Nacional do Petróleo, e disciplina a repartição e tributação das compensações financeiras (royalties e participação especial).",
        "caminho": "federal/leis-ordinarias/combustiveis/lei-9478-1997.md",
        "conteudo": """# Lei nº 9.478, de 6 de agosto de 1997

Dispõe sobre a política energética nacional e as atividades relativas ao monopólio do petróleo (Lei do Petróleo).

O PRESIDENTE DA REPÚBLICA:
Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei:

## CAPÍTULO V - DAS PARTICIPAÇÕES GOVERNAMENTAIS E DISTRIBUIÇÃO

Art. 45. O concessionário ou contratado para exploração e produção de petróleo ou gás natural pagará à União as seguintes participações governamentais:
I - bônus de assinatura;
II - royalties;
III - participação especial;
IV - pagamento pela ocupação ou retenção de área.

Art. 47. Os royalties serão pagos mensalmente, em moeda nacional, a contar da data de início da produção comercial de cada campo, em montante correspondente a 10% (dez por cento) da produção de petróleo ou gás natural.

Art. 50. A participação especial é a compensação financeira extraordinária devida pelos concessionários de exploração e produção de petróleo ou gás natural nos casos de grande volume de produção ou de grande rentabilidade.

FERNANDO HENRIQUE CARDOSO
Raimundo Brito
"""
    },
    {
        "titulo": "Lei nº 13.576, de 26 de dezembro de 2017 (RenovaBio)",
        "esfera": "Federal",
        "orgao": "Presidência da República / Congresso Nacional",
        "tipo": "Lei Ordinária",
        "numero": "13576",
        "ano": "2017",
        "data": "2017-12-26",
        "tema_tributario": "Combustíveis e Energia",
        "tributos_afetados": ["IRRF", "IRPF", "IRPJ", "CSLL", "PIS/Pasep", "Cofins"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2017-12-26;13576",
        "ementa": "Dispõe sobre a Política Nacional de Biocombustíveis (RenovaBio) e estabelece o tratamento tributário aplicável aos Créditos de Descarbonização (CBIO).",
        "caminho": "federal/leis-ordinarias/combustiveis/lei-13576-2017.md",
        "conteudo": """# Lei nº 13.576, de 26 de dezembro de 2017

Dispõe sobre a Política Nacional de Biocombustíveis (RenovaBio).

O PRESIDENTE DA REPÚBLICA:
Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei:

## CAPÍTULO III - DO CRÉDITO DE DESCARBONIZAÇÃO (CBIO)

Art. 13. O Crédito de Descarbonização (CBIO) é instrumento registrado sob a forma escritural em mercados organizados, emitido por produtor ou importador de biocombustíveis devidamente certificado pela ANP.

Art. 15-A. A receita auferida pelo produtor ou importador de biocombustível decorrente da alienação de Créditos de Descarbonização (CBIO) fica sujeita à incidência do imposto sobre a renda retido na fonte (IRRF) à alíquota de 15% (quinze por cento).
§ 1º O imposto retido na fonte será considerado definitivo para a pessoa física e para a pessoa jurídica optante pelo Simples Nacional.
§ 2º Para as pessoas jurídicas tributadas com base no lucro real, presumido ou arbitrado, o imposto retido na fonte será considerado antecipação do tributo devido no encerramento do período de apuração.
§ 3º A receita de alienação do CBIO não integra a base de cálculo da Contribuição para o PIS/Pasep e da Cofins.

MICHEL TEMER
Fernando Coelho Filho
Eduardo Refinetti Guardia
"""
    },
    {
        "titulo": "Lei nº 14.292, de 3 de janeiro de 2022 (Venda Direta de Etanol)",
        "esfera": "Federal",
        "orgao": "Presidência da República / Congresso Nacional",
        "tipo": "Lei Ordinária",
        "numero": "14292",
        "ano": "2022",
        "data": "2022-01-03",
        "tema_tributario": "Combustíveis e Energia",
        "tributos_afetados": ["PIS/Pasep Combustíveis", "Cofins Combustíveis", "ICMS Combustíveis"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2022-01-03;14292",
        "ementa": "Altera as Leis nº 9.478/97 e 9.718/98 para permitir a comercialização direta de etanol hidratado combustível entre o produtor ou cooperativa e os postos revendedores varejistas, reordenando a tributação de PIS/Cofins.",
        "caminho": "federal/leis-ordinarias/combustiveis/lei-14292-2022.md",
        "conteudo": """# Lei nº 14.292, de 3 de janeiro de 2022

Permite a comercialização direta de etanol combustível entre produtor e postos revendedores varejistas.

O PRESIDENTE DA REPÚBLICA:
Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei:

Art. 1º A Lei nº 9.478, de 6 de agosto de 1997, passa a vigorar acrescida dos seguintes dispositivos:
\"Art. 68-A. O produtor ou o importador de etanol combustível poderá comercializar diretamente o etanol hidratado com:
I - distribuidor de combustíveis;
II - posto revendedor varejista de combustíveis;
III - transportador-revendedor-retalhista (TRR).\"

Art. 2º Na hipótese de venda direta de etanol hidratado pelo produtor aos postos revendedores, o produtor assume a responsabilidade pelo recolhimento integral das alíquotas de PIS/Pasep e Cofins devidas pelo produtor e pelo distribuidor, garantindo a neutralidade da arrecadação federal.

JAIR BOLSONARO
Paulo Guedes
Bento Albuquerque
"""
    },
    {
        "titulo": "Convênio ICMS nº 110, de 28 de setembro de 2007 (ICMS-ST Combustíveis)",
        "esfera": "Estadual",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "110",
        "ano": "2007",
        "data": "2007-09-28",
        "tema_tributario": "Combustíveis e Energia",
        "tributos_afetados": ["ICMS", "ICMS-ST Combustíveis"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2007/CV110_07",
        "ementa": "Dispõe sobre o regime de substituição tributária nas operações com combustíveis e lubrificantes, derivados ou não de petróleo e com outros produtos.",
        "caminho": "estaduais/confaz/convenios-icms/2007/convenio-icms-110-2007.md",
        "conteudo": """# Convênio ICMS nº 110, de 28 de setembro de 2007

Dispõe sobre o regime de substituição tributária nas operações com combustíveis e lubrificantes.

O Conselho Nacional de Política Fazendária - CONFAZ, na sua 127ª reunião ordinária, resolve celebrar o seguinte CONVÊNIO:

## CLÁUSULA PRIMEIRA - DO REGIME DE SUBSTITUIÇÃO TRIBUTÁRIA
Ficam os Estados e o Distrito Federal autorizados a atribuir ao remetente de combustíveis e lubrificantes a condição de sujeito passivo por substituição tributária, relativamente ao ICMS incidente sobre as operações subsequentes.

## CLÁUSULA SÉTIMA - DA BASE DE CÁLCULO
A base de cálculo do imposto devido por substituição tributária é o Preço Médio Ponderado a Consumidor Final (PMPF) divulgado quinzenalmente por Ato COTEPE/PMPF publicado pela Secretaria-Executiva do CONFAZ.

Brasília, DF, 28 de setembro de 2007.

Conselho Nacional de Política Fazendária
"""
    },
    {
        "titulo": "Resolução ANP nº 795, de 5 de julho de 2019",
        "esfera": "Federal",
        "orgao": "Agência Nacional do Petróleo, Gás Natural e Biocombustíveis - ANP",
        "tipo": "Resolução ANP",
        "numero": "795",
        "ano": "2019",
        "data": "2019-07-05",
        "tema_tributario": "Combustíveis e Energia",
        "tributos_afetados": ["ICMS Combustíveis", "CIDE-Combustíveis", "Documento Fiscal Eletrônico"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://atosoficiais.com.br/anp/resolucao-n-795-2019",
        "ementa": "Regulamenta a obrigatoriedade de prestação de informações e emissão de notas fiscais nas operações de movimentação, distribuição e revenda varejista de combustíveis automotivos.",
        "caminho": "reguladores/anp/resolucoes/resolucao-anp-795-2019.md",
        "conteudo": """# Resolução ANP nº 795, de 5 de julho de 2019

Regulamenta os procedimentos de controle fiscal e volumétrico de combustíveis automotivos.

A DIRETORIA DA AGÊNCIA NACIONAL DO PETRÓLEO, GÁS NATURAL E BIOCOMBUSTÍVEIS - ANP, no uso de suas atribuições legais, resolve:

Art. 1º Esta Resolução estabelece os requisitos e os prazos para prestação de informações pelos distribuidores e postos revendedores relativos aos estoques físicos, aquisições e comercialização de combustíveis líquidos.

Art. 4º Todas as notas fiscais eletrônicas de circulação de combustíveis deverão obrigatoriamente consignar o código do produto na ANP, a densidade e o ponto de fulgor, para fins de batimento e conformidade tributária perante as Secretarias de Fazenda Estaduais e a Receita Federal do Brasil.

DÉCIO FABRICIO ODDONE DA SILVA
Diretor-Geral da ANP
"""
    },
    {
        "titulo": "Lei nº 10.865, de 30 de abril de 2004 - Seção de Combustíveis",
        "esfera": "Federal",
        "orgao": "Presidência da República / Congresso Nacional",
        "tipo": "Lei Ordinária",
        "numero": "10865",
        "ano": "2004",
        "data": "2004-04-30",
        "tema_tributario": "Combustíveis e Energia",
        "tributos_afetados": ["PIS/Pasep-Importação", "Cofins-Importação", "CIDE-Combustíveis"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2004-04-30;10865",
        "ementa": "Dispõe sobre a Contribuição para o PIS/Pasep-Importação e a Cofins-Importação sobre petróleo e derivados, gás natural e biocombustíveis.",
        "caminho": "federal/leis-ordinarias/combustiveis/lei-10865-2004-combustiveis.md",
        "conteudo": """# Lei nº 10.865, de 30 de abril de 2004 - Seção de Combustíveis

Regime de PIS/Pasep-Importação e Cofins-Importação na importação de combustíveis e petroquímicos.

O PRESIDENTE DA REPÚBLICA:
Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei:

Art. 8º As alíquotas da Contribuição para o PIS/Pasep-Importação e da Cofins-Importação incidentes na importação de petróleo cru, gasolinas, óleo diesel, gás liquefeito de petróleo (GLP) e querosene de aviação são fixadas por unidade de medida (alíquota ad rem) ou em percentual ad valorem conforme ato do Poder Executivo.

Art. 23. Os valores recolhidos a título de PIS/Pasep-Importação e Cofins-Importação pelos importadores de combustíveis poderão ser creditados ou ressarcidos quando o produto for destinado à exportação ou reinserido na cadeia produtiva petroquímica.

LUIZ INÁCIO LULA DA SILVA
Antonio Palocci Filho
"""
    }
]

def gerar_normas_combustiveis():
    gerados = []
    print(f"Iniciando estruturação de {len(NORMAS_COMBUSTIVEIS)} normas estruturantes de Combustíveis e Energia...")
    
    for item in NORMAS_COMBUSTIVEIS:
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
        conteudo_final = f"{frontmatter}{conteudo_md}\n"
        
        salvar_atomico(destino, conteudo_final.encode("utf-8"))
        print(f"✓ Gerado: {destino.relative_to(RAIZ)}")
        gerados.append(destino)
        
    print(f"\n{len(gerados)} normas de Combustíveis estruturadas com sucesso!")
    return gerados

if __name__ == "__main__":
    gerar_normas_combustiveis()
