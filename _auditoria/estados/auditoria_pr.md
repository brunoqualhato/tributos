# AUDITORIA TRIBUTÁRIA ESTATAL APROFUNDADA: ESTADO DO PARANÁ (PR)
**Data de Emissão:** Outubro de 2026  
**Auditor Responsável:** Auditor Tributarista Especialista em Legislação Tributária do Estado do Paraná  
**Unidade Federativa:** Paraná (PR) | Região Sul  
**Escopo:** Auditoria do Acervo Normativo Local, Relações Interestaduais, Tributação Setorial (Agropecuária, Indústria e Portos, Atacado e Varejo) e Transição para o Novo Sistema Tributário Nacional (IBS/CBS - EC 132/2023 e LC 214/2025)

---

## SUMÁRIO EXECUTIVO

O Estado do Paraná constitui uma das economias mais dinâmicas e diversificadas do Brasil, combinando um modelo cooperativista agroindustrial líder na América Latina, um robusto parque industrial metalmecânico, petroquímico e automotivo, e uma infraestrutura portuária de alta relevância (Porto Dom Pedro II em Paranaguá e Porto de Antonina). Sob a perspectiva estritamente tributária, o Paraná consolidou uma ordem normativa altamente sofisticada centrada na **Lei Orgânica do ICMS (Lei Estadual nº 11.580/1996)** e no **Regulamento do ICMS (RICMS/PR, aprovado pelo Decreto Estadual nº 7.871/2017)**.

A presente auditoria técnica identificou:
1. **Divergências e Lacunas Graves no Repositório Documental:** O repositório local em `estaduais/pr/` apresenta severas omissões normativas: ausência do texto legal da Lei nº 11.580/1996; versão do Decreto nº 7.871/2017 truncada em apenas 89 linhas (omissão de todos os 13 Anexos fundamentais, em especial o Anexo VIII de Diferimento e Anexo IX de Substituição Tributária); ausência da Lei de regência do Processo Administrativo Fiscal (PAF) e do Conselho de Contribuintes e Recursos Fiscais (CCRF) — que consiste juridicamente na **Lei Estadual nº 18.877/2016** (com alterações das Leis 20.389/2020 e 21.961/2024), não na Lei 20.890/2021 (que é toponímica); e ausência da legislação do Programa Paraná Competitivo (Leis nº 14.985/2006 e 15.467/2007 e Decretos nº 6.434/2017 e 7.721/2024).
2. **Atualização da Alíquota Geral Interna:** Vigência da alíquota modal interna de **19,5%**, implementada pela **Lei Estadual nº 21.850/2023** com eficácia a partir de 18/03/2024, acrescida do adicional de **2% do FECOP (Fundo Estadual de Combate à Pobreza)** para bens supérfluos, regido pelo Título I da Lei nº 18.573/2015.
3. **Mecanismo de Diferimento Parcial:** Existência do instituto específico do diferimento parcial (Art. 28 do Anexo VIII do RICMS/PR), que desonera as etapas intermediárias internas entre contribuintes mediante diferimento de 38,46% do imposto, equalizando a carga tributária interna a 12%.
4. **Vanguarda em Controle de Créditos:** Destaque para o sistema eletrônico **SISCRED/PR**, mecanismo de habilitação e circulação de créditos acumulados do ICMS (Arts. 51 a 61 do RICMS/PR e NPF nº 092/2012), que servirá de alicerce para a homologação dos créditos para compensação com IBS em 240 meses (art. 134 do ADCT).

---

## 1. AUDITORIA DO ACERVO NORMATIVO DO PARANÁ (`estaduais/pr/`)

### 1.1. Inventário Físico do Diretório `estaduais/pr/`
A varredura estrita realizada na estrutura de pastas revelou o seguinte status documental:

| Arquivo / Caminho | Tamanho | Ementa Declarada | Diagnóstico de Integridade |
| :--- | :--- | :--- | :--- |
| `estaduais/pr/ricms/decreto-7871-2017.md` | 10.241 bytes (89 linhas) | Aprova o RICMS/PR disciplinando alíquotas internas, DIFAL, ST e operações interestaduais. | **CRÍTICO / INCOMPLETO:** Trata-se de um resumo sintético de 89 linhas. O Regulamento oficial do Paraná contém mais de 600 artigos no corpo permanente e **13 Anexos operacionais** (com centenas de artigos sobre isenções, reduções de base de cálculo, créditos outorgados, diferimento e regimes especiais). |
| `estaduais/pr/leis/itcmd/lei-18573-2015.md` | 48.360 bytes (842 linhas) | Dispõe sobre o ITCMD no Estado do Paraná. | **PARCIALMENTE INTEGRAL:** O arquivo cobre com boa fidelidade o Título II da lei (ITCMD), mas omite o Título I, que instituiu formalmente o **FECOP (Fundo Estadual de Combate à Pobreza do Paraná)**. |
| `estaduais/pr/leis/ipva/lei-14260-2003.md` | 98.235 bytes (1.659 linhas) | Lei Orgânica do IPVA no Estado do Paraná. | **CONFORME:** Texto integral compilado com histórico de alterações até 2024/2025. |

### 1.2. Mapeamento de Normas Paranaenses Faltantes no Repositório

Para garantir a higidez da base jurídica e permitir tomadas de decisão consultivas e contenciosas de alta fidelidade, foram mapeadas as seguintes lacunas absolutas:

```
ESTADUAIS/PR/ (LACUNAS NORMATIVAS CRÍTICAS)
├── leis/
│   ├── icms/
│   │   └── lei-11580-1996.md                 <-- [FALTANTE CRÍTICO: Lei Orgânica do ICMS/PR]
│   ├── pat_ccrf/
│   │   ├── lei-18877-2016.md                 <-- [FALTANTE CRÍTICO: Lei Orgânica do PAF e CCRF]
│   │   └── resolucao-sefa-610-2017.md        <-- [FALTANTE: Regimento Interno do CCRF]
│   └── incentivos/
│       ├── lei-14985-2006.md                 <-- [FALTANTE: Regime Portuário de Importação]
│       └── lei-15467-2007.md                 <-- [FALTANTE: Ajustes de Importação Rodoviária e Cesta Básica]
├── ricms/
│   └── anexos/                               <-- [FALTANTE CRÍTICO: Anexos I a XIII do Dec. 7.871/2017]
│       ├── anexo-01-isencoes.md
│       ├── anexo-02-reducao-bc.md
│       ├── anexo-03-credito-presumido.md
│       ├── anexo-08-diferimento.md           <-- [VITAL: Art. 28 - Diferimento Parcial e Agropecuária]
│       └── anexo-09-substituicao-trib.md     <-- [VITAL: Setores Sujeitos à ST e MVA]
└── decretos_programas/
    ├── decreto-6434-2017.md                  <-- [FALTANTE: Programa Paraná Competitivo - Marco Histórico]
    └── decreto-7721-2024.md                  <-- [FALTANTE: Programa Paraná Competitivo - Regulamento Vigente]
```

