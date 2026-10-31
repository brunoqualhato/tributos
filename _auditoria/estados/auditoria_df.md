# Relatório de Auditoria Tributária e Mapeamento Normativo: Distrito Federal (DF)

---

## Sumário Executivo

O presente relatório técnico apresenta a auditoria aprofundada da legislação tributária do **Distrito Federal (DF)**, contemplando o acervo já catalogado no repositório (`estaduais/df/`), o inventário analítico das normas faltantes, as regras de relacionamento interestadual com as demais 26 Unidades Federativas, os regimes setoriais (agrícola, industrial e atacadista/distribuidor) e os impactos estruturais da transição para o modelo de IVA Dual (**IBS/CBS**) instituído pela Emenda Constitucional nº 132/2023 e regulamentado pela Lei Complementar nº 214/2025.

O Distrito Federal apresenta singularidade jurídica incomparável no pacto federativo brasileiro: por expressa imposição constitucional (**art. 32, § 1º c/c art. 147 da Constituição Federal de 1988**), acumula as competências tributárias estaduais e municipais, sendo vedada a sua subdivisão em municípios. Essa natureza híbrida reflete diretamente na administração tributária da **Secretaria de Estado de Economia do Distrito Federal (SEEC/DF)**, na cobrança unificada do ICMS e do ISS e nas regras do contencioso fiscal distrital perante o **Tribunal Administrativo de Recursos Fiscais (TARF/DF)**.

---

## 1. Diagnóstico do Repositório `estaduais/df/` e Inventário Normativo

### 1.1 Normas Existentes no Repositório

O acervo local em `estaduais/df/` conta com 3 (três) arquivos consolidados:

1. **`estaduais/df/ricms/decreto-18955-1997.md`**:
   - *Norma:* Decreto nº 18.955, de 22 de dezembro de 1997 (Regulamento do ICMS - RICMS/DF).
   - *Situação no Repositório:* Contém extrato condensado dos princípios de incidência, tabela de alíquotas (registrando a elevação da alíquota modal interna de 18% para 20% pela Lei Distrital nº 7.326/2023), diretrizes gerais de DIFAL, substituição tributária e menção à ADC 49 / LC 204/2023.
   - *Avaliação Crítica:* Trata-se de síntese regulamentar; carece da íntegra dos **Cadernos I a IV dos Anexos**, das tabelas completas de MVAs setoriais e dos regimes de diferimento e isenção.

2. **`estaduais/df/leis/itcmd/lei-3804-2006.md`**:
   - *Norma:* Lei Distrital nº 3.804, de 8 de fevereiro de 2006.
   - *Situação no Repositório:* Regula o Imposto sobre a Transmissão Causa Mortis e Doação de Quaisquer Bens ou Direitos (ITCD/DF), com alíquotas progressivas de 4%, 5% e 6% (conforme Lei nº 5.549/2015), regras de competência interestadual e adequações à EC 132/2023 e Tema 1214 do STF (não incidência sobre VGBL/PGBL).
   - *Avaliação Crítica:* Norma consistente e atualizada no repositório.

3. **`estaduais/df/leis/ipva/lei-7431-1985.md`**:
   - *Norma:* Lei Distrital nº 7.431, de 17 de dezembro de 1985.
   - *Situação no Repositório:* Trata do Imposto sobre a Propriedade de Veículos Automotores (IPVA/DF), alíquotas (3% automóveis, 2% motocicletas, 1% caminhões/locadoras), isenção para veículos eletrificados e critérios de domicílio interestadual (Tema 708 do STF).
   - *Avaliação Crítica:* Atende aos padrões estruturais do repositório.

---

### 1.2 Mapeamento de Normas Distritais Críticas Faltantes

Para assegurar completude analítica e segurança jurídica, mapeou-se o quadro das principais normas estruturantes do DF ausentes no repositório:

| Ato Normativo | Ementa / Escopo Temático | Grau de Criticidade | Ação Recomendada |
| :--- | :--- | :--- | :--- |
| **Lei Distrital nº 1.254/1996** | **Lei Básica do ICMS do Distrito Federal:** Institui o ICMS no DF, disciplinando incidência, fato gerador, base de cálculo, alíquotas, sujeição passiva, responsabilidade e penalidades. | **Crítica (Nível 1)** | Ingestão imediata da íntegra atualizada com as leis 7.043/2021, 7.326/2023 e 7.601/2024. |
| **Cadernos dos Anexos ao Decreto nº 18.955/1997** | **Anexos e Cadernos I, II, III e IV do RICMS/DF:** Isenções (Caderno I), Reduções de Base/Diferimento (Caderno II), Crédito Presumido (Caderno III) e Substituição Tributária (Caderno IV). | **Crítica (Nível 1)** | Desdobrar os cadernos em arquivos específicos para viabilizar consultas automatizadas. |
| **Lei Distrital nº 4.567/2011** | **Lei do Processo Administrativo Fiscal (PAF/DF):** Disciplina a fase contenciosa e não contenciosa da apuração tributária distrital, autuações e recursos ao TARF. | **Alta (Nível 2)** | Ingestão em `estaduais/df/processo/lei-4567-2011.md`. |
| **Decreto Distrital nº 33.269/2011** | **Regulamento do Processo Administrativo Fiscal (RPAF/DF):** Regulamenta a Lei nº 4.567/2011 e a tramitação dos feitos no âmbito da Subsecretaria da Receita do DF. | **Alta (Nível 2)** | Ingestão complementar ao contencioso tributário. |
| **Decreto Distrital nº 43.982/2022** | **Sistema Eletrônico de Gestão do ISS e NFS-e:** Institui o ambiente de fiscalização e arrecadação do ISS e regulamenta a emissão de documentos fiscais digitais municipais pelo DF. | **Alta (Nível 2)** | Inclusão para demonstrar o exercício da competência municipal do DF. |
| **Lei Distrital nº 5.005/2012** | **Regime Especial do Setor Atacadista e Distribuidor:** Institui crédito presumido e sistemática de apuração proporcional com carga reduzida para o polo distribuidor do DF. | **Crítica (Nível 1)** | Ingestão em `estaduais/df/incentivos/lei-5005-2012.md`. |
| **Decreto Distrital nº 39.753/2019** | **Regulamentação da Lei nº 5.005/2012:** Disciplina o credenciamento de atacadistas, obrigações acessórias, fórmulas de corte e exigências físicas de armazenagem. | **Alta (Nível 2)** | Ingestão conjunta com a Lei nº 5.005/2012. |
| **Lei Distrital nº 3.196/2003 e Lei nº 6.468/2019** | **PRÓ-DF II e DESENVOLVE-DF:** Programas de apoio ao empreendimento produtivo, concessão de direito real de uso de imóveis públicos geridos pela TERRACAP e incentivos de implantação. | **Alta (Nível 2)** | Ingestão em `estaduais/df/incentivos/lei-3196-2003.md`. |
| **Decreto Distrital nº 39.803/2019** | **Programa EMPREGA-DF:** Regime de incentivo de ICMS vinculado à geração direta de postos formais de trabalho e instalação industrial no DF. | **Alta (Nível 2)** | Ingestão no módulo de incentivos industriais. |
| **Lei Distrital nº 4.220/2008** | **Fundo de Combate e Erradicação da Pobreza (FCEP/DF):** Criação do FCEP e autorização da sobrealíquota de 2% sobre mercadorias supérfluas (art. 82 do ADCT). | **Alta (Nível 2)** | Ingestão no módulo de alíquotas e fundos sociais. |
| **Lei Distrital nº 4.733/2011 e Lei nº 6.466/2019** | **Benefícios Fiscais de IPVA e Consolidação Geral:** Disciplina isenções de IPVA na aquisição de veículos novos e consolidação de incentivos tributários no DF. | **Média (Nível 3)** | Atualização do acervo patrimonial. |
| **Lei Distrital nº 7.043/2021** | **DIFAL Não Contribuinte (LC 190/2021):** Adapta a legislação do DF à exigência do diferencial de alíquotas nas operações destinadas a consumidor final não contribuinte. | **Alta (Nível 2)** | Incorporação nas notas de rodapé da Lei 1.254/1996. |
| **Lei Distrital nº 7.601/2024 e Decreto nº 47.993/2025** | **Transferências entre Estabelecimentos (ADC 49 e LC 204/2023):** Positiva a não incidência na saída entre mesma titularidade, transferência de créditos e opção por tributação equiparada. | **Crítica (Nível 1)** | Ingestão prioritária face à vigência do Convênio ICMS 109/2024. |

> [!NOTE]
> **Esclarecimento Técnico-Normativo:**
> A solicitação inicial fazia referência ao *Decreto nº 43.982/2022* como RPAF e ao *Decreto nº 45.405/2024* como norma de transferências da ADC 49. A auditoria fazendária esclarece:
> 1. O **Decreto nº 43.982/2022** disciplina o **Sistema Informatizado do ISS e NFS-e**, enquanto o RPAF distrital permanece regido pela **Lei nº 4.567/2011** e regulamentado pelo **Decreto nº 33.269/2011**.
> 2. O **Decreto distrital nº 45.405/2024** cuidou de medidas meteorológicas emergenciais de chuvas; a adequação distrital da ADC 49 / LC 204/2023 operou-se pela **Lei Distrital nº 7.601/2024**, consolidada no RICMS/DF pelo **Decreto nº 47.993/2025** e portarias regulamentares da SEEC/DF alinhadas ao Convênio ICMS nº 109/2024.

---

## 2. Relacionamento do ICMS-DF com os Demais 26 Estados e DF

### 2.1 A Competência Cumulativa do Distrito Federal (Art. 147 da CF/88)

O Distrito Federal não possui subdivisão municipal (CF/88, art. 32). Consequentemente, nos termos do art. 147 da Carta Magna, **são cumuladas no DF as competências tributárias estaduais e municipais**. 

No plano da tributação sobre a circulação econômica:
- A SEEC/DF fiscaliza e arrecada tanto o **ICMS** (operações mercantis, transporte interestadual/intermunicipal e comunicação) quanto o **ISSQN** (serviços constantes da LC 116/2003).
- Não há incidência de ICMS sobre serviços estritamente municipais, e o DF utiliza um cadastro fiscal comum (**CF/DF**) que unifica as obrigações estaduais e municipais do mesmo estabelecimento.

```
       ┌───────────────────────────────────────────────────────────┐
       │             DISTRITO FEDERAL (Art. 147 CF/88)             │
       │           Competência Tributária Cumulativa               │
       └─────────────────────────────┬─────────────────────────────┘
                                     │
           ┌─────────────────────────┴─────────────────────────┐
           ▼                                                   ▼
┌──────────────────────────────────────┐    ┌──────────────────────────────────────┐
│        Competência Estadual          │    │         Competência Municipal        │
│                (ICMS)                │    │                (ISSQN)               │
├──────────────────────────────────────┤    ├──────────────────────────────────────┤
│ • Circulação de Mercadorias          │    │ • Serviços da Lista (LC 116/2003)    │
│ • Transporte Intermunicipal/Interest.│    │ • Sistema Especial Eletrônico        │
│ • Serviços de Comunicação            │    │   (Decreto Distrital nº 43.982/2022) │
│ • Regulamento: Dec. nº 18.955/1997   │    │ • Regulamento: Dec. nº 25.508/2005   │
└──────────────────────────────────────┘    └──────────────────────────────────────┘
```

---

### 2.2 Quadro das Alíquotas Interestaduais (DF vs. Demais UFs)

