# Relatório de Auditoria Tributária Estadual: Amazonas (AM)
**Unidade Federativa:** Amazonas | **Sigla:** AM | **Região:** Norte  
**Órgão Fazendário:** Secretaria de Estado da Fazenda do Amazonas (SEFAZ/AM)  
**Data da Auditoria:** Outubro de 2026 | **Status:** Atualizado com a EC nº 132/2023 e LC nº 214/2025  

---

## 1. Mapeamento das Normas no Repositório e Diagnóstico de Lacunas

### 1.1. Acervo Documental Existente no Repositório (`estaduais/am/`)

O repositório apresenta os seguintes arquivos cadastrados no âmbito do Estado do Amazonas:

1. [`estaduais/am/ricms/decreto-20686-1999.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/am/ricms/decreto-20686-1999.md): Síntese estrutural do Regulamento do ICMS do Estado do Amazonas (RICMS/AM), aprovado pelo Decreto nº 20.686, de 28 de dezembro de 1999.
2. [`estaduais/am/ricms/lei-2826-2003-incentivos-zfm-pim-am.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/am/ricms/lei-2826-2003-incentivos-zfm-pim-am.md): Estrutura fundamental da Lei Estadual nº 2.826, de 29 de setembro de 2003, disciplinadora da Política Estadual de Incentivos Fiscais e Extrafiscais vinculada ao Polo Industrial de Manaus (PIM).
3. [`estaduais/am/leis/itcmd/lei-19-1997.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/am/leis/itcmd/lei-19-1997.md): Disposições relativas ao Imposto sobre Transmissão Causa Mortis e Doação (ITCMD), integradas ao Código Tributário do Estado (Lei Complementar nº 19/1997).
4. [`estaduais/am/leis/ipva/lei-19-1997.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/am/leis/ipva/lei-19-1997.md): Disposições normativas do Imposto sobre a Propriedade de Veículos Automotores (IPVA), igualmente alocadas na LC nº 19/1997.

### 1.2. Inventário de Normas Fundamentais Ausentes (Lacunas Críticas)

Para atingir conformidade técnica plena, o repositório demanda a incorporação urgente dos seguintes diplomas legais e infralegais:

| Diploma Legal Faltante | Ementa / Objeto Jurídico | Prioridade | Impacto Técnico no Repositório |
| :--- | :--- | :---: | :--- |
| **Lei Complementar Estadual nº 19/1997 (Texto Integral)** | Código Tributário do Estado do Amazonas (CTE/AM) — Matriz do ICMS, taxas, infrações, penalidades e obrigação tributária. | **Crítica** | Base de legalidade estrita de todas as exações estaduais. |
| **Lei Estadual nº 4.730/2018** | Reestruturação do contencioso administrativo e alterações nas alíquotas e taxas de expediente da SEFAZ/AM. | **Alta** | Rito recursal administrativo e fiscalização. |
| **Lei Complementar Estadual nº 242/2022** | Elevação da alíquota modal interna de ICMS de 18% para 20% (em vigor a partir de março de 2023). | **Crítica** | Parâmetro imperativo de cálculo do DIFAL e operações internas. |
| **Decreto Estadual nº 23.994/2003** | Regulamento da Lei nº 2.826/2003 — Procedimentos para obtenção de Crédito Estímulo e laudos CODAM/SEFAZ. | **Crítica** | Operacionalização dos percentuais de crédito estímulo (55% a 100%). |
| **Leis nº 3.830/2012 e 4.164/2015 (FTI, FMPES e UEA)** | Instituição e regulamentação das contribuições compulsórias sobre incentivos fiscais destinadas a fundos públicos. | **Alta** | Avaliação do custo tributário total e segurança jurídica contra glosas. |
| **Lei nº 7.965/1989 e Dec. 4.095/2002** | Criação e regulamentação da Área de Livre Comércio de Tabatinga (ALC Tabatinga). | **Média** | Regime aduaneiro e tributário especial de fronteira. |
| **Decreto Estadual nº 4.564/1979 e alterações** | Regulamento do Processo Administrativo Tributário (RPAF/AM) e Conselho de Recursos Fiscais (CRF/AM). | **Alta** | Defesa administrativa tributária e suspensão de exigibilidade. |