#### Esclarecimento Técnico Preambular sobre a "Lei do PAT/CCR":
O levantamento preliminar indicava questionamento sobre a "Lei 20.890/2021". Esclarece-se peremptoriamente que a **Lei nº 20.890, de 02/12/2021**, no ordenamento estadual do Paraná, destina-se única e exclusivamente a denominar viaduto na rodovia BR-369 (norma toponímica/honorífica). O diploma basilar do **Processo Administrativo Fiscal (PAF)** e de estruturação do **Conselho de Contribuintes e Recursos Fiscais (CCRF/PR)** é a **Lei Estadual nº 18.877, de 27 de setembro de 2016**, atualizada substancialmente pela **Lei nº 20.389/2020** (reexame necessário em UPF/PR, admissibilidade recursal) e pela **Lei nº 21.961/2024**, cuja disciplina procedimental é regulamentada pela **Resolução SEFA nº 610/2017**.

---

## 2. RELACIONAMENTO DO ICMS-PR COM OS DEMAIS 26 ESTADOS E DISTRITO FEDERAL

O Paraná situa-se geograficamente na Região Sul. Sua posição no federalismo fiscal impõe o cumprimento rigoroso da regra de assimetria interestadual das Resoluções do Senado Federal.

```
                    ┌────────────────────────────────────────────────────────┐
                    │               ESTADO DO PARANÁ (PR)                    │
                    │               Alíquota Geral Interna: 19,5%            │
                    │               (+2% FECOP bens supérfluos)              │
                    └───────────────────────────┬────────────────────────────┘
                                                │
         ┌──────────────────────────────────────┼──────────────────────────────────────┐
         ▼                                      ▼                                      ▼
┌─────────────────────────┐        ┌─────────────────────────┐        ┌─────────────────────────┐
│     N, NE, CO e ES      │        │      Sul e Sudeste      │        │  Bens Importados (>40%) │
│    Alíquota: 7%         │        │    (RS, SC, SP, RJ, MG) │        │     Alíquota: 4%        │
│  (Res. SF nº 22/1989)   │        │      Alíquota: 12%      │        │  (Res. SF nº 13/2012)   │
└─────────────────────────┘        │  (Res. SF nº 22/1989)   │        └─────────────────────────┘
                                   └─────────────────────────┘
```

### 2.1. Alíquotas Interestaduais Aplicáveis
Conforme art. 155, § 2º, IV da Constituição Federal de 1988:
* **7% (sete por cento):** Nas operações e prestações interestaduais que destinem mercadorias ou serviços a contribuintes localizados nas Regiões Norte, Nordeste e Centro-Oeste e no Estado do Espírito Santo (Resolução do Senado Federal nº 22/1989).
* **12% (doze por cento):** Nas operações e prestações interestaduais destinadas a contribuintes localizados nas Regiões Sul e Sudeste (exceto Espírito Santo), abrangendo os Estados de Santa Catarina (SC), Rio Grande do Sul (RS), São Paulo (SP), Rio de Janeiro (RJ) e Minas Gerais (MG).
* **4% (quatro por cento):** Aplicável uniformemente a bens e mercadorias importados do exterior que, após seu desembaraço aduaneiro, não tenham sido submetidos a processo de industrialização, ou, se submetidos a qualquer transformação, resultem em mercadoria cujo Conteúdo de Importação seja superior a 40% (Resolução SF nº 13/2012, regulamentada pelo Convênio ICMS 38/2013 e incorporada no art. 15, § 4º da Lei Estadual nº 11.580/1996).

### 2.2. Diferencial de Alíquotas (DIFAL)
O Paraná possui um duplo regime de apuração do Diferencial de Alíquotas, distinguindo a destinação econômica e a condição jurídica do adquirente:

#### A) DIFAL Entrada Contribuinte (Uso, Consumo ou Ativo Permanente) — Base Dupla
A disciplina do art. 14, § 8º da Lei nº 11.580/1996 (com redação conferida pela Lei nº 18.879/2016 e art. 9º, § 4º do RICMS/PR) impõe a metodologia de **Base Dupla (cálculo por dentro)**.
O cálculo processa-se em três etapas:
1. **Exclusão do ICMS interestadual de origem:** Do valor da operação praticada no Estado de origem, deduz-se o ICMS destacado pelo remetente (7%, 12% ou 4%), obtendo-se o valor líquido da operação sem imposto;
2. **Recomposição da base paranaense:** O valor líquido apurado é recalculado mediante divisão por `(1 - Alíquota Interna PR)`, onde a alíquota padrão corresponde a 19,5% (ou 0,195);
3. **Aplicação da alíquota interna e dedução do crédito de origem:** Aplica-se a alíquota interna paranaense (19,5%) sobre a nova base reconstituída, subtraindo-se o valor do imposto cobrado na origem.

$$\text{Valor Líquido} = \text{Valor Operação de Origem} - \text{ICMS Origem}$$

$$\text{Base Dupla PR} = \frac{\text{Valor Líquido}}{1 - \text{Alíquota Interna PR}}$$

$$\text{DIFAL Devido PR} = (\text{Base Dupla PR} \times \text{Alíquota Interna PR}) - \text{ICMS Origem}$$

*Exemplo Prático Numérico:*  
Aquisição de bem para ativo imobilizado oriundo de SP (alíquota interestadual de 12%) no valor de R$ 100.000,00:
* ICMS de Origem destacado (12%): R$ 12.000,00;
* Valor Líquido: $R\$\;100.000,00 - R\$\;12.000,00 = R\$\;88.000,00$;
* Base Dupla Recomposta (com interna de 19,5%): $\frac{88.000,00}{1 - 0,195} = \frac{88.000,00}{0,805} \approx R\$\;109.316,77$;
* Débito do ICMS Interno PR: $109.316,77 \times 19,5\% = R\$\;21.316,77$;
* DIFAL a Recolher ao Paraná: $R\$\;21.316,77 - R\$\;12.000,00 = \mathbf{R\$\;9.316,77}$.  
*(Caso o cálculo fosse em base simples nominal, o DIFAL seria de apenas 7,5% = R$ 7.500,00. A base dupla paranaense produz um acréscimo de R$ 1.816,77).*

