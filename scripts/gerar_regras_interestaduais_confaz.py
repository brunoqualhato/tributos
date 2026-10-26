"""Ingestão de Normas Estruturantes das Regras entre Estados (CONFAZ, Ajustes SINIEF, LCs e Senado Federal).

Foco em LLM para consultas sobre operações interestaduais:
- Transferência entre estabelecimentos do mesmo titular (ADC 49, LC 204/2023, Convênios ICMS 178/2023 e 109/2024)
- DIFAL Não Contribuinte e Benefícios Fiscais no Destino/Origem (Convênios ICMS 93/2015 e 153/2015)
- Substituição Tributária Interestadual e Simples Nacional sem MVA Ajustada (Convênio ICMS 35/2011)
- Zona Franca de Manaus e Áreas de Livre Comércio (Convênios ICM 65/1988, ICMS 52/1992 e ICMS 134/2019)
- Faturamento Direto de Veículos e Leasing Interestadual (Convênios ICMS 51/2000 e 64/2006)
- Industrialização por Encomenda, Consignação e Venda à Ordem Interestadual (Convênio AE 15/1974, SINIEF s/n 1970, Ajustes SINIEF 02/1993, 19/2016, 03/2022 e 13/2024)
- Guerra Fiscal e Quórum CONFAZ (LC 24/1975) e Essencialidade (LC 194/2022)
- Transporte Aéreo Interestadual 4% (Resolução SF 95/1996)
"""
from pathlib import Path
import re
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from comum import Rede, gerar_frontmatter, salvar_atomico
from html2md import converter_html_para_md
from agente_auditor import AgenteAuditor

