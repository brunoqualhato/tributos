# Relatório de Auditoria e Diagnóstico Tributário: Estado do Rio de Janeiro (RJ)

**Jurisdição:** Estado do Rio de Janeiro (SEFAZ/RJ)  
**Data da Auditoria:** Outubro de 2026  
**Período de Referência:** Ordenamento Vigente (Legislação Consolidada até 2026 e Transição da Reforma Tributária - EC 132/2023 e LC 214/2025)  
**Status do Repositório Local (`estaduais/rj/`):** Auditoria Crítica de Cobertura e Lacunas

---

## SUMÁRIO EXECUTIVO

O presente relatório técnico-jurídico apresenta o diagnóstico detalhado e exaustivo da estrutura tributária do Estado do Rio de Janeiro (RJ). A auditoria confronta o acervo do repositório local em `estaduais/rj/` com o arcabouço normativo fluminense efetivamente exigível, cobrindo o contencioso administrativo, regimes de crédito e dedução, as relações interestaduais federativas (DIFAL, ADC 49, ICMS-ST), os regimes setoriais vitais para a economia fluminense (Agrícola, Industrial/Óleo e Gás/Offshore, Atacado/Varejo) e o impacto fiscal da transição para o modelo do IBS/CBS da Reforma Tributária.

O repositório local encontra-se em estado incipiente: possui apenas três arquivos sintéticos e desprovidos de detalhamento regulamentar integral (`decreto-27427-2000.md` condensado em 89 linhas, `lei-7174-2015.md` do ITD e `lei-2877-1997.md` do IPVA), inexistindo a matriz primária do ICMS estadual (Lei Ordinária nº 2.657/1996), a espinha dorsal de obrigações acessórias (Resolução SEFAZ nº 720/2014), a regulação do Processo Administrativo Tributário (PAT/RJ) e o complexo microssistema de benefícios fiscais convalidados e fundos parafiscais (FEEF/FOT).

---

## 1. NORMAS ESTADUAIS NO REPOSITÓRIO E AUDITORIA DE LACUNAS NORMATIVAS

### 1.1. Inventário Crítico do Diretório `estaduais/rj/`

A inspeção física do diretório revelou a existência exclusiva dos seguintes arquivos:
1. `estaduais/rj/ricms/decreto-27427-2000.md`: Resumo executivo de 89 linhas que sumariza a aprovação do RICMS/RJ e cita a alíquota modal de 20% + 2% FECP = 22% (vigente a partir de 20/03/2024 via Lei Estadual nº 10.253/2023), mas omite os 18 Livros regulamentares, anexos de benefícios fiscais, regimes especiais e pautas de Substituição Tributária.
2. `estaduais/rj/leis/itcmd/lei-7174-2015.md`: Transcrição de excertos da lei do Imposto sobre a Transmissão Causa Mortis e por Doação (ITD), prevendo alíquotas progressivas de 4% a 8%, sem a consolidação dos decretos de apuração de base de cálculo para quotas societárias e participações em fundos fechados.
3. `estaduais/rj/leis/ipva/lei-2877-1997.md`: Estrutura de incidência do Imposto sobre a Propriedade de Veículos Automotores (IPVA), contendo as alíquotas de 1% a 4%, sem detalhar as hipóteses de isenção e benefícios para frotas de locadoras e veículos híbridos/elétricos.

### 1.2. Mapeamento Analítico das Normas Fluminenses Faltantes

Para assegurar a integridade do acervo jurídico do repositório, é imperativa a ingestão das seguintes normas primárias e secundárias:

| Instrumento Normativo | Denominação / Ementa | Relevância Jurídica e Conteúdo Faltante |
| :--- | :--- | :--- |
| **Lei nº 2.657/1996** | **Lei Orgânica do ICMS/RJ** | **Norma Mater do ICMS Fluminense.** Disciplina o fato gerador, base de cálculo, alíquotas (art. 14), sujeição passiva, responsabilidade solidária de intermediadores (art. 18), e as modificações da Lei 7.071/2015 (base dupla DIFAL), Lei 9.531/2021 (DIFAL LC 190) e Lei 10.253/2023 (alíquota modal de 20%). |
| **Decreto nº 27.427/2000** *(Texto Integral)* | **Regulamento do ICMS (RICMS/RJ)** | Estrutura completa dos **Livros I a XVIII**: Livro I (Obrigações Principais e Créditos), Livro II (Substituição Tributária), Livro III (Crédito Acumulado), Livro VI (Documentos e Livros Fiscais), Livro XIV (Agropecuária), Livros de regimes setoriais. |
| **Resolução SEFAZ nº 720/2014** | **Regulamento de Obrigações Acessórias e Procedimentos** | **Norma operacional central.** Composta pela Parte Geral e Anexos I a XIV. Regula a Inscrição Estadual (CAD-ICMS), emissão e escrituração de NF-e, NFC-e, CT-e, MDF-e, EFD-ICMS/IPI (SPED Fiscal), controle do CIAP (Anexo XI) e adesão a tratamentos tributários setoriais. |
| **Decreto-Lei nº 5/1975** e **Decreto nº 2.473/1979** c/c **Lei nº 5.427/2009** | **Código Tributário Estadual (CTE-RJ) e Regulamento do Processo Administrativo Tributário (RPAT/RJ)** | Regência do contencioso fiscal fluminense: rito de lançamento, autuação fiscal, impugnação em 1ª Instância perante a **Junta de Revisão Fiscal (JRF)** e recursos em 2ª Instância perante o colegiado paritário do **Conselho de Contribuintes do Estado do Rio de Janeiro (CCERJ)**, complementados pela Lei nº 5.427/2009. |
| **Lei nº 4.056/2002** e **Decreto nº 46.825/2019** | **Fundo Estadual de Combate à Pobreza e às Desigualdades Sociais (FECP)** | Adicional de alíquota do ICMS destinado ao fundo social: regra geral de **2%** que incide sobre a esmagadora maioria das operações e prestações internas e importações, alcançando **4%** em artigos supérfluos (art. 82 do ADCT). |
| **Lei nº 8.645/2019** alterada pela **Lei nº 11.071/2025** e **Decreto nº 50.248/2026** | **Fundo Orçamentário Temporário (FOT)** *(Antigo FEEF - Lei nº 7.428/2016)* | Condicionante de fruição de benefícios fiscais convalidados: retenção e depósito mensal de parcela sobre o valor da desoneração. Reformulado pela **Lei 11.071/2025** pós-Tema 1.386/STF, fixando cronograma progressivo de 20% (2026) a 60% (2032) para benefícios não onerosos e taxa fixa de 18,18% para benefícios onerosos da LC 214/2025, ressalvadas exceções setoriais de 10%. |
| **Lei nº 6.979/2015** | **Tratamento Tributário Especial da Indústria Fluminense** | Concede carga tributária efetiva de **3% de ICMS** para indústrias instaladas em municípios do interior fluminense, com diferimento nas compras de ativo e matérias-primas. Convalidada até 2032 (LC 160/2017). |
| **Lei nº 8.890/2020** e **Resolução SEFAZ nº 153/2020** | **Regime Especial de Óleo, Gás e Petróleo (REPETRO-SPED)** | Internalização dos Convênios ICMS 03/2018 e 220/2019: isenção na admissão temporária de ativos offshore e redução de base de cálculo com alíquota efetiva de **3%** nas aquisições e importações definitivas até 31/12/2040. |
| **Lei nº 9.025/2020** e **Lei nº 4.173/2003** | **Regime Especial do Comércio Atacadista e Centros de Distribuição (Novo Rio Log)** | Carga tributária efetiva de **1,1%** nas operações internas e **1,5%** nas interestaduais para atacadistas e centros de distribuição, associada ao diferimento do ICMS na importação por portos e aeroportos fluminenses. |
| **Lei nº 8.960/2020** | **Regime Diferenciado do Setor Metalmecânico ("Lei do Aço")** | Concede crédito presumido de ICMS para indústrias do setor metalmecânico e siderúrgico, resultando em carga tributária de **3%** nas saídas de mercadorias. |