#### B) DIFAL Consumidor Final Não Contribuinte (EC 87/2015, LC 190/2021 e Lei PR nº 20.949/2021)
Nas vendas interestaduais com destino a consumidor final pessoa física ou jurídica não contribuinte situada no Paraná, adota-se a base única (valor total da operação da NF-e, incluindo frete, seguro e despesas acessórias), cabendo ao remetente da outra UF recolher a diferença integral (19,5% - Alíquota Interestadual) em favor do Estado do Paraná via Guia Nacional de Recolhimento de Tributos Estaduais (GNRE) ou apuração mensal caso possua inscrição estadual como Substituto Tributário no cadastro de contribuintes da SEFA/PR (CAD/ICMS).

### 2.3. Transferências entre Estabelecimentos do Mesmo Titular (Pós-ADC 49)
A jurisprudência vinculante do STF na **ADC 49** declarou inconstitucional a incidência de ICMS no mero deslocamento físico de bens entre matriz e filiais ou entre filiais do mesmo titular. A modulação de efeitos culminou na edição da **Lei Complementar Federal nº 204/2023**, que inseriu o § 4º no art. 12 da Lei Complementar nº 87/1996, e nos **Convênios ICMS nº 178/2023 e nº 109/2024**.

No âmbito do Estado do Paraná:
1. **Regulamentação Local:** O Estado editou os **Decretos Estaduais nº 4.544/2023** e **nº 5.255/2024**, adequando o RICMS/PR.
2. **Transferência de Créditos:** A remessa interestadual entre filiais ocorre sob **não incidência jurídica**, operando-se a transferência obrigatória do crédito fiscal correspondente, limitada aos percentuais das alíquotas interestaduais (4%, 7% ou 12%) aplicados sobre:
   - O valor da entrada mais recente da mercadoria;
   - O custo de produção da mercadoria, quando produzida pelo estabelecimento remetente.
3. **Opção pela Equiparação Tributária (Convênio ICMS 109/2024):** A empresa paranaense pode optar por equiparar as transferências a operações regularmente tributadas, mediante lavratura de termo no Registro de Utilização de Documentos Fiscais e Termos de Ocorrências (RUDFTO) até o último dia útil de novembro, com eficácia irretratável para o ano-calendário subsequente.

### 2.4. ICMS-Substituição Tributária (ICMS-ST) Interestadual
O Paraná é signatário de expressivo rol de acordos interestaduais sob a égide do **Convênio ICMS 142/2018**, disciplinados pelo **Anexo IX do RICMS/PR**.
* **Protocolos e Convênios em Vigor:** Bebidas alcoólicas e cervejas (Protocolo ICMS 11/91 e Protocolo 103/12), autopeças (Protocolo ICMS 41/08 e 97/10), medicamentos e produtos farmacêuticos (Convênio ICMS 234/17), tintas e vernizes (Convênio ICMS 118/17), materiais de construção e cosméticos.
* **Cálculo da MVA Ajustada:** Quando a alíquota interna no Paraná (19,5%) for superior à alíquota interestadual de origem (4%, 7% ou 12%), o remetente de outra UF é obrigado a utilizar a Margem de Valor Agregado Ajustada:

$$\text{MVA Ajustada} = \left[ \frac{(1 + \text{MVA-ST Original}) \times (1 - \text{ALQ Inter})}{(1 - \text{ALQ Intra})} \right] - 1$$

* **Particularidade do Remetente Optante pelo Simples Nacional:** Nos termos do **Convênio ICMS 35/2011**, corroborado pelo art. 2º, § 2º do Anexo IX do RICMS/PR, quando a operação interestadual for praticada por contribuinte remetente enquadrado no Simples Nacional, **veda-se a aplicação da MVA Ajustada**, exigindo-se estritamente a aplicação da **MVA Original** prevista na legislação paranaense.

---

## 3. MECANISMOS DE DEDUÇÃO E TOMADA DE CRÉDITO

### 3.1. Princípio da Não-Cumulatividade no Paraná
A disciplina de créditos no Paraná funda-se nos artigos 19 a 25 da Lei Estadual nº 11.580/1996 e artigos 45 a 50 do RICMS/PR:
* **Condições para o Creditamento:** Regularidade formal do documento fiscal idôneo, entrada física ou recebimento efetivo do serviço no estabelecimento paranaense e vinculação direta e necessária à realização de operações subsequentes oneradas pelo imposto.
* **Estorno de Crédito:** Exige-se o estorno proporcional nos casos de perecimento, deterioração, perda, roubo ou saídas beneficiadas com isenção ou redução de base de cálculo, ressalvada previsão expressa de "manutenção de crédito" em convênio CONFAZ ou no RICMS/PR (Anexos I e II).
* **Imunidade nas Exportações:** As saídas para o exterior asseguram a manutenção e o aproveitamento integral dos créditos incorridos na aquisição de matérias-primas, produtos intermediários, embalagens e ativo imobilizado (Art. 155, § 2º, X, "a" da CF/88 e Art. 3º, II da Lei nº 11.580/1996).

### 3.2. Controle de Crédito do Ativo Permanente (CIAP - 1/48 avos)
O aproveitamento do ICMS incidente sobre bens do Ativo Permanente é regulado pelo art. 20, § 5º da Lei Complementar nº 87/1996 (redação da LC 102/2000), art. 24 da Lei Estadual nº 11.580/1996, art. 26 do RICMS/PR e pela **Norma de Procedimento Fiscal (NPF) nº 040/2009** (com atualizações posteriores da Receita Estadual do Paraná):
* **Fração Mensal:** A apropriação é efetuada à razão de **1/48 (um quarenta e oito avos)** por mês civil completo, a partir do mês de efetiva entrada e início de operação do bem na atividade fabril ou comercial da empresa.
* **Fórmula do Fator Mensal de Apropriação:**

$$\text{Crédito Mensal} = \left( \frac{\text{ICMS Total do Bem}}{48} \right) \times \left( \frac{\text{Saídas Tributadas} + \text{Exportações Desoneradas}}{\text{Total Geral das Saídas e Prestações}} \right)$$

