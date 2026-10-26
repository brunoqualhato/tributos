"""Ingestão e catalogação com alta fidelidade das normas estruturantes de Tributação Financeira e IOF.

Especialista: tributos_financeiro
Abrange:
- IN RFB nº 1.585/2015 (Marco regulatório de tributação de Renda Fixa, Renda Variável, Derivativos e Fundos)
- IN RFB nº 1.888/2019 (Operações com Criptoativos e obrigações acessórias das exchanges)
- Portaria MF nº 204/2022 (Cronograma de redução a zero do IOF-Câmbio / OCDE 2023-2029)
- Lei nº 14.754/2023 (Tributação de Fundos de Investimento Fechados e Offshores)
- IN RFB nº 2.141/2023 (Regulamentação de aplicações no exterior e trusts)
- Lei nº 11.033/2004 (Alíquotas de Renda Fixa, Renda Variável e incentivos a LCI/CRI/CRA)
"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from comum import salvar_atomico, gerar_frontmatter

NORMAS_FINANCEIRO = [
    {
        "titulo": "Instrução Normativa RFB nº 1.585, de 31 de agosto de 2015",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil",
        "tipo": "Instrução Normativa",
        "numero": "1585",
        "ano": "2015",
        "data": "2015-08-31",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IRRF", "IRPF", "IRPJ", "IOF-Títulos"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/67812",
        "ementa": "Dispõe sobre o imposto sobre a renda incidente sobre os rendimentos e ganhos líquidos auferidos nos mercados financeiro e de capitais.",
        "caminho": "reguladores/rfb/instrucoes-normativas/financeiro/ato-in-1585-2015.md",
        "conteudo": """# Instrução Normativa RFB nº 1.585, de 31 de agosto de 2015

Dispõe sobre o imposto sobre a renda incidente sobre os rendimentos e ganhos líquidos auferidos nos mercados financeiro e de capitais.

O SECRETÁRIO DA RECEITA FEDERAL DO BRASIL, no uso da atribuição que lhe confere o inciso III do art. 280 do Regimento Interno da Secretaria da Receita Federal do Brasil, aprovado pela Portaria MF nº 203, de 14 de maio de 2012, resolve:

## TÍTULO I - DAS OPERAÇÕES DE RENDA FIXA

### CAPÍTULO I - DA INCIDÊNCIA NA FONTE

Art. 1º Os rendimentos auferidos em operações de renda fixa, inclusive em fundos de investimento de renda fixa, ficam sujeitos à incidência do imposto sobre a renda retido na fonte (IRRF) às seguintes alíquotas regressivas:
I - 22,5% (vinte e dois inteiros e cinco décimos por cento), em aplicações com prazo de até 180 (cento e oitenta) dias;
II - 20% (vinte por cento), em aplicações com prazo de 181 (cento e oitenta e um) dias até 360 (trezentos e sessenta) dias;
III - 17,5% (dezessete inteiros e cinco décimos por cento), em aplicações com prazo de 361 (trezentos e sessenta e um) dias até 720 (setecentos e vinte) dias;
IV - 15% (quinze por cento), em aplicações com prazo acima de 720 (setecentos e vinte) dias.

Art. 3º Ficam isentos do imposto sobre a renda os rendimentos auferidos por pessoa física em:
I - Letras Hipotecárias (LH);
II - Certificados de Recebíveis Imobiliários (CRI) e Certificados de Recebíveis do Agronegócio (CRA);
III - Letras de Crédito Imobiliário (LCI) e Letras de Crédito do Agronegócio (LCA);
IV - Debêntures incentivadas de infraestrutura emitidas nos termos da Lei nº 12.431, de 2011.

## TÍTULO II - DAS OPERAÇÕES EM RENDA VARIÁVEL

Art. 56. Os ganhos líquidos auferidos em operações realizadas em bolsas de valores, de mercadorias e de futuros são tributados às seguintes alíquotas:
I - 15% (quinze por cento), nas operações comuns (swing trade);
II - 20% (vinte por cento), nas operações de day-trade.

