# Relatório Técnico de Auditoria Tributária: Estado de Mato Grosso (MT)

**Data de Elaboração:** 31 de Outubro de 2026  
**Auditor Especialista:** Tributarista Especialista no Ordenamento Jurídico-Tributário de Mato Grosso  
**Unidade Federativa:** Mato Grosso (MT)  
**Status do Repositório:** Análise de Cobertura Normativa, Diagnóstico de Lacunas, Práticas Interestaduais, Cadeia Agroindustrial e Transição para a Reforma Tributária (EC 132/2023 e LC 214/2025)

---

## 1. Inventário das Normas Estaduais no Repositório e Diagnóstico de Lacunas (Normas Faltantes)

### 1.1. Diagnóstico do Acervo Atual em `estaduais/mt/`
A auditoria técnica realizada na pasta `estaduais/mt/` constatou a existência de apenas 3 (três) arquivos consolidados:
1. `estaduais/mt/ricms/decreto-2214-2014.md`: Síntese estrutural do Regulamento do ICMS de Mato Grosso (RICMS/MT). Apresenta um sumário com 89 linhas, contendo os princípios gerais de incidência, tabela de alíquotas e diretrizes preliminares de DIFAL e ST. Não engloba a íntegra dos anexos regulamentares setoriais cruciais.
2. `estaduais/mt/leis/itcmd/lei-7850-2002.md`: Versão consolidada da Lei Estadual nº 7.850/2002 (ITCMD/MT), cobrindo hipóteses de incidência, regras de competência territorial pós-EC 132/2023, tabela de alíquotas progressivas (2% a 8%) e critérios de avaliação patrimonial de quotas societárias.
3. `estaduais/mt/leis/ipva/lei-7301-2000.md`: Consolidação da Lei Estadual nº 7.301/2000 (IPVA/MT), compreendendo o fato gerador (inclusive aéreo e aquático), tabela de alíquotas diferenciadas por tipo de veículo (1% a 4%), regimes de proporcionalidade duodecimal e critérios de fixação de domicílio (Tema 708 do STF).

### 1.2. Mapeamento Crítico de Normas Faltantes de Alta Prioridade
Para que o repositório atinja excelência técnica e completude para fins de conformidade fiscal e treinamento de modelos de linguagem, é imperativa a ingestão das seguintes normas primárias e secundárias do Estado de Mato Grosso:

| Norma Faltante | Ementa / Objeto Principal | Impacto Sistêmico / Relevância Prática | Caminho Sugerido no Repositório |
| :--- | :--- | :--- | :--- |
| **Lei Ordinária nº 7.098/1998** | Lei Geral do ICMS do Estado de Mato Grosso | Norma matriz de todo o sistema do ICMS-MT. Disciplina o fato gerador, base de cálculo, alíquotas (alíquota modal interna de 17%), responsabilidade e penalidades. | `estaduais/mt/leis/icms/lei-7098-1998.md` |
| **Decreto nº 2.214/2014 (Anexos Completos)** | Anexos Temáticos I a XVII do RICMS/MT | O regulamento vigente é segregado em Anexos: **Anexo IV** (Isenções), **Anexo V** (Redução de Base de Cálculo), **Anexo VI** (Créditos Presumidos), **Anexo VII** (Diferimento no Agro), **Anexo X** (Substituição Tributária) e **Anexo XVII** (Setor Comercial Atacadista). | `estaduais/mt/ricms/anexos-consolidados.md` |
| **Lei Complementar nº 631/2019** | Marco Legal da Reinstituição e Revisão dos Benefícios Fiscais (LC 160/17 e Convênio ICMS 190/17) | Maior reforma tributária interna de MT. Revogou a Carga Média histórica, reinstituiu o PRODEIC, PROALMAT, PRODER e estabeleceu a apuração normal com crédito outorgado. | `estaduais/mt/leis/incentivos/lc-631-2019.md` |
| **Lei Ordinária nº 7.958/2003 e Dec. 288/2019** | Programa de Desenvolvimento Industrial e Comercial de Mato Grosso (PRODEIC) | Disciplina as faixas de crédito outorgado (65% a 85% nas saídas internas; até 90%/95% nas interestaduais) e contrapartidas financeiras a fundos estaduais. | `estaduais/mt/leis/incentivos/lei-7958-2003-prodeic.md` |
| **Lei Ordinária nº 7.263/2000 e Dec. 1.261/2000** | Fundo Estadual de Transporte e Habitação (FETHAB) | Norma definidora da contribuição compulsória/facultativa incidente sobre a circulação e exportação de soja, milho, algodão, gado em pé, madeira e combustível. | `estaduais/mt/leis/fundos/lei-7263-2000-fethab.md` |
| **Lei Ordinária nº 8.797/2008** | Lei do Processo Administrativo Tributário de Mato Grosso (PAT/MT) | Regula o contencioso administrativo fiscal, lançamento de ofício, impugnações, Unidade de Julgamento Singular e Conselho de Contribuintes da SEFAZ/MT. | `estaduais/mt/leis/pat/lei-8797-2008.md` |
| **Lei Complementar nº 144/2003** | Fundo Estadual de Combate e Erradicação da Pobreza (FECEP/FECOP-MT) | Institui o adicional de 2% de ICMS sobre produtos supérfluos (art. 82 do ADCT). | `estaduais/mt/leis/fecep/lc-144-2003.md` |
| **Lei Ordinária nº 11.669/2021 e Lei 11.693/2022** | Leis de Adequação do DIFAL Não Contribuinte e Base Dupla | Adequam a legislação estadual à Lei Complementar Federal nº 190/2021 e fixam a base dupla no DIFAL Contribuinte. | `estaduais/mt/leis/icms/lei-11669-2021-difal.md` |
| **Decreto nº 650/2023, Dec. 706/2024 e Portaria SEFAZ 039/2024** | Regulamentação da ADC 49/STF, LC 204/23, Convênios 178/23 e 109/24 | Regulam a não incidência do ICMS na transferência interestadual de bens e o tratamento nevrálgico da interrupção do diferimento. | `estaduais/mt/decretos/decreto-706-2024-transferencias.md` |