---

## 2. Relacionamento Interestadual com as 26 UFs e Distrito Federal

```
                                      +------------------------------------+
                                      |     ESTADO DO AMAZONAS (AM)        |
                                      +------------------------------------+
                                       /          |                \
        Saída Interestadual Geral (12%)|          |Entradas Nac.   |Bens Importados >40%
        PPB ZFM: Alíquota 12% (Res.13) |          |(Conv. ICM 65)  |(sem PPB): 4%
                                       v          v                v
                        +--------------------+  +---------------+  +---------------------+
                        | Demais 26 UFs e DF |  |Isenção Origem |  | Todas as UFs Destino|
                        | (Sul, SE, Centro,  |  |Créd.Presumido |  +---------------------+
                        | Norte e Nordeste)  |  |7% ou 12% AM   |
                        +--------------------+  +---------------+
```

### 2.1. Matriz de Alíquotas Interestaduais (Resoluções SF nº 22/1989, 95/1996 e 13/2012)

O Estado do Amazonas situa-se na Região Norte do Brasil. Conforme a regra federativa de compensação regional:
- **Saídas do Amazonas para qualquer Unidade da Federação:** A alíquota interestadual geral aplicável é de **12%** (Resolução do Senado Federal nº 22/1989), tanto para os Estados das Regiões Norte, Nordeste e Centro-Oeste quanto para os Estados desenvolvidos do Sul e Sudeste.
- **Entradas interestaduais no Amazonas:**
  - Remessas oriundas do **Sul e Sudeste (exceto Espírito Santo):** Alíquota interestadual na origem de **7%**.
  - Remessas oriundas do **Norte, Nordeste, Centro-Oeste e Espírito Santo:** Alíquota interestadual na origem de **12%**.
- **Transporte Aéreo Interestadual:** Alíquota unificada de **4%** (Resolução SF nº 95/1996).

#### Exceção Vital do Polo Industrial de Manaus na Resolução SF nº 13/2012
A Resolução do Senado Federal nº 13/2012 impõe alíquota interestadual de **4%** para mercadorias importadas ou submetidas a processo produtivo com Conteúdo de Importação superior a 40% (CST de origem 1, 2, 3 ou 8). 
**Contudo, por mandamento expresso do art. 1º, § 4º, inciso II da referida Resolução, essa restrição NÃO SE APLICA às mercadorias produzidas na Zona Franca de Manaus segundo os Processos Produtivos Básicos (PPB - Decreto-Lei nº 288/1967).**
- Mercadorias industrializadas no PIM com PPB (CST de Origem `4`): mantêm a **alíquota interestadual de 12%** em suas saídas para qualquer destino nacional, mesmo quando constituídas predominantemente de componentes eletrônicos ou matérias-primas importadas do exterior.

### 2.2. Tratamento Singular da Zona Franca de Manaus (ZFM) e Convênios Nacionais

A Zona Franca de Manaus goza de imunidade/isenção constitucional com amparo nos artigos 40 e 92-A do Ato das Disposições Constitucionais Transitórias (ADCT) da CF/88 c/c Decreto-Lei nº 288/1967:

```
                            SISTEMÁTICA FISCAL ZFM / CONVÊNIO ICM 65/88
   +-----------------------+                         +-------------------------------+
   | Remetente Nacional    |                         | Indústria Incentivada no PIM  |
   | (Sul, SE, Centro, NE) |                         | (Manaus - Amazonas)           |
   +-----------------------+                         +-------------------------------+
              |                                                      |
              | 1. Saída com ISENÇÃO DE ICMS                         | 3. Apropriação de CRÉDITO
              |    (Convênio ICM 65/1988)                            |    PRESUMIDO (art. 49 DL 288)
              |    Abate ICMS desonerado da NF-e                     |    7% (Sul/SE) ou 12% (demais)
              +----------------------------------------------------->|
                                                                     | 4. Industrialização com PPB
                                                                     |
                                                                     v
   +-----------------------+                         +-------------------------------+
   | Destinatário no Brasil| <-----------------------| Saída Interestadual tributada |
   | (Direito ao Crédito)  |   NF-e com ICMS a 12%   | a 12% + Crédito Estímulo      |
   +-----------------------+   (Tema 517 STF)        | deduzido internamente         |
                                                     +-------------------------------+
```

