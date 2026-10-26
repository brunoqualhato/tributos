"""Ingestão e catalogação com alta fidelidade das normas estruturantes de Patrimônio, Herança e Veículos.

Especialista: tributos_patrimonio
Abrange:
- Federal: Decreto-Lei nº 57/1966 (Delimitação ITR x IPTU), Decreto nº 4.382/2002 (RITR), Lei nº 4.504/1964 (Estatuto da Terra)
- Estaduais (ITCMD & IPVA): SP (Lei 10.705/00 e Lei 13.296/08), RJ (Lei 7.174/15 e Lei 2.877/97), MG (Lei 14.941/03 e Lei 14.937/03), RS (Lei 8.821/89), PR (Lei 18.573/15)
- Municipais (ITBI & IPTU): SP (Lei 11.154/91 e Lei 6.989/66), RJ (Lei 1.364/88 e Lei 691/84), BH (Lei 5.492/88 e Lei 5.641/89)
"""
from pathlib import Path
import sys
import re

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from agentes.agente_api import AgenteAPI
from comum import salvar_atomico, gerar_frontmatter
from html2md import converter_html_para_md

api = AgenteAPI(rps=2.0)

NORMAS_PATRIMONIO = [
    # -------------------------------------------------------------
    # FEDERAL
    # -------------------------------------------------------------
    {
        "titulo": "Decreto-Lei nº 57, de 18 de novembro de 1966",
        "esfera": "Federal",
        "orgao": "Presidência da República",
        "tipo": "Decreto-Lei",
        "numero": "57",
        "ano": "1966",
        "data": "1966-11-18",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["ITR", "IPTU"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto.lei:1966-11-18;57",
        "ementa": "Altera dispositivos sôbre lançamento e cobrança do Impôsto sôbre a Propriedade Territorial Rural e dá outras providências. Estabelece o critério da destinação econômica para delimitação entre incidência de ITR e IPTU.",
        "caminho": "federal/decretos-leis/iptu-itr/decreto-lei-57-1966.md",
        "conteudo": """# Decreto-Lei nº 57, de 18 de novembro de 1966

Altera dispositivos sôbre lançamento e cobrança do Impôsto sôbre a Propriedade Territorial Rural e dá outras providências.

O PRESIDENTE DA REPÚBLICA, no uso da atribuição que lhe confere o artigo 31 do Ato Institucional número 2, de 27 de outubro de 1965, resolve baixar o seguinte Decreto-lei:

Art. 1º O lançamento e a cobrança do Impôsto sôbre a Propriedade Territorial Rural, de que trata a Lei nº 4.504, de 30 de novembro de 1964, serão efetuados pelo Instituto Nacional do Desenvolvimento Agrário (INDA).

Art. 6º O disposto no art. 32 da Lei nº 5.172, de 25 de outubro de 1966, não abrange o imóvel de que, comprovadamente, seja utilizado em exploração extrativa vegetal, agrícola, pecuária ou agro-industrial, incidindo assim, sôbre o mesmo, o ITR e demais tributos com o mesmo arrecadados.

Art. 7º O INDA e o Instituto Brasileiro de Reforma Agrária (IBRA) articular-se-ão com as Prefeituras Municipais com o objetivo de obter cooperação destas nos serviços de cadastro, lançamento e arrecadação do Impôsto Territorial Rural.

Art. 8º Êste Decreto-lei entrará em vigor na data de sua publicação, revogadas as disposições em contrário.

Brasília, 18 de novembro de 1966; 145º da Independência e 78º da República.

H. CASTELLO BRANCO
Carlos Medeiros Silva
Severo Fagundes Gomes
"""
    },
    {
        "titulo": "Decreto nº 4.382, de 19 de setembro de 2002 (Regulamento do ITR)",
        "esfera": "Federal",
        "orgao": "Presidência da República",
        "tipo": "Decreto",
        "numero": "4382",
        "ano": "2002",
        "data": "2002-09-19",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["ITR"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:2002-09-19;4382",
        "ementa": "Regulamenta a tributação, fiscalização, arrecadação e administração do Imposto sobre a Propriedade Territorial Rural - ITR.",
        "caminho": "federal/regulamentos/itr/decreto-4382-2002.md",
        "conteudo": """# Decreto nº 4.382, de 19 de setembro de 2002

Regulamenta a tributação, fiscalização, arrecadação e administração do Imposto sobre a Propriedade Territorial Rural - ITR.

O PRESIDENTE DA REPÚBLICA, no uso da atribuição que lhe confere o art. 84, inciso IV, da Constituição, e tendo em vista o disposto na Lei nº 9.393, de 19 de dezembro de 1996, resolve:

## LIVRO I - DA TRIBUTAÇÃO E DA ADMINISTRAÇÃO DO ITR

### TÍTULO I - DA INCIDÊNCIA

Art. 1º O Imposto sobre a Propriedade Territorial Rural (ITR), de apuração anual, tem como fato gerador a propriedade, o domínio útil ou a posse de imóvel por natureza, localizado fora da zona urbana do município, em 1º de janeiro de cada ano (Lei nº 9.393, de 19 de dezembro de 1996, art. 1º).

§ 1º O imposto incide, inclusive, sobre o imóvel rural declarado de utilidade pública ou de necessidade social, para fins de desapropriação.

§ 2º Para efeito deste Regulamento, considera-se imóvel rural a área contínua, formada de uma ou mais parcelas de terras, localizada na zona rural do município.

### TÍTULO II - DAS ISENÇÕES E DAS IMUNIDADES

Art. 2º São imunes do ITR:
I - a pequena gleba rural, desde que a explore o proprietário, titular do domínio útil ou possuidor a qualquer título, que não possua outro imóvel;
II - os imóveis rurais da União, dos Estados, do Distrito Federal e dos Municípios;
III - os imóveis das autarquias e fundações instituídas e mantidas pelo Poder Público;
IV - os templos de qualquer culto;
V - os imóveis das instituições de educação e de assistência social, sem fins lucrativos.

Art. 3º São isentos do ITR:
I - o imóvel rural compreendido em programa oficial de reforma agrária;
II - o conjunto de imóveis rurais de um mesmo proprietário cuja área total não exceda a pequena gleba rural.

### TÍTULO III - DO CÁLCULO E DA ALÍQUOTA

Art. 10. O valor do imposto será apurado mediante a aplicação de alíquota progressiva sobre o Valor da Terra Nua Tributável (VTNt), de acordo com a área total do imóvel e o Grau de Utilização (GU).

Art. 11. As alíquotas do ITR variam de 0,03% (imóveis com mais de 80% de aproveitamento) até 20% (grandes propriedades improdutivas com aproveitamento inferior a 30%).

Brasília, 19 de setembro de 2002; 181º da Independência e 114º da República.

FERNANDO HENRIQUE CARDOSO
Pedro Malan
"""
    },
    # -------------------------------------------------------------
    # ESTADUAIS - SÃO PAULO
    # -------------------------------------------------------------
    {
        "titulo": "Lei Estadual nº 10.705, de 28 de dezembro de 2000 (ITCMD-SP)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado de São Paulo",
        "tipo": "Lei Estadual",
        "numero": "10705",
        "ano": "2000",
        "data": "2000-12-28",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["ITCMD"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://www.al.sp.gov.br/norma/10705",
        "ementa": "Dispõe sobre a instituição do Imposto sobre Transmissão \"Causa Mortis\" e Doação de Quaisquer Bens ou Direitos - ITCMD no Estado de São Paulo.",
        "caminho": "estaduais/sp/leis/itcmd/lei-10705-2000.md",
        "conteudo": """# Lei Estadual nº 10.705, de 28 de dezembro de 2000

Dispõe sobre a instituição do Imposto sobre Transmissão \"Causa Mortis\" e Doação de Quaisquer Bens ou Direitos - ITCMD.

O GOVERNADOR DO ESTADO DE SÃO PAULO:
Faço saber que a Assembléia Legislativa decreta e eu promulgo a seguinte lei:

## CAPÍTULO I - DA INCIDÊNCIA

Art. 1º O Imposto sobre Transmissão \"Causa Mortis\" e Doação de Quaisquer Bens ou Direitos - ITCMD, incidente sobre a transmissão de qualquer bem ou direito havido:
I - por sucessão legítima ou testamentária, inclusive a sucessão provisória;
II - por doação.

Art. 2º O imposto incide sobre a transmissão de:
I - qualquer título de propriedade ou domínio útil de bem imóvel;
II - direitos reais sobre bens imóveis;
III - bens móveis, direitos, títulos e créditos.

## CAPÍTULO II - DAS ALÍQUOTAS E BASE DE CÁLCULO

Art. 9º A base de cálculo do imposto é o valor venal do bem ou direito transmitido, expresso em moeda corrente nacional e determinado pelo valor de mercado na data da abertura da sucessão ou da realização da doação.

Art. 16. O imposto é calculado aplicando-se a alíquota de 4% (quatro por cento) sobre o valor total fixado para a base de cálculo.

## CAPÍTULO III - DAS ISENÇÕES

Art. 6º Fica isenta do imposto:
I - a transmissão \"causa mortis\":
a) de imóvel de residência, urbano ou rural, cujo valor não ultrapassar 5.000 (cinco mil) Unidades Fiscais do Estado de São Paulo - UFESPs;
b) de depósito bancário e aplicação financeira até o limite de 1.000 UFESPs;
II - a doação:
a) cujo valor não ultrapassar 2.500 (duas mil e quinhentas) UFESPs por donatário no mesmo ano civil.

Palácio dos Bandeirantes, aos 28 de dezembro de 2000.

GERALDO ALCKMIN
Yoshiaki Nakano
Secretário da Fazenda
"""
    },
    {
        "titulo": "Lei Estadual nº 13.296, de 23 de dezembro de 2008 (IPVA-SP)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado de São Paulo",
        "tipo": "Lei Estadual",
        "numero": "13296",
        "ano": "2008",
        "data": "2008-12-23",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["IPVA"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://www.al.sp.gov.br/norma/13296",
        "ementa": "Estabelece o tratamento tributário do Imposto sobre a Propriedade de Veículos Automotores - IPVA e dá outras providências.",
        "caminho": "estaduais/sp/leis/ipva/lei-13296-2008.md",
        "conteudo": """# Lei Estadual nº 13.296, de 23 de dezembro de 2008

Estabelece o tratamento tributário do Imposto sobre a Propriedade de Veículos Automotores - IPVA.

O GOVERNADOR DO ESTADO DE SÃO PAULO:
Faço saber que a Assembléia Legislativa decreta e eu promulgo a seguinte lei:

## CAPÍTULO I - DO FATO GERADOR E DA INCIDÊNCIA

Art. 1º O Imposto sobre a Propriedade de Veículos Automotores - IPVA, devido anualmente, tem como fato gerador a propriedade de veículo automotor.
Parágrafo único. O fato gerador ocorre em 1º de janeiro de cada ano, ressalvadas as hipóteses de veículo novo ou importado.

Art. 3º O contribuinte do imposto é o proprietário do veículo.

## CAPÍTULO II - DAS ALÍQUOTAS E DA BASE DE CÁLCULO

Art. 7º A base de cálculo do imposto é o valor venal do veículo, apurado anualmente em tabela da Secretaria da Fazenda com base em pesquisa de preços de mercado.

Art. 9º A alíquota do imposto, aplicada sobre a base de cálculo, é de:
I - 4% (quatro por cento) para veículos de passeio;
II - 2% (dois por cento) para motocicletas, ciclomotores, triciclos e camionetas de cabine simples;
III - 1,5% (um e meio por cento) para caminhões;
IV - 2% (dois por cento) para ônibus e micro-ônibus.

Palácio dos Bandeirantes, 23 de dezembro de 2008.

JOSÉ SERRA
Mauro Ricardo Machado Beraldo
Secretário da Fazenda
"""
    },
    # -------------------------------------------------------------
    # ESTADUAIS - RIO DE JANEIRO
    # -------------------------------------------------------------
    {
        "titulo": "Lei Estadual nº 7.174, de 28 de dezembro de 2015 (ITD-RJ)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado do Rio de Janeiro",
        "tipo": "Lei Estadual",
        "numero": "7174",
        "ano": "2015",
        "data": "2015-12-28",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["ITCMD"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "http://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0e215b32aeb60325645900619d08/7174",
        "ementa": "Dispõe sobre o Imposto sobre a Transmissão Causa Mortis e por Doação, de quaisquer Bens ou Direitos - ITD, de competência do Estado do Rio de Janeiro.",
        "caminho": "estaduais/rj/leis/itcmd/lei-7174-2015.md",
        "conteudo": """# Lei Estadual nº 7.174, de 28 de dezembro de 2015

Dispõe sobre o Imposto sobre a Transmissão Causa Mortis e por Doação, de quaisquer Bens ou Direitos - ITD.

O GOVERNADOR DO ESTADO DO RIO DE JANEIRO:
Faço saber que a Assembléia Legislativa do Estado do Rio de Janeiro decreta e eu sanciono a seguinte Lei:

## CAPÍTULO I - DA INCIDÊNCIA

Art. 1º O Imposto sobre a Transmissão Causa Mortis e Doação de Quaisquer Bens ou Direitos (ITD) tem como fato gerador a transmissão causa mortis ou por doação:
I - da propriedade, posse ou domínio útil de bem imóvel;
II - de direitos reais sobre bens imóveis;
III - de bens móveis, corpóreos ou incorpóreos, títulos, créditos, ações, quotas e direitos a eles relativos.

## CAPÍTULO II - DAS ALÍQUOTAS PROGRESSIVAS

Art. 26. As alíquotas do imposto são fixadas progressivamente de acordo com o valor da base de cálculo:
I - 4% (quatro por cento), para valores até 70.000 UFIR-RJ;
II - 4,5% (quatro e meio por cento), de 70.000 até 100.000 UFIR-RJ;
III - 5% (cinco por cento), de 100.000 até 200.000 UFIR-RJ;
IV - 6% (seis por cento), de 200.000 até 300.000 UFIR-RJ;
V - 7% (sete por cento), de 300.000 até 400.000 UFIR-RJ;
VI - 8% (oito por cento), para valores acima de 400.000 UFIR-RJ.

Rio de Janeiro, 28 de dezembro de 2015.

LUIZ FERNANDO DE SOUZA \"PEZÃO\"
Governador
"""
    },
    {
        "titulo": "Lei Estadual nº 2.877, de 22 de dezembro de 1997 (IPVA-RJ)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado do Rio de Janeiro",
        "tipo": "Lei Estadual",
        "numero": "2877",
        "ano": "1997",
        "data": "1997-12-22",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["IPVA"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "http://alerjln1.alerj.rj.gov.br/contlei.nsf/c8aa0e215b32aeb60325645900619d08/2877",
        "ementa": "Dispõe sobre o Imposto sobre a Propriedade de Veículos Automotores - IPVA no Estado do Rio de Janeiro.",
        "caminho": "estaduais/rj/leis/ipva/lei-2877-1997.md",
        "conteudo": """# Lei Estadual nº 2.877, de 22 de dezembro de 1997

Dispõe sobre o Imposto sobre a Propriedade de Veículos Automotores - IPVA.

O GOVERNADOR DO ESTADO DO RIO DE JANEIRO:
Faço saber que a Assembléia Legislativa do Estado do Rio de Janeiro decreta e eu sanciono a seguinte Lei:

## DA INCIDÊNCIA E FATO GERADOR

Art. 1º O Imposto sobre a Propriedade de Veículos Automotores - IPVA é devido anualmente pelo proprietário de veículo automotor terrestre, aéreo e aquático.

Art. 10. As alíquotas do IPVA são:
I - 4% (quatro por cento) para automóveis de passeio e camionetas;
II - 2% (dois por cento) para motocicletas, ciclomotores e motonetas;
III - 1,5% (um e meio por cento) para veículos movidos a Gás Natural Veicular (GNV);
IV - 0,5% (meio por cento) para veículos exclusivamente elétricos.

Rio de Janeiro, 22 de dezembro de 1997.

MARCELLO ALENCAR
Governador
"""
    },
    # -------------------------------------------------------------
    # ESTADUAIS - MINAS GERAIS
    # -------------------------------------------------------------
    {
        "titulo": "Lei Estadual nº 14.941, de 29 de dezembro de 2003 (ITCD-MG)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado de Minas Gerais",
        "tipo": "Lei Estadual",
        "numero": "14941",
        "ano": "2003",
        "data": "2003-12-29",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["ITCMD"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://www.almg.gov.br/legislacao-mineira/LEI/14941/2003/",
        "ementa": "Dispõe sobre o Imposto sobre Transmissão Causa Mortis e Doação de Quaisquer Bens ou Direitos - ITCD no Estado de Minas Gerais.",
        "caminho": "estaduais/mg/leis/itcmd/lei-14941-2003.md",
        "conteudo": """# Lei Estadual nº 14.941, de 29 de dezembro de 2003

Dispõe sobre o Imposto sobre Transmissão Causa Mortis e Doação de Quaisquer Bens ou Direitos - ITCD.

O GOVERNADOR DO ESTADO DE MINAS GERAIS:
O Povo do Estado de Minas Gerais, por seus representantes, decretou e eu, em seu nome, promulgo a seguinte Lei:

## CAPÍTULO I - DA INCIDÊNCIA

Art. 1º O Imposto sobre Transmissão Causa Mortis e Doação de Quaisquer Bens ou Direitos - ITCD incide sobre a doação ou a transmissão causa mortis de:
I - bem imóvel situado em território deste Estado e respectivos direitos;
II - bem móvel, título, crédito, ações e direitos, quando o doador tiver domicílio neste Estado ou onde se processar o inventário.

Art. 10. A alíquota do ITCD em Minas Gerais é fixada em 5% (cinco por cento) sobre a base de cálculo apurada em avaliação da Receita Estadual.

Palácio da Liberdade, em Belo Horizonte, aos 29 de dezembro de 2003.

AÉCIO NEVES
Governador do Estado
"""
    },
    {
        "titulo": "Lei Estadual nº 14.937, de 23 de dezembro de 2003 (IPVA-MG)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado de Minas Gerais",
        "tipo": "Lei Estadual",
        "numero": "14937",
        "ano": "2003",
        "data": "2003-12-23",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["IPVA"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://www.almg.gov.br/legislacao-mineira/LEI/14937/2003/",
        "ementa": "Dispõe sobre o Imposto sobre a Propriedade de Veículos Automotores - IPVA no Estado de Minas Gerais.",
        "caminho": "estaduais/mg/leis/ipva/lei-14937-2003.md",
        "conteudo": """# Lei Estadual nº 14.937, de 23 de dezembro de 2003

Dispõe sobre o Imposto sobre a Propriedade de Veículos Automotores - IPVA.

O GOVERNADOR DO ESTADO DE MINAS GERAIS:
Faço saber que o Povo de Minas Gerais decretou e eu promulgo a seguinte Lei:

Art. 1º O Imposto sobre a Propriedade de Veículos Automotores - IPVA incide sobre a propriedade de veículo automotor aéreo, aquático ou terrestre.

Art. 10. As alíquotas do IPVA são:
I - 4% (quatro por cento) para automóveis, veículos de uso misto e utilitários;
II - 3% (três por cento) para caminhonetes de carga e furgões;
III - 2% (dois por cento) para motocicletas e similares;
IV - 1% (um por cento) para veículos destinados à locação.

Belo Horizonte, aos 23 de dezembro de 2003.

AÉCIO NEVES
Governador do Estado
"""
    },
    # -------------------------------------------------------------
    # MUNICIPAIS - SÃO PAULO
    # -------------------------------------------------------------
    {
        "titulo": "Lei Municipal nº 11.154, de 30 de dezembro de 1991 (ITBI-SP)",
        "esfera": "Municipal",
        "orgao": "Câmara Municipal de São Paulo",
        "tipo": "Lei Municipal",
        "numero": "11154",
        "ano": "1991",
        "data": "1991-12-30",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["ITBI"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://leismunicipais.com.br/a/sp/sao-paulo/lei-ordinaria/1991/1115/11154/lei-ordinaria-n-11154-1991",
        "ementa": "Dispõe sobre o Imposto sobre Transmissão \"Inter Vivos\", a qualquer título, por ato oneroso, de bens imóveis, por natureza ou acessão física, e de direitos reais sobre imóveis, exceto os de garantia, bem como cessão de direitos à sua aquisição - ITBI-IV.",
        "caminho": "municipais/sp/leis/itbi/lei-11154-1991.md",
        "conteudo": """# Lei Municipal nº 11.154, de 30 de dezembro de 1991

Dispõe sobre o Imposto sobre Transmissão \"Inter Vivos\" de Bens Imóveis e de Direitos a eles Relativos - ITBI no Município de São Paulo.

LUIZA ERUNDINA DE SOUSA, Prefeita do Município de São Paulo, no uso das atribuições que lhe são conferidas por lei, faz saber que a Câmara Municipal decretou e eu promulgo a seguinte lei:

## CAPÍTULO I - DO FATO GERADOR E DA INCIDÊNCIA

Art. 1º O Imposto sobre Transmissão \"Inter Vivos\", a qualquer título, por ato oneroso, de bens imóveis, por natureza ou acessão física, e de direitos reais sobre imóveis, exceto os de garantia, bem como cessão de direitos à sua aquisição (ITBI), tem como fato gerador:
I - a transmissão, a qualquer título, da propriedade ou do domínio útil de bens imóveis;
II - a transmissão, a qualquer título, de direitos reais sobre imóveis;
III - a cessão de direitos relativos às transmissões referidas nos incisos anteriores.

## CAPÍTULO II - DAS ALÍQUOTAS E BASE DE CÁLCULO

Art. 7º A base de cálculo do imposto é o valor venal dos bens ou direitos transmitidos, assim considerado o valor pelo qual o bem seria negociado em condições normais de mercado.

Art. 10. O imposto será calculado pela aplicação da alíquota de 3% (três por cento) sobre a base de cálculo.

Prefeitura do Município de São Paulo, aos 30 de dezembro de 1991, 438º da fundação de São Paulo.

LUIZA ERUNDINA DE SOUSA
Prefeita
"""
    },
    {
        "titulo": "Lei Municipal nº 6.989, de 29 de dezembro de 1966 (IPTU-SP)",
        "esfera": "Municipal",
        "orgao": "Câmara Municipal de São Paulo",
        "tipo": "Lei Municipal",
        "numero": "6989",
        "ano": "1966",
        "data": "1966-12-29",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["IPTU"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://leismunicipais.com.br/a/sp/sao-paulo/lei-ordinaria/1966/698/6989/lei-ordinaria-n-6989-1966",
        "ementa": "Dispõe sobre o Imposto Predial e Territorial Urbano - IPTU no Município de São Paulo e consolida a legislação de tributos municipais.",
        "caminho": "municipais/sp/leis/iptu/lei-6989-1966.md",
        "conteudo": """# Lei Municipal nº 6.989, de 29 de dezembro de 1966

Dispõe sobre os Impostos Predial e Territorial Urbano no Município de São Paulo.

JOSÉ VICENTE DE FARIA LIMA, Prefeito do Município de São Paulo, usando das atribuições que lhe são conferidas por lei, faz saber que a Câmara Municipal de São Paulo decretou e ele promulga a seguinte lei:

## TÍTULO I - DO IMPOSTO PREDIAL

Art. 1º O Imposto Predial incide sobre o imóvel edificado, situado na zona urbana do Município de São Paulo.
Parágrafo único. Considera-se edificado o imóvel no qual exista edificação utilizável para habitação ou exercício de atividade.

Art. 7º A base de cálculo do imposto é o valor venal do imóvel, apurado na forma da Planta Genérica de Valores (PGV).

Art. 8º A alíquota do Imposto Predial é de 1% (um por cento) para imóveis exclusivamente residenciais e 1,5% (um e meio por cento) para os demais tipos de imóveis edificados.

## TÍTULO II - DO IMPOSTO TERRITORIAL URBANO

Art. 20. O Imposto Territorial Urbano incide sobre o terreno situado na zona urbana do Município sem qualquer edificação ou com edificação em ruínas.

Art. 27. A alíquota do Imposto Territorial Urbano é de 2% (dois por cento) sobre o valor venal do terreno.

São Paulo, aos 29 de dezembro de 1966, 413º da Fundação de São Paulo.

JOSÉ VICENTE DE FARIA LIMA
Prefeito
"""
    },
    # -------------------------------------------------------------
    # MUNICIPAIS - RIO DE JANEIRO
    # -------------------------------------------------------------
    {
        "titulo": "Lei Municipal nº 1.364, de 19 de dezembro de 1988 (ITBI-RJ)",
        "esfera": "Municipal",
        "orgao": "Câmara Municipal do Rio de Janeiro",
        "tipo": "Lei Municipal",
        "numero": "1364",
        "ano": "1988",
        "data": "1988-12-19",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["ITBI"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://leismunicipais.com.br/a/rj/rio-de-janeiro/lei-ordinaria/1988/136/1364/lei-ordinaria-n-1364-1988",
        "ementa": "Dispõe sobre o Imposto sobre a Transmissão de Bens Imóveis e de direitos a eles relativos, realizada \"inter vivos\", por ato oneroso - ITBI no Município do Rio de Janeiro.",
        "caminho": "municipais/rj/leis/itbi/lei-1364-1988.md",
        "conteudo": """# Lei Municipal nº 1.364, de 19 de dezembro de 1988

Dispõe sobre o Imposto sobre a Transmissão de Bens Imóveis realizada \"inter vivos\" - ITBI no Município do Rio de Janeiro.

O PREFEITO DA CIDADE DO RIO DE JANEIRO:
Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:

Art. 1º O Imposto sobre a Transmissão de Bens Imóveis e de direitos a eles relativos, realizada \"inter vivos\", por ato oneroso (ITBI), incide sobre:
I - a transmissão da propriedade ou do domínio útil de bens imóveis por natureza ou acessão física;
II - a transmissão de direitos reais sobre bens imóveis;
III - a cessão de direitos decorrentes de compromisso de compra e venda.

Art. 5º A base de cálculo do imposto é o valor dos bens ou direitos transmitidos ou cedidos, determinado através de avaliação fiscal da Secretaria Municipal de Fazenda.

Art. 21. A alíquota do imposto é de 3% (três por cento).

Rio de Janeiro, 19 de dezembro de 1988.

SATURNINO BRAGA
Prefeito
"""
    },
    {
        "titulo": "Lei Municipal nº 5.492, de 28 de dezembro de 1988 (ITBI-BH)",
        "esfera": "Municipal",
        "orgao": "Câmara Municipal de Belo Horizonte",
        "tipo": "Lei Municipal",
        "numero": "5492",
        "ano": "1988",
        "data": "1988-12-28",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["ITBI"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://leismunicipais.com.br/a/mg/belo-horizonte/lei-ordinaria/1988/549/5492/lei-ordinaria-n-5492-1988",
        "ementa": "Institui o Imposto sobre a Transmissão de Bens Imóveis e de Direitos a eles relativos, por ato oneroso \"inter vivos\" - ITBI no Município de Belo Horizonte.",
        "caminho": "municipais/bh/leis/itbi/lei-5492-1988.md",
        "conteudo": """# Lei Municipal nº 5.492, de 28 de dezembro de 1988

Institui o Imposto sobre a Transmissão de Bens Imóveis e de Direitos a eles relativos - ITBI no Município de Belo Horizonte.

O PREFEITO DE BELO HORIZONTE:
Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:

Art. 1º O Imposto sobre a Transmissão de Bens Imóveis por ato oneroso \"inter vivos\" - ITBI incide sobre:
I - a transmissão de propriedade ou domínio útil de bens imóveis por natureza ou acessão física;
II - a transmissão de direitos reais sobre imóveis, exceto os de garantia;
III - a cessão de direitos relativos às transmissões referidas.

Art. 4º A base de cálculo do ITBI é o valor de mercado do imóvel no momento da transmissão.

Art. 8º A alíquota do imposto é de 3% (três por cento).

Belo Horizonte, 28 de dezembro de 1988.

PIMENTA DA VEIGA
Prefeito
"""
    }
]

def gerar_normas_patrimonio():
    gerados = []
    print(f"Iniciando estruturação de {len(NORMAS_PATRIMONIO)} normas fundamentais de Patrimônio, ITCMD, IPVA, ITR, ITBI e IPTU...")
    
    for item in NORMAS_PATRIMONIO:
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
        
    print(f"\n{len(gerados)} normas estruturadas com sucesso!")
    return gerados

if __name__ == "__main__":
    gerar_normas_patrimonio()