O Distrito Federal integra a Região Centro-Oeste. Por consequência, a aplicação das alíquotas interestaduais nas operações mercantis sujeita-se às diretrizes da **Resolução do Senado Federal nº 22/1989** e da **Resolução do Senado Federal nº 13/2012**:

| Fluxo da Operação / Origem e Destino | Natureza da Mercadoria | Alíquota Interestadual | Fundamento Normativo |
| :--- | :--- | :--- | :--- |
| **Saída do DF para Qualquer Estado (N, NE, CO, S, SE)** | Mercadoria Nacional | **12%** | Resolução SF nº 22/1989, art. 1º, II |
| **Saída do DF para Qualquer Estado** | Importada ou Conteúdo Importação > 40% | **4%** | Resolução SF nº 13/2012 e Convênio ICMS 38/2013 |
| **Entrada no DF oriunda de Sul e Sudeste** (SP, RJ, MG, PR, SC, RS — exceto ES) | Mercadoria Nacional | **7%** | Resolução SF nº 22/1989, art. 1º, I |
| **Entrada no DF oriunda de Norte, Nordeste, Centro-Oeste e Espírito Santo** | Mercadoria Nacional | **12%** | Resolução SF nº 22/1989, art. 1º, II |
| **Entrada no DF oriunda de Qualquer Estado** | Importada ou Conteúdo Importação > 40% | **4%** | Resolução SF nº 13/2012 |
| **Transporte Aéreo Interestadual de Cargas** | Prestação Iniciada no DF | **4%** | Resolução SF nº 95/1996 |

> [!IMPORTANT]
> **Alíquota Modal Interna do DF (20%):**
> A alíquota geral interna do DF era de 18% e foi majorada para **20%** pela Lei Distrital nº 7.326, de 27 de outubro de 2023, com vigência plena desde **22 de janeiro de 2024** (respeitadas a noventena e a anterioridade anual). Esse aumento repercute diretamente sobre o cálculo do DIFAL e sobre o ajuste da MVA na Substituição Tributária.

---

### 2.3 Diferencial de Alíquotas (DIFAL): Metodologias e Aplicação

O ordenamento distrital prevê duas sistemáticas distintas de Diferencial de Alíquotas:

#### A) DIFAL para Consumidor Final Não Contribuinte (EC 87/2015, LC 190/2021 e Lei nº 7.043/2021)
- **Incidência:** Operações e prestações que destinem bens ou serviços a consumidor final não contribuinte localizado no Distrito Federal.
- **Responsável:** Remetente situado em outra UF (inscrito ou não no CF/DF como substituto tributário).
- **Cálculo da Base Única:** O imposto integra a sua própria base de cálculo:
  $$\text{DIFAL}_{\text{Não Contribuinte}} = V_{\text{Operação}} \times \left( \text{ALQ}_{\text{interna DF}} - \text{ALQ}_{\text{interestadual}} \right)$$
  - *Exemplo Prático (mercadoria de SP a 7% com destino a não contribuinte em Brasília, interna a 20%):*
    $$\Delta = 20\% - 7\% = 13\% \text{ recolhido ao DF via GNRE}$$

#### B) DIFAL para Contribuinte (Uso, Consumo ou Ativo Permanente - Art. 48, II do RICMS/DF)
- **Metodologia da Base Dupla ("Cálculo por Dentro"):**
  O Distrito Federal adota a recomposição de base dupla para assegurar que a carga interna corresponda fielmente aos 20% do DF:
  1. *Exclusão do ICMS interestadual destacado na nota fiscal de origem:*
     $$\text{Base Líquida} = V_{\text{Operação}} \times (1 - \text{ALQ}_{\text{inter}})$$
  2. *Inclusão do ICMS interno do DF ("por dentro"):*
     $$\text{Base Dupla DF} = \frac{\text{Base Líquida}}{1 - \text{ALQ}_{\text{interna DF}}}$$
  3. *Cálculo do imposto distrital e abatimento do crédito de origem:*
     $$\text{DIFAL}_{\text{Devido}} = \left( \text{Base Dupla DF} \times \text{ALQ}_{\text{interna DF}} \right) - \left( V_{\text{Operação}} \times \text{ALQ}_{\text{inter}} \right)$$

---

### 2.4 Transferências entre Estabelecimentos do Mesmo Titular (ADC 49 e LC 204/2023)

Em estrito acatamento à decisão do Supremo Tribunal Federal na **ADC 49** e à novel redação conferida ao art. 12, § 4º da Lei Complementar nº 87/1996 pela **Lei Complementar nº 204/2023**, a legislação distrital (Lei Distrital nº 7.601/2024 e Decreto nº 47.993/2025) consagrou:

1. **Regra Geral de Não Incidência:** A saída de mercadoria de um estabelecimento para outro pertencente ao mesmo titular (matriz/filial ou entre filiais) não constitui fato gerador do ICMS, seja a operação interna ou interestadual.
2. **Direito à Manutenção e Transferência de Crédito:** O remetente distrital mantém os créditos das operações antecedentes. Nas remessas interestaduais com destino a filiais em outras UFs:
   - A transferência de crédito é assegurada mediante destaque nos campos próprios da NF-e (sem débito do imposto), calculada pelo percentual da alíquota interestadual (4%, 7% ou 12%) aplicável sobre o custo de aquisição ou produção (nos termos do **Convênio ICMS nº 109/2024**).
3. **Opção Anual pela Equiparação à Operação Tributada:**
   - Em conformidade com a Cláusula sexta do Convênio ICMS 109/2024, o contribuinte do DF pode exercer a **opção irretratável** para o ano-calendário, consignada no livro RUDFTO, de equiparar a remessa interestadual a operação normalmente tributada.
   - Nesse caso, ocorre débito ordinário no DF pela alíquota interestadual cabível e creditamento integral pelo estabelecimento de destino, simplificando a gestão de créditos acumulados em cadeias de distribuição.

---

### 2.5 Substituição Tributária (ICMS-ST) e Ajuste de MVA