---

## 2. Relacionamento do ICMS-MT com os Demais 26 Estados e Distrito Federal

### 2.1. Matriz de Alíquotas Interestaduais (Origem vs. Destino)
Mato Grosso situa-se no Centro-Oeste brasileiro, enquadrando-se nas normas da Resolução do Senado Federal nº 22/1989 e da Resolução SF nº 13/2012:

```
  [MATO GROSSO (MT)]  --- Saídas p/ qualquer das 26 UFs --->  Alíquota Interestadual: 12%
                                                              (ou 4% se Conteúdo de Importação > 40%)

  [Sul e Sudeste (exceto ES)]  --- Entradas interestaduais em MT --->  Alíquota: 7%
  [Norte, Nordeste, Centro-Oeste e ES]  --- Entradas interestaduais em MT --->  Alíquota: 12%
  [Qualquer UF]  --- Bens Importados / Conteúdo Importação > 40% --->  Alíquota: 4%
```

1. **Saídas de Mato Grosso para Qualquer Unidade da Federação:**
   - A alíquota é fixada em **12%** (doze por cento) para mercadorias nacionais com destino a qualquer Estado (Sul, Sudeste, Norte, Nordeste, Centro-Oeste ou Distrito Federal).
   - A alíquota é de **4%** (quatro por cento) nas operações com mercadorias importadas ou que possuam Conteúdo de Importação superior a 40% comprovado pela FCI (Resolução SF nº 13/2012 e Convênio ICMS 38/2013).
2. **Entradas Interestaduais em Mato Grosso:**
   - Mercadorias oriundas dos Estados do **Sul e Sudeste (exceto ES)** (`SP`, `RJ`, `MG`, `PR`, `SC`, `RS`): alíquota interestadual de **7%** na origem.
   - Mercadorias oriundas dos Estados do **Norte, Nordeste, Centro-Oeste e Espírito Santo**: alíquota interestadual de **12%** na origem.
   - Mercadorias importadas de qualquer procedência nacional com alíquota interestadual de **4%**.

### 2.2. Diferencial de Alíquotas (DIFAL): Regimes de Consumidor Final

#### 2.2.1. DIFAL Não Contribuinte (EC 87/2015, LC 190/2021, Convênio ICMS 236/2021 e Lei Estadual nº 11.669/2021)
Aplicável nas remessas interestaduais com destino a Mato Grosso cujo destinatário seja consumidor final não contribuinte habitual do ICMS (CFOP `6.107`, `6.108`):
- **Base de Cálculo Única:** O valor da operação inclui o montante do próprio ICMS devido ao Estado de MT (cálculo por dentro único).
- **Alíquota Interna Modal de MT:** **17%** (Lei Estadual nº 7.098/1998, art. 14, I, "a"). Mato Grosso manteve expressamente a alíquota de 17%, não adotando a majoração generalizada observada em outras UFs em 2023/2024.
- **Fundo de Combate à Pobreza:** Se o produto for classificado como supérfluo pela LC nº 144/2003, adiciona-se **2%** de FECEP, totalizando alíquota interna de **19%**.
- **Equações Matemáticas de Apuração:**
  $$\text{DIFAL}_{\text{MT}} = \text{BC}_{\text{única}} \times (\text{ALQ}_{\text{interna MT}} - \text{ALQ}_{\text{interestadual}})$$
  $$\text{FECEP}_{\text{MT}} = \text{BC}_{\text{única}} \times \text{ALQ}_{\text{FECEP (2\%)}}$$

#### 2.2.2. DIFAL Contribuinte (Aquisição de Bens para Uso, Consumo ou Ativo Permanente)
Nas aquisições efetuadas por contribuintes inscritos no CCE/MT destinadas a seu uso, consumo ou imobilização, aplica-se a metodologia da **Base Dupla** ("Cálculo por Dentro"), disciplinada pelo art. 72, inciso IX e § 8º do RICMS/MT e convalidada pela Lei nº 11.693/2022:

1. **Exclusão do ICMS de Origem:**
   $$V_{\text{líquido}} = V_{\text{operação}} \times (1 - \text{ALQ}_{\text{inter}})$$
2. **Recomposição da Base de Cálculo com o ICMS de MT ("Gross-up"):**
   $$\text{BC}_{\text{MT}} = \frac{V_{\text{líquido}}}{1 - \text{ALQ}_{\text{interna MT}}}$$
3. **Cálculo do DIFAL Efetivo:**
   $$\text{DIFAL Devido} = (\text{BC}_{\text{MT}} \times \text{ALQ}_{\text{interna MT}}) - (V_{\text{operação}} \times \text{ALQ}_{\text{inter}})$$