1. **Remessas de Mercadorias de Origem Nacional destinadas à ZFM:**
   - **Isenção do ICMS de Origem:** Nos termos do Convênio ICM nº 65/1988 e do art. 4º do Decreto-Lei nº 288/1967, a saída de produtos industrializados de origem nacional para internamento na ZFM (Manaus, Rio Preto da Eva e Presidente Figueiredo) é equiparada a exportação para o exterior, sendo isenta do ICMS. O remetente abate o valor do imposto desonerado do preço faturado.
   - **Direito a Crédito Presumido no Amazonas:** Nos termos do art. 49 do Decreto-Lei nº 288/1967 e do art. 15 da Lei Estadual nº 2.826/2003, o adquirente industrial amazonense escritura em sua escrita fiscal um **crédito fiscal presumido de ICMS** no montante de **7%** (se oriundo do Sul/Sudeste) ou **12%** (se oriundo do N/NE/CO/ES), recompondo o crédito como se o imposto tivesse sido integralmente cobrado.
   - **Controle de Internamento (Convênio ICMS nº 23/2008):** O gozo dos benefícios subordina-se à homologação do desembaraço físico e eletrônico conjunto perante a SEFAZ/AM e a SUFRAMA (Suframaweb / Sistema Vistoria Eletrônica).

2. **Crédito Pleno na Destinação Final Interestadual (Tema 517 STF):**
   - O Supremo Tribunal Federal, ao julgar o RE nº 593.542/PR (Tema 517 de Repercussão Geral), fixou a tese de que: *"O adquirente de mercadorias provenientes da Zona Franca de Manaus tem direito ao creditamento do ICMS destacado na nota fiscal de saída, nos termos do art. 40 do ADCT e da Lei Complementar nº 24/1975"*, fulminando as pretensões de Secretarias de Fazenda de outros Estados de glosar créditos derivados do PIM.

### 2.3. DIFAL (EC nº 87/2015, LC nº 190/2021 e Convênio ICMS nº 236/2021)

1. **DIFAL Destinado a Não Contribuintes (B2C / E-Commerce):**
   - Nas operações e prestações interestaduais que destinem bens e serviços a consumidor final não contribuinte no Amazonas, aplica-se a sistemática da LC nº 190/2021 e Convênio ICMS nº 236/2021.
   - A base de cálculo é única (valor da operação acrescido do frete, despesas acessórias e montante do ICMS interno do AM).
   - O DIFAL é partilhado: a alíquota interestadual (4%, 7% ou 12%) pertence ao Estado de origem, e a diferença até a alíquota modal do Amazonas (**20%**, nos termos da LC nº 242/2022) acrescida de até 2% de Fundo de Promoção Social e Erradicação da Pobreza (FPS/AM, Lei nº 3.584/2010), quando aplicável a bens supérfluos, pertence integralmente à SEFAZ/AM.

2. **DIFAL para Bens de Uso, Consumo e Ativo Permanente de Contribuinte (Base Dupla):**
   - O Estado do Amazonas adota formalmente a metodologia da **Base Dupla (Cálculo por Dentro)**, disposta no Art. 13 da Lei Complementar Estadual nº 19/1997 (com as alterações introduzidas pela LC nº 219/2021):
     $$V_{\text{sem ICMS}} = V_{\text{operação interestadual}} \times (1 - \text{ALQ}_{\text{origem}})$$
     $$BC_{\text{destino (AM)}} = \frac{V_{\text{sem ICMS}}}{1 - \text{ALQ}_{\text{interna AM}}}$$
     $$\text{DIFAL}_{\text{devido}} = (BC_{\text{destino}} \times \text{ALQ}_{\text{interna AM}}) - (V_{\text{operação}} \times \text{ALQ}_{\text{origem}})$$