---

## 2. RELACIONAMENTO TRIBUTÁRIO DO ICMS-RJ COM OS DEMAIS 26 ESTADOS E DF

O relacionamento interestadual do Rio de Janeiro é caracterizado por sua posição de Estado polo na Região Sudeste, combinando expressiva produção extrativa e industrial com elevado mercado consumidor final.

```
       OPERACÕES INTERESTADUAIS ENVOLVENDO O RIO DE JANEIRO (RJ)
       
       SAÍDAS DE RJ:
       ├── Destino: Regiões Norte, Nordeste, Centro-Oeste e ES ───> Alíquota: 7%
       ├── Destino: Regiões Sul e Sudeste (exceto ES: SP, MG, PR, SC, RS) ──> Alíquota: 12%
       └── Bens Importados (FCI > 40%) para qualquer UF ───────────> Alíquota: 4%
       
       ENTRADAS EM RJ:
       ├── Origem: SP, MG, PR, SC, RS ─────────────────────────────> Alíquota: 12%
       ├── Origem: Norte, Nordeste, Centro-Oeste e ES ──────────────> Alíquota: 7%
       └── Bens Importados (FCI > 40%) de qualquer UF ─────────────> Alíquota: 4%
```

### 2.1. Alíquotas Interestaduais (Resoluções do Senado Federal nº 22/1989, 13/2012 e 95/1996)

1. **Saídas Interestaduais promovidas por estabelecimentos situados no RJ:**
   - **Alíquota de 7%:** Aplicável nas operações e prestações com destino às Regiões Norte, Nordeste e Centro-Oeste, bem como ao Estado do Espírito Santo (Resolução SF nº 22/1989, art. 1º, inciso II).
   - **Alíquota de 12%:** Aplicável nas operações e prestações destinadas aos demais Estados das Regiões Sul e Sudeste (São Paulo, Minas Gerais, Paraná, Santa Catarina e Rio Grande do Sul).
   - **Alíquota de 4% (Bens e Mercadorias Importadas):** Incide nas saídas interestaduais de bens ou mercadorias importados do exterior que não tenham sido submetidos a processo de industrialização, ou que, após processo de industrialização no estabelecimento fluminense, resultem em mercadoria com **Conteúdo de Importação superior a 40%** (Resolução SF nº 13/2012 c/c Convênio ICMS nº 38/2013).
     - *Exceções à alíquota de 4%:* Gás natural importado do exterior; bens e mercadorias sem similar nacional constantes de listas editadas pela CAMEX; produtos sob o regime de bens de informática e automação abrangidos pela Lei Federal nº 8.248/1991.
   - **Alíquota de 4% (Transporte Aéreo):** Prestações de transporte aéreo interestadual de passageiros, cargas e mala postal iniciadas no RJ sujeitam-se à alíquota de 4% (Resolução SF nº 95/1996).

2. **Entradas Interestaduais em favor de destinatários fluminenses:**
   - Carga de entrada creditável de 12% se originária de SP, MG, RS, SC ou PR.
   - Carga de entrada creditável de 7% se originária do Norte, Nordeste, Centro-Oeste ou Espírito Santo.
   - Carga de entrada creditável de 4% nas mercadorias abrangidas pela Resolução SF nº 13/2012 acompanhadas da respectiva Ficha de Conteúdo de Importação (FCI).

### 2.2. Diferencial de Alíquotas (DIFAL)

O ordenamento fluminense possui duas sistemáticas distintas de Diferencial de Alíquotas:

#### A. DIFAL para Consumidor Final Não Contribuinte (EC nº 87/2015, LC nº 190/2021 e Lei Estadual nº 9.531/2021)
- **Hipótese de Incidência:** Operações e prestações interestaduais que destinem bens ou serviços a consumidor final não contribuinte do ICMS situado no Rio de Janeiro.
- **Base Legal:** Arts. 3º, inciso XVIII, e 4º, inciso X, da Lei Estadual nº 2.657/1996 (redação da Lei nº 9.531/2021), regulamentados pelo Convênio ICMS nº 236/2021.
- **Responsável Tributário:** Remetente da mercadoria situado em outra UF, exigindo-se recolhimento operação a operação via GNRE ou por apuração mensal caso possua inscrição estadual especial no CAD-ICMS do RJ.
- **Cálculo com Base Única:**
  $$\text{DIFAL}_{\text{Não Contribuinte}} = \text{Base de Cálculo} \times [(\text{Alíquota Interna RJ} + \text{FECP}) - \text{Alíquota Interestadual}]$$
  - Tomando-se como exemplo a alíquota modal do RJ de 20% + 2% FECP = 22%, e mercadoria nacional oriunda de São Paulo (alíquota interestadual de 12%):
  $$\text{DIFAL} = \text{Base} \times (22\% - 12\%) = \text{Base} \times 10\%$$
  - Sendo produto importado (alíquota interestadual de 4%):
  $$\text{DIFAL} = \text{Base} \times (22\% - 4\%) = \text{Base} \times 18\%$$

#### B. DIFAL para Contribuinte do ICMS (Bens de Uso, Consumo ou Ativo Permanente)
- **Hipótese de Incidência:** Entrada física no território fluminense de mercadorias provenientes de outra UF destinadas a integrar o Ativo Imobilizado ou o Uso e Consumo do adquirente contribuinte fluminense.
- **Metodologia de "Base Dupla" ("Cálculo por Dentro"):** Prevista no art. 4º, inciso VI, alínea 'b' da Lei nº 2.657/1996 (incluída pela Lei Estadual nº 7.071/2015):
  1. Do valor da operação na UF de origem, deduz-se o montante do ICMS interestadual destacado na NF-e de origem;
  2. Adiciona-se ao montante resultante o percentual da alíquota interna fluminense (22% efetiva modal), calculando o imposto "por dentro":
     $$\text{Base Dupla} = \frac{\text{Valor da Operação} - \text{ICMS Origem}}{1 - \text{Alíquota Interna RJ}}$$
  3. Aplica-se a alíquota interna do RJ sobre a base recomposta e subtrai-se o ICMS destacado na origem:
     $$\text{DIFAL Devido} = (\text{Base Dupla} \times \text{Alíquota Interna RJ}) - \text{ICMS Origem}$$

