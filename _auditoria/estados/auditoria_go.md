# Relatório de Auditoria Tributária Estadual: Goiás (GO)
**Jurisdição:** Estado de Goiás (SEFAZ/GO - Secretaria de Estado da Economia)  
**Data da Auditoria:** Outubro de 2026  
**Especialidade:** ICMS, ICMS-ST, Benefícios Fiscais, Agronegócio, Indústria, Atacado e Transição para o IBS/CBS (EC 132/2023 e LC 214/2025)

---

## 1. Diagnóstico do Repositório `estaduais/go/` e Mapeamento de Normas Faltantes

### 1.1. Inventário dos Arquivos Existentes no Repositório

O repositório do Estado de Goiás (`estaduais/go/`) conta atualmente com 4 (quatro) arquivos estruturais:

1. **`estaduais/go/ricms/decreto-4852-1997.md`**
   - *Objeto:* Regulamento do Código Tributário do Estado de Goiás (RCTE/GO), aprovado pelo Decreto Estadual nº 4.852/1997.
   - *Conteúdo Atual:* Síntese contendo hipóteses de incidência e não incidência (art. 2º e 3º), quadro geral de alíquotas (alíquota modal de 19% elevada pela Lei nº 22.460/2023), DIFAL (contribuinte por dentro e não contribuinte via LC 190/2021), resumo de ICMS-ST, transferência de filiais (LC 204/2023 e Convênio 109/2024) e menção sucinta a incentivos.
   - *Diagnóstico Crítico:* Trata-se de um resumo executivo de 88 linhas. Faltam o detalhamento analítico do corpo permanente (arts. 1º a 180 do RCTE) e a quase totalidade dos **Anexos Fundamentais**, especialmente:
     - **Anexo VIII:** Substituição Tributária (regras operacionais, mercadorias sujeitas, apuração e ressarcimento);
     - **Anexo IX:** Dos Benefícios Fiscais (isenções, reduções de base de cálculo, créditos outorgados, diferimento e suspensão — coração operacional dos incentivos fiscais goianos);
     - **Anexo X e XIII:** Documentos fiscais eletrônicos, EFD e obrigações acessórias.

2. **`estaduais/go/ricms/lei-20787-2020-progoias-atacadista-fundeinfra.md`**
   - *Objeto:* Consolidação do Programa de Desenvolvimento Regional (PROGOIÁS - Lei nº 20.787/2020), do Crédito Outorgado Atacadista (RCTE/GO, Anexo IX, art. 11, III) e da contribuição ao Fundo Estadual de Infraestrutura (FUNDEINFRA - Lei nº 21.670/2022).
   - *Conteúdo Atual:* Resumo de 83 linhas com percentuais do crédito outorgado industrial (64% a 67%), contrapartida regressiva do PROTEGE GOIÁS (10%, 8%, 6%), mecânica do atacado interestadual (3% de crédito outorgado) e parâmetros do FUNDEINFRA.
   - *Diagnóstico Crítico:* Embora correto em seus valores essenciais, não traz as minúcias regulamentares do Decreto nº 9.724/2020 (regulamento do PROGOIÁS), os critérios de cálculo para empresas migradas dos programas PRODUZIR e FOMENTAR, nem a discriminação pormenorizada das mercadorias e alíquotas do FUNDEINFRA e suas instruções normativas.

3. **`estaduais/go/leis/itcmd/lei-11651-1991.md`**
   - *Objeto:* Recorte temático da Lei Estadual nº 11.651/1991 (Código Tributário do Estado de Goiás - CTE/GO) dedicado ao Imposto sobre a Transmissão Causa Mortis e Doação de Quaisquer Bens ou Direitos (ITCMD).
   - *Conteúdo Atual:* Fato gerador, regras de competência interestadual harmonizadas à EC 132/2023, progressividade de alíquotas (2%, 4%, 6% e 8%), não incidência sobre VGBL/PGBL (Tema 1214 STF), avaliação societária e penalidades.
   - *Diagnóstico Crítico:* Adequado para o escopo do ITCMD, servindo de base sólida para inventários e planejamentos sucessórios.

4. **`estaduais/go/leis/ipva/lei-11651-1991.md`**
   - *Objeto:* Recorte temático da Lei Estadual nº 11.651/1991 dedicado ao Imposto sobre a Propriedade de Veículos Automotores (IPVA).
   - *Conteúdo Atual:* Fato gerador ampliado (veículos aéreos e aquáticos conforme EC 132/2023), competência de domicílio (Tema 708 STF), alíquotas por modalidade (1,25% a 3,75%), imunidades, desonerações e repartição constitucional de receitas.
   - *Diagnóstico Crítico:* Bem estruturado e atualizado juridicamente.

---

### 1.2. Mapeamento de Normas Faltantes e Lacunas Críticas

Para conferir higidez e completude de nível pericial ao repositório de Goiás, constata-se a necessidade imediata de incorporação dos seguintes atos normativos:

| Ato Normativo | Ementa / Objeto Essencial | Prioridade de Inclusão | Justificativa Técnica |
| :--- | :--- | :--- | :--- |
| **Lei nº 11.651/1991 (Integral / ICMS)** | Código Tributário do Estado de Goiás (CTE/GO) — Parte Geral e Normas Materiais do ICMS (arts. 1º a 70). | **Crítica (Urgente)** | Base legal primária de todo o sistema tributário estadual. Atualmente, o repositório só possui recortes de ITCD e IPVA. |
| **Decreto nº 4.852/1997 (Anexo IX Completo)** | Anexo IX do RCTE/GO — Dos Benefícios Fiscais. | **Crítica (Urgente)** | Disciplina exaustivamente todas as isenções, reduções de base de cálculo, créditos outorgados e diferimentos do ICMS em GO. |
| **Decreto nº 4.852/1997 (Anexo VIII Completo)** | Anexo VIII do RCTE/GO — Da Substituição Tributária. | **Alta** | Define as regras de responsabilidade tributária, MVA, retenção na fonte e ressarcimento de ICMS-ST interno e interestadual. |
| **Lei nº 16.469/2009** | Regula o Processo Administrativo Tributário (PAT/GO) e a estrutura do Conselho Administrativo Tributário (CAT/GO). | **Alta** | Norma indispensável para o contencioso administrativo fiscal, prazos de impugnação, recursos (Câmaras e Pleno) e nulidades. |
| **Lei nº 14.469/2003 e Dec. nº 5.833/2003** | Institui o Fundo de Proteção Social do Estado de Goiás (PROTEGE GOIÁS). | **Alta** | Regula o adicional de até 2% de ICMS sobre supérfluos e a cobrança financeira compulsória sobre fruição de benefícios fiscais. |
| **Lei nº 21.670/2022 e Lei nº 21.671/2022** | Criação do FUNDEINFRA e fixação da contribuição sobre produtos agropecuários e minerais (Taxa do Agro). | **Crítica (Urgente)** | Vital para o agronegócio e mineração em GO; condicionante obrigatória de diferimentos e regimes especiais de exportação. |
| **Decreto nº 9.724/2020** | Regulamenta o Programa PROGOIÁS (Lei nº 20.787/2020). | **Média** | Detalha a metodologia de enquadramento, cálculo do crédito outorgado, transição de empresas do PRODUZIR e metas de investimento. |
| **Leis nº 11.180/1990 e nº 13.591/2000** | Leis instituidoras dos Programas FOMENTAR e PRODUZIR. | **Média (Histórica/Acervo)** | Embora substituídos pelo PROGOIÁS, ainda regem contratos antigos em fase de liquidação/migração e passivos fiscais correlatos. |
| **Lei nº 21.245/2022 e Lei nº 22.460/2023** | Adequação do CTE/GO à LC 190/2021 (DIFAL) e majoração da alíquota modal interna do ICMS para 19% (a contar de 01/04/2024). | **Alta** | Fundamentos legais vigentes que balizam a formação de preços e alíquotas no comércio B2B e B2C interestadual e interno. |
| **Decreto nº 10.370/2023** | Incorpora a desoneração de transferências entre filiais e a faculdade de equiparação à tributação (Convênios 178/23 e 109/24). | **Alta** | Regulamentação da ADC 49 e LC 204/2023 no âmbito do Fisco goiano. |

---

## 2. Relacionamento do ICMS-GO com os Demais 26 Estados e Distrito Federal

Goiás ocupa posição geográfica central e estratégica no território nacional (Centro-Oeste), atuando tanto como grande exportador de commodities agropecuárias e bens industriais (medicamentos, veículos, alimentos processados) quanto como polo de importação e distribuição interestadual (hub atacadista do DAIA e Anápolis).

```
                      +---------------------------------------+
                      |       ESTADO DE GOIÁS (GO)            |
                      |  Alíquota Geral Interna: 19%          |
                      +---------------------------------------+
                                     /         \
    Saídas Interestaduais de GO     /           \     Entradas Interestaduais em GO
   (Resolução SF nº 22/1989):      /             \   (Resolução SF nº 22/1989 & 13/2012):
  +-------------------------------+               +---------------------------------------+
  |  12% para QUALQUER UF         |               |  - 7% do Sul/Sudeste (exceto ES)      |
  |  (Norte, Nordeste, Centro-    |               |  - 12% do Norte, NE, CO e ES          |
  |   Oeste, Sul, Sudeste e DF)   |               |  - 4% Bens Importados (Conteúdo >40%) |
  |  4% se Conteúdo Importado >40%|               +---------------------------------------+
  +-------------------------------+
```

### 2.1. Matriz de Alíquotas Interestaduais Aplicáveis a Goiás

Em estrita consonância com a Resolução do Senado Federal nº 22/1989 e com a Resolução do Senado Federal nº 13/2012:

1. **Nas Saídas Originadas no Estado de Goiás com Destino a Outras Unidades da Federação:**
   - **Alíquota Geral de 12%:** Aplica-se às saídas de mercadorias nacionais com destino a **todas as demais 26 Unidades Federadas e ao Distrito Federal** (tanto para as Regiões Norte, Nordeste e Centro-Oeste quanto para as Regiões Sul e Sudeste). Goiás, sendo estado do Centro-Oeste, não possui alíquota interestadual de saída de 7%.
   - **Alíquota de 4% (Bens e Mercadorias Importadas do Exterior):** Aplica-se nas operações interestaduais com bens e mercadorias importados que, após seu desembaraço aduaneiro, não tenham sido submetidos a processo de industrialização, ou, caso submetidos, resultem em mercadoria cujo Conteúdo de Importação seja superior a 40% (FCI - Ficha de Conteúdo de Importação), nos termos da Resolução SF nº 13/2012 e Convênio ICMS 38/2013.
   - **Alíquota de 4% (Transporte Aéreo Interestadual):** Conforme Resolução SF nº 95/1996, aplicada a passageiros, cargas e malas postais.

2. **Nas Entradas no Estado de Goiás Provenientes de Outras Unidades da Federação:**
   - **Alíquota de 7%:** Quando as mercadorias forem remetidas por estabelecimentos localizados nas Regiões **Sul e Sudeste** (exceto Estado do Espírito Santo).
   - **Alíquota de 12%:** Quando as mercadorias forem remetidas por estabelecimentos situados nas Regiões **Norte, Nordeste, Centro-Oeste** e no Estado do **Espírito Santo**.
   - **Alíquota de 4%:** Quando a mercadoria remetida por qualquer unidade federada possuir Conteúdo de Importação superior a 40%.

---

### 2.2. Diferencial de Alíquotas (DIFAL)

O Diferencial de Alíquotas no Estado de Goiás opera sob dois regimes jurídicos perfeitamente demarcados:

#### A) DIFAL Contribuinte (Aquisições para Uso, Consumo ou Ativo Permanente)
- **Base Normativa:** CTE/GO, art. 20, § 1º-A (incluído pela Lei nº 19.999/2018 e mantido pelas Leis 21.245/2022 e 22.460/2023) e RCTE/GO, art. 65, inciso III.
- **Metodologia de Cálculo — Base Dupla ("Cálculo por Dentro"):** O Fisco goiano adota a fórmula de cálculo por dentro, na qual exclui-se o ICMS incidente na operação interestadual na origem e embute-se a alíquota interna de Goiás (19%) sobre o valor líquido, recalculando a base do imposto.