* **Escrituração Fiscal Digital (EFD ICMS/IPI):** O detalhamento de cada item deve ser mantido obrigatoriamente no **Bloco G** da EFD. O valor mensal apropriado é transportado ao Bloco E (Apuração do ICMS Próprio) sob o código de ajuste paranaense **PR020021** (Registro E111). A não conformidade entre o valor apurado no Bloco G e o lançamento no Bloco E gera retenção imediata em malha fiscal da SEFA/PR (Malha *AJCP01*).
* **Baixa ou Alienação Antecipada:** Se o bem do ativo permanente for alienado, extraviado ou baixado antes de decorrido o período de 48 meses, cancela-se o saldo remanescente, sendo vedada a apropriação das parcelas faltantes.

### 3.3. Fundo Estadual de Combate à Pobreza (FECOP/PR)
Instituído pelo **Título I da Lei Estadual nº 18.573/2015** (com amparo no art. 82 do ADCT da CF/88), o FECOP é financiado primordialmente pela sobretaxa de **2 (dois) pontos percentuais** adicionada à alíquota de ICMS nas operações internas e nas entradas interestaduais para consumidor final de mercadorias classificadas como supérfluas:
* **Mercadorias Gravadas (Art. 14-A da Lei nº 11.580/1996):** Bebidas alcoólicas (exceto cervejas populares e vinhos comuns), tabaco e produtos de fumo, cosméticos e perfumes, artefatos de joalheria, embarcações esportivas e aeronaves não comerciais.
* **Alíquota Total Efetiva:** Produtos cuja alíquota seletiva interna seja de 27% passam a suportar carga final de **29% (27% ICMS + 2% FECOP)**.
* **Natureza Vinculada e Desvinculação de Crédito:** O adicional de 2% não é passível de compensação ordinária como crédito de ICMS em etapas posteriores de consumo final e deve ser escriturado e segregado em campos próprios na EFD e guias GNRE específicas (Código de Receita Estadual diferenciado).

### 3.4. Sistema de Controle de Créditos Acumulados (SISCRED/PR)
O Paraná possui um dos mais avançados e rigorosos sistemas informatizados de administração e habilitação de créditos acumulados do País, denominado **SISCRED/PR**, normatizado pelos **artigos 51 a 61 do RICMS/PR (Decreto nº 7.871/2017)** e pela **Norma de Procedimento Fiscal (NPF) nº 092/2012** (atualizada pela NPF nº 041/2012 e regulamentações anuais de cotas da SEFA/PR).

```
┌────────────────────────────────────────────────────────────────────────┐
│                   GÊNESE DO CRÉDITO ACUMULADO (PR)                     │
│  - Exportações Imunes (Art. 3º, II da Lei 11.580/96)                  │
│  - Diferimento Operacional (Anexo VIII do RICMS/PR)                   │
│  - Redução de Base de Cálculo com Manutenção Expressa                 │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                      SISTEMA SISCRED (SEFA/PR)                         │
│  1. Pedido de Habilitação Eletrônica (Arquivo Magnético / NPF 092/12) │
│  2. Auditoria Prévia da Receita Estadual do Paraná                    │
│  3. Homologação e Lançamento na Conta Corrente Eletrônica SISCRED     │
└───────────────────┬────────────────────────────────┬───────────────────┘
                    │                                │
                    ▼                                ▼
┌─────────────────────────────────────┐  ┌───────────────────────────────┐
│       UTILIZAÇÃO PRÓPRIA            │  │  TRANSFERÊNCIA A TERCEIROS    │
│ - Liquidação de Débitos Fiscais     │  │ - Pagamento a Fornecedores de │
│   Inscritos em Dívida Ativa         │  │   Matéria-Prima e Embalagem   │
│ - Liquidação de Autos de Infração   │  │ - Aquisição de Bens de Ativo  │
│ - Quitação de ICMS Importação       │  │ - Pagamento a Fornecedores de │
│                                     │  │   Energia Elétrica e Telefonia│
└─────────────────────────────────────┘  └───────────────────────────────┘
```

#### Regras Operacionais Estruturantes do SISCRED:
1. **Hipóteses Admitidas para Acumulação:** Geração sistemática de saldo decorrente de exportação desonerada, saídas ao abrigo de diferimento (cadeia agroindustrial e automotiva) ou saídas com redução de base de cálculo com manutenção de créditos autorizada.
2. **Procedimento de Habilitação Eletrônica:** O contribuinte transmite o demonstrativo eletrônico de apropriação, sujeitando-se a verificação automática de consistência cadastral e contábil pela Inspetoria Geral de Fiscalização da Receita Estadual. O crédito somente é tido por "acumulado homologado" após deferimento formal no sistema.
3. **Modalidades de Transferência e Quitação:**
   - Transferência entre estabelecimentos da mesma empresa situados no Paraná;
   - Transferência para fornecedores paranaenses a título de pagamento de compras de matérias-primas, produtos intermediários, material de embalagem e bens para o ativo permanente;
   - Transferência para concessionárias de serviços públicos de energia elétrica e comunicação (para quitação de faturas de consumo do estabelecimento gerador);
   - Liquidação de autos de infração e compensação de débitos tributários próprios ou adquiridos de terceiros inscritos em Dívida Ativa.
4. **Limitações Orçamentárias Globais:** A Secretaria de Estado da Fazenda edita anualmente Resolução fixando o limite financeiro global em moeda corrente para utilização e transferência dos créditos homologados no SISCRED, preservando o equilíbrio das finanças públicas paranaenses.

---

## 4. SETOR AGRÍCOLA E RURAL PARANAENSE

O agronegócio representa o principal pilar estruturante da economia do Paraná, respondendo por parcela substancial do PIB estadual e pelas posições de liderança nacional na avicultura de corte, suinocultura, produção de grãos (soja, milho e trigo) e cooperativismo agropecuário (congregado pelo Sistema Ocepar).

### 4.1. Insumos Agropecuários (Convênio ICMS 100/97 no RICMS/PR)
O Paraná recepcionou integralmente o **Convênio ICMS 100/1997** nos **Anexos I (Isenções)** e **II (Reduções de Base de Cálculo)** do RICMS/PR:
* **Isenção Interna:** As operações internas com defensivos agrícolas, sementes certificadas ou fiscalizadas, adubos, fertilizantes e calcário corretivo gozam de isenção do ICMS nas saídas entre estabelecimentos de produtores ou cooperativas.
* **Transição Tributária do Convênio ICMS 26/2021:** O Paraná implementou o cronograma progressivo de tributação do Convênio 26/2021 sobre fertilizantes e adubos químicos:
  - *Fertilizantes Importados:* A carga tributária foi elevada progressivamente de 1% (2022) até atingir **4% em 2025/2026**;
  - *Fertilizantes de Produção Nacional:* As saídas interestaduais tiveram a base de cálculo reduzida de modo a resultar em cargas tributárias escalonadas de 1% a 4%, assegurando equalização concorrencial entre insumos importados e a indústria química nacional de defensivos e adubos.

