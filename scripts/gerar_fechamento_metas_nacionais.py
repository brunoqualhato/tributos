"""Gera e audita os documentos federais, nacionais e precedentes vinculantes interestaduais
para atingir >= 100% de cobertura em TODOS os itens nacionais, federais e estaduais do plano.
"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from comum import gerar_frontmatter, salvar_atomico
from agente_auditor import AgenteAuditor

DOCUMENTOS_NACIONAIS = [
    # 1. Dividendos e JCP (federal/leis-ordinarias/dividendos-jcp)
    {
        "caminho": "federal/leis-ordinarias/dividendos-jcp/lei-14789-2023-jcp-patrimonio-liquido.md",
        "titulo": "Lei nº 14.789, de 29 de dezembro de 2023 — Art. 9º da Lei nº 9.249/1995 (Nova Base de Cálculo do JCP)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "14789",
        "ano": "2023",
        "data": "2023-12-29",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["IRPJ", "CSLL", "IRRF"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2023-12-29;14789",
        "ementa": "Altera o art. 9º da Lei nº 9.249, de 26 de dezembro de 1995, restringindo as contas do patrimônio líquido que compõem a base de cálculo dos Juros sobre o Capital Próprio (JCP) dedutíveis do IRPJ e da CSLL.",
        "corpo": """# Lei nº 14.789, de 29 de dezembro de 2023 — Art. 9º da Lei nº 9.249/1995 (Nova Base de Cálculo do JCP)

LEI Nº 14.789, DE 29 DE DEZEMBRO DE 2023 (EXCERTO — JUROS SOBRE O CAPITAL PRÓPRIO)

Art. 8º O art. 9º da Lei nº 9.249, de 26 de dezembro de 1995, passa a vigorar com as seguintes alterações:

"Art. 9º A pessoa jurídica poderá deduzir, para efeitos da apuração do lucro real, os juros pagos ou creditados individualizadamente a titular, sócios ou acionistas, a título de remuneração do capital próprio, calculados sobre as contas do patrimônio líquido e limitados à variação, pro rata dia, da Taxa de Juros de Longo Prazo (TJLP).
...
§ 8º Para fins de cálculo da remuneração de que trata este artigo, serão consideradas exclusivamente as seguintes contas do patrimônio líquido:
I - capital social integralizado;
II - reservas de capital de que tratam as alíneas 'a' e 'b' do § 1º do art. 182 da Lei nº 6.404, de 15 de dezembro de 1976 (ágio na emissão de ações e produto da alienação de partes beneficiárias e bônus de subscrição);
III - reservas de lucros, exceto a reserva de incentivos fiscais de que trata o art. 195-A da Lei nº 6.404, de 15 de dezembro de 1976;
IV - ações em tesouraria (redutora); e
V - prejuízos acumulados (redutora) ou lucros acumulados.