$$\text{Valor Líquido} = \text{Valor da Operação Interestadual} - \text{ICMS Origem}$$

$$\text{Base Dupla (GO)} = \frac{\text{Valor Líquido}}{1 - \text{Alíquota Interna GO (0,19)}}$$

$$\text{DIFAL Devido} = (\text{Base Dupla} \times \text{Alíquota Interna GO}) - \text{ICMS Origem}$$

*Exemplo Prático (Máquina Industrial do Ativo oriunda de SP a 7%):*
- Valor da mercadoria com frete: R$ 100.000,00.
- ICMS destacado na origem (7% de SP): R$ 7.000,00.
- Valor Líquido (sem ICMS SP): R$ 93.000,00.
- Base Dupla GO: $\frac{93.000,00}{1 - 0,19} = \frac{93.000,00}{0,81} = \text{R\$\ } 114.814,81$.
- ICMS Total calculado à alíquota de 19%: $114.814,81 \times 0,19 = \text{R\$\ } 21.814,81$.
- **DIFAL Devido a GO:** $\text{R\$\ } 21.814,81 - \text{R\$\ } 7.000,00 = \mathbf{\text{R\$\ } 14.814,81}$ (Carga efetiva de 14,81%, superior à diferença nominal de $19\% - 7\% = 12\%$).

#### B) DIFAL Não Contribuinte (Operações Destinadas a Consumidor Final — EC 87/2015)
- **Base Normativa:** Lei Complementar Federal nº 190/2021, Convênio ICMS 236/2021 e Lei Estadual nº 21.245, de 30 de março de 2022.
- **Metodologia de Base Única Nacional:** Em conformidade com a redação dada pela LC 190/2021 ao art. 13, § 1º, inciso I da Lei Complementar nº 87/1996, o imposto devido a título de DIFAL não contribuinte utiliza a **base única** correspondente ao valor da operação praticada no destino.
- **Recolhimento:** Cabe integralmente ao remetente de outra UF o recolhimento em favor do Estado de Goiás por meio de GNRE (código 10010-2) operação a operação, ou, caso possua inscrição estadual como substituto tributário DIFAL em GO, por apuração mensal via Guia Nacional de Informação e Apuração do ICMS Substituição Tributária (GIA-ST) e recolhimento até o dia 15 do mês subsequente.

---

### 2.3. Transferências entre Estabelecimentos do Mesmo Titular (Matriz e Filiais)

A histórica controvérsia da incidência de ICMS em transferências de mercadorias entre filiais da mesma empresa foi pacificada pela **ADC 49/DF do STF**, positivada pela **Lei Complementar nº 204/2023** e regulamentada pelo **Convênio ICMS nº 109/2024** e **Decreto Estadual nº 10.370/2023**:

1. **Regra Geral de Não Incidência:** A saída de mercadoria de um estabelecimento para outro pertencente ao mesmo titular (mesma pessoa jurídica) não constitui fato gerador do ICMS (LC 87/1996, art. 12, § 4º).
2. **Transferência Obrigatória do Crédito da Entrada:** Fica assegurada ao contribuinte a transferência dos créditos da não-cumulatividade acumulados nas aquisições anteriores, limitando-se o repasse às alíquotas interestaduais estabelecidas pelo Senado Federal (4%, 7% ou 12%), calculadas sobre:
   - O valor correspondente à entrada mais recente da mercadoria;
   - O custo de produção da mercadoria, se de fabricação própria;
   - O preço corrente da mercadoria no mercado atacadista do estabelecimento remetente.
3. **Opção Facultativa pela Manutenção da Tributação (Cláusula Sexta do Convênio ICMS 109/2024):**
   - O Estado de Goiás permite que o estabelecimento remetente opte por equiparar a transferência a uma operação tributada comum.
   - *Procedimento:* A opção deve ser formalizada até o último dia do mês de dezembro de cada ano com efeitos para o ano-calendário subsequente, mediante registro expresso no Livro Registro de Utilização de Documentos Fiscais e Termos de Ocorrências (RUDFTO) de todos os estabelecimentos do titular em Goiás.
   - *Vantagem Estratégica:* A equiparação à tributação regular é amplamente adotada pelas indústrias e redes varejistas sediadas em Goiás beneficiárias do PROGOIÁS ou de créditos outorgados, pois resguarda a manutenção integral dos regimes incentivados sem o risco de glosa de créditos no estado de destino.

---

### 2.4. Substituição Tributária Interestadual (ICMS-ST) e Protocolos Celebrados por GO

O Estado de Goiás é signatário de ampla gama de Convênios e Protocolos ICMS no âmbito do CONFAZ, sob a égide do **Convênio ICMS 142/2018** e do **Anexo VIII do RCTE/GO**:

- **Principais Segmentos Regulados:**
  - *Medicamentos e Produtos Farmacêuticos:* Protocolo ICMS 37/2009 (indústria de Anápolis/DAIA atua fortemente como substituta tributária remetente para todo o Brasil);
  - *Bebidas Alcoólicas e Frias (Cerveja, Chopp, Refrigerantes, Água Mineral):* Protocolo ICMS 11/1991 e alterações posteriores (polo cervejeiro de Anápolis e Itumbiara);
  - *Veículos Automotores Novos:* Convênio ICMS 199/2017 (montadoras de Anápolis e Catalão);
  - *Autopeças:* Protocolo ICMS 41/2008 e Protocolo ICMS 97/2010;
  - *Materiais de Construção, Acabamento e Elétricos:* Protocolo ICMS 85/2011;
  - *Cosméticos, Perfumaria e Higiene Pessoal:* Protocolo ICMS 191/2009;
  - *Tintas, Vernizes e Solventes:* Convênio ICMS 118/2017;
  - *Cigarros e Produtos de Tabacaria:* Convênio ICMS 111/2017.