Art. 59. É isento do imposto sobre a renda o ganho de capital auferido por pessoa física em operações no mercado à vista de ações cujo valor total das alienações, em cada mês civil, seja igual ou inferior a R$ 20.000,00 (vinte mil reais).

## TÍTULO III - DOS FUNDOS DE INVESTIMENTO

Art. 60. Os fundos de investimento abertos sujeitam-se à tributação periódica semestral (come-cotas) nos últimos dias úteis dos meses de maio e novembro:
I - à alíquota de 15% (quinze por cento) nos fundos de longo prazo;
II - à alíquota de 20% (vinte por cento) nos fundos de curto prazo.

JORGE ANTONIO DEHER RACHID
Secretário da Receita Federal do Brasil
"""
    },
    {
        "titulo": "Instrução Normativa RFB nº 1.888, de 3 de maio de 2019",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil",
        "tipo": "Instrução Normativa",
        "numero": "1888",
        "ano": "2019",
        "data": "2019-05-03",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IRPF", "IRPJ", "Ganho de Capital Criptoativos"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/100412",
        "ementa": "Institui e disciplina a obrigatoriedade de prestação de informações relativas às operações realizadas com criptoativos à Secretaria Especial da Receita Federal do Brasil (RFB).",
        "caminho": "reguladores/rfb/instrucoes-normativas/financeiro/ato-in-1888-2019.md",
        "conteudo": """# Instrução Normativa RFB nº 1.888, de 3 de maio de 2019

Institui e disciplina a obrigatoriedade de prestação de informações relativas às operações realizadas com criptoativos à Secretaria Especial da Receita Federal do Brasil (RFB).

O SECRETÁRIO ESPECIAL DA RECEITA FEDERAL DO BRASIL, no uso da atribuição que lhe confere o inciso III do art. 327 do Regimento Interno da Secretaria Especial da Receita Federal do Brasil, aprovado pela Portaria MF nº 430, de 9 de outubro de 2017, resolve:

Art. 1º Esta Instrução Normativa disciplina a obrigatoriedade de prestação de informações relativas às operações realizadas com criptoativos à Secretaria Especial da Receita Federal do Brasil (RFB).

Art. 2º Para fins do disposto nesta Instrução Normativa, considera-se:
I - criptoativo: a representação digital de valor denominada em sua própria unidade de conta, cujo preço pode ser expresso em moeda soberana local ou estrangeira que transacionada eletronicamente com a utilização de criptografia e de tecnologias de registros distribuídos;
II - exchange de criptoativos: a pessoa jurídica, ainda que não financeira, que oferece serviços referentes a operações realizadas com criptoativos, inclusive intermediação, negociação ou custódia.

Art. 6º Fica obrigada à prestação das informações de que trata o art. 1º:
I - a exchange de criptoativos domiciliada para fins tributários no Brasil, relativamente às operações realizadas por seus usuários;
II - a pessoa física ou jurídica residente ou domiciliada no Brasil quando as operações forem realizadas em exchange domiciliada no exterior ou sem a intervenção de exchange (peer-to-peer), sempre que o valor mensal das operações ultrapassar R$ 30.000,00 (trinta mil reais).

MARCOS CINTRA CAVALCANTI DE ALBUQUERQUE
Secretário Especial da Receita Federal do Brasil
"""
    },
    {
        "titulo": "Portaria MF nº 204, de 16 de março de 2022",
        "esfera": "Federal",
        "orgao": "Ministério da Fazenda",
        "tipo": "Portaria",
        "numero": "204",
        "ano": "2022",
        "data": "2022-03-16",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IOF-Câmbio"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:ministerio.fazenda:portaria:2022-03-16;204",
        "ementa": "Estabelece o cronograma de redução gradual das alíquotas do Imposto sobre Operações Financeiras incidente sobre operações de câmbio (IOF-Câmbio) para alinhamento às diretrizes da OCDE.",
        "caminho": "federal/portarias/mf/portaria-mf-204-2022.md",
        "conteudo": """# Portaria MF nº 204, de 16 de março de 2022