### 2.3. Transferências entre Estabelecimentos do Mesmo Titular (ADC 49, LC 204/2023 e Convênio ICMS 109/2024)

O julgamento da Ação Declaratória de Constitucionalidade nº 49 (STF) fixou a tese de que o simples deslocamento de mercadorias entre matriz e filiais não constitui fato gerador do ICMS por ausência de transferência de titularidade econômica ou jurídica.

1. **Marco Regulatório Positivado:**
   - Lei Complementar nº 204/2023 inseriu os §§ 4º e 5º no art. 12 da Lei Complementar nº 87/1996, assegurando a **não incidência de ICMS** na saída de mercadorias entre estabelecimentos do mesmo titular e garantindo a manutenção do crédito das operações anteriores.
   - O Convênio ICMS nº 178/2023 e, posteriormente, o **Convênio ICMS nº 109/2024** uniformizaram nacionalmente o procedimento de transferência obrigatória dos créditos fiscais.

2. **Mecanismo Padrão de Transferência de Crédito:**
   - A operação de saída física de mercadorias em transferência interestadual (CFOP `6.151` ou `6.152`) ocorre com não incidência, efetuando-se a transferência do crédito fiscal vinculado limitado aos percentuais das alíquotas interestaduais (4%, 7% ou 12%) aplicados sobre:
     * O valor da entrada mais recente da mercadoria;
     * O custo da mercadoria produzida (matéria-prima, insumos e custos diretos);
     * No caso de produtos não industrializados, a soma dos custos de sua produção.
   - O crédito é escriturado a débito no estabelecimento remetente e a crédito no estabelecimento destinatário na EFD-ICMS/IPI.

3. **Faculdade de Equiparação a Operação Tributada (Cláusula Sexta do Convênio 109/2024):**
   - É facultado ao contribuinte fluminense optar por equiparar as transferências de mercadorias a operações sujeitas à tributação regular do ICMS.
   - **Procedimento no Rio de Janeiro:** A opção deve ser formalizada mediante registro lavrado no Livro Eletrônico de Registro de Utilização de Documentos Fiscais e Termos de Ocorrências (RUDFTO) da SEFAZ/RJ, com validade anual, irretratável para todo o ano-calendário, vinculando todos os estabelecimentos da empresa situados no território fluminense.

### 2.4. Substituição Tributária Interestadual (ICMS-ST) e Protocolos CONFAZ

A sistemática de ICMS-ST no Estado do Rio de Janeiro é regida pelo Livro II do RICMS/RJ (Decreto nº 27.427/2000) e pelas diretrizes gerais do **Convênio ICMS nº 142/2018**.

1. **Protocolos Interestaduais Celebrados pelo RJ:**
   O Estado do Rio de Janeiro é signatário de dezenas de Protocolos ICMS que impõem ao remetente de outras UFs a obrigação de retenção e recolhimento do ICMS-ST e do respectivo FECP-ST em favor do Fisco fluminense. Dentre os principais segmentos conveniados destacam-se:
   - Autopeças (Protocolo ICMS 41/2008);
   - Produtos Farmacêuticos e Medicamentos (Convênio ICMS 234/2017);
   - Cosméticos, Perfumaria e Higiene Pessoal (Protocolo ICMS 97/2010);
   - Bebidas Frias - Cervejas, Chopes e Refrigerantes (Protocolo ICMS 11/1991 e pautas PMPF);
   - Materiais de Construção, Acabamento e Elétricos (Protocolo ICMS 32/2014);
   - Pneus e Câmaras de Ar (Convênio ICMS 102/2017).

2. **Cálculo da Margem de Valor Agregado Ajustada (MVA Ajustada):**
   Nas aquisições de mercadorias sujeitas à ST oriundas de outras UFs tributadas às alíquotas interestaduais de 4%, 7% ou 12%, cuja alíquota interna no Rio de Janeiro seja superior (22% na regra modal), o remetente deve aplicar a fórmula de ajustamento da margem para evitar distorção concorrencial:
   $$\text{MVA Ajustada} = \left[ \frac{(1 + \text{MVA Original}) \times (1 - \text{ALQ Inter})}{(1 - \text{ALQ Intra})} \right] - 1$$
   - Onde:
     * $\text{MVA Original}$: Margem estabelecida na legislação do RJ para a operação interna;
     * $\text{ALQ Inter}$: Alíquota interestadual aplicada pelo remetente (0,04, 0,07 ou 0,12);
     * $\text{ALQ Intra}$: Coeficiente correspondente à carga tributária interna do RJ (0,22 na regra geral).

3. **Inaplicabilidade da MVA Ajustada para o Simples Nacional (Convênio ICMS nº 35/2011):**
   Nas remessas promovidas por estabelecimentos optantes pelo regime do Simples Nacional sediados em qualquer UF com destino ao Rio de Janeiro, aplica-se invariavelmente a **MVA Original**, sendo expressamente vedada a utilização da MVA Ajustada, sob pena de violação ao tratamento favorecido da LC 123/2006.

4. **Restituição e Complementação do ICMS-ST (Tema 201 STF e Lei Estadual nº 8.445/2019):**
   - O Supremo Tribunal Federal, no julgamento do RE nº 593.849/MG (Tema 201), assentou o direito do contribuinte à restituição da diferença do ICMS pago a maior sob o regime de ST para frente quando a base de cálculo real da operação for inferior à base presumida.
   - O Estado do Rio de Janeiro disciplinou a matéria através da **Lei Estadual nº 8.445/2019**, instituindo tanto a obrigação de restituição do imposto pago a maior quanto o dever de complementação pelo contribuinte substituído fluminense quando o preço praticado na venda ao consumidor for superior à base de cálculo fixada pelo regime de ST.

---

## 3. MECANISMOS DE DEDUÇÃO E TOMADA DE CRÉDITO NO ICMS FLUMINENSE

A não-cumulatividade do ICMS no Rio de Janeiro encontra suporte regulamentar no Livro I do RICMS/RJ (Decreto nº 27.427/2000) e no Livro VI da Resolução SEFAZ nº 720/2014, operando pelo confronto mensal entre créditos e débitos devidamente comprovados por documentação fiscal idônea.

```
       CICLO DE CRÉDITO E APURAÇÃO DO ICMS FLUMINENSE
       
       ENTRADA DE BENS E SERVIÇOS
       ├── Insumos Industriais (Matéria-prima / Embalagem) ───> Crédito Integral (100%)
       ├── Ativo Permanente (Máquinas / Equipamentos) ────────> CIAP: 1/48 avos/mês (Bloco G)
       ├── Energia Elétrica e Telecomunicações ───────────────> Regra Restritiva LC 87/96
       │                                                         (Exige Laudo Técnico Industrial)
       └── Uso e Consumo Geral ────────────────────────────────> Crédito Vedado até 2033
       
       APURAÇÃO MENSAL (LIVRO I RICMS / LIVRO VI RES. 720)
       ├── Total Débitos (-) Total Créditos
       ├── Manutenção Assegurada: Exportações (Art. 40 Lei 2.657/96)
       └── Hipóteses de Estorno: Saídas Isentas / Não Tributadas / Sinistros
```