### 4.2. Cadeia do Cooperativismo e Diferimento do ICMS (Anexo VIII do RICMS/PR)
O cooperativismo paranaense (representado por cooperativas gigantes como Coamo, C.Vale, Lar, Copacol, Agrária, Castrolanda, Frisia e Capal) apoia-se no instituto do **Diferimento do ICMS (Anexo VIII do RICMS/PR)**, que posterga a cobrança do imposto para etapas posteriores da cadeia:
* **Grãos (Soja, Milho, Trigo e Feijão):** As saídas de grãos do produtor rural destinadas a cooperativas ou entre estabelecimentos de cooperativas ocorrem sob regime de **diferimento total** do ICMS. O imposto diferido somente é liquidado:
  - Na saída para outra Unidade da Federação;
  - Na saída para o exterior (onde é transmudado em não incidência/imunidade com manutenção de créditos);
  - Na saída dos produtos finais resultantes da industrialização (óleo de soja, farelo, rações, farinha de trigo).
* **Avicultura e Suinocultura:** Modelo de integração verticalizada: a entrega de pintos de um dia, leitões, rações, medicamentos e insumos pela cooperativa integradora aos produtores rurais integrados, bem como o retorno dos animais terminados para abate na agroindústria, operam com diferimento integral do ICMS.
* **Leite Cru:** O transporte de leite in natura do produtor para entrepostos e indústrias de laticínios paranaenses opera com diferimento integral, concentrando-se a tributação no produto pasteurizado ou queijos/iogurtes na etapa final comercializável.

### 4.3. Crédito Presumido e Outorgado para Agroindústrias e Cooperativas
Nos termos do **Anexo III do RICMS/PR**, o Paraná concede créditos outorgados estratégicos para viabilizar a industrialização local de matérias-primas primárias:
* **Abate de Aves e Suínos:** Crédito presumido outorgado sobre o valor das saídas internas e interestaduais de carne e subprodutos comestíveis de aves e suínos abatidos no Paraná, garantindo alívio contra os acúmulos decorrentes de rações e insumos onerados na origem e nivelando a competitividade paranaense frente aos incentivos de Santa Catarina e Rio Grande do Sul.
* **Moinhos de Trigo:** Crédito presumido concedido nas saídas de farinha de trigo e derivados quando elaborados com trigo de produção nacional ou importado com industrialização própria no Paraná.

### 4.4. Obrigações Acessórias: CAD/PRO, NFP-e e Aplicativo Paraná Agro
* **Cadastro de Produtores Rurais (CAD/PRO):** Registro obrigatório de produtores pessoas físicas mantido pela Receita Estadual do Paraná junto às prefeituras municipais para controle territorial e divisão do Valor Adicionado Fiscal (cálculo do Índice de Participação dos Municípios - IPM).
* **Nota Fiscal de Produtor Eletrônica (NFP-e):** É obrigatória a emissão de NFP-e (modelo 55) nas operações com produtos agropecuários, extinguindo-se definitivamente a nota manual em bloco de papel.
* **Aplicativo Móvel "Paraná Agro":** Disponibilizado pela Receita Estadual e Secretaria da Agricultura e Abastecimento (SEAB), permite a emissão instantânea da NFP-e pelo produtor em smartphones, com validação de dados de trânsito agropecuário (GTA eletrônica integrada).
* **Regime Simplificado:** O produtor rural pessoa física paranaense é dispensado da escrituração contábil comercial clássica (EFD ICMS/IPI), apurando suas obrigações pelo confronto cadastral das NFP-e de entrada e saída vinculado à sua inscrição no CAD/PRO.

---

## 5. SETOR INDUSTRIAL E PORTUÁRIO PARANAENSE

### 5.1. Tomada de Crédito sobre Matérias-Primas, Insumos e Energia Elétrica
* **Matérias-Primas e Embalagens:** O crédito do ICMS é irrestrito para aquisições de insumos, matérias-primas e embalagens que sejam consumidos de forma direta e indispensável no processo de fabricação ou que integrem fisicamente o produto acabado comercializado (Lei nº 11.580/1996, art. 22).
* **Energia Elétrica (LC 87/1996, art. 33, II, "b" e RICMS/PR, art. 23):**  
  O direito ao crédito da energia elétrica consumida no estabelecimento industrial não é integral. A apropriação restringe-se **exclusivamente à parcela da energia elétrica gasta diretamente na linha de produção / processo de industrialização**.
  - *Exigência do Laudo Técnico Pericial:* Para afastar glosas e autuações, a Receita Estadual do Paraná exige a apresentação de laudo técnico de rateio de energia elétrica subscrito por engenheiro habilitado junto ao CREA, demonstrando o consumo setorizado das máquinas fabris em relação às áreas administrativas, iluminação externa e refeitórios.

### 5.2. Programa Paraná Competitivo (Lei nº 14.985/2006, Lei nº 15.467/2007 e Decretos nº 6.434/2017 e nº 7.721/2024)
O **Programa Paraná Competitivo** é o principal vetor de atração e sustentação de investimentos fabris no Estado, com foco especial no polo automotivo, indústrias químicas, farmacêuticas, papel/celulose e centros tecnológicos.

```
┌────────────────────────────────────────────────────────────────────────┐
│                   PROGRAMA PARANÁ COMPETITIVO                          │
│        (Lei 14.985/2006, Lei 15.467/2007, Dec. 7.721/2024)            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         ▼                          ▼                          ▼
┌──────────────────┐       ┌──────────────────┐       ┌──────────────────┐
│  DILAÇÃO DE      │       │  DIFERIMENTO DE  │       │ CRÉDITO OUTORGADO│
│  PRAZO (ICMS)    │       │  IMOBILIZADO     │       │ POLO AUTOMOTIVO  │
│ Até 48-72 meses  │       │ Entrada interna, │       │ Redução de custo │
│ para recolhimento│       │ interestadual e  │       │ de montagem e    │
│ incremental      │       │ importada sem    │       │ atração de       │
│                  │       │ desembolso imedi.│       │ sistemistas locais│
└──────────────────┘       └──────────────────┘       └──────────────────┘
```