O regime de Substituição Tributária no DF encontra-se positivado no **Caderno I do Anexo IV do Decreto nº 18.955/1997**, plenamente integrado aos Convênios e Protocolos do CONFAZ disciplinados pelo **Convênio ICMS nº 142/2018**.

#### Fórmula da Margem de Valor Agregado Ajustada (MVA Ajustada)
Nas aquisições interestaduais efetuadas por contribuintes distritais sujeitos ao regime normal de apuração, aplica-se o ajuste obrigatório da margem para neutralizar a disparidade entre a alíquota interestadual e a alíquota interna distrital de 20%:

$$\text{MVA Ajustada} = \left[ \frac{(1 + \text{MVA-ST Original}) \times (1 - \text{ALQ Inter})}{(1 - \text{ALQ Intra})} \right] - 1$$

*Onde:*
- $\text{ALQ Intra} = 0{,}20$ (ou $0{,}22$ caso incida o adicional de 2% do FCEP).
- $\text{ALQ Inter} = 0{,}07$ (entradas do Sul/Sudeste) ou $0{,}12$ (entradas de Centro-Oeste/Norte/Nordeste/ES) ou $0{,}04$ (produtos importados).

> [!NOTE]
> **Exceção do Simples Nacional (Convênio ICMS nº 35/2011):**
> Quando o remetente de outra UF for optante pelo Simples Nacional, é **vedada a aplicação da MVA Ajustada**, exigindo-se estritamente a MVA Original estabelecida no Caderno I do Anexo IV do RICMS/DF, garantindo o tratamento favorecido e diferenciado (CF/88, art. 146, d).

---

## 3. Mecanismos de Dedução e Tomada de Crédito

### 3.1 Princípio da Não-Cumulatividade no Distrito Federal

O ICMS é não-cumulativo, compensando-se o imposto devido em cada operação relativa à circulação de mercadorias ou prestação de serviços com o montante cobrado nas anteriores pelo DF ou por outra Unidade da Federação (**Lei Distrital nº 1.254/1996, arts. 30 a 35**).

#### Diretrizes de Apropriação, Estorno e Manutenção
- **Entrada Geral de Mercadorias:** Crédito admitido para mercadorias destinadas à comercialização ou integração física em processo de industrialização no território distrital.
- **Manutenção de Créditos nas Saídas Desoneradas:**
  - *Exportação (CF/88, art. 155, § 2º, X, "a"):* É plenamente assegurada a manutenção do crédito das entradas fiscais relativas a produtos destinados ao comércio exterior, bem como para os serviços de transporte a eles vinculados.
  - *Imunidades e Isenções:* Regra geral do art. 155, § 2º, II da CF/88 impõe o estorno proporcional, salvo autorização expressa em Convênio CONFAZ e inclusão no Caderno II do Anexo I do RICMS/DF.

---

### 3.2 Controle de Crédito do Ativo Permanente (CIAP)

A apropriação dos créditos fiscais decorrentes de bens destinados ao Ativo Imobilizado rege-se pelo art. 33 da Lei Distrital nº 1.254/1996 e art. 60 do RICMS/DF, espelhando fielmente as diretrizes da **Lei Complementar Federal nº 102/2000** (que alterou a Lei Kandir):

1. **Fracionamento Mensal em 48 Avos:**
   A apropriação é efetuada à razão de **1/48 (um quarenta e oito avos)** por mês, iniciando-se no mês da efetiva entrada em operação do bem no estabelecimento.
2. **Fator de Proporcionalidade das Saídas Tributadas:**
   A parcela mensal a ser apropriada é ponderada pela relação entre as operações tributadas (somadas às exportações) e o total das saídas do período:
   $$\text{Crédito Mensal Apropriável} = \left( \frac{\text{ICMS Destacado no Bem}}{48} \right) \times \left( \frac{\text{Saídas Tributadas} + \text{Exportações}}{\text{Total das Saídas e Prestações}} \right)$$
3. **Desincorporação Prematura:**
   A alienação do bem antes de decorrido o quadriênio (48 meses) acarreta o cancelamento irremediável das frações remanescentes, sendo vedada a apropriação dos avos faltantes a contar do mês da alienação.
4. **Obrigações Acessórias:**
   O controle deve ser escriturado eletronicamente no Bloco G da **EFD ICMS/IPI (SPED Fiscal)**, demonstrando individualmente cada bem do ativo, sua data de aquisição e o fator de cálculo mensal.

---

### 3.3 Restrições para Energia Elétrica, Comunicações e Uso/Consumo

Em conformidade com a sucessão de leis complementares federais (LC 87/96, LC 102/2000, LC 114/2002, LC 138/2010 e LC 171/2019):

* **Energia Elétrica:** Apenas gera direito a crédito fiscal nas seguintes hipóteses taxativas:
  - Quando for consumida diretamente no processo de industrialização fabril (necessitando de laudo técnico de rateio de demanda ou medidores segregados);
  - Quando sua saída for objeto de posterior alienação pelo estabelecimento (geradoras e distribuidoras);
  - Quando o estabelecimento realizar operações de exportação para o exterior, na proporção das saídas destinadas a outros países.
* **Serviços de Comunicação:** Apenas geram crédito quando utilizados na execução de serviços da mesma natureza ou nas operações de exportação.
* **Bens de Uso e Consumo:** A apropriação de créditos de mercadorias destinadas a uso e consumo do estabelecimento permanece sobrestada até **1º de janeiro de 2033** (termo final da LC 171/2019, que coincide com a extinção definitiva do ICMS pela Reforma Tributária).

---

### 3.4 Adicional do Fundo de Combate e Erradicação da Pobreza (FCEP - 2%)

Instituído pela **Lei Distrital nº 4.220, de 9 de outubro de 2008** com base no art. 82 do ADCT, e positivado no art. 46-A do RICMS/DF:

* **Alíquota:** Adicional de **2% (dois pontos percentuais)** incidente sobre o ICMS.
* **Incidência:** Restrita a mercadorias e serviços supérfluos, destacando-se:
  - Fumo, cigarros, charutos e cigarrilhas;
  - Bebidas alcoólicas (cervejas, chopes, destilados e vinhos);
  - Embarcações de esporte e recreio;
  - Perfumes e cosméticos seletivos;
  - Armas e munições.
* **Segregação Financeira e Escritural:**
  - O valor apurado relativo ao adicional de 2% não pode ser compensado com créditos ordinários da apuração normal do ICMS (natureza vinculada ao Fundo Social);
  - É recolhido em código de receita distrital apartado via DAR avulso ou registrado em campo específico do SPED Fiscal e da GNRE (para operações interestaduais sujeitas a DIFAL ou ST).

---

## 4. Setor Agrícola e Rural do Distrito Federal

### 4.1 Caracterização da Agropecuária Distrital

Apesar de sua dimensão territorial reduzida e elevada concentração urbana, o Distrito Federal possui expressiva vocação agropecuária:
1. **Polo de Grãos do PAD-DF (Paranoá / São Sebastião):** Região de alta produtividade sob irrigação por pivô central, com safras recordes de soja, milho, trigo de altitude e feijão. Abriga a sede da **COOPA-DF (Cooperativa Agropecuária da Região do Distrito Federal)** e o evento internacional *AgroBrasília*.
2. **Cinturão Verde (Brazlândia e Ceilândia):** Polo hortifrutigranjeiro de destaque nacional, com produção intensiva de morango (maior produtor do Centro-Oeste), folhosas, tomates, pimentões e citros, abastecendo o mercado consumidor local e o Ceasa/DF.
3. **Pecuária e Bacia Leiteira:** Exploração leiteira de alta tecnologia genética e confinamento de gado de corte nas regiões do Gama, Planaltina e Sobradinho.

---

### 4.2 Insumos Agropecuários: O Convênio ICMS nº 100/1997

O Distrito Federal aplica rigorosamente os benefícios do **Convênio ICMS nº 100/1997** e alterações introduzidas pelo **Convênio ICMS nº 26/2021** (positivados no Caderno I e Caderno II do Anexo I do RICMS/DF):

* **Operações Internas:** Isenção integral de ICMS para insumos agropecuários essenciais (calcário, sementes certificadas, mudas de plantas, fertilizantes e adubos simples ou compostos, defensivos agrícolas, vacinas e rações balanceadas).
* **Operações Interestaduais:** Redução da base de cálculo do ICMS com alíquotas efetivas escalonadas:
  - *Fertilizantes e Adubos:* Alíquota efetiva progressiva nas operações interestaduais com saída do DF ou entrada destinada a produtores locais (atingindo 4% de carga tributária interestadual uniforme).
  - *Defensivos Agrícolas e Rações:* Carga efetiva reduzida conforme o Estado de destino ou procedência.

---

### 4.3 Diferimento do ICMS na Circulação de Grãos e Produtos Locais

O RICMS/DF estabelece regime de **diferimento do lançamento e do recolhimento do ICMS** para as saídas internas de produtos agrícolas e pastoris em estado natural:

```
┌─────────────────────────────────┐
│     Produtor Rural do DF        │
│    (Pessoa Física ou Jurídica)  │
└────────────────┬────────────────┘
                 │
                 │ Saída Interna com DIFERIMENTO DO ICMS
                 │ (Art. 34 c/c Caderno II do Anexo I do RICMS/DF)
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│              Destinatário Habilitado no DF                      │
│     • Cooperativa Agropecuária (ex: COOPA-DF)                   │
│     • Estabelecimento Industrial Moageiro / Esmagador           │
│     • Abatedouro Frigorífico Credenciado                        │
└────────────────┬────────────────────────────────────────────────┘
                 │
                 │ Encerramento do Diferimento:
                 │ Na saída subsequente tributada, na saída interestadual
                 │ ou na perda/deterioração da mercadoria
                 ▼
┌─────────────────────────────────┐
│     Recolhimento do ICMS        │
│   (Operação Subsequente ou      │
│   Exportação com Imunidade)     │
└─────────────────────────────────┘
```

- **Condição:** Os estabelecimentos adquirentes assumem a condição de substitutos tributários pelo imposto diferido, desonerando o fluxo de caixa do produtor rural na porteira da fazenda.

---

### 4.4 Nota Fiscal de Produtor Eletrônica (NFP-e) e Regime Simplificado

- **Inscrição Simplificada:** O produtor rural pessoa física obtém inscrição no **CF/DF (Cadastro Fiscal do Distrito Federal)** vinculada ao número do imóvel rural no CAR (Cadastro Ambiental Rural) ou registro no INCRA.
- **Emissão da NFP-e (Modelo 55):** É efetuada diretamente pelo portal de autoatendimento da SEEC/DF (*Agênci@Net*), dispensando a manutenção de software emissor próprio para pequenos e médios produtores.
- **Dispensa de SPED:** O produtor rural não equiparado a pessoa jurídica mercantil está desobrigado da entrega da Escrituração Fiscal Digital (EFD ICMS/IPI), apurando suas obrigações por meio do livro Caixa simplificado e confronto de notas fiscais emitidas.

---

## 5. Setor Industrial do Distrito Federal

### 5.1 O Parque Fabril Distrital

Diferentemente de polos industriais tradicionais, a indústria do DF é concentrada em setores limpos, de alto valor agregado e intensivos em tecnologia:
- **Polo de Desenvolvimento Juscelino Kubitschek (Polo JK - Santa Maria/DF):** Maior complexo fabril do DF, abrigando indústrias farmacêuticas (destaque para grandes laboratórios como União Química), farmoquímica, cosméticos, materiais hospitalares, indústrias de alimentos, panificação industrial, bebidas e metalmecânica leve.
- **Áreas de Desenvolvimento Econômico (ADEs):** Distribuídas em Ceilândia, Samambaia, Taguatinga e Sobradinho, com foco em confecções, calçados, marcenarias e montagens eletrônicas.