### 3.1. Regras Fundamentais da Não-Cumulatividade Fluminense

1. **Princípio do Crédito Físico e Financeiro:** O direito de creditamento pressupõe que a mercadoria entrada se destine a operação de saída subsequente regularmente tributada pelo ICMS, ou integrada a processo de transformação e industrialização cujos produtos finais sejam tributados.
2. **Vedações Expressas de Crédito:**
   - Mercadorias ou serviços destinados a uso ou consumo do próprio estabelecimento (aproveitamento postergado para 1º de janeiro de 2033 pela LC 204/2023);
   - Aquisições destinadas a operações de saída isentas ou não tributadas pelo ICMS;
   - Aquisições vinculadas a prestações de serviços de transporte ou comunicação não tributadas;
   - Imposto destacado em documento fiscal emitido em desacordo com as exigências formais ou emitido por estabelecimento em situação cadastral irregular/inidônea perante a SEFAZ/RJ.
3. **Hipóteses de Estorno de Crédito:**
   - Mercadoria que vier a perecer, deteriorar-se, extraviar-se ou for objeto de furto/roubo no estabelecimento;
   - Mercadoria utilizada em fins alheios à atividade operacional da empresa;
   - Saídas posteriores com isenção ou não incidência, salvo autorização expressa em contrário da legislação.
4. **Manutenção do Crédito Fiscal:**
   - **Exportações:** O art. 40 da Lei Estadual nº 2.657/1996 e o art. 20, § 1º, da LC 87/1996 asseguram a manutenção integral dos créditos relativos à entrada de mercadorias e serviços utilizados na produção ou comercialização de mercadorias remetidas com não incidência ao exterior;
   - **Benefícios Fiscais com Manutenção Assegurada:** Hipóteses taxativas de convênios ou leis estaduais (ex: Convênio ICMS nº 100/1997 para insumos agropecuários).

### 3.2. Controle de Crédito do Ativo Permanente (CIAP - 1/48 avos)

A tomada de créditos relativos à aquisição de bens destinados ao Ativo Imobilizado rege-se pelo art. 20, § 5º, da LC 87/1996 (com redação da LC 102/2000), consolidada no Livro I do RICMS/RJ e no Anexo XI da Resolução SEFAZ nº 720/2014.

1. **Fração Mensal de Apropriação:** O montante do crédito apurado na entrada do bem é apropriado à razão de **1/48 (um quarenta e oito avos) por mês**, iniciando-se no mês em que ocorrer a sua efetiva entrada física no estabelecimento.
2. **Fator de Proporcionalidade das Operações Tributadas:**
   Em cada período de apuração mensal, o valor do crédito efetivamente aproveitável corresponde a 1/48 do imposto original multiplicado pela razão entre o valor das operações de saídas tributadas (e exportações imunes) e o total geral das saídas promovidas pelo estabelecimento:
   $$\text{Crédito CIAP}_{\text{Mês}} = \left( \frac{\text{ICMS Total do Bem}}{48} \right) \times \left( \frac{\text{Saídas Tributadas} + \text{Exportações}}{\text{Total das Saídas}} \right)$$
3. **Escrituração no Bloco G da EFD-ICMS/IPI:**
   O controle individualizado de cada bem do ativo imobilizado é escriturado compulsoriamente no Bloco G do SPED Fiscal fluminense, detalhando o código do bem, data de entrada, número de parcelas, fator de rateio mensal e saldo remanescente de quotas.
4. **Alienação ou Baixa Antecipada:**
   Se o bem for alienado, transferido, baixado ou desincorporado antes do encerramento do prazo de 48 meses, cancela-se em definitivo o direito à apropriação do saldo restante das quotas de 1/48 avos a partir da data do evento.

### 3.3. Restrições Específicas: Energia Elétrica e Telecomunicações

A apropriação de créditos decorrentes da entrada de energia elétrica e serviços de comunicação submete-se às severas travas do art. 33, incisos II e IV, da Lei Kandir (prorrogadas até 2033 pela LC 204/2023):

1. **Energia Elétrica:**
   - O crédito fiscal é estritamente admitido nas seguintes hipóteses:
     * Quando for objeto de operação de subsequente saída de energia;
     * Quando consumida diretamente em processo de industrialização;
     * Quando seu consumo resultar em operação de saída ou prestação para o exterior (proporcionalmente).
   - **Exigência de Laudo Técnico no RJ:** Para a tomada de crédito pelo estabelecimento industrial fluminense, a SEFAZ/RJ exige laudo técnico pericial de rateio de energia elétrica elaborado por engenheiro eletricista devidamente registrado no CREA/RJ, atestando o percentual efetivamente despendido nas linhas produtivas fabris, segregando a energia consumida nos setores administrativos, comerciais e de logística estática.
2. **Serviços de Comunicação:**
   - Crédito condicionado exclusivamente às hipóteses de terem sido prestados ao contribuinte para utilização em sua própria prestação de serviços de comunicação, ou quando a prestação de serviços resultar em prestação para o exterior.
3. **Incidência do FECP sobre Energia e Telecomunicações:**
   - Com o advento da Lei Complementar Federal nº 194/2022, a energia elétrica e os serviços de telecomunicação foram definidos como bens e serviços essenciais. No Rio de Janeiro, a alíquota básica foi ajustada para o patamar modal de 20%, ao qual se soma a cobrança do FECP (2%), resultando na carga de **22%**.

### 3.4. Gestão e Habilitação de Crédito Acumulado de ICMS (Sistema e-SCA)

O crédito acumulado do ICMS — originado de saídas imunes de exportação, manutenção de créditos com saídas desoneradas ou saídas tributadas a alíquotas interestaduais inferiores à carga tributária de entrada — é regido pelo Livro III do RICMS/RJ e pela **Resolução SEFAZ nº 191/2017**.

1. **Processo Eletrônico de Habilitação (e-SCA):**
   O contribuinte detentor de saldos credores acumulados não pode utilizá-los livremente sem prévio procedimento administrativo de auditoria e validação eletrônica pela SEFAZ/RJ, instaurado no Sistema de Crédito Acumulado (e-SCA). A auditoria fiscal fiscaliza a higidez de todos os documentos fiscais de entrada e o efetivo desembaraço das operações de exportação.
2. **Vias Legais de Aproveitamento do Saldo Habilitado:**
   - Compensação direta com débitos tributários próprios vincendos de ICMS na apuração normal;
   - Transferência entre estabelecimentos da mesma empresa situados no território fluminense;
   - Transferência a estabelecimentos industriais fornecedores de matérias-primas, produtos intermediários ou material de embalagem;
   - Transferência para fornecedor a título de aquisição de bens destinados ao Ativo Permanente do estabelecimento;
   - Transferência a terceiros não coligados, sujeita a expressa autorização do Secretário de Estado de Fazenda e limitada a quotas orçamentárias anuais de desoneração fixadas pela SEFAZ/RJ.