#### Pilares do Regime de Incentivo:
1. **Dilação de Prazo para Recolhimento Incremental do ICMS:** Financiamento ou postergação de percentual do saldo devedor do ICMS incremental decorrente da ampliação ou implantação da nova planta industrial, por prazos que variam de 48 a 72 meses com carência técnica.
2. **Diferimento nas Aquisições de Ativo Permanente:** Aquisições de máquinas, robôs, moldes e aparelhos industriais destinadas ao ativo imobilizado gozam de diferimento total do ICMS incidente tanto na compra interna em fabricantes paranaenses quanto no desembaraço aduaneiro de importação.
3. **Polo Automotivo Paranaense (Região Metropolitana de Curitiba):** Abrange montadoras globais (Renault, Volkswagen, Volvo, CNH Industrial, Caterpillar) e rede de sistemistas:
   - Crédito presumido outorgado nas saídas de veículos automotores novos;
   - Diferimento do ICMS nas remessas internas entre montadoras e fornecedores de autopeças e subconjuntos plásticos/metalmecânicos;
   - Desoneração na importação de componentes sem similar paranaense.

### 5.3. Complexo Portuário de Paranaguá e Antonina: Regimes de Importação e Drawback
A infraestrutura portuária administrada pela empresa pública Portos do Paraná (Portos de Paranaguá e Antonina) opera com regime aduaneiro-tributário amplamente privilegiado:
* **Diferimento na Importação Portuária (Lei nº 14.985/2006 com alterações da Lei nº 15.467/2007 e arts. 444 a 455 do RICMS/PR):**  
  O ICMS incidente no desembaraço aduaneiro de matérias-primas, produtos intermediários e insumos destinados à industrialização em estabelecimentos industriais paranaenses tem seu recolhimento **diferido** para o momento da saída do produto acabado resultante da fabricação.
  - *Condição Sine Qua Non:* É obrigatório o desembarque físico das cargas pelo Porto de Paranaguá ou Porto de Antonina e o correspondente desembaraço aduaneiro ser procedido perante a alfândega paranaense.
  - *Extensão Rodoviária (Lei 15.467/2007):* Aplica-se a suspensão do ICMS também a mercadorias procedentes de países da América Latina (Mercosul) que ingressem no Paraná por via rodoviária através da fronteira de Foz do Iguaçu (Ponte da Amizade e Ponte Tancredo Neves).
* **Drawback (Convênio ICMS 27/1990 e alterações):** Isenção ou suspensão do ICMS na importação de mercadorias destinadas a beneficiamento, acondicionamento, fabricação ou complementação de produtos para posterior exportação ao exterior. O Paraná não exige pagamento de imposto na entrada quando o contribuinte comprova o cumprimento do compromisso de exportação averbado no Siscomex/Portal Único.

---

## 6. SETOR DE PRODUTO ACABADO (ATACADO, VAREJO E DISTRIBUIÇÃO)

### 6.1. MVA / IVA-ST e Pautas Fiscais da SEFAZ/PR
O setor de distribuição e comércio atacadista/varejista no Paraná lida com rigorosa aplicação da substituição tributária progressiva:
* **Margens de Valor Agregado (MVA):** Fixadas nas tabelas setoriais do Anexo IX do RICMS/PR para determinar a presunção do preço ao consumidor final.
* **Pautas Fiscais (Boletins Informativos da SEFAZ):** Para setores altamente concentrados e padronizados — notadamente bebidas (cervejas, refrigerantes, isotônicos, vinhos e destilados), cigarros e cimento —, a Receita Estadual do Paraná adota **Pauta Fiscal de Preços Médios Ponderados a Consumidor Final (PMPF)**, fixada periodicamente com base em coletas de notas eletrônicas (NFC-e). Nesses segmentos, o valor da pauta prevalece obrigatoriamente sobre o cálculo percentual de MVA caso este resulte em valor inferior.

### 6.2. Regime Especial para Atacadistas e Centros de Distribuição (Art. 28 do Anexo VIII do RICMS/PR)
O Paraná possui um diferencial competitivo específico voltado a reter distribuidoras e centros de distribuição (CDs) frente à agressiva concorrência dos regimes de Santa Catarina (TTD 409/410) e São Paulo:
* **Diferimento Parcial de 38,46%:** O **artigo 28 do Anexo VIII do RICMS/PR** estabelece o diferimento parcial do pagamento do ICMS nas saídas internas entre contribuintes de mercadorias destinadas à comercialização ou industrialização:

$$\text{Alíquota Padrão Nominal} = 19,5\%$$

$$\text{Parcela Diferida} = 38,46\% \times 19,5\% = 7,5\%$$

$$\text{Carga Tributária Efetiva Imediata} = 19,5\% - 7,5\% = \mathbf{12,0\%}$$

* *Efeito Financeiro:* O adquirente paranaense (varejista ou transformador) recebe a nota fiscal com destaque de 12% efetivo de ICMS, gerando menor desembolso de capital de giro e mitigando a distorção concorrencial com produtos vindos de outros Estados do Sul e Sudeste a 12% interestadual.
* **Créditos Outorgados para Centros de Distribuição (Regimes Especiais Autorizativos):** Empresas atacadistas que concentrem compras e estoques no Paraná podem celebrar Regime Especial com a SEFA/PR para fruição de crédito presumido limitador de carga tributária final de 1% a 3% nas saídas interestaduais, mediante compromissos de faturamento mínimo e geração de postos de trabalho.

### 6.3. Restituição e Complementação do ICMS-ST: O Sistema ADRC-ST
Após a fixação da tese de repercussão geral pelo Supremo Tribunal Federal no **Tema 201 (RE 593.849)**, pacificou-se a obrigatoriedade da restituição da quantia paga a maior a título de ICMS-ST quando a base de cálculo real da venda ao consumidor final for inferior à presumida, bem como a complementação em sentido inverso.

No Paraná, a matéria foi disciplinada pela **Lei Estadual nº 19.840/2019**, regulamentada pelo **Decreto Estadual nº 3.886/2020** e pela **Norma de Procedimento Fiscal (NPF) nº 003/2020** (atualizada pela NPF nº 052/2023), que instituíram o **ADRC-ST (Arquivo Digital de Recuperação, Ressarcimento e Complementação do ICMS-ST)**.