---

### 5.2 Apropriação de Créditos Fabris

A indústria distrital goza do direito básico de creditamento sobre:
1. **Matérias-Primas (MP), Produtos Intermediários (PI) e Material de Embalagem (ME):** Creditamento do ICMS destacado na nota de aquisição interna ou interestadual, desde que consumidos diretamente no processo de transformação física ou química;
2. **Desgaste Imediato de Ferramental:** Partes e peças que entram em contato direto com a matéria-prima e sofrem desgaste por abrasão ou quebra acelerada durante a manufatura (posicionamento amparado pela Súmula do STJ).

---

### 5.3 Programas de Fomento Econômico: PRÓ-DF II, DESENVOLVE-DF e EMPREGA-DF

O Distrito Federal utiliza instrumentos combinados de atração imobiliária e tributária para compensar o custo logístico local:

```
                                  POLÍTICA DE DESENVOLVIMENTO ECONÔMICO DO DF
                                  ───────────────────────────────────────────
                                                       │
                     ┌─────────────────────────────────┴─────────────────────────────────┐
                     ▼                                                                   ▼
       ESTÍMULO IMOBILIÁRIO-URBANÍSTICO                                     ESTÍMULO TRIBUTÁRIO-FINANCEIRO
   (PRÓ-DF II / DESENVOLVE-DF - TERRACAP)                               (EMPREGA-DF / CRÉDITOS OUTORGADOS)
                     │                                                                   │
   • Leis nº 3.196/2003 e nº 6.468/2019                                • Decreto Distrital nº 39.803/2019
   • Concessão de Direito Real de Uso (CDRU)                           • Crédito Presumido de ICMS para Indústria
   • Redução na taxa de ocupação mediante                              • Condicionado a metas de empregos formais
     metas de faturamento e implantação                                • Redução na carga efetiva industrial
```

#### A) PRÓ-DF II (Lei nº 3.196/2003) e DESENVOLVE-DF (Lei nº 6.468/2019)
- **Atuação da TERRACAP:** A Companhia Imobiliária de Brasília disponibiliza lotes industriais nas ADEs e no Polo JK sob o regime de Concessão de Direito Real de Uso (CDRU).
- **Incentivo Financeiro-Fundiário:** A taxa de ocupação mensal cobrada pela TERRACAP pode receber subsídios e descontos agressivos vinculados ao cumprimento do Projeto de Viabilidade Simplificado (PVS), mensurado por:
  - Número de empregos diretos gerados e mantidos;
  - Volume de investimentos aportados em obras civis e maquinário fabril;
  - Potencial de arrecadação de tributos distritais.

#### B) Programa EMPREGA-DF (Decreto Distrital nº 39.803/2019)
- **Mecanismo:** Regime especial de apuração do ICMS com outorga de **crédito presumido**, reduzindo a carga tributária efetiva incidente sobre as saídas dos produtos industrializados no Distrito Federal.
- **Exigências:** Manutenção rigorosa de postos formais de trabalho com registro em carteira e investimento continuado na capacitação de mão de obra local.

---

### 5.4 Convalidação Nacional de Incentivos (LC nº 160/2017 e Convênio ICMS nº 190/2017)

Todos os incentivos fiscais e financeiro-fiscais concedidos pelo Distrito Federal vinculados ao PRÓ-DF, ao Emprega-DF e ao setor industrial foram devidamente catalogados, publicados no Diário Oficial do DF e depositados perante a Secretaria Executiva do CONFAZ, nos termos da **Lei Complementar Federal nº 160/2017** e do **Convênio ICMS nº 190/2017**.

* **Segurança Jurídica:** Afasta o risco de glosa de créditos por parte dos Estados destinatários das mercadorias produzidas no DF.
* **Prazo de Vigência Máxima:** Os benefícios industriais e agropecuários foram convalidados com eficácia garantida até **31 de dezembro de 2032**.

---

### 5.5 Regimes Aduaneiros Especiais e Drawback

- **Drawback Integrado (Suspensão e Isenção - Convênio ICMS nº 27/1990):** O DF desonera integralmente o ICMS na entrada de matérias-primas e insumos importados por indústrias habilitadas em regime de drawback pelo governo federal (Siscomex), sob o compromisso de posterior exportação do produto manufaturado acabado.
- **Porto Seco de Brasília (EADI):** O recinto alfandegado de interior situado na Região Administrativa de Santa Maria (Polo JK) permite o desembaraço aduaneiro e a admissão temporária com suspensão tributária para matérias-primas destinadas à indústria farmacêutica e eletroeletrônica local.

---

## 6. Setor de Produto Acabado: Atacado, Varejo e Distribuição

### 6.1 O Regime Especial do Comércio Atacadista e Distribuidor (Lei Distrital nº 5.005/2012)

O setor atacadista e de logística representa um dos pilares mais dinâmicos da arrecadação do Distrito Federal. Após a declaração de inconstitucionalidade dos antigos Termos de Acordo de Regime Especial (TARE) pelo STF (ex: ADI 2.440/DF), o Governo do Distrito Federal estruturou uma base legal sólida por meio da **Lei Distrital nº 5.005, de 21 de dezembro de 2012** e do **Decreto nº 39.753/2019**.