---

## 4. O REGIME DO SETOR AGRÍCOLA E RURAL FLUMINENSE

Apesar do perfil majoritariamente urbano e industrial do Estado do Rio de Janeiro, a atividade agropecuária fluminense apresenta relevância em cadeias específicas (cana-de-açúcar e etanol nas Regiões Norte e Noroeste; bacia leiteira no Médio Paraíba e Centro-Sul; hortifrutigranjeiros na Região Serrana e café arábica no Noroeste).

```
         CADEIA TRIBUTÁRIA DO SETOR AGROPECUÁRIO FLUMINENSE
         
    [Insumos Agrícolas] ──> Convênio ICMS 100/97 c/c 26/2021 (Isenção / Redução BC)
           │
    [Produtor Rural PF] ──> Inscrição CAP / NFP-e modelo 55 (Dispensa de EFD)
           │
           ├── Saída Interna (Produto em Estado Natural) ──> Diferimento (Livro XIV)
           │                                                  para Indústria/Cooperativa
           └── Saída com Transformação Própria ────────────> Programas Especiais
                                                              (Leis 4.177/03 e 5.636/10)
```

### 4.1. Insumos Agropecuários (Convênio ICMS nº 100/1997 e Convênio nº 26/2021)

1. **Internalização Fluminense:** O Estado do Rio de Janeiro aplica integralmente as desonerações previstas no Convênio ICMS nº 100/1997 para insumos utilizados na agropecuária (fertilizantes, defensivos agrícolas, calcário, sementes fiscalizadas, rações balanceadas e embriões).
2. **Impacto do Convênio ICMS nº 26/2021:**
   - O cronograma de retorno gradual da tributação sobre fertilizantes e insumos importados/interestaduais passou a escalonar as alíquotas do ICMS até alcançar 4% nas saídas interestaduais e reduzir o benefício interno, exigindo das revendas agropecuárias fluminenses segregação criteriosa nas notas fiscais emitidas a produtores locais.

### 4.2. Diferimento do ICMS na Produção Rural (Livro XIV do RICMS/RJ)

1. **Diferimento nas Saídas Internas:**
   Conforme o Livro XIV do RICMS/RJ, o imposto incidente sobre a saída interna de produtos agrícolas em estado natural promovida por produtor rural inscrito no Cadastro Agropecuário (CAP) com destino a estabelecimentos industriais, comerciais atacadistas ou cooperativas situadas no Estado do Rio de Janeiro é **diferido**.
2. **Momento do Encerramento do Diferimento:**
   O recolhimento do ICMS postergado transfere-se para o adquirente e encerra-se na subsequente:
   - Saída dos produtos para consumidor final;
   - Saída para outra unidade da Federação;
   - Saída para o exterior;
   - Saída do produto acabado resultante de seu processo de industrialização.

### 4.3. Regimes Setoriais da Agroindústria Fluminense

- **Setor Lácteo e Queijarias (Lei Estadual nº 4.177/2003):** Regime tributário especial concedendo crédito presumido e diferimento na aquisição de leite cru produzido no RJ, reduzindo a carga fiscal interna de queijos e derivados para incentivar a retenção da produção primária no Vale do Paraíba e Região Serrana.
- **Setor Sucroalcooleiro (Lei Estadual nº 5.636/2010):** Regime especial de ICMS incidente sobre o etanol combustível e a cana-de-açúcar produzida no Norte e Noroeste Fluminense (especialmente no município de Campos dos Goytacazes), com alíquota reduzida e diferimentos para fortalecer o parque industrial usineiro fluminense.

### 4.4. NFP-e e Conformidade Tributária do Produtor Rural Pessoa Física

1. **Nota Fiscal de Produtor Eletrônica (NFP-e - Modelo 55):**
   - O Estado do Rio de Janeiro aderiu ao cronograma de obrigatoriedade nacional da NFP-e (Ajuste SINIEF nº 10/2022 e alterações posteriores pelo Ajuste SINIEF nº 01/2024), extinguindo progressivamente a utilização das notas fiscais em papel modelo 4 para os produtores rurais pessoas físicas.
2. **Simplificação Cadastral e Acessória (CAP/SEFAZ):**
   - O produtor rural pessoa física sem personalidade jurídica própria é cadastrado no Cadastro Agropecuário (CAP) perante a SEFAZ/RJ.
   - É desonerado da escrituração da EFD-ICMS/IPI e do cumprimento das obrigações acessórias complexas reservadas aos estabelecimentos empresariais normais.
   - Nas aquisições de produção primária efetuadas por empresas industriais e cooperativas, prevalece a faculdade de emissão de NF-e de Entrada (contranota) pelo estabelecimento adquirente (CFOP `1.101` ou `1.102`), que documenta o trânsito da mercadoria e formaliza o encerramento do diferimento.

---

## 5. O COMPLEXO INDUSTRIAL E PETROLÍFERO FLUMINENSE

O setor industrial fluminense tem no segmento de Petróleo, Gás Natural e Apoio Marítimo Offshore a sua maior força motriz, complementado por polos industriais interiorizados nos setores metalmecânico, automotivo, químico e farmacêutico.

```
       ARQUITETURA DE INCENTIVOS INDUSTRIAIS FLUMINENSES (CONVALIDADOS LC 160/17)
       
       SETOR INDUSTRIAL / OFFSHORE NO RJ
       │
       ├── REPETRO-SPED / OFFSHORE (Lei 8.890/2020 e Res. SEFAZ 153/2020)
       │   ├── Admissão Temporária de FPSO e Sondas ───> Isenção Total de ICMS
       │   └── Aquisições Definitivas e Insumos ───────> Alíquota Efetiva de 3% (até 2040)
       │
       ├── LEI Nº 6.979/2015 (Tratamento Especial da Indústria no Interior)
       │   ├── Carga Tributária Efetiva nas Saídas ───> 3% de ICMS (incluindo FECP)
       │   └── Importação / Aquisição de Ativo/Insumo ─> Diferimento Total
       │
       └── REGIMES PORTUÁRIOS E DRAWBACK
           ├── RIOLOG (Leis 4.173/03 e 9.025/20) ──────> Desembaraço Portuário RJ Diferido
           └── Drawback (Convênio ICMS 27/1990) ───────> Suspensão na Importação com Exportação
```

### 5.1. Tomada de Crédito sobre Insumos Industriais

As indústrias fluminenses apropriam crédito do ICMS destacado nas notas fiscais de matérias-primas, produtos intermediários e materiais de embalagem, desde que consumidos imediata e integralmente no processo de fabricação ou integrados fisicamente ao produto final (critério físico-econômico do Livro I do RICMS/RJ).
- *Partes e Peças de Desgaste Mecânico:* Ferramentas, matrizes e peças de maquinário que sofrem desgaste gradativo e periódico pela ação operacional são enquadradas no Ativo Imobilizado ou em Uso/Consumo, sendo vedado o creditamento imediato de insumos fabris, permitindo-se apenas a apropriação em 48 meses quando ativadas como imobilizado fabril.