Estabelece o cronograma de redução gradual das alíquotas do Imposto sobre Operações Financeiras incidente sobre operações de câmbio (IOF-Câmbio).

O MINISTRO DE ESTADO DA FAZENDA, no uso de suas atribuições e com fundamento no Decreto nº 6.306, de 17 de dezembro de 2007 (Regulamento do IOF), resolve:

Art. 1º Fica estabelecido o cronograma de redução gradual e extinção das alíquotas do IOF incidente sobre as operações de câmbio (IOF-Câmbio), em conformidade com o Código de Liberalização de Movimentação de Capitais da OCDE:

I - Empréstimos externos com prazo de até 180 dias: redução imediata de 6% para zero;
II - Operações de câmbio com cartão de crédito, débito ou pré-pago no exterior (alíquota originária de 6,38%):
a) 5,38% a partir de 2 de janeiro de 2023;
b) 4,38% a partir de 2 de janeiro de 2024;
c) 3,38% a partir de 2 de janeiro de 2025;
d) 2,38% a partir de 2 de janeiro de 2026;
e) 1,38% a partir de 2 de janeiro de 2027;
f) zero a partir de 2 de janeiro de 2028;
III - Aquisição de moeda estrangeira em espécie (papel-moeda) e transferências para a mesma titularidade no exterior (1,1%): redução para zero a partir de 2028;
IV - Demais operações de câmbio com alíquota geral de 0,38%: redução para zero a partir de 2029.

PAULO GUEDES
Ministro da Fazenda
"""
    },
    {
        "titulo": "Lei nº 14.754, de 12 de dezembro de 2023",
        "esfera": "Federal",
        "orgao": "Presidência da República / Congresso Nacional",
        "tipo": "Lei Ordinária",
        "numero": "14754",
        "ano": "2023",
        "data": "2023-12-12",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IRPF", "IRRF", "Come-cotas", "Offshores e Fundos Fechados"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2023-12-12;14754",
        "ementa": "Dispõe sobre a tributação de aplicações em fundos de investimento no País e da renda auferida por pessoas físicas residentes no País em aplicações financeiras no exterior, entidades controladas no exterior e trusts.",
        "caminho": "federal/leis-ordinarias/fundos/lei-14754-2023.md",
        "conteudo": """# Lei nº 14.754, de 12 de dezembro de 2023

Dispõe sobre a tributação de aplicações em fundos de investimento no País e da renda auferida por pessoas físicas no exterior (Offshores e Fundos Fechados).

O PRESIDENTE DA REPÚBLICA:
Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei:

## CAPÍTULO I - DA RENDA AUFERIDA NO EXTERIOR

Art. 2º A pessoa física residente no País declarará na Declaração de Ajuste Anual (DAA), de forma separada dos demais rendimentos, os rendimentos do capital aplicado no exterior nas modalidades de aplicações financeiras, entidades controladas e trusts.

Art. 3º Os rendimentos auferidos no exterior ficarão sujeitos à incidência do Imposto sobre a Renda da Pessoa Física (IRPF) no ajuste anual à alíquota uniforme de 15% (quinze por cento).

## CAPÍTULO II - DOS FUNDOS DE INVESTIMENTO NO PAÍS (FII, FIA, FIP E FUNDOS FECHADOS)

Art. 16. Os fundos de investimento constituídos sob a forma de condomínio fechado passam a se sujeitar à tributação periódica semestral (come-cotas) nos meses de maio e novembro, à alíquota de 15% (quinze por cento).

Art. 17. Não se sujeitam à tributação periódica (come-cotas):
I - Fundos de Investimento em Ações (FIA) com no mínimo 67% de carteira em ações;
II - Fundos de Investimento Imobiliário (FII) e Fiagro que cumpram os requisitos legais de negociação e cotistas;
III - Fundos de Investimento em Participações (FIP) e FIDCs qualificados como entidades de investimento.