### 2.4. Transferências entre Estabelecimentos do Mesmo Titular (ADC 49 STF, LC 204/2023 e Convênio ICMS 109/2024)

- Em conformidade com a decisão definitiva do STF na **ADC 49**, o art. 12, § 4º da LC nº 87/1996 (redação da LC nº 204/2023) estabeleceu a **não incidência de ICMS** nas saídas físicas de mercadorias entre matriz e filiais ou filiais entre si.
- O **Convênio ICMS nº 109/2024** disciplinou o direito de crédito:
  - **Regra Padrão (CFOP 6.151/6.152):** Não há destaque de imposto próprio a pagar, mas opera-se a transferência de créditos acumulados vinculados à entrada, limitados à aplicação das alíquotas interestaduais (4%, 7% ou 12%) sobre o custo de produção ou média móvel ponderada das entradas.
  - **Opção de Equiparação a Venda Tributada (Cláusula Sexta do Conv. 109/2024):** O contribuinte estabelecido no PIM pode optar formalmente, em termo lavrado no Livro RUDFTO, pela tributação da operação de transferência interestadual como se de venda se tratasse, viabilizando o destaque de 12% de ICMS para possibilitar a fruição do crédito estímulo da Lei Estadual nº 2.826/2003 e viabilizar a transferência límpida do crédito de 12% ao adquirente localizado em outra UF.

### 2.5. Substituição Tributária (ICMS-ST) e Desembaraço DT-e

- O Estado do Amazonas integra dezenas de Protocolos ICMS no CONFAZ (combustíveis, bebidas, fumo, veículos, fármacos e cosméticos).
- **MVA Ajustada Interestadual (Convênio ICMS nº 142/2018):**
  $$\text{MVA Ajustada} = \left[ \frac{(1 + \text{MVA-ST Original}) \times (1 - \text{ALQ Inter})}{(1 - \text{ALQ Intra AM})} \right] - 1$$
- **Desembaraço DT-e na Fronteira/Porto:** Conforme art. 107 do RICMS/AM, nenhuma mercadoria ingressa fisicamente no Estado sem prévia liberação pelo Domicílio Tributário Eletrônico (DT-e) e validação da Guia Nacional de Recolhimento (GNRE) da ST ou da antecipação tributária do imposto.

---

## 3. Mecanismos de Dedução e Crédito do ICMS

### 3.1. Não-Cumulatividade, Apropriação e Manutenção de Créditos

- **Regra Geral:** O imposto é não-cumulativo, compensando-se o que for devido em cada operação relativa à circulação de mercadorias com o montante cobrado nas anteriores pelo Estado do Amazonas ou por outra UF (art. 155, § 2º, I da CF c/c Lei Complementar nº 87/1996 e LC nº 19/1997).
- **Manutenção de Crédito em Exportações:** As saídas para o exterior são imunes (art. 155, § 2º, X, "a" da CF/88), assegurada a manutenção e o aproveitamento integral dos créditos fiscais cobrados nas etapas antecedentes de aquisição de insumos, matérias-primas e energia consumida.
- **Estorno Obrigatório:** Opera-se o estorno proporcional do crédito de entrada quando a operação subsequente for isenta ou não tributada (exceto se houver cláusula expressa de manutenção em Convênio CONFAZ ou na Lei 2.826/2003).

### 3.2. Controle de Crédito do Ativo Permanente (CIAP — LC nº 102/2000)

- Os créditos relativos à entrada de bens destinados ao ativo imobilizado do estabelecimento fabril ou comercial são apropriados à razão de **1/48 (um quarenta e oito avos) por mês**, nos termos do art. 20, § 5º da LC nº 87/1996 e disciplina regulamentar do RICMS/AM:
  $$\text{Crédito Mensal Apropriável} = \left(\frac{\text{Crédito Total do Bem}}{48}\right) \times \left(\frac{\text{Saídas Tributadas e Exportações}}{\text{Total das Saídas}}\right)$$