### 5.2. O Regime Especial de Óleo, Gás e Offshore: REPETRO-SPED

O Estado do Rio de Janeiro concentra o maior parque de exploração e produção de hidrocarbonetos do país (Bacia de Campos e Bacia de Santos / Pré-Sal). A desoneração das atividades de E&P offshore é regulada pelo **REPETRO-SPED** e **REPETRO-INDUSTRIALIZAÇÃO**:

1. **Marco Normativo:**
   - Convênio ICMS nº 03/2018 e Convênio ICMS nº 220/2019 (CONFAZ);
   - **Lei Estadual nº 8.890/2020**, regulamentada pelas **Resoluções SEFAZ nº 153/2020, nº 169/2020 e nº 465/2022** (Capítulo XXXVIII do Anexo XIII da Resolução SEFAZ nº 720/2014).
2. **Tratamento Tributário Distinto por Modalidade:**
   - **Admissão Temporária de Bens sem Transferência de Propriedade:** Isenção integral do ICMS e do FECP no desembaraço aduaneiro de plataformas marítimas (FPSO, semi-submersíveis), sondas de perfuração, embarcações de apoio offshore (OSVs), equipamentos submarinos e tubulações de injeção/produção submetidos ao regime de Repetro-Sped temporário.
   - **Aquisições Definitivas (Nacionais ou Importadas):** Redução da base de cálculo de forma que a **carga tributária efetiva resulte em 3% de ICMS** (já englobando o FECP), vedado o aproveitamento de créditos fiscais vinculados.
   - **Repetro-Industrialização:** Diferimento do ICMS nas operações internas e isenção nas operações interestaduais com insumos, matérias-primas e componentes fornecidos a fabricantes intermediários e finais credenciados na fabricação de bens a serem fornecidos às operadoras de petróleo.
3. **Condicionantes Rígidas de Adesão e Vigência:**
   - Formalização de Termo de Comunicação perante a Auditoria Fiscal Especializada de Petróleo e Combustíveis da SEFAZ/RJ;
   - Renúncia irretratável a litígios judiciais ou administrativos que questionem a cobrança de ICMS sobre afretamentos ou importações sem transferência de domínio;
   - Vigência assegurada legalmente até **31 de dezembro de 2040**.

### 5.3. A Lei nº 6.979/2015: Política Industrial Fluminense

Instituída para descentralizar o desenvolvimento econômico da capital e da Região Metropolitana, a **Lei Estadual nº 6.979/2015** é o principal mecanismo de incentivo à indústria transformadora no Rio de Janeiro:

1. **Benefícios Concedidos:**
   - **Carga Tributária Efetiva de 3%:** Nas saídas internas e interestaduais de produtos industrializados pelo próprio estabelecimento, o imposto é apurado mediante a aplicação direta da alíquota global de **3% sobre o faturamento industrial** (sendo 2% destinados ao ICMS ordinário e 1% ao FECP), em total substituição ao regime normal de confronto de débitos e créditos.
   - **Diferimento Amplo na Entrada:**
     * Importação de máquinas, equipamentos, partes e peças destinados ao ativo imobilizado desprovidos de similar nacional fluminense (diferido para o momento da eventual desincorporação);
     * Aquisição interna de ativo imobilizado;
     * Importação e aquisição interna de matérias-primas, produtos intermediários e embalagens (diferido para a saída do produto transformado).
2. **Territorialidade e Vedações (Lei Estadual nº 10.203/2023):**
   - Válido exclusivamente para plantas fabris instaladas nos municípios listados na lei (ex: Resende, Porto Real, Valença, Três Rios, Nova Friburgo, Campos, Macaé, entre dezenas de outros).
   - A Lei nº 10.203/2023 introduziu vedações taxativas: proibição expressa ao setor extrativo mineral bruto e fabricantes de cimento, bem como trava a transferências fraudulentas de plantas apenas para redução artificial de carga tributária.
3. **Convalidação Nacional:**
   - Convalidada perante o CONFAZ com arrimo na Lei Complementar nº 160/2017 e Cláusula Décima Terceira do Convênio ICMS nº 190/2017, garantindo a incolumidade do benefício e a segurança jurídica de créditos em outras UFs até **31 de dezembro de 2032**.

### 5.4. Regimes Portuários, Aeroportuários e Drawback

- **RIOLOG e Desembaraço no Estado:** Os incentivos fiscais vinculados às importações (como a Lei nº 4.173/2003 e a Lei nº 9.025/2020) impõem como contrapartida indispensável a realização do desembaraço aduaneiro nos recintos alfandegados situados no próprio Estado do Rio de Janeiro (Porto do Rio de Janeiro, Porto de Itaguaí, Porto do Açu e Aeroporto Internacional Tom Jobim - Galeão), sob pena de cassação imediata da desoneração.
- **Drawback Integrado (Convênio ICMS nº 27/1990):** O Rio de Janeiro adota a suspensão e a isenção do ICMS incidente na importação de mercadorias destinadas a beneficiamento, montagem ou transformação no território fluminense para posterior exportação compulsória vinculada a Ato Concessório da SECEX/MDIC.

---

## 6. O SETOR DE PRODUTO ACABADO: ATACADO, VAREJO E DISTRIBUIÇÃO

O setor atacadista e de logística de distribuição do Rio de Janeiro desempenha papel chave no abastecimento regional do Sudeste, operando em constante fiscalização de fronteiras contra a evasão tributária.

```
       OPERAÇÕES ATACADISTAS E DISTRIBUIÇÃO NO RJ (LEI 9.025/2020)
       
       MERCADORIAS IMPORTADAS / ADQUIRIDAS
       ├── Desembaraço em Portos/Aeroportos do RJ ───> ICMS Importação Diferido
       │
       ├── SAÍDAS INTERESTADUAIS (B2B)
       │   └── Carga Efetiva: 1,10% (Crédito Presumido / Sem outros créditos)
       │
       └── SAÍDAS INTERNAS (B2B)
           ├── Cesta Básica: 7%
           ├── Demais Mercadorias: 12% (10% + 2% FECP)
           └── Retenção de ICMS-ST para o Varejo Subsequente (Anexo Único)
```

### 6.1. Margens de Valor Agregado (MVA), PMPF e Barreira Fiscal

1. **Preço Médio Ponderado a Consumidor Final (PMPF):**
   Para mercadorias de consumo padronizado e alto giro (cervejas, refrigerantes, águas minerais, combustíveis e cimento), a Subsecretaria de Estado de Receita (SER/SEFAZ) publica Portarias periódicas fixando tabelas de PMPF apuradas em pesquisas amostrais de mercado. A base de cálculo do ICMS-ST é o valor da pauta fiscal, sobrepondo-se à aplicação do MVA percentual.