- **Fórmula de Ajuste da Margem de Valor Agregado (MVA Ajustada):**  
  Nas operações interestaduais originadas em outros estados com destino a contribuintes goianos, quando a alíquota interna em Goiás (19%) for superior à alíquota interestadual de origem (7% ou 4%), aplica-se a MVA Ajustada obrigatória:

$$\text{MVA Ajustada} = \left[ \frac{(1 + \text{MVA-ST Original}) \times (1 - \text{ALQ Inter})}{(1 - \text{ALQ Intra})} \right] - 1$$

*Onde:*
- $\text{ALQ Inter}$ = alíquota interestadual (0,07 ou 0,04 ou 0,12);
- $\text{ALQ Intra}$ = alíquota interna de Goiás (0,19).
- *Exceção Obrigatória:* Se o remetente de outra UF for optante pelo **Simples Nacional**, é vedada a exigência da MVA Ajustada, aplicando-se imperativamente a **MVA Original** (Convênio ICMS 35/2011 e ADI 4884/STF).

---

## 3. Mecanismos de Dedução, Crédito e Compensação em Goiás

### 3.1. Não-Cumulatividade no CTE/GO e RCTE/GO
O direito à compensação do imposto devido em cada operação com o cobrado nas operações anteriores repousa nos artigos 58 a 64 do CTE/GO e artigos 46 a 62 do RCTE/GO:
- **Princípio da Idoneidade:** O aproveitamento do crédito condiciona-se à regular emissão de documento fiscal idôneo (NF-e modelo 55) e escrituração regular na Escrituração Fiscal Digital (EFD ICMS/IPI).
- **Estorno de Créditos (Art. 61 do CTE/GO):** O sujeito passivo deve estornar o crédito tomado sempre que a mercadoria entrada vier a ser objeto de:
  1. Saída ou prestação subsequente isenta ou não tributada;
  2. Saída ou prestação com base de cálculo reduzida (estorno proporcional);
  3. Deterioração, perecimento, furto, roubo ou extravio;
  4. Utilização em fim alheio à atividade operacional do estabelecimento.
- **Manutenção de Crédito Assegurada:** Fica dispensado o estorno nas operações de exportação para o exterior (art. 155, § 2º, X, "a" da CF/88) e nas hipóteses em que a lei estadual ou convênio CONFAZ conceder benefício fiscal com expressa previsão de "manutenção do crédito" (frequente no Anexo IX do RCTE).

---

### 3.2. Controle de Crédito do Ativo Permanente (CIAP)
A tomada de crédito do ICMS relativo à aquisição de bens destinados ao ativo imobilizado fabril ou operacional segue as diretrizes da Lei Complementar nº 102/2000, do art. 20, § 5º da LC 87/1996 e do art. 52, § 3º do RCTE/GO:

$$\text{Crédito Mensal Apropriável} = \left( \frac{\text{ICMS Destacado no Ativo}}{48} \right) \times \left( \frac{\text{Saídas Tributadas e Exportações do Mês}}{\text{Total das Saídas e Prestações do Mês}} \right)$$

- **Prazo:** Apropriação fracionada em 48 (quarenta e oito) meses consecutivos;
- **Bloco G da EFD:** Escrituração obrigatória no Bloco G da EFD ICMS/IPI;
- **Alienação Antecipada:** Na alienação do bem antes de transcorridos os 48 meses, o saldo credor remanescente é cancelado definitivamente, sendo vedada a apropriação das parcelas faltantes.

---

### 3.3. Restrições Específicas: Energia Elétrica e Telecomunicações
Em obediência ao art. 33 da Lei Complementar nº 87/1996 e art. 58 do CTE/GO:
1. **Energia Elétrica:** Somente confere direito a crédito do imposto:
   - Quando for consumida diretamente no processo de industrialização da mercadoria (exigindo laudo técnico expedido por engenheiro ou entidade idônea discriminando a fração produtiva da administrativa);
   - Quando sua distribuição ou geração for o próprio objeto da empresa;
   - Quando a saída de produtos resultante for destinada ao exterior (proporcionalmente).
2. **Serviços de Comunicação:** Somente geram crédito quando utilizados na execução de serviços de mesma natureza ou nas operações que destinem mercadorias ao exterior.
3. **Bens de Uso e Consumo:** Direito a crédito postergado até 1º de janeiro de 2033 (conforme LC 203/2023), conectando-se diretamente com o início da vigência do IBS/CBS.

---

### 3.4. Fundo de Proteção Social do Estado de Goiás (PROTEGE GOIÁS)
Instituído pela Lei Estadual nº 14.469/2003 e regulamentado pelo Decreto Estadual nº 5.833/2003:
- **Natureza Dupla:**
  1. *Adicional de Alíquota:* Adicional de até 2% (dois por cento) sobre a alíquota interna de ICMS incidente em operações com mercadorias e serviços supérfluos (bebidas alcoólicas, cigarros, cosméticos de luxo, gasolina, serviços de telecomunicação).
  2. *Contribuição Financeira Vinculada a Benefícios Fiscais:* Para usufruir de incentivos fiscais elencados no Anexo IX do RCTE/GO e no programa PROGOIÁS, a legislação goiana impõe ao contribuinte o recolhimento compulsório de uma porcentagem do benefício fiscal aproveitado em favor do Fundo PROTEGE.
  - *Alíquotas Regressivas no PROGOIÁS:* 10% (1º ano), 8% (2º ano) e 6% (a partir do 3º ano) do valor do crédito outorgado aproveitado.
  - *Alíquotas Gerais do Anexo IX:* Até 15% sobre a parcela de desoneração fiscal.
- *Efeito Jurídico Resolutivo:* O recolhimento tempestivo da contribuição ao PROTEGE é condição resolutiva para a validade do benefício fiscal. A inadimplência acarreta a caducidade do incentivo no período e a exigência integral do ICMS sem benefício, acompanhado de multa moratória e juros.

---