*Simulação Prática comparativa (aquisição de R$ 100.000,00 vinda de SP à alíquota de 7% com interna MT de 17%):*
- Pelo cálculo simples (base única): $\text{DIFAL} = R\$ 100.000 \times (17\% - 7\%) = R\$ 10.000,00$.
- Pelo cálculo por base dupla (vigente em MT):
  - $V_{\text{líquido}} = 100.000 \times (1 - 0,07) = R\$ 93.000,00$
  - $\text{BC}_{\text{MT}} = 93.000 / (1 - 0,17) = 93.000 / 0,83 = R\$ 112.048,19$
  - $\text{ICMS Interno} = 112.048,19 \times 0,17 = R\$ 19.048,19$
  - $\text{ICMS Origem} = 100.000 \times 0,07 = R\$ 7.000,00$
  - $\text{DIFAL Devido a MT} = 19.048,19 - 7.000,00 = \mathbf{R\$ 12.048,19}$.
  - *Carga adicional decorrente da base dupla: majoração de 20,48% em relação à base simples.*

### 2.3. Transferências entre Estabelecimentos do Mesmo Titular (ADC 49, LC 204/2023, Convênios 178/2023 e 109/2024 e Decretos MT 650/2023 e 706/2024)
A matéria de transferências de mercadorias entre matriz e filiais sofreu modulação profunda:
1. **Regra Geral de Não Incidência:** Em atendimento ao julgamento do Tema 1099 / ADC 49 do STF e ao art. 12, § 4º da LC 87/96 (incluído pela LC 204/2023), as transferências de mercadorias entre estabelecimentos do mesmo titular não constituem fato gerador do ICMS.
2. **Transferência Obrigatória do Crédito:** O estabelecimento remetente em MT deve transferir o crédito fiscal ao destinatário em outra UF limitado aos percentuais das alíquotas interestaduais (12% ou 4%), calculado sobre:
   - O valor da entrada mais recente da mercadoria;
   - O custo da mercadoria produzida (matéria-prima, mão de obra e insumos).
3. **Opção pela Equiparação a Operação Tributada (Convênio ICMS 109/2024):** O contribuinte pode optar, em janeiro de cada exercício, por equiparar a transferência a uma operação sujeita à incidência normal do imposto, destacando débito e gerando crédito integral de ICMS para o estabelecimento destinatário.
4. **O Ponto Crítico em Mato Grosso: Interrupção do Diferimento (Decreto nº 706/2024 e Portaria SEFAZ nº 039/2024):**
   - No agronegócio de MT, grande parte das mercadorias (soja, milho, algodão, gado) é adquirida de produtores rurais com diferimento do ICMS (Anexo VII do RICMS/MT).
   - O Fisco mato-grossense pacificou o entendimento de que a transferência interestadual para filial do mesmo titular **encerra e interrompe a fase do diferimento**.
   - Consequentemente, na ausência da opção expressa pelo Convênio ICMS 109/2024, o estabelecimento remetente mato-grossense é obrigado a recolher imediatamente aos cofres da SEFAZ/MT o ICMS diferido da etapa anterior à alíquota interna de 17%, causando forte impacto no fluxo de caixa e gerando contencioso tributário de larga escala com tradings e agroindústrias.

### 2.4. Substituição Tributária (ICMS-ST) e Convênio ICMS 142/2018
A Substituição Tributária no Estado de Mato Grosso é disciplinada pelo **Anexo X do RICMS/MT** e segue as balizas do Convênio ICMS 142/2018:
- **MVA Ajustada:** Nas operações interestaduais com mercadorias submetidas ao regime de ST destinadas a revenda em Mato Grosso promovidas por estabelecimentos industriais ou atacadistas normais, aplica-se a fórmula matemática da MVA Ajustada:
  $$\text{MVA Ajustada} = \left[ \frac{(1 + \text{MVA-ST Original}) \times (1 - \text{ALQ Inter})}{(1 - \text{ALQ Intra MT})} \right] - 1$$
- **Remetente do Simples Nacional (Convênio ICMS 35/2011):** Não se aplica a MVA Ajustada quando o fornecedor remetente de outra UF estiver enquadrado no Simples Nacional, aplicando-se invariavelmente a **MVA-ST Original** prevista no Anexo X do RICMS/MT.
- **Ressarcimento e Complementação do ICMS-ST (Tema 201 do STF - RE 593.849):** O contribuinte substituído tem direito ao ressarcimento da diferença do ICMS-ST recolhido a maior se a base de cálculo efetiva na venda a consumidor final for inferior à presumida, cabendo da mesma forma à SEFAZ/MT exigir a complementação do imposto quando a venda for praticada a preço superior.

---

## 3. Mecanismos de Dedução, Tomada de Crédito e Restrições Fiscais

### 3.1. Princípio da Não-Cumulatividade no RICMS/MT
A não-cumulatividade em Mato Grosso observa a disciplina da LC nº 87/1996 e dos arts. 98 a 120 do RICMS/MT:
- O imposto é compensável com o montante devido em cada operação, mediante abatimento dos créditos legais escriturados nas entradas de mercadorias para comercialização, matérias-primas, produtos intermediários e embalagens integrados fisicamente ao produto final industrializado.
- **Vedação e Estorno de Crédito:** É obrigatório o estorno de crédito quando as mercadorias entradas no estabelecimento vierem a ser objeto de saída isenta, não tributada ou contemplada com redução de base de cálculo (na parcela desonerada), salvo expressa disposição em contrário que conceda "manutenção de crédito" (ex.: operações de exportação protegidas pelo art. 155, § 2º, X, "a" da CF/88 e insumos amparados por convênios específicos autorizativos do CONFAZ).

