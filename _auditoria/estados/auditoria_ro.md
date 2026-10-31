# Relatório de Auditoria Tributária Estadual: Rondônia (RO)
**Unidade Federativa:** Rondônia | **Sigla:** RO | **Região:** Norte  
**Órgão Fazendário:** Secretaria de Estado de Finanças de Rondônia (SEFIN/RO)  
**Data da Auditoria:** Outubro de 2026 | **Status:** Atualizado com a EC nº 132/2023 e LC nº 214/2025  

---

## 1. Mapeamento das Normas no Repositório e Diagnóstico de Lacunas

### 1.1. Acervo Documental Existente no Repositório (`estaduais/ro/`)

O repositório apresenta os seguintes arquivos cadastrados no âmbito de Rondônia:

1. [`estaduais/ro/ricms/decreto-22721-2018.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/ro/ricms/decreto-22721-2018.md): Estrutura sintética do Regulamento do ICMS do Estado de Rondônia (RICMS/RO), aprovado pelo Decreto nº 22.721, de 05 de abril de 2018.
2. [`estaduais/ro/leis/itcmd/lei-959-2000.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/ro/leis/itcmd/lei-959-2000.md): Disciplina normativa do Imposto sobre Transmissão Causa Mortis e Doação (ITCMD), instituído pela Lei Estadual nº 959, de 28 de dezembro de 2000.
3. [`estaduais/ro/leis/ipva/lei-950-2000.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/ro/leis/ipva/lei-950-2000.md): Disposições jurídicas do Imposto sobre a Propriedade de Veículos Automotores (IPVA), fundadas na Lei Estadual nº 950, de 22 de dezembro de 2000.

### 1.2. Inventário de Normas Fundamentais Ausentes (Lacunas Críticas)

Para propiciar respaldo técnico e analítico integral, o repositório requer a inclusão prioritária dos seguintes diplomas:

| Diploma Legal Faltante | Ementa / Objeto Jurídico | Prioridade | Impacto Técnico no Repositório |
| :--- | :--- | :---: | :--- |
| **Lei Estadual nº 688/1996 (Texto Consolidado)** | Lei Orgânica do ICMS de Rondônia — Regulação de fatos geradores, bases de cálculo, alíquotas, sujeição passiva e penalidades. | **Crítica** | Marco da estrita legalidade tributária do imposto estadual. |
| **Lei Estadual nº 5.629/2023** | Elevação da alíquota modal interna do ICMS de 17,5% para 19,5% (em vigor desde 12 de janeiro de 2024). | **Crítica** | Base compulsória para apuração do DIFAL e operações internas. |
| **Lei Complementar nº 842/2015 (FECOEP/RO)** | Institui o Fundo Estadual de Combate e Erradicação da Pobreza de Rondônia (adicional de até 2% sobre mercadorias supérfluas). | **Alta** | Cálculo exato da carga incidente em bebidas alcoólicas e fumo. |
| **Lei Complementar nº 61/1992 e Lei nº 1.558/2005 (CONDER / PIDISE)** | Programa de Incentivo ao Desenvolvimento Industrial e Social do Estado de Rondônia — Crédito presumido industrial de até 85%. | **Crítica** | Modelo de atração de frigoríficos, agroindústrias e laticínios. |
| **Lei Federal nº 8.256/1991 e Dec. nº 616/1992** | Criação e regulamento da Área de Livre Comércio de Guajará-Mirim (ALCGM). | **Alta** | Regime tributário e aduaneiro de fronteira com a Bolívia. |
| **Lei Estadual nº 1.488/2005 e Dec. nº 11.908/2005** | Regulação do Processo Administrativo Tributário (PAT/RO) e Tribunal Administrativo de Tributos Estaduais (TATE/RO). | **Alta** | Rito contencioso administrativo, impugnações e recursos fiscais. |
| **Lei Estadual nº 1.473/2005 e Lei nº 4.210/2017** | Benefícios para Comércio Importador e Atacadista em Rondônia. | **Média** | Regimes especiais para atacadistas e centros de distribuição. |

---

## 2. Relacionamento Interestadual com as 26 UFs e Distrito Federal

```
                                      +------------------------------------+
                                      |     ESTADO DE RONDÔNIA (RO)        |
                                      +------------------------------------+
                                       /          |                \
         Saídas Interestaduais (12%)  |          |Entradas Sul/SE |Importados >40%: 4%
         Mercadorias Nacionais        |          |Origem: 7%      |(Resolução SF 13/12)
                                      v          v                v
                        +--------------------+  +---------------+  +---------------------+
                        | Demais 26 UFs e DF |  | Base Dupla no |  | Todas as UFs Destino|
                        | (Sul, SE, Centro,  |  | Destino (RO): |  +---------------------+
                        | Norte e Nordeste)  |  | DIFAL=19,5%-7%|
                        +--------------------+  +---------------+
```

### 2.1. Matriz de Alíquotas Interestaduais (Resoluções SF nº 22/1989 e 13/2012)

- **Saídas interestaduais promovidas de Rondônia:** Por estar situado na Região Norte, as saídas de mercadorias nacionais com destino a **qualquer Estado brasileiro** (inclusive São Paulo, Rio de Janeiro, Minas Gerais e Região Sul) são tributadas à alíquota interestadual de **12%** (Resolução SF nº 22/1989).
- **Entradas interestaduais em Rondônia:**
  - Procedentes das Regiões **Sul e Sudeste (exceto Espírito Santo):** Alíquota interestadual na origem de **7%**.
  - Procedentes das Regiões **Norte, Nordeste, Centro-Oeste e Espírito Santo:** Alíquota interestadual na origem de **12%**.
- **Produtos Importados do Exterior (Resolução SF nº 13/2012):**
  - Alíquota uniforme de **4%** em operações interestaduais com bens importados sem industrialização ou com Conteúdo de Importação superior a 40% apurado na FCI.
- **Transporte Aéreo Interestadual:** Alíquota uniforme de **4%** (Resolução SF nº 95/1996).

### 2.2. A Área de Livre Comércio de Guajará-Mirim (ALCGM)

- Criada pela Lei Federal nº 8.256/1991 e vinculada à SUFRAMA, a ALCGM goza do benefício do **Convênio ICMS nº 52/1992**:
  - As remessas de produtos industrializados de origem nacional destinados ao consumo e comercialização na ALCGM são desoneradas do ICMS na origem, devendo o valor correspondente ao benefício ser expressamente abatido do preço da mercadoria destacado na nota fiscal.
  - O controle de ingresso de mercadorias é operado conjuntamente entre a SEFIN/RO, a Receita Federal do Brasil e a SUFRAMA.

### 2.3. Diferencial de Alíquotas (DIFAL) nas Entradas em Território Rondoniense

#### 1. DIFAL Contribuinte (Uso, Consumo e Ativo Permanente — Base Dupla)
O Estado de Rondônia adota expressamente a sistemática de **Base Dupla (Cálculo por Dentro)**, regulada no Art. 18 da Lei Estadual nº 688/1996 (com as modificações da Lei Estadual nº 5.298/2022) e no art. 42 do RICMS/RO:
1. Apuração da base de cálculo sem o ICMS da operação de origem:
   $$V_{\text{sem ICMS}} = V_{\text{operação}} \times (1 - \text{ALQ}_{\text{inter}})$$
2. Inclusão da alíquota interna de Rondônia (19,5%):
   $$BC_{\text{destino (RO)}} = \frac{V_{\text{sem ICMS}}}{1 - 0{,}195}$$
3. Cálculo do DIFAL a recolher à SEFIN/RO:
   $$\text{DIFAL}_{\text{RO}} = (BC_{\text{destino}} \times 0{,}195) - (V_{\text{operação}} \times \text{ALQ}_{\text{inter}})$$

#### 2. DIFAL Não Contribuinte (EC nº 87/2015, LC nº 190/2021 e Convênio ICMS nº 236/2021)
- Nas remessas para consumidores finais não contribuintes em Rondônia, o remetente de outra UF apura o DIFAL por base única, aplicando a alíquota interna rondoniense de **19,5%** deduzida da alíquota interestadual (4%, 7% ou 12%).
- Nas operações com mercadorias supérfluas sujeitas ao FECOEP/RO (Lei Complementar nº 842/2015), incide o adicional de até 2% recolhido em DAE específico.

### 2.4. Transferências Interestaduais entre Filiais (ADC 49 STF e Convênio ICMS 109/2024)

- **Regra Geral:** Em consonância com a ADC 49 e a LC nº 204/2023, as remessas entre matriz e filiais são isentas de fato gerador de ICMS.
- **Transferência do Crédito e Opção no RUDFTO:** O Convênio ICMS nº 109/2024 estabelece a faculdade (Cláusula Sexta) de o contribuinte rondoniense optar pela equiparação à operação regularmente tributada mediante lavratura de termo no RUDFTO. Essa opção é amplamente adotada pelas redes de frigoríficos e tradings rondonienses para evitar perdas ou entraves na transferência de créditos presumidos aos centros de comercialização situados em São Paulo e Paraná.

### 2.5. Substituição Tributária (ICMS-ST) e Antecipação sem Encerramento (Anexo VII do RICMS/RO)

- **MVA Ajustada nas Operações Interestaduais:**
  $$\text{MVA Ajustada} = \left[ \frac{(1 + \text{MVA-ST Original}) \times (1 - \text{ALQ Inter})}{(1 - 0{,}195)} \right] - 1$$
- **Antecipação do Imposto sem Encerramento de Fase:** Mecanismo central da política arrecadatória da SEFIN/RO (Anexo VII do RICMS/RO), incidente na entrada de mercadorias no território estadual procedentes de outras UFs desprovidas de acordo interestadual de substituição tributária, calculada pela margem de valor agregado e cobrada no desembaraço do sistema **Fisconforme**.

---

## 3. Mecanismos de Dedução e Crédito do ICMS

### 3.1. Princípio da Não-Cumulatividade e Direito de Crédito

- Compensação do tributo devido com o montante anteriormente cobrado nas operações com mercadorias e serviços recebidos, respeitando as normas de estorno obrigatório quando a saída for isenta ou não tributada (art. 155, § 2º, I da CF c/c LC nº 87/1996 e Lei Estadual nº 688/1996).
- **Manutenção de Créditos nas Exportações:** As saídas destinadas ao mercado externo (soja em grão, milho, carne bovina congelada e café verde) operam sob imunidade constitucional ampla (art. 155, § 2º, X, "a" da CF/88), assegurado o direito à apropriação e manutenção dos créditos decorrentes da aquisição de combustíveis, embalagens, medicamentos veterinários e insumos industriais.

### 3.2. Controle de Crédito do Ativo Permanente (CIAP — LC nº 102/2000)

- O crédito de ICMS na aquisição de bens do ativo imobilizado é escriturado no Livro CIAP (Bloco G da EFD) e fracionado em **48 parcelas mensais (1/48 avos)**:
  $$\text{Crédito Mensal} = \left(\frac{\text{ICMS do Bem}}{48}\right) \times \left(\frac{\text{Saídas Tributadas} + \text{Exportações}}{\text{Total das Saídas}}\right)$$
- Nas instalações fabris de agroindústrias beneficiadas pelo CONDER/PIDISE, há previsão de diferimento ou dispensa do DIFAL na entrada de máquinas industriais novas destinadas à linha de produção, otimizando o fluxo de caixa do investimento.

### 3.3. Restrições sobre Energia Elétrica e Telecomunicações (LC nº 87/96 e LC nº 194/22)

- **Energia Elétrica (Art. 33, II da LC nº 87/1996):** Admitida a tomada de crédito apenas pela indústria de transformação (frigoríficos, laticínios, torrefações e usinas de beneficiamento), condicionada à apresentação de laudo pericial que isole o consumo dos motores industriais e câmaras frigoríficas do consumo administrativo geral.
- **Telecomunicações (Art. 33, IV da LC nº 87/1996):** Crédito integralmente vedado a estabelecimentos industriais e comerciais em geral.
- **Efeitos da LC nº 194/2022:** A alíquota de ICMS sobre energia elétrica e comunicações no Estado de Rondônia foi rebaixada ao patamar modal (atualmente 19,5%), extinguindo as alíquotas históricas que alcançavam até 27%.

---

## 4. Setor Agrícola, Rural e Pecuária de Alta Tecnologia

```
                     CADEIA AGROPECUÁRIA E FRIGORÍFICA EM RONDÔNIA
+--------------------------+                         +-------------------------------+
| Produtor Rural RO        |                         | Complexo Frigorífico /        |
| (Gado de Corte, Leite,   |                         | Agroindústria / Exportadoras  |
| Café Clonal e Cacau)     |                         | (JBS, Marfrig, Minerva)       |
+--------------------------+                         +-------------------------------+
             |                                                       |
             | Saída Interna com DIFERIMENTO DO ICMS                 | Abate e Desossa com
             | (Decreto nº 22.721/2018)                              | Crédito Outorgado CONDER/PIDISE
             +------------------------------------------------------>|
                                                                     |
                                             +-----------------------+-----------------------+
                                             |                                               |
                                             v                                               v
                             +-------------------------------+               +-------------------------------+
                             | Exportação Global via         |               | Mercado Nacional Interestadual|
                             | Hidrovia Madeira / Portos     |               | Saída Tributada a 12%         |
                             | Imunidade + Manutenção Crédito|               +-------------------------------+
                             +-------------------------------+
```

### 4.1. Perfil Econômico-Produtivo de Rondônia

O Estado de Rondônia destaca-se no cenário nacional pelo vigor de suas cadeias agropecuárias:
1. **Pecuária Bovina de Corte e Leiteira:** Rebanho bovino superior a 15 milhões de cabeças, reconhecido internacionalmente pela Organização Mundial de Saúde Animal (OMSA) como **Zona Livre de Febre Aftosa sem Vacinação**. Essa condição sanitária de elite abre os mercados mais exigentes do mundo para a carne rondoniense.
2. **Café Clonal (*Coffea canephora* / Robusta Amazônico):** Rondônia é o segundo maior produtor de café canéfora do Brasil e líder absoluto em produtividade média por hectare, baseada em clonagem de mudas e irrigação tecnificada.
3. **Cacau e Grãos:** Destaque na produção de cacau e expansão das lavouras de soja e milho no Cone Sul de Rondônia (Vilhena, Cerejeiras, Chupinguaia).

### 4.2. Insumos Agropecuários (Convênios ICMS nº 100/1997 e 26/2021)

- Concessão de isenção e redução da base de cálculo em rações animais, sementes selecionadas, vacinas, produtos veterinários e adubos químicos conforme Convênio ICMS nº 100/1997, observando-se a escala de alíquotas interestaduais nas operações com fertilizantes estabelecida pelo Convênio nº 26/2021.

### 4.3. Diferimento do ICMS nas Operações Internas

- **Gado em Pé:** As operações internas de remessa de gado bovino para abate em frigoríficos credenciados ocorrem com **diferimento do ICMS**, transferindo o recolhimento do tributo para a saída dos produtos comestíveis resultantes do abate.
- **Grãos e Café em Coco:** As saídas internas do produtor agropecuário para cooperativas ou armazéns gerais também operam com diferimento do imposto.

### 4.4. Créditos Presumidos e Incentivos ao Produtor Rural

- **Crédito Presumido de Café Clonal e Leite:** Concessão de crédito outorgado de ICMS aos produtores e usinas de laticínio nas aquisições internas de leite fresco e operações com café processado, fomentando a renda no campo e a industrialização local.
- **Subvenções ao Calcário:** O Estado concede desoneração fiscal sobre o transporte e aquisição de calcário dolomítico para correção da acidez do solo da região amazônica.

### 4.5. Nota Fiscal de Produtor Eletrônica (NFP-e) e IDARON

- Emissão de **NFP-e (modelo 55)** obrigatória para operações comerciais agropecuárias, vinculada à emissão simultânea da Guia de Trânsito Animal (GTA) da Agência de Defesa Sanitária Agrosilvopastoril de Rondônia (IDARON).

---

## 5. Setor Industrial e Hidrelétrico: As Usinas do Madeira e a Indústria de Proteína

### 5.1. O Polo Hidrelétrico do Rio Madeira (UHE Santo Antônio e UHE Jirau)

- O Rio Madeira abriga duas das maiores hidrelétricas a fio d'água do planeta:
  - **UHE Santo Antônio:** Potência instalada de 3.568 MW.
  - **UHE Jirau:** Potência instalada de 3.750 MW.
- **O Tratamento Tributário Constitucional da Energia Elétrica (Art. 155, § 2º, X, "b" da CF/88):**
  - O texto constitucional estabelece que o ICMS **não incide sobre operações interestaduais relativas a energia elétrica**. O imposto cabe integralmente ao Estado onde ocorrer o consumo da eletricidade.
  - Consequência: Embora Rondônia gere cerca de 10% da energia hidrelétrica nacional e a exporte via bipolos em corrente contínua (HVDC) para as Regiões Sudeste e Sul, a SEFIN/RO **não arrecada ICMS sobre a energia enviada para fora**, dependendo de royalties, compensações financeiras de recursos hídricos (CFURH) e ISS incidente na prestação de serviços de manutenção local.

### 5.2. Programa de Incentivo Industrial (CONDER e PIDISE — Lei Complementar nº 61/1992)

- O Conselho de Desenvolvimento do Estado de Rondônia (CONDER) gerencia o **PIDISE**, concedendo **Crédito Presumido de até 85% do saldo devedor do ICMS** para:
  - Indústrias frigoríficas de abate e desossa de carne bovina, suína e de aves;
  - Laticínios e usinas de pasteurização de leite;
  - Torrefadoras e solúveis de café clonal;
  - Indústria de processamento de pescado e couro.

### 5.3. Mineração de Estanho e Cassiterita

- Região de Ariquemes e Bom Futuro: Polo de extração de cassiterita (minério de estanho). As operações de exportação gozam de imunidade da Lei Kandir, havendo regulação estadual para controle da comercialização interna de concentrado de estanho.

---

## 6. Setor de Produto Acabado: Comércio Atacadista, Varejo e Logística

### 6.1. Regime Diferenciado para Centrais de Distribuição e Atacadistas (Lei nº 1.473/2005)

- Para neutralizar as assimetrias logísticas do Norte do País e estimular o estabelecimento de entrepostos de distribuição em Porto Velho, Ji-Paraná e Vilhena, a legislação de Rondônia concede:
  - **Crédito presumido nas saídas interestaduais**, resultando em carga tributária líquida competitiva entre **1,5% e 3%**;
  - Diferimento ou suspensão da cobrança da antecipação na entrada de mercadorias destinadas a contribuintes detentores de Termo de Acordo de Regime Especial (TARE).

### 6.2. Logística Fluvial pelo Corredor do Rio Madeira

- O Porto Organizado de Porto Velho constitui a hidrovia estratégica que liga o Noroeste do Brasil e o Mato Grosso ao Oceano Atlântico (via Rio Amazonas em Itacoatiara/AM). O transporte aquaviário de cargas operado por balsas conta com isenções e regimes especiais de ICMS sobre serviços de navegação fluvial interior.

### 6.3. E-Commerce e Plataformas Digitais

- Fiscalização integrada do transporte rodoviário (BR-364) e malha aérea no Aeroporto Governador Jorge Teixeira, com exigência de responsabilidade solidária para transportadoras e intermediadores de venda digital quanto à verificação da idoneidade da NF-e e CT-e.

---

## 7. Transição para o IBS / CBS da Reforma Tributária (EC nº 132/2023 e LC nº 214/2025)

```
                     IMPACTOS DA REFORMA TRIBUTÁRIA NO ESTADO DE RONDÔNIA
+---------------------------------------------------------------------------------------------------------+
| EC nº 132/2023: TRANSIÇÃO COMPLETA DO PRINCÍPIO DA ORIGEM PARA O PRINCÍPIO DO DESTINO                  |
+---------------------------------------------------------------------------------------------------------+
       |                                      |                                    |
       v                                      v                                    v
+-------------------------------+  +-------------------------------+  +-------------------------------+
| Ganho Distributivo de Receita |  | Homologação de Saldo Credor   |  | Fundo de Compensação de       |
| Fim da evasão por compra      |  | dos Frigoríficos e Tradings:  |  | Benefícios Fiscais (FCBF):    |
| interestadual; IBS passa a ser|  | Auditoria rigorosa da SEFIN/RO|  | Compensação aos frigoríficos  |
| arrecadado no consumo local.  |  | para amortização em 240 meses.|  | incentivados pelo CONDER/PIDISE|
+-------------------------------+  +-------------------------------+  +-------------------------------+
```

### 7.1. Migração para o Princípio do Destino e Benefícios Fiscais Locais

- **Ganho Estrutural:** Sendo Rondônia um Estado eminentemente exportador agropecuário (portanto já desonerado na origem pela Lei Kandir) e importador de bens de consumo acabados das fábricas do Sudeste, a migração definitiva para o **princípio do destino** no IBS garantirá que a arrecadação incidente sobre o consumo da sociedade rondoniense fique no próprio Estado.
- **Fim da Guerra Fiscal (2029-2032):** Os incentivos do CONDER/PIDISE serão progressivamente reduzidos a partir de 2029 na proporção de 10% ao ano, sendo extintos em 2033 juntamente com o ICMS.

### 7.2. Fundo de Compensação de Benefícios Fiscais (FCBF)

- As agroindústrias e frigoríficos rondonienses que possuem incentivos regularmente convalidados perante a Lei Complementar nº 160/2017 e Convênio ICMS nº 190/2017 terão direito à habilitação perante o **Fundo de Compensação de Benefícios Fiscais (FCBF)** da União, mitigando a elevação do custo tributário durante o período de transição (2029 a 2032).

### 7.3. Homologação do Saldo Credor Acumulado de ICMS (Art. 134 do ADCT / LC nº 214/2025)

- **O Passivo Creditório dos Exportadores:** Cooperativas agropecuárias, frigoríficos e exportadores de grãos detêm substanciais estoques de créditos de ICMS acumulados.
- **Regras de Homologação pela SEFIN/RO:**
  1. O contribuinte deverá formular requerimento detalhado no sistema eletrônico da SEFIN/RO até a data limite fixada pela lei complementar;
  2. O Fisco Rondoniense procederá à auditoria fiscal das operações de aquisição de insumos e saídas imunes para validação da certeza e liquidez dos créditos;
  3. Uma vez chancelado pelo Fisco, o crédito será pago/compensado em **240 (duzentas e quarenta) parcelas mensais** corrigidas pelo IPCA, deduzíveis do IBS devido ou ressarcidas financeiramente pelo Comitê Gestor do IBS.

---

## 8. Plano de Ação e Recomendações Normativas para o Repositório

Com vistas ao enriquecimento do acervo documental de Rondônia, formulam-se as seguintes diretrizes:

1. **Inserção da Lei Estadual nº 5.629/2023:** Atualizar formalmente o acervo normativo para registrar a alteração da alíquota modal do ICMS para 19,5%.
2. **Criação da Pasta do Processo Administrativo Fiscal (`estaduais/ro/pat/`):** Incorporar a Lei nº 1.488/2005 e o Decreto nº 11.908/2005, detalhando as regras recursais perante o Tribunal Administrativo de Tributos Estaduais (TATE/RO).
3. **Mapeamento Normativo do CONDER/PIDISE:** Incluir a Lei Complementar nº 61/1992 e o Decreto nº 12.988/2007 para disponibilizar as regras de apuração do crédito presumido agroindustrial.
4. **Disciplina Normativa da ALC de Guajará-Mirim:** Codificar os parâmetros de internação, selagem eletrônica e fruição da isenção do Convênio ICMS 52/1992.