### 3.5. Acúmulo de Saldos Credores e Ressarcimento
- **Hipóteses Geradoras:** Concentram-se nas indústrias exportadoras de commodities (grãos, carnes, minérios), estabelecimentos comerciais atacadistas com vendas interestaduais e fabricantes de itens contemplados com alíquotas reduzidas na saída com insumos gravados à alíquota padrão.
- **Ressarcimento de ICMS-ST (Instrução Normativa GSE nº 1.442/2019):**  
  O contribuinte substituído tem direito ao ressarcimento do ICMS retido por ST quando:
  1. Promover saída para estabelecimento situado em outra unidade da Federação;
  2. A mercadoria for objeto de perecimento, quebra, furto ou sinistro;
  3. A base de cálculo efetiva da operação com o consumidor final for comprovadamente inferior à base de cálculo presumida (Tema 201 da Repercussão Geral do STF - RE 593849).

---

## 4. Setor Agrícola e Rural Goiano

O agronegócio é o pilar motriz do Produto Interno Bruto (PIB) do Estado de Goiás, com liderança nacional na produção de soja, milho, cana-de-açúcar, algodão, carnes bovina, suína e avícola, e mineração vinculada (fertilizantes fosfatados).

```
   PRODUTOR RURAL (GO)
  (NFP-e Modelo 55 / CCE-GO)
         |
         |  DIFERIMENTO DO ICMS (Apêndice II, Anexo VIII RCTE/GO)
         |  + Condicionante: Recolhimento ao FUNDEINFRA (até 1,65%)
         v
   INDÚSTRIA / COOPERATIVA / USINA (GO)
  (Esmagamento, Abate, Açúcar e Etanol)
         |
         +---------------------------------+
         |                                 |
         v                                 v
   SAÍDAS INTERNAS INDUSTRIALIZADAS   EXPORTAÇÃO DIRETA / TRADING
   (Crédito Outorgado Carne/Etanol)  (Imunidade Art. 155, X, "a" CF)
```

### 4.1. Insumos Agropecuários e Convênio ICMS 100/97 no RCTE/GO
A internalização do Convênio ICMS 100/1997 em Goiás opera pelo Anexo IX do RCTE/GO (artigos 6º e 7º):
- **Isenção Interna:** Aplicada nas operações internas com inseticidas, fungicidas, herbicidas, vacinas veterinárias, sementes certificadas e rações balanceadas.
- **Reduções de Base nas Saídas Interestaduais:** Reduções de 30% a 60% na base de cálculo para saídas destinadas a produtores rurais em outras UFs.
- **Recomposição Tributária Progressiva (Convênio ICMS 26/2021):** O Fisco goiano aplica a recomposição paulatina da carga de ICMS sobre fertilizantes e adubos químicos simples ou compostos, fixando alíquotas efetivas graduadas (1%, 2%, 3% e 4%) nas operações interestaduais e internas, eliminando antigas isenções totais e onerando o custo operacional de fertilizantes químicos.

---

### 4.2. FUNDEINFRA (Lei Estadual nº 21.670/2022 — A "Taxa do Agro")

Instituída no apagar das luzes de 2022 para recompor o erário goiano após a queda de arrecadação do ICMS imposta pela Lei Complementar federal nº 194/2022 (combustíveis e energia):

- **Estruturação Jurídica e Natureza Condicionante:**  
  A contribuição ao Fundo Estadual de Infraestrutura (FUNDEINFRA) não foi instituída formalmente como imposto compulsório autônomo, mas sim como uma **condição potestativa/resolutiva de acesso a regimes tributários favorecidos**:
  - Para usufruir de **Diferimento do ICMS** nas operações internas;
  - Para usufruir de **Regime Especial de Apuração e Exportação** (dispensa de comprovação ato a ato do ICMS nas saídas com fim específico de exportação ou remessa para o exterior).
  - *Mecanismo Prático:* Caso o produtor rural ou a agroindústria opte por **não recolher** a contribuição ao FUNDEINFRA, o diferimento do ICMS é sumariamente suspenso, devendo a operação interna ser submetida à incidência imediata e recolhimento antecipado do ICMS à alíquota de 19% ou 12%.

- **Alíquotas e Valores Fixados pela Secretaria de Estado da Economia (IN nº 155/2022-SRE e IN GSE nº 001/2023):**
  - **Soja e Milho:** até 1,65% sobre o valor da operação;
  - **Cana-de-Açúcar destinada à moagem:** até 0,50%;
  - **Gado Bovino e Bufalino (abate interno ou saída viva):** até 0,50%;
  - **Algodão em caroço e em pluma:** até 1,65%;
  - **Minérios (Ferro, Ouro, Níquel, Fosfato):** até 1,65%.

- **Contencioso Constitucional (ADI 7363 / STF):**  
  Ajuizada pela Confederação Nacional da Indústria (CNI) e entidades do agronegócio, sustentando vício formal de tributação e quebra da não afetação de receitas. O Plenário do STF, em decisão de mérito com repercussão nacional, referendou a higidez do fundo, assentando que fundos vinculados a regimes desonerativos estaduais são válidos desde que:
  1. A contribuição seja rigorosamente facultativa (subsistindo ao contribuinte a opção de tributação ordinária pelo ICMS sem benefícios);
  2. As receitas auferidas fiquem estritamente vinculadas a obras de infraestrutura de transporte e logística agropecuária, vedado o desvio para despesas correntes de pessoal.

---

### 4.3. Diferimento do ICMS nas Commodities Agrícolas em Goiás
Regulado pelo Apêndice II do Anexo VIII do RCTE/GO e Anexo IX:
- **Soja, Milho e Algodão:** Saídas do produtor rural para armazéns gerais, cooperativas e tradings localizadas em Goiás operam sob diferimento total do ICMS. O diferimento encerra-se no momento da saída física para fora do Estado (tributada a 12%) ou na destinação final industrial.
- **Gado Bovino em Pé:** Diferimento nas operações entre produtores rurais inscritos (cria e recria) e no fornecimento para frigoríficos instalados no Estado de Goiás. O imposto diferido é considerado incorporado na apuração subsequente das saídas de carne pelo frigorífico.
- **Cana-de-Açúcar:** Diferimento total na entrega das lavouras (produtores independentes ou arrendatários) para as usinas sucroalcooleiras instaladas no território goiano.