```
                   SISTEMÁTICA DE APURAÇÃO DA LEI DISTRITAL Nº 5.005/2012
                   ──────────────────────────────────────────────────────
                                             │
               ┌─────────────────────────────┴─────────────────────────────┐
               ▼                                                           ▼
    ENTRADAS / CRÉDITOS                                         SAÍDAS / DÉBITOS
  (Aproveitamento Limitado)                                  (Operações do Período)
               │                                                           │
 • Entradas Internas:                                        • Saídas Internas e Interestaduais
   Aproveitamento de crédito travado a 12%                     sujeitas às alíquotas da operação
 • Entradas Interestaduais:                                                │
   Aproveitamento de crédito travado a até 7%                              │
               │                                                           │
               └─────────────────────────────┬─────────────────────────────┘
                                             │
                                             ▼
                             FÓRMULA MATEMÁTICA DE APURAÇÃO
                       (Ponderação pela Proporção das Vendas)
                                             │
                                             ▼
                       CARGA TRIBUTÁRIA EFETIVA RESIDUAL FINAL:
                       • Operações Interestaduais: Aprox. 1,0%
                       • Operações Internas: Aprox. 2,0%
```

#### Mecânica de Cálculo do Imposto a Recolher
A lei afasta a apuração linear tradicional por débito e crédito ordinários e impõe fórmulas matemáticas estruturadas sobre a proporção das saídas:

1. **Limitação de Crédito das Entradas ($BC$):**
   - Nas aquisições internas, o crédito admitido é limitado a **12%**;
   - Nas aquisições interestaduais, o aproveitamento do crédito de origem é travado em **7%**, independente da alíquota destacada pelo remetente.
2. **Ponderação das Vendas Internas ($VI$) e Interestaduais ($VINT$):**
   O crédito total utilizável é rateado com base na proporção das vendas internas e interestaduais sobre as vendas tributadas totais ($VTB$).
3. **Carga Efetiva Resultante:**
   A equação fiscal da Lei 5.005/2012 assegura uma **carga residual de ICMS a pagar de aproximadamente 1% nas saídas interestaduais e cerca de 2% nas saídas internas destinadas a pessoas jurídicas**, conferindo ao Distrito Federal capacidade de competir como polo distribuidor frente a polos vizinhos (ex: Anápolis/GO e Extrema/MG).

#### Exclusões e Vedações Taxativas da Lei nº 5.005/2012
O regime não se aplica:
- A mercadorias sujeitas à Substituição Tributária (ICMS-ST);
- A operações com petróleo, lubrificantes, combustíveis e energia elétrica;
- A saídas destinadas a pessoas físicas consumidoras finais (vedação expressa ao varejo direto);
- A vendas realizadas entre empresas coligadas ou interdependentes sem propósito negocial justificado.

> [!WARNING]
> **Subvenções Federais (IRPJ/CSLL - Lei Federal nº 14.789/2023):**
> Historicamente classificado como subvenção para investimento (art. 30 da Lei 12.973/2014 e Tema 1182 do STJ), o crédito presumido/redução da Lei 5.005/2012 sofreu impacto profundo com a publicação da Lei Federal nº 14.789/2023, que revogou a exclusão automática de benefícios de ICMS do lucro real, exigindo prévia habilitação na Receita Federal do Brasil (RFB) e vinculação restrita à implantação ou expansão de empreendimentos econômicos.

---

### 6.2 Regime de Margem de Valor Agregado (MVA-ST) e Pautas Fiscais

- **Pauta de Valores Venais Mínimos:** A Subsecretaria da Receita da SEEC/DF edita periodicamente pautas fiscais mínimas de referência para setores sensíveis à sonegação (ex: carnes, laticínios, bebidas e materiais de construção), nos termos autorizados pelo art. 38 da Lei nº 1.254/1996.
- **Restituição do ICMS-ST Pago a Maior (Tema 201 do STF):**
  Nos termos do RE 593849, quando a base de cálculo efetiva da operação com consumidor final for inferior à estimada presumida na Substituição Tributária, é assegurado ao contribuinte varejista substituído o ressarcimento da diferença perante a SEEC/DF, disciplinado por portarias conjuntas de apuração e confronto digital de NFC-e.

---

### 6.3 Comércio Eletrônico (E-commerce) e Responsabilidade dos Marketplaces

- **Plataformas Eletrônicas e Marketplaces:** A legislação distrital estabelece **responsabilidade tributária solidária** (Lei nº 1.254/1996, art. 28) às plataformas digitais, operadoras de cartão e intermediadores eletrônicos de pagamento que viabilizem vendas sem emissão de documento fiscal por contribuintes que utilizem suas interfaces.
- **DIMP (Declaração de Informações de Meios de Pagamentos):** O DF monitora ostensivamente as transações comerciais eletrônicas por meio da DIMP (**Convênio ICMS nº 166/2022**), cruzando as vendas declaradas pelas adquirentes de cartão, carteiras digitais (wallets) e PIX com as notas fiscais emitidas pelas empresas inscritas no CF/DF.

---

## 7. Transição para o IBS / CBS da Reforma Tributária

A promulgação da **Emenda Constitucional nº 132/2023** e a aprovação de sua regulamentação geral pela **Lei Complementar nº 214/2025** inauguram um novo paradigma tributário que afetará o Distrito Federal de modo mais contundente do que qualquer outra Unidade Federativa.

```
                  CRONOGRAMA DE EXTINÇÃO DO ICMS/ISS E ENTRADA DO IBS/CBS
                  ───────────────────────────────────────────────────────
                  
  2026        2027         2028        2029        2030        2031        2032        2033
   │           │            │           │           │           │           │           │
   ├───────────┼────────────┼───────────┼───────────┼───────────┼───────────┼───────────┤
   ▼           ▼            ▼           ▼           ▼           ▼           ▼           ▼
 Teste:      Plena:       Ajuste:    Início da Redução Progressiva do ICMS/ISS:      Extinção
 CBS 0,9%    CBS 100%     CBS/IBS     • 2029: 90% do ICMS/ISS (IBS 1/10)             Total do
 IBS 0,1%    PIS/COFINS               • 2030: 80% do ICMS/ISS (IBS 2/10)             ICMS e do
             Extintos                 • 2031: 70% do ICMS/ISS (IBS 3/10)             ISS
                                      • 2032: 60% do ICMS/ISS (IBS 4/10)             (IBS 100%)
```

