# Relatório de Auditoria Tributária Estadual: Tocantins (TO)
**Unidade Federativa:** Tocantins | **Sigla:** TO | **Região:** Norte  
**Órgão Fazendário:** Secretaria da Fazenda do Estado do Tocantins (SEFAZ/TO)  
**Data da Auditoria:** Outubro de 2026 | **Status:** Atualizado com a EC nº 132/2023 e LC nº 214/2025  

---

## 1. Mapeamento das Normas no Repositório e Diagnóstico de Lacunas

### 1.1. Acervo Documental Existente no Repositório (`estaduais/to/`)

O repositório apresenta as seguintes normas no âmbito do Estado do Tocantins:

1. [`estaduais/to/ricms/decreto-2912-2006.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/to/ricms/decreto-2912-2006.md): Estrutura sintética do Regulamento do ICMS do Tocantins (RICMS/TO), aprovado pelo Decreto Estadual nº 2.912, de 29 de dezembro de 2006.
2. [`estaduais/to/ricms/lei-1201-2000-atacadista-ecommerce-to.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/to/ricms/lei-1201-2000-atacadista-ecommerce-to.md): Regime jurídico da Lei Estadual nº 1.201/2000 (Comércio Atacadista e E-Commerce) e referências estruturais à Lei nº 1.385/2003 (PROSPERAR / PROINDÚSTRIA).
3. [`estaduais/to/leis/itcmd/lei-1287-2001.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/to/leis/itcmd/lei-1287-2001.md): Disposições normativas do Imposto sobre Transmissão Causa Mortis e Doação (ITCMD), integradas ao Código Tributário Estadual (Lei nº 1.287/2001).
4. [`estaduais/to/leis/ipva/lei-1287-2001.md`](file:///Users/brunoqualhato/Documents/meus/tributos/estaduais/to/leis/ipva/lei-1287-2001.md): Regime legal do Imposto sobre a Propriedade de Veículos Automotores (IPVA), contido na Lei nº 1.287/2001.

### 1.2. Inventário de Normas Fundamentais Ausentes (Lacunas Críticas)

Para atingir consistência jurídica e profundidade de análise plenas, faz-se necessária a incorporação dos seguintes diplomas:

| Diploma Legal Faltante | Ementa / Objeto Jurídico | Prioridade | Impacto Técnico no Repositório |
| :--- | :--- | :---: | :--- |
| **Lei Estadual nº 1.287/2001 (Texto Consolidado do ICMS)** | Código Tributário do Estado do Tocantins (CTE/TO) — Fatos geradores, base de cálculo, alíquotas, sujeição passiva, responsabilidade e multas. | **Crítica** | Matriz constitucional e legal primária do ICMS tocantinense. |
| **Lei Estadual nº 4.141/2023 (Conversão MP nº 33/2022)** | Elevação da alíquota modal interna de ICMS de 18% para 20% (em vigor desde 01/04/2023). | **Crítica** | Base legal obrigatória para o cálculo do DIFAL e operações internas. |
| **Lei Estadual nº 3.015/2015 (FECOEP/TO)** | Fundo Estadual de Combate e Erradicação da Pobreza (adicional de até 2% sobre bens e serviços supérfluos). | **Alta** | Apuração de tributação sobre bebidas alcoólicas, fumo e cosméticos. |
| **Lei Estadual nº 1.385/2003 (Texto Integral do PROINDÚSTRIA)** | Programa de Industrialização Direcionada — Concessão de créditos presumidos de até 75% e diferimento para o ativo imobilizado fabril. | **Crítica** | Análise de atração de esmagadoras de soja, frigoríficos e indústrias. |
| **Lei Estadual nº 1.746/2006 (FDE-TO)** | Institui o Fundo de Desenvolvimento Econômico do Tocantins (contrapartida de 0,3% sobre faturamento incentivado). | **Alta** | Requisito indispensável de validade da Lei 1.201/2000 e do PROINDÚSTRIA. |
| **Lei Estadual nº 1.288/2001 e Dec. nº 7.000/2024** | Lei do Contencioso Administrativo Tributário (CAT/TO) e Conselho de Contribuintes e Recursos Fiscais (CCRF/TO). | **Alta** | Procedimento de impugnação fiscal, defesas e recursos administrativos. |
| **Lei Estadual nº 1.695/2006** | Regime Tributário de Atração do Comércio Importador e Portos Secos no Tocantins. | **Média** | Tributação do comércio exterior por recintos alfandegados. |

---

## 2. Relacionamento Interestadual com as 26 UFs e Distrito Federal

```
                                      +------------------------------------+
                                      |     ESTADO DO TOCANTINS (TO)       |
                                      +------------------------------------+
                                       /          |                \
         Saídas Interestaduais (12%)  |          |Entradas Sul/SE |Importados >40%: 4%
         Mercadorias Nacionais        |          |Origem: 7%      |(Resolução SF 13/12)
                                      v          v                v
                        +--------------------+  +---------------+  +---------------------+
                        | Demais 26 UFs e DF |  | Base Dupla no |  | Todas as UFs Destino|
                        | (Sul, SE, Centro,  |  | Destino (TO): |  +---------------------+
                        | Norte e Nordeste)  |  | DIFAL = 20%-7%|
                        +--------------------+  +---------------+
```

### 2.1. Matriz de Alíquotas Interestaduais (Resoluções SF nº 22/1989 e 13/2012)

- **Posição Geopolítica Privilegiada:** Integrando a Região Norte, o Tocantins faz divisa direta com as Regiões Centro-Oeste (GO, MT), Nordeste (MA, PI, BA) e Norte (PA).
- **Saídas Interestaduais promovidas do Tocantins:** Submetem-se à alíquota de **12%** para **todas as 26 UFs e Distrito Federal** (Resolução SF nº 22/1989), independentemente de o destino ser um Estado vizinho do Norte/Nordeste ou os mercados de SP, RJ, MG, PR, SC e RS.
- **Entradas Interestaduais no Tocantins:**
  - Procedentes do **Sul e Sudeste (exceto Espírito Santo):** Alíquota interestadual na origem de **7%**.
  - Procedentes do **Norte, Nordeste, Centro-Oeste e Espírito Santo:** Alíquota interestadual na origem de **12%**.
- **Produtos Importados do Exterior (Resolução SF nº 13/2012):** Alíquota unificada de **4%** nas saídas interestaduais de bens importados ou com Conteúdo de Importação superior a 40%.
- **Transporte Aéreo Interestadual:** Alíquota uniforme de **4%** (Resolução SF nº 95/1996).

### 2.2. A Assimetria Tributária Estrutural Positiva do Tocantins

```
                      ARBITRAGEM TRIBUTÁRIA DO ATACADO TOCANTINENSE
    +------------------------+                         +-------------------------------+
    | Indústria em SP/MG/RS  |                         | Central de Distribuição em TO |
    | (Sul / Sudeste)        |                         | (Lei nº 1.201/2000 - TARE)    |
    +------------------------+                         +-------------------------------+
                |                                                      |
                | Compra à Alíquota de 7%                              | Venda Interestadual B2B
                | (Entrada interestadual)                              | com destaque regular de 12%
                +----------------------------------------------------->|
                                                                       | Carga Efetiva em TO: 1% a 2%
                                                                       | (Crédito Presumido Convalidado)
                                                                       |
                                                                       v
                                                       +-------------------------------+
                                                       | Comprador Contribuinte em     |
                                                       | SP, RJ, BA, GO, DF, MA        |
                                                       | (Apropria CRÉDITO DE 12%)     |
                                                       +-------------------------------+
```

O Tocantins opera como um dos maiores entrepostos distribuidores do Brasil graças à conjunção de dois fatores:
1. **Regra Federativa da Resolução SF 22/1989:** O Tocantins adquire mercadorias de fábricas de SP, RJ e Sul com destaque de **7%** de ICMS na origem, mas promove a revenda interestadual com destaque de **12%** de ICMS.
2. **Incentivo da Lei nº 1.201/2000:** A legislação tocantinense outorga um crédito presumido na saída interestadual que reduz o imposto devido ao Fisco de TO para apenas **1,0% a 2,0%** sobre o valor da operação, enquanto o comprador em qualquer Estado do Brasil apropria o **crédito integral de 12%** destacado no documento fiscal (blindado pela Lei Complementar nº 160/2017 e Convênio ICMS 190/2017).

### 2.3. Diferencial de Alíquotas (DIFAL) nas Entradas em Território Tocantinense

#### 1. DIFAL Contribuinte (Uso, Consumo e Ativo Permanente — Base Dupla)
O Tocantins aplica a metodologia de **Base Dupla (Cálculo por Dentro)**, regulada no Art. 22 da Lei Estadual nº 1.287/2001 (com as alterações da Lei nº 3.890/2022) e disciplinada no RICMS/TO:
1. Dedução do ICMS da operação de origem:
   $$V_{\text{sem ICMS}} = V_{\text{operação}} \times (1 - \text{ALQ}_{\text{inter}})$$
2. Recomposição pela alíquota interna tocantinense (20%):
   $$BC_{\text{destino (TO)}} = \frac{V_{\text{sem ICMS}}}{1 - 0{,}20}$$
3. Montante do DIFAL devido à SEFAZ/TO:
   $$\text{DIFAL}_{\text{TO}} = (BC_{\text{destino}} \times 0{,}20) - (V_{\text{operação}} \times \text{ALQ}_{\text{inter}})$$

#### 2. DIFAL Não Contribuinte (EC nº 87/2015, LC nº 190/2021 e Convênio ICMS nº 236/2021)
- Nas aquisições de consumidores finais não contribuintes estabelecidos no Tocantins, o remetente de outra UF apura o DIFAL por base única pela diferença entre 20% (+ até 2% FECOEP quando bem supérfluo) e a alíquota interestadual de origem (4%, 7% ou 12%).
- **Vantagem Competitiva dos E-Commerces sediados no Tocantins:** Na venda não presencial interestadual B2C saindo do Tocantins para consumidores de outros Estados, o DIFAL a recolher ao Estado de destino é apurado deduzindo-se a alíquota cheia de **12%** ($Alíquota\ Interna_{Destino} - 12\%$), ao passo que o imposto próprio pertencente ao Tocantins é reduzido para **1% a 2%** pela Lei nº 1.641/2005 e Decreto nº 2.912/2006.

### 2.4. Transferências Interestaduais entre Estabelecimentos do Mesmo Titular (ADC 49 STF e Convênio ICMS 109/2024)

- **Não Ocorrência de Fato Gerador:** Em conformidade com a ADC 49 e a LC nº 204/2023, as remessas entre matriz e filiais são desprovidas de incidência de ICMS.
- **Exercício da Opção de Equiparação a Venda Tributada:** Nos termos da Cláusula Sexta do Convênio ICMS nº 109/2024, contribuintes tocantinenses titulares de TARE (atacadistas, tradings de grãos e indústrias) utilizam amplamente a **opção anual no Livro RUDFTO** para equiparar as transferências a operações tributadas, assegurando o destaque de 12% na NF-e e preservando a liquidez e fruição do crédito presumido estadual.

### 2.5. Substituição Tributária (ICMS-ST) e Antecipação (Anexo XXI do RICMS/TO)

- Aplicação dos Protocolos e Convênios do CONFAZ, com apuração de MVA Ajustada nas operações interestaduais:
  $$\text{MVA Ajustada} = \left[ \frac{(1 + \text{MVA-ST Original}) \times (1 - \text{ALQ Inter})}{(1 - 0{,}20)} \right] - 1$$
- **Complementação de Alíquota:** Exigência de antecipação tributária nas entradas interestaduais de mercadorias destinadas à revenda quando adquiridas por contribuintes enquadrados no Simples Nacional.

---

## 3. Mecanismos de Dedução e Crédito do ICMS

### 3.1. Princípio da Não-Cumulatividade e Dinâmica Creditória

- O imposto é não-cumulativo, operando-se a compensação dos débitos decorrentes de saídas tributadas com os créditos destacados nas entradas de matérias-primas, insumos, produtos intermediários e embalagens (art. 155, § 2º, I da CF c/c LC nº 87/1996 e Lei nº 1.287/2001).
- **Manutenção de Créditos na Exportação (Art. 155, § 2º, X, "a" da CF/88):** Total desoneração das exportações diretas de commodities agrícolas (complexo soja e carne bovina in natura ou congelada), sendo expressamente garantida a manutenção dos créditos fiscais decorrentes das aquisições de insumos.
- **Regime Monofásico de Estorno na Lei nº 1.201/2000:** A opção pelo benefício fiscal de atacadista impõe a renúncia formal e o estorno completo de quaisquer créditos fiscais de ICMS das entradas, operando o crédito presumido como sucedâneo definitivo da apuração convencional.

### 3.2. Controle de Crédito do Ativo Permanente (CIAP — LC nº 102/2000)

- Créditos sobre máquinas, tratores, implementos e equipamentos fabris adquiridos para o ativo imobilizado são escriturados no Bloco G da EFD e apropriados à razão de **1/48 (um quarenta e oito avos) mensal** (art. 37 do RICMS/TO):
  $$\text{Fração Mensal} = \left(\frac{\text{Crédito Integral}}{48}\right) \times \left(\frac{\text{Saídas Tributadas} + \text{Exportações}}{\text{Total das Saídas}}\right)$$
- **Diferimento e Isenção do Ativo no PROINDÚSTRIA (Lei nº 1.385/2003):** Empresas industriais aprovadas no PROSPERAR/PROINDÚSTRIA contam com **isenção ou diferimento total do ICMS** incidente na importação do exterior e do DIFAL interestadual nas aquisições de máquinas industriais para modernização fabril.

### 3.3. Restrições sobre Energia Elétrica e Telecomunicações (LC nº 87/96 e LC nº 194/22)

- **Energia Elétrica (Art. 33, II da LC nº 87/1996):** Direito de crédito franqueado exclusivamente aos estabelecimentos industriais (esmagadoras de soja, fábricas de ração e frigoríficos), exigindo laudo pericial técnico de segregação energética da planta fabril.
- **Telecomunicações (Art. 33, IV da LC nº 87/1996):** Vedação integral de apropriação de crédito para estabelecimentos comerciais e agropecuários gerais.
- **Enquadramento na LC nº 194/2022:** A alíquota incidente sobre energia e comunicações foi adequada ao teto modal de 20%, extinguindo as antigas sobretaxas seletivas estaduais.

---

## 4. Setor Agrícola, Rural e a Potência do MATOPIBA

```
                      CADEIA DO AGRONEGÓCIO TOCANTINENSE (MATOPIBA)
+--------------------------+                         +-------------------------------+
| Produtor Rural do TO     |                         | Grandes Tradings /            |
| (Soja, Milho, Arroz,     |                         | Cooperativas / Esmagadoras    |
| Pecuária de Corte)       |                         | (Bunge, Cargill, Fazendão)    |
+--------------------------+                         +-------------------------------+
             |                                                       |
             | Saída Interna com DIFERIMENTO DO ICMS                 | Industrialização / Esmagamento
             | (Decreto nº 2.912/2006)                               | (Crédito Outorgado PROINDÚSTRIA)
             +------------------------------------------------------>|
                                                                     |
                                             +-----------------------+-----------------------+
                                             |                                               |
                                             v                                               v
                             +-------------------------------+               +-------------------------------+
                             | Exportação pelo Arco Norte:   |               | Mercado Nacional Interestadual|
                             | Pátio Multimodal da FNS       |               | Saída Tributada a 12%         |
                             | Ferrovia Norte-Sul -> Itaqui  |               +-------------------------------+
                             | Imunidade + Manutenção Crédito|
                             +-------------------------------+
```

### 4.1. Perfil Agrícola: O Centro Dinâmico do MATOPIBA

O Tocantins integra o MATOPIBA, a mais pujante fronteira de expansão agrícola sustentável do mundo:
1. **Complexo Soja e Milho:** Destaque nas regiões de Campos Lindos, Pedro Afonso, Porto Nacional, Paraíso do Tocantins, Guaraí e Gurupi, alcançando safras sucessivas de alta produtividade.
2. **Arroz Irrigado Tropical:** O Tocantins é o terceiro maior produtor de arroz do Brasil e líder absoluto em arroz tropical irrigado por inundação na Bacia do Rio Formoso (Formoso do Araguaia e Lagoa da Confusão).
3. **Pecuária de Corte:** Rebanho bovino ultrapassando 9 milhões de cabeças, caracterizado pela terminação em confinamento e integração lavoura-pecuária (ILP).

### 4.2. Insumos Agropecuários (Convênio ICMS nº 100/1997 e Convênio ICMS nº 26/2021)

- Aplicação regular dos benefícios do Convênio ICMS nº 100/1997: isenção e redução da base de cálculo nas operações internas e interestaduais com fertilizantes, sementes certificadas, calcário dolomítico e defensivos agrícolas, com atendimento ao cronograma de reoneração escalonada do Convênio nº 26/2021.

### 4.3. Diferimento do ICMS nas Saídas Internas

- **Grãos do Produtor:** As saídas internas de soja, milho, arroz e feijão promovidas por produtores rurais com destino a cooperativas, indústrias moageiras ou tradings com sede no Estado ocorrem com **diferimento do lançamento do ICMS**.
- O pagamento do tributo fica postergado para o momento da saída interestadual tributada, ou considera-se encerrado sem débito nas remessas com fim específico de exportação desoneradas pela Lei Kandir.
- **Gado em Pé:** As remessas de bovinos entre produtores para recria ou engorda e as remessas para frigoríficos credenciados no território tocantinense são contempladas por diferimento do imposto.

### 4.4. Créditos Presumidos e Incentivos ao Produtor Rural

- Concessão de crédito outorgado de ICMS para cooperativas agropecuárias e agroindústrias locais de aves, suínos e laticínios, estimulando a agregação de valor antes do envio para outros Estados.
- Subvenções tributárias para fomento da correção de solo com calcário extraído nas jazidas tocantinenses de Almas e Xambioá.

### 4.5. Nota Fiscal de Produtor Eletrônica (NFP-e) e ADAPEC

- Obrigatoriedade de emissão de NFP-e (modelo 55) acoplada ao sistema eletrônico da Agência de Defesa Agropecuária do Estado do Tocantins (ADAPEC), condicionando a validação fiscal das cargas animais à correspondente Guia de Trânsito Animal (GTA).

---

## 5. Setor Industrial e Logístico: A Ferrovia Norte-Sul e o Esmagamento de Grãos

### 5.1. A Infraestrutura Logística Multimodal da Ferrovia Norte-Sul (FNS)

- O Tocantins é cortado de norte a sul pelos trilhos da Ferrovia Norte-Sul (Malha Central e Malha Norte), operada pela Rumo e VLI Multimodal.
- **Pátios Multimodais Estratégicos:**
  - **Pátio de Porto Nacional:** Maior centro integrador de grãos do Tocantins, com transbordo imediato para composições férreas rumo ao Porto do Itaqui (São Luís/MA);
  - **Pátio de Palmeirante / Aguiarnópolis:** Polo de escoamento da produção do norte tocantinense e sul do Maranhão;
  - **Pátio de Gurupi:** Centro de escoamento da produção do sul tocantinense e leste de Mato Grosso.

### 5.2. O Polo de Esmagamento e Processamento de Soja

- A presença da ferrovia atraiu gigantes do processamento agroindustrial (Bunge, Cargill, Fazendão Agronegócios), instalando unidades de esmagamento para transformação do grão em óleo degomado de soja e farelo proteico para ração animal (bens intermediários incentivados).

### 5.3. O Programa de Industrialização Direcionada — PROINDÚSTRIA (Lei Estadual nº 1.385/2003)

- Concessão de incentivos fiscais para indústrias habilitadas pelo Conselho de Desenvolvimento Econômico do Estado do Tocantins (CDE-TO):
  1. **Crédito Presumido de até 75%** sobre o saldo devedor mensal do ICMS da atividade industrial;
  2. Alternativamente, fixação de alíquota efetiva líquida de **1,0% a 2,0%** sobre o faturamento de produtos processados nas saídas interestaduais;
  3. **Isenção e Diferimento de ICMS** no desembaraço de máquinas importadas e no DIFAL de bens de capital novos;
  4. **Contrapartida Compulsória ao FDE-TO (Lei nº 1.746/2006):** Recolhimento mensal de **0,3% (três décimos por cento)** incidente sobre o faturamento incentivado para manutenção do Termo de Acordo de Regime Especial (TARE).

### 5.4. Convalidação Conforme a LC nº 160/2017 e Convênio ICMS 190/2017

- A Lei nº 1.385/2003 (PROINDÚSTRIA/PROSPERAR) e seus respectivos TAREs foram regularmente registrados e depositados na Secretaria Executiva do CONFAZ, assegurando vigência e proteção contra glosas creditórias de outros Estados até 31 de dezembro de 2032.

---

## 6. Setor de Produto Acabado: Comércio Atacadista, Centrais de Distribuição e E-Commerce

### 6.1. O Regime Atacadista da Lei Estadual nº 1.201/2000

```
                   SÍNTESE OPERACIONAL DO TARE ATACADISTA (TO)
+------------------------------------------------------------------------------------+
| 1. OPERAÇÕES DE SAÍDA INTERESTADUAL (B2B PARA CONTRIBUINTES DO ICMS):              |
|    - Destaque em Nota Fiscal (NF-e): Alíquota cheia de 12% (Nacional) ou 4% (Imp.) |
|    - Apuração do ICMS com Crédito Presumido: Carga Tributária Efetiva de 1% a 2%   |
|    - Comprador em outra UF: Apropriação de CRÉDITO PLENO DE 12% (ou 4%)            |
|    - Contrapartida: Estorno integral dos créditos de entrada e recolhe 0,3% FDE-TO |
+------------------------------------------------------------------------------------+
| 2. OPERAÇÕES INTERNAS (B2B PARA VAREJISTAS TOCANTINENSES):                         |
|    - Carga tributária reduzida por crédito outorgado com dispensa de antecipação.  |
+------------------------------------------------------------------------------------+
```

A Lei nº 1.201/2000 é o esteio do comércio tocantinense:
- Permitiu a instalação de centenas de Centrais de Distribuição (CDs) de redes atacadistas de medicamentos, autopeças, confecções, materiais elétricos e produtos alimentícios;
- Transforma a vantagem da alíquota de 12% da Região Norte em diferencial econômico para suprir os mercados do Nordeste, Centro-Oeste e Sudeste.

### 6.2. Comércio Eletrônico (*E-Commerce*) e Vendas Não Presenciais (Lei nº 1.641/2005)

- Para operações de comércio eletrônico, internet, telemarketing e plataformas de *marketplace* destinadas a **consumidores finais não contribuintes de outros Estados**:
  - Aplicação de crédito presumido de ICMS de tal magnitude que a **carga tributária na origem tocantinense resulta entre 1,0% e 2,0%**;
  - Como a remessa parte da Região Norte, a parcela de dedução para o cálculo do DIFAL do Estado de destino considera a alíquota de **12%**, conferindo às plataformas logísticas tocantinenses uma estrutura de custo altamente competitiva frente aos centros de distribuição de São Paulo e Minas Gerais.

### 6.3. Fiscalização e Responsabilidade Tributária de Intermediadores

- A legislação do Tocantins impõe responsabilidade solidária por substituição tributária aos operadores de *marketplaces* e plataformas digitais que viabilizarem a intermediação de mercadorias no Tocantins sem comprovação do pagamento do ICMS ou com documentação inidônea.
- Rígido controle de cargas rodoviárias nos postos fiscais de divisa na rodovia Belém-Brasília (BR-153) e na ponte sobre o Rio Tocantins.

---

## 7. Transição para o IBS / CBS da Reforma Tributária (EC nº 132/2023 e LC nº 214/2025)

```
                    DESAFIOS DA REFORMA TRIBUTÁRIA NO ESTADO DO TOCANTINS
+---------------------------------------------------------------------------------------------------------+
| EC nº 132/2023: TRANSIÇÃO PROGRESSIVA DO ICMS (2029-2032) E EXTINÇÃO DA ARBITRAGEM TRIBUTÁRIA DE ORIGEM |
+---------------------------------------------------------------------------------------------------------+
       |                                      |                                    |
       v                                      v                                    v
+-------------------------------+  +-------------------------------+  +-------------------------------+
| Erosão do Modelo Atacadista   |  | Fundo de Compensação de       |  | Homologação de Saldo Credor   |
| A Lei nº 1.201/2000 perde seu |  | Benefícios Fiscais (FCBF):    |  | Acumulado do Agronegócio:     |
| diferencial com o IBS no      |  | Suporte da União para         |  | Esmagadoras e tradings terão  |
| destino; a competição migrará |  | atenuar perdas das empresas   |  | saldos homologados na SEFAZ/TO|
| para a eficiência logística.  |  | incentivadas até 2032.        |  | para uso em 240 meses no IBS. |
+-------------------------------+  +-------------------------------+  +-------------------------------+
```

### 7.1. O Impacto Estrutural da Mudança para o Princípio do Destino

- **A Reconfiguração do Modelo Atacadista da Lei nº 1.201/2000:**
  - O Estado do Tocantins é, sem dúvida, a Unidade da Federação que enfrentará o maior desafio de ajuste de modelo de negócios com a substituição do ICMS pelo IBS.
  - Como o IBS incidirá integralmente no **local de destino do consumo final**, a vantagem artificial do diferencial de alíquota interestadual (comprar a 7%, vender a 12% e pagar 1% a 2% na origem) deixará de existir a partir da transição (2029 a 2032) e extinção total do ICMS em 2033.
  - As centrais de distribuição instaladas no Tocantins precisarão capitalizar sua localização geográfica e a malha rodoferroviária da Ferrovia Norte-Sul para competir por agilidade física e custo operacional de frete, e não mais por assimetria tributária.

### 7.2. Fundo de Compensação de Benefícios Fiscais (FCBF) e Fundo de Desenvolvimento Regional (FDR)

1. **Habilitação no FCBF:** As empresas atacadistas e industriais detentoras de TARE decorrente das Leis nº 1.201/2000 e 1.385/2003 poderão habilitar-se perante o FCBF federal, recebendo subvenções diretas da União durante o período de transição proporcional (2029 a 2032) para equalizar a redução gradual dos benefícios fiscais.
2. **Aporte do Fundo de Desenvolvimento Regional (FDR):** O Tocantins será um dos maiores beneficiários per capita dos recursos do FDR previstos no art. 159-A da Constituição Federal, garantindo verbas orçamentárias expressivas para investimentos em ferrovias vicinais, rodovias de integração do MATOPIBA e portos fluviais.

### 7.3. Homologação do Saldo Credor Acumulado de ICMS (Art. 134 do ADCT / LC nº 214/2025)

- **Auditoria Fazendária SEFAZ/TO:** As grandes plantas industriais de esmagamento de grãos, frigoríficos e exportadoras de commodities agrícolas sediadas no Tocantins acumulam saldos credores de ICMS decorrentes de saídas imunes e investimentos em bens de capital.
- **Amortização em 240 Meses:**
  - Os créditos acumulados até 31 de dezembro de 2032 deverão ser submetidos a processo formal de **homologação perante a SEFAZ/TO**;
  - Após homologação, os créditos serão convertidos e amortizados em **240 parcelas mensais e sucessivas**, corrigidas pelo IPCA, com direito à dedução direta do IBS ou ressarcimento financeiro centralizado pelo Comitê Gestor do IBS.

---

## 8. Plano de Ação e Recomendações Normativas para o Repositório

Com vistas à excelência analítica do repositório normativo do Estado do Tocantins, orienta-se a execução das seguintes ações:

1. **Inserção da Lei Estadual nº 4.141/2023:** Atualizar o acervo normativo para registrar oficialmente a vigência da alíquota modal interna de 20%.
2. **Publicação da Lei nº 1.385/2003 (PROINDÚSTRIA / PROSPERAR):** Criar pasta específica `estaduais/to/incentivos/` para conter a íntegra da legislação de atração industrial tocantinense.
3. **Mapeamento do Fundo FDE-TO (Lei nº 1.746/2006):** Inserir a disciplina legal da contribuição compulsória de 0,3% e suas condições resolutórias de vigência dos TAREs.
4. **Acervo do Contencioso Administrativo Tributário (CAT/TO):** Inserir a Lei nº 1.288/2001 e o Decreto nº 7.000/2024 para cobrir as normas de impugnação fiscal e rito recursal do Conselho de Contribuintes e Recursos Fiscais (CCRF/TO).