---

### 4.4. Créditos Outorgados na Agroindústria
- **Frigoríficos e Abatedouros (Anexo IX, Art. 11, do RCTE/GO):** Crédito outorgado concedido na saída interestadual de carne resfriada ou congelada, bovina, suína ou de aves, resultando em uma carga tributária líquida efetiva de **1% a 3%** do ICMS.
- **Setor Sucroalcooleiro (Etanol e Açúcar):** Mecanismos combinados de crédito outorgado que reduzem a carga incidente sobre a comercialização de Etanol Hidratado Combustível (EHC), estimulando a competitividade das usinas goianas em relação a São Paulo e Minas Gerais.

---

### 4.5. NFP-e e Regime Simplificado do Produtor Rural
- **Obrigatoriedade da NF-e (Modelo 55):** O produtor rural pessoa física estabelecido em Goiás está integralmente sujeito à emissão da Nota Fiscal de Produtor Eletrônica (NFP-e). Para pequenos produtores rurais familiares, a Secretaria da Economia disponibiliza o aplicativo "Nota Fiscal Fácil - NFF" e o serviço web de emissão de Nota Fiscal Avulsa Eletrônica (NFA-e).
- **Cadastro de Contribuintes do Estado (CCE):** O produtor rural goiano que atua como pessoa física é inscrito no CCE-GO na condição de produtor rural não equiparado a comerciante, estando dispensado da entrega da EFD ICMS/IPI complexa, realizando suas apurações fiscais vinculadas às guias de diferimento e recolhimentos simplificados.

---

## 5. Setor Industrial Goiano

### 5.1. Programa PROGOIÁS (Lei nº 20.787/2020 e Decreto nº 9.724/2020)

O Programa de Desenvolvimento Regional (**PROGOIÁS**) representou a transição modernizadora da política industrial do Estado de Goiás, substituindo o antigo e engessado modelo dos programas **FOMENTAR** (Lei nº 11.180/1990) e **PRODUZIR** (Lei nº 13.591/2000), os quais funcionavam como financiamento do saldo devedor do ICMS com deságios de liquidação.

```
+---------------------------------------------------------------------------------+
|                       PROGRAMA PROGOIÁS (Lei nº 20.787/2020)                   |
+---------------------------------------------------------------------------------+
|  Mecanismo: Crédito Outorgado Direto sobre o Saldo Devedor Mensal do ICMS       |
|                                                                                 |
|  Percentuais de Desoneração:                                                    |
|  - 1º ao 12º mês: 64% de Crédito Outorgado                                      |
|  - 13º ao 24º mês: 65% de Crédito Outorgado                                     |
|  - A partir do 25º mês: 66% de Crédito Outorgado                                |
|  - Municípios Prioritários (Oeste/Nordeste): 67% IMEDIATO                       |
|                                                                                 |
|  Contrapartida Financeira (PROTEGE GOIÁS):                                      |
|  - 10% (1º ano) -> 8% (2º ano) -> 6% (a partir do 3º ano) sobre o incentivo     |
|                                                                                 |
|  Diferimento Estratégico:                                                       |
|  - Importação de matérias-primas e insumos (Porto Seco de Anápolis)             |
|  - Aquisição interestadual e importação de Ativo Imobilizado (Dispensa DIFAL)   |
+---------------------------------------------------------------------------------+
```

- **Mecânica Operacional do PROGOIÁS:**
  1. O estabelecimento industrial apura normalmente seus débitos de saídas de produtos fabricados e seus créditos de entradas (matérias-primas, insumos, fretes).
  2. Apurado o saldo devedor mensal do ICMS da produção própria, aplica-se o percentual de crédito outorgado concedido (64% a 67%).
  3. O contribuinte recolhe apenas a parcela remanescente (33% a 36% do saldo devedor) a título de ICMS normal.
  4. Sobre o valor do crédito outorgado efetivamente aproveitado no mês, incide a contrapartida regressiva destinada ao Fundo PROTEGE GOIÁS (10% a 6%).

---

### 5.2. Polos Industriais Estratégicos de Goiás

1. **Polo Farmacêutico de Anápolis (DAIA - Distrito Agroindustrial de Anápolis):**
   - É o segundo maior polo de fabricação de medicamentos da América Latina (Hypera/Brainfarma, Teuto/Pfizer, EMS, Gehaka, Melcon, Vitamedic).
   - *Vantagem Tributária:* Combina o diferimento na importação de Insumos Farmacêuticos Ativos (IFAs) desembaraçados na Estação Aduaneira do Interior (Porto Seco Centro-Oeste / Anápolis) com o crédito outorgado do PROGOIÁS e a localização logística central no cruzamento das Ferrovias Norte-Sul e Centro-Atlântica e rodovias BR-060 e BR-153.
2. **Polo Automotivo de Catalão e Anápolis:**
   - Montadora HPE Automotores (Mitsubishi e Suzuki) em Catalão e montadora CAOA Chery (Hyundai e Chery) em Anápolis.
   - Operam sob incentivos estaduais do PRODUZIR/PROGOIÁS associados aos benefícios federais do Regime Automotivo do Norte, Nordeste e Centro-Oeste (art. 40 da Lei Federal nº 9.440/1997 e prorrogações da Lei Federal nº 14.802/2024).
3. **Polo de Processamento de Alimentos e Fertilizantes (Sudoeste Goiano):**
   - Municípios de Rio Verde, Jataí, Mineiros, Itumbiara e Montividiu. Complexos industriais da JBS, BRF, Cargill, Caramuru Alimentos, Comigo, Mosaic Fertilizantes e Yara.

---

### 5.3. Tomada de Crédito sobre Insumos e Drawback
- **Insumos Industriais:** Apropriação permitida sobre matérias-primas, produtos intermediários e materiais de embalagem consumidos diretamente no processo produtivo fabril (inclusive insumos secundários como ácidos, abrasivos e reagentes consumidos por desgaste mecânico ou químico contínuo).
- **Drawback (Convênio ICMS 27/1990 e RCTE/GO, Anexo IX, Art. 6º):** Isenção e suspensão do ICMS na entrada de mercadorias importadas sob o regime de Drawback Suspensão, desde que vinculadas a compromisso de exportação posterior e devidamente comprovado o cumprimento do ato concessório federal.