- **Diferimento de Ativo para Indústrias do PIM:** Na esteira do art. 14, II da Lei Estadual nº 2.826/2003, as indústrias incentivadas possuem o benefício de **diferimento do ICMS** incidente na importação do exterior e no DIFAL interestadual na aquisição de máquinas e equipamentos novos para emprego fabril, eliminando a retenção de caixa e a dependência do estorno/recomposição do CIAP.

### 3.3. Restrições Legais sobre Energia Elétrica e Serviços de Comunicação (LC nº 87/96 e LC nº 194/22)

- **Energia Elétrica (Art. 33, II da LC nº 87/1996):** O crédito de ICMS referente à entrada de energia elétrica só é admitido:
  1. Quando for objeto de operação de subsequente saída de energia;
  2. Quando consumida no processo de industrialização (mediante laudo técnico pericial de consumo de energia fabril rateando a área administrativa);
  3. Quando o percentual de saídas para o exterior superar os limites da LC 87/96.
- **Comunicações (Art. 33, IV da LC nº 87/1996):** Tomada de crédito vedada para estabelecimentos em geral, autorizada exclusivamente para concessionárias de telecomunicação na prestação de seus próprios serviços.
- **Impacto da LC nº 194/2022:** A energia elétrica e as telecomunicações foram categorizadas como bens e serviços essenciais, limitando a alíquota interna ao teto modal geral do Estado (20%), vedando a aplicação de alíquotas majoradas seletivas que historicamente chegavam a 25%.

---

## 4. Setor Agrícola, Rural e Extrativismo Sustentável

### 4.1. Perfil Econômico-Tributário Regional

O setor rural no Estado do Amazonas é caracterizado pela coexistência entre a agricultura familiar ribeirinha, a agroindústria de polpas e derivados de frutas nativas, o manejo florestal sustentável de madeira e o extrativismo não madeireiro da sociobiodiversidade (açaí, castanha-do-brasil, borracha natural/látex, guaraná de Maués, cacau nativo e piscicultura intensiva de espécies amazônicas como pirarucu e tambaqui).

### 4.2. Insumos Agropecuários (Convênio ICMS nº 100/1997 e Convênio ICMS nº 26/2021)

- Aplicação integral do Convênio ICMS nº 100/1997 no Estado do Amazonas:
  - **Isenção e Redução da Base de Cálculo:** Inseticidas, fungicidas, herbicidas, sementes certificadas, adubos e fertilizantes usufruem de redução da base de cálculo nas operações interestaduais e internas, com alíquotas escalonadas introduzidas pelo Convênio ICMS nº 26/2021.
  - **Rações e Alimentos para Aquicultura:** Insumos destinados à alimentação de peixes de cativeiro no Amazonas possuem desoneração tributária para fomento da cadeia aquícola do Rio Solimões e Médio Amazonas.

### 4.3. Diferimento do ICMS nas Saídas Internas de Produtor Rural

- **Diferimento Operacional:** As saídas de produtos agrícolas e extrativos *in natura* promovidas por pequenos produtores rurais ou extrativistas cadastrados com destino a cooperativas, centrais de processamento ou indústrias estabelecidas no Estado são submetidas a **diferimento do lançamento do ICMS** para a etapa da saída subsequente do produto beneficiado ou industrializado.
- **Dispensa de Emissão Formal:** Extrativistas não personificados operam sob regime simplificado, sendo o ICMS acobertado mediante Nota Fiscal de Entrada emitida pelo estabelecimento adquirente (indústria ou cooperativa).

### 4.4. Créditos Presumidos para Agroindústria e Produtos da Biodiversidade