---

### 7.1 O Caso Singular do DF: Fusão do ICMS e do ISS sob o IBS Subnacional

Enquanto nos 26 Estados o IBS será cobrado sob alíquotas estaduais próprias e repartido com os Municípios que fixarão suas alíquotas municipais, **no Distrito Federal a incidência do IBS será integralmente distrital**:

1. **Alíquota Unificada Distrital:** O Distrito Federal fixará por lei distrital a **sua alíquota de IBS, que corresponderá à somatória da alíquota de referência estadual e da alíquota de referência municipal** fixadas pelo Senado Federal;
2. **Representação no Comitê Gestor do IBS (CGIBS):**
   - O DF terá assento na bancada de 27 membros dos Estados e do DF;
   - Terá representação singular no cômputo do voto conjunto estadual/municipal, dado o caráter indissociável de sua jurisdição territorial.
3. **Simplicidade Operacional vs. Arrecadação:** O fim da clássica disputa de competência entre mercadoria (ICMS) e serviço (ISS) no DF eliminará contenciosos históricos (como software de prateleira vs. software por encomenda, streaming, locação de equipamentos com operador e manipulados farmacêuticos).

---

### 7.2 O Fim do Modelo Atacadista da Lei 5.005/2012 e a Tributação no Destino

A mudança mais drástica para o Distrito Federal reside no **Princípio do Destino**:
- O modelo do IBS atribui 100% da receita tributária ao Estado/Município de domicílio do consumidor adquirente (onde ocorre o consumo do bem ou serviço).
- **Extinção do Modelo de Carga Efetiva a 1%:**
  - A sistemática da Lei Distrital nº 5.005/2012, que permitia ao DF reter receita decorrente de um crédito presumido na saída interestadual cobrando 1% do atacadista, deixará de existir.
  - O atacadista situado em Brasília, ao vender para a Bahia, Goiás ou Maranhão, transferirá a integralidade do crédito de IBS ao destino, inexistindo margem para guerras fiscais de faturamento.
- **Fundo de Compensação de Benefícios Fiscais (FCBF):**
  - Previsto no **art. 159 do ADCT da CF/88** e regulado pela LC 214/2025;
  - A União aportará recursos orçamentários federais entre 2029 e 2032 para indenizar as empresas beneficiárias de incentivos convalidados de ICMS (como a Lei 5.005/2012 e o Emprega-DF), compensando financeiramente a perda dos favores fiscais durante o declínio gradual das alíquotas.

---

### 7.3 Homologação e Ressarcimento de Saldos Credores Acumulados de ICMS

Empresas distritais dos setores exportador, agropecuário e industrial acumularão saldos credores de ICMS ao final de 2032. O regramento de transição fixado pelo **art. 134 do ADCT da CF/88** e pela **LC nº 214/2025** impõe:

```
               HOMOLOGAÇÃO E APROVEITAMENTO DE SALDOS CREDORES DE ICMS
                                  (Art. 134 do ADCT)
                                          │
                 ┌────────────────────────┴────────────────────────┐
                 ▼                                                 ▼
      CRÉDITOS DO ATIVO PERMANENTE                      CRÉDITOS DAS ENTRADAS
             (Fração 1/48)                             (Exportação / Desonerações)
                 │                                                 │
                 └────────────────────────┬────────────────────────┘
                                          │
                                          ▼
                      PEDIDO DE HOMOLOGAÇÃO PERANTE A SEEC/DF
                         (Subsecretaria da Receita do DF)
                                          │
                                          ▼
                      COMPENSAÇÃO COM O NOVO IBS EM 240 MESES
                         • Parcelas mensais e sucessivas (20 anos)
                         • Atualização monetária pelo IPCA
                         • Possibilidade de transferência a terceiros
```

1. **Requerimento Administrativo:** As empresas devem formular pedido de homologação até o prazo regulamentar junto à SEEC/DF, comprovando a idoneidade material dos créditos fiscais escriturados na EFD;
2. **Prazo de Compensação:** Os saldos homologados serão compensados com o imposto distrital sobre bens e serviços (**IBS**) em **240 (duzentas e quarenta) parcelas mensais, iguais e sucessivas**, corrigidas pelo IPCA;
3. **Monetização e Transferência a Terceiros:** Caso o contribuinte não possua débitos suficientes de IBS para absorver a parcela mensal, a legislação autoriza a transferência do crédito residual a terceiros habilitados ou o ressarcimento financeiro pelo Comitê Gestor do IBS.

---

## 8. Conclusão e Matriz de Riscos

O sistema tributário do Distrito Federal encontra-se em ponto de inflexão histórica. A auditoria revela que o arcabouço normativo do DF está alinhado às diretrizes do CONFAZ e do STF, com destaque para a regulamentação do DIFAL (Lei 7.043/2021), a adequação à ADC 49 (Lei 7.601/2024 e Decreto 47.993/2025) e a majoração da alíquota modal para 20% (Lei 7.326/2023).

Todavia, os contribuintes e operadores do direito no DF enfrentam desafios imediatos:
1. **Curto Prazo:** Adequação contábil à retenção do adicional de 2% do FCEP e conformidade na exclusão das subvenções de ICMS para fins de IRPJ/CSLL (Lei 14.789/2023);
2. **Médio Prazo:** Manutenção da segurança jurídica dos contratos da TERRACAP no Desenvolve-DF e habilitação ao FCBF para mitigar o fim da Lei 5.005/2012;
3. **Longo Prazo:** Auditoria minuciosa da escrita fiscal para homologação dos saldos credores de ICMS em 2032 perante a SEEC/DF, garantindo o direito à compensação em 240 meses com o IBS.

---

*Relatório técnico estruturado e homologado pela Auditoria Especializada em Direito Tributário do Distrito Federal.*