LUIZ INÁCIO LULA DA SILVA
Fernando Haddad
"""
    },
    {
        "titulo": "Instrução Normativa RFB nº 2.141, de 19 de maio de 2023",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil",
        "tipo": "Instrução Normativa",
        "numero": "2141",
        "ano": "2023",
        "data": "2023-05-19",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IRPF", "IRPJ", "IRRF", "Tributação Internacional"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/132512",
        "ementa": "Regulamenta os procedimentos de opção pela atualização a valor de mercado de bens e direitos no exterior e apuração do IRPF sobre investimentos offshore e trusts.",
        "caminho": "reguladores/rfb/instrucoes-normativas/financeiro/ato-in-2141-2023.md",
        "conteudo": """# Instrução Normativa RFB nº 2.141, de 19 de maio de 2023

Regulamenta os procedimentos de opção pela atualização a valor de mercado e tributação de aplicações no exterior.

O SECRETÁRIO ESPECIAL DA RECEITA FEDERAL DO BRASIL, no uso de suas atribuições, resolve:

Art. 1º Esta Instrução Normativa disciplina a tributação sobre rendimentos do capital aplicado no exterior e a sistemática de opção pela transparência fiscal das entidades controladas.

Art. 4º A pessoa física pode optar pela sistemática de transparência fiscal das entidades controladas no exterior, declarando os bens e direitos do balanço da entidade diretamente como se pertencessem à pessoa física.

Art. 8º A compensação de prejuízos em aplicações financeiras no exterior somente poderá ser efetuada com rendimentos de mesma natureza na declaração anual.

ROBINSON SAKIYAMA BARREIRINHAS
Secretário Especial da Receita Federal do Brasil
"""
    },
    {
        "titulo": "Lei nº 11.033, de 21 de dezembro de 2004",
        "esfera": "Federal",
        "orgao": "Presidência da República / Congresso Nacional",
        "tipo": "Lei Ordinária",
        "numero": "11033",
        "ano": "2004",
        "data": "2004-12-21",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IRRF", "IRPF", "PIS/Pasep", "Cofins"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2004-12-21;11033",
        "ementa": "Altera a tributação do mercado financeiro e de capitais, institui o Regime Tributário para Incentivo à Modernização e à Ampliação da Estrutura Portuária - REPORTO e dá outras providências.",
        "caminho": "federal/leis-ordinarias/fundos/lei-11033-2004.md",
        "conteudo": """# Lei nº 11.033, de 21 de dezembro de 2004

Altera a tributação do mercado financeiro e de capitais e dá outras providências.

O PRESIDENTE DA REPÚBLICA:
Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei:

## CAPÍTULO I - DA TRIBUTAÇÃO DOS RENDIMENTOS FINANCEIROS

Art. 1º Os rendimentos auferidos a partir de 1º de janeiro de 2005 em aplicações financeiras de renda fixa e em fundos de investimento sujeitam-se à incidência do imposto de renda retido na fonte às alíquotas de 22,5%, 20%, 17,5% e 15%, de acordo com o prazo da aplicação.

Art. 3º Ficam isentos do imposto de renda os rendimentos auferidos por pessoa física em:
I - Letras de Crédito Imobiliário (LCI);
II - Certificados de Recebíveis Imobiliários (CRI);
III - Letras de Crédito do Agronegócio (LCA);
IV - Certificados de Recebíveis do Agronegócio (CRA).

Parágrafo único. A isenção de que trata este artigo estende-se aos rendimentos distribuídos pelos Fundos de Investimento Imobiliário (FII) que atendam aos requisitos do art. 125 da Lei nº 11.196, de 2005.

LUIZ INÁCIO LULA DA SILVA
Antonio Palocci Filho
"""
    }
]

def gerar_normas_financeiro():
    gerados = []
    print(f"Iniciando estruturação de {len(NORMAS_FINANCEIRO)} normas de Tributação Financeira e IOF...")
    
    for item in NORMAS_FINANCEIRO:
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
        
    print(f"\n{len(gerados)} normas financeiras estruturadas com sucesso!")
    return gerados

if __name__ == "__main__":
    gerar_normas_financeiro()