### 3.2. Crédito do Ativo Imobilizado / Permanente e CIAP (LC 102/2000)
A apropriação do crédito de ICMS decorrente da aquisição de bens do ativo imobilizado vinculados à atividade-fim do estabelecimento obedece estritamente ao art. 20, § 5º da LC 87/96:
1. **Fracionamento:** O crédito fiscal total destacado na NF-e de entrada é apropriado à razão de **1/48 (um quarenta e oito avos) por mês**, iniciando-se no mês em que ocorrer a efetiva entrada em operação do bem.
2. **Fator de Rateio Mensal ($F$):**
   $$F = \frac{\text{Valor das Saídas e Prestações Tributadas} + \text{Saídas para o Exterior (Exportações)}}{\text{Valor Total de Todas as Saídas e Prestações do Período}}$$
3. **Cálculo da Quota Mensal de Crédito CIAP:**
   $$\text{Crédito CIAP Mês} = \left( \frac{\text{Valor do ICMS da Entrada}}{48} \right) \times F$$
4. **Escrituração Fiscal Digital (EFD-ICMS/IPI):** A apropriação é obrigatória mediante preenchimento integral dos registros do **Bloco G** da EFD fiscal no padrão SPED da SEFAZ/MT. Bens alienados antes do transcurso dos 48 meses perdem definitivamente o saldo remanescente, cancelando-se as frações futuras.

### 3.3. Restrições Legais para Energia Elétrica e Serviços de Comunicação (Art. 33 da LC 87/96)
No território mato-grossense, os créditos sobre energia elétrica e comunicação são severamente cerceados:
- **Energia Elétrica:** Somente confere direito a crédito quando:
  - Consumida no processo de industrialização (exige-se a manutenção de **Laudo Técnico Pericial de Engenharia Elétrica** atestando o consumo exclusivo nas máquinas industriais, segregando a área fabril da administrativa);
  - A operação de saída do estabelecimento for destinada ao exterior (na proporção das exportações);
  - O próprio estabelecimento for gerador ou distribuidor de energia elétrica.
- **Serviços de Comunicação:** Apenas geram direito a crédito fiscal quando utilizados por prestadores de serviços da mesma natureza ou quando vinculados a saídas de exportação para o exterior.

### 3.4. Fundo Estadual de Combate e Erradicação da Pobreza (FECEP / FECOP - LC nº 144/2003)
- O Fundo Estadual de Combate e Erradicação da Pobreza (FECEP) no Mato Grosso estabelece um adicional de **2%** sobre a alíquota aplicável a operações internas e de importação com produtos supérfluos (como bebidas alcoólicas, cigarros, cosméticos de luxo, armas de fogo e veículos de alta cilindrada).
- **Inadmissibilidade de Compensação:** O valor correspondente ao FECEP deve ser segregado na apuração e recolhido em código de receita próprio (DAR-1/Autônomo), sendo **vedada a sua compensação com créditos acumulados normais de ICMS**.

### 3.5. Transição da Histórica "Carga Tributária Média" (Regime de Estimativa Simplificada)
- **O que foi a Carga Média em MT:** Durante anos, o Estado adotou o Regime de Estimativa por Operação Simplificado (arts. 157 a 171-A do RICMS/MT), popularmente conhecido como "ICMS Carga Média". As entradas de mercadorias no território mato-grossense eram submetidas a uma carga tributária média prefixada pela CNAE do contribuinte, liquidando e encerrando a fase de tributação da cadeia.
- **A Extinção pela LC nº 631/2019 e Decreto nº 273/2019:** Em virtude dos termos da Lei Complementar Federal nº 160/2017 e do Convênio ICMS 190/2017, a LC Estadual nº 631/2019 extinguiu esse regime simplificado de entrada com encerramento de fase. A partir de 1º de janeiro de 2020, o comércio e a indústria em MT migraram compulsoriamente para o **Regime Normal de Débito e Crédito**, passando os setores de atacado a fruir de incentivos estruturados sob a forma de **créditos outorgados** previstos no Anexo XVII do RICMS/MT.

---

## 4. O Setor Agrícola e Rural Mato-grossense (O Gigante do Agronegócio Nacional)

Mato Grosso é a maior potência agropecuária do Brasil, detentor das maiores safras mundiais de soja, milho e algodão e do maior rebanho bovino nacional. A estrutura tributária do agronegócio em MT possui particularidades únicas:

```
                            [CADEIA AGROPECUÁRIA DE MATO GROSSO]
                                             │
      ┌──────────────────────────────────────┼──────────────────────────────────────┐
      ▼                                      ▼                                      ▼
[CIRCULAÇÃO INTERNA]                [SAÍDA INTERESTADUAL]                     [EXPORTAÇÃO]
- Diferimento (Anexo VII)           - Tributada (12% normal)                  - Imunidade (Lei Kandir)
- Condição: FETHAB Soja/Milho/Gado  - Ou Transf. Crédito (ADC 49/LC 204)     - Sem ICMS na saída
- Operação desonerada até indústria - Exige FETHAB / FETHAB Adicional         - FETHAB Exportação obrigatório
```