2. **Barreira Fiscal e Operação Foco:**
   A SEFAZ/RJ e a Secretaria de Governo operam o programa permanente da **Barreira Fiscal (Operação Foco)** nos postos de fronteira interestadual (Nhangapi/Dutra, Comendador Levy Gasparian/BR-040, Morro do Coco/BR-101 Norte, Timbó e Angra/Rio-Santos), fiscalizando cargas e exigindo a comprovação do recolhimento antecipado do ICMS-ST e do DIFAL pelas notas fiscais eletrônicas em trânsito antes do ingresso físico no território fluminense.

### 6.2. O Regime Tributário Especial do Atacado: A Lei nº 9.025/2020 (Novo Rio Log)

Para conter a migração de centros de distribuição para estados limítrofes (como o Espírito Santo e Minas Gerais), o Rio de Janeiro editou a **Lei Estadual nº 9.025/2020**, espelhando o modelo de fomento atacadista capixaba (fundamentada no § 8º do art. 3º da LC 160/2017 e Convênio ICMS 190/2017):

1. **Estrutura dos Benefícios Fiscais da Lei nº 9.025/2020:**
   - **Saídas Interestaduais:** Crédito presumido de ICMS de tal forma que a **carga tributária efetiva resulte no montante fixo de 1,10%** do valor da operação, vedado o aproveitamento de quaisquer outros créditos fiscais de entrada;
   - **Saídas Internas:** Alíquota reduzida de:
     * **7%** para mercadorias que compõem a cesta básica;
     * **12%** (sendo 10% de ICMS normal e 2% destinados ao FECP) para as demais mercadorias;
   - **Diferimento na Importação:** Diferimento total do ICMS incidente no desembaraço aduaneiro de mercadorias importadas pelo estabelecimento atacadista habilitado, transferindo o recolhimento para o momento da saída subsequente da mercadoria, **exigindo-se que o desembaraço ocorra obrigatoriamente em portos ou aeroportos do território fluminense**.
2. **Atribuição da Condição de Substituto Tributário:**
   A Lei nº 9.025/2020 erige a empresa atacadista enquadrada à condição de substituta tributária (ICMS-ST) em relação às saídas internas promovidas com destino aos estabelecimentos varejistas fluminenses nas mercadorias listadas em seu Anexo Único.
3. **Condicionantes Operacionais:**
   - Comprovação de metragem mínima de área de armazenagem física no Estado;
   - Faturamento mínimo operacional estabelecido em Termo de Acordo;
   - Depósito compulsório em favor do Fundo Orçamentário Temporário (FOT - Lei nº 8.645/2019 e Lei nº 11.071/2025).

### 6.3. O Fundo Orçamentário Temporário (FOT): Lei nº 11.071/2025 e Decreto nº 50.248/2026

Um dos temas mais sensíveis da tributação de empresas atacadistas e industriais incentivadas no Rio de Janeiro é a cobrança do Fundo Orçamentário Temporário (FOT), sucessor do antigo FEEF (Lei nº 7.428/2016).

1. **Marco Constitucional (Tema 1.386/STF):**
   O STF julgou constitucional a instituição de fundos estaduais que vinculam a manutenção de benefícios fiscais ao depósito financeiro de parcela do benefício aproveitado.
2. **A Nova Estrutura da Lei Estadual nº 11.071/2025 (Efeitos a partir de 2026):**
   A Lei Estadual nº 11.071/2025 extinguiu a alíquota única de 10% e instituiu um modelo dual de retenção regulamentado pelo **Decreto nº 50.248/2026** e Resoluções SEFAZ nº 875/2026 e 876/2026:
   - **Benefícios Fiscais Não Onerosos:** Exigência de depósito mensal escalonado no FOT que se inicia em **20% no ano de 2026**, progredindo para **25% em 2027**, **27% em 2028**, **30% em 2029**, **40% em 2030**, **50% em 2031** e atingindo **60% em 2032** sobre o valor da renúncia fiscal fruída;
   - **Benefícios Fiscais Onerosos e Condicionados (LC 214/2025):** Percentual fixo de **18,18%** sobre o benefício fruído, sem progressividade temporal;
   - **Exceções Preservadas (10%):** A ALERJ derrubou vetos governamentais em meados de 2026, mantendo a incidência especial de **10%** para segmentos protegidos como E&P de campos maduros de petróleo, a Lei nº 6.979/2015 (indústrias do interior) e a Lei nº 8.960/2020 (indústria do aço).

### 6.4. Comércio Eletrônico (E-commerce) e Responsabilidade dos Marketplaces

1. **Solidariedade Tributária dos Intermediadores Digitais:**
   Com esteio no art. 18 da Lei Estadual nº 2.657/1996 (com as atualizações promovidas pela Lei nº 9.531/2021) e nos termos do Convênio ICMS nº 166/2022, as plataformas eletrônicas e marketplaces são **responsáveis solidários** pelo recolhimento do ICMS e penalidades decorrentes de operações comerciais promovidas em seus ambientes virtuais por lojistas que não emitam documento fiscal idôneo ou que operem sem inscrição estadual válida no Rio de Janeiro.
2. **Obrigações Acessórias - DIMP:**
   As instituições de pagamento, credenciadoras de cartão de crédito e intermediadores digitais transmitem mensalmente à SEFAZ/RJ a Declaração de Informações de Meios de Pagamentos (DIMP), permitindo o cruzamento fiscal automático entre o faturamento declarado na EFD e as vendas liquidadas eletronicamente.
3. **Hubs Logísticos:**
   Grandes plataformas de e-commerce mantêm centros de distribuição em áreas estratégicas da Baixada Fluminense (Duque de Caxias, Queimados) e Sul Fluminense (Resende), usufruindo de regimes especiais de fracionamento de pedidos e emissão centralizada de documentos auxiliares (DANFE Simplificado).

---

## 7. A TRANSIÇÃO PARA O IBS / CBS DA REFORMA TRIBUTÁRIA (EC 132/2023 E LC 214/2025)

A promulgação da Emenda Constitucional nº 132/2023 e sua regulamentação pela Lei Complementar Federal nº 214/2025 impõem transformações de magnitude histórica para a política fiscal e as finanças públicas do Estado do Rio de Janeiro.

```
       CRONOGRAMA DE TRANSIÇÃO DO ICMS FLUMINENSE PARA O IBS (2026 - 2033)
       
       2026: Início dos testes operacionais (CBS 0,9% e IBS 0,1%)
       2027: Entrada em vigor integral da CBS; extinção do PIS/COFINS; início do Imposto Seletivo
       2029: Redução das Alíquotas do ICMS para 90% (Redução proporcional dos Incentivos)
       2030: Redução das Alíquotas do ICMS para 80% (Redução proporcional dos Incentivos)
       2031: Redução das Alíquotas do ICMS para 70% (Redução proporcional dos Incentivos)
       2032: Redução das Alíquotas do ICMS para 60% (Redução proporcional dos Incentivos)
       2033: EXTINÇÃO TOTAL DO ICMS FLUMINENSE E ENTRADA EM VIGOR PLENA DO IBS
```

### 7.1. Dinâmica da Arrecadação Fluminense: Princípio do Destino vs. Royalties do Petróleo