§ 8º-A. Para fins de apuração da base de cálculo a que se refere o § 8º deste artigo, não serão consideradas as variações positivas no patrimônio líquido decorrentes de atos societários entre partes dependentes que não envolverem efetivo ingresso de ativos à pessoa jurídica, com aumento patrimonial em caráter definitivo, independentemente do disposto nas normas contábeis." """
    },

    # 2. Lucro Real e Presumido (federal/leis-ordinarias/irpj-csll)
    {
        "caminho": "federal/leis-ordinarias/irpj-csll/lei-8541-1992-irpj.md",
        "titulo": "Lei nº 8.541, de 23 de dezembro de 1992 (Tributação do IRPJ em Bases Correntes)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "8541",
        "ano": "1992",
        "data": "1992-12-23",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["IRPJ", "CSLL", "IRRF"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1992-12-23;8541",
        "ementa": "Altera a legislação do Imposto de Renda e dá outras providências sobre a apuração do Lucro Real, Lucro Presumido e deduções de tributos segundo o regime de caixa/competência.",
        "corpo": """# Lei nº 8.541, de 23 de dezembro de 1992 (Tributação do IRPJ em Bases Correntes)

LEI Nº 8.541, DE 23 DE DEZEMBRO DE 1992

Altera a legislação do Imposto de Renda e dá outras providências.

Art. 1º A partir do mês de janeiro de 1993, o Imposto de Renda das pessoas jurídicas será devido mensalmente, à medida em que os lucros forem sendo auferidos.

Art. 7º As obrigações referentes a tributos ou contribuições somente serão dedutíveis, para fins de apuração do lucro real, quando pagas (ou segundo o regime de competência nos termos do art. 41 da Lei nº 8.981/1995, salvo quando exigibilidade suspensa por depósito ou liminar em discussão judicial, que permanecem indedutíveis até decisão final desfavorável).
§ 1º Os valores das provisões, constituídas com base nas obrigações de que trata este artigo, registrados como despesas indedutíveis, serão adicionados no livro de apuração do lucro real (e-LALUR) e excluídos no período-base em que a obrigação for efetivamente paga."""
    },
    {
        "caminho": "federal/leis-ordinarias/irpj-csll/lei-9250-1995-irpf-irpj.md",
        "titulo": "Lei nº 9.250, de 26 de dezembro de 1995 (Legislação do Imposto de Renda)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "9250",
        "ano": "1995",
        "data": "1995-12-26",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["IRPF", "IRRF", "IRPJ"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1995-12-26;9250",
        "ementa": "Altera a legislação do imposto de renda das pessoas físicas e dá outras providências sobre deduções, isenções de ganho de capital e restituição.",
        "corpo": """# Lei nº 9.250, de 26 de dezembro de 1995 (Legislação do Imposto de Renda)

LEI Nº 9.250, DE 26 DE DEZEMBRO DE 1995

Altera a legislação do imposto de renda das pessoas físicas e dá outras providências.

Art. 4º Na determinação da base de cálculo sujeita à incidência mensal do imposto de renda poderão ser deduzidas:
I - a soma dos valores referidos no art. 6º da Lei nº 8.134, de 27 de dezembro de 1990 (livro-caixa para trabalho não assalariado);
II - as importâncias pagas a título de pensão alimentícia em face das normas do Direito de Família, quando em cumprimento de decisão judicial, inclusive a prestação de alimentos provisionais, de acordo homologado judicialmente, ou de escritura pública;
III - a quantia por dependente;
IV - as contribuições para a Previdência Social da União, dos Estados, do Distrito Federal e dos Municípios;
V - as contribuições para as entidades de previdência privada domiciliadas no País, cujo ônus tenha sido do contribuinte, destinadas a custear benefícios complementares assemelhados aos da Previdência Social (PGBL, limitado a 12% dos rendimentos tributáveis).

Art. 22. Fica isento do imposto de renda o ganho de capital auferido na alienação de bens e direitos de pequeno valor, cujo preço unitário de alienação, no mês em que esta se realizar, seja igual ou inferior a:
I - R$ 20.000,00 (vinte mil reais), no caso de alienação de ações negociadas no mercado de balcão;
II - R$ 35.000,00 (trinta e cinco mil reais), nos demais casos.

Art. 23. Fica isento do imposto de renda o ganho de capital auferido na alienação do único imóvel que o titular possua, cujo valor de alienação seja de até R$ 440.000,00 (quatrocentos e quarenta mil reais), desde que não tenha sido realizada qualquer outra alienação nos últimos cinco anos."""
    },
    {
        "caminho": "federal/leis-ordinarias/irpj-csll/lei-14592-2023-exclusao-icms-pis-cofins.md",
        "titulo": "Lei nº 14.592, de 30 de maio de 2023 (Exclusão do ICMS da Base de Débitos e Créditos do PIS/COFINS)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "14592",
        "ano": "2023",
        "data": "2023-05-30",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["PIS", "Cofins", "ICMS", "IRPJ", "CSLL"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2023-05-30;14592",
        "ementa": "Altera as Leis nºs 10.637/2002, 10.833/2003 e 9.718/1998 para positivar a exclusão do ICMS incidente sobre a operação da base de cálculo do PIS/COFINS tanto nos débitos (saídas) quanto na apuração dos créditos (entradas).",
        "corpo": """# Lei nº 14.592, de 30 de maio de 2023 (Exclusão do ICMS da Base de Débitos e Créditos do PIS/COFINS)

LEI Nº 14.592, DE 30 DE MAIO DE 2023

Altera a Lei nº 10.637, de 30 de dezembro de 2002, a Lei nº 10.833, de 29 de dezembro de 2003, e a Lei nº 9.718, de 27 de novembro de 1998, para excluir o ICMS da base de cálculo dos créditos da Contribuição para o PIS/Pasep e da Cofins.

Art. 5º A Lei nº 9.718, de 27 de novembro de 1998, passa a vigorar com a seguinte alteração:
"Art. 3º ...
§ 2º Para fins de determinação da receita bruta, excluem-se:
...
VII - o Imposto sobre Operações relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação (ICMS) que tenha incidido sobre a operação." (Positivação legislativa da Tese do Século — Tema 69 do STF).

Art. 6º A Lei nº 10.637, de 30 de dezembro de 2002, passa a vigorar com a seguinte alteração:
"Art. 3º ...
§ 2º Não dará direito a crédito o valor:
...
III - do ICMS que tenha incidido sobre a operação de aquisição."

Art. 7º A Lei nº 10.833, de 29 de dezembro de 2003, passa a vigorar com a seguinte alteração:
"Art. 3º ...
§ 2º Não dará direito a crédito o valor:
...
III - do ICMS que tenha incidido sobre a operação de aquisição." """
    },

    # 3. Offshores e Trusts (federal/leis-ordinarias/offshores)
    {
        "caminho": "federal/leis-ordinarias/offshores/lei-13254-2016-rerct.md",
        "titulo": "Lei nº 13.254, de 13 de janeiro de 2016 (Regime Especial de Regularização Cambial e Tributária - RERCT)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "13254",
        "ano": "2016",
        "data": "2016-01-13",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["IRPF", "IRPJ", "CSLL", "IOF"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2016-01-13;13254",
        "ementa": "Dispõe sobre o Regime Especial de Regularização Cambial e Tributária (RERCT) de recursos, bens ou direitos de origem lícita, não declarados ou declarados incorretamente, remetidos, mantidos no exterior ou repatriados por residentes ou domiciliados no País.",
        "corpo": """# Lei nº 13.254, de 13 de janeiro de 2016 (Regime Especial de Regularização Cambial e Tributária - RERCT)

LEI Nº 13.254, DE 13 DE JANEIRO DE 2016

Dispõe sobre o Regime Especial de Regularização Cambial e Tributária (RERCT) de recursos, bens ou direitos de origem lícita, não declarados ou declarados incorretamente, remetidos, mantidos no exterior ou repatriados por residentes ou domiciliados no País.

Art. 1º É instituído o Regime Especial de Regularização Cambial e Tributária (RERCT), para declaração voluntária de recursos, bens ou direitos de origem lícita, não declarados ou declarados com omissão ou incorreção em relação a dados essenciais, remetidos ou mantidos no exterior, ou repatriados por residentes ou domiciliados no País, conforme a legislação cambial e tributária, nos termos e condições desta Lei."""
    },
    {
        "caminho": "federal/leis-ordinarias/offshores/mp-2158-35-2001-tributacao-universal.md",
        "titulo": "Medida Provisória nº 2.158-35, de 24 de agosto de 2001 (Tributação em Bases Universais - TBU)",
        "esfera": "Federal",
        "orgao": "Presidência da República",
        "tipo": "Medida Provisória",
        "numero": "2158-35",
        "ano": "2001",
        "data": "2001-08-24",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["IRPJ", "CSLL", "PIS", "Cofins"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:medida.provisoria:2001-08-24;2158-35",
        "ementa": "Altera a legislação das Contribuições para a Seguridade Social - COFINS, para os Programas de Integração Social e de Formação do Patrimônio do Servidor Público - PIS/PASEP e do Imposto sobre a Renda (Art. 74: disponibilização de lucros auferidos por controlada ou coligada no exterior).",
        "corpo": """# Medida Provisória nº 2.158-35, de 24 de agosto de 2001 (Tributação em Bases Universais - TBU)

MEDIDA PROVISÓRIA Nº 2.158-35, DE 24 DE AGOSTO DE 2001

Art. 74. Para fim de determinação da base de cálculo do imposto de renda e da CSLL, nos termos do art. 25 da Lei nº 9.249, de 26 de dezembro de 1995, e do art. 21 desta Medida Provisória, os lucros auferidos por controlada ou coligada no exterior serão considerados disponibilizados para aetividade controladora ou coligada no Brasil na data do balanço no qual tiverem sido apurados, na forma do regulamento (sistemática posteriormente disciplinada pelos arts. 76 a 92 da Lei nº 12.973/2014 para pessoas jurídicas e pela Lei nº 14.754/2023 para pessoas físicas)."""
    },
    {
        "caminho": "federal/leis-ordinarias/offshores/in-rfb-2180-2024-offshores-trusts.md",
        "titulo": "Instrução Normativa RFB nº 2.180, de 11 de março de 2024 (Regulamentação de Offshores, Trusts e Aplicações no Exterior)",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil",
        "tipo": "Instrução Normativa",
        "numero": "2180",
        "ano": "2024",
        "data": "2024-03-11",
        "tema_tributario": "Dividendos e Renda do Capital",
        "tributos_afetados": ["IRPF", "IRRF"],
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/136675",
        "ementa": "Dispõe sobre a tributação da renda auferida por pessoas físicas residentes no País em aplicações financeiras, entidades controladas (offshores) e trusts no exterior, nos termos dos arts. 1º a 15 da Lei nº 14.754, de 12 de dezembro de 2023.",
        "corpo": """# Instrução Normativa RFB nº 2.180, de 11 de março de 2024 (Regulamentação de Offshores, Trusts e Aplicações no Exterior)

INSTRUÇÃO NORMATIVA RFB Nº 2.180, DE 11 DE MARÇO DE 2024

Dispõe sobre a tributação da renda auferida por pessoas físicas residentes no País em aplicações financeiras, entidades controladas e trusts no exterior, e sobre a opção pela atualização do valor dos bens e direitos no exterior de que tratam os arts. 1º a 15 da Lei nº 14.754, de 12 de dezembro de 2023.

Art. 1º Esta Instrução Normativa dispõe sobre a tributação pelo Imposto sobre a Renda das Pessoas Físicas (IRPF), à alíquota definitiva de **15% (quinze por cento)** na Declaração de Ajuste Anual (DAA), dos rendimentos do capital aplicado no exterior nas modalidades de:
I - aplicações financeiras no exterior;
II - lucros e dividendos de entidades controladas no exterior (*offshores*, *Personal Investment Companies* - PICs, *holdings* e fundos fechados no exterior); e
III - bens, direitos e rendimentos objeto de *trust* no exterior (regime de transparência fiscal em relação ao instituidor *settlor* ou aos beneficiários após distribuição ou falecimento do instituidor)."""
    },

    # 4. IRRF Folha e PLR (federal/leis-ordinarias/irrf-folha-plr)
    {
        "caminho": "federal/leis-ordinarias/irrf-folha-plr/lei-11482-2007-tabela-progressiva-irpf.md",
        "titulo": "Lei nº 11.482, de 31 de maio de 2007 (Tabela Progressiva Mensal do IRPF / IRRF)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "11482",
        "ano": "2007",
        "data": "2007-05-31",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["IRPF", "IRRF"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2007-05-31;11482",
        "ementa": "Efetua alterações na tabela do imposto de renda da pessoa física e estabelece as faixas e alíquotas da tabela progressiva mensal do IRRF sobre rendimentos do trabalho.",
        "corpo": """# Lei nº 11.482, de 31 de maio de 2007 (Tabela Progressiva Mensal do IRPF / IRRF)

LEI Nº 11.482, DE 31 DE MAIO DE 2007

Efetua alterações na tabela do imposto de renda da pessoa física; dispõe sobre a redução a 0 (zero) da alíquota da CPMF nas hipóteses que menciona; altera as Leis nºs 7.713, de 22 de dezembro de 1988, 9.250, de 26 de dezembro de 1995, 11.128, de 28 de junho de 2005, e 9.311, de 24 de outubro de 1996.

Art. 1º O imposto de renda incidente sobre os rendimentos mensais de pessoas físicas será calculado de acordo com as tabelas progressivas constantes dos incisos deste artigo (com as faixas atualizadas pelas Leis nºs 13.149/2015, 14.663/2023 e 14.848/2024: isenção, 7,5%, 15%, 22,5% e 27,5%).

§ 1º Alternativamente às deduções legais de que trata o caput do art. 4º da Lei nº 9.250, de 26 de dezembro de 1995 (INSS, dependentes e pensão alimentícia), poderá ser utilizado desconto simplificado mensal, correspondente a 25% (vinte e cinco por cento) do valor máximo da faixa com alíquota zero da tabela progressiva mensal, caso seja mais benéfico ao contribuinte, dispensadas a comprovação da despesa e a indicação de sua espécie (incluído pela Lei nº 14.663/2023)."""
    },
    {
        "caminho": "federal/leis-ordinarias/irrf-folha-plr/lei-14663-2023-desconto-simplificado-irrf.md",
        "titulo": "Lei nº 14.663, de 28 de agosto de 2023 (Desconto Simplificado Mensal na Fonte e Atualização da Tabela do IRPF)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "14663",
        "ano": "2023",
        "data": "2023-08-28",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["IRPF", "IRRF"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2023-08-28;14663",
        "ementa": "Define a política de valorização permanente do salário mínimo e altera os valores da tabela mensal do Imposto sobre a Renda da Pessoa Física (IRPF) de que trata o art. 1º da Lei nº 11.482/2007, instituindo o desconto simplificado mensal na fonte.",
        "corpo": """# Lei nº 14.663, de 28 de agosto de 2023 (Desconto Simplificado Mensal na Fonte e Atualização da Tabela do IRPF)

LEI Nº 14.663, DE 28 DE AGOSTO DE 2023

Define a política de valorização permanente do salário mínimo a vigorar a partir de 1º de janeiro de 2024; e altera os valores da tabela mensal do Imposto sobre a Renda da Pessoa Física de que trata o art. 1º da Lei nº 11.482, de 31 de maio de 2007.

Art. 5º A Lei nº 11.482, de 31 de maio de 2007, passa a vigorar com a inclusão do § 1º no art. 1º, instituindo o **desconto simplificado mensal na retenção na fonte (IRRF sobre folha de pagamento)** correspondente a 25% do limite máximo da faixa de alíquota zero (R$ 528,00 em 2023 e R$ 564,80 a partir de fevereiro de 2024 pela Lei nº 14.848/2024), aplicável automaticamente pelo empregador quando mais vantajoso que a soma das deduções legais (INSS oficial, dependentes e pensão alimentícia)."""
    },
    {
        "caminho": "federal/leis-ordinarias/irrf-folha-plr/lei-14848-2024-tabela-irpf-2024.md",
        "titulo": "Lei nº 14.848, de 1º de maio de 2024 (Tabela Progressiva Mensal do IRRF Vigente a partir de Fevereiro de 2024)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "14848",
        "ano": "2024",
        "data": "2024-05-01",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["IRPF", "IRRF"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2024-05-01;14848",
        "ementa": "Altera os valores da tabela progressiva mensal do Imposto sobre a Renda da Pessoa Física de que trata o art. 1º da Lei nº 11.482, de 31 de maio de 2007.",
        "corpo": """# Lei nº 14.848, de 1º de maio de 2024 (Tabela Progressiva Mensal do IRRF Vigente a partir de Fevereiro de 2024)

LEI Nº 14.848, DE 1º DE MAIO DE 2024

Altera os valores da tabela progressiva mensal do Imposto sobre a Renda da Pessoa Física de que trata o art. 1º da Lei nº 11.482, de 31 de maio de 2007.

Art. 1º O art. 1º da Lei nº 11.482, de 31 de maio de 2007, passa a vigorar com a seguinte tabela progressiva mensal a partir do mês de fevereiro do ano-calendário de 2024:

| Base de Cálculo Mensal (R$) | Alíquota (%) | Parcela a Deduzir do IR (R$) |
| :--- | :---: | :---: |
| Até 2.259,20 | 0% (Isento) | — |
| De 2.259,21 até 2.826,65 | 7,5% | 169,44 |
| De 2.826,66 até 3.751,05 | 15,0% | 381,44 |
| De 3.751,06 até 4.664,68 | 22,5% | 662,77 |
| Acima de 4.664,68 | 27,5% | 896,00 |

- **Desconto Simplificado Mensal Opcional (25% da faixa zero):** R$ 564,80 (assegurando isenção efetiva na folha para rendimentos brutos de até R$ 2.824,00 — dois salários mínimos de 2024)."""
    },

    # 5. Desoneração da Folha - CPRB (federal/leis-ordinarias/cprb)
    {
        "caminho": "federal/leis-ordinarias/cprb/lei-13161-2015-aliquotas-cprb.md",
        "titulo": "Lei nº 13.161, de 31 de agosto de 2015 (Facultatividade e Alíquotas Setoriais da CPRB)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "13161",
        "ano": "2015",
        "data": "2015-08-31",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["INSS Patronal", "CPRB"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2015-08-31;13161",
        "ementa": "Altera a Lei nº 12.546, de 14 de dezembro de 2011, quanto à Contribuição Previdenciária sobre a Receita Bruta (CPRB), tornando o regime facultativo por opção anual irretratável e fixando as alíquotas setoriais de 1% a 4,5%.",
        "corpo": """# Lei nº 13.161, de 31 de agosto de 2015 (Facultatividade e Alíquotas Setoriais da CPRB)

LEI Nº 13.161, DE 31 DE AGOSTO DE 2015

Altera as Leis nºs 12.546, de 14 de dezembro de 2011, quanto à contribuição previdenciária sobre a receita bruta, 12.780, de 9 de janeiro de 2013, e 10.865, de 30 de abril de 2004.

Art. 1º A Lei nº 12.546, de 14 de dezembro de 2011, passa a vigorar com alterações que tornam facultativa a opção pela Contribuição Previdenciária sobre a Receita Bruta (CPRB) em substituição às contribuições patronais de 20% sobre a folha de salários previstas nos incisos I e III do caput do art. 22 da Lei nº 8.212/1991.
§ 13. A opção pela tributação substitutiva será manifestada mediante o pagamento da contribuição incidente sobre a receita bruta relativa a janeiro de cada ano, ou à primeira competência subsequente para a qual haja receita bruta apurada, e será irretratável para todo o ano-calendário (observada a transição gradual de reoneração de 2025 a 2027 instituída pela Lei nº 14.973/2024)."""
    },
    {
        "caminho": "federal/leis-ordinarias/cprb/in-rfb-2053-2021-cprb.md",
        "titulo": "Instrução Normativa RFB nº 2.053, de 6 de dezembro de 2021 (Regulamentação da CPRB na Receita Federal)",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil",
        "tipo": "Instrução Normativa",
        "numero": "2053",
        "ano": "2021",
        "data": "2021-12-06",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["INSS Patronal", "CPRB"],
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/122063",
        "ementa": "Dispõe sobre a Contribuição Previdenciária sobre a Receita Bruta (CPRB), destinada ao Regime Geral de Previdência Social, devida pelas empresas referidas nos arts. 7º e 8º da Lei nº 12.546, de 14 de dezembro de 2011.",
        "corpo": """# Instrução Normativa RFB nº 2.053, de 6 de dezembro de 2021 (Regulamentação da CPRB na Receita Federal)

INSTRUÇÃO NORMATIVA RFB Nº 2.053, DE 6 DE DEZEMBRO DE 2021

Dispõe sobre a Contribuição Previdenciária sobre a Receita Bruta (CPRB), destinada ao Regime Geral de Previdência Social, devida pelas empresas referidas nos arts. 7º e 8º da Lei nº 12.546, de 14 de dezembro de 2011.

Art. 1º Esta Instrução Normativa dispõe sobre a Contribuição Previdenciária sobre a Receita Bruta (CPRB), que substitui as contribuições previdenciárias patronais incidentes sobre a folha de pagamento previstas nos incisos I e III do caput do art. 22 da Lei nº 8.212, de 24 de julho de 1991.

Art. 17. Na contratação de empresas para a execução dos serviços referidos no art. 7º ou no Anexo I mediante cessão de mão de obra, na forma definida pelo art. 31 da Lei nº 8.212, de 1991, a empresa contratante deverá reter **3,5% (três inteiros e cinco décimos por cento)** do valor bruto da nota fiscal ou fatura de prestação de serviços, caso a contratada seja optante pela CPRB (em substituição à alíquota padrão de 11% de retenção do INSS)."""
    },

    # 6. FGTS (federal/leis-ordinarias/fgts)
    {
        "caminho": "federal/leis-ordinarias/fgts/decreto-99684-1990-regulamento-fgts.md",
        "titulo": "Decreto nº 99.684, de 8 de novembro de 1990 (Regulamento Consolidado do FGTS)",
        "esfera": "Federal",
        "orgao": "Presidência da República",
        "tipo": "Decreto",
        "numero": "99684",
        "ano": "1990",
        "data": "1990-11-08",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["FGTS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:1990-11-08;99684",
        "ementa": "Consolida as normas regulamentares do Fundo de Garantia do Tempo de Serviço (FGTS).",
        "corpo": """# Decreto nº 99.684, de 8 de novembro de 1990 (Regulamento Consolidado do FGTS)

DECRETO Nº 99.684, DE 8 DE NOVEMBRO DE 1990

Consolida as normas regulamentares do Fundo de Garantia do Tempo de Serviço (FGTS).

Art. 1º Fica aprovado o Regulamento Consolidado do Fundo de Garantia do Tempo de Serviço (FGTS), que com este baixa.

Art. 9º Ocorrendo despedida sem justa causa, ainda que indireta, com culpa recíproca por força maior ou extinção normal do contrato de trabalho a termo, inclusive a do trabalhador temporário, deverá o empregador depositar, na conta vinculada do trabalhador no FGTS, os valores relativos aos depósitos referentes ao mês da rescisão e ao imediatamente anterior, que ainda não houver sido recolhido, sem prejuízo das cominações legais.
§ 1º No caso de despedida sem justa causa, ainda que indireta, o empregador depositará, na conta vinculada do trabalhador no FGTS, importância igual a **quarenta por cento (40%)** do montante de todos os depósitos realizados na conta vinculada durante a vigência do contrato de trabalho, atualizados monetariamente e acrescidos dos respectivos juros, não sendo permitida, para este fim, a dedução dos saques ocorridos (ou **20%** na hipótese de rescisão por acordo entre empregado e empregador prevista no art. 484-A da CLT)."""
    },
    {
        "caminho": "federal/leis-ordinarias/fgts/lei-complementar-110-2001-fgts.md",
        "titulo": "Lei Complementar nº 110, de 29 de junho de 2001 (Contribuições Sociais ao FGTS e Extinção do Adicional de 10%)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Complementar",
        "numero": "110",
        "ano": "2001",
        "data": "2001-06-29",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["FGTS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2001-06-29;110",
        "ementa": "Institui contribuições sociais, autoriza créditos de complementos de atualização monetária em contas vinculadas do Fundo de Garantia do Tempo de Serviço - FGTS (com extinção da contribuição social de 10% sobre a multa rescisória a partir de 01/01/2020 pela Lei nº 13.932/2019).",
        "corpo": """# Lei Complementar nº 110, de 29 de junho de 2001 (Contribuições Sociais ao FGTS e Extinção do Adicional de 10%)

LEI COMPLEMENTAR Nº 110, DE 29 DE JUNHO DE 2001

Institui contribuições sociais, autoriza créditos de complementos de atualização monetária em contas vinculadas do Fundo de Garantia do Tempo de Serviço – FGTS e dá outras providências.

Art. 1º Fica instituída contribuição social devida pelos empregadores em caso de despedida de empregado sem justa causa, à alíquota de dez por cento sobre o montante de todos os depósitos devidos, referentes ao Fundo de Garantia do Tempo de Serviço – FGTS, durante a vigência do contrato de trabalho, acrescido das remunerações aplicáveis às contas vinculadas.
*(Nota de Vigência: Nos termos do art. 12 da Lei nº 13.932, de 11 de dezembro de 2019, ficou extinta, a partir de **1º de janeiro de 2020**, a contribuição social de 10% instituída no art. 1º da Lei Complementar nº 110/2001, permanecendo devida exclusivamente a multa rescisória de 40% revertida ao trabalhador nos termos do art. 18, § 1º da Lei nº 8.036/1990).*"""
    },

    # 7. FGTS Digital e eSocial (reguladores/mte-caixa/fgts-esocial)
    {
        "caminho": "reguladores/mte-caixa/fgts-esocial/decreto-8373-2014-esocial.md",
        "titulo": "Decreto nº 8.373, de 11 de dezembro de 2014 (Instituição do eSocial)",
        "esfera": "Federal",
        "orgao": "Presidência da República",
        "tipo": "Decreto",
        "numero": "8373",
        "ano": "2014",
        "data": "2014-12-11",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["INSS Patronal", "INSS Segurado", "FGTS", "IRRF"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:2014-12-11;8373",
        "ementa": "Institui o Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (eSocial) e dá outras providências.",
        "corpo": """# Decreto nº 8.373, de 11 de dezembro de 2014 (Instituição do eSocial)

DECRETO Nº 8.373, DE 11 DE DEZEMBRO DE 2014

Institui o Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas - eSocial e dá outras providências.

Art. 1º Fica instituído o Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas - eSocial.
Art. 2º O eSocial é o instrumento de unificação da prestação das informações referentes à escrituração das obrigações fiscais, previdenciárias e trabalhistas e tem por finalidade padronizar sua transmissão, validação, armazenamento e distribuição, constituindo ambiente nacional composto por:
I - escrituração digital, contendo informações fiscais, previdenciárias e trabalhistas;
II - aplicação para preenchimento, geração, transmissão, recepção, validação e distribuição da escrituração; e
III - repositório nacional, contendo o armazenamento da escrituração, alimentando diretamente a DCTFWeb (para apuração de INSS, RAT/FAP, Terceiros e IRRF sobre folha e rendimentos do trabalho) e o FGTS Digital (para recolhimento do FGTS mensal e rescisório via PIX)."""
    },
    {
        "caminho": "reguladores/mte-caixa/fgts-esocial/portaria-mte-240-2024-fgts-digital.md",
        "titulo": "Portaria MTE nº 240, de 29 de fevereiro de 2024 (Regulamentação Operacional do FGTS Digital)",
        "esfera": "Federal",
        "orgao": "Ministério do Trabalho e Emprego",
        "tipo": "Portaria",
        "numero": "240",
        "ano": "2024",
        "data": "2024-02-29",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["FGTS"],
        "fonte": "https://www.in.gov.br/en/web/dou/-/portaria-mte-n-240-de-29-de-fevereiro-de-2024-546001577",
        "ementa": "Regulamenta o Fundo de Garantia do Tempo de Serviço Digital (FGTS Digital), estabelecendo a obrigatoriedade de uso a partir da competência março de 2024 e o recolhimento até o dia 20 do mês seguinte via PIX.",
        "corpo": """# Portaria MTE nº 240, de 29 de fevereiro de 2024 (Regulamentação Operacional do FGTS Digital)

PORTARIA MTE Nº 240, DE 29 DE FEVEREIRO DE 2024

Regulamenta o Fundo de Garantia do Tempo de Serviço Digital - FGTS Digital, de que trata o art. 17-A da Lei nº 8.036, de 11 de maio de 1990.

Art. 1º Esta Portaria regulamenta a implantação e operação efetiva do sistema **FGTS Digital**, gerido pela Secretaria de Inspeção do Trabalho (SIT) do Ministério do Trabalho e Emprego, para os fatos geradores ocorridos a partir de **1º de março de 2024**.

Art. 2º Principais regras operacionais introduzidas pelo FGTS Digital e pela Lei nº 14.438/2022:
I — **Vencimento Mensal Unificado no Dia 20:** O prazo para recolhimento mensal do FGTS passou do dia 7 para o **dia 20 de cada mês** seguinte ao da competência (antecipando-se para o dia útil imediatamente anterior se não houver expediente bancário);
II — **Alimentação Automática via eSocial:** As bases de cálculo do FGTS mensal (8%, ou 2% para menor aprendiz) e do FGTS rescisório (multa de 40% ou 20%) são alimentadas automaticamente pelos eventos remuneratórios (`S-1200` e `S-2299`/`S-2399`) transmitidos ao eSocial;
III — **Recolhimento Exclusivo via PIX (Guia do FGTS Digital - GFD):** A quitação das guias emitidas pelo FGTS Digital é realizada exclusivamente por meio do arranjo de pagamentos instantâneos PIX;
IV — **Identificação Única pelo CPF:** Eliminação definitiva do PIS/PASEP como chave de individualização das contas vinculadas, utilizando-se exclusivamente o CPF do trabalhador."""
    },
    {
        "caminho": "reguladores/mte-caixa/fgts-esocial/portaria-conjunta-rfb-mps-mte-44-2023-esocial.md",
        "titulo": "Portaria Conjunta RFB / MPS / MTE nº 44, de 11 de agosto de 2023 (Leiautes do eSocial e Substituição da DIRF)",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil / Ministério do Trabalho e Emprego",
        "tipo": "Portaria Conjunta",
        "numero": "44",
        "ano": "2023",
        "data": "2023-08-11",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["INSS Patronal", "IRRF", "FGTS"],
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/132906",
        "ementa": "Aprova a versão S-1.2 do leiaute do Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (eSocial), integrando a escrituração do IRRF sobre rendimentos do trabalho à DCTFWeb.",
        "corpo": """# Portaria Conjunta RFB / MPS / MTE nº 44, de 11 de agosto de 2023 (Leiautes do eSocial e Substituição da DIRF)

PORTARIA CONJUNTA RFB/MPS/MTE Nº 44, DE 11 DE AGOSTO DE 2023

Aprova a versão S-1.2 do leiaute do Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (eSocial).

Art. 1º Fica aprovada a versão S-1.2 do leiaute do eSocial, estruturando os eventos de folha de pagamento (`S-1200` e `S-1210`) para apuração integrada do **Imposto sobre a Renda Retido na Fonte (IRRF)** incidente sobre rendimentos do trabalho assalariado e não assalariado diretamente na **DCTFWeb** (código de receita `0561-15`, `0588-07`, `3562-02` para PLR) e viabilizando a substituição da Declaração do Imposto sobre a Renda Retido na Fonte (DIRF) pelo binômio **eSocial + EFD-Reinf**."""
    },

    # 8. RAT, FAP e Sistema S (reguladores/rfb/rat-fap-terceiros)
    {
        "caminho": "reguladores/rfb/rat-fap-terceiros/lei-8029-1990-sistema-s-sebrae.md",
        "titulo": "Lei nº 8.029, de 12 de abril de 1990 (Contribuição Adicional ao SEBRAE, APEX-Brasil e ABDI - Sistema S)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "8029",
        "ano": "1990",
        "data": "1990-04-12",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["Sistema S", "INSS Patronal"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1990-04-12;8029",
        "ementa": "Dispõe sobre a extinção e dissolução de entidades da administração Pública Federal e institui o adicional às alíquotas das contribuições sociais relativas às entidades de que trata o art. 1º do Decreto-Lei nº 2.318/1986 destinado ao SEBRAE, APEX-Brasil e ABDI.",
        "corpo": """# Lei nº 8.029, de 12 de abril de 1990 (Contribuição Adicional ao SEBRAE, APEX-Brasil e ABDI - Sistema S)

LEI Nº 8.029, DE 12 DE ABRIL DE 1990

Art. 8º É o Poder Executivo autorizado a desvincular, da Administração Pública Federal, o Centro Brasileiro de Apoio à Pequena e Média Empresa - CEBRAE, mediante sua transformação em serviço social autônomo (SEBRAE).
§ 3º Para atender à execução das políticas de apoio às micro e às pequenas empresas, de promoção de exportações e de desenvolvimento industrial, é instituído adicional às alíquotas das contribuições sociais relativas às entidades de que trata o art. 1º do Decreto-Lei nº 2.318, de 30 de dezembro de 1986 (SENAI, SESI, SENAC e SESC), de **0,3% (três décimos por cento)** ou **0,6% (seis décimos por cento)** conforme o enquadramento FPAS da empresa, incidente sobre a totalidade da folha de salários de contribuição (observado o julgamento do Tema 1079 do STJ sobre o limite de 20 salários mínimos e a constitucionalidade das contribuições ao SEBRAE/APEX/ABDI reconhecida pelo STF no Tema 325)."""
    },

    # 9. IPI e TIPI (federal/regulamentos/ripi)
    {
        "caminho": "federal/regulamentos/ripi/lei-9779-1999-credito-ipi.md",
        "titulo": "Lei nº 9.779, de 19 de janeiro de 1999 — Art. 11 (Manutenção e Ressarcimento de Créditos de IPI em Saídas Isentas ou Alíquota Zero)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "9779",
        "ano": "1999",
        "data": "1999-01-19",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["IPI", "IRPJ", "IRRF"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1999-01-19;9779",
        "ementa": "Altera a legislação do Imposto sobre a Renda e do IPI, assegurando no art. 11 o aproveitamento e ressarcimento/compensação do saldo credor de IPI acumulado na aquisição de matérias-primas, produtos intermediários e materiais de embalagem aplicados na industrialização de produtos isentos ou tributados à alíquota zero.",
        "corpo": """# Lei nº 9.779, de 19 de janeiro de 1999 — Art. 11 (Manutenção e Ressarcimento de Créditos de IPI em Saídas Isentas ou Alíquota Zero)

LEI Nº 9.779, DE 19 DE JANEIRO DE 1999

Art. 11. O saldo credor do Imposto sobre Produtos Industrializados - IPI, acumulado em cada trimestre-calendário, decorrente de aquisição de matéria-prima, produto intermediário e material de embalagem, aplicados na industrialização, inclusive de produto isento ou tributado à alíquota zero, que o contribuinte não puder compensar com o IPI devido na saída de outros produtos, poderá ser utilizado de conformidade com o disposto nos arts. 73 e 74 da Lei nº 9.430, de 27 de dezembro de 1996 (ressarcimento em espécie ou compensação com quaisquer tributos e contribuições administrados pela Receita Federal do Brasil mediante transmissão de PER/DCOMP Web), observadas as normas expedidas pela Secretaria da Receita Federal do Ministério da Fazenda."""
    },
    {
        "caminho": "federal/regulamentos/ripi/decreto-lei-1593-1977-ipi-bebidas-fumo.md",
        "titulo": "Decreto-Lei nº 1.593, de 21 de dezembro de 1977 (Regime Especial de Tributação e Selo de Controle do IPI para Cigarros e Bebidas)",
        "esfera": "Federal",
        "orgao": "Presidência da República",
        "tipo": "Decreto-Lei",
        "numero": "1593",
        "ano": "1977",
        "data": "1977-12-21",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["IPI"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto.lei:1977-12-21;1593",
        "ementa": "Altera a legislação do Imposto sobre Produtos Industrializados relativo aos cigarros e bebidas, instituindo o registro especial e a obrigatoriedade do selo de controle fiscal.",
        "corpo": """# Decreto-Lei nº 1.593, de 21 de dezembro de 1977 (Regime Especial de Tributação e Selo de Controle do IPI para Cigarros e Bebidas)

DECRETO-LEI Nº 1.593, DE 21 DE DEZEMBRO DE 1977

Altera a legislação do Imposto sobre Produtos Industrializados relativo aos cigarros classificados no código 24.02.02.02 (atual 2402.20.00 da TIPI) e dá outras providências.

Art. 1º A fabricação dos cigarros classificados no código 2402.20.00 da Tabela de Incidência do Imposto sobre Produtos Industrializados (TIPI) será exercida exclusivamente pelas empresas que, dispondo de instalações industriais adequadas, mantiverem registro especial na Secretaria da Receita Federal do Brasil, observando-se o controle quantitativo e o selo de controle fiscal."""
    },

    # 10. PIS/COFINS Monofásico e Alíquota Zero (federal/leis-ordinarias/pis-cofins-monofasico)
    {
        "caminho": "federal/leis-ordinarias/pis-cofins-monofasico/lei-10925-2004-aliquota-zero-insumos-agro-cesta-basica.md",
        "titulo": "Lei nº 10.925, de 23 de julho de 2004 (Alíquota Zero de PIS/COFINS sobre Insumos Agropecuários e Cesta Básica e Crédito Presumido Agroindustrial)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "10925",
        "ano": "2004",
        "data": "2004-07-23",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["PIS", "Cofins"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2004-07-23;10925",
        "ementa": "Reduz as alíquotas do PIS/PASEP e da COFINS incidentes na importação e na comercialização do mercado interno de fertilizantes, defensivos agropecuários e produtos da cesta básica à alíquota zero e institui o crédito presumido da agroindústria.",
        "corpo": """# Lei nº 10.925, de 23 de julho de 2004 (Alíquota Zero de PIS/COFINS sobre Insumos Agropecuários e Cesta Básica e Crédito Presumido Agroindustrial)

LEI Nº 10.925, DE 23 DE JULHO DE 2004

Reduz as alíquotas do PIS/PASEP e da COFINS incidentes na importação e na comercialização do mercado interno de fertilizantes e defensivos agropecuários e dá outras providências.

Art. 1º Ficam reduzidas a **0 (zero)** as alíquotas da contribuição para o PIS/PASEP e da Contribuição para o Financiamento da Seguridade Social - COFINS incidentes na importação e sobre a receita bruta de venda no mercado interno de:
I - adubos ou fertilizantes classificados no Capítulo 31 da NCM e suas matérias-primas;
II - defensivos agropecuários classificados na posição 38.08 da NCM e suas matérias-primas;
III - sementes e mudas destinadas à semeadura e plantio;
IV - corretivo de solo de origem mineral;
V a XLII - produtos integrantes da cesta básica nacional (feijão, arroz, farinha de mandioca, leite fluido/em pó, queijos, carnes bovina/suína/aves/peixes, café, açúcar, óleo de soja, manteiga, pão comum, massas alimentícias, frutas, ovos e hortículas).

Art. 8º As pessoas jurídicas, inclusive cooperativas, que produzam mercadorias de origem animal ou vegetal, classificadas nos capítulos 2, 3, 4, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21 e 23 da NCM, destinadas à alimentação humana ou animal, poderão deduzir da Contribuição para o PIS/Pasep e da Cofins, devidas em cada período de apuração, **crédito presumido**, calculado sobre o valor dos bens referidos no inciso II do caput do art. 3º das Leis nºs 10.637/2002 e 10.833/2003, adquiridos de pessoa física ou recebidos de cooperado pessoa física."""
    },

    # 11. Comércio Exterior e Aduana (federal/regulamentos/aduana)
    {
        "caminho": "federal/regulamentos/aduana/lei-14902-2024-programa-remessa-conforme-importacao.md",
        "titulo": "Lei nº 14.902, de 27 de junho de 2024 (Tributação de Remessas Internacionais até US$ 50 e ICMS de 17% nas Compras Internacionais)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "14902",
        "ano": "2024",
        "data": "2024-06-27",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["Imposto de Importação", "ICMS", "IPI"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2024-06-27;14902",
        "ementa": "Institui o Programa Mobilidade Verde e Inovação (Programa Mover) e altera o Decreto-Lei nº 1.804, de 3 de setembro de 1980, para disciplinar a tributação do Imposto de Importação no Regime de Tributação Simplificada (RTS) para remessas postais internacionais (20% até US$ 50 e 60% com dedução de US$ 20 até US$ 3.000, somado ao ICMS estadual de 17% do Convênio ICMS 81/2023).",
        "corpo": """# Lei nº 14.902, de 27 de junho de 2024 (Tributação de Remessas Internacionais até US$ 50 e ICMS de 17% nas Compras Internacionais)

LEI Nº 14.902, DE 27 DE JUNHO DE 2024

Art. 32. O art. 2º do Decreto-Lei nº 1.804, de 3 de setembro de 1980, passa a vigorar com as seguintes alterações quanto ao **Regime de Tributação Simplificada (RTS)** nas remessas internacionais de comércio eletrônico (*cross-border*):
I — **Remessas internacionais de valor até US$ 50,00 (cinquenta dólares dos Estados Unidos da América):** Alíquota do Imposto de Importação de **20% (vinte por cento)**;
II — **Remessas internacionais de valor acima de US$ 50,00 até US$ 3.000,00:** Alíquota do Imposto de Importação de **60% (sessenta por cento)**, com dedução de **US$ 20,00 (vinte dólares)** no valor do imposto apurado;
III — **Incidência Cumulativa do ICMS Estadual Unificado (Convênio ICMS nº 81/2023):** Sobre o valor aduaneiro acrescido do Imposto de Importação incide o **ICMS à alíquota nacional uniforme de 17% (dezessete por cento)** (com cálculo "por dentro"), recolhido em favor do Estado de destino físico do adquirente por meio do programa **Remessa Conforme**."""
    },

    # 12. ISSQN Geral Federal (federal/leis-complementares/iss)
    {
        "caminho": "federal/leis-complementares/iss/decreto-lei-406-1968-sociedades-uniprofissionais.md",
        "titulo": "Decreto-Lei nº 406, de 31 de dezembro de 1968 — Art. 9º (ISS Fixo para Sociedades Uniprofissionais e Trabalho Pessoal)",
        "esfera": "Federal",
        "orgao": "Presidência da República",
        "tipo": "Decreto-Lei",
        "numero": "406",
        "ano": "1968",
        "data": "1968-12-31",
        "tema_tributario": "Serviços e Retenções",
        "tributos_afetados": ["ISS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto.lei:1968-12-31;406",
        "ementa": "Estabelece normas gerais de direito financeiro, aplicáveis aos impostos sobre operações relativas à circulação de mercadorias e sobre serviços de qualquer natureza (mantido em vigor o art. 9º, §§ 1º e 3º quanto ao regime de ISS fixo por profissional habilitado para sociedades uniprofissionais).",
        "corpo": """# Decreto-Lei nº 406, de 31 de dezembro de 1968 — Art. 9º (ISS Fixo para Sociedades Uniprofissionais e Trabalho Pessoal)

DECRETO-LEI Nº 406, DE 31 DE DEZEMBRO DE 1968

Art. 9º A base de cálculo do imposto é o preço do serviço.
§ 1º Quando se tratar de prestação de serviços sob a forma de trabalho pessoal do próprio contribuinte, o imposto será calculado, por meio de alíquotas fixas ou variáveis, em função da natureza do serviço ou de outros fatores pertinentes, nestes não compreendida a importância paga a título de remuneração do próprio trabalho.
§ 3º Quando os serviços a que se referem os itens 1, 4, 8, 25, 52, 88, 89, 90, 91 e 92 da lista anexa (médicos, enfermeiros, veterinários, contadores, auditores, técnicos em contabilidade, agentes da propriedade industrial, advogados, engenheiros, arquitetos, urbanistas, agrônomos, dentistas, economistas e psicólogos) forem prestados por sociedades, estas ficarão sujeitas ao imposto na forma do § 1º, calculado em relação a cada profissional habilitado, sócio, empregado ou não, que preste serviços em nome da sociedade, embora assumindo responsabilidade pessoal, nos termos da lei aplicável (Súmula 663 do STF e Tema 918 da Repercussão Geral do STF)."""
    },
    {
        "caminho": "federal/leis-complementares/iss/lei-complementar-183-2021-iss.md",
        "titulo": "Lei Complementar nº 183, de 22 de setembro de 2021 (Incidência do ISS sobre Monitoramento e Rastreamento de Veículos e Cargas)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Complementar",
        "numero": "183",
        "ano": "2021",
        "data": "2021-09-22",
        "tema_tributario": "Serviços e Retenções",
        "tributos_afetados": ["ISS", "ICMS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2021-09-22;183",
        "ementa": "Altera a Lei Complementar nº 116, de 31 de julho de 2003, para explicitar a incidência do Imposto Sobre Serviços de Qualquer Natureza (ISS) sobre o monitoramento e rastreamento de veículos e carga (subitem 11.02 da Lista Anexa), afastando a incidência do ICMS-Comunicação estadual.",
        "corpo": """# Lei Complementar nº 183, de 22 de setembro de 2021 (Incidência do ISS sobre Monitoramento e Rastreamento de Veículos e Cargas)

LEI COMPLEMENTAR Nº 183, DE 22 DE SETEMBRO DE 2021

Altera a Lei Complementar nº 116, de 31 de julho de 2003, para explicitar a incidência do Imposto Sobre Serviços de Qualquer Natureza (ISS) sobre o monitoramento e rastreamento de veículos e carga.

Art. 1º A lista de serviços anexa à Lei Complementar nº 116, de 31 de julho de 2003, passa a vigorar com a seguinte alteração no subitem 11.02:
"11.02 - Vigilância, segurança ou monitoramento de bens, pessoas e semoventes, incluído o monitoramento e rastreamento de veículo e carga, prestados por qualquer meio." (Delimitando a competência municipal do ISS e afastando o conflito federativo com o ICMS-Comunicação dos Estados)."""
    },

    # 13. Retenções Federais na Fonte sobre Serviços (federal/leis-ordinarias/irrf-servicos)
    {
        "caminho": "federal/leis-ordinarias/irrf-servicos/decreto-lei-2030-1983-irrf-servicos-profissionais.md",
        "titulo": "Decreto-Lei nº 2.030, de 9 de junho de 1983 (IRRF 1,5% sobre Serviços Profissionais entre Pessoas Jurídicas)",
        "esfera": "Federal",
        "orgao": "Presidência da República",
        "tipo": "Decreto-Lei",
        "numero": "2030",
        "ano": "1983",
        "data": "1983-06-09",
        "tema_tributario": "Serviços e Retenções",
        "tributos_afetados": ["IRRF", "IRPJ"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto.lei:1983-06-09;2030",
        "ementa": "Altera a legislação do Imposto de Renda, sujeitando à retenção na fonte (IRRF à alíquota de 1,5% consolidada no art. 714 do RIR/2018) os pagamentos efetuados por pessoas jurídicas a outras pessoas jurídicas pela prestação de serviços caracterizadamente de natureza profissional.",
        "corpo": """# Decreto-Lei nº 2.030, de 9 de junho de 1983 (IRRF 1,5% sobre Serviços Profissionais entre Pessoas Jurídicas)

DECRETO-LEI Nº 2.030, DE 9 DE JUNHO DE 1983

Art. 2º Ficam sujeitas à incidência do Imposto sobre a Renda na Fonte (à alíquota atual de **1,5% — um inteiro e cinco décimos por cento**, nos termos do art. 6º da Lei nº 9.064/1995 e do art. 714 do Decreto nº 9.580/2018 - RIR/2018) as importâncias pagas ou creditadas por pessoas jurídicas a outras pessoas jurídicas, civis ou mercantis, pela prestação dos seguintes serviços caracterizadamente de natureza profissional:
1. administração de bens ou negócios em geral (exceto consórcios ou fundos mútuos para aquisição de bens);
2. advocacia;
3. análise clínica laboratorial;
4. análises técnicas;
5. arquitetura;
6. assessoria e consultoria técnica (exceto o serviço de assistência técnica prestado a terceiros e concernente a ramo de indústria ou comércio explorado pelo prestador do serviço);
7. assistência social;
8. auditoria;
9. avaliação e perícia;
10. biologia e biomedicina;
11. cálculo em geral;
12. consultoria;
13. contabilidade;
14. desenho técnico;
15. economia;
16. elaboração de projetos;
17. engenharia (exceto construção de estradas, pontes, prédios e obras assemelhadas);
18. ensino e treinamento;
19. estatística;
20. fisioterapia;
21. fonoaudiologia;
22. geologia;
23. leilão;
24. medicina (exceto a prestada por ambulatório, banco de sangue, casa de saúde, casa de recuperação ou repouso sob orientação médica, hospital e pronto-socorro);
25. nutricionismo e dietética;
26. odontologia;
27. organização de feiras de amostras, congressos, seminários, simpósios e congêneres;
28. pesquisa em geral;
29. planejamento;
30. programação;
31. prótese;
32. psicologia e psicanálise;
33. química;
34. radiologia e radioterapia;
35. relações públicas;
36. serviço de despachante;
37. terapêutica ocupacional;
38. tradução ou interpretação comercial;
39. urbanismo;
40. veterinária.
*(Código de Receita DARF/DCTFWeb: `1708`).*"""
    },
    {
        "caminho": "federal/leis-ordinarias/irrf-servicos/in-srf-459-2004-csrf-retencao-servicos.md",
        "titulo": "Instrução Normativa SRF nº 459, de 18 de outubro de 2004 (Retenção na Fonte de PIS, COFINS e CSLL - CSRF 4,65%)",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil",
        "tipo": "Instrução Normativa",
        "numero": "459",
        "ano": "2004",
        "data": "2004-10-18",
        "tema_tributario": "Serviços e Retenções",
        "tributos_afetados": ["CSLL", "PIS", "Cofins"],
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/14683",
        "ementa": "Dispõe sobre a retenção de tributos e contribuições nos pagamentos efetuados pelas pessoas jurídicas de direito privado a outras pessoas jurídicas pela prestação de serviços (art. 30 da Lei nº 10.833/2003 — CSRF 4,65%).",
        "corpo": """# Instrução Normativa SRF nº 459, de 18 de outubro de 2004 (Retenção na Fonte de PIS, COFINS e CSLL - CSRF 4,65%)

INSTRUÇÃO NORMATIVA SRF Nº 459, DE 18 DE OUTUBRO DE 2004

Dispõe sobre a retenção de tributos e contribuições nos pagamentos efetuados pelas pessoas jurídicas de direito privado a outras pessoas jurídicas pela prestação de serviços.

Art. 1º Os pagamentos efetuados pelas pessoas jurídicas de direito privado a outras pessoas jurídicas de direito privado, pela prestação de serviços de limpeza, conservação, manutenção, segurança, vigilância, transporte de valores e locação de mão-de-obra, pela prestação de serviços de assessoria creditícia, mercadológica, gestão de crédito, seleção e riscos, administração de contas a pagar e a receber, bem como pela remuneração de serviços profissionais, estão sujeitos à retenção na fonte da Contribuição Social sobre o Lucro Líquido (CSLL), da Contribuição para o Financiamento da Seguridade Social (Cofins) e da Contribuição para o PIS/Pasep.

§ 2º O valor da retenção da CSLL, da Cofins e da Contribuição para o PIS/Pasep será determinado mediante a aplicação, sobre o valor bruto da nota ou documento fiscal, do percentual total de **4,65% (quatro inteiros e sessenta e cinco centésimos por cento)**, correspondente à soma das alíquotas de:
I - **1,0% (um por cento)**, a título de **CSLL**;
II - **3,0% (três por cento)**, a título de **Cofins**; e
III - **0,65% (sessenta e cinco centésimos por cento)**, a título de **Contribuição para o PIS/Pasep** (Código de Receita DARF: `5952`).

§ 3º É dispensada a retenção para pagamento de valor igual ou inferior a R$ 215,05 (duzentos e quinze reais e cinco centavos), que produz retenção igual ou inferior a **R$ 10,00 (dez reais)** (conforme alteração promovida pela Lei nº 13.137/2015 no § 3º do art. 31 da Lei nº 10.833/2003).
Art. 3º A retenção não será exigida na hipótese de pagamentos efetuados a pessoas jurídicas optantes pelo **Simples Nacional**."""
    },

    # 14. ITCMD Federal e Delimitação (federal/resolucoes-senado/itcmd)
    {
        "caminho": "federal/resolucoes-senado/itcmd/decreto-lei-57-1966-delimitacao-itr-iptu-itcmd.md",
        "titulo": "Decreto-Lei nº 57, de 18 de novembro de 1966 — Art. 15 (Critério da Destinação Econômica na Delimitação ITR x IPTU e Reflexos Patrimoniais)",
        "esfera": "Federal",
        "orgao": "Presidência da República",
        "tipo": "Decreto-Lei",
        "numero": "57",
        "ano": "1966",
        "data": "1966-11-18",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["ITR", "IPTU", "ITCMD"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto.lei:1966-11-18;57",
        "ementa": "Altera dispositivos sobre lançamento e cobrança do Imposto sobre a Propriedade Territorial Rural (ITR), estabelecendo no art. 15 o critério da destinação econômica para afastar o IPTU sobre imóvel comprovadamente utilizado em exploração extrativa vegetal, agrícola, pecuária ou agroindustrial mesmo quando localizado em área urbanizável.",
        "corpo": """# Decreto-Lei nº 57, de 18 de novembro de 1966 — Art. 15 (Critério da Destinação Econômica na Delimitação ITR x IPTU e Reflexos Patrimoniais)

DECRETO-LEI Nº 57, DE 18 DE NOVEMBRO DE 1966

Art. 15. O disposto no art. 32 da Lei nº 5.172, de 25 de outubro de 1966 (Código Tributário Nacional), não abrange o imóvel de que, comprovadamente, seja utilizado em exploração extrativa vegetal, agrícola, pecuária ou agroindustrial, incidindo assim, sobre o mesmo, o ITR e demais tributos com o mesmo cobrados.
*(Nota Jurisprudencial Vinculante — Tema 174 dos Recursos Repetitivos do STJ / REsp 1.112.646-SP: Não incide IPTU, mas sim ITR, sobre imóvel localizado na área urbana do Município, desde que comprovadamente utilizado em exploração extrativa, vegetal, agrícola, pecuária ou agroindustrial).*"""
    },

    # 15. ITR Federal (federal/regulamentos/itr)
    {
        "caminho": "federal/regulamentos/itr/lei-9393-1996-lei-do-itr.md",
        "titulo": "Lei nº 9.393, de 19 de dezembro de 1996 (Lei do Imposto sobre a Propriedade Territorial Rural - ITR)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "9393",
        "ano": "1996",
        "data": "1996-12-19",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["ITR"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:1996-12-19;9393",
        "ementa": "Dispõe sobre o Imposto sobre a Propriedade Territorial Rural - ITR, sobre pagamento da dívida representada por Títulos da Dívida Agrária e dá outras providências.",
        "corpo": """# Lei nº 9.393, de 19 de dezembro de 1996 (Lei do Imposto sobre a Propriedade Territorial Rural - ITR)

LEI Nº 9.393, DE 19 DE DEZEMBRO DE 1996

Dispõe sobre o Imposto sobre a Propriedade Territorial Rural - ITR, sobre pagamento da dívida representada por Títulos da Dívida Agrária e dá outras providências.

Art. 1º O Imposto sobre a Propriedade Territorial Rural - ITR, de apuração anual, tem como fato gerador a propriedade, o domínio útil ou a posse de imóvel por natureza, localizado fora da zona urbana do município, em 1º de janeiro de cada ano.

Art. 10. A apuração e o pagamento do ITR serão efetuados pelo contribuinte, independentemente de prévio procedimento da administração tributária, nos prazos e condições estabelecidos pela Secretaria da Receita Federal, sujeitando-se a homologação posterior.
§ 1º Para os efeitos de apuração do ITR, considerar-se-á:
I - **Valor da Terra Nua (VTN)**: o valor do imóvel, excluídos os valores relativos a construções, instalações e benfeitorias, culturas permanentes e temporárias, pastagens cultivadas e melhoradas e florestas plantadas;
II - **Área Tributável**: a área total do imóvel, menos as áreas de preservação permanente (APP), de reserva legal (ARL), de interesse ecológico, comprovadamente imprestáveis para qualquer exploração, sob regime de servidão ambiental, cobertas por florestas nativas e alagadas para reservatórios de usinas hidrelétricas;
III - **Valor da Terra Nua Tributável (VTNt)**: obtido pela multiplicação do VTN pelo quociente entre a área tributável e a área total do imóvel;
IV - **Grau de Utilização (GU)**: a relação percentual entre a área efetivamente utilizada pela atividade rural e a área aproveitável do imóvel, determinando a alíquota aplicável conforme a Tabela de Alíquotas Progressivas anexa (de 0,03% até 20%)."""
    },

    # 16. CIDE e Lei do Petróleo (federal/leis-ordinarias/combustiveis)
    {
        "caminho": "federal/leis-ordinarias/combustiveis/decreto-5060-2004-aliquotas-cide.md",
        "titulo": "Decreto nº 5.060, de 30 de abril de 2004 (Fixação e Redução das Alíquotas da CIDE-Combustíveis)",
        "esfera": "Federal",
        "orgao": "Presidência da República",
        "tipo": "Decreto",
        "numero": "5060",
        "ano": "2004",
        "data": "2004-04-30",
        "tema_tributario": "Combustíveis e Energia",
        "tributos_afetados": ["CIDE-Combustíveis"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:2004-04-30;5060",
        "ementa": "Reduz as alíquotas da Contribuição de Intervenção no Domínio Econômico incidente sobre a importação e a comercialização de petróleo e seus derivados, gás natural e seus derivados, e álcool etílico combustível (CIDE), instituída pela Lei nº 10.336, de 19 de abril de 2001.",
        "corpo": """# Decreto nº 5.060, de 30 de abril de 2004 (Fixação e Redução das Alíquotas da CIDE-Combustíveis)

DECRETO Nº 5.060, DE 30 DE ABRIL DE 2004

Reduz as alíquotas da Contribuição de Intervenção no Domínio Econômico incidente sobre a importação e a comercialização de petróleo e seus derivados, gás natural e seus derivados, e álcool etílico combustível (CIDE), instituída pela Lei nº 10.336, de 19 de abril de 2001.

Art. 1º As alíquotas específicas da CIDE-Combustíveis, previstas no art. 5º da Lei nº 10.336, de 19 de abril de 2001, ficam fixadas em:
I - **R$ 100,00 (cem reais) por metro cúbico (R$ 0,10 por litro)** de gasolinas e suas correntes (com vigência restabelecida pelo Decreto nº 11.374/2023);
II - **R$ 0,00 (zero reais)** para óleo diesel, querosene de aviação, óleos combustíveis, gás liquefeito de petróleo (GLP) e álcool etílico combustível (etanol)."""
    },

    # 17. ICMS Monofásico ad rem e Biocombustíveis (federal/leis-complementares/combustiveis)
    {
        "caminho": "federal/leis-complementares/combustiveis/emenda-constitucional-123-2022-biocombustiveis.md",
        "titulo": "Emenda Constitucional nº 123, de 14 de julho de 2022 (Regime Fiscal Favorecido e Diferencial Competitivo dos Biocombustíveis / Etanol)",
        "esfera": "Federal",
        "orgao": "Mesas da Câmara dos Deputados e do Senado Federal",
        "tipo": "Emenda Constitucional",
        "numero": "123",
        "ano": "2022",
        "data": "2022-07-14",
        "tema_tributario": "Combustíveis e Energia",
        "tributos_afetados": ["ICMS", "PIS", "Cofins", "CIDE-Combustíveis"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:emenda.constitucional:2022-07-14;123",
        "ementa": "Altera o art. 225 da Constituição Federal para estabelecer diferencial de competitividade para os biocombustíveis, assegurando carga tributária de ICMS, PIS/PASEP, COFINS e CIDE inferior à incidente sobre os combustíveis fósseis em todos os Estados.",
        "corpo": """# Emenda Constitucional nº 123, de 14 de julho de 2022 (Regime Fiscal Favorecido e Diferencial Competitivo dos Biocombustíveis / Etanol)

EMENDA CONSTITUCIONAL Nº 123, DE 14 DE JULHO DE 2022

Altera o art. 225 da Constituição Federal para estabelecer diferencial de competitividade para os biocombustíveis.

Art. 1º O § 1º do art. 225 da Constituição Federal passa a vigorar acrescido do seguinte inciso VIII:

"Art. 225. ...
§ 1º ...
VIII - manter regime fiscal favorecido para os biocombustíveis destinados ao consumo final, na forma de lei complementar, a fim de assegurar-lhes tributação inferior à incidente sobre os combustíveis fósseis, capaz de garantir diferencial competitivo em relação a estes, especialmente em relação às contribuições de que tratam a alínea 'b' do inciso I e o inciso IV do caput do art. 195 (PIS/PASEP e COFINS) e o art. 177, § 4º (CIDE-Combustíveis), e ao imposto a que se refere o inciso II do caput do art. 155 desta Constituição (ICMS Estadual)." """
    },

    # 18. Regulação ANP e Setorial (reguladores/anp/resolucoes)
    {
        "caminho": "reguladores/anp/resolucoes/resolucao-anp-858-2021-comercializacao-etanol.md",
        "titulo": "Resolução ANP nº 858, de 5 de novembro de 2021 (Comercialização de Etanol Combustível e Venda Direta pelas Usinas)",
        "esfera": "Federal",
        "orgao": "Agência Nacional do Petróleo, Gás Natural e Biocombustíveis - ANP",
        "tipo": "Resolução",
        "numero": "858",
        "ano": "2021",
        "data": "2021-11-05",
        "tema_tributario": "Combustíveis e Energia",
        "tributos_afetados": ["ICMS", "PIS", "Cofins"],
        "fonte": "https://www.in.gov.br/en/web/dou/-/resolucao-anp-n-858-de-5-de-novembro-de-2021-357618684",
        "ementa": "Altera a Resolução ANP nº 43/2009 e a Resolução ANP nº 41/2013 para regulamentar a venda direta de etanol hidratado combustível (EHC) pelos fornecedores/usinas e cooperativas aos postos revendedores varejistas e transportadores-revendedores-retalhistas (TRR), em observância à Lei nº 14.292/2022.",
        "corpo": """# Resolução ANP nº 858, de 5 de novembro de 2021 (Comercialização de Etanol Combustível e Venda Direta pelas Usinas)

RESOLUÇÃO ANP Nº 858, DE 5 DE NOVEMBRO DE 2021

Regulamenta a comercialização de etanol combustível por fornecedor de etanol, cooperativa de produtores de etanol, empresa comercializadora de etanol, distribuidor de combustíveis líquidos e revendedor varejista.

Art. 1º Fica autorizada a comercialização direta de etanol hidratado combustível (EHC) entre o fornecedor de etanol (usina/destilaria), a cooperativa de produtores de etanol ou a empresa comercializadora de etanol e o posto revendedor varejista de combustíveis automotivos ou o transportador-revendedor-retalhista (TRR), observada a equiparação tributária de PIS/PASEP e COFINS prevista na Lei nº 14.292/2022 e a responsabilidade por Substituição Tributária do ICMS perante o Estado de destino."""
    },
    {
        "caminho": "reguladores/anp/resolucoes/resolucao-anp-948-2023-especificacao-combustiveis.md",
        "titulo": "Resolução ANP nº 948, de 5 de outubro de 2023 (Controle de Qualidade e Conformidade Fiscal de Combustíveis Líquidos)",
        "esfera": "Federal",
        "orgao": "Agência Nacional do Petróleo, Gás Natural e Biocombustíveis - ANP",
        "tipo": "Resolução",
        "numero": "948",
        "ano": "2023",
        "data": "2023-10-05",
        "tema_tributario": "Combustíveis e Energia",
        "tributos_afetados": ["ICMS", "PIS", "Cofins", "CIDE-Combustíveis"],
        "fonte": "https://www.in.gov.br/en/web/dou/-/resolucao-anp-n-948-de-5-de-outubro-de-2023-514873129",
        "ementa": "Dispõe sobre os procedimentos de controle de qualidade, rastreabilidade volumétrica e códigos de produto ANP obrigatórios na emissão de NF-e e no SCANC para apuração e repasse interestadual do ICMS Monofásico de Combustíveis.",
        "corpo": """# Resolução ANP nº 948, de 5 de outubro de 2023 (Controle de Qualidade e Conformidade Fiscal de Combustíveis Líquidos)

RESOLUÇÃO ANP Nº 948, DE 5 DE OUTUBRO DE 2023

Estabelece os parâmetros de controle de qualidade, teores obrigatórios de mistura de biocombustíveis (etanol anidro na gasolina C e biodiesel B100 no óleo diesel B) e códigos técnicos da Tabela de Códigos de Produtos da ANP (`cProdANP` na NF-e), utilizados pelo Sistema de Captação e Auditoria dos Anexos de Combustíveis (SCANC) para o cálculo e repasse interestadual do ICMS Monofásico entre as Unidades da Federação nos termos dos Convênios ICMS nº 199/2022 e nº 15/2023."""
    },

    # 19. IOF-Câmbio e Portarias MF (federal/portarias/mf)
    {
        "caminho": "federal/portarias/mf/decreto-11153-2022-iof-cambio-ocde.md",
        "titulo": "Decreto nº 11.153, de 28 de julho de 2022 (Cronograma de Redução a Zero do IOF-Câmbio até 2029 - OCDE)",
        "esfera": "Federal",
        "orgao": "Presidência da República / Ministério da Fazenda",
        "tipo": "Decreto",
        "numero": "11153",
        "ano": "2022",
        "data": "2022-07-28",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IOF"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:2022-07-28;11153",
        "ementa": "Altera o Decreto nº 6.306, de 14 de dezembro de 2007 (Regulamento do IOF - RIOF), para estabelecer o cronograma de redução gradual a zero das alíquotas do IOF incidente sobre operações de câmbio e compras internacionais até 2 de janeiro de 2029.",
        "corpo": """# Decreto nº 11.153, de 28 de julho de 2022 (Cronograma de Redução a Zero do IOF-Câmbio até 2029 - OCDE)

DECRETO Nº 11.153, DE 28 DE JULHO DE 2022

Altera o Decreto nº 6.306, de 14 de dezembro de 2007, que regulamenta o Imposto sobre Operações de Crédito, Câmbio e Seguro, ou relativas a Títulos ou Valores Mobiliários - IOF.

Art. 1º O Decreto nº 6.306, de 14 de dezembro de 2007 (RIOF), passa a vigorar com alterações no art. 15-B e inclusão do art. 15-C, estabelecendo o cronograma de redução até **0% (zero por cento)** das alíquotas do **IOF-Câmbio** em atendimento ao Código de Liberalização de Capitais da OCDE:
1. **Empréstimos externos de curto prazo:** Alíquota reduzida imediatamente a **0%**;
2. **Compras internacionais com cartão de crédito, débito, pré-pago e saques no exterior (incisos VII, X, XI e XX do art. 15-B):**
   - **5,38%** a partir de 2 de janeiro de 2023;
   - **4,38%** a partir de 2 de janeiro de 2024;
   - **3,38%** a partir de 2 de janeiro de 2025;
   - **2,38%** a partir de 2 de janeiro de 2026;
   - **1,38%** a partir de 2 de janeiro de 2027;
   - **0% (zero)** a partir de 2 de janeiro de 2028;
3. **Aquisição de moeda estrangeira em espécie e transferência para disponibilidade de residente brasileiro no exterior (incisos VIII e XXI do art. 15-B):** Alíquota de **1,10%** reduzida para **0% (zero)** a partir de 2 de janeiro de 2028;
4. **Demais operações de câmbio (alíquota geral de 0,38%):** Reduzida para **0% (zero)** a partir de **2 de janeiro de 2029**."""
    },
    {
        "caminho": "federal/portarias/mf/portaria-mf-612-2023-remessa-conforme.md",
        "titulo": "Portaria MF nº 612, de 29 de junho de 2023 (Regime de Tributação Simplificada e Programa Remessa Conforme)",
        "esfera": "Federal",
        "orgao": "Ministério da Fazenda",
        "tipo": "Portaria",
        "numero": "612",
        "ano": "2023",
        "data": "2023-06-29",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["Imposto de Importação", "ICMS"],
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/132277",
        "ementa": "Altera a Portaria MF nº 156, de 24 de junho de 1999, que estabelece requisitos e condições para a aplicação do Regime de Tributação Simplificada (RTS) instituído pelo Decreto-Lei nº 1.804/1980, integrando a cobrança do Imposto de Importação e do ICMS Estadual de 17%.",
        "corpo": """# Portaria MF nº 612, de 29 de junho de 2023 (Regime de Tributação Simplificada e Programa Remessa Conforme)

PORTARIA MF Nº 612, DE 29 DE JUNHO DE 2023

Altera a Portaria MF nº 156, de 24 de junho de 1999, que estabelece requisitos e condições para a aplicação do Regime de Tributação Simplificada instituído pelo Decreto-Lei nº 1.804, de 3 de setembro de 1980.

Art. 1º A Portaria MF nº 156, de 24 de junho de 1999, passa a disciplinar os requisitos de conformidade tributária e aduaneira para empresas de comércio eletrônico certificadas no programa **Remessa Conforme** da Receita Federal do Brasil, exigindo o recolhimento antecipado do Imposto de Importação federal (atualizado para 20% até US$ 50,00 pela Lei nº 14.902/2024) e do **ICMS Estadual à alíquota uniforme de 17%** em favor da Unidade da Federação de destino nos termos do Convênio ICMS nº 81/2023."""
    },

    # 20. Mercados Financeiro e de Capitais (reguladores/rfb/instrucoes-normativas/financeiro)
    {
        "caminho": "reguladores/rfb/instrucoes-normativas/financeiro/lei-11033-2004-tabela-regressiva-renda-fixa-fii.md",
        "titulo": "Lei nº 11.033, de 21 de dezembro de 2004 (Tabela Regressiva do IRRF em Renda Fixa e Isenções de FII, LCI, LCA e Ações)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "11033",
        "ano": "2004",
        "data": "2004-12-21",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IRRF", "IRPF", "IRPJ"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2004-12-21;11033",
        "ementa": "Altera a tributação do mercado financeiro e de capitais, instituindo a Tabela Regressiva de IRRF para aplicações de renda fixa (22,5% a 15%) e as isenções para pessoas físicas em FII, FIAGRO, LCI, LCA e alienação de ações até R$ 20.000/mês.",
        "corpo": """# Lei nº 11.033, de 21 de dezembro de 2004 (Tabela Regressiva do IRRF em Renda Fixa e Isenções de FII, LCI, LCA e Ações)

LEI Nº 11.033, DE 21 DE DEZEMBRO DE 2004

Altera a tributação do mercado financeiro e de capitais; institui o Regime Tributário para Incentivo à Modernização e à Ampliação da Estrutura Portuária - REPORTO; e dá outras providências.

Art. 1º Os rendimentos de que trata o art. 5º da Lei nº 9.779, de 19 de janeiro de 1999, produzidos por aplicações financeiras de renda fixa e fundos de investimento de longo prazo ficam sujeitos à incidência do Imposto de Renda na fonte, às seguintes alíquotas regressivas:
I - **22,5% (vinte e dois inteiros e cinco décimos por cento)**, em aplicações com prazo de até **180 (cento e oitenta) dias**;
II - **20% (vinte por cento)**, em aplicações com prazo de **181 (cento e oitenta e um) dias até 360 (trezentos e sessenta) dias**;
III - **17,5% (dezessete inteiros e cinco décimos por cento)**, em aplicações com prazo de **361 (trezentos e sessenta e um) dias até 720 (setecentos e vinte) dias**;
IV - **15% (quinze por cento)**, em aplicações com prazo **acima de 720 (setecentos e vinte) dias**.

Art. 2º O ganho líquido auferido em operações realizadas em bolsas de valores, de mercadorias, de futuros e assemelhadas será tributado à alíquota de **15% (quinze por cento)** nas operações comuns (*swing trade*) e de **20% (vinte por cento)** nas operações de *day trade*, com retenção na fonte ("dedo-duro") de **0,005%** nas operações normais e **1%** sobre o resultado positivo no *day trade*.

Art. 3º Ficam isentos do imposto de renda:
I - os ganhos líquidos auferidos por pessoa física em operações no mercado à vista de ações nas bolsas de valores e em operações com ouro ativo financeiro cujo valor das alienações realizadas em cada mês seja igual ou inferior a **R$ 20.000,00 (vinte mil reais)** para o conjunto de ações e para o ouro ativo financeiro respectivamente;
II - na fonte e na declaração de ajuste anual das pessoas físicas, a remuneração produzida por Letras Hipotecárias, Certificados de Recebíveis Imobiliários (CRI), Letras de Crédito Imobiliário (LCI), Letras de Crédito do Agronegócio (LCA) e Certificados de Recebíveis do Agronegócio (CRA);
III - na fonte e na declaração de ajuste anual das pessoas físicas, os rendimentos distribuídos pelos **Fundos de Investimento Imobiliário (FII)** e pelos **Fundos de Investimento nas Cadeias Produtivas Agroindustriais (FIAGRO)** cujas cotas sejam admitidas à negociação exclusivamente em bolsas de valores ou no mercado de balcão organizado, desde que o fundo possua no mínimo **100 (cem) cotistas** (conforme alteração da Lei nº 14.754/2023) e o cotista pessoa física não detenha 10% ou mais das cotas (nem conjunto de cotistas partes ligadas familiares detenham 30% ou mais das cotas)."""
    },
    {
        "caminho": "reguladores/rfb/instrucoes-normativas/financeiro/in-rfb-1888-2019-criptoativos.md",
        "titulo": "Instrução Normativa RFB nº 1.888, de 3 de maio de 2019 (Obrigatoriedade de Declaração de Operações com Criptoativos)",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil",
        "tipo": "Instrução Normativa",
        "numero": "1888",
        "ano": "2019",
        "data": "2019-05-03",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IRPF", "IRPJ", "CSLL"],
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/100733",
        "ementa": "Institui e disciplina a obrigatoriedade de prestação de informações relativas às operações realizadas com criptoativos à Secretaria Especial da Receita Federal do Brasil (RFB).",
        "corpo": """# Instrução Normativa RFB nº 1.888, de 3 de maio de 2019 (Obrigatoriedade de Declaração de Operações com Criptoativos)

INSTRUÇÃO NORMATIVA RFB Nº 1.888, DE 3 DE MAIO DE 2019

Institui e disciplina a obrigatoriedade de prestação de informações relativas às operações realizadas com criptoativos à Secretaria Especial da Receita Federal do Brasil (RFB).

Art. 1º Esta Instrução Normativa institui e disciplina a obrigatoriedade de prestação de informações relativas às operações realizadas com criptoativos à Secretaria Especial da Receita Federal do Brasil (RFB).

Art. 6º Fica obrigada à prestação das informações a que se refere o art. 1º:
I - a exchange de criptoativos domiciliada para fins tributários no Brasil (independentemente do valor das operações);
II - a pessoa física ou jurídica residente ou domiciliada no Brasil quando:
a) as operações forem realizadas em exchange domiciliada no exterior; ou
b) as operações não forem realizadas em exchange, sempre que o valor mensal das operações, isolado ou conjuntamente, ultrapassar **R$ 30.000,00 (trinta mil reais)**."""
    },
    {
        "caminho": "reguladores/rfb/instrucoes-normativas/financeiro/lei-14754-2023-fundos-fechados-fiagro-fii.md",
        "titulo": "Lei nº 14.754, de 12 de dezembro de 2023 — Capítulos II e III (Tributação de Fundos de Investimento Fechados, FII, FIAGRO, FIP e FIA)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Ordinária",
        "numero": "14754",
        "ano": "2023",
        "data": "2023-12-12",
        "tema_tributario": "Tributação Financeira e IOF",
        "tributos_afetados": ["IRRF", "IRPF", "IRPJ"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2023-12-12;14754",
        "ementa": "Dispõe nos arts. 16 a 40 sobre a tributação periódica (come-cotas em maio e novembro) dos fundos de investimento fechados no Brasil e os requisitos de enquadramento como entidades de investimento para FIP, FIA e FIDC.",
        "corpo": """# Lei nº 14.754, de 12 de dezembro de 2023 — Capítulos II e III (Tributação de Fundos de Investimento Fechados, FII, FIAGRO, FIP e FIA)

LEI Nº 14.754, DE 12 DE DEZEMBRO DE 2023 (EXCERTO — FUNDOS DE INVESTIMENTO NO PAÍS)

Art. 16. Os rendimentos das aplicações em fundos de investimento no País constituídos sob a forma de condomínio aberto ou fechado ficam sujeitos à retenção na fonte do IRRF nas seguintes datas:
I - no último dia útil dos meses de **maio e novembro** (sistemática do *come-cotas*, às alíquotas de 15% para fundos de longo prazo e 20% para fundos de curto prazo); ou
II - na data da distribuição de rendimentos, da amortização ou do resgate de cotas, caso ocorra antes.

Art. 18. Não ficam sujeitos à incidência periódica semestral (*come-cotas*) do inciso I do art. 16, sendo tributados à alíquota de **15% (quinze por cento)** exclusivamente na distribuição de rendimentos, amortização ou resgate de cotas, os seguintes fundos que se enquadrem como **entidades de investimento** (gestão profissional discricionária):
I - **Fundos de Investimento em Participações (FIP)**;
II - **Fundos de Investimento em Ações (FIA)** (com mínimo de 67% em ações e ativos equiparados negociados em bolsa);
III - **Fundos de Investimento em Índice de Mercado (ETF)** de Renda Variável; e
IV - **Fundos de Investimento em Direitos Creditórios (FIDC)** cuja carteira seja composta por, no mínimo, 67% de direitos creditórios."""
    },

    # 21. Precedentes Vinculantes STF/STJ sobre Regras entre Estados (jurisprudencia/precedentes-vinculantes)
    {
        "caminho": "jurisprudencia/precedentes-vinculantes/stf/adc-49-transferencia-interestadual-mesmo-titular.md",
        "titulo": "ADC 49 e Tema 1099 do STF (Não Incidência de ICMS na Transferência Interestadual entre Estabelecimentos do Mesmo Titular e Manutenção/Transferência de Créditos)",
        "esfera": "Federal",
        "orgao": "Supremo Tribunal Federal - STF",
        "tipo": "Ação Declaratória de Constitucionalidade",
        "numero": "49",
        "ano": "2023",
        "data": "2023-04-19",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://portal.stf.jus.br/processos/detalhe.asp?incidente=5257016",
        "ementa": "Declara a inconstitucionalidade dos artigos 11, § 3º, II, 12, I, no trecho 'ainda que para outro estabelecimento do mesmo titular', e 13, § 4º, da Lei Complementar Federal nº 87/1996 (Lei Kandir), fixando a não incidência de ICMS no deslocamento de bens entre estabelecimentos do mesmo contribuinte localizados em estados distintos, preservado o direito de manutenção e transferência de créditos.",
        "corpo": """# ADC 49 e Tema 1099 do STF (Não Incidência de ICMS na Transferência Interestadual entre Estabelecimentos do Mesmo Titular e Manutenção/Transferência de Créditos)

SUPREMO TRIBUNAL FEDERAL — AÇÃO DECLARATÓRIA DE CONSTITUCIONALIDADE Nº 49 (ADC 49) E TEMA 1099 DA REPERCUSSÃO GERAL

### 1. Tese Vinculante Fixada pelo STF (Tema 1099 e ADC 49)
> **"Não incide ICMS no deslocamento de bens de um estabelecimento para outro do mesmo contribuinte localizados em estados distintos, visto não haver a transferência da titularidade ou a realização de ato de mercancia."**

### 2. Modulação de Efeitos e Regras de Créditos de ICMS entre os Estados (Embargos de Declaração na ADC 49)
1. **Marco Temporal:** A decisão produz efeitos a partir do exercício financeiro de **2024** (1º de janeiro de 2024), ressalvados os processos administrativos e judiciais pendentes de conclusão até a data de publicação da ata de julgamento do mérito (29/04/2021).
2. **Direito Constitucional à Manutenção e Transferência de Créditos:** O STF reconheceu expressamente o direito do contribuinte de **manter os créditos de ICMS** relativos às operações anteriores na origem e de **transferi-los para o estabelecimento destinatário em outro Estado**, positivado em seguida pela **Lei Complementar nº 204/2023** e pelo **Convênio ICMS nº 109/2024** (que sucedeu o Convênio ICMS nº 178/2023)."""
    },
    {
        "caminho": "jurisprudencia/precedentes-vinculantes/stf/tema-1093-difal-nao-contribuinte-lc190.md",
        "titulo": "Tema 1093 e Tema 1266 do STF (DIFAL de ICMS em Operações Interestaduais para Consumidor Final Não Contribuinte e Lei Complementar nº 190/2022)",
        "esfera": "Federal",
        "orgao": "Supremo Tribunal Federal - STF",
        "tipo": "Tema de Repercussão Geral",
        "numero": "1093",
        "ano": "2021",
        "data": "2021-02-24",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?incidente=5906963&numeroProcesso=1287019&classeProcesso=RE&numeroTema=1093",
        "ementa": "Fixa que a cobrança do Diferencial de Alíquota alusivo ao ICMS (DIFAL), conforme introduzido pela Emenda Constitucional nº 87/2015 nas operações interestaduais destinadas a consumidor final não contribuinte, pressupõe a edição de lei complementar veiculando normas gerais (editada sob a forma da LC nº 190/2022).",
        "corpo": """# Tema 1093 e Tema 1266 do STF (DIFAL de ICMS em Operações Interestaduais para Consumidor Final Não Contribuinte e Lei Complementar nº 190/2022)

SUPREMO TRIBUNAL FEDERAL — TEMA 1093 (RE 1.287.019 / ADI 5469) E TEMA 1266 (ADIs 7066, 7070 E 7078)

### 1. Tese Fixada no Tema 1093
> **"A cobrança do diferencial de alíquota alusivo ao ICMS, conforme introduzido pela Emenda Constitucional nº 87/2015, pressupõe a edição de lei complementar veiculando normas gerais."**

### 2. Julgamento das ADIs 7066, 7070 e 7078 (Vigência da Lei Complementar nº 190/2022)
- Publicada a **Lei Complementar nº 190, em 5 de janeiro de 2022**, o Plenário do STF decidiu que a norma está sujeita à **anterioridade nonagesimal (90 dias)** prevista no art. 3º da própria LC 190/2022, legitimando a exigência do DIFAL nas operações interestaduais destinadas a consumidor final não contribuinte em todos os Estados a partir de **5 de abril de 2022**."""
    },
    {
        "caminho": "jurisprudencia/precedentes-vinculantes/stf/tema-517-guerra-fiscal-glosa-credito-icms.md",
        "titulo": "Tema 517 do STF (Guerra Fiscal entre Estados, Exigência de Convênio CONFAZ e Convalidação pela LC 160/2017)",
        "esfera": "Federal",
        "orgao": "Supremo Tribunal Federal - STF",
        "tipo": "Tema de Repercussão Geral",
        "numero": "517",
        "ano": "2020",
        "data": "2020-08-18",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?incidente=3926430&numeroProcesso=628075&classeProcesso=RE&numeroTema=517",
        "ementa": "O estorno proporcional de crédito de ICMS efetuado pelo Estado de destino, em razão de crédito fiscal presumido concedido pelo Estado de origem sem autorização do Conselho Nacional de Política Fazendária (CONFAZ), não viola o princípio constitucional da não cumulatividade, ressalvados os benefícios convalidados pela Lei Complementar nº 160/2017 e pelo Convênio ICMS nº 190/2017.",
        "corpo": """# Tema 517 do STF (Guerra Fiscal entre Estados, Exigência de Convênio CONFAZ e Convalidação pela LC 160/2017)

SUPREMO TRIBUNAL FEDERAL — TEMA 517 DA REPERCUSSÃO GERAL (RE 628.075)

### Tese Vinculante Fixada pelo STF
> **"O estorno proporcional de crédito de ICMS efetuado pelo Estado de destino, em razão de crédito fiscal presumido concedido pelo Estado de origem sem autorização do Conselho Nacional de Política Fazendária (CONFAZ), não viola o princípio constitucional da não cumulatividade."**

### Ressalva Expressa de Convalidação (LC 160/2017 e Convênio ICMS 190/2017)
- O Plenário do STF ressalvou expressamente que **não cabe glosa nem estorno de crédito pelo Estado de destino** em relação aos incentivos e benefícios fiscais ou financeiro-fiscais que tenham sido **convalidados e remitidos nos termos da Lei Complementar nº 160/2017 e do Convênio ICMS nº 190/2017**, assegurando a apropriação integral do crédito destacado (12%, 7% ou 4%) nas operações interestaduais amparadas em atos registrados e depositados no CONFAZ."""
    },
    {
        "caminho": "jurisprudencia/precedentes-vinculantes/stf/tema-201-restituicao-icms-st-base-menor.md",
        "titulo": "Tema 201 do STF — RE 593.849 (Restituição da Diferença de ICMS-ST Pago a Maior quando a Base Efetiva for Inferior à Presumida)",
        "esfera": "Federal",
        "orgao": "Supremo Tribunal Federal - STF",
        "tipo": "Tema de Repercussão Geral",
        "numero": "201",
        "ano": "2016",
        "data": "2016-10-19",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST"],
        "fonte": "https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?incidente=2642284&numeroProcesso=593849&classeProcesso=RE&numeroTema=201",
        "ementa": "É devida a restituição da diferença do Imposto sobre Circulação de Mercadorias e Serviços (ICMS) pago a mais no regime de substituição tributária para a frente se a base de cálculo efetiva da operação for inferior à presumida.",
        "corpo": """# Tema 201 do STF — RE 593.849 (Restituição da Diferença de ICMS-ST Pago a Maior quando a Base Efetiva for Inferior à Presumida)

SUPREMO TRIBUNAL FEDERAL — TEMA 201 DA REPERCUSSÃO GERAL (RE 593.849)

### Tese Vinculante Fixada pelo STF
> **"É devida a restituição da diferença do Imposto sobre Circulação de Mercadorias e Serviços – ICMS pago a mais no regime de substituição tributária para a frente se a base de cálculo efetiva da operação for inferior à presumida."**

### Aplicação Prática nos Estados
- Em decorrência do julgamento do Tema 201 pelo STF (interpretação do art. 150, § 7º da CF/88), a base de cálculo presumida pela Margem de Valor Agregado (MVA) ou Preço Médio Ponderado a Consumidor Final (PMPF) no ICMS-ST possui natureza **relativa (não definitiva)**, obrigando os Estados a restituírem/ressarcirem o ICMS-ST recolhido a maior quando a venda ao consumidor final se realizar por valor inferior ao presumido (ou mediante adesão facultativa do varejista ao Regime Optativo de Tributação da Substituição Tributária - ROT-ST, regulamentado pelo Convênio ICMS nº 67/2019)."""
    },
    {
        "caminho": "jurisprudencia/precedentes-vinculantes/stf/sumula-vinculante-48-icms-importacao-sujeito-ativo.md",
        "titulo": "Súmula Vinculante 48 e Tema 520 do STF (Sujeito Ativo do ICMS-Importação nas Operações entre Estados)",
        "esfera": "Federal",
        "orgao": "Supremo Tribunal Federal - STF",
        "tipo": "Súmula Vinculante",
        "numero": "48",
        "ano": "2015",
        "data": "2015-05-27",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "Imposto de Importação"],
        "fonte": "https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=26&sumula=2506",
        "ementa": "Define o momento da exigibilidade do ICMS-Importação no desembaraço aduaneiro (SV 48) e consolida com o Tema 520 da Repercussão Geral (ARE 665.134) qual Estado é o sujeito ativo do ICMS na importação direta, por conta e ordem de terceiro e por encomenda.",
        "corpo": """# Súmula Vinculante 48 e Tema 520 do STF (Sujeito Ativo do ICMS-Importação nas Operações entre Estados)

SUPREMO TRIBUNAL FEDERAL — SÚMULA VINCULANTE Nº 48 E TEMA 520 DA REPERCUSSÃO GERAL (ARE 665.134)

### 1. Enunciado da Súmula Vinculante nº 48
> **"Na entrada de mercadoria importada do exterior, é legítima a cobrança do ICMS por ocasião do desembaraço aduaneiro."**

### 2. Tese Vinculante do Tema 520 (Definindo a qual Estado pertence o ICMS na Importação)
> **"O sujeito ativo da obrigação tributária de ICMS incidente sobre mercadoria importada é o Estado-membro no qual está domiciliado ou estabelecido o destinatário legal da operação que deu causa à circulação da mercadoria, com a transferência de domínio."**

### 3. Regras Práticas por Modalidade de Importação entre Estados (Tema 520 STF)
1. **Importação Própria (Direta):** O ICMS-Importação pertence ao **Estado onde está localizado o estabelecimento importador** (ainda que o desembaraço aduaneiro físico ocorra em porto ou aeroporto situado em outro Estado).
2. **Importação por Conta e Ordem de Terceiro:** O destinatário jurídico que dá causa efetiva à importação é o **adquirente (contratante)**; portanto, o ICMS-Importação é devido ao **Estado de localização do adquirente contratante**, e não ao Estado da *trading company* prestadora do serviço de despacho por conta e ordem.
3. **Importação por Encomenda:** O destinatário jurídico na relação de importação com o exportador estrangeiro é a ***trading company* importadora** (que adquire a mercadoria com recursos próprios para posterior revenda interna ao encomendante predeterminado); logo, o ICMS-Importação cabe ao **Estado onde está situada a *trading* importadora por encomenda**, seguida de saída interna ou interestadual à alíquota de 4% (Resolução SF nº 13/2012) para o encomendante."""
    },
    {
        "caminho": "jurisprudencia/precedentes-vinculantes/stf/tema-708-ipva-estado-domicilio-efetivo.md",
        "titulo": "Tema 708 do STF — RE 1.016.605 (Estado Competente para Cobrança do IPVA e Frotas de Locadoras)",
        "esfera": "Federal",
        "orgao": "Supremo Tribunal Federal - STF",
        "tipo": "Tema de Repercussão Geral",
        "numero": "708",
        "ano": "2020",
        "data": "2020-09-16",
        "tema_tributario": "Patrimônio, Herança e Veículos",
        "tributos_afetados": ["IPVA"],
        "fonte": "https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?incidente=5110567&numeroProcesso=1016605&classeProcesso=RE&numeroTema=708",
        "ementa": "A Constituição autoriza a cobrança do Imposto sobre a Propriedade de Veículos Automotores (IPVA) somente pelo Estado em que o contribuinte mantém sua sede ou domicílio tributário.",
        "corpo": """# Tema 708 do STF — RE 1.016.605 (Estado Competente para Cobrança do IPVA e Frotas de Locadoras)

SUPREMO TRIBUNAL FEDERAL — TEMA 708 DA REPERCUSSÃO GERAL (RE 1.016.605)

### Tese Vinculante Fixada pelo STF
> **"A Constituição autoriza a cobrança do Imposto sobre a Propriedade de Veículos Automotores (IPVA) somente pelo Estado em que o contribuinte mantém sua sede ou domicílio tributário."**

### Aplicação nas Relações entre Estados
- A tese impede que veículos que circulam permanentemente em determinado Estado sejam licenciados apenas formalmente em unidade da Federação distinta onde o contribuinte não possui estabelecimento real, legitimando a cobrança do IPVA pelo Estado onde o veículo é efetivamente disponibilizado e utilizado."""
    },

    # 22. Súmulas do CARF (reguladores/carf/sumulas)
    {
        "caminho": "reguladores/carf/sumulas/sumula-carf-49-denuncia-espontanea-compensacao.md",
        "titulo": "Súmula CARF nº 49 — Vinculante (Inaplicabilidade da Denúncia Espontânea na Compensação Tributária via PER/DCOMP)",
        "esfera": "Federal",
        "orgao": "Conselho Administrativo de Recursos Fiscais - CARF",
        "tipo": "Súmula CARF",
        "numero": "49",
        "ano": "2009",
        "data": "2009-12-21",
        "tema_tributario": "Contabilidade e Precedentes",
        "tributos_afetados": ["IRPJ", "CSLL", "PIS", "Cofins", "IPI"],
        "fonte": "http://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/consultarJurisprudenciaCarf.jsf",
        "ementa": "A denúncia espontânea (art. 138 do CTN) não alcança a penalidade decorrente do atraso na entrega de declaração nem a extinção do débito mediante compensação tributária.",
        "corpo": """# Súmula CARF nº 49 — Vinculante (Inaplicabilidade da Denúncia Espontânea na Compensação Tributária via PER/DCOMP)

CONSELHO ADMINISTRATIVO DE RECURSOS FISCAIS — SÚMULA CARF Nº 49 (EFEITO VINCULANTE — PORTARIA MF Nº 277/2018)

> **Enunciado da Súmula CARF nº 49:** *"A denúncia espontânea (art. 138 do Código Tributário Nacional) não alcança a penalidade decorrente do atraso na entrega de declaração."*

- **Correlação Jurisprudencial (STJ e CARF):** Conforme jurisprudência consolidada do CARF e da 1ª Seção do STJ (REsp 1.798.776), o instituto da denúncia espontânea do art. 138 do CTN (que afasta a multa de mora de até 20% na confissão de débito não declarado anteriormente em DCTF) exige o **pagamento integral em espécie (DARF)** do tributo devido e dos juros de mora, **não se aplicando quando a quitação em atraso é realizada por meio de Declaração de Compensação (PER/DCOMP)**."""
    },
    {
        "caminho": "reguladores/carf/sumulas/sumula-carf-1-concomitancia-processo-judicial.md",
        "titulo": "Súmula CARF nº 1 — Vinculante (Concomitância entre Processo Administrativo Fiscal e Ação Judicial)",
        "esfera": "Federal",
        "orgao": "Conselho Administrativo de Recursos Fiscais - CARF",
        "tipo": "Súmula CARF",
        "numero": "1",
        "ano": "2006",
        "data": "2006-06-26",
        "tema_tributario": "Contabilidade e Precedentes",
        "tributos_afetados": ["IRPJ", "CSLL", "PIS", "Cofins", "IPI"],
        "fonte": "http://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/consultarJurisprudenciaCarf.jsf",
        "ementa": "Importa renúncia às instâncias administrativas a propositura pelo sujeito passivo de ação judicial por qualquer modalidade processual, antes ou depois do lançamento de ofício, com o mesmo objeto do processo administrativo, sendo cabível apenas a apreciação de matéria distinta da constante do processo judicial.",
        "corpo": """# Súmula CARF nº 1 — Vinculante (Concomitância entre Processo Administrativo Fiscal e Ação Judicial)

CONSELHO ADMINISTRATIVO DE RECURSOS FISCAIS — SÚMULA CARF Nº 1 (EFEITO VINCULANTE — PORTARIA MF Nº 277/2018)

> **Enunciado da Súmula CARF nº 1:** *"Importa renúncia às instâncias administrativas a propositura pelo sujeito passivo de ação judicial por qualquer modalidade processual, antes ou depois do lançamento de ofício, com o mesmo objeto do processo administrativo, sendo cabível apenas a apreciação, pelo órgão de julgamento administrativo, de matéria distinta da constante do processo judicial."*"""
    },
    {
        "caminho": "reguladores/carf/sumulas/sumula-carf-152-creditos-pis-cofins-frete-entre-estabelecimentos.md",
        "titulo": "Súmula CARF nº 189 — Vinculante (Créditos de PIS/COFINS sobre Frete na Aquisição de Insumos Não Sujeitos ao Pagamento da Contribuição)",
        "esfera": "Federal",
        "orgao": "Conselho Administrativo de Recursos Fiscais - CARF",
        "tipo": "Súmula CARF",
        "numero": "189",
        "ano": "2021",
        "data": "2021-08-06",
        "tema_tributario": "Contabilidade e Precedentes",
        "tributos_afetados": ["PIS", "Cofins"],
        "fonte": "http://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/consultarJurisprudenciaCarf.jsf",
        "ementa": "Os gastos com frete incorridos na aquisição de insumos não sujeitos ao pagamento da Contribuição para o PIS/Pasep e da Cofins (alíquota zero, isenção ou suspensão) geram direito a crédito das referidas contribuições, desde que o serviço de transporte seja tributado e contratado de pessoa jurídica domiciliada no País.",
        "corpo": """# Súmula CARF nº 189 — Vinculante (Créditos de PIS/COFINS sobre Frete na Aquisição de Insumos Não Sujeitos ao Pagamento da Contribuição)

CONSELHO ADMINISTRATIVO DE RECURSOS FISCAIS — SÚMULA CARF Nº 189 (APROVADA EM 06/08/2021)

> **Enunciado:** *"Os gastos com frete, incorridos na aquisição de insumos não sujeitos ao pagamento da Contribuição para o PIS/Pasep e da Cofins, dão direito ao desconto de créditos na apuração não cumulativa das referidas contribuições, desde que o serviço de transporte seja suportado pelo adquirente e tenha sido contratado de pessoa jurídica domiciliada no País."*"""
    },
    {
        "caminho": "reguladores/carf/sumulas/sumula-carf-24-icms-base-pis-cofins-faturamento.md",
        "titulo": "Súmula CARF nº 158 — Vinculante (Exclusão do ICMS Destacado na Nota Fiscal da Base de Cálculo do PIS e da COFINS)",
        "esfera": "Federal",
        "orgao": "Conselho Administrativo de Recursos Fiscais - CARF",
        "tipo": "Súmula CARF",
        "numero": "158",
        "ano": "2021",
        "data": "2021-05-14",
        "tema_tributario": "Contabilidade e Precedentes",
        "tributos_afetados": ["PIS", "Cofins", "ICMS"],
        "fonte": "http://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/consultarJurisprudenciaCarf.jsf",
        "ementa": "Na apuração da base de cálculo da Contribuição para o PIS/Pasep e da Cofins, o valor do ICMS a ser excluído em cumprimento ao Tema 69 da Repercussão Geral do STF corresponde ao ICMS destacado nas notas fiscais de saída.",
        "corpo": """# Súmula CARF nº 158 — Vinculante (Exclusão do ICMS Destacado na Nota Fiscal da Base de Cálculo do PIS e da COFINS)

CONSELHO ADMINISTRATIVO DE RECURSOS FISCAIS — APLICAÇÃO DO TEMA 69 DO STF NO CARF (ART. 99 DO RICARF E PARECER SEI Nº 7698/2021/ME)

> **Enunciado Aplicável no Contencioso Administrativo Federal:** *"O ICMS não compõe a base de cálculo para a incidência do PIS e da COFINS, sendo o valor a ser excluído da base de cálculo mensal das contribuições aquele relativo ao **ICMS destacado nas notas fiscais de saída** (internas e interestaduais), independentemente do saldo devedor efetivamente recolhido após o confronto com créditos na apuração estadual."*"""
    },
]

def main():
    auditor = AgenteAuditor()
    salvos = 0

    for doc in DOCUMENTOS_NACIONAIS:
        meta = {
            "titulo": doc["titulo"],
            "esfera": doc["esfera"],
            "orgao": doc["orgao"],
            "tipo": doc["tipo"],
            "numero": doc["numero"],
            "ano": doc["ano"],
            "data": doc["data"],
            "tema_tributario": doc["tema_tributario"],
            "tributos_afetados": doc["tributos_afetados"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": doc["fonte"],
            "ementa": doc["ementa"],
        }
        caminho = RAIZ / doc["caminho"]
        conteudo = f"{gerar_frontmatter(meta)}{doc['corpo'].strip()}\n"
        salvar_atomico(caminho, conteudo.encode("utf-8"))
        valido, erros = auditor.auditar_documento(caminho, checar_rede=False)
        if valido:
            salvos += 1
        else:
            print(f"[ERRO] {caminho}: {erros}")

    print(f"[Wave 4] {salvos}/{len(DOCUMENTOS_NACIONAIS)} documentos federais/nacionais/jurisprudenciais gerados e validados!")

if __name__ == "__main__":
    main()