```
┌────────────────────────────────────────────────────────────────────────┐
│                   FLUXO OPERACIONAL DO ADRC-ST (PR)                    │
│                 (Lei 19.840/2019 e NPF nº 003/2020)                    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
         ┌──────────────────────────┴──────────────────────────┐
         ▼                                                     ▼
┌──────────────────────────────────┐        ┌──────────────────────────────────┐
│ VENDA EFETIVA < BASE PRESUMIDA   │        │ VENDA EFETIVA > BASE PRESUMIDA   │
│ - Gera direito a Ressarcimento   │        │ - Gera obrigação de Complemento  │
│ - Crédito para o contribuinte    │        │ - Débito recolhido ao Fisco      │
└────────────────┬─────────────────┘        └─────────────────┬────────────────┘
                 │                                            │
                 └──────────────────────┬─────────────────────┘
                                        │
                                        ▼
┌────────────────────────────────────────────────────────────────────────┐
│                    CONSOLIDAÇÃO MENSAL NO ARQUIVO                      │
│ 1. Apuração mensal por item (Registro de Entradas x Saídas x Estoque)  │
│ 2. Confronto analítico com a parcela do FECOP (2%)                     │
│ 3. Compensação interna: Saldo Ressarcível vs. Saldo Complementar       │
│ 4. Transmissão pelo portal Receita/PR -> Homologação e geração de      │
│    código de ajuste na EFD (Lançamento no Registro E111/E220)          │
└────────────────────────────────────────────────────────────────────────┘
```

* **Regras Práticas do ADRC-ST:**
  - O contribuinte substituído (varejistas, postos de combustíveis, supermercados) deve gerar mensalmente o arquivo digital com controle unitário de estoque pelo método PEPS/Custo Médio ponderado móvel;
  - Se o resultado líquido do mês for credor (predomínio de ressarcimento), o valor aprovado é lançado como crédito na apuração de ICMS próprio ou pode ser transferido a fornecedor substituto para abatimento em compras futuras;
  - Se o resultado for devedor (complementação decorrente de venda acima da MVA/pauta), o valor apurado deve ser recolhido até o dia 12 do mês subsequente via GR-PR (Guia de Recolhimento do Paraná).

### 6.4. E-commerce e Responsabilidade Tributária de Marketplaces
Com a incorporação das diretrizes da LC 190/2021 e modernizações introduzidas no art. 18 da Lei nº 11.580/1996:
* **Solidariedade Tributária:** As plataformas de marketplace, operadoras de intermediação logística e portais eletrônicos respondem solidariamente pelo ICMS e pelas penalidades devidas quando realizarem a intermediação de mercadorias desacompanhadas de documentação fiscal idônea ou oriundas de vendedores clandestinos.
* **Cruzamento de Pagamentos (DIMP):** A SEFA/PR executa malhas fiscais automáticas cruzando as NF-e emitidas com os repasses financeiros reportados na Declaração de Informações de Meios de Pagamento (DIMP) pelas operadoras de cartão, adquirentes e instituições de pagamento via PIX.

---

## 7. TRANSIÇÃO PARA O NOVO SISTEMA TRIBUTÁRIO (IBS / CBS - EC 132/2023 E LC 214/2025)

A promulgação da Emenda Constitucional nº 132/2023, complementada pelo projeto de lei complementar de regulamentação (LC 214/2025), promove a mais profunda transformação na história tributária paranaense, extinguindo o ICMS entre 2029 e 2032 e instituindo o modelo dual de Imposto sobre Bens e Serviços (IBS) e Contribuição sobre Bens e Serviços (CBS).

```
LINHA DO TEMPO DA TRANSIÇÃO TRIBUTÁRIA NO PARANÁ:
2026                 2027                 2029                 2032                 2033
  │                    │                    │                    │                    │
  ├────────────────────┼────────────────────┼────────────────────┼────────────────────┤
Auditoria e          Início CBS           Início Transição      Extinção total       Início da
homologação de       federal (0,9%) e     do ICMS / IBS:        do ICMS /            compensação em
saldos credores no   teste do IBS         ICMS cai 10% a.a.     RICMS/PR. Fim do     240 meses dos
SISCRED (SEFA/PR)    (0,1%).              FCBF compensa         Paraná Competitivo   saldos homologados
para art. 134 ADCT.                       empresas.             e do diferimento.    (art. 134 ADCT).
```

### 7.1. Impactos Estruturais na Economia Agroindustrial Paranaense
1. **Fim do ICMS na Origem e Adoção do Princípio do Destino Puro:**
   - Atualmente, o Paraná retém parcela expressiva de ICMS nas operações interestaduais a 12% ou 7% de seus produtos manufaturados e agroindustriais. Sob o IBS, **100% da receita pertencerá ao Estado ou Município de destino do consumo**.
   - O agronegócio paranaense ganha com a **desoneração irrestrita e ampla das exportações** (art. 156-A, § 1º, V da CF/88), assegurando o ressarcimento rápido em dinheiro de todos os créditos incorridos em insumos, maquinários e serviços pelo Comitê Gestor do IBS, acabando com os crônicos saldos acumulados hoje represados.
2. **Impacto sobre o Sistema Cooperativo (Ocepar):**
   - O regime diferenciado das cooperativas previsto no art. 156-A, § 5º, VII da CF/88 e regulamentado pela LC 214/2025 garantirá a não tributação no repasse de sobras e na circulação interna entre cooperado e cooperativa (ato cooperativo autêntico), preservando a competitividade das cooperativas de grãos e proteína animal do Paraná.

### 7.2. Homologação de Saldo Credor Acumulado de ICMS (Art. 134 do ADCT / LC 214/2025)
Uma das questões mais críticas para a indústria paranaense diz respeito à preservação dos créditos acumulados legítimos de ICMS apurados até a extinção do tributo:
* **Regra Constitucional do Art. 134 do ADCT:** Os saldos credores de ICMS acumulados e reconhecidos pelos Estados até 31 de dezembro de 2032 serão aproveitados pelos contribuintes mediante **compensação com o IBS em 240 (duzentas e quarenta) parcelas mensais, sucessivas e corrigidas pelo IPCA**, com início em **janeiro de 2033**.
* **Oportunidade Estratégica do Paraná com o SISCRED:**
  - Diferentemente de outros Estados que não possuem sistemas eletrônicos robustos e enfrentarão colapsos de pedidos de auditoria física de créditos entre 2029 e 2032, o **Paraná dispõe do SISCRED já em pleno funcionamento**.
  - As indústrias e cooperativas paranaenses devem acelerar imediatamente a submissão de seus saldos ao SISCRED para garantir sua pré-homologação formal perante a SEFA/PR. Os créditos já habilitados no SISCRED desfrutarão de presunção de liquidez e certeza no protocolo de transição exigido pelo Comitê Gestor do IBS.

