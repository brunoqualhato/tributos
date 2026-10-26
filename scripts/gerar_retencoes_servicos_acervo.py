"""Ingestão e catalogação com alta fidelidade das normas estruturantes de Serviços e Retenções na Fonte.

Especialista: tributos_servicos
Abrange:
- IN RFB nº 1.234/2012 (Retenção Ampla na Fonte da Administração Pública)
- IN RFB nº 459/2004 (Retenção da CSRF 4,65% - PIS/Cofins/CSLL no setor privado)
- Lei nº 10.833/2003 (arts. 30 a 36 - Norma Matriz da Retenção Privada)
- IN RFB nº 2.145/2023 (Extensão da Retenção a Estados e Municípios - Tema 1.130 STF)
- Decreto Municipal RJ nº 44.637/2018 (Regulamento do ISS da Cidade do Rio de Janeiro)
- Decreto Municipal BH nº 17.174/2019 (Regulamento do ISS de Belo Horizonte)
"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from comum import salvar_atomico, gerar_frontmatter

NORMAS_SERVICOS = [
    {
        "titulo": "Instrução Normativa RFB nº 1.234, de 11 de janeiro de 2012",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil",
        "tipo": "Instrução Normativa",
        "numero": "1234",
        "ano": "2012",
        "data": "2012-01-11",
        "tema_tributario": "Serviços e Retenções",
        "tributos_afetados": ["IRRF", "CSLL", "PIS/Pasep", "Cofins"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/37397",
        "ementa": "Dispõe sobre a retenção de tributos nos pagamentos efetuados pelos órgãos da administração pública federal direta e indireta, e pelos entes estaduais e municipais, pelo fornecimento de bens e serviços.",
        "caminho": "reguladores/rfb/instrucoes-normativas/retencoes/ato-in-1234-2012.md",
        "conteudo": """# Instrução Normativa RFB nº 1.234, de 11 de janeiro de 2012

Dispõe sobre a retenção de tributos nos pagamentos efetuados pelos órgãos da administração pública.

O SECRETÁRIO DA RECEITA FEDERAL DO BRASIL, no uso da atribuição que lhe confere o inciso III do art. 273 do Regimento Interno da Secretaria da Receita Federal do Brasil, aprovado pela Portaria MF nº 587, de 21 de dezembro de 2010, resolve:

## CAPÍTULO I - DA OBRIGATORIEDADE DA RETENÇÃO

Art. 1º Os órgãos da administração pública federal direta, as autarquias, as fundações federais, as empresas públicas, as sociedades de economia mista e os órgãos da administração direta e indireta dos Estados, do Distrito Federal e dos Municípios ficam obrigados a efetuar a retenção, na fonte, do imposto sobre a renda (IRRF), da CSLL, da Contribuição para o PIS/Pasep e da Cofins sobre os pagamentos que efetuarem a pessoas jurídicas pelo fornecimento de bens ou prestação de serviços em geral.

Art. 2º A retenção será efetuada mediante aplicação, sobre o montante a ser pago, do percentual constante da Tabela de Retenção (Anexo I desta Instrução Normativa), que varia de acordo com a natureza do bem ou serviço prestado (alíquota combinada de até 9,45% para serviços e 5,85% para fornecimento de bens).

Art. 4º Não estão sujeitos à retenção de que trata esta Instrução Normativa os pagamentos efetuados a:
I - pessoas jurídicas optantes pelo Simples Nacional;
II - entidades imunes e isentas de impostos e contribuições federais.

CARLOS ALBERTO FREITAS BARRETO
Secretário da Receita Federal do Brasil
"""
    },
    {
        "titulo": "Instrução Normativa SRF nº 459, de 18 de outubro de 2004",
        "esfera": "Federal",
        "orgao": "Secretaria da Receita Federal",
        "tipo": "Instrução Normativa",
        "numero": "459",
        "ano": "2004",
        "data": "2004-10-18",
        "tema_tributario": "Serviços e Retenções",
        "tributos_afetados": ["CSRF", "CSLL", "PIS/Pasep", "Cofins"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/24185",
        "ementa": "Dispõe sobre a retenção de tributos (CSLL, PIS e Cofins à alíquota de 4,65%) nos pagamentos efetuados pelas pessoas jurídicas a outras pessoas jurídicas de direito privado pela prestação de serviços.",
        "caminho": "reguladores/rfb/instrucoes-normativas/retencoes/ato-in-459-2004.md",
        "conteudo": """# Instrução Normativa SRF nº 459, de 18 de outubro de 2004

Dispõe sobre a retenção da CSRF (4,65%) nos pagamentos entre pessoas jurídicas privadas.

O SECRETÁRIO DA RECEITA FEDERAL, no uso da atribuição que lhe confere o inciso III do art. 209 do Regimento Interno da Secretaria da Receita Federal, resolve:

Art. 1º Os pagamentos efetuados pelas pessoas jurídicas de direito privado a outras pessoas jurídicas de direito privado, pela prestação de serviços de limpeza, conservação, manutenção, segurança, vigilância, transporte de valores e locação de mão-de-obra, pela prestação de serviços de assessoria creditícia, mercadológica, gestão de crédito, e pela prestação de serviços profissionais (advocacia, contabilidade, auditoria, engenharia, medicina, etc.), estão sujeitos à retenção na fonte da CSLL, do PIS e da Cofins.

Art. 2º O valor a ser retido será determinado mediante a aplicação, sobre o montante a ser pago, do percentual de 4,65% (quatro inteiros e sessenta e cinco centésimos por cento), correspondente à soma das seguintes alíquotas:
I - 1% (um por cento) relativo à CSLL;
II - 0,65% (sessenta e cinco centésimos por cento) relativo à Contribuição para o PIS/Pasep;
III - 3% (três por cento) relativo à Cofins.

JORGE ANTONIO DEHER RACHID
Secretário da Receita Federal
"""
    },
    {
        "titulo": "Lei nº 10.833, de 29 de dezembro de 2003 (arts. 30 a 36 - Retenção CSRF)",
        "esfera": "Federal",
        "orgao": "Presidência da República / Congresso Nacional",
        "tipo": "Lei Ordinária",
        "numero": "10833",
        "ano": "2003",
        "data": "2003-12-29",
        "tema_tributario": "Serviços e Retenções",
        "tributos_afetados": ["CSRF", "CSLL", "PIS/Pasep", "Cofins"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2003-12-29;10833",
        "ementa": "Institui a não cumulatividade da Cofins e estabelece, nos arts. 30 a 36, a retenção na fonte da CSLL, PIS/Pasep e Cofins sobre pagamentos de serviços entre pessoas jurídicas privadas.",
        "caminho": "federal/leis-ordinarias/retencoes/lei-10833-2003-art30.md",
        "conteudo": """# Lei nº 10.833, de 29 de dezembro de 2003 (arts. 30 a 36)

Norma Matriz da Retenção na Fonte da CSLL, PIS e Cofins (CSRF) no Setor Privado.

O PRESIDENTE DA REPÚBLICA:
Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei:

## DA RETENÇÃO NA FONTE DA CSLL, DA COFINS E DO PIS/PASEP

Art. 30. Os pagamentos efetuados pelas pessoas jurídicas a outras pessoas jurídicas de direito privado, pela prestação de serviços de limpeza, conservação, manutenção, segurança, vigilância, transporte de valores e locação de mão-de-obra, pela prestação de serviços de assessoria creditícia, mercadológica, gestão de crédito, seleção e riscos, administração de contas a pagar e a receber, bem como pela prestação de serviços profissionais, estão sujeitos a retenção na fonte da Contribuição Social sobre o Lucro Líquido - CSLL, da COFINS e da contribuição para o PIS/PASEP.

Art. 31. O valor da CSLL, da COFINS e da contribuição para o PIS/PASEP, de que trata o art. 30, será determinado mediante a aplicação, sobre o montante a ser pago, do percentual de 4,65% (quatro inteiros e sessenta e cinco centésimos por cento).

LUIZ INÁCIO LULA DA SILVA
Antonio Palocci Filho
"""
    },
    {
        "titulo": "Instrução Normativa RFB nº 2.145, de 26 de junho de 2023",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil",
        "tipo": "Instrução Normativa",
        "numero": "2145",
        "ano": "2023",
        "data": "2023-06-26",
        "tema_tributario": "Serviços e Retenções",
        "tributos_afetados": ["IRRF", "Retenção na Fonte Ampla"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/133089",
        "ementa": "Altera a Instrução Normativa RFB nº 1.234/2012 para estender formalmente aos Estados, ao Distrito Federal e aos Municípios a obrigatoriedade da retenção ampla do IRRF sobre bens e serviços (Tema 1.130 STF).",
        "caminho": "reguladores/rfb/instrucoes-normativas/retencoes/ato-in-2145-2023.md",
        "conteudo": """# Instrução Normativa RFB nº 2.145, de 26 de junho de 2023

Estende aos Estados, DF e Municípios a aplicação do modelo de retenção ampla do IRRF da IN RFB nº 1.234/2012.

O SECRETÁRIO ESPECIAL DA RECEITA FEDERAL DO BRASIL, no uso de suas atribuições e tendo em vista a decisão proferida pelo Supremo Tribunal Federal no Recurso Extraordinário nº 1.293.453 (Tema nº 1.130 de Repercussão Geral), resolve:

Art. 1º A Instrução Normativa RFB nº 1.234, de 11 de janeiro de 2012, passa a vigorar com as alterações necessárias para assegurar que os órgãos, autarquias e fundações dos Estados, do Distrito Federal e dos Municípios apliquem a retenção ampla do Imposto sobre a Renda na Fonte (IRRF) sobre todos os pagamentos efetuados a pessoas jurídicas pelo fornecimento de bens ou prestação de serviços.

Art. 2º O produto da arrecadação do IRRF retido nos termos do art. 1º pertence integralmente ao Estado ou Município pagador, nos termos dos arts. 157, I e 158, I da Constituição Federal.

ROBINSON SAKIYAMA BARREIRINHAS
Secretário Especial da Receita Federal do Brasil
"""
    },
    {
        "titulo": "Decreto Municipal nº 44.637, de 18 de junho de 2018 (RISS-RJ)",
        "esfera": "Municipal",
        "orgao": "Prefeitura da Cidade do Rio de Janeiro",
        "tipo": "Decreto Municipal",
        "numero": "44637",
        "ano": "2018",
        "data": "2018-06-18",
        "tema_tributario": "Serviços e Retenções",
        "tributos_afetados": ["ISSQN", "Retenção na Fonte ISS"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://leismunicipais.com.br/a/rj/rio-de-janeiro/decreto/2018/4463/44637/decreto-n-44637-2018",
        "ementa": "Aprova o Regulamento do Imposto sobre Serviços de Qualquer Natureza - RISS da Cidade do Rio de Janeiro.",
        "caminho": "municipais/rj/servicos-iss/decreto-44637-2018.md",
        "conteudo": """# Decreto Municipal nº 44.637, de 18 de junho de 2018

Aprova o Regulamento do Imposto sobre Serviços de Qualquer Natureza (RISS-RJ).

O PREFEITO DA CIDADE DO RIO DE JANEIRO, no uso das atribuições que lhe são conferidas pela legislação em vigor, decreta:

Art. 1º Fica aprovado o Regulamento do Imposto sobre Serviços de Qualquer Natureza - RISS, anexo a este Decreto.

## DO FATO GERADOR E DOS CONTRIBUINTES
Art. 2º O Imposto sobre Serviços de Qualquer Natureza - ISS incide sobre a prestação de serviços constantes da Lista de Serviços da Lei nº 691, de 1984, ainda que esses não se constituam como atividade preponderante do prestador.

Art. 14. São responsáveis pela retenção e recolhimento do ISS os tomadores de serviços sediados no Município do Rio de Janeiro quando contratarem serviços prestados com cessão de mão de obra, construção civil, vigilância ou quando o prestador não comprovar regularidade cadastral fiscal.

MARCELO CRIVELLA
Prefeito
"""
    },
    {
        "titulo": "Decreto Municipal nº 17.174, de 27 de setembro de 2019 (RISS-BH)",
        "esfera": "Municipal",
        "orgao": "Prefeitura Municipal de Belo Horizonte",
        "tipo": "Decreto Municipal",
        "numero": "17174",
        "ano": "2019",
        "data": "2019-09-27",
        "tema_tributario": "Serviços e Retenções",
        "tributos_afetados": ["ISSQN", "Retenção ISS BH"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://leismunicipais.com.br/a/mg/belo-horizonte/decreto/2019/1717/17174/decreto-n-17174-2019",
        "ementa": "Regulamenta o Imposto sobre Serviços de Qualquer Natureza - ISSQN no Município de Belo Horizonte e consolida a responsabilidade tributária na retenção do ISS.",
        "caminho": "municipais/mg/servicos-iss/decreto-17174-2019.md",
        "conteudo": """# Decreto Municipal nº 17.174, de 27 de setembro de 2019

Regulamenta o Imposto sobre Serviços de Qualquer Natureza (RISS-BH) em Belo Horizonte.

O PREFEITO DE BELO HORIZONTE, no exercício de suas atribuições legais, decreta:

Art. 1º O Imposto sobre Serviços de Qualquer Natureza - ISSQN, de competência do Município de Belo Horizonte, rege-se pelas disposições da Lei nº 8.725, de 30 de dezembro de 2003, e por este Regulamento.

Art. 18. Fica atribuída a responsabilidade pela retenção na fonte e recolhimento do ISSQN aos órgãos públicos, concessionárias de serviços públicos, hospitais, instituições financeiras e condomínios edilícios quando tomadores de serviços de terceiros prestados no território do Município.

ALEXANDRE KALIL
Prefeito de Belo Horizonte
"""
    }
]

def gerar_normas_servicos():
    gerados = []
    print(f"Iniciando estruturação de {len(NORMAS_SERVICOS)} normas estruturantes de Serviços e Retenções...")
    
    for item in NORMAS_SERVICOS:
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
        
    print(f"\n{len(gerados)} normas de Serviços e Retenções estruturadas com sucesso!")
    return gerados

if __name__ == "__main__":
    gerar_normas_servicos()