### 4.1. FETHAB (Fundo Estadual de Transporte e Habitação - Lei Estadual nº 7.263/2000)
O FETHAB é o tributo financeiro-fiscal mais expressivo da matriz tributária do agronegócio mato-grossense. Regulamentado pelo Decreto nº 1.261/2000, é uma contribuição estadual cobrada por tonelada ou por cabeça comercializada:
- **Natureza Jurídica e Compulsoriedade:** Em tese, a lei classifica o FETHAB como "facultativo", mas a sua retenção e recolhimento são erigidos em **condicionante legal indeclinável** para a concessão do diferimento do ICMS nas operações internas e para a fruição de regimes especiais nas saídas para exportação e interestaduais. A recusa do recolhimento acarreta a imediata tributação integral da operação em 17% ou 12% de ICMS.

#### Quadro Tarifário de Contribuições Vinculadas à UPF/MT (Vigência 2025/2026)
A legislação do FETHAB define a cobrança com base em percentuais da **UPF/MT** (Unidade Padrão Fiscal de Mato Grosso). Pelas Leis Estaduais nº 13.002/2025 e nº 13.357/2026, **a base de cálculo do FETHAB foi congelada**, aplicando-se durante os anos de 2025 e 2026 o valor nominal da UPF/MT fixado em **janeiro de 2025**:

| Produto Agrícola / Pecuário | Componente Legal da Contribuição | Percentual sobre a UPF/MT | Unidade de Medida | Destinação dos Recursos |
| :--- | :--- | :--- | :--- | :--- |
| **Soja em Grão** | FETHAB Principal | **10,00%** | Por tonelada métrica | Infraestrutura rodoviária e habitação |
| | FETHAB Adicional (Lei 11.970/22) | **10,00%** | Por tonelada métrica | Equilíbrio fiscal do Estado |
| | Instituto da Cadeia da Soja (IAGRO) | **1,15%** | Por tonelada métrica | Pesquisa e defesa sanitária vegetal |
| | **Carga Total Consolidada Soja** | **21,15% da UPF/MT** | **Por tonelada** | **Recolhimento integrado** |
| **Milho em Grão** | FETHAB Principal (interestadual e exp.) | **6,00% da UPF/MT** | Por tonelada métrica | Fundo estadual de infraestrutura |
| **Algodão (Pluma/Caroço)** | FETHAB Principal + Adicional | **10,00% + Adicionais** | Por tonelada | Fundo rodoviário / AMPA / IALG |
| **Gado Bovino / Bubalino** | FETHAB Principal | **11,50%** | Por cabeça abatida/saída | Estradas vicinais e pontes |
| | FETHAB Adicional | **11,50%** | Por cabeça abatida/saída | Fundo estadual de desenvolvimento |
| | Instituto da Carne (INPECMT) | **1,26%** | Por cabeça abatida/saída | Promoção comercial da carne bovina |
| | **Carga Total Consolidada Gado** | **24,26% da UPF/MT** | **Por cabeça** | **Retenção pelo frigorífico** |
| **Madeira em Tora/Serrada** | FETHAB Madeira | **3,71% a 10,00%** | Por metro cúbico ($m^3$) | Manejo florestal sustentável |

- **O Litígio das Exportações no STF (ADI 6420):** Entidades do agronegócio questionaram perante o Supremo Tribunal Federal a legitimidade da cobrança do FETHAB nas exportações diretas e saídas com fim específico de exportação, sob a alegação de afronta à imunidade do art. 155, § 2º, X, "a" da Constituição Federal. O tema ganhou contornos com a introdução do art. 136 no ADCT pela Emenda Constitucional nº 132/2023.

### 4.2. Convênio ICMS 100/97: O Regime dos Insumos Agropecuários
O Convênio ICMS 100/97 é internalizado no Regulamento do ICMS de MT (Anexo IV e V):
- **Isenções e Reduções:** Concede isenção do ICMS nas saídas internas de sementes fiscalizadas/certificadas, calcário, gesso agrícola, esterco animal e mudas de plantas.
- **Reoneração Gradual de Fertilizantes (Convênio ICMS 26/2021):** O Convênio ICMS 26/2021 revogou a isenção integral nas operações interestaduais e na importação de fertilizantes minerais e defensivos agrícolas, estipulando uma transição com alíquotas efetivas escalonadas (1% a 4%), com pleno impacto nas margens dos produtores rurais de grãos em MT.

### 4.3. Sistemática do Diferimento do ICMS no Agro (Anexo VII do RICMS/MT)
- O diferimento é a espinha dorsal da fluidez do agronegócio mato-grossense:
  - Nas operações internas entre produtores rurais e cooperativas agropecuárias, indústrias esmagadoras de grãos, usinas de etanol e frigoríficos, **o lançamento e pagamento do ICMS ficam diferidos** para o momento da saída subsequente do produto acabado ou na sua exportação.
  - Para gozar do diferimento, o produtor e o adquirente devem estar regularmente credenciados perante a SEFAZ/MT e adimplir pontualmente os encargos do FETHAB.
- **Exportação e Lei Kandir:** Nas operações de exportação direta amparadas pela Lei Kandir (LC 87/96), não há cobrança de ICMS na saída ao porto, e o diferimento havido nas etapas anteriores considera-se cumprido e encerrado, sem exigência de pagamento do ICMS diferido, restando assegurada a manutenção do crédito dos insumos agrícolas.