- **Incentivo da Lei nº 2.826/2003 (Art. 16, I, "c"):** As agroindústrias e indústrias fitoterápicas e farmoquímicas que utilizem matérias-primas regionais nativas extrativas (como óleos essenciais de andiroba e copaíba, castanha e guaraná) fazem jus ao **Crédito Estímulo máximo de 100%** do saldo devedor de ICMS, além de isenção de taxas estaduais, visando à interiorização do desenvolvimento econômico.
- **Subvenção Estadual ao Manejo de Borracha e Juta:** Pagamento de subsídios diretos com dispensa tributária integral de ICMS para fixação do homem no campo e proteção florestal.

### 4.5. Nota Fiscal de Produtor Eletrônica (NFP-e) e Cadastro do Produtor Rural

- A SEFAZ/AM implementou a obrigatoriedade da **NFP-e (modelo 55)** para produtores rurais com faturamento relevante, mantendo a emissão pelo aplicativo "Nota Fiscal Fácil - NFF" para pequenos sitiantes e cooperados.

---

## 5. Setor Industrial: O Polo Industrial de Manaus (PIM / ZFM)

### 5.1. Mecânica Jurídica do PIM (Lei Estadual nº 2.826/2003)

O Polo Industrial de Manaus abriga um dos maiores complexos fabris da América Latina, estruturado em torno de incentivos vinculados ao Processo Produtivo Básico (PPB):

```
       MATRIZ DE CRÉDITO ESTÍMULO DO ICMS - LEI ESTADUAL Nº 2.826/2003 (AM)
+--------------------------------------------------------------+--------------------+
| Categoria Industrial / Tipo de Produto                       | Crédito Estímulo   |
+--------------------------------------------------------------+--------------------+
| - Bens Intermediários (insumos fabris, componentes, placas)  |                    |
| - Bens de Informática e Automação e Celulares                |      100,00%       |
| - Brinquedos, Medicamentos Regionais e Agroindústria         |                    |
+--------------------------------------------------------------+--------------------+
| - Bens de Capital (máquinas, equipamentos, ferramentas)      |                    |
| - Polo de Duas Rodas (motocicletas e ciclomotores)           |       90,25%       |
| - Ar Condicionado, Relógios e Lentes Ópticas                 |                    |
+--------------------------------------------------------------+--------------------+
| - Bens de Consumo Eletroeletrônicos (TVs LED/OLED, Som, etc) |       75,00%       |
+--------------------------------------------------------------+--------------------+
| - Concentrados e Xaropes de Bebidas / Refrigerantes          |       55,00%       |
+--------------------------------------------------------------+--------------------+
```

### 5.2. Desoneração Aduaneira na Importação de Insumos

- **Diferimento Integral na Entrada de Insumos:** Conforme art. 14, I da Lei nº 2.826/2003, a importação de matérias-primas, produtos intermediários e embalagens destinados à linha de produção incentivada no Amazonas ocorre com **diferimento de 100% do ICMS da importação**. O imposto diferido é considerado recolhido/compensado no momento da saída da mercadoria acabada mediante a aplicação dos percentuais de crédito estímulo.

### 5.3. Contrapartidas Financeiras aos Fundos Estaduais (FTI, UEA e FMPES)

As indústrias incentivadas no PIM são obrigadas, sob pena de perda imediata do crédito estímulo, a recolher encargos parafiscais mensais:
1. **Fundo de Fomento ao Turismo, Infraestrutura e Interiorização (FTI):** Recolhimento de percentual que varia de **1,0% a 2,0%** sobre o valor FOB das importações de insumos ou sobre o faturamento de produtos incentivados (Lei nº 2.826/2003 e Lei nº 3.830/2012).
2. **Universidade do Estado do Amazonas (UEA):** Contribuição de **1,0% a 1,5%** sobre o faturamento bruto ou sobre o valor nominal do crédito estímulo apurado (Lei nº 2.879/2004). O STF analisou a constitucionalidade da cobrança da cota UEA na ADI 5.485/AM, validando os parâmetros gerais da contrapartida aos benefícios fiscais concedidos com base no pacto federativo regional.
3. **Fundo de Apoio às Micro e Pequenas Empresas (FMPES):** Cota mensal de apoio ao desenvolvimento de microempreendimentos locais.