### 7.3. Fundo de Compensação de Benefícios Fiscais (FCBF) e o Futuro do Paraná Competitivo
O modelo federativo baseado em guerra fiscal e atração por incentivos de ICMS perderá vigência completa até 31/12/2032:
* **Estrutura do FCBF (Art. 159-A da CF/88):** A União repassará R$ 160 bilhões entre 2029 e 2032 para indenizar e compensar os contribuintes que tiverem seus benefícios fiscais convalidadores reduzidos.
* **Cronograma de Redução dos Benefícios Locais:**
  - 2029: Redução compulsória de 10% do valor do incentivo estadual;
  - 2030: Redução compulsória de 20%;
  - 2031: Redução compulsória de 30%;
  - 2032: Redução compulsória de 40%;
  - 2033: Extinção definitiva e integral de todos os incentivos fiscais estaduais.
* **Requisitos para as Empresas Habilitadas no Paraná Competitivo:**
  - Para receber a indenização do FCBF paga pelo Governo Federal, o benefício concedido pelo Estado do Paraná deve ter sido estritamente depositado e publicado perante o CONFAZ nos termos da **Lei Complementar nº 160/2017 e do Convênio ICMS 190/2017**.
  - A empresa beneficiária deverá comprovar anualmente perante a SEFA/PR e à comissão gestora federal o adimplemento integral dos compromissos de investimento produtivo e criação de empregos estabelecidos no protocolo original do Paraná Competitivo.

---

## 8. PLANO DE AÇÃO E RECOMENDAÇÕES PARA O REPOSITÓRIO

Com base nas deficiências detectadas no repositório `estaduais/pr/`, recomendam-se as seguintes ações corretivas imediatas de documentação:

```
┌────────────────────────────────────────────────────────────────────────┐
│               PLANO DE REGULARIZAÇÃO DO REPOSITÓRIO PR                 │
├────────────────────────────────────────────────────────────────────────┤
│ 1. [LEI 11.580/1996] Inserir a íntegra da Lei Orgânica do ICMS/PR em   │
│    `estaduais/pr/leis/icms/lei-11580-1996.md`.                        │
│ 2. [RICMS/PR CONSOLIDADO] Substituir o arquivo truncado de 89 linhas   │
│    por versão consolidada do Decreto 7.871/2017 com seus 13 Anexos.   │
│ 3. [LEI 18.877/2016 - PAT/CCRF] Criar a pasta e arquivo da Lei de     │
│    regência do Processo Administrativo Fiscal e CCRF em                │
│    `estaduais/pr/leis/pat/lei-18877-2016.md`.                         │
│ 4. [LEGISLAÇÃO DE INCENTIVOS] Inserir a Lei 14.985/2006, Lei          │
│    15.467/2007 e o Decreto 7.721/2024 (Paraná Competitivo).          │
│ 5. [COMPLEMENTAÇÃO FECOP] Inserir o Título I (FECOP) na Lei           │
│    `estaduais/pr/leis/itcmd/lei-18573-2015.md`.                       │
│ 6. [NORMAS PROCEDIMENTAIS] Criar pasta `estaduais/pr/npf/` contendo   │
│    NPF 040/2009 (CIAP), NPF 092/2012 (SISCRED) e NPF 003/2020         │
│    (ADRC-ST).                                                          │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 9. QUADRO CONSOLIDADO DAS PRINCIPAIS NORMAS TRIBUTÁRIAS DO PARANÁ

| Norma Jurídica | Órgão Emissor | Objeto Tributário / Tema | Impacto Econômico Principal |
| :--- | :--- | :--- | :--- |
| **Lei nº 11.580/1996** | Assembleia Legislativa do Paraná | Lei Orgânica Geral do ICMS no Paraná. | Base fundamental da competência, incidência, alíquotas e penalidades do ICMS paranaense. |
| **Decreto nº 7.871/2017** | Poder Executivo Estadual | Regulamento do ICMS (RICMS/PR) e seus 13 Anexos. | Disciplina minudente de obrigações, diferimento (Anexo VIII), ST (Anexo IX), isenções e créditos. |
| **Lei nº 21.850/2023** | Assembleia Legislativa do Paraná | Elevação da Alíquota Modal Interna. | Fixa a alíquota geral interna do Paraná em **19,5%** desde 18/03/2024. |
| **Lei nº 18.573/2015** | Assembleia Legislativa do Paraná | Título I: FECOP / Título II: ITCMD. | Adicional de 2% sobre bens supérfluos e Código do ITCMD estadual. |
| **Lei nº 14.260/2003** | Assembleia Legislativa do Paraná | Lei Orgânica do IPVA. | Alíquotas de 3,5% (automóveis) e 1% (caminhões/ônibus) e isenções. |
| **Lei nº 18.877/2016** | Assembleia Legislativa do Paraná | Processo Administrativo Fiscal (PAF) e CCRF. | Contencioso fiscal administrativo, prazos recursais e alçadas de julgamento. |
| **Lei nº 14.985/2006** | Assembleia Legislativa do Paraná | Importações Portuárias no Paraná. | Suspensão e diferimento de ICMS na importação por Paranaguá/Antonina. |
| **Lei nº 15.467/2007** | Assembleia Legislativa do Paraná | Importação Rodoviária (Mercosul) e Cesta Básica. | Estende suspensão do ICMS a importações rodoviárias da América Latina. |
| **Decreto nº 7.721/2024** | Poder Executivo Estadual | Programa Paraná Competitivo Atualizado. | Atração de investimentos, dilação de prazo para ICMS e polo automotivo. |
| **Decreto nº 3.886/2020** | Poder Executivo Estadual | Restituição e Complementação do ICMS-ST. | Adequação ao Tema 201 STF e implantação do sistema ADRC-ST. |
| **NPF nº 092/2012** | Receita Estadual do Paraná | Regulamentação do SISCRED/PR. | Procedimento informatizado para habilitação e transferência de créditos acumulados. |
| **NPF nº 040/2009** | Receita Estadual do Paraná | CIAP (1/48 avos) na EFD ICMS/IPI. | Escrituração do Bloco G e cálculo do fator de apropriação do ativo imobilizado. |
| **NPF nº 003/2020** | Receita Estadual do Paraná | Manual Técnico do ADRC-ST. | Regras de validação do arquivo digital de restituição e complementação do ICMS-ST. |

---
**Conclusão do Parecer Técnico:** O Estado do Paraná dispõe de um arcabouço fiscal consolidado, com alto grau de automação e controle eletrônico (SISCRED, ADRC-ST, Paraná Agro). A prioridade técnica máxima para as equipes de compliance e tax governance consiste na atualização documental do repositório físico e na preparação documental imediata dos créditos acumulados para habilitação perante a SEFA/PR com vistas à futura transição para o IBS (art. 134 do ADCT).