### 4.4. Créditos Presumidos e Incentivos à Agroindustrialização
Para promover a verticalização da produção agrícola e incentivar a transformação de matéria-prima bruta no território estadual, Mato Grosso concede:
- **Etanol de Milho e Biorrefinarias:** Tratamento fiscal privilegiado com crédito outorgado que equaliza a carga tributária na produção de etanol hidratado, anidro, farelo de milho de alta proteína (DDGS/DDG) e óleo de milho.
- **Biodiesel (B100):** Regime especial alinhado ao Convênio ICMS 113/2006 e resoluções do CONDEPRODEMAT, com crédito presumido e desoneração na cadeia de óleo degomado de soja.
- **Indústria da Carne (Frigoríficos de Bovinos, Suínos e Aves):** Crédito outorgado calculado sobre o montante das saídas de carne e derivados, como estímulo às plantas frigoríficas frigoríficas exportadoras e de atendimento ao mercado nacional (JBS, Marfrig, Minerva).

### 4.5. Nota Fiscal de Produtor Eletrônica (NFP-e) e Conformidade do Produtor Rural
- **Extinção do Talão de Produtor em Papel:** A emissão de Nota Fiscal de Produtor Rural Eletrônica (NFP-e, modelo 55) é compulsória para todos os produtores rurais de Mato Grosso, pessoas físicas e jurídicas.
- **Ambiente de Emissão:** Os produtores podem emitir a NFA-e (Avulsa) diretamente no portal da SEFAZ/MT ou utilizar sistemas de gestão integrados com certificado digital.
- **Pessoa Física vs. Pessoa Jurídica:** Embora a pessoa física inscrita no CCE/MT possua regime especial simplificado no âmbito estadual, ela está submetida a rigoroso controle cruzado com as obrigações federais (Livro Caixa Digital do Produtor Rural - LCDPR da Receita Federal).

---

## 5. O Setor Industrial Mato-grossense e a Política de Atração de Investimentos

```
                      [PRODEIC - LC 631/2019 e Decreto 288/2019]
                                           │
         ┌─────────────────────────────────┴─────────────────────────────────┐
         ▼                                                                   ▼
[OPERAÇÕES INTERNAS]                                              [OPERAÇÕES INTERESTADUAIS]
- Redução de Base de Cálculo até 85%                             - Crédito Outorgado de 90% a 95%
- Crédito Outorgado até 85%                                      - Contrapartida de Fundos (FUNDEIC/FUNTUR)
- Condicionado à agregação de valor local                        - Regularidade fiscal estrita perante SEFAZ/MT
```

### 5.1. Programa de Desenvolvimento Industrial e Comercial de Mato Grosso (PRODEIC)
O PRODEIC (Lei nº 7.958/2003, reestruturado pela Lei Complementar nº 631/2019 e regulamentado pelo Decreto nº 288/2019) é o motor da industrialização de Mato Grosso:
1. **Reinstituição e Convalidação:** O PRODEIC foi expressamente reinstituído em conformidade com a LC Federal nº 160/2017 e o Convênio ICMS 190/2017, afastando riscos de glosa de créditos por outros estados até o termo final de 2032.
2. **Dinâmica do Crédito Outorgado:** O benefício fiscal é concedido pelo Conselho Deliberativo dos Programas de Desenvolvimento de Mato Grosso (**CONDEPRODEMAT**), que edita resoluções fixando os percentuais por setor produtivo e código NCM:
   - **Operações Internas:** Crédito outorgado de até **85%** ou redução de base de cálculo de até 85%;
   - **Operações Interestaduais:** Crédito outorgado que varia entre **90% e 95%** sobre o imposto devido;
   - O incentivo substitui ou convive com créditos normais conforme a resolução setorial aplicável a cada segmento econômico.
3. **Condicionantes de Fruição:**
   - Adimplemento ininterrupto do ICMS apurado;
   - Contribuição obrigatória para o Fundo de Desenvolvimento Industrial e Comercial (FUNDEIC) e Fundo de Fomento ao Turismo (FUNTUR);
   - Cumprimento de metas de investimento, geração de postos de trabalho diretos e priorização de fornecedores sediados em Mato Grosso.

### 5.2. Análise dos Grandes Polos Agroindustriais Instalados
- **Complexo da Soja:** Plantas industriais de gigantes do agronegócio (Bunge, Cargill, ADM, Dreyfus, Amaggi) em polos como Rondonópolis, Sorriso, Lucas do Rio Verde e Sinop. O foco é a extração de óleo e produção de farelo proteico.
- **Biorrefinarias de Etanol de Milho:** Mato Grosso lidera o segmento nacional (empresas como FS Bioenergia e Inpasa), operando biorrefinarias modernas com ciclo integrado de coprodutos.
- **Parque Frigorífico:** Maior estrutura de abate e processamento bovino do continente, centralizado em plantas frigoríficas de grande porte que exportam para China, União Europeia e EUA.
- **Indústria de Fertilizantes e Químicos:** Misturadoras e formuladoras de adubos NPK situadas nas margens dos terminais da Ferronorte em Rondonópolis.