### 5.4. Convalidação perante a Lei Complementar nº 160/2017 e Convênio ICMS 190/2017

Embora os incentivos do PIM possuam assento constitucional autônomo (art. 40 do ADCT), o Estado do Amazonas efetuou o registro e depósito formal da Lei nº 2.826/2003 e de seus atos concessivos no CONFAZ, conferindo blindagem integral contra questionamentos tributários interestaduais de "guerra fiscal" até 31 de dezembro de 2032.

---

## 6. Setor de Produto Acabado: Atacado, Varejo, Distribuição e E-Commerce

### 6.1. Área de Livre Comércio de Tabatinga (ALC Tabatinga)

- Criada pela Lei Federal nº 7.965/1989 e regulamentada pelo Decreto nº 4.095/2002, a ALC Tabatinga situa-se na tríplice fronteira Brasil-Colômbia-Peru.
- As remessas de mercadorias nacionais para a ALC Tabatinga gozam de isenção de ICMS nos moldes do Convênio ICMS nº 52/1992 e Convênio ICM nº 65/1988, com destinação ao consumo e comercialização interna no município de Tabatinga, sendo vedada a reintrodução irregular para o restante do território nacional sem o pagamento do imposto desonerado.

### 6.2. Comércio Atacadista e Corredor de Importação de Manaus

- **Corredor de Importação (Lei Estadual nº 3.830/2012):** Para mercadorias destinadas à comercialização (fora do modelo fabril do PIM), o Amazonas disponibiliza o regime de entreposto aduaneiro e corredor comercial, com diferimento de ICMS no desembaraço e carga tributária reduzida na saída interestadual, fomentando centros atacadistas e importadores sediados em Manaus.

### 6.3. Comércio Eletrônico e Responsabilidade de Marketplaces

- **Responsabilidade Tributária:** O Amazonas implementou o regime de responsabilização solidária para plataformas digitais de intermediação de vendas e intermediadores logísticos que não exigirem nota fiscal idônea ou facilitarem o descaminho tributário em território amazonense (alterações da LC nº 19/1997 e regulamentação SEFAZ/AM).
- **Controle de Escoamento Aeroportuário:** Rígida fiscalização no Aeroporto Internacional Eduardo Gomes e portos fluviais de Manaus, com cruzamento imediato de MDF-e, NF-e e CT-e antes do embarque das encomendas para o restante do país.

---

## 7. Transição para o IBS / CBS da Reforma Tributária (EC nº 132/2023 e LC nº 214/2025)

```
                            MODELO CONSTITUCIONAL ZFM NA REFORMA TRIBUTÁRIA
+---------------------------------------------------------------------------------------------------------+
| Art. 40 e 92-A do ADCT / EC nº 132/2023: PRESERVAÇÃO CONSTITUCIONAL DO DIFERENCIAL COMPETITIVO DA ZFM |
+---------------------------------------------------------------------------------------------------------+
       |                                      |                                    |
       v                                      v                                    v
+-------------------------------+  +-------------------------------+  +-------------------------------+
| Créditos Presumidos de IBS/CBS|  | CIDE-ZFM / CIDE-Importação    |  | Imposto Seletivo (IS)         |
| Indústrias com PPB geram      |  | Tributação federal extra sobre|  | Incidência sobre produtos de  |
| crédito financeiro pleno no   |  | produção nacional/estrangeira |  | fora da ZFM concorrentes com  |
| destino final sem glosa.      |  | de bens fabricados no PIM.    |  | bens fabricados no PIM.       |
+-------------------------------+  +-------------------------------+  +-------------------------------+
```

### 7.1. O Tratamento Constitucional Exclusivo da Zona Franca de Manaus (EC nº 132/2023)