1. **A Migração da Tributação da Origem para o Destino:**
   O Rio de Janeiro, no modelo atual do ICMS, beneficia-se da cobrança tributária no local de produção de bens industriais e distribuição atacadista. Sob o IBS (Imposto sobre Bens e Serviços), o produto da arrecadação pertencerá inteiramente ao **Estado de destino do consumo final**.
   - *O Contrapeso Consumidor:* Por ser a terceira maior população do país e o segundo maior mercado consumidor estadual, o Estado do Rio de Janeiro captará substancial receita de IBS sobre bens e serviços consumidos em seu território procedentes de outras regiões do país.
2. **A Intangibilidade dos Royalties e Participações Especiais:**
   É imperativo ressaltar a distinção entre receitas tributárias e receitas patrimoniais. Os vultosos ingressos de **Royalties e Participações Especiais** da produção de petróleo e gás natural auferidos pelo Estado do Rio de Janeiro e seus municípios confrontantes (fundamentados no art. 20, § 1º, da CF/88 e Lei Federal nº 9.478/1997) **não constituem tributos** e não sofrem qualquer interferência ou revogação pela criação do IBS e da CBS.
3. **O Imposto Seletivo (IS - Art. 153, VIII da CF/88):**
   A Reforma Tributária autoriza a incidência do Imposto Seletivo sobre a atividade de extração de recursos minerais e petróleo, limitando a alíquota ao teto máximo de **1% sobre o valor de mercado do recurso extraído**. O art. 158, inciso V, e o art. 159, inciso IV, da Constituição Federal garantem a partilha de parcelas dessa arrecadação com Estados e Municípios produtores, constituindo vetor compensatório direto para o Rio de Janeiro.

### 7.2. Extinção Progressiva do ICMS e Perda dos Regimes Regionais

A transição federativa preconizada nos artigos 128 a 130 do ADCT impõe o desmonte gradual do ICMS:
- Em 2029, as alíquotas do ICMS do RJ serão reduzidas a 9/10 (90%) de seu valor;
- Em 2030, a 8/10 (80%);
- Em 2031, a 7/10 (70%);
- Em 2032, a 6/10 (60%);
- Em **1º de janeiro de 2033**, o ICMS fluminense e o FECP extinguem-se definitivamente.

**Perda da Autonomia Concessória:**
Os programas estaduais consagrados (Lei nº 6.979/2015 para a indústria, Lei nº 9.025/2020 para o atacado e incentivos portuários) sofrerão decréscimo compulsório na mesma razão matemática da redução do ICMS (2029 a 2032). Sob o IBS, gerido pelo Comitê Gestor descentralizado, fica vedada qualquer concessão de benefício fiscal individual por unidade federativa, findando a guerra fiscal interestadual.

### 7.3. Homologação e Monetização dos Saldos Credores Acumulados (Art. 134 do ADCT)

Um dos maiores desafios de transição para o empresariado fluminense reside na recuperação dos saldos credores de ICMS existentes na escrituração fiscal em **31 de dezembro de 2032**:

1. **Rito de Habilitação perante a SEFAZ/RJ:**
   - O contribuinte deverá formalizar pedido de homologação do saldo credor perante a SEFAZ/RJ nos termos e prazos estipulados pela Lei Complementar Federal nº 214/2025.
   - A SEFAZ/RJ terá prazo legal de até **24 meses** para concluir o processo de auditoria de conformidade dos créditos. Findo esse prazo sem decisão administrativa, os créditos serão considerados **tacitamente homologados**.
2. **Compensação com o IBS em 240 Parcelas Mensais:**
   - O montante do saldo homologado será aproveitado para compensar o IBS apurado pelo sujeito passivo no prazo de **240 meses (20 anos)**, à razão de 1/240 avos por mês;
   - Os valores das parcelas mensais serão corrigidos monetariamente com base no Índice Nacional de Preços ao Consumidor Amplo (**IPCA**);
   - Os créditos que não puderem ser compensados diretamente com débitos próprios de IBS poderão ser ressarcidos pelo Comitê Gestor do IBS ou transferidos a terceiros.

### 7.4. O Fundo de Compensação de Benefícios Fiscais (FCBF)

Para proteger a higidez patrimonial e os investimentos de empresas industriais que se instalaram sob a égide de incentivos do ICMS formalmente convalidados pela LC nº 160/2017, a Constituição instituiu o **Fundo de Compensação de Benefícios Fiscais (FCBF)** (art. 159-A da CF e art. 135 do ADCT):
1. **Recursos da União:** A União aportará montantes financeiros federais no FCBF, com desembolsos anuais crescentes de 2029 a 2032 (partindo de R$ 8 bilhões até alcançar patamares superiores a R$ 32 bilhões anuais).
2. **Destinatários Fluminenses:** Empresas beneficiárias da Lei Estadual nº 6.979/2015 e regimes industriais com investimentos onerosos comprovados farão jus à indenização pecuniária correspondente à perda gradativa da vantagem fiscal decorrente da extinção antecipada e paulatina do benefício estadual no período de 2029 a 2032.

---

## 8. RECOMENDAÇÕES PARA O REPOSITÓRIO E AUDITORIA DE SISTEMAS

Diante do diagnóstico elaborado, recomenda-se com prioridade crítica:

1. **Ingestão Normativa:**
   - Criação urgente de `estaduais/rj/leis/icms/lei-2657-1996.md` com a redação consolidada da Lei Geral do ICMS fluminense.
   - Expansão do arquivo `estaduais/rj/ricms/decreto-27427-2000.md` para albergar a estrutura dos 18 Livros regulamentares e seus anexos operacionais.
   - Ingestão da `Resolução SEFAZ nº 720/2014` em `estaduais/rj/resolucoes/resolucao-sefaz-720-2014.md`.
   - Adição da legislação do contencioso fiscal (Lei Estadual nº 5.427/2009 e Decreto nº 2.473/1979) e do regime parafiscal do FOT (Lei Estadual nº 8.645/2019 e Lei Estadual nº 11.071/2025).
2. **Atualização de Alíquotas e Fórmulas em Motores de Cálculo:**
   - Parametrizar a alíquota modal interna fluminense em **22% de carga efetiva** (20% de alíquota básica + 2% de FECP, conforme Lei Estadual nº 10.253/2023 vigente desde 20/03/2024);
   - Aplicar a fórmula de **Base Dupla** para o DIFAL Contribuinte nas entradas de ativo e consumo no RJ;
   - Monitorar a escalada do FOT (Lei 11.071/2025) a partir do ciclo fiscal de 2026.
3. **Mapeamento de Créditos Acumulados:**
   - Implementar regras de auditoria preventiva sobre saldos credores de ICMS para subsidiar os contribuintes no processo de homologação decenal perante o e-SCA da SEFAZ/RJ com vistas à transição para o IBS (art. 134 do ADCT).

---
*Relatório de Auditoria Técnica Fluminense elaborado com esteio na legislação da SEFAZ/RJ, CONFAZ e Supremo Tribunal Federal.*