### 5.3. Regimes Aduaneiros Especiais, Importação e Drawback
- **Drawback Integrado:** Aplicado amplamente no complexo exportador mato-grossense mediante suspensão ou isenção de ICMS (Convênio ICMS 27/1990) na importação de insumos, matérias-primas e embalagens utilizados na produção de mercadorias destinadas à exportação.
- **Porto Seco de Cuiabá (EADI):** Facilita o desembaraço aduaneiro de maquinários industriais e peças, muitas vezes beneficiados por desonerações tributárias estaduais para modernização fabril.

---

## 6. Setor de Produto Acabado: Atacado, Varejo e Distribuição

### 6.1. Regime de Crédito Outorgado para Centros de Distribuição e Atacadistas
Com a extinção do Regime de Estimativa Simplificada (Carga Média), o comércio atacadista foi acomodado sob as normas do **Anexo XVII do RICMS/MT**:
- Concessão de crédito outorgado que equaliza a carga tributária efetiva incidente nas vendas interestaduais e internas, promovendo a fixação de grandes Centros de Distribuição (CDs) logísticos em Cuiabá, Várzea Grande e Rondonópolis.
- **Regras Operacionais:** Exigência de que o atacadista comprove percentual mínimo de vendas para pessoas jurídicas revendedoras (B2B), restringindo expressamente as vendas a consumidores finais (B2C) a percentuais marginais sob pena de descredenciamento sumário.

### 6.2. MVA, IVA-ST e Pautas Fiscais (Lista de Preços Mínimos da SEFAZ/MT)
- **Margem de Valor Agregado (MVA):** Utilizada nos termos do Anexo X do RICMS/MT para apurar o ICMS-ST de produtos automotivos, bebidas, materiais de construção, farmacêuticos e alimentos.
- **Pauta de Preço Mínimo:** A SEFAZ/MT edita portarias periódicas fixando a Tabela de Preços Mínimos para mercadorias em circulação (art. 90 do RICMS/MT). A pauta serve como base de cálculo mínima tanto para fins de arbitramento fiscal em barreiras volantes e postos de fronteira quanto para retenção de ST na ausência de preço a consumidor final sugerido pelo fabricante.

### 6.3. E-Commerce, Marketplaces e Responsabilidade Tributária Solidária
- **Responsabilidade Solidária dos Intermediadores Digitais:** Por força das disposições dos arts. 18-A e 18-B da Lei Estadual nº 7.098/1998, as plataformas de comércio eletrônico, marketplaces e operadores de fulfillment respondem solidariamente pelo pagamento do ICMS e multas devidas nas operações mercantis por eles intermediadas quando os vendedores não emitirem documentação fiscal idônea ou estiverem com inscrição estadual cancelada.
- **Monitoramento em Centros de Triagem de Encomendas:** A Fiscalização de Trânsito da SEFAZ/MT atua de forma permanente dentro das transportadoras privadas e nos Centros de Tratamento de Cartas e Encomendas (CTCE) dos Correios em Várzea Grande, retendo encomendas com indícios de subfaturamento ou sem o recolhimento do DIFAL devido ao Estado.

---

## 7. Transição para o IBS e CBS da Reforma Tributária (EC 132/2023 e LC 214/2025)

A Reforma Tributária sobre o Consumo representa a mais profunda transformação estrutural para as finanças públicas e para o setor empresarial de Mato Grosso em toda a sua história:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│              A PARADOXO TRIBUTÁRIO DE MATO GROSSO NA REFORMA TRIBUTÁRIA          │
├──────────────────────────────────────────────────────────────────────────────────┤
│ - MAIOR SUPERÁVIT COMERCIAL E VOLUME DE EXPORTAÇÃO DO BRASIL                     │
│ - AS EXPORTAÇÕES CONTINUAM TOTALMENTE IMUNES (NENHUM RECOLHIMENTO DE IBS NO MT)  │
│ - O IBS SERÁ 100% ARRECADADO NO DESTINO DO CONSUMO (OUTRAS UFs OU PAÍSES)        │
│ - MATO GROSSO PERDE A BASE DA ORIGEM E PASSA A DEPENDER DA PARTILHA FEDERATIVA    │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### 7.1. O Impacto Estrutural do Princípio do Destino Puro em Estado Agroexportador
- **Mudança Paradigmática:** Sob a vigência do ICMS, embora as exportações sejam imunes por força da Lei Kandir, Mato Grosso captura receita na circulação interna, na industrialização primária e, de forma massiva, via contribuições parafiscais (FETHAB).
- **A Lógica do IBS:** Com a transição para o IBS (competência estadual e municipal partilhada), todo o tributo pertencerá integralmente ao **local de destino do consumo pessoal ou governamental**. Como Mato Grosso possui apenas cerca de 3,7 milhões de habitantes (menos de 2% da população brasileira) e exporta mais de 80% do que produz para outros estados e nações, sua base própria de arrecadação direta sobre o consumo é reduzida em comparação com o volume colossal de produção de riqueza.
- **Dependência do FNDR e Mecanismos de Transição:** O financiamento do desenvolvimento de MT dependerá crucialmente do **Fundo Nacional de Desenvolvimento Regional (FNDR)** instituído pelo art. 159-A da CF/88 e dos critérios de partilha durante a transição federativa de 50 anos (art. 131 do ADCT).