A Emenda Constitucional nº 132/2023 e a Lei Complementar nº 214/2025 asseguraram de forma inédita e explícita a intangibilidade do modelo de desenvolvimento da Zona Franca de Manaus:
1. **Preservação do Diferencial Competitivo (Art. 92-B do ADCT):** A União e os Estados são obrigados a manter os diferenciais econômicos da ZFM em relação às demais regiões do País nos impostos sobre bens e serviços (IBS e CBS).
2. **Crédito Presumido de IBS e CBS:** Os adquirentes de produtos industrializados no PIM conforme PPB farão jus a **créditos presumidos de IBS e de CBS**, garantindo que a aquisição do produto fabricado em Manaus mantenha carga fiscal substancialmente inferior à produção fabricada em outras UFs.
3. **Cide-Importação / Cide-ZFM:** Instituição de contribuição de intervenção no domínio econômico incidente sobre a importação e a comercialização de bens originários de outros locais que rivalizem diretamente com a produção da ZFM.
4. **Imposto Seletivo (Art. 153, VIII e art. 92-B, § 1º do ADCT):** Incidência de Imposto Seletivo federal sobre produtos de outras origens concorrentes aos bens produzidos no Polo Industrial de Manaus, mantendo o desnível de preços em favor da indústria amazonense.

### 7.2. Extinção Progressiva do ICMS (2029 a 2032) e Adaptação dos Fundos Estaduais

- O ICMS entrará em fase de decréscimo proporcional de suas alíquotas (90% em 2029, 80% em 2030, 70% em 2031, 60% em 2032 e extinção em 2033).
- **Fundo de Sustentabilidade Hidráulica e Bioeconômica do Amazonas (Art. 92-B, § 2º do ADCT):** Recursos federais específicos serão aportados para compensar a substituição gradual das contribuições do FTI, UEA e FMPES, viabilizando o equilíbrio das contas públicas do Amazonas no pós-ICMS.

### 7.3. Homologação do Saldo Credor Acumulado de ICMS (Art. 134 do ADCT / LC nº 214/2025)

- **Regra Geral:** Os estabelecimentos do Amazonas que acumularem saldos credores legítimos de ICMS até 31 de dezembro de 2032 deverão protocolar pedido de **homologação perante a SEFAZ/AM**.
- **Amortização em 240 Meses:** Uma vez homologados pela autoridade fazendária no prazo previsto na lei complementar federal, os saldos serão amortizados em **240 (duzentas e quarenta) parcelas mensais, iguais e sucessivas**, corrigidas pelo IPCA, utilizáveis para compensação direta com o **IBS** (ou ressarcidas financeiramente pelo Comitê Gestor do IBS caso inviável a compensação).
- **Particularidade do PIM:** Devido à sistemática do crédito estímulo e das compras com crédito presumido da ZFM, a análise fazendária do Amazonas será altamente rigorosa na verificação da efetiva entrada física, legitimidade de laudos do CODAM e adimplemento das cotas da UEA/FTI antes de autorizar a conversão para moeda de crédito de IBS.

---

## 8. Plano de Ação e Recomendações Normativas para o Repositório

Com base no diagnóstico da auditoria, formulam-se as seguintes recomendações prioritárias para complementação do acervo documental do Estado do Amazonas:

1. **Incorporação da Lei Complementar nº 242/2022:** Atualizar a documentação do RICMS/AM com o texto oficial da lei que elevou a alíquota modal para 20%.
2. **Elaboração de Documento Normativo do Contencioso Administrativo (PAT/AM):** Inserir diretório `estaduais/am/pat/` com o Decreto nº 4.564/1979 e a Lei nº 4.730/2018 para municiar o repositório com o procedimento de defesa fiscal, recursos ordinários e pedidos de reconsideração ao CRF/AM.
3. **Mapeamento Consolidado do Processo Produtivo Básico (PPB):** Adicionar sumário com as Portarias Interministeriais MDIC/MCTI que definem as etapas fabris mínimas exigidas das indústrias incentivadas para manutenção do CST 4 e alíquota de 12%.
4. **Codificação da Legislação dos Fundos FTI, UEA e FMPES:** Estruturar as fórmulas de cálculo e bases de incidência das taxas de contrapartida para cálculo de viabilidade financeira e contábil das indústrias incentivadas.