---

## 6. Setor de Produto Acabado: Atacado, Varejo e Distribuição

### 6.1. Centros de Distribuição e Atacadistas (Crédito Outorgado do Art. 11, III do Anexo IX do RCTE/GO)

O Estado de Goiás consolidou-se como um dos principais eixos logísticos da distribuição mercantil atacadista do país (com expressiva concentração de Centros de Distribuição em Aparecida de Goiânia, Goiânia, Senador Canedo e Anápolis) mediante uma das mais competitivas sistemáticas tributárias do Brasil:

```
               OPERAÇÃO ATACADISTA INTERESTADUAL DE GOIÁS
    
    1. Entrada no CD em Goiás (origem SP - alíquota 7%):
       - Custo de Compra: R$ 1.000.000,00
       - Crédito de ICMS de Entrada: R$ 70.000,00 (7%)
    
    2. Saída Interestadual do Atacadista de GO (alíquota 12%):
       - Valor de Venda Interestadual: R$ 1.200.000,00
       - Débito Bruto Destacado na NF-e: R$ 144.000,00 (12%)
       - Crédito Outorgado de GO (Art. 11, III): R$ 36.000,00 (3% da Base)
       - Débito Efetivo Estadual: R$ 108.000,00 (9%)
    
    3. Apuração Líquida do ICMS em Goiás:
       - Débito Efetivo (R$ 108.000,00) - Crédito Entrada (R$ 70.000,00)
       - ICMS Líquido a Recolher em GO: R$ 38.000,00 (Carga líquida de apenas 3,16%!)
       * Destinatário em outro Estado apropria CRÉDITO INTEGRAL de 12% (R$ 144.000,00).
```

- **Mecânica Operacional (Art. 11, III do Anexo IX):**
  - Concede **Crédito Outorgado de 3% (três por cento)** sobre o valor da base de cálculo nas saídas interestaduais promovidas por estabelecimentos comerciais atacadistas e centros de distribuição estabelecidos em Goiás, em operações tributadas à alíquota de **12%**.
  - O débito fiscal próprio é reduzido para **9%**, preservando-se o destaque de **12%** na NF-e para que o cliente adquirente contribuinte em outro Estado aproveite o crédito de 12% sem questionamento.
  - O atacadista toma os créditos integrais de entrada das regiões Sul e Sudeste (7% ou 4%), resultando em margens extraordinariamente atrativas para distribuição em escala nacional.

- **Saídas Internas B2B (Art. 8º, VIII do Anexo IX do RCTE/GO):**
  - Redução da base de cálculo nas operações internas realizadas por atacadistas ou industriais destinadas a contribuintes goianos para revenda ou industrialização, de tal sorte que a **carga tributária final resulte em 10% (dez por cento)**, impondo-se a trava de limitação dos créditos das entradas a 10%.

---

### 6.2. Margem de Valor Agregado (MVA), Pautas Fiscais e ICMS-ST
- **Pautas Fiscais (Boletim de Preços da Economia/GO):** A SEFAZ/GO edita pautas periódicas de valores mínimos de referência de mercado para fixação da base de cálculo do ICMS em produtos agrícolas (gado, grãos, leite), materiais de construção e bebidas. Caso o valor constante da nota fiscal seja inferior à pauta, o imposto é calculado compulsoriamente pelo valor pautado.
- **Ressarcimento e Restituição:** O Fisco goiano exige prévia homologação pelo sistema eletrônico da SEFAZ para apropriação ou transferência de créditos decorrentes de ICMS-ST recolhido a maior ou mercadorias com saída interestadual.

---

### 6.3. E-commerce e Marketplaces (Responsabilidade Tributária)
- **Responsabilidade Solidária do Intermediador de Negócios (CTE/GO, Art. 45, inciso XII-A):**
  - As plataformas de e-commerce, marketplaces e intermediadores digitais de pagamento são expressamente definidas como responsáveis solidárias pelo pagamento do ICMS quando realizarem a intermediação de operações de mercadorias destinadas ao Estado de Goiás cujo vendedor não emita documento fiscal eletrônico idôneo ou utilize dados cadastrais falsos.
- **Monitoramento Fiscal de Centros de Triagem:** Fiscalização eletrônica intensiva em centros de distribuição e hubs das transportadoras e Correios em Goiás (especialmente no anel rodoviário de Goiânia e Aparecida de Goiânia), com lavratura automática de Auto de Infração via cruzamento de Manifesto Eletrônico de Documentos Fiscais (MDF-e) com extrato de pagamentos eletrônicos e cartões (DIMP).

---

## 7. Transição para o IBS / CBS da Reforma Tributária (EC 132/2023, LC 214/2025 e LC 227/2026)

A promulgação da **Emenda Constitucional nº 132/2023** e a disciplina da **Lei Complementar nº 214/2025** operam uma transformação tectônica no arranjo produtivo e tributário do Estado de Goiás.

```
       CRONOGRAMA DE TRANSIÇÃO DO ICMS PARA O IBS EM GOIÁS
  
  2026-2028: Teste Federal CBS (0,9%) e IBS (0,1%) | PROGOIÁS e Atacado 100%
  2029: Início da redução gradual do ICMS (90%) | Redução de 10% dos Benefícios
  2030: Redução de 25% dos Benefícios Fiscais (Fruição de 75%)
  2031: Redução de 40% dos Benefícios Fiscais (Fruição de 60%)
  2032: Redução de 55% dos Benefícios Fiscais (Fruição de 45%)
  2033: EXTINÇÃO TOTAL DO ICMS | Extinção de Todos os Benefícios Goianos
        Entrada em pleno vigor do IBS no Princípio do Destino
```

### 7.1. Fim dos Benefícios Fiscais e Impacto no Modelo Goiano

