# Relatório de Auditoria Tributária Estadual: Pará (PA)
**Unidade Federativa:** Pará | **Sigla:** PA | **Região:** Norte  
**Órgão Fazendário:** Secretaria de Estado da Fazenda do Pará (SEFA/PA)  
**Data da Auditoria:** Outubro de 2026 | **Status:** Atualizado com a EC nº 132/2023 e LC nº 214/2025  

---

## 1. Mapeamento das Normas no Repositório e Diagnóstico de Lacunas

### 1.1. Acervo Documental Existente no Repositório (`estaduais/pa/`)

O repositório apresenta atualmente as seguintes peças no âmbito do Estado do Pará:

1. [`estaduais/pa/ricms/decreto-4676-2001.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/pa/ricms/decreto-4676-2001.md): Estrutura sintética do Regulamento do ICMS do Estado do Pará (RICMS/PA), aprovado pelo Decreto nº 4.676, de 18 de junho de 2001.
2. [`estaduais/pa/leis/itcmd/lei-5529-1989.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/pa/leis/itcmd/lei-5529-1989.md): Disposições normativas do Imposto sobre Transmissão Causa Mortis e Doação (ITCMD), instituído pela Lei Estadual nº 5.529, de 05 de janeiro de 1989.
3. [`estaduais/pa/leis/ipva/lei-6017-1996.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/pa/leis/ipva/lei-6017-1996.md): Regime jurídico do Imposto sobre a Propriedade de Veículos Automotores (IPVA), fundado na Lei Estadual nº 6.017, de 27 de dezembro de 1996.

### 1.2. Inventário de Normas Fundamentais Ausentes (Lacunas Críticas)

Para propiciar suporte fático e jurídico pleno, o repositório demanda a imediata integração dos seguintes diplomas:

| Diploma Legal Faltante | Ementa / Objeto Jurídico | Prioridade | Impacto Técnico no Repositório |
| :--- | :--- | :---: | :--- |
| **Lei Estadual nº 5.530/1989 (Texto Consolidado)** | Lei Orgânica do ICMS do Estado do Pará — Fatos geradores, base de cálculo, sujeição passiva, responsabilidade e infrações. | **Crítica** | Matriz de estrita legalidade tributária do imposto estadual. |
| **Lei Estadual nº 9.755/2022** | Elevação da alíquota modal interna do ICMS de 17% para 19% (vigente desde março de 2023). | **Crítica** | Fixação de base para cálculo de DIFAL e operações internas. |
| **Lei Estadual nº 7.591/2011 (TFRM)** | Instituição da Taxa de Controle, Acompanhamento e Fiscalização das Atividades de Pesquisa, Lavra, Exploração e Aproveitamento de Recursos Minerais (TFRM). | **Crítica** | Marco da tributação da atividade minerária paraense (validada na ADI 4785 STF). |
| **Lei Estadual nº 6.489/2002 e Dec. nº 2.492/2006** | Política de Incentivos ao Desenvolvimento Socioeconômico do Pará — Créditos presumidos industriais, minerais e agropecuários. | **Alta** | Regime de atração fabril e verticalização de matérias-primas locais. |
| **Lei Estadual nº 6.182/1998** | Regula o Processo Administrativo Tributário (PAT/PA) e o Tribunal Administrativo de Recursos Tributários (TART/PA). | **Alta** | Impugnação de autos de infração e defesas administrativas. |
| **Anexos e Apêndices do RICMS/PA (Dec. 4.676/01)** | Apêndice I (Antecipação Especial de Entrada) e Anexo XIII (Substituição Tributária). | **Alta** | Operações diárias interestaduais e retenção nas fronteiras. |
| **Lei Estadual nº 8.328/2015** | Lei Geral de Taxas Estaduais da Secretaria de Estado da Fazenda (SEFA/PA). | **Média** | Custos operacionais acessórios e fiscalização. |

---

## 2. Relacionamento Interestadual com as 26 UFs e Distrito Federal

```
                                      +------------------------------------+
                                      |       ESTADO DO PARÁ (PA)          |
                                      +------------------------------------+
                                       /          |                \
         Saídas Interestaduais (12%)  |          |Entradas Sul/SE |Importados >40%: 4%
         Mercadorias Nacionais        |          |Origem: 7%      |(Resolução SF 13/12)
                                      v          v                v
                        +--------------------+  +---------------+  +---------------------+
                        | Demais 26 UFs e DF |  | Base Dupla no |  | Todas as UFs Destino|
                        | (Sul, SE, Centro,  |  | Destino (PA): |  +---------------------+
                        | Norte e Nordeste)  |  | DIFAL = 19%-7%|
                        +--------------------+  +---------------+
```

### 2.1. Matriz de Alíquotas Interestaduais (Resoluções SF nº 22/1989 e 13/2012)

- **Saídas promovidas por contribuintes do Pará para qualquer UF:** A alíquota interestadual geral aplicável é de **12%** (Resolução do Senado Federal nº 22/1989), por integrar a Região Norte. Aplica-se nas vendas destinadas aos Estados das Regiões Sul e Sudeste, bem como aos Estados do Norte, Nordeste e Centro-Oeste.
- **Entradas interestaduais no Pará:**
  - Procedentes das Regiões **Sul e Sudeste (exceto Espírito Santo):** Alíquota de **7%**.
  - Procedentes das Regiões **Norte, Nordeste, Centro-Oeste e Estado do Espírito Santo:** Alíquota de **12%**.
- **Bens e Mercadorias Importadas do Exterior (Resolução SF nº 13/2012):**
  - Alíquota uniforme de **4%** em operações interestaduais com bens importados ou que possuam Conteúdo de Importação superior a 40% (CST de origem 1, 2, 3 ou 8), ressalvadas as hipóteses sem similar nacional da Lista CAMEX ou gás natural.

### 2.2. Diferencial de Alíquotas (DIFAL) nas Entradas em Território Paraense

#### 1. DIFAL Contribuinte (Uso, Consumo e Ativo Permanente — Base Dupla)
Nos termos do Art. 12 da Lei Estadual nº 5.530/1989 (com redação aperfeiçoada pela Lei nº 8.870/2019 e Lei nº 9.541/2022), o Estado do Pará exige o DIFAL pelo método de **Base Dupla (Cálculo por Dentro)**:
1. Exclusão do ICMS de origem do valor da operação:
   $$V_{\text{sem ICMS}} = V_{\text{operação}} \times (1 - \text{ALQ}_{\text{inter}})$$
2. Inclusão da alíquota interna do Pará (19%):
   $$BC_{\text{destino (PA)}} = \frac{V_{\text{sem ICMS}}}{1 - 0{,}19}$$
3. Apuração do imposto devido ao Estado do Pará:
   $$\text{DIFAL}_{\text{PA}} = (BC_{\text{destino}} \times 0{,}19) - (V_{\text{operação}} \times \text{ALQ}_{\text{inter}})$$

#### 2. DIFAL Não Contribuinte (EC nº 87/2015, LC nº 190/2021 e Convênio ICMS nº 236/2021)
- Nas vendas B2C destinadas a consumidor final não contribuinte no Pará, o remetente de outra UF recolhe o DIFAL mediante aplicação de base única.
- **Inexistência de FCP Geral:** O Estado do Pará é uma das poucas unidades federativas que **não instituiu adicional geral de Fundo de Combate à Pobreza (0% de FCP)** sobre a alíquota modal interna, facilitando o cálculo da diferença estrita de $19\% - 12\% = 7\%$ (ou $19\% - 7\% = 12\%$ nas compras de origem importada a 4%, onde o DIFAL é $19\% - 4\% = 15\%$).

### 2.3. Transferências Interestaduais entre Estabelecimentos do Mesmo Titular (ADC 49 STF e Convênio ICMS 109/2024)

- **Não Incidência:** Em atendimento à ADC 49 e à Lei Complementar nº 204/2023, as remessas de mercadorias entre matriz e filiais do mesmo titular não constituem fato gerador de ICMS.
- **Transferência de Créditos:** A remessa interestadual transfere ao estabelecimento destinatário créditos limitados às alíquotas interestaduais (4% ou 12%) aplicadas sobre o custo de produção dos insumos ou valor de entrada dos produtos (CFOP 6.151/6.152).
- **Opção pelo Regime de Tributação Normal:** Conforme facultado pela Cláusula Sexta do Convênio ICMS nº 109/2024, contribuintes paraenses (especialmente do complexo agroindustrial e mineral) podem optar anualmente pela equiparação à operação regularmente tributada, mantendo o destaque integral do imposto para viabilizar a fruição encadeada de incentivos fiscais locais e neutralizar passivos de glosa em outras UFs.

### 2.4. ICMS-ST e Antecipação Especial (Apêndice I do RICMS/PA)

- **MVA Ajustada nas Entradas Interestaduais:**
  $$\text{MVA Ajustada} = \left[ \frac{(1 + \text{MVA-ST Original}) \times (1 - \text{ALQ Inter})}{(1 - 0{,}19)} \right] - 1$$
- **Antecipação Especial de Entrada:** O Pará adota regime de antecipação do ICMS sem encerramento da fase de tributação sobre mercadorias relacionadas no Apêndice I do RICMS/PA oriundas de outras UFs, exigindo o recolhimento antecipado no primeiro posto fiscal de divisa interestadual (Itinga, Serra do Cachimbo, etc.) ou via DAE pago antecipadamente.

---

## 3. Mecanismos de Dedução e Crédito do ICMS

### 3.1. Princípio da Não-Cumulatividade e Dinâmica Creditória

- Compensação integral do imposto devido com o montante anteriormente cobrado nas operações com insumos, matérias-primas e embalagens destinadas à comercialização ou processo de transformação industrial (art. 155, § 2º, I da CF c/c Lei Complementar nº 87/1996 e Lei nº 5.530/1989).
- **Manutenção de Créditos na Exportação (Art. 155, § 2º, X, "a" da CF - Lei Kandir):** 
  - As exportações diretas e remessas com fim específico de exportação de produtos minerais (minério de ferro, cobre, bauxita) e agropecuários (soja, carne bovina) são completamente desoneradas do ICMS.
  - Assegura-se expressamente a **manutenção e o acúmulo de créditos fiscais** de ICMS suportados na compra de máquinas, combustíveis, reagentes químicos fabris e energia elétrica utilizada na extração e processamento.
  - **O Desafio do Saldo Credor Acumulado:** O Pará abriga o maior estoque per capita de créditos acumulados de ICMS decorrentes da Lei Kandir no País, exigindo ritos de transferência para terceiros e compensações na SEFA/PA (Decreto nº 4.676/2001, arts. 54 a 60).

### 3.2. Controle de Crédito do Ativo Imobilizado (CIAP — LC nº 102/2000)

- Créditos sobre bens adquiridos para o Ativo Não Circulante Imobilizado são escriturados em Bloco G da EFD-ICMS/IPI e apropriados na proporção de **1/48 (um quarenta e oito avos) mensal**:
  $$\text{Fração Mensal} = \left(\frac{\text{ICMS Destacado no Bem}}{48}\right) \times \left(\frac{\text{Operações Tributadas} + \text{Exportações Desoneradas}}{\text{Total das Saídas}}\right)$$
- No caso das grandes plantas minerárias e de beneficiamento de bauxita/alumínio em Barcarena e Carajás, o coeficiente de creditamento aproxima-se de 1,0 em razão da equiparação das exportações a saídas tributadas para efeitos de apropriação do CIAP.

### 3.3. Restrições Legais sobre Energia Elétrica e Telecomunicações (LC nº 87/96 e LC nº 194/22)

- **Energia Elétrica (Art. 33, II da LC nº 87/96):** Crédito restrito à energia diretamente consumida no processo fabril, exigindo laudo técnico expedido por engenheiro pericial habilitado para segregação do consumo da planta industrial frente às instalações administrativas e canteiros operacionais.
- **Complexo Eletrointensivo do Alumínio (Albras / Hydro):** A produção de alumínio primário em Barcarena consome gigantescos volumes de energia hidrelétrica (UHE Tucuruí). A legislação estadual do Pará disciplinou regime especial de diferimento e compensação para impedir a estrangulação financeira por retenção de créditos de energia.
- **Teto da LC nº 194/2022:** As alíquotas de energia elétrica e serviços de telecomunicação foram niveladas à alíquota modal de 19%, cessando a cobrança histórica de 25% a 27%.

---

## 4. Setor Agrícola, Rural e Fruticultura Tropical

```
                         CADEIA DO AGRONEGÓCIO E PECUÁRIA NO PARÁ
+--------------------------+                         +-------------------------------+
| Produtor Rural Paraense  |                         | Agroindústria / Frigorífico / |
| (Soja, Milho, Gado em Pé)|                         | Tradings de Grãos Exportadoras|
+--------------------------+                         +-------------------------------+
             |                                                       |
             | Saída Interna com DIFERIMENTO DO ICMS                 | Beneficiamento / Abate
             | (Dec. nº 4.676/2001)                                  | (Crédito Outorgado / Isenção)
             +------------------------------------------------------>|
                                                                     |
                                             +-----------------------+-----------------------+
                                             |                                               |
                                             v                                               v
                             +-------------------------------+               +-------------------------------+
                             | Exportação Direta (Porto Vila |               | Mercado Interno Interestadual |
                             | do Conde / Barcarena e Itaqui)|               | Saída Tributada a 12%         |
                             | Imunidade + Manutenção Crédito|               +-------------------------------+
                             +-------------------------------+
```

### 4.1. Perfil da Fronteira Agrícola Paraense

O Estado do Pará consolidou-se como potência agropecuária:
1. **Pecuária Bovina de Corte:** Segundo maior rebanho bovino do Brasil (superando 24 milhões de cabeças), concentrado em municípios como São Félix do Xingu, Marabá e Redenção, abastecendo frigoríficos exportadores credenciados.
2. **Grãos (Soja e Milho):** Expansão acelerada nos polos de Paragominas, Dom Eliseu, Santarém e Belterra, utilizando a infraestrutura hidroviária da bacia dos rios Tapajós e Amazonas.
3. **Fruticultura Tropical e Dendê:** Líder absoluto nacional na produção de **açaí** e **cacau** (com polo de excelência em Medicilândia na Transamazônica) e concentração do polo de **óleo de palma / dendê** em Moju, Tailândia e Acará.

### 4.2. Insumos Agropecuários (Convênio ICMS nº 100/1997 e Convênio ICMS nº 26/2021)

- Aplicação das isenções e reduções de base de cálculo do Convênio ICMS nº 100/1997 em fertilizantes, calcário agrícola, adubos, sementes selecionadas e defensivos químicos, com reoneração gradual das operações interestaduais de adubos e fertilizantes conforme diretrizes do Convênio ICMS nº 26/2021.

### 4.3. Diferimento do ICMS nas Saídas Internas

- **Grãos e Gado em Pé:** As operações internas de remessa de soja, milho, arroz e gado bovino em pé do produtor agropecuário para estabelecimentos frigoríficos credenciados, cooperativas ou centrais exportadoras operam sob **diferimento do imposto**.
- O lançamento do ICMS fica diferido para o momento da saída interestadual da mercadoria ou do produto resultante de sua industrialização, ou encerra-se com a desoneração nas remessas diretas de exportação ao exterior.

### 4.4. Créditos Presumidos e Incentivos à Verticalização Agroindustrial

- **Incentivo a Frigoríficos:** Concessão de crédito presumido de ICMS aos estabelecimentos abatedores de gado bovino inscritos no Pará, assegurando carga tributária reduzida e competitiva perante os frigoríficos do Centro-Oeste e Rondônia.
- **Cacau e Palma:** Desoneração fiscal nas operações com amêndoas de cacau e óleo bruto de palma, fomentando o refino e a produção de chocolates e biocombustíveis no território estadual.

### 4.5. Nota Fiscal de Produtor Eletrônica (NFP-e) e Integração com a ADEPARA

- A SEFA/PA exige a emissão da NFP-e integrada eletronicamente aos sistemas da Agência de Defesa Agropecuária do Estado do Pará (ADEPARA), exigindo o cruzamento simultâneo entre a NF-e e a **Guia de Trânsito Animal (GTA)** para transporte e abate de rebanhos.

---

## 5. Setor Industrial e Mineral: O Maior Polo Minerário do País

### 5.1. Complexo Mineral da Província de Carajás e Bauxita/Alumínio

O Pará lidera a produção mineral brasileira:
- **Minério de Ferro, Manganês e Cobre:** Complexo minerário da Vale S.A. em Canaã dos Carajás (Complexo S11D) e Parauapebas (Mina de Carajás), com escoamento ferroviário pela Estrada de Ferro Carajás até o Porto do Itaqui (MA).
- **Cobre:** Minas de Sossego e Salobo em Marabá e Canaã dos Carajás.
- **Bauxita, Alumina e Alumínio Primário:** Mineração Rio do Norte (MRN) em Oriximiná e Hydro Paragominas, alimentando a maior refinaria de alumina do mundo (Hydro Alunorte) e a fábrica de alumínio primário (Albras) em Barcarena.

### 5.2. Taxa Mineral (TFRM — Lei Estadual nº 7.591/2011) e Julgamento da ADI nº 4.785 no STF

```
                          TRIBUTAÇÃO MINERAL NO ESTADO DO PARÁ
+------------------------------------------------------------------------------------+
| CF/1988, art. 155, § 2º, X, "a" c/c Lei Kandir (LC 87/96):                         |
| IMUNIDADE TOTAL DO ICMS NAS EXPORTAÇÕES DE MINÉRIO DE FERRO, COBRE E ALUMÍNIO       |
+------------------------------------------------------------------------------------+
                                          |
                                          v
+------------------------------------------------------------------------------------+
| Mecanismo de Arrecadação Estadual Criado pelo Pará:                                |
| LEI ESTADUAL Nº 7.591/2011 — TAXA DE CONTROLE E FISCALIZAÇÃO MINERAL (TFRM)        |
+------------------------------------------------------------------------------------+
       |
       | Julgamento da Ação Direta de Inconstitucionalidade nº 4.785 / STF:
       | -> CONSTITUCIONALIDADE RECONHECIDA PELO PLENÁRIO DO STF.
       | -> Fixação de tese: A taxa é legítima desde que o valor arrecadado guarde
       |    razoável equivalência e proporção com os custos do Poder de Polícia
       |    exercido pelos órgãos ambientais e fazendários do Estado.
       v
+------------------------------------------------------------------------------------+
| Cobrança Mensal: Valor em UPF-PA por tonelada métrica de minério extraído/lavrado  |
| Contribuintes: Mineradoras atuantes no território paraense (Vale, Hydro, MRN, etc) |
+------------------------------------------------------------------------------------+
```

1. **A Criação da TFRM:** Diante da desoneração do ICMS sobre as exportações de minério imposta pela Lei Kandir, o Estado do Pará instituiu a **TFRM** pela Lei Estadual nº 7.591/2011, calculada sobre a tonelada métrica de minério extraído e destinada a custear a fiscalização ambiental e tributária da atividade de lavra.
2. **O Julgamento Histórico do STF (ADI 4785):** A Confederação Nacional da Indústria (CNI) ajuizou a ADI 4785 questionando a base de cálculo (tonelada extraída) e alegando caráter de tributação disfarçada sobre as exportações. O STF declarou a **constitucionalidade da TFRM do Pará**, firmando entendimento de que os Estados detêm competência material concorrente para fiscalizar a exploração mineral e que a tonelagem é critério idôneo para dimensionar a magnitude do impacto fiscalizatório.

### 5.3. Incentivos à Verticalização Mineral (Lei Estadual nº 6.489/2002)

- Para combater o modelo estritamente primário-exportador, o Pará instituiu a **Política de Incentivos ao Desenvolvimento Socioeconômico (Lei nº 6.489/2002)**, concedendo **crédito presumido de até 85% do saldo devedor do ICMS** para empresas que instalem plantas de verticalização siderúrgica, laminação de aço, refino de cobre e produção de semiacabados de alumínio no Estado.

### 5.4. Regimes de Drawback e Zonas Portuárias

- O Porto de Vila do Conde (Barcarena) e os terminais fluviais de Santarém e Miritituba operam com suspensão e isenção do ICMS nos regimes aduaneiros de Drawback Suspensão e Isenção (Convênio ICMS nº 27/1990) na importação de insumos utilizados na fabricação de bens acabados para o exterior.

---

## 6. Setor de Produto Acabado: Atacado, Varejo, Centrais de Distribuição e E-Commerce

### 6.1. Regime Especial Tributário para o Comércio Atacadista (RICMS/PA)

- O comércio atacadista no Pará usufrui de **Regime Especial de Tributação (RET Atacadista)**, mediante Termo de Acordo celebrado com a SEFA/PA:
  - Nas vendas internas destinadas a contribuintes varejistas, aplica-se crédito presumido ou redução de base de cálculo, equalizando a carga tributária em patamares que desestimulam a aquisição predatória junto a atacadistas de outros Estados;
  - Exige-se contrapartida de geração de empregos formais, investimentos em instalações físicas e depósito de mercadorias no território paraense.

### 6.2. Margens de Valor Agregado (MVA / IVA-ST) e Malhas Fiscais

- A SEFA/PA atua de modo intensivo no monitoramento das MVAs originais e ajustadas fixadas pelos Convênios e Protocolos do CONFAZ para setores alimentícios, materiais de construção, autopeças e eletrodomésticos.
- O Fisco Paraense implementou o sistema **Malha Fiscal Eletrônica**, que cruza o arquivo da EFD com a ECF e extratos bancários, emitindo autos de infração automáticos caso a margem declarada e o imposto antecipado fiquem abaixo dos índices setoriais mínimos.

### 6.3. E-Commerce e Responsabilidade dos Intermediadores Digitais

- Na linha da legislação federal complementar, a legislação do Pará imputa responsabilidade solidária aos operadores de plataformas eletrônicas (*marketplaces*), centros de triagem postal e empresas de transporte fracionado pelo imposto e penalidades devidas na hipótese de comercialização ou entrega de mercadorias desacompanhadas de documentação fiscal idônea destinadas a consumidores finais paraenses.

---

## 7. Transição para o IBS / CBS da Reforma Tributária (EC nº 132/2023 e LC nº 214/2025)

```
                       IMPACTOS DA REFORMA TRIBUTÁRIA NO ESTADO DO PARÁ
+---------------------------------------------------------------------------------------------------------+
| EC nº 132/2023: TRANSIÇÃO DO PRINCÍPIO DA ORIGEM PARA O PRINCÍPIO DO DESTINO                            |
+---------------------------------------------------------------------------------------------------------+
       |                                      |                                    |
       v                                      v                                    v
+-------------------------------+  +-------------------------------+  +-------------------------------+
| Ganho Estrutural de Receita   |  | Homologação de Saldo Credor   |  | Art. 20 da EC nº 132/2023     |
| Pará possui grande população  |  | Acumulado da Lei Kandir:      |  | Instituição de contribuição   |
| consumidora (8,5 mi hab) e    |  | Bilhões em créditos de ICMS   |  | estadual sobre produtos       |
| sua produção mineral/agrícola |  | da mineração a serem auditados|  | primários e semielaborados    |
| já era desonerada na origem.  |  | para amortização em 240 meses.|  | para obras e infraestrutura.  |
+-------------------------------+  +-------------------------------+  +-------------------------------+
```

### 7.1. O Pará como Grande Beneficiário do Princípio do Destino

- A arrecadação tributária sob a égide do ICMS sempre penalizou o Estado do Pará: sua imensa riqueza mineral (dezenas de bilhões de dólares anuais de minério exportado) é completamente imune ao ICMS por força da Lei Kandir (art. 155, § 2º, X, "a" da CF), ao passo que os bens de consumo e industriais consumidos por seus mais de 8,5 milhões de habitantes eram tributados no polo de origem fabril (SP, RJ, MG, PR, RS) pela alíquota interestadual de 7%.
- Com a migração progressiva (2029 a 2032) para o **Imposto sobre Bens e Serviços (IBS)** e incidência exclusiva no **local de destino do consumo**, o Pará experimentará um incremento substancial de sua fatia distributiva de receitas tributárias nacionais.

### 7.2. Homologação do Saldo Credor Acumulado de ICMS (Art. 134 do ADCT / LC nº 214/2025)

- **O Mega Passivo Creditório Paraense:** Grandes mineradoras globais e tradings de grãos sediadas no Pará detêm montantes multibilionários de saldos credores legítimos de ICMS acumulados em suas contas correntes fiscais em virtude da manutenção de créditos de exportação da Lei Kandir.
- **Rito de Amortização em 240 Parcelas:**
  1. Conforme estabelecido pelo art. 134 do ADCT, as empresas deverão submeter a totalidade de seus créditos à **auditoria e homologação pela SEFA/PA**;
  2. Os créditos homologados serão amortizados em **240 (duzentas e quarenta) parcelas mensais**, atualizadas monetariamente pelo IPCA, para compensação com o IBS a recolher;
  3. Na hipótese de ausência de débito suficiente de IBS para absorver as parcelas mensais, o **Comitê Gestor do IBS** efetuará o ressarcimento financeiro direto do saldo remanescente.

### 7.3. Fundo de Compensação de Benefícios Fiscais (FCBF) e Artigo 20 da EC nº 132/2023

1. **Compensação dos Benefícios Convalidados:** As indústrias incentivadas pela Lei nº 6.489/2002 e pelos regimes de atração fabril do Pará receberão recursos compensatórios do FCBF federal entre 2029 e 2032, minimizando o impacto da perda progressiva dos incentivos de ICMS.
2. **Contribuição sobre Produtos Primários e Semielaborados (Art. 20 da EC 132/2023):** O Pará poderá manter ou disciplinar contribuição incidente sobre produtos primários e semielaborados extraídos no Estado com destinação a investimentos em infraestrutura e habitação, vinculada às balizas do art. 20 da Emenda Constitucional até 31 de dezembro de 2043.

---

## 8. Plano de Ação e Recomendações Normativas para o Repositório

Com base na auditoria efetuada, recomenda-se a execução das seguintes medidas estruturais no acervo do Estado do Pará:

1. **Digitalização e Inserção da Lei nº 7.591/2011 (TFRM):** Criar pasta `estaduais/pa/tfrm/` com o texto consolidado da Lei da Taxa Mineral e decretos de regulamentação de alíquotas por tonelada métrica.
2. **Incorporação da Lei Estadual nº 9.755/2022:** Atualizar a legislação do ICMS paraense para refletir documentalmente a vigência da alíquota modal interna de 19%.
3. **Mapeamento da Lei de Incentivos Socioeconômicos (Lei nº 6.489/2002):** Incluir o regulamento de concessão de créditos presumidos para indústrias de verticalização mineral e agropecuária.
4. **Acervo do Processo Administrativo Tributário (Lei Estadual nº 6.182/1998):** Incorporar o regulamento do contencioso fiscal e rito perante o Tribunal Administrativo de Recursos Tributários (TART/PA).