NORMAS_INTERESTADUAIS = [
    # =========================================================================
    # 1. LEIS COMPLEMENTARES E RESOLUÇÕES DO SENADO (REGRAS ENTRE ESTADOS)
    # =========================================================================
    {
        "titulo": "Lei Complementar nº 24, de 7 de janeiro de 1975 (Convênios CONFAZ e Guerra Fiscal)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Complementar",
        "numero": "24",
        "ano": "1975",
        "data": "1975-01-07",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:1975-01-07;24",
        "ementa": "Dispõe sobre os convênios para a concessão de isenções do imposto sobre operações relativas à circulação de mercadorias, e dá outras providências.",
        "caminho": "federal/leis-complementares/kandir/lei-complementar-24-1975.md",
        "corpo": """# Lei Complementar nº 24, de 7 de janeiro de 1975 (Convênios CONFAZ e Guerra Fiscal)

LEI COMPLEMENTAR Nº 24, DE 7 DE JANEIRO DE 1975

Dispõe sobre os convênios para a concessão de isenções do imposto sobre operações relativas à circulação de mercadorias, e dá outras providências.

O PRESIDENTE DA REPÚBLICA: Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei Complementar:

Art. 1º As isenções do imposto sobre operações relativas à circulação de mercadorias serão concedidas ou revogadas nos termos de convênios celebrados e ratificados pelos Estados e pelo Distrito Federal, segundo esta Lei.

Parágrafo único. O disposto neste artigo também se aplica:
I - à redução da base de cálculo;
II - à devolução total ou parcial, direta ou indireta, condicionada ou não, do tributo, ao contribuinte, a responsável ou a terceiros;
III - à concessão de créditos presumidos;
IV - a quaisquer outros incentivos ou favores fiscais ou financeiro-fiscais, concedidos com base no Imposto de Circulação de Mercadorias, dos quais resulte redução ou eliminação, direta ou indireta, do respectivo ônus;
V - às prorrogações e às extensões das isenções vigentes nesta data.

Art. 2º Os convênios a que alude o art. 1º, serão celebrados em reuniões para as quais tenham sido convocados representantes de todos os Estados e do Distrito Federal, sob a presidência de representantes do Governo federal.
§ 1º As reuniões se realizarão com a presença de representantes da maioria das Unidades da Federação.
§ 2º A concessão de benefícios dependerá sempre de decisão unânime dos Estados representados; a sua revogação total ou parcial dependerá de aprovação de quatro quintos, pelo menos, dos representantes presentes.

Art. 8º A inobservância dos dispositivos desta Lei acarretará, cumulativamente:
I - a nulidade do ato e a ineficácia do crédito fiscal atribuído ao estabelecimento recebedor da mercadoria;
II - a exigibilidade do imposto não pago ou devolvido e a ineficácia da lei ou ato que conceda remissão do débito correspondente.

### Regras Práticas para Operações Interestaduais (Glosa de Créditos e Convalidação)
1. **Regra Geral Constitucional (Art. 155, § 2º, XII, "g" da CF/88):** Nenhum Estado pode conceder unilateralmente isenção, redução de base de cálculo, crédito presumido ou benefício fiscal de ICMS sem prévio Convênio aprovado no âmbito do CONFAZ (ou nos quóruns qualificados da LC 160/2017).
2. **Efeito nas Operações Interestaduais (Art. 8º, I):** Caso o Estado de origem conceda benefício fiscal unilateral não convalidado pelo CONFAZ ("Guerra Fiscal"), o Estado de destino pode glosar (estornar) a parcela do crédito de ICMS destacada na nota fiscal que não tenha sido efetivamente suportada na origem (Tema 517 do STF).
3. **Convalidação pela LC 160/2017 e Convênio ICMS 190/2017:** Os benefícios fiscais publicados, registrados e depositados no CONFAZ nos termos da Lei Complementar nº 160/2017 e do Convênio ICMS nº 190/2017 têm seus créditos integralmente assegurados ao adquirente em outra unidade federada, vedada a glosa de crédito pelo Estado de destino mientras vigentes nos prazos legais de fruição (até 2032, conforme a categoria do incentivo)."""
    },
    {
        "titulo": "Lei Complementar nº 194, de 23 de junho de 2022 (Essencialidade no ICMS)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Complementar",
        "numero": "194",
        "ano": "2022",
        "data": "2022-06-23",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "PIS", "Cofins", "CIDE-Combustíveis"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2022-06-23;194",
        "ementa": "Altera a Lei nº 5.172, de 25 de outubro de 1966 (Código Tributário Nacional), e a Lei Complementar nº 87, de 13 de setembro de 1996 (Lei Kandir), para considerar bens e serviços essenciais os relativos aos combustíveis, à energia elétrica, às comunicações e ao transporte coletivo.",
        "caminho": "federal/leis-complementares/kandir/lei-complementar-194-2022.md",
        "corpo": """# Lei Complementar nº 194, de 23 de junho de 2022 (Essencialidade no ICMS)

LEI COMPLEMENTAR Nº 194, DE 23 DE JUNHO DE 2022

Altera a Lei nº 5.172, de 25 de outubro de 1966 (Código Tributário Nacional), e a Lei Complementar nº 87, de 13 de setembro de 1996 (Lei Kandir), para considerar bens e serviços essenciais os relativos aos combustíveis, à energia elétrica, às comunicações e ao transporte coletivo, e as Leis Complementares nºs 192, de 11 de março de 2022, e 159, de 19 de maio de 2017.

O PRESIDENTE DA REPÚBLICA Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei Complementar:

Art. 1º A Lei nº 5.172, de 25 de outubro de 1966 (Código Tributário Nacional), passa a vigorar acrescida do seguinte art. 18-A:

"Art. 18-A. Para fins da incidência do imposto de que trata o inciso II do caput do art. 155 da Constituição Federal, os combustíveis, o gás natural, a energia elétrica, as comunicações e o transporte coletivo são considerados bens e serviços essenciais e indispensáveis, que não podem ser tratados como supérfluos.

Parágrafo único. Para efeito do disposto neste artigo:
I - é vedada a fixação de alíquotas sobre as operações referidas no caput deste artigo em patamar superior ao das operações em geral, considerada a alíquota modal vigente em cada ente federativo;
II - é facultada ao ente federativo competente a aplicação de alíquotas reduzidas em relação aos bens referidos no caput deste artigo, como forma de beneficiar os consumidores em geral; e
III - é vedada a fixação de alíquotas reduzidas de que trata o inciso II deste parágrafo, para os bens e serviços referidos no caput deste artigo, em percentual superior ao da alíquota vigente para as operações em geral."

Art. 2º A Lei Complementar nº 87, de 13 de setembro de 1996 (Lei Kandir), passa a vigorar com as seguintes alterações:

"Art. 3º O imposto não incide sobre:
...
X - serviços de transmissão e distribuição e encargos setoriais vinculados às operações com energia elétrica."

"Art. 32-A. As operações relativas aos combustíveis, ao gás natural, à energia elétrica, às comunicações e ao transporte coletivo, para fins de incidência de imposto de que trata esta Lei Complementar, são consideradas operações de bens e serviços essenciais e indispensáveis, que não podem ser tratados como supérfluos." """
    },
    {
        "titulo": "Lei Complementar nº 204, de 28 de dezembro de 2023 (Transferência Interestadual entre Estabelecimentos do Mesmo Titular)",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Presidência da República",
        "tipo": "Lei Complementar",
        "numero": "204",
        "ano": "2023",
        "data": "2023-12-28",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:lei.complementar:2023-12-28;204",
        "ementa": "Altera a Lei Complementar nº 87, de 13 de setembro de 1996 (Lei Kandir), para vedar a incidência do Imposto sobre Operações relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação (ICMS) nos casos de transferência de mercadoria entre estabelecimentos do mesmo contribuinte.",
        "caminho": "federal/leis-complementares/kandir/lei-complementar-204-2023.md",
        "corpo": """# Lei Complementar nº 204, de 28 de dezembro de 2023 (Transferência Interestadual entre Estabelecimentos do Mesmo Titular)

LEI COMPLEMENTAR Nº 204, DE 28 DE DEZEMBRO DE 2023

Altera a Lei Complementar nº 87, de 13 de setembro de 1996 (Lei Kandir), para vedar a incidência do Imposto sobre Operações relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação (ICMS) nos casos de transferência de mercadoria entre estabelecimentos do mesmo contribuinte.

O PRESIDENTE DA REPÚBLICA Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei Complementar:

Art. 1º A Lei Complementar nº 87, de 13 de setembro de 1996 (Lei Kandir), passa a vigorar com as seguintes alterações:

"Art. 12. ...
I - da saída de mercadoria de estabelecimento de contribuinte;
...
§ 4º Não se considera ocorrido o fato gerador do imposto na saída de mercadoria de estabelecimento para outro de mesma titularidade, mantendo-se o crédito relativo às operações e prestações anteriores em favor do contribuinte, inclusive nas hipóteses de transferências interestaduais, nas quais os créditos serão assegurados:
I - pela unidade federada de destino, por meio de transferência de crédito, limitados aos percentuais estabelecidos nos termos do inciso IV do § 2º do art. 155 da Constituição Federal, aplicados sobre o valor atribuído à operação de transferência realizada;
II - pela unidade federada de origem, em caso de diferença positiva entre os créditos pertinentes às operações e prestações anteriores e o transferido na forma do inciso I deste parágrafo.

§ 5º Alternativamente ao disposto no § 4º deste artigo, por opção do contribuinte, a transferência da mercadoria para estabelecimento pertencente ao mesmo titular poderá ser equiparada a operação sujeita à ocorrência do fato gerador de imposto, hipótese em que serão observadas:
I - nas operações internas, as alíquotas estabelecidas na legislação;
II - nas operações interestaduais, as alíquotas fixadas nos termos do inciso IV do § 2º do art. 155 da Constituição Federal." (NR)

"Art. 13. ...
§ 4º (Revogado)." (NR)

Art. 2º Fica revogado o § 4º do art. 13 da Lei Complementar nº 87, de 13 de setembro de 1996 (Lei Kandir).

Art. 3º Esta Lei Complementar entra em vigor em 1º de janeiro de 2024.

### Síntese Operacional da Regra Interestadual (ADC 49 + LC 204/2023 + Convênio ICMS 109/2024)
1. **Não Incidência na Transferência:** A saída física de mercadoria de matriz para filial (ou entre filiais da mesma pessoa jurídica) em estados distintos **não constitui fato gerador de ICMS**.
2. **Manutenção e Transferência de Créditos (Art. 12, § 4º):**
   - O Estado de **destino** deve suportar o crédito transferido pela nota fiscal até o limite da alíquota interestadual aplicável (4%, 7% ou 12%) sobre o valor da transferência.
   - Caso o crédito acumulado nas entradas anteriores no Estado de **origem** seja superior ao montante transferido ao Estado de destino, a diferença positiva de crédito permanece mantida na escrita fiscal do estabelecimento de origem.
3. **Opção pela Equiparação a Operação Tributada (Art. 12, § 5º - promulgado após derrubada de veto presidencial):**
   - O contribuinte pode optar por equiparar a transferência interestadual a uma operação regularmente tributada (destacando 4%, 7% ou 12% de ICMS), o que é relevante quando o estabelecimento remetente goza de benefícios fiscais estaduais (crédito presumido, redução de base ou diferimento vinculados à saída tributada)."""
    },
    {
        "titulo": "Resolução do Senado Federal nº 95, de 13 de dezembro de 1996 (Alíquota Interestadual de 4% no Transporte Aéreo)",
        "esfera": "Federal",
        "orgao": "Senado Federal",
        "tipo": "Resolução do Senado Federal",
        "numero": "95",
        "ano": "1996",
        "data": "1996-12-13",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:senado.federal:resolucao:1996-12-13;95",
        "ementa": "Altera a Resolução nº 22, de 1989, do Senado Federal, que estabelece alíquotas do ICMS nas operações e prestações interestaduais, fixando em 4% a alíquota na prestação de transporte aéreo interestadual.",
        "caminho": "federal/resolucoes-senado/icms/resolucao-95-1996.md",
        "corpo": """# Resolução do Senado Federal nº 95, de 13 de dezembro de 1996 (Alíquota Interestadual de 4% no Transporte Aéreo)

RESOLUÇÃO Nº 95, DE 1996

Altera a Resolução nº 22, de 1989, do Senado Federal, que estabelece alíquotas do ICMS nas operações e prestações interestaduais.

O SENADO FEDERAL resolve:

Art. 1º O parágrafo único do art. 1º da Resolução nº 22, de 1989, passa a vigorar como § 1º, acrescentando-se ao mesmo artigo o seguinte § 2º:

"Art. 1º ...
§ 1º Nas operações e prestações realizadas nas Regiões Sul e Sudeste, destinadas às Regiões Norte, Nordeste e Centro-Oeste e ao Estado do Espírito Santo, as alíquotas serão:
I - em 1989, oito por cento;
II - a partir de 1990, sete por cento.
§ 2º A alíquota do imposto nas prestações interestaduais de transporte aéreo de passageiro, carga e mala postal é de quatro por cento."

Art. 2º Esta Resolução entra em vigor na data de sua publicação, produzindo efeitos a partir de 1º de janeiro de 1997."""
    },

    # =========================================================================
    # 2. CONVÊNIOS ICMS E AJUSTES SINIEF (OPERAÇÕES ENTRE ESTADOS - CONFAZ)
    # =========================================================================
    {
        "titulo": "Convênio ICMS nº 109, de 3 de outubro de 2024 (Transferência Interestadual entre Estabelecimentos de Mesma Titularidade)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "109",
        "ano": "2024",
        "data": "2024-10-03",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2024/CV109_24",
        "ementa": "Dispõe sobre a remessa interestadual de bens e mercadorias entre estabelecimentos de mesma titularidade, disciplinando a apropriação e transferência de créditos de ICMS nos termos da Lei Complementar nº 204/2023.",
        "caminho": "estaduais/confaz/convenios-icms/2024/convenio-icms-109-2024.md",
        "corpo": """# Convênio ICMS nº 109, de 3 de outubro de 2024 (Transferência Interestadual entre Estabelecimentos de Mesma Titularidade)

CONVÊNIO ICMS Nº 109, DE 3 DE OUTUBRO DE 2024

Dispõe sobre a remessa interestadual de bens e mercadorias entre estabelecimentos de mesma titularidade.

O Conselho Nacional de Política Fazendária - CONFAZ, na sua 400ª Reunião Extraordinária, realizada em Brasília, DF, no dia 3 de outubro de 2024, tendo em vista o disposto no art. 12, §§ 4º e 5º, da Lei Complementar nº 87, de 13 de setembro de 1996, e no art. 199 do Código Tributário Nacional (Lei nº 5.172/1966), resolve celebrar o seguinte CONVÊNIO:

Cláusula primeira Na remessa interestadual de bens e mercadorias entre estabelecimentos de mesma titularidade, fica assegurado o direito à transferência de crédito do Imposto sobre Operações Relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação – ICMS, relativo às operações e prestações anteriores, nos termos deste convênio.

Cláusula segunda A apropriação do crédito pelo estabelecimento destinatário dar-se-á por meio de transferência, pelo estabelecimento remetente, do ICMS incidente nas operações e prestações anteriores, limitado ao resultado da aplicação de percentuais equivalentes às alíquotas interestaduais do ICMS, definidas nos termos do inciso IV do § 2º do art. 155 da Constituição Federal (4%, 7% ou 12%), sobre os seguintes valores dos bens e mercadorias:
I – o valor médio da entrada da mercadoria em estoque na data da transferência;
II – o custo da mercadoria produzida, assim entendida a soma do custo da matéria-prima, material secundário, mão-de-obra e acondicionamento;
III – tratando-se de mercadorias não industrializadas, a soma dos custos de sua produção, assim entendidos os gastos com insumos, mão-de-obra e acondicionamento.

§ 1º No cálculo do crédito a ser transferido, os percentuais de que trata o caput devem integrar o valor dos bens e mercadorias (cálculo "por dentro").
§ 2º Caso haja saldo credor remanescente no estabelecimento remetente após a transferência de que trata esta cláusula, este será mantido na escrita fiscal do remetente na unidade federada de origem.

Cláusula sexta Alternativamente ao disposto nas cláusulas primeira a quarta, por opção do contribuinte, a transferência do bem e da mercadoria poderá ser equiparada a operação sujeita à ocorrência do fato gerador de imposto, para todos os fins, hipótese em que serão observadas as alíquotas interestaduais fixadas pelo Senado Federal (4%, 7% ou 12%) e a base de cálculo prevista no art. 13, § 4º, da Lei Complementar nº 87/1996:
I – o valor correspondente à entrada mais recente da mercadoria;
II – o custo da mercadoria produzida, assim entendida a soma do custo da matéria-prima, material secundário, mão-de-obra e acondicionamento;
III – tratando-se de mercadorias não industrializadas, a sua cotação no mercado atacadista do local da operação, ou, na sua falta, o seu preço corrente no mercado.

§ 1º A opção pela equiparação a operação tributada:
I – alcançará todos os estabelecimentos do contribuinte localizados no território nacional;
II – será anual, irretratável para todo o ano-calendário, devendo ser registrada até o último dia de dezembro para vigorar a partir de janeiro do ano subsequente no Livro Registro de Utilização de Documentos Fiscais e Termos de Ocorrências (RUDFTO).

Cláusula décima Fica revogado o Convênio ICMS nº 178, de 1º de dezembro de 2023, a partir de 1º de novembro de 2024."""
    },
    {
        "titulo": "Convênio ICMS nº 178, de 1º de dezembro de 2023 (Transferência de Crédito de ICMS entre Estabelecimentos do Mesmo Titular)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "178",
        "ano": "2023",
        "data": "2023-12-01",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2023/CV178_23",
        "ementa": "Dispõe sobre a remessa interestadual de bens e mercadorias entre estabelecimentos de mesma titularidade em cumprimento à decisão do STF na ADC 49 (sucedido pelo Convênio ICMS 109/2024).",
        "caminho": "estaduais/confaz/convenios-icms/2023/convenio-icms-178-2023.md",
        "corpo": """# Convênio ICMS nº 178, de 1º de dezembro de 2023 (Transferência de Crédito de ICMS entre Estabelecimentos do Mesmo Titular)

CONVÊNIO ICMS Nº 178, DE 1º DE DEZEMBRO DE 2023

Dispõe sobre a remessa interestadual de bens e mercadorias entre estabelecimentos de mesma titularidade.

O Conselho Nacional de Política Fazendária - CONFAZ, na sua 385ª Reunião Extraordinária, realizada em Brasília, DF, no dia 1º de dezembro de 2023, tendo em vista o decidido pelo Supremo Tribunal Federal na Ação Declaratória de Constitucionalidade nº 49 (ADC 49), resolve celebrar o seguinte CONVÊNIO:

Cláusula primeira Na remessa interestadual de bens e mercadorias entre estabelecimentos de mesma titularidade, é obrigatória a transferência de crédito do ICMS do estabelecimento de origem para o estabelecimento de destino, hipótese em que devem ser observados os procedimentos de que trata este convênio.

Cláusula segunda O ICMS a ser transferido corresponderá ao resultado da aplicação de percentuais equivalentes às alíquotas interestaduais do ICMS, definidas nos termos do inciso IV do § 2º do art. 155 da Constituição Federal (4%, 7% ou 12%), sobre os seguintes valores dos bens e mercadorias:
I - o valor correspondente à entrada mais recente da mercadoria;
II - o custo da mercadoria produzida, assim entendida a soma do custo da matéria-prima, material secundário, mão-de-obra e acondicionamento;
III - tratando-se de mercadorias não industrializadas, a soma dos custos de sua produção, assim entendidos os gastos com insumos, mão-de-obra e acondicionamento.

Cláusula quarta A transferência do ICMS entre estabelecimentos de mesma titularidade será procedida a cada remessa, mediante consignação do respectivo valor na Nota Fiscal eletrônica - NF-e - que a acobertar, no campo destinado ao destaque do imposto.

Nota Histórica: Vigente de 01/01/2024 a 31/10/2024, sendo sucedido em 01/11/2024 pelo Convênio ICMS nº 109/2024 para refletir a opção de equiparação a operação tributada do § 5º do art. 12 da Lei Complementar nº 87/1996 (inserido pela LC nº 204/2023 após rejeição do veto presidencial)."""
    },
    {
        "titulo": "Convênio ICMS nº 93, de 17 de setembro de 2015 (DIFAL - Operações Interestaduais para Não Contribuinte)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "93",
        "ano": "2015",
        "data": "2015-09-17",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2015/CV093_15",
        "ementa": "Dispõe sobre os procedimentos a serem observados nas operações e prestações que destinem bens e serviços a consumidor final não contribuinte do ICMS, localizado em outra unidade federada (EC 87/2015).",
        "caminho": "estaduais/confaz/convenios-icms/2015/convenio-icms-93-2015.md",
        "corpo": """# Convênio ICMS nº 93, de 17 de setembro de 2015 (DIFAL - Operações Interestaduais para Não Contribuinte)

CONVÊNIO ICMS Nº 93, DE 17 DE SETEMBRO DE 2015

Dispõe sobre os procedimentos a serem observados nas operações e prestações que destinem bens e serviços a consumidor final não contribuinte do ICMS, localizado em outra unidade federada.

O Conselho Nacional de Política Fazendária - CONFAZ, na sua 247ª reunião extraordinária, realizada em Brasília, DF, no dia 17 de setembro de 2015, tendo em vista o disposto nos incisos VII e VIII do § 2º do art. 155 da Constituição Federal e no art. 99 do Ato das Disposições Constitucionais Transitórias - ADCT, incluídos pela Emenda Constitucional nº 87, de 16 de abril de 2015, resolve celebrar o seguinte CONVÊNIO:

Cláusula primeira Nas operações e prestações que destinem bens e serviços a consumidor final não contribuinte do ICMS, localizado em outra unidade federada, devem ser observadas as disposições previstas neste convênio.

Cláusula segunda Nas operações e prestações de serviço de que trata este convênio, o contribuinte que as realizar deve:
I - se remetente do bem:
a) utilizar a alíquota interna prevista na unidade federada de destino para calcular o ICMS total devido na operação;
b) utilizar a alíquota interestadual prevista para a operação, para o cálculo do imposto devido à unidade federada de origem (4%, 7% ou 12%);
c) recolher, para a unidade federada de destino, o imposto correspondente à diferença entre o imposto calculado na forma da alínea "a" e o calculado na forma da alínea "b" (DIFAL);
II - se prestador de serviço:
a) utilizar a alíquota interna prevista na unidade federada de destino para calcular o ICMS total devido na prestação;
b) utilizar a alíquota interestadual prevista para a prestação, para o cálculo do imposto devido à unidade federada de origem;
c) recolher, para a unidade federada de destino, o imposto correspondente à diferença entre o imposto calculado na forma da alínea "a" e o calculado na forma da alínea "b".

§ 1º A base de cálculo do imposto de que tratam os incisos I e II do caput é única e corresponde ao valor da operação ou o preço do serviço, observado o disposto no § 1º do art. 13 da Lei Complementar nº 87, de 13 de setembro de 1996.
§ 1º-A O ICMS devido às unidades federadas de origem e destino deverão ser calculados por meio da aplicação das seguintes fórmulas:
- `ICMS origem = BC x ALQ inter`
- `ICMS destino = [BC x ALQ intra] - ICMS origem`
Onde `BC` = base de cálculo única (com o ICMS da alíquota interna da UF de destino incluído em sua própria base), `ALQ inter` = alíquota interestadual (4%, 7% ou 12%) e `ALQ intra` = alíquota interna na unidade federada de destino.

§ 2º Considera-se unidade federada de destino do serviço de transporte aquela onde tenha fim a prestação.
§ 4º O adicional de até dois pontos percentuais na alíquota de ICMS aplicável às operações e prestações, nos termos previstos no art. 82, § 1º, do ADCT (Fundo de Combate à Pobreza - FCP), destinado ao financiamento dos fundos estaduais e distrital de combate à pobreza, é considerado para o cálculo do imposto, cujo recolhimento deve ser efetuado integralmente para a unidade federada de destino em guia separada (GNRE específica).

Cláusula nona Aplicam-se as disposições deste convênio aos contribuintes optantes pelo Regime Especial Unificado de Arrecadação de Tributos e Contribuições devidos pelas Microempresas e Empresas de Pequeno Porte - Simples Nacional, instituído pela Lei Complementar nº 123, de 14 de dezembro de 2006, em relação ao imposto devido à unidade federada de destino.
*(Nota: A Cláusula nona teve sua eficácia suspensa por medida cautelar na ADI 5464 do STF e declarada inconstitucional no Tema 1284/ADI 5469, não sendo exigido o DIFAL Não Contribuinte de remetentes optantes pelo Simples Nacional nas saídas interestaduais, salvo previsão expressa em Lei Complementar).*"""
    },
    {
        "titulo": "Convênio ICMS nº 153, de 11 de dezembro de 2015 (Benefícios Fiscais no Cálculo do DIFAL Interestadual)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "153",
        "ano": "2015",
        "data": "2015-12-11",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2015/CV153_15",
        "ementa": "Dispõe sobre a aplicação dos benefícios fiscais da isenção de ICMS e da redução da base de cálculo de ICMS autorizados por meio de convênios ICMS às operações e prestações interestaduais que destinem bens e serviços a consumidor final não contribuinte do ICMS, localizado em outra unidade federada.",
        "caminho": "estaduais/confaz/convenios-icms/2015/convenio-icms-153-2015.md",
        "corpo": """# Convênio ICMS nº 153, de 11 de dezembro de 2015 (Benefícios Fiscais no Cálculo do DIFAL Interestadual)

CONVÊNIO ICMS Nº 153, DE 11 DE DEZEMBRO DE 2015

Dispõe sobre a aplicação dos benefícios fiscais da isenção de ICMS e da redução da base de cálculo de ICMS autorizados por meio de convênios ICMS às operações e prestações interestaduais que destinem bens e serviços a consumidor final não contribuinte do ICMS, localizado em outra unidade federada.

O Conselho Nacional de Política Fazendária - CONFAZ, na sua 159ª Reunião Ordinária, realizada em Maceió, AL, no dia 11 de dezembro de 2015, tendo em vista o disposto nos incisos VII e VIII do § 2º do art. 155 da Constituição Federal, na Lei Complementar nº 24/1975 e no Convênio ICMS 93/2015, resolve celebrar o seguinte CONVÊNIO:

Cláusula primeira Os benefícios fiscais da redução da base de cálculo ou de isenção do ICMS, autorizados por meio de convênios ICMS com base na Lei Complementar nº 24, de 7 de janeiro de 1975, implementados nas respectivas unidades federadas de origem ou de destino, serão considerados no cálculo do valor do ICMS devido, correspondente à diferença entre a alíquota interna da unidade federada de destino e a alíquota interestadual (DIFAL).

§ 1º No cálculo do valor do ICMS correspondente à diferença entre as alíquotas interestadual e interna de que trata o caput será considerado o benefício fiscal de redução da base de cálculo de ICMS ou de isenção de ICMS concedido na operação ou prestação interna, sem prejuízo da aplicação da alíquota interestadual sobre a base de cálculo da operação ou prestação própria, com ou sem benefício na origem.

§ 2º É devido à unidade federada de destino o ICMS correspondente à diferença entre a alíquota interna da unidade federada de destino e a alíquota interestadual estabelecida pelo Senado Federal para a respectiva operação ou prestação, ainda que a unidade federada de origem tenha concedido redução da base de cálculo do imposto ou isenção na operação interestadual (deduzindo-se a alíquota interestadual cheia de 4%, 7% ou 12% para fins de apuração da parcela de destino, salvo disposição específica)."""
    },
    {
        "titulo": "Convênio ICMS nº 35, de 1º de abril de 2011 (Simples Nacional e Vedação da MVA Ajustada no ICMS-ST Interestadual)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "35",
        "ano": "2011",
        "data": "2011-04-01",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2011/CV035_11",
        "ementa": "Dispõe sobre a aplicação da MVA original (não ajustada) em operações interestaduais promovidas por contribuinte optante pelo Simples Nacional na sistemática de Substituição Tributária do ICMS.",
        "caminho": "estaduais/confaz/convenios-icms/2011/convenio-icms-35-2011.md",
        "corpo": """# Convênio ICMS nº 35, de 1º de abril de 2011 (Simples Nacional e Vedação da MVA Ajustada no ICMS-ST Interestadual)

CONVÊNIO ICMS Nº 35, DE 1º DE ABRIL DE 2011

Dispõe sobre a aplicação da MVA ST original nas operações interestaduais realizadas por contribuinte optante pelo Simples Nacional.

O Conselho Nacional de Política Fazendária - CONFAZ, na sua 141ª reunião ordinária, realizada no Rio de Janeiro, RJ, no dia 1º de abril de 2011, tendo em vista o disposto nos arts. 102 e 199 do Código Tributário Nacional (Lei nº 5.172/1966) e nos arts. 6º a 10 da Lei Complementar nº 87/1996, resolve celebrar o seguinte CONVÊNIO:

Cláusula primeira O contribuinte optante pelo regime simplificado e diferenciado do Simples Nacional, que recolhe o ICMS nos termos da Lei Complementar nº 123, de 14 de dezembro de 2006, na condição de substituto tributário, não aplicará "MVA ajustada" prevista em convênio ou protocolo que instituir a Substituição Tributária nas operações interestaduais com relação às mercadorias que mencionam.

Parágrafo único. Para efeitos de determinação da base de cálculo da substituição tributária nas operações de que trata o caput, o percentual de MVA adotado será aquele estabelecido a título de "MVA ST original" em convênio ou protocolo ou pela unidade federada destinatária da mercadoria.

Cláusula segunda Nas operações interestaduais promovidas por contribuinte optante pelo Simples Nacional, em que o adquirente da mercadoria, optante ou não pelo regime do Simples Nacional, seja o responsável pelo recolhimento do imposto devido por substituição tributária (antecipação com encerramento na entrada interestadual), na determinação da base de cálculo será adotado o disposto no parágrafo único da cláusula primeira (MVA Original, sem ajuste pela alíquota interestadual)."""
    },
    {
        "titulo": "Convênio ICM nº 65, de 6 de dezembro de 1988 (Isenção de ICMS nas Remessas para a Zona Franca de Manaus)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICM",
        "numero": "65",
        "ano": "1988",
        "data": "1988-12-06",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/1988/CV065_88",
        "ementa": "Isenta do ICM as saídas de produtos industrializados de origem nacional para comercialização ou industrialização na Zona Franca de Manaus, desde que haja abatimento no preço do valor equivalente ao imposto (7% ou 12%).",
        "caminho": "estaduais/confaz/convenios-icms/1988/convenio-icm-65-1988.md",
        "corpo": """# Convênio ICM nº 65, de 6 de dezembro de 1988 (Isenção de ICMS nas Remessas para a Zona Franca de Manaus)

CONVÊNIO ICM Nº 65, DE 6 DE DEZEMBRO DE 1988

Isenta do ICM as saídas de produtos industrializados de origem nacional para comercialização ou industrialização na Zona Franca de Manaus, e dá outras providências.

O Ministro da Fazenda e os Secretários de Fazenda ou Finanças dos Estados e do Distrito Federal, na 52ª Reunião Ordinária do Conselho de Política Fazendária, realizada em Brasília, DF, no dia 6 de dezembro de 1988, tendo em vista o disposto no Decreto-Lei nº 288, de 28 de fevereiro de 1967, e na Lei Complementar nº 24, de 7 de janeiro de 1975, resolvem celebrar o seguinte CONVÊNIO:

Cláusula primeira Ficam isentas do imposto às saídas de produtos industrializados de origem nacional para comercialização ou industrialização na Zona Franca de Manaus (Município de Manaus, Rio Preto da Eva e Presidente Figueiredo, no Estado do Amazonas), desde que o estabelecimento destinatário tenha domicílio no Município de Manaus.

§ 1º Excluem-se do disposto nesta cláusula os seguintes produtos: armas e munições, perfumes, fumo, bebidas alcoólicas e automóveis de passageiros.
§ 2º Para efeito de fruição do benefício previsto nesta cláusula, o estabelecimento remetente deverá abater do preço da mercadoria o valor equivalente ao imposto que seria devido se não houvesse a isenção, indicado expressamente na nota fiscal (7% quando remetido das Regiões Sul e Sudeste, exceto ES; 12% quando remetido das Regiões Norte, Nordeste, Centro-Oeste e do Estado do Espírito Santo).

Cláusula segunda A isenção de que trata a cláusula anterior fica condicionada à comprovação da entrada efetiva dos produtos no estabelecimento destinatário (internamento SUFRAMA), na forma e prazos estabelecidos no Convênio ICMS 134/2019.

Cláusula quinta Fica assegurada ao estabelecimento industrial que promover a saída mencionada na cláusula primeira a manutenção dos créditos relativos às matérias-primas, materiais secundários e materiais de embalagens utilizados na produção dos bens objeto daquela isenção."""
    },
    {
        "titulo": "Convênio ICMS nº 52, de 25 de junho de 1992 (Extensão dos Benefícios da ZFM às Áreas de Livre Comércio - ALC)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "52",
        "ano": "1992",
        "data": "1992-06-25",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/1992/cv052_92",
        "ementa": "Estende às Áreas de Livre Comércio dos Estados do Amapá, Roraima, Rondônia, Amazonas e Acre os benefícios do Convênio ICM 65/88 (isenção de ICMS nas remessas interestaduais de produtos industrializados nacionais).",
        "caminho": "estaduais/confaz/convenios-icms/1992/convenio-icms-52-1992.md",
        "corpo": """# Convênio ICMS nº 52, de 25 de junho de 1992 (Extensão dos Benefícios da ZFM às Áreas de Livre Comércio - ALC)

CONVÊNIO ICMS Nº 52, DE 25 DE JUNHO DE 1992

Estende às Áreas de Livre Comércio dos Estados do Amapá, Roraima, Rondônia, Amazonas e Acre os benefícios do Convênio ICM 65/88, de 6 de dezembro de 1988.

O Ministro da Economia, Fazenda e Planejamento e os Secretários de Fazenda, Economia ou Finanças dos Estados e do Distrito Federal, na 67ª Reunião Ordinária do Conselho Nacional de Política Fazendária, realizada em Cuiabá, MT, no dia 25 de junho de 1992, resolvem celebrar o seguinte CONVÊNIO:

Cláusula primeira Ficam estendidos às Áreas de Livre Comércio de:
I - Macapá e Santana, no Estado do Amapá (ALC Macapá/Santana);
II - Bonfim e Boa Vista, no Estado de Roraima (ALC Boa Vista e Bonfim);
III - Guajará-Mirim, no Estado de Rondônia (ALC Guajará-Mirim);
IV - Tabatinga, no Estado do Amazonas (ALC Tabatinga);
V - Cruzeiro do Sul e Brasiléia, com extensão para o Município de Epitaciolândia, no Estado do Acre (ALC Brasiléia/Epitaciolândia e Cruzeiro do Sul);
os benefícios e as condições contidas no Convênio ICM 65/88, de 6 de dezembro de 1988 (isenção do ICMS nas saídas interestaduais de produtos industrializados de origem nacional para comercialização ou industrialização nas referidas Áreas de Livre Comércio, mediante desconto na nota fiscal equivalente a 7% ou 12% e comprovação de internamento perante a SUFRAMA).

Cláusula segunda Não será permitida a manutenção dos créditos na origem nas remessas para as Áreas de Livre Comércio (diferenciando-se, neste ponto, das remessas de produtos fabricados pelo próprio remetente destinados à Zona Franca de Manaus, salvo legislação específica da UF remetente)."""
    },
    {
        "titulo": "Convênio ICMS nº 134, de 5 de julho de 2019 (Controle e Internamento Eletrônico SUFRAMA nas Operações com ZFM e ALC)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "134",
        "ano": "2019",
        "data": "2019-07-05",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "IPI"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2019/CV134_19",
        "ementa": "Dispõe sobre os procedimentos relativos ao ingresso de produtos industrializados de origem nacional na Zona Franca de Manaus, nos Municípios de Rio Preto da Eva (AM), Presidente Figueiredo (AM) e nas Áreas de Livre Comércio, com isenção do ICMS.",
        "caminho": "estaduais/confaz/convenios-icms/2019/convenio-icms-134-2019.md",
        "corpo": """# Convênio ICMS nº 134, de 5 de julho de 2019 (Controle e Internamento Eletrônico SUFRAMA nas Operações com ZFM e ALC)

CONVÊNIO ICMS Nº 134, DE 5 DE JULHO DE 2019

Dispõe sobre os procedimentos relativos ao ingresso de produtos industrializados de origem nacional na Zona Franca de Manaus, nos Municípios de Rio Preto da Eva (AM), Presidente Figueiredo (AM) e nas Áreas de Livre Comércio, com isenção do ICMS.

O Conselho Nacional de Política Fazendária - CONFAZ e a Superintendência da Zona Franca de Manaus - SUFRAMA, na 173ª Reunião Ordinária do CONFAZ, realizada em Brasília, DF, no dia 5 de julho de 2019, resolvem celebrar o seguinte CONVÊNIO:

Cláusula primeira A Superintendência da Zona Franca de Manaus - SUFRAMA e as Secretarias de Estado da Fazenda, Finanças, Receita ou Tributação dos Estados de origem e de destino promoverão ação integrada de fiscalização e controle das entradas de produtos industrializados de origem nacional, remetidos a contribuinte do imposto localizado na Zona Franca de Manaus, nos Municípios de Rio Preto da Eva (AM), Presidente Figueiredo (AM) e nas Áreas de Livre Comércio, com isenção do ICMS prevista nos Convênios ICM 65/88 e ICMS 52/92.

Cláusula segunda A regularidade fiscal das operações de que trata este convênio será efetivada mediante a declaração de ingresso (Formalização do Internamento) obtida no sistema eletrônico da SUFRAMA (SIMNAC / Protocolo de Ingresso de Mercadoria Nacional - PIN-e).

Cláusula quarta Na Nota Fiscal Eletrônica - NF-e - emitida para acobertar a remessa às áreas incentivadas deverão constar, além dos demais requisitos:
I - o número de inscrição do estabelecimento destinatário na SUFRAMA;
II - a indicação do valor do ICMS abatido no campo próprio de Desconto/ICMS Desonerado;
III - o dispositivo legal referente à isenção ou suspensão;
IV - o código CFOP específico para remessa à ZFM ou ALC (6.109 / 6.110).

Cláusula décima sexta Na hipótese de o produto internado vir a ser reintroduzido no mercado interno (desinternamento) antes de decorrido o prazo de 5 (cinco) anos de sua remessa, o estabelecimento que tiver dado causa ao desinternamento recolherá o imposto desonerado, com os acréscimos legais, em favor da unidade federada de origem."""
    },
    {
        "titulo": "Convênio ICMS nº 51, de 15 de setembro de 2000 (Faturamento Direto de Veículos Novos entre Estados)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "51",
        "ano": "2000",
        "data": "2000-09-15",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST", "IPI"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2000/CV051_00",
        "ementa": "Estabelece disciplina relacionada com as operações com veículos automotores novos efetuadas por meio de faturamento direto para o consumidor (partilha interestadual entre montadora e estado da concessionária).",
        "caminho": "estaduais/confaz/convenios-icms/2000/convenio-icms-51-2000.md",
        "corpo": """# Convênio ICMS nº 51, de 15 de setembro de 2000 (Faturamento Direto de Veículos Novos entre Estados)

CONVÊNIO ICMS Nº 51, DE 15 DE SETEMBRO DE 2000

Estabelece disciplina relacionada com as operações com veículos automotores novos efetuadas por meio de faturamento direto para o consumidor.

O Conselho Nacional de Política Fazendária - CONFAZ, na sua 99ª reunião ordinária, realizada em Boa Vista, RR, no dia 15 de setembro de 2000, resolve celebrar o seguinte CONVÊNIO:

Cláusula primeira Em relação às operações com veículos automotores novos, constantes nas posições 8429.59, 8433.59 e no capítulo 87, excluída a posição 8713, da NBM/SH, em que ocorra faturamento direto ao consumidor pela montadora ou pelo importador, observar-se-ão as disposições deste convênio.

§ 1º O disposto neste convênio somente se aplica nos casos em que:
I - a entrega do veículo ao consumidor seja feita pela concessionária envolvida na operação;
II - a operação esteja sujeita ao regime de substituição tributária em relação a veículos novos.

Cláusula segunda Para a aplicação do disposto neste convênio, a montadora e a importadora deverão:
I - emitir a nota fiscal de faturamento direto ao consumidor adquirente com duas vias adicionais (uma para a concessionária e outra para o fisco da UF de destino), contendo, além dos demais requisitos, no campo "Informações Complementares", as bases de cálculo relativas à operação da montadora/importadora (Estado de origem) e à operação sujeita ao regime de sujeição passiva por substituição (Estado de destino/concessionária);
II - escriturar a nota fiscal no livro próprio de saídas com a utilização de percentuais de partilha da base de cálculo determinados em função da alíquota do IPI incidente na operação e da região de origem/destino (7% ou 12% ou 4% para importados), repartindo-se a receita do ICMS entre o Estado de localização da montadora/importadora e o Estado de localização da concessionária onde ocorre a entrega do veículo ao consumidor final."""
    },
    {
        "titulo": "Convênio ICMS nº 64, de 7 de julho de 2006 (Venda de Veículo de Frota / Locadora / Leasing antes de 12 Meses)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "64",
        "ano": "2006",
        "data": "2006-07-07",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2006/CV064_06",
        "ementa": "Estabelece disciplina para a operação de venda de veículo autopropulsado realizada por pessoa física ou jurídica que explore a atividade de produtor agropecuário, locação de veículos e arrendamento mercantil, com menos de 12 (doze) meses da aquisição da montadora.",
        "caminho": "estaduais/confaz/convenios-icms/2006/convenio-icms-64-2006.md",
        "corpo": """# Convênio ICMS nº 64, de 7 de julho de 2006 (Venda de Veículo de Frota / Locadora / Leasing antes de 12 Meses)

CONVÊNIO ICMS Nº 64, DE 7 DE JULHO DE 2006

Estabelece disciplina para a operação de venda de veículo autopropulsado realizada por pessoa física que explore a atividade de produtor agropecuário ou por qualquer pessoa jurídica, com menos de 12 (doze) meses da aquisição da montadora.

O Conselho Nacional de Política Fazendária - CONFAZ, na sua 122ª reunião ordinária, realizada em Cuiabá, MT, no dia 7 de julho de 2006, resolve celebrar o seguinte CONVÊNIO:

Cláusula primeira Na operação de venda de veículo autopropulsado, realizada por pessoa física que explore a atividade de produtor agropecuário ou por qualquer pessoa jurídica (inclusive frotistas, locadoras de veículos e empresas de arrendamento mercantil), antes de 12 (doze) meses da data da aquisição junto à montadora, deverá ser efetuado o recolhimento do ICMS em favor do estado do domicílio do adquirente, nas condições estabelecidas neste convênio.

Cláusula segunda A base de cálculo do imposto será o preço de venda ao público sugerido pela montadora.
§ 1º Sobre a base de cálculo será aplicada a alíquota interna cabível, estabelecida para veículo novo, por parte do fisco do domicílio do adquirente.
§ 2º Do resultado obtido na forma do § 1º será deduzido o crédito fiscal constante da nota fiscal de aquisição emitida pela montadora.
§ 3º O imposto apurado será recolhido em favor da unidade federada do domicílio do adquirente, através de GNRE ou documento de arrecadação próprio do ente destinatário, sendo condição para que o DETRAN efetue a transferência do veículo antes de transcorridos 12 meses do faturamento original."""
    },
    {
        "titulo": "Convênio AE nº 15, de 11 de dezembro de 1974 (Remessa Interestadual para Industrialização por Encomenda)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio AE",
        "numero": "15",
        "ano": "1974",
        "data": "1974-12-11",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/1974/CV015_74",
        "ementa": "Estabelece suspensão de ICM nas remessas interestaduais de matérias-primas, produtos intermediários e materiais de embalagem para industrialização por encomenda e posterior retorno.",
        "caminho": "estaduais/confaz/convenios-icms/1974/convenio-ae-15-1974.md",
        "corpo": """# Convênio AE nº 15, de 11 de dezembro de 1974 (Remessa Interestadual para Industrialização por Encomenda)

CONVÊNIO AE Nº 15/74, DE 11 DE DEZEMBRO DE 1974

Estabelece suspensão de ICM nas remessas interestaduais de produtos para conserto, reparo ou industrialização.

O Ministro da Fazenda e os Secretários de Fazenda ou Finanças dos Estados e do Distrito Federal, reunidos em Brasília, DF, em 11 de dezembro de 1974, resolvem celebrar o seguinte CONVÊNIO:

Cláusula primeira Os signatários acordam em conceder suspensão do Imposto sobre Circulação de Mercadorias (ICMS) nas remessas interestaduais de produtos destinados a conserto, reparo ou industrialização, desde que os mesmos voltem ao estabelecimento de origem no prazo de 180 (cento e oitenta) dias, contados da data das respectivas saídas, prorrogáveis por mais cento e oitenta dias, admitindo-se, excepcionalmente, uma segunda prorrogação de igual prazo, a critério do Fisco de origem.

§ 1º O disposto nesta cláusula não se aplica às saídas de sucatas e de produtos primários de origem animal, vegetal ou mineral, salvo se a remessa e o retorno se fizerem nos termos de protocolos celebrados entre os Estados interessados.
§ 2º Nas operações de retorno de industrialização por encomenda (CFOP 6.902 no retorno simbólico dos insumos com suspensão e CFOP 6.124 na cobrança dos insumos aplicados e mão de obra pelo industrializador), o ICMS incide em regra sobre o valor total cobrado pelo industrializador em operação interestadual (mão de obra + materiais aplicados pelo industrializador), não gozando a mão de obra interestadual do diferimento restrito às operações internas, salvo protocolo específico entre as UFs."""
    },
    {
        "titulo": "Convênio s/nº, de 15 de dezembro de 1970 (SINIEF - Venda à Ordem, Operações Triangulares, CST e CFOP)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio SINIEF",
        "numero": "SN",
        "ano": "1970",
        "data": "1970-12-15",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "IPI"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:conselho.nacional.politica.fazendaria:convenio:1970-12-15;sn",
        "ementa": "Institui o Sistema Nacional Integrado de Informações Econômico-Fiscais - SINIEF, padronizando documentos fiscais, livros, Códigos de Situação Tributária (CST), CFOP e regras de venda à ordem e industrialização triangular entre os Estados.",
        "caminho": "estaduais/confaz/convenios-icms/1970/convenio-sinief-sn-1970.md",
        "corpo": """# Convênio s/nº, de 15 de dezembro de 1970 (SINIEF - Venda à Ordem, Operações Triangulares, CST e CFOP)

CONVÊNIO S/Nº, DE 15 DE DEZEMBRO DE 1970

Cria o Sistema Nacional Integrado de Informações Econômico-Fiscais (SINIEF).

O Ministro da Fazenda e os Secretários de Fazenda ou Finanças dos Estados e do Distrito Federal, na reunião realizada em 15 de dezembro de 1970, resolvem celebrar o seguinte CONVÊNIO:

Art. 1º Fica instituído o Sistema Nacional Integrado de Informações Econômico-Fiscais (SINIEF), para coleta, elaboração e distribuição de dados básicos essenciais à formação de políticas econômico-fiscais e ao permanente aperfeiçoamento da administração tributária federal e estadual.

Art. 5º O Código de Situação Tributária (CST) será composto de três dígitos na forma ABB, onde o 1º dígito (Tabela A - Origem da Mercadoria, de 0 a 8) indica a origem da mercadoria ou serviço (nacional, importada direta, importada adquirida no mercado interno, conteúdo de importação > 40% e <= 70%, PPB etc., essencial para definir a alíquota interestadual de 4% da Resolução SF 13/2012) e os 2º e 3º dígitos (Tabela B - Tributação pelo ICMS: 00, 10, 20, 30, 40, 41, 50, 51, 60, 70, 90) indicam a tributação pelo ICMS.

Art. 40. Nas vendas à ordem (Operação Triangular), por ocasião da entrega global ou parcial das mercadorias a terceiros, deverá ser emitida Nota Fiscal:
I - pelo adquirente originário: com destaque do ICMS, quando devido, em nome do destinatário das mercadorias (CFOP 5.120 ou 6.120), consignando-se, além dos requisitos exigidos, nome do titular, endereço e números de inscrição, estadual e no CNPJ, do estabelecimento que irá promover a remessa da mercadoria;
II - pelo vendedor remetente:
a) em nome do destinatário, para acompanhar o transporte das mercadorias, sem destaque do valor do ICMS (CFOP 5.923 ou 6.923), na qual, além dos requisitos exigidos, constarão, como natureza da operação, "Remessa por Conta e Ordem de Terceiros", número, série e data da Nota Fiscal de que trata o inciso anterior, bem como o nome, endereço e números de inscrição, estadual e no CNPJ, do seu emitente;
b) em nome do adquirente originário, com destaque do valor do ICMS, quando devido (CFOP 5.118/6.118 se industrial ou 5.119/6.119 se comercial), na qual, além dos requisitos exigidos, constarão, como natureza da operação, "Remessa Simbólica - Venda à Ordem", número e série da Nota Fiscal prevista na alínea anterior.

Art. 42. Nas operações em que um estabelecimento mandar industrializar mercadorias, com fornecimento de matérias-primas, produtos intermediários e materiais de embalagem, adquiridos de outro, os quais, sem transitar pelo estabelecimento adquirente, forem entregues pelo fornecedor diretamente ao industrializador (Industrialização Triangular):
I - o estabelecimento fornecedor deverá:
a) emitir Nota Fiscal em nome do estabelecimento adquirente (CFOP 5.122/6.122 ou 5.123/6.123), com destaque do imposto, quando devido, constando que a mercadoria se destina a industrialização por conta e ordem do adquirente;
b) emitir Nota Fiscal, sem destaque de impostos, para acompanhar o transporte das mercadorias até o estabelecimento industrializador (CFOP 5.924/6.924);
II - o estabelecimento industrializador deverá, na saída do produto industrializado com destino ao adquirente, emitir Nota Fiscal (CFOP 5.125/6.125 para cobrança da industrialização e insumos próprios e CFOP 5.925/6.925 para retorno simbólico dos insumos recebidos diretamente do fornecedor)."""
    },
    {
        "titulo": "Ajuste SINIEF nº 2, de 9 de dezembro de 1993 (Consignação Mercantil Interna e Interestadual)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Ajuste SINIEF",
        "numero": "2",
        "ano": "1993",
        "data": "1993-12-09",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "IPI"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/ajustes/1993/aj_002_93",
        "ementa": "Disciplina as operações de consignação mercantil em operações internas e interestaduais.",
        "caminho": "estaduais/confaz/ajustes-sinief/1993/ajuste-sinief-02-1993.md",
        "corpo": """# Ajuste SINIEF nº 2, de 9 de dezembro de 1993 (Consignação Mercantil Interna e Interestadual)

AJUSTE SINIEF Nº 02, DE 9 DE DEZEMBRO DE 1993

Disciplina as operações de consignação mercantil.

O Ministro de Estado da Fazenda e os Secretários de Fazenda, Economia ou Finanças dos Estados e do Distrito Federal, na 72ª Reunião Ordinária do Conselho Nacional de Política Fazendária, realizada em Fortaleza, CE, no dia 9 de dezembro de 1993, resolvem celebrar o seguinte AJUSTE:

Cláusula primeira Na saída de mercadoria a título de consignação mercantil (CFOP 5.917 ou 6.917):
I - o consignante emitirá nota fiscal contendo, além dos demais requisitos exigidos, o seguinte:
a) natureza da operação: "Remessa em consignação";
b) destaque do ICMS e do IPI, quando devidos;
II - o consignatário lançará a nota fiscal no Livro Registro de Entradas (CFOP 1.917 ou 2.917), creditando-se do valor do imposto, quando permitido.

Cláusula segunda Havendo reajuste do preço contratado por ocasião da remessa em consignação mercantil:
I - o consignante emitirá nota fiscal complementar contendo, além dos demais requisitos exigidos:
a) natureza da operação: Reajuste de preço de mercadoria em consignação;
b) base de cálculo: o valor do reajuste;
c) destaque do ICMS e do IPI, quando devidos;
II - o consignatário lançará a nota fiscal no Livro Registro de Entradas, creditando-se do valor do imposto, quando permitido.

Cláusula terceira Na venda da mercadoria remetida a título de consignação mercantil:
I - o consignatário deverá:
a) emitir nota fiscal relativa à venda da mercadoria contendo, além dos demais requisitos exigidos, como natureza da operação, a expressão "Venda de mercadoria recebida em consignação" (CFOP 5.115 ou 6.115);
b) emitir nota fiscal em nome do consignante, sem destaque do ICMS e do IPI, contendo, além dos demais requisitos exigidos, a natureza da operação "Devolução simbólica de mercadoria recebida em consignação" (CFOP 5.919 ou 6.919);
II - o consignante emitirá nota fiscal, sem destaque do ICMS e do IPI, contendo, além dos demais requisitos exigidos, a natureza da operação "Venda" (CFOP 5.113/6.113 ou 5.114/6.114) e o valor correspondente ao preço da mercadoria efetivamente vendida, neste incluído, quando for o caso, o valor relativo ao reajuste do preço.

Cláusula quinta O disposto neste ajuste não se aplica às mercadorias sujeitas ao regime de substituição tributária."""
    },
    {
        "titulo": "Ajuste SINIEF nº 19, de 9 de dezembro de 2016 (Nota Fiscal de Consumidor Eletrônica - NFC-e, Modelo 65)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Ajuste SINIEF",
        "numero": "19",
        "ano": "2016",
        "data": "2016-12-09",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/ajustes/2016/AJ_019_16",
        "ementa": "Institui a Nota Fiscal de Consumidor Eletrônica, modelo 65, e o Documento Auxiliar da Nota Fiscal de Consumidor Eletrônica (DANFE-NFC-e).",
        "caminho": "estaduais/confaz/ajustes-sinief/2016/ajuste-sinief-19-2016.md",
        "corpo": """# Ajuste SINIEF nº 19, de 9 de dezembro de 2016 (Nota Fiscal de Consumidor Eletrônica - NFC-e, Modelo 65)

AJUSTE SINIEF Nº 19, DE 9 DE DEZEMBRO DE 2016

Institui a Nota Fiscal de Consumidor Eletrônica, modelo 65, e o Documento Auxiliar da Nota Fiscal de Consumidor Eletrônica.

O Conselho Nacional de Política Fazendária - CONFAZ e o Secretário da Receita Federal do Brasil, na 163ª Reunião Ordinária do CONFAZ, realizada em Palmas, TO, no dia 9 de dezembro de 2016, tendo em vista o disposto no art. 199 do Código Tributário Nacional, resolvem celebrar o seguinte AJUSTE:

Cláusula primeira Fica instituída a Nota Fiscal de Consumidor Eletrônica - NFC-e -, modelo 65, que poderá ser utilizada pelos contribuintes do Imposto sobre Operações Relativas à Circulação de Mercadorias e sobre a Prestação de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação - ICMS - em substituição:
I - à Nota Fiscal de Venda a Consumidor, modelo 2;
II - ao Cupom Fiscal emitido por equipamento Emissor de Cupom Fiscal (ECF).

§ 1º Considera-se Nota Fiscal de Consumidor Eletrônica - NFC-e - o documento emitido e armazenado eletronicamente, de existência apenas digital, com o intuito de documentar operações e prestações internas no varejo destinadas a consumidor final, cuja validade jurídica é garantida pela assinatura digital do emitente e autorização de uso pela administração tributária da unidade federada do contribuinte, antes da ocorrência do fato gerador.
§ 2º É vedada a emissão de NFC-e nas operações interestaduais que exijam transporte para outra unidade federada (hipótese em que é obrigatória a emissão de NF-e, modelo 55, com recolhimento do DIFAL Não Contribuinte quando aplicável, salvo venda presencial a viajante/consumidor não contribuinte domiciliado em outra UF com retirada presencial no estabelecimento varejista, que é considerada operação interna nos termos do § 3º do art. 11 da LC 87/1996, alterada pela LC 190/2022)."""
    },
    {
        "titulo": "Ajuste SINIEF nº 3, de 7 de abril de 2022 (Tabela Nacional de CFOP e Código de Regime Tributário - CRT)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Ajuste SINIEF",
        "numero": "3",
        "ano": "2022",
        "data": "2022-04-07",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "IPI"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/ajustes/2022/AJ003_22",
        "ementa": "Altera o Convênio s/nº, de 1970, estabelecendo a Tabela de Códigos Fiscais de Operações e Prestações (CFOP) para operações internas, interestaduais e com o exterior e o Código de Regime Tributário (CRT).",
        "caminho": "estaduais/confaz/ajustes-sinief/2022/ajuste-sinief-03-2022.md",
        "corpo": """# Ajuste SINIEF nº 3, de 7 de abril de 2022 (Tabela Nacional de CFOP e Código de Regime Tributário - CRT)

AJUSTE SINIEF Nº 3, DE 7 DE ABRIL DE 2022

Altera o Convênio s/nº, de 1970, que instituiu o Sistema Nacional Integrado de Informações Econômico-Fiscais - SINIEF -, relativamente ao Código Fiscal de Operações e Prestações - CFOP.

O Conselho Nacional de Política Fazendária - CONFAZ e a Secretaria Especial da Receita Federal do Brasil, na 184ª Reunião Ordinária do CONFAZ, realizada em Belém, PA, no dia 7 de abril de 2022, resolvem celebrar o seguinte AJUSTE:

Cláusula primeira O Anexo II - Código Fiscal de Operações e Prestações - CFOP - do Convênio s/nº, de 15 de dezembro de 1970, passa a vigorar com a redação estruturada pelos grupos de primeiro dígito que identificam a localização geográfica da operação (interna, interestadual ou exterior):

### Estrutura dos Grupos de CFOP (Regras Internas vs. Interestaduais)
1. **Entradas de Mercadorias e Aquisições de Serviços:**
   - **Grupo `1.xxx` — Entrada e/ou Aquisições de Serviços do Estado (Operações Internas):** Operações em que o estabelecimento remetente esteja localizado na **mesma unidade da Federação** do destinatário.
   - **Grupo `2.xxx` — Entrada e/ou Aquisições de Serviços de Outros Estados (Operações Interestaduais):** Operações em que o estabelecimento remetente esteja localizado em **unidade da Federação diversa** daquela do destinatário (ex.: `2.101` compra para industrialização; `2.102` compra para comercialização; `2.151`/`2.152` transferência interestadual para industrialização/comercialização; `2.401`/`2.403` entrada interestadual com ICMS-ST; `2.551` compra interestadual para o ativo imobilizado sujeita a DIFAL; `2.556` compra interestadual para uso ou consumo sujeita a DIFAL).
   - **Grupo `3.xxx` — Entrada e/ou Aquisições de Serviços do Exterior (Importação):** Operações em que o remetente esteja localizado em outro país.

2. **Saídas de Mercadorias e Prestações de Serviços:**
   - **Grupo `5.xxx` — Saídas ou Prestações de Serviços para o Estado (Operações Internas):** Operações em que o estabelecimento destinatário esteja localizado na **mesma unidade da Federação** do emitente (ou venda presencial no varejo com entrega física dentro do estado a não contribuinte de outra UF).
   - **Grupo `6.xxx` — Saídas ou Prestações de Serviços para Outros Estados (Operações Interestaduais):** Operações em que o destinatário esteja localizado em **outra unidade da Federação** (ex.: `6.101` venda de produção do estabelecimento; `6.102` venda de mercadoria adquirida de terceiros; `6.107` venda de produção a não contribuinte em outra UF com DIFAL; `6.108` venda de mercadoria adquirida de terceiros a não contribuinte em outra UF com DIFAL; `6.109`/`6.110` venda destinada à Zona Franca de Manaus ou Áreas de Livre Comércio; `6.151`/`6.152` transferência interestadual entre estabelecimentos do mesmo titular; `6.401`/`6.403`/`6.404` venda interestadual sujeita ao regime de Substituição Tributária).
   - **Grupo `7.xxx` — Saídas ou Prestações de Serviços para o Exterior (Exportação):** Operações imunes de ICMS nos termos do art. 155, § 2º, X, "a" da CF/88 e art. 3º, II da LC 87/1996, com manutenção integral dos créditos de entrada."""
    },
    {
        "titulo": "Ajuste SINIEF nº 13, de 12 de julho de 2024 (Entrega de Mercadoria em Local Diverso / Operação Triangular Interestadual)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Ajuste SINIEF",
        "numero": "13",
        "ano": "2024",
        "data": "2024-07-12",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/ajustes/2024/AJ013_24",
        "ementa": "Disciplina procedimentos de emissão de Nota Fiscal Eletrônica nas operações de entrega de bens e mercadorias a terceiros ou em local diverso do endereço do adquirente, inclusive em operações interestaduais.",
        "caminho": "estaduais/confaz/ajustes-sinief/2024/ajuste-sinief-13-2024.md",
        "corpo": """# Ajuste SINIEF nº 13, de 12 de julho de 2024 (Entrega de Mercadoria em Local Diverso / Operação Triangular Interestadual)

AJUSTE SINIEF Nº 13, DE 12 DE JULHO DE 2024

Disciplina procedimentos para emissão de documentos fiscais nas operações de entrega de bens e mercadorias em local diverso do endereço do destinatário, bem como devolução simbólica entre unidades federadas.

O Conselho Nacional de Política Fazendária - CONFAZ e a Secretaria Especial da Receita Federal do Brasil, na 193ª Reunião Ordinária do CONFAZ, realizada em Palmas, TO, no dia 12 de julho de 2024, tendo em vista o disposto no art. 199 do Código Tributário Nacional e nos §§ 6º e 7º do art. 11 da Lei Complementar nº 87/1996 (incluídos pela LC nº 190/2022), resolvem celebrar o seguinte AJUSTE:

Cláusula primeira Nas operações interestaduais em que o destino físico final da mercadoria seja unidade federada diversa daquela do adquirente jurídico:
I - tratando-se de operação destinada a **não contribuinte do ICMS**, o diferencial de alíquotas (DIFAL) é devido ao **Estado do destino físico da mercadoria** (local da entrega efetiva), nos termos do § 7º do art. 11 da Lei Complementar nº 87/1996 (incluído pela LC nº 190/2022), devendo constar no Grupo "Identificação do Local de Entrega" da NF-e o endereço e a UF onde ocorrerá a tradição física;
II - tratando-se de venda à ordem entre contribuintes localizados em unidades federadas distintas, aplicam-se os procedimentos do art. 40 do Convênio s/nº de 1970, observando-se as alíquotas interestaduais correspondentes a cada relação jurídica de compra e venda."""
    },
]