Conforme o artigo 130 do Ato das Disposições Constitucionais Transitórias (ADCT):
1. **Perda da Eficácia dos Benefícios Convalidados:** Todos os benefícios fiscais e financeiro-fiscais concedidos por Goiás com base na LC 160/2017 e Convênio ICMS 190/2017 (PROGOIÁS, Crédito Outorgado Atacadista de 3%, reduções de base do agronegócio e frigoríficos) serão linearmente reduzidos entre 2029 e 2032 até a sua extinção total em 1º de janeiro de 2033.
2. **Erosão da Atratividade Logística e Fabril:**
   - Com a transição para o **Princípio do Destino Puro** no Imposto sobre Bens e Serviços (IBS), a receita tributária passará a pertencer integralmente ao Estado onde se situa o consumidor ou adquirente final do bem.
   - Os Centros de Distribuição de Aparecida de Goiânia e o Polo Farmacêutico de Anápolis não poderão mais transferir vantagens tributárias originárias aos seus compradores localizados em São Paulo, Rio de Janeiro ou Minas Gerais, nivelando artificialmente os custos com as regiões litorâneas e consumidoras.

---

### 7.2. Fundo de Compensação de Benefícios Fiscais (FCBF)
Instituído pelo art. 159 da Constituição Federal e art. 131 do ADCT, regulamentado no âmbito da Lei Complementar da Reforma Tributária:
- **Aporte Financeiro Nacional:** R$ 160 bilhões de recursos da União aportados entre 2029 e 2032 (R$ 8 bilhões em 2029, R$ 16 bilhões em 2030, R$ 24 bilhões em 2031 e R$ 32 bilhões em 2032, mantendo parcelas decrescentes de compensação até 2043).
- **Habilitação das Empresas de Goiás:**
  - Terão direito a compensação financeira as pessoas jurídicas titulares de benefícios fiscais devidamente convalidados na forma da LC 160/2017 e vigentes em **31 de maio de 2023**.
  - As indústrias farmacêuticas de Anápolis, montadoras e empresas atacadistas instaladas em Goiás deverão comprovar perante a comissão mista federal-estadual a realização efetiva dos investimentos pactuados em seus termos de acordo de regime especial (TARE).

---

### 7.3. Homologação de Saldos Credores Acumulados de ICMS (Art. 134 do ADCT)
- **Regra Constitucional:** O saldo credor de ICMS acumulado e escriturado pelos contribuintes até 31 de dezembro de 2032, oriundo de operações de exportação e aquisições de ativo imobilizado, será submetido a processo de **homologação formal pela SEFAZ/GO**.
- **Prazo de Compensação:** Uma vez homologado, o saldo credor será compensado com o IBS devido no âmbito estadual em **240 (duzentas e quarenta) parcelas mensais, iguais e sucessivas (20 anos)**, a contar de 1º de janeiro de 2033, devidamente atualizado monetariamente pelo IPCA.
- **Risco Crítico para o Agronegócio e Indústrias Goianas:** O volume expressivo de saldo credor represado em cooperativas de grãos, frigoríficos e tradings corre severo risco de perda de liquidez financeira caso a Secretaria da Economia de Goiás imponha travas cadastrais ou morosidade excessiva nas homologações administrativas.

---

### 7.4. O Futuro do FUNDEINFRA e a Sobreposição com o Imposto Seletivo
- **Exceção Transitória Constitucional (Art. 136 do ADCT):** A EC 132/2023 inseriu o art. 136 do ADCT (denominado "Emenda FUNDEINFRA/FETHAB"), permitindo aos estados manterem as contribuições sobre produtos primários e semielaborados existentes em 30 de abril de 2023 até **31 de dezembro de 2043**.
- **Conflito Material e Insegurança Jurídica:**
  - Embora expressamente salvo pelo art. 136 do ADCT, o FUNDEINFRA enfrentará grave crise de coexistência material a partir de 2027 com a instituição do **Imposto Seletivo (IS)** da União (art. 153, VIII da CF/88), o qual incidirá sobre a extração de bens minerais (como ouro, níquel e fosfatos minerados em GO).
  - Além disso, a perda do diferimento do ICMS em 2033 esvaziará a natureza potestativa/condicionante do FUNDEINFRA: se não existirá mais ICMS para ser diferido, o Fundo perderá sua âncora jurídica desonerativa, transformando-se em exação autônoma de legalidade questionável e sob imensa pressão de extinção por parte da Frente Parlamentar da Agropecuária (FPA).

---

## 8. Recomendações Técnicas e Plano de Ação para o Repositório

Com base na auditoria exaustiva realizada, recomenda-se a execução imediata das seguintes medidas de estruturação documental e normativa no repositório:

1. **Desdobrar e Integrar a Lei Estadual nº 11.651/1991 (CTE/GO):** Criar em `estaduais/go/leis/` a consolidação integral da Lei nº 11.651/1991 contemplando a Parte Geral e o Livro do ICMS (arts. 1º a 70), superando a fragmentação que atualmente só disponibiliza ITCD e IPVA.
2. **Incorporar o Anexo IX do RCTE/GO (Benefícios Fiscais):** Adicionar à pasta `estaduais/go/ricms/` o arquivo `anexo-ix-beneficios-fiscais.md`, indexando as disposições de isenções, reduções de base de cálculo do agronegócio e atacado e créditos outorgados industriais.
3. **Incorporar a Legislação do Processo Administrativo Tributário (PAT/GO):** Inserir a **Lei Estadual nº 16.469/2009** e o regimento do Conselho Administrativo Tributário (CAT/GO).
4. **Atualizar o Decreto nº 10.370/2023:** Detalhar no arquivo do RCTE a cláusula sexta do Convênio ICMS 109/2024 regulamentando o procedimento de opção irretratável pela tributação nas transferências de mercadorias entre filiais goianas e de outros estados.
5. **Consolidar os Atos do FUNDEINFRA:** Compilar a Lei nº 21.670/2022, Lei nº 21.671/2022, Decreto nº 10.187/2022 e a Instrução Normativa GSE nº 001/2023 em documento de consulta específica para o agronegócio.