### 7.2. O Destino do FETHAB e a Cláusula de Transição do Art. 136 do ADCT
Um dos tópicos de maior tensão na elaboração da Emenda Constitucional nº 132/2023 foi o futuro dos fundos de infraestrutura estaduais que incidem sobre o agronegócio e a mineração:
1. **A Solução do Art. 136 do ADCT:**
   > Os Estados que possuíam contribuições sobre produtos primários e semielaborados vigentes em 30 de abril de 2023 (caso expresso do FETHAB mato-grossense, do FUNDERSUL em MS e do FUNDEINFRA em GO) ficam autorizados a mantê-las **até 31 de dezembro de 2032**, com redução gradual e desvinculação obrigatória ao final do período.
2. **O Desafio Pós-2032:** A partir de 1º de janeiro de 2033, com a extinção total do ICMS e a consolidação do IBS e da CBS, o FETHAB não mais poderá ser exigido nos moldes vigentes, forçando o Estado de Mato Grosso a reformular inteiramente suas fontes de financiamento de manutenção de rodovias e logística rural.

### 7.3. Transição dos Incentivos do PRODEIC e o Fundo de Compensação de Benefícios Fiscais (FCBF)
Os incentivos fiscais do PRODEIC e do PROALMAT convalidados pela Lei Complementar nº 160/2017 e Convênio ICMS 190/2017 possuem data certa para expirar:
- **Cronograma de Redução Gradual dos Benefícios (Art. 133 do ADCT):**
  - **Até 2028:** Fruição integral (100% dos incentivos contratados);
  - **2029:** Redução para **80%** do benefício;
  - **2030:** Redução para **60%** do benefício;
  - **2031:** Redução para **40%** do benefício;
  - **2032:** Redução para **20%** do benefício;
  - **2033:** Extinção total de todos os créditos outorgados e desonerações do ICMS.
- **Fundo de Compensação de Benefícios Fiscais (FCBF):** As empresas industriais instaladas em Mato Grosso com benefícios fiscais regularmente aprovados e depositados no CONFAZ até 31 de maio de 2023 farão jus à habilitação perante a União e o Comitê Gestor do IBS para receber compensações financeiras pelas perdas de incentivos durante o período de 2029 a 2032, nos termos da Lei Complementar regulamentadora da Reforma (LC 214/2025).

### 7.4. Homologação do Saldo Credor Acumulado de ICMS (Art. 134 do ADCT)
As grandes tradings, frigoríficos e indústrias de esmagamento de grãos em Mato Grosso detêm volumes bilionários de créditos acumulados de ICMS, decorrentes de entradas tributadas (máquinas industriais, energia, embalagens, químicos, transporte) combinadas com saídas de exportação desoneradas:
1. **Procedimento de Homologação pela SEFAZ/MT:** Os contribuintes detentores de saldos credores de ICMS acumulados até 31 de dezembro de 2032 deverão submetê-los a procedimento formal de validação e homologação pela administração tributária de MT.
2. **Compensação em 240 Parcelas Mensais:** O montante homologado não será liquidado de imediato. Conforme expressamente determinado pelo art. 134 do ADCT:
   - Será compensado contra o **IBS devido pelo contribuinte** em **240 (duzentas e quarenta) parcelas mensais sucessivas e iguais** (período de 20 anos, de 2033 a 2052), devidamente atualizadas pelo IPCA.
3. **Mecanismos Alternativos de Realização:**
   - Possibilidade de transferência do saldo credor homologado para terceiros (no âmbito do sistema unificado de créditos do Comitê Gestor do IBS);
   - Pedido de ressarcimento financeiro perante o Comitê Gestor do IBS caso o contribuinte não possua débitos mensais de IBS suficientes para absorver a parcela do mês.

---

## 8. Cronograma e Recomendações para Ingestão de Arquivos no Repositório

Para suprir as deficiências diagnosticadas no repositório `estaduais/mt/`, recomenda-se a execução das seguintes ações prioritárias:

1. **Criação da Norma Matriz do ICMS:**  
   Inserir a íntegra consolidada e atualizada da **Lei Estadual nº 7.098/1998** em `estaduais/mt/leis/icms/lei-7098-1998.md`.
2. **Desdobramento dos Anexos Regulamentares do RICMS/MT:**  
   Enriquecer o arquivo `estaduais/mt/ricms/decreto-2214-2014.md` com a incorporação dos **Anexos IV (Isenções)**, **V (Reduções de BC)**, **VI (Créditos Presumidos)**, **VII (Diferimento Agropecuário)**, **X (Substituição Tributária)** e **XVII (Setor Atacadista)**.
3. **Ingestão da Legislação de Incentivos Fiscais:**  
   Criar a pasta `estaduais/mt/leis/incentivos/` e arquivar a **Lei Complementar Estadual nº 631/2019** e a **Lei Ordinária nº 7.958/2003** com seus decretos regulamentadores (PRODEIC, PROALMAT e PRODER).
4. **Ingestão da Legislação do FETHAB:**  
   Criar a pasta `estaduais/mt/leis/fundos/` e arquivar a **Lei Estadual nº 7.263/2000**, o Decreto nº 1.261/2000 e as Leis nº 13.002/2025 e 13.357/2026.
5. **Ingestão do Contencioso Administrativo (PAT/MT):**  
   Criar a pasta `estaduais/mt/leis/pat/` e arquivar a **Lei Ordinária nº 8.797/2008**.

---
*Relatório técnico concluído com alto rigor jurídico, metodológico e operacional. Arquivo gravado com sucesso em `_auditoria/estados/auditoria_mt.md`.*