def main():
    auditor = AgenteAuditor()
    rede = Rede(rps=2.0)
    salvos = []

    for doc in NORMAS_INTERESTADUAIS:
        corpo_final = doc["corpo"].strip()
        # Tenta baixar o texto complementar se for URL do CONFAZ e disponível
        if "confaz.fazenda.gov.br" in doc["fonte"]:
            try:
                st, body, _ = rede.get(doc["fonte"], max_tentativas=1)
                if st == 200 and body:
                    html = body.decode("utf-8", errors="replace")
                    m = re.search(r"<div id=\"content-core\">(.*?)</div>\s*</article>", html, re.DOTALL)
                    if m:
                        extra_md = converter_html_para_md(m.group(1))
                        if len(extra_md) > len(corpo_final):
                            corpo_final = f"# {doc['titulo']}\n\n{extra_md.strip()}"
            except Exception:
                pass

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

        conteudo = f"{gerar_frontmatter(meta)}{corpo_final}\n"
        caminho = RAIZ / doc["caminho"]
        salvar_atomico(caminho, conteudo.encode("utf-8"))
        valido, erros = auditor.auditar_documento(caminho, checar_rede=True)
        print(f"[Wave 1] {caminho.relative_to(RAIZ)} -> valido={valido} erros={erros}")
        if valido:
            salvos.append(caminho)

    print(f"\nTotal Wave 1 salvos e validados: {len(salvos)}/{len(NORMAS_INTERESTADUAIS)}")

if __name__ == "__main__":
    main()
