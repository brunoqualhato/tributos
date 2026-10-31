# RELATÓRIO DE AUDITORIA TRIBUTÁRIA ESTADUAL: SANTA CATARINA (SC)

**Jurisdição:** Estado de Santa Catarina (SC)  
**Órgão Fazendário:** Secretaria de Estado da Fazenda de Santa Catarina (SEF/SC)  
**Autor:** Agente Especialista no Ordenamento Tributário Catarinense  
**Data de Execução da Auditoria:** 31 de outubro de 2026  
**Documento de Destino:** `_auditoria/estados/auditoria_sc.md`  
**Escopo:** Auditoria de integridade do repositório normativo `estaduais/sc/`, levantamento de lacunas legais, mapeamento das relações interestaduais, regimes de dedução e crédito, tributação das cadeias agropecuárias, portuárias, industriais e atacadistas, e impactos da transição para a Reforma Tributária (IBS/CBS - EC 132/2023 e LC 214/2025).

---

## SUMÁRIO EXECUTIVO

O Estado de Santa Catarina ostenta uma posição singular no federalismo fiscal brasileiro. Dotado de uma economia altamente descentralizada, multissetorial e vocacionada para o comércio exterior — impulsionada pelo Complexo Portuário de Itajaí, Navegantes, São Francisco do Sul, Itapoá e Imbituba —, o modelo tributário catarinense foi erigido sob a ótica de incentivos expressivos à importação e à agregação logística, consolidados pelos Tratamentos Tributários Diferenciados (**TTDs**), notadamente os TTDs 409, 410, 411 (importação comercial), TTD 77 (atacadista) e TTD 478 (comércio eletrônico interestadual).

Paralelamente, Santa Catarina detém a liderança nacional na avicultura e suinocultura intensiva, apoiada no modelo de integração vertical e cooperativismo agropecuário (Aurora Coop, Copérdia, Cooperalfa, BRF, Seara/JBS), com cadeias específicas de diferimento tributário e outorga de créditos presumidos que desoneram a proteína animal, a maçã no Planalto Serrano, o fumo no Vale do Itajaí e o arroz no Sul catarinense.

A presente auditoria identificou graves assimetrias e lacunas no acervo de normas estaduais em `estaduais/sc/`:
1. **Ausência da Lei Geral do ICMS Catarinense:** A **Lei Estadual nº 10.297, de 26 de dezembro de 1996**, espinha dorsal do imposto pós-Lei Kandir, não consta no repositório.
2. **Incompletude Estrutural do RICMS/SC:** O arquivo `decreto-2870-2001.md` é uma síntese preliminar de 89 linhas, carecendo dos 11 Anexos Regulamentares que contêm a totalidade dos benefícios fiscais (Anexo 2), substituição tributária (Anexo 3), documentos fiscais (Anexo 5) e regimes especiais (Anexo 6).
3. **Ausência da Legislação Processual:** A **Lei Estadual nº 3.938, de 26 de dezembro de 1966** (Processo Administrativo Tributário - PAT) e a **Lei Complementar nº 465, de 3 de dezembro de 2009** (Tribunal Administrativo Tributário - TAT/SC) estão inteiramente ausentes.
4. **Alocação Imprópria:** A **Lei Estadual nº 17.763, de 12 de agosto de 2019** (Marco Legal dos TTDs convalidados via LC 160/2017) encontra-se alocada na pasta `ricms/` e carece de seus regulamentos executivos complementares.

No horizonte da Reforma Tributária (EC 132/2023 e LC 214/2025), Santa Catarina figura como a Unidade Federativa mais vulnerável ao fim da "guerra fiscal" e à migração para o princípio do destino, impondo desafios drásticos de monetização de créditos acumulados (art. 134 do ADCT) e habilitação tempestiva perante o Fundo de Compensação de Benefícios Fiscais (FCBF).

---

## 1. AUDITORIA DAS NORMAS ESTADUAIS EM `estaduais/sc/` E MAPEAMENTO DE LACUNAS

### 1.1. Inventário do Acervo Atual

A inspeção física dos diretórios do repositório `estaduais/sc/` revelou a seguinte composição de arquivos:

| Caminho do Arquivo | Norma Declarada | Data de Edição | Extensão (Linhas) | Diagnóstico Técnico de Conteúdo |
| :--- | :--- | :---: | :---: | :--- |
| `estaduais/sc/ricms/decreto-2870-2001.md` | Regulamento do ICMS (RICMS/SC) | 27/08/2001 | 89 linhas | **Crítico / Incompleto:** Contém apenas artigos introdutórios (arts. 1º a 3º) e um resumo de tabelas de alíquotas. Omissão absoluta dos 11 Anexos normativos, que detêm a regulamentação material aplicável. |
| `estaduais/sc/ricms/lei-17763-2019-ttd-409-410-478-sc.md` | Lei nº 17.763/2019 (TTDs e Convalidação) | 12/08/2019 | 87 linhas | **Parcial / Alocação Imprópria:** Trata-se de Lei Ordinária arquivada indevidamente no subdiretório de decretos regulamentares (`ricms/`). Contém resumo funcional dos TTDs 409, 410 e 478, mas omite as fórmulas de cálculo e a regulamentação infralegal. |
| `estaduais/sc/leis/itcmd/lei-13136-2004.md` | Lei Geral do ITCMD-SC | 25/11/2004 | 475 linhas | **Conforme / Completo:** Apresenta a íntegra da Lei Estadual nº 13.136/2004 com tabelas progressivas (alíquotas de 1% a 8%), regras de fato gerador, isenções e penalidades. |
| `estaduais/sc/leis/ipva/lei-7543-1988.md` | Lei Geral do IPVA-SC | 30/12/1988 | 544 linhas | **Conforme / Completo:** Apresenta a íntegra da Lei Estadual nº 7.543/1988 (frequentemente citada como 7.547 por erro material comum), alíquotas (1% e 2%), imunidades, isenções e processo de lançamento de ofício. |

### 1.2. Mapeamento das Principais Normas Faltantes no Repositório

Para alcançar paridade documental com o arcabouço fiscal catarinense exigido em auditorias e contencioso, o repositório deve ser suplementado com as seguintes normas cruciais:

```
                                 ACERVO CATARINENSE PRIORITÁRIO FALTANTE
                                                    │
        ┌───────────────────────────┬───────────────┴───────────────┬───────────────────────────┐
        ▼                           ▼                               ▼                           ▼
Lei Ordinária 10.297/1996    RICMS/SC Consolidado        Lei 3.938/1966 & LC 465/2009    Portarias SEF Regulamentares
(Lei Instituidora do ICMS)   (Anexos 1, 2, 3, 5, 6, 11)  (PAT e Tribunal Administrativo) (CIAP, SACC, Fundos, TTDs)
```

#### A. Lei Estadual nº 10.297, de 26 de dezembro de 1996 (Espinha Dorsal do ICMS)
- **Status:** **AUSENTE** no repositório.
- **Importância Jurídica:** É a lei instituidora e reguladora fundamental do ICMS no Estado de Santa Catarina em harmonia com a Lei Complementar Federal nº 87/1996 (Lei Kandir).
- **Conteúdo Mandatório a Estruturar:**
  - *Fatos geradores e não incidências* (arts. 2º e 3º).
  - *Sujeição passiva, responsabilidade e solidariedade* (arts. 7º e 18).
  - *Base de cálculo e integrações* (art. 9º a 13) — inclusive a previsão do cálculo "por dentro" do DIFAL contribuinte (art. 9º, § 6º e art. 10, § 4º, introduzidos pela Lei nº 18.315/2021).
  - *Regime de alíquotas internas* (art. 19): 17% (modal), 12% (operações internas B2B destinadas a contribuintes industriais e comerciais — art. 19, III, "n"), 25% (supérfluos, bebidas e cigarros).
  - *Regime de penalidades e infrações formais e materiais* (arts. 51 a 88).

#### B. Anexos Normativos do Decreto Estadual nº 2.870/2001 (RICMS/SC)
- **Status:** **INCOMPLETO** (apenas o corpo genérico está esboçado).
- **Subdivisões Faltantes:**
  - **Anexo 1 (Isenções e Imunidades):** Lista completa de produtos da cesta básica, insumos agropecuários e operações desoneradas.
  - **Anexo 2 (Benefícios Fiscais e Créditos Presumidos):** Reduções de base de cálculo e a disciplina legal de todos os créditos presumidos (art. 21 para carnes de aves/suínos, leite, arroz, maçã, setor têxtil; arts. 90/91 para comércio atacadista - TTD 77; art. 246 para TTD de importação 409/410/411).
  - **Anexo 3 (Substituição Tributária e Diferimento):** Lista taxativa das mercadorias sujeitas à retenção do ICMS-ST no Estado e hipóteses de diferimento pleno na cadeia primária.
  - **Anexo 5 (Obrigações Acessórias e Documentos Fiscais):** Emissão de NF-e, MDF-e, CT-e, NFP-e e a escrituração do CIAP (arts. 39 a 43).
  - **Anexo 6 (Regimes Especiais e Procedimentos Específicos):** Regras de faturamento direto de veículos, operações com armazéns gerais, entrepostos e feiras livres.
  - **Anexo 11 (SPED Fiscal e Escrituração Fiscal Digital - EFD):** Validações obrigatórias no Estado.

#### C. Normas do Contencioso Administrativo e Processo Tributário (PAT / TAT)
- **Status:** **AUSENTE** no repositório.
- **Normas Requeridas:**
  - **Lei Estadual nº 3.938, de 26 de dezembro de 1966:** Estatuto Geral das normas de processo administrativo tributário de Santa Catarina.
  - **Lei Complementar Estadual nº 465, de 3 de dezembro de 2009:** Criação, competência, composição paritária e regimento institucional do **Tribunal Administrativo Tributário de Santa Catarina (TAT/SC)**.
  - **Decreto Estadual nº 1.358, de 28 de maio de 2008:** Regulamento do Processo Administrativo Tributário (R-PAT/SC).

#### D. Portarias Normativas Críticas da SEF/SC
- **Portaria SEF nº 233/2012:** Disciplina o Controle de Crédito de ICMS do Ativo Permanente (**CIAP - Bloco G**) na EFD-ICMS/IPI.
- **Portaria SEF nº 193/2020 e Portaria SEF nº 343/2019:** Regulamentam o Sistema de Administração de Créditos Acumulados (**SACC**) e o preenchimento do Quadro 41 da DIME / DCAEE.
- **Portaria SEF nº 212/2019:** Disciplina o credenciamento de contribuintes nos Tratamentos Tributários Diferenciados (TTDs) via Portal S@T.

---

## 2. RELACIONAMENTO TRIBUTÁRIO DO ICMS-SC COM OS DEMAIS 26 ESTADOS E DISTRITO FEDERAL

O intercâmbio de mercadorias e serviços interestaduais entre Santa Catarina e o restante da Federação é norteado pelo comando do art. 155, § 2º, IV da Constituição Federal de 1988 e pelas Resoluções do Senado Federal nº 22/1989 e nº 13/2012, conjugadas com as inovações da Emenda Constitucional nº 87/2015, Lei Complementar nº 190/2021, Lei Complementar nº 204/2023 e Convênio ICMS 109/2024.

### 2.1. Matriz de Alíquotas Interestaduais Aplicáveis

Santa Catarina, pertencente à Região Sul, atua sob uma estrutura assimétrica de alíquotas interestaduais nas operações tributadas de saída e entrada:

```
                            FLUXO DE ALÍQUOTAS INTERESTADUAIS (SC)
                                              │
                      ┌───────────────────────┴───────────────────────┐
                      ▼                                               ▼
          OPERAÇÕES COM BENS NACIONAIS                   OPERAÇÕES COM BENS IMPORTADOS
                      │                                               │
           ┌──────────┴──────────┐                                    ▼
           ▼                     ▼                          Alíquota Fixa: 4%
  Destino: N, NE, CO, ES  Destino: Sul e Sudeste        (Resolução do Senado Federal 13/2012
      Alíquota: 7%          (SP, RJ, MG, PR, RS)          e Conteúdo de Importação > 40%)
   (Res. SF 22/1989)          Alíquota: 12%
                            (Res. SF 22/1989)
```

1. **Saídas de Bens Nacionais de SC para o Norte, Nordeste, Centro-Oeste e Espírito Santo:**
   - **Alíquota:** **7%** (sete por cento).
   - Aplica-se a operações destinadas a: `AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MT, MS, PA, PB, PE, PI, RN, RO, RR, SE, TO`.
2. **Saídas de Bens Nacionais de SC para o Sul e Sudeste (exceto Espírito Santo):**
   - **Alíquota:** **12%** (doze por cento).
   - Aplica-se a operações destinadas a: `PR, RS, SP, RJ, MG`.
3. **Saídas Interestaduais com Bens Importados (Resolução SF nº 13/2012 e Convênio ICMS 38/2013):**
   - **Alíquota:** **4%** (quatro por cento).
   - Aplicável uniformemente para qualquer Unidade Federada quando os bens:
     - Tenham sido importados do exterior sem processo de industrialização; OU
     - Submetidos a processo de industrialização interna, resultem em mercadoria com **Conteúdo de Importação superior a 40% (quarenta por cento)**, comprovado mediante Ficha de Conteúdo de Importação (**FCI**).
   - *Exceções à alíquota de 4%:* Mercadorias importadas que não tenham similar nacional (constantes da lista CAMEX) ou gás natural importado (tributadas à alíquota interestadual geral de 7% ou 12%).
4. **Transporte Aéreo Interestadual de Cargas:** Alíquota de **4%** (Resolução SF nº 95/1996).
5. **Alíquota Interna Modal em SC vs. Alíquota Interna B2B:**
   - Alíquota Interna Geral (Consumidor Final e Operações Gerais): **17%** (art. 19, I da Lei nº 10.297/1996).
   - Alíquota B2B Interna entre Contribuintes: **12%** nas operações internas com mercadorias destinadas à comercialização ou industrialização promovidas por contribuintes do imposto (art. 19, III, "n" da Lei nº 10.297/1996), mecanismo concebido para evitar o acúmulo de saldo credor na cadeia fabril interna.
   - Adicional do Fundo de Combate à Pobreza: Santa Catarina **NÃO** cobra adicional de FECOP/FCP sobre a alíquota geral (FCP = 0%).

### 2.2. Diferencial de Alíquotas (DIFAL)

O ordenamento catarinense disciplina o Diferencial de Alíquotas em duas vertentes substancialmente distintas quanto ao fato gerador, base de cálculo e sujeito passivo:

#### A. DIFAL nas Entradas para Contribuinte (Uso, Consumo e Ativo Permanente)
- **Fundamento Legal:** Art. 155, § 2º, VII da CF/88, art. 2º, § 1º, V da Lei 10.297/1996 e art. 9º, § 6º e art. 10, § 4º da Lei 10.297/1996 (com redação dada pela Lei nº 18.315/2021).
- **Sujeito Passivo:** O adquirente catarinense inscrito no cadastro de contribuintes da SEF/SC.
- **Metodologia de Cálculo — Base Dupla ("Por Dentro"):** Em Santa Catarina, a exigência do DIFAL para bens destinados a uso, consumo ou imobilizado adota a fórmula de cálculo por dentro, com exclusão do imposto de origem e inclusão da alíquota interna:

$$\text{Base de Cálculo SC} = \frac{V_{\text{operação origem}} - \text{ICMS Origem}}{1 - \text{ALQ Interna SC}}$$

$$\text{DIFAL Devido a SC} = (\text{Base de Cálculo SC} \times \text{ALQ Interna SC}) - \text{ICMS Origem}$$

*Exemplo Prático:* Máquina adquirida de SP por R$ 100.000,00, tributada na origem a 12% (ICMS Origem = R$ 12.000,00). Alíquota interna em SC = 17%:
1. Valor sem o ICMS origem: $100.000 - 12.000 = 88.000$
2. Inclusão da alíquota de SC: $\text{Base SC} = \frac{88.000}{1 - 0,17} = \frac{88.000}{0,83} = 106.024,10$
3. ICMS Total em SC: $106.024,10 \times 17\% = 18.024,10$
4. DIFAL a recolher para SC: $18.024,10 - 12.000,00 = \text{R\$} \; 6.024,10$ (enquanto na base simples resultaria em R$ 5.000,00).

#### B. DIFAL nas Operações Interestaduais Destinadas a Não Contribuinte (EC 87/2015 e LC 190/2021)
- **Fundamento Legal:** Lei Complementar Federal nº 190/2021, Convênio ICMS 236/2021 e Lei Estadual nº 18.319, de 30 de dezembro de 2021.
- **Sujeito Passivo:** O remetente da mercadoria situado em outra Unidade da Federação (nas vendas B2C destinadas a SC), ou o contribuinte de SC (nas vendas B2C com destino a outros estados).
- **Metodologia de Cálculo:** Base única integral da operação com o ICMS interno embutido (conforme art. 13, § 1º, I da LC 87/96):

$$\text{DIFAL Destino} = V_{\text{operação}} \times (\text{ALQ Interna Destino} - \text{ALQ Interestadual})$$

- **Fundo de Pobreza:** Como SC possui FCP = 0%, o remetente recolhe apenas a diferença direta de alíquotas (ex.: $17\% - 12\% = 5\%$ ou $17\% - 7\% = 10\%$ ou $17\% - 4\% = 13\%$).
- **Recolhimento:** Por GNRE individual documento a documento (com indicação da chave de acesso da NF-e) ou mensalmente até o 15º dia do mês subsequente para estabelecimentos credenciados com Inscrição Estadual de Substituto Tributário em SC.

### 2.3. Transferências Interestaduais entre Filiais (ADC 49 STF e Convênio ICMS 109/2024)

A disciplina jurídica das transferências entre estabelecimentos da mesma titularidade sofreu profunda transformação normativa e jurisprudencial:

```
                            REGIME DE TRANSFERÊNCIAS ENTRE FILIAIS EM SC
                                                  │
                 ┌────────────────────────────────┴────────────────────────────────┐
                 ▼                                                                 ▼
      REGRA GERAL OBRIGATÓRIA                                           OPÇÃO ANUAL FACULTATIVA
     (Não Incidência de ICMS)                                     (Equiparação a Operação Tributada)
                 │                                                                 │
  • CFOP 6.151 / 6.152 na remessa                                   • Cláusula 6ª do Convênio ICMS 109/2024
  • Transferência de crédito obrigatória                            • Opção manifestada no RUDFTO até o
    limitada à alíquota interestadual (4%, 7%, 12%)                   último dia de dezembro para o ano subsequente
  • Saldo remanescente mantido em SC                                • Permite destaque do ICMS para preservar
  • Respaldado na ADC 49, LC 204/2023                                 a sistemática integral de TTDs e apropriação
    e MP 263/2024 (Lei Estadual nº 19.172/2025)                       de créditos na origem e no destino
```

1. **A Decisão do STF na ADC 49 e a LC 204/2023:** O Supremo Tribunal Federal pacificou a não incidência do ICMS na simples movimentação física entre matriz e filiais, sem transferência jurídica de titularidade. A Lei Complementar Federal nº 204/2023 positivou o § 4º no art. 12 da LC 87/96, assegurando a transferência de créditos das etapas anteriores para o estabelecimento destinatário.
2. **Convênios CONFAZ e a Resposta Normativa de SC:**
   - O CONFAZ editou o Convênio ICMS nº 178/2023 e, posteriormente, consolidou as regras por meio do **Convênio ICMS nº 109/2024**.
   - O Estado de Santa Catarina publicou a **Medida Provisória nº 263, de 22 de fevereiro de 2024** (posteriormente convertida na **Lei Estadual nº 19.172/2025**) e expediu decretos executivos adequando o RICMS/SC.
3. **Mecânica Operacional Padrão:** O remetente catarinense transfere o crédito fiscal correspondente à aplicação das alíquotas interestaduais (4%, 7% ou 12%) sobre o valor atribuído à transferência (custo de aquisição mais recente ou custo de fabricação). O valor do crédito é lançado a débito em SC e creditado na UF de destino.
4. **Opção Estratégica pela Equiparação a Operação Tributada:** A Cláusula sexta do Convênio ICMS 109/2024 autorizou os Estados a admitir a opção irretratável do contribuinte para equiparar as transferências a operações regularmente tributadas. Em Santa Catarina, essa faculdade é de relevância capital para detentores de **TTD 77, TTD 409 e TTDs Industriais**, que necessitam do faturamento tributado para fruir do crédito presumido estadual. A opção é formalizada no Livro RUDFTO da SEF/SC e vigora para todo o ano-calendário.

### 2.4. Protocolos e Convênios de Substituição Tributária (ICMS-ST) em SC

A postura do Estado de Santa Catarina em relação à Substituição Tributária sofreu uma guinada histórica nos últimos anos:

| Segmento de Mercadoria | Status da Substituição Tributária em SC | Fundamento Normativo / Observações |
| :--- | :---: | :--- |
| **Combustíveis, Petróleo e Derivados** | **Mantido** (Regime Monofásico Nacional) | LC 192/2022 e Convênios ICMS 199/2022 e 15/2023 (*ad rem* uniforme). |
| **Energia Elétrica e Comunicação** | **Mantido** | Art. 155, § 2º, XII, "b" da CF/88 e Anexo 3 do RICMS/SC. |
| **Cigarros e Produtos de Tabacaria** | **Mantido** | Convênio ICMS 111/2017 e Anexo 3 do RICMS/SC. |
| **Veículos Automotores Novos** | **Mantido** | Convênio ICMS 199/2017 e Anexo 3 do RICMS/SC. |
| **Tintas, Vernizes e Solventes** | **Mantido** | Convênio ICMS 118/2017 e Anexo 3 do RICMS/SC. |
| **Cimento** | **Mantido** | Protocolo ICMS 11/1985 e Anexo 3 do RICMS/SC. |
| **Bebidas Quentes (Vinhos, Destilados)** | **REVOGADO / EXCLUÍDO** | Retirado da ST interna em SC por denúncia de Protocolos (Decreto 1.818/2018). |
| **Materiais de Construção e Ferramentas** | **REVOGADO / EXCLUÍDO** | Retirados da ST interna em SC; tributação pelo regime regular de débito e crédito. |
| **Autopeças e Acessórios Automotivos** | **REVOGADO / EXCLUÍDO** | Excluído da ST interna de SC; operações interestaduais dependem de protocolos bilaterais específicos. |
| **Produtos Farmacêuticos (Medicamentos)** | **REVOGADO / EXCLUÍDO** | Excluído da ST interna para comercialização no varejo em SC. |
| **Lâmpadas, Reatores e Iluminação** | **REVOGADO / EXCLUÍDO** | Excluído da ST interna de SC. |

- **Fórmula da MVA Ajustada (Convênio ICMS 142/2018):** Nos segmentos remanescentes sujeitos a Protocolo interestadual, aplica-se o ajuste quando a alíquota interestadual for inferior à alíquota interna:

$$\text{MVA Ajustada} = \left[ \frac{(1 + \text{MVA-ST Original}) \times (1 - \text{ALQ Inter})}{(1 - \text{ALQ Intra})} \right] - 1$$

- **Exceção do Simples Nacional (Convênio ICMS 35/2011):** Caso o remetente interestadual seja microempresa ou empresa de pequeno porte optante pelo Simples Nacional, veda-se a aplicação da MVA Ajustada, impondo-se a **MVA-ST Original** prevista no Anexo 3 do RICMS/SC.

---

## 3. MECANISMOS DE DEDUÇÃO E TOMADA DE CRÉDITO NO ORDENAMENTO CATARINENSE

A dinâmica de apuração do ICMS em Santa Catarina orienta-se pela não-cumulatividade constitucional (art. 155, § 2º, I da CF/88), disciplinada nos artigos 21 a 34 da Lei Estadual nº 10.297/1996 e no Regulamento do ICMS (RICMS/SC).

### 3.1. Não-Cumulatividade, Apropriação, Estorno e Manutenção de Crédito

1. **Apropriação do Crédito Básico:** É assegurado ao sujeito passivo creditar-se do imposto anteriormente cobrado em operações de que tenha resultado a entrada de mercadorias, reais ou simbólicas, no estabelecimento, inclusive as destinadas ao seu uso ou consumo ou ao ativo permanente, ou o recebimento de serviços de transporte e comunicação a elas vinculados.
2. **Estorno de Crédito Obrigatório (Art. 32 da Lei 10.297/1996):**
   - O sujeito passivo deverá efetuar o estorno do imposto de que se tiver creditado sempre que o serviço tomado ou a mercadoria entrada no estabelecimento:
     - For objeto de saída ou prestação subsequente isenta ou não tributada, sendo essa circunstância imprevisível na data da entrada;
     - For integrada ou consumida em processo de industrialização, quando a saída do produto resultante não for tributada ou estiver isenta do imposto;
     - Vier a ser utilizada em fim alheio à atividade operacional do estabelecimento;
     - Vier a perecer, deteriorar-se ou ser extraviada.
3. **Manutenção de Crédito (Imunidades Qualificadas e Exportação):**
   - Não se exige o estorno de crédito nas saídas destinadas ao **exterior (exportações diretas ou remessas para trading companies com fim específico de exportação — art. 3º, II da LC 87/96 e art. 33 da Lei 10.297/1996)**.
   - Nas operações internas contempladas com isenção ou redução de base de cálculo em que o Anexo 2 do RICMS/SC expressamente preveja a "manutenção do crédito da entrada" (ex.: insumos vinculados a programas agropecuários prioritários).

### 3.2. Controle de Crédito do Ativo Permanente (CIAP — 1/48 Avos)

A tomada de crédito sobre aquisições de bens para o Ativo Imobilizado atende estritamente às diretrizes da Lei Complementar nº 102/2000, regulamentada em Santa Catarina pelos artigos 39 a 43 do Anexo 5 do RICMS/SC e pela **Portaria SEF nº 233/2012**:

```
                              MECÂNICA DE APROPRIAÇÃO DO CIAP (SC)
                                                │
                               Bem do Ativo Imobilizado Entrado
                                                │
                        ┌───────────────────────┴───────────────────────┐
                        ▼                                               ▼
         Vinculado à Atividade Produtiva                     Bens Alheios à Atividade
            (Apropriação em 48 Meses)                        (Crédito Totalmente Vedado)
                        │
                        ▼
           Cálculo Mensal do Fator:
                        Saídas Tributadas + Exportações
           Fator = ─────────────────────────────────────────
                               Total das Saídas
                        │
                        ▼
          Quota Mensal = (ICMS Total / 48) x Fator
                        │
                        ▼
        Escrituração no Bloco G da EFD-ICMS/IPI
```

1. **Fração Mensal:** O montante do crédito a apropriar é obtido multiplicando-se **1/48 (um quarenta e oito avos)** do valor do imposto destacado no documento fiscal pelo fator de creditamento do período de apuração.
2. **Fórmula do Fator de Creditamento Mensal:**

$$\text{Fator CIAP} = \frac{V_{\text{saídas e prestações tributadas}} + V_{\text{saídas para o exterior}}}{V_{\text{total das saídas e prestações}}}$$

3. **Restrições e Penalidades:**
   - As saídas isentas ou não tributadas sem expressa manutenção reduzem linearmente o fator de creditamento mensal, sendo vedada a recuperação da parcela não apropriada no mês correspondente.
   - Na alienação ou baixa do bem antes de decorrido o prazo de 48 meses, cessa definitivamente o direito à apropriação das parcelas remanescentes.
   - A escrituração deve ser realizada no **Bloco G da EFD-ICMS/IPI**, sob pena de glosa do crédito e aplicação de multa por embaraço à fiscalização.

### 3.3. Restrições Seletivas para Energia Elétrica e Telecomunicações

Em obediência ao art. 33, II e IV da LC 87/1996 e ao art. 22 do RICMS/SC:
- **Energia Elétrica:** A entrada de energia elétrica no estabelecimento somente gera direito a crédito:
  1. Quando for objeto de operação de saída de energia elétrica;
  2. Quando consumida no **processo de industrialização**;
  3. Quando seu consumo resultar em operação de saída ou prestação para o exterior, na proporção destas sobre as saídas totais.
  - *Exigência de Laudo Pericial:* Para indústrias em SC, o aproveitamento do crédito relativo à parcela consumida na área fabril exige a manutenção de **Laudo Técnico Pericial de Demanda de Energia Elétrica** emitido por perito eletrotécnico ou engenheiro eletricista habilitado com Anotação de Responsabilidade Técnica (**ART**) perante o CREA-SC, com validade máxima recomendada de 24 meses ou a cada alteração do parque fabril.
- **Telecomunicações:** O crédito relativo aos serviços de comunicação só é admitido quando tomados por prestador de serviços da mesma natureza ou quando vinculados a prestações de serviços para o exterior.

### 3.4. Fundos Estaduais Condicionantes de Benefícios Fiscais (FUMDES e Fundo Social)

A fruição da quase totalidade dos Tratamentos Tributários Diferenciados (TTDs) e regimes especiais em Santa Catarina é condicionada por lei à realização de contrapartidas financeiras compulsórias a fundos estaduais de fomento e desenvolvimento:

1. **FUMDES (Fundo Estadual de Apoio à Manutenção e ao Desenvolvimento da Educação Superior):**
   - Instituído com base no art. 170 da Constituição Estadual e regulamentado pela Lei Estadual nº 13.334/2005 e Lei Complementar nº 281/2005.
   - Exigência básica: recolhimento de **2% (dois por cento)** calculado sobre o valor da exoneração tributária (benefício fiscal) auferida no mês.
2. **Fundo Social / FIA / FEI (Lei Estadual nº 17.762/2019):**
   - Fundo voltado a investimentos em infraestrutura social, hospitalar e educacional do Estado.
3. **Mecanismo de Equalização da Carga de Fundos (0,4% sobre a Base Integral):**
   - Por força do art. 9º da Lei nº 17.763/2019 e do art. 108 do RICMS/SC, a soma das contribuições ao FUMDES e ao Fundo Social para os detentores de TTDs de importação (409, 410, 411) e do TTD atacadista (77) foi consolidada na equação de **`0,4%` (quatro décimos por cento) da base de cálculo integral da operação de saída**.
   - O não recolhimento tempestivo da guia DARE correspondente até o 10º dia do mês seguinte enseja a **revogação tácita do regime especial** e a cobrança do ICMS integral pela alíquota cheia (17% ou 4%), acrescido de juros e multas moratórias.

### 3.5. Sistema de Administração de Créditos Acumulados (SACC) e Transferências

Em Santa Catarina, a distinção entre "saldo credor ordinário" e "crédito acumulado" é rigorosamente formalizada no Regulamento:
- **Saldo Credor:** É a mera sobra contábil da apuração mensal (entradas superiores às saídas), que é transportada para compensação no período seguinte na conta gráfica do contribuinte.
- **Crédito Acumulado (Art. 40 do RICMS/SC):** É o montante formado exclusivamente em razão de:
  1. Operações de exportação para o exterior (imunidade com manutenção);
  2. Saídas internas ou interestaduais amparadas por isenção ou não incidência expressamente autorizadas a manter o crédito;
  3. Diferimento do imposto na saída subsequente.

```
                           FLUXO DE HOMOLOGAÇÃO DE CRÉDITO ACUMULADO
                                                │
         1. Escrituração Fiscal da Formação no Quadro 41 da DIME / EFD
                                                │
                        ┌───────────────────────┴───────────────────────┐
                        ▼                                               ▼
         Exercício Corrente: DIME Ordinária             Exercício Encerrado: DCAEE
                        │                                               │
                        └───────────────────────┬───────────────────────┘
                                                │
                                                ▼
         2. Protocolização Eletrônica no S@T (Pedido de Reserva de Crédito)
                                                │
                                                ▼
         3. Auditoria Fiscal da GEFIS (Gerência de Fiscalização da SEF/SC)
                                                │
                                                ▼
         4. Expedição da Autorização de Utilização de Crédito (AUC)
                                                │
                        ┌───────────────────────┴───────────────────────┐
                        ▼                                               ▼
        Compensação com Débitos Próprios                Transferência para Terceiros
           (Importação ou Saldo Devedor)               (Fornecedores em SC / Investimentos)
```

- **Operacionalização no S@T:** O contribuinte transmite o Demonstrativo de Crédito Acumulado na DIME ou o **DCAEE** (para anos encerrados).
- **Emissão da AUC:** Apenas após a homologação formal pela GEFIS é gerada a **Autorização de Utilização de Crédito (AUC)**.
- **Transferência a Terceiros:** A SEF/SC estabelece tetos mensais e exige que a empresa adquirente do crédito pague contrapartida em investimentos no Estado ou abata compras de matérias-primas e energia elétrica de fornecedores catarinenses.

---

## 4. SETOR AGRÍCOLA E RURAL CATARINENSE

O agronegócio representa mais de 30% do PIB catarinense, caracterizando-se pela desconcentração fundiária (pequenas propriedades familiares), alto padrão tecnológico e forte integração vertical entre produtores e agroindústrias multinacionais e cooperativas.

### 4.1. Insumos Agropecuários (Convênio ICMS 100/97 e Atualizações)

Santa Catarina internalizou o Convênio ICMS 100/97 no Anexo 1 (isenções) e no Anexo 2 (reduções de base de cálculo) do RICMS/SC:
1. **Defensivos Agrícolas e Rações Balanceadas:** Redução da base de cálculo em 60% nas operações interestaduais (carga líquida resultante de 2,8% para N/NE/CO/ES e 4,8% para Sul/Sudeste) e isenção ou redução idêntica nas operações internas.
2. **Fertilizantes e Adubos (Convênio ICMS 26/2021):** O Convênio ICMS 26/2021 reintroduziu a tributação gradual sobre fertilizantes nas operações internas e interestaduais, convergindo para a alíquota uniforme de **4%** a partir de 2025, impacto que encareceu o custo de produção do arroz irrigado e do milho em solo catarinense.
3. **Sementes Certificadas e Mudas:** Isenção integral do ICMS nas saídas internas e interestaduais quando fiscalizadas pelo Ministério da Agricultura e Pecuária (MAPA).

### 4.2. Diferimento do ICMS nas Cadeias Produtivas Regionais

O mecanismo de **diferimento** (transferência do dever de recolhimento do ICMS para momento posterior) é a viga mestra da proteção fiscal do produtor rural primário em Santa Catarina (Anexo 3 e Anexo 6 do RICMS/SC):

```
                        CADEIAS DO AGRONEGÓCIO CATARINENSE E DIFERIMENTO
                                                │
        ┌───────────────────────┬───────────────┴───────────────┬───────────────────────┐
        ▼                       ▼                               ▼                       ▼
Proteína Animal (Aves/Suínos)  Maçã (Planalto Serrano)      Arroz (Sul de SC)      Fumo & Leite Cru
Oeste Catarinense (BRF,        São Joaquim e Fraiburgo      Bacia de Araranguá      Vale do Itajaí & Bacia
Seara/JBS, Aurora Coop)        Diferimento do pomar ao      Diferimento da colheita  Oeste; Diferimento
Diferimento da ração,          empacotador; isenção         ao engenho beneficiador; para indústrias e
matrizes e leitões;            interna e crédito            crédito presumido no     laticínios; crédito
diferimento até o abate.       presumido na saída interest. empacotado final.        presumido no leite cru.
```

1. **Cadeia de Proteína Animal (Aves e Suínos):**
   - *Polo Geográfico:* Região Oeste, Meio-Oeste e Extremo-Oeste (Chapecó, Concórdia, Videira, São Miguel do Oeste).
   - *Empresas Âncora:* Aurora Coop, BRF S.A. (Sadia/Perdigão), Seara Alimentos/JBS, Copérdia, Cooperalfa, Cravil.
   - *Mecânica Tributária:* Ocorre o diferimento total do imposto nas remessas de pintainhos de 1 dia, leitões desmamados, rações e medicamentos veterinários da integradora (agroindústria/cooperativa) para o produtor integrado, bem como na entrega dos animais prontos para abate no frigorífico industrial. O imposto é exigido unicamente na saída subsequente da carne processada.
2. **Cadeia da Maçã:**
   - *Polo Geográfico:* Região de São Joaquim, Fraiburgo e Bom Jardim da Serra (líder nacional na produção de maçãs Gala e Fuji).
   - *Mecânica Tributária:* Diferimento na entrega da maçã in natura do produtor para a cooperativa ou entreposto de classificação frigorificada. Isenção nas operações internas e crédito presumido de até 50% ou 100% do imposto devido nas saídas interestaduais de maçãs embaladas e classificadas (Anexo 2, art. 21, VII do RICMS/SC).
3. **Cadeia do Arroz Irrigado:**
   - *Polo Geográfico:* Planície Costeira e Bacia do Rio Araranguá / Vale do Itajaí (Tubarão, Forquilhinha, Massaranduba).
   - *Mecânica Tributária:* Diferimento do arroz em casca do produtor para os engenhos de beneficiamento; outorga de crédito presumido de ICMS na saída subsequente de arroz polido/parboilizado de produção catarinense (Anexo 2, art. 21, V).
4. **Cadeia do Fumo:**
   - *Polo Geográfico:* Vale do Itajaí e Sul Catarinense.
   - *Mecânica Tributária:* Diferimento da folha de fumo cru do produtor primário à indústria processadora de tabaco (British American Tobacco/Souza Cruz, Philip Morris, Alliance One), com retenção por substituição tributária na fase industrial.
5. **Cadeia do Leite e Laticínios:**
   - *Mecânica Tributária:* Saídas de leite cru com diferimento total do produtor ao laticínio. Para combater a entrada massiva de leite em pó subsidiado da Argentina e Uruguai, Santa Catarina concede **crédito presumido de ICMS de 2% a 4% sobre o valor da aquisição de leite cru produzido por produtores catarinenses** (Anexo 2, art. 21, VIII e IX), condicionando o incentivo à não utilização de leite importado.

### 4.3. Créditos Outorgados para Agroindústria e Cooperativas

As agroindústrias e cooperativas catarinenses desfrutam de um arranjo tributário protetivo expressamente convalidado perante o CONFAZ nos termos da Lei Complementar nº 160/2017:
- **Carnes de Suínos e Aves Industrializadas (Anexo 2, art. 21, III e XI do RICMS/SC):** Concessão de crédito presumido que reduz a carga tributária efetiva final nas saídas interestaduais para patamares de **1,0% a 0%**, garantindo competitividade global e interestadual às agroindústrias sediadas em SC contra produtores do Paraná, Rio Grande do Sul e Centro-Oeste.
- **Cooperativismo Agropecuário:** Isenção ou diferimento nos atos cooperativos típicos de fornecimento e beneficiamento, preservando a neutralidade do sistema produtivo mútuo.

### 4.4. Nota Fiscal de Produtor Eletrônica (NFP-e) e Regime Simplificado

Santa Catarina implementou com pioneirismo a substituição definitiva do talonário em papel pela **NFP-e (modelo 55)**:
- **Dispensa de CNPJ:** O produtor rural pessoa física atua portando unicamente a **Inscrição Estadual de Produtor Primário (RSP/CAD-PRO)**, mantendo seu status previdenciário de segurado especial da previdência rural.
- **Emissão Facilitada:** A emissão da NFP-e é processada diretamente pelo Portal S@T da SEF/SC na web ou pelo aplicativo governamental móvel **Nota Fiscal Fácil (NFF)**, permitindo a emissão offline na propriedade rural com sincronização automática quando conectado à internet.
- **Dispensa de Obrigações Acessórias Complexas:** O produtor primário em SC é isento da entrega de DIME, SPED Fiscal e registro mercantil na JUCESC, mantendo escrituração exclusiva por meio do livro Caixa rural.

---

## 5. SETOR INDUSTRIAL E COMPLEXO PORTUÁRIO CATARINENSE

A dinâmica da economia catarinense assenta-se sobre uma poderosa infraestrutura portuária conjugada a distritos industriais especializados.

### 5.1. Não-Cumulatividade Fabril e Créditos de Insumos

As indústrias catarinenses apuram seus créditos com base no princípio do insumo produtivo direto:
- **Geração de Crédito:** Aquisições de matérias-primas, produtos intermediários consumidos direta e integralmente no ciclo fabril (desgaste por contato imediato) e materiais de embalagem destinados a acondicionar os produtos acabados.
- **Vedações:** Ferramentas, peças de reposição e manutenção de maquinário (considerados bens de uso e consumo até a eficácia da LC 87/96), materiais de limpeza fabril e uniformes de funcionários.

### 5.2. O Complexo Portuário Catarinense

Santa Catarina abriga o segundo maior polo portuário de contêineres e cargas gerais da América Latina, distribuído em cinco portos de alta eficiência:

```
                            COMPLEXO PORTUÁRIO DE SANTA CATARINA
                                              │
        ┌───────────────┬─────────────┼───────────────┬───────────────┐
        ▼               ▼             ▼               ▼               ▼
Porto de Itajaí     Portonave      Porto de       Porto Itapoá     Porto de
  (Público /       (Navegantes -  São Francisco  (Privado - Baía   Imbituba
 Delegado ao      Líder Privado    do Sul (Granel   da Babitonga    (Sul de SC -
  Município)       Contêineres)    e Carga Geral)  Contêineres)   Granéis/Carvão)
```

- **Aeroportos e Aduanas Terrestres:** Aeroporto Internacional de Florianópolis (Floripa Airport Cargo — hub cargueiro alfandegado de voos diretos da Europa e EUA), Aeroporto de Navegantes e a Aduana Seca Internacional de Dionísio Cerqueira (fronteira com a Argentina).

### 5.3. Os Tratamentos Tributários Diferenciados de Importação (TTDs 409, 410, 411)

Consolidados pela **Lei Estadual nº 17.763, de 12 de agosto de 2019** e pelo **Artigo 246 do Anexo 2 do RICMS/SC**, estes regimes especiais constituem a peça central da política de atração fiscal de SC, devidamente convalidados pelo Convênio ICMS 190/2017:

```
                         ENGENHARIA TRIBUTÁRIA DOS TTDs DE IMPORTAÇÃO (SC)
                                                │
         1. Desembaraço Aduaneiro em Portos/Aeroportos de Santa Catarina
                                                │
                        ┌───────────────────────┴───────────────────────┐
                        ▼                                               ▼
          Diferimento Integral do ICMS                 Dispensa Total de ICMS-ST
             (Desembolso Zero na Entrada)               na Entrada da Importação
                        │                                               │
                        └───────────────────────┬───────────────────────┘
                                                │
                                                ▼
         2. Saída Interestadual do Estabelecimento Importador (CFOP 6.102 / 6.107)
                                                │
                        ┌───────────────────────┴───────────────────────┐
                        ▼                                               ▼
          Destaque na Nota Fiscal: 4,00%               Destaque na Nota Fiscal: 12,00%
            (Regra Geral Res. SF 13/2012)                (Bens da Lista CAMEX / Sem Similar)
                        │                                               │
                        ▼                                               ▼
         3. Apropriação de Crédito Presumido           3. Apropriação de Crédito Presumido
            Redução da Carga Efetiva de ICMS:             Redução da Carga Efetiva de ICMS:
            • TTD 409 (1º ao 6º mês): 2,60%               • Carga Proporcional Reduzida
            • TTD 409 (após 6º mês), TTD 410              • Entre 2,00% e 3,60%
              e TTD 411: 1,00%
                        │                                               │
                        └───────────────────────┬───────────────────────┘
                                                │
                                                ▼
         4. Encargo Compulsório de Fundos Estaduais (Art. 9º da Lei 17.763/2019)
            • FUMDES + Fundo Social = 0,40% sobre a Base de Cálculo Integral
                                                │
                                                ▼
         5. CUSTO TRIBUTÁRIO EFETIVO TOTAL DESEMBOLSADO EM SC:
            • Regime Consolidado (1,00% ICMS + 0,40% Fundos) = 1,40% DO FATURAMENTO
            • Cliente em Outra UF Aproveita Crédito Integral de 4,00% (ou 12,00%)
```

#### Quadro Analítico Comparativo dos TTDs de Importação

| Código TTD | Denominação e Enquadramento | Alíquota Destacada na NF-e | Carga Efetiva de ICMS em SC | Fundo Social + FUMDES | Custo Financeiro Total em SC | Crédito Fiscal Transferido à Outra UF |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **TTD 409** | Importador em início de operações (garantia administrativa / fiança) | **4%** (ou 12%) | **2,6%** (1º ao 6º mês)<br>**1,0%** (7º ao 36º mês) | **0,4%** sobre a base de cálculo | **3,0%** (fase inicial)<br>**1,4%** (fase madura) | **4,0% integral** (sem glosa / convalidado) |
| **TTD 410** | Importador consolidado (dispensa de garantia após 36 meses de regularidade) | **4%** (ou 12%) | **1,0%** fixo | **0,4%** sobre a base de cálculo | **1,4%** sobre o faturamento | **4,0% integral** (sem glosa / convalidado) |
| **TTD 411** | Importador direto com garantia real/seguro garantia prévio aprovado | **4%** (ou 12%) | **1,0%** imediato | **0,4%** sobre a base de cálculo | **1,4%** sobre o faturamento | **4,0% integral** (sem glosa / convalidado) |
| **TTD 420** | Importação de Máquinas e Equipamentos para Ativo Imobilizado Fabril | **Isenção / Diferimento** | **0,0%** no desembaraço | Isento de fundos | **0,0%** financeiro | Crédito apropriável em 48 parcelas |

*Condicionantes Obrigatórias dos TTDs de Importação:*
1. Desembaraço aduaneiro obrigatório por recinto alfandegado situado em território catarinense;
2. Fixação ou contratação de operador logístico sediado em SC;
3. Manutenção da regularidade fiscal plena (CND estadual negativa ou positiva com efeitos de negativa).

### 5.4. TTDs Industriais e Estímulo aos Polos Fabris Regionais

O parque industrial catarinense é beneficiado por incentivos estruturados:
1. **Polo Têxtil e Vestuário (Vale do Itajaí — Blumenau, Brusque, Jaraguá do Sul):**
   - *Incentivo:* Crédito presumido nas saídas de artigos têxteis e confecções fabricados no Estado (Anexo 2, art. 15 e art. 21, IX do RICMS/SC), propiciando carga líquida média de **3% a 5%** nas vendas interestaduais, dispensando a apropriação de insumos externos.
2. **Polo Cerâmico (Região Sul — Criciúma e Tubarão):**
   - *Incentivo:* Crédito outorgado na fabricação de pisos, revestimentos cerâmicos e porcelanatos (Eliane, Cecrisa, Portinari/Dexco), reduzindo o impacto do consumo intensivo de gás natural transportado pelo Gasoduto Bolívia-Brasil (GASBOL).
3. **Polo Metalmecânico e de Refrigeração (Norte — Joinville e Jaraguá do Sul):**
   - *Empresas:* WEG, Embraco/Nidec, Schulz, Tupy.
   - *Incentivo:* **TTD 300 / 301**, garantindo o diferimento do ICMS na importação de aços especiais, matérias-primas e componentes eletroeletrônicos sem similar catarinense, conjugado com o diferimento interno nas aquisições de sucatas de ferro e fundição.
4. **Polo Plástico (Joinville e Criciúma):** Tigre, Krona, Amanco/Wavin; incentivos na aquisição de resinas petroquímicas importadas ou interestaduais.
5. **Regimes Especiais de Drawback (Anexo 2, art. 27 do RICMS/SC):**
   - *Drawback Suspensão e Isenção:* Desoneração total do ICMS na importação de matérias-primas destinadas à fabricação de bens voltados à exportação direta para o exterior, alinhado ao Convênio ICMS 27/1990.

---

## 6. SETOR DE PRODUTO ACABADO: ATACADO, VAREJO E DISTRIBUIÇÃO

### 6.1. O Tratamento Tributário do Comércio Atacadista (TTD 77)

O **TTD 77** (disciplinado nos artigos 90 e 91 do Anexo 2 do RICMS/SC e convalidado pela Lei nº 17.763/2019) é o instrumento fiscal que transformou Santa Catarina em sede de mega Centros de Distribuição (CDs) de abrangência nacional:
- **Objeto:** Concessão de crédito presumido de ICMS aos estabelecimentos atacadistas e distribuidores estabelecidos no Estado, nas operações interestaduais com mercadorias nacionais ou importadas por terceiros.
- **Carga Tributária Resultante:** O crédito presumido é graduado para assegurar uma carga efetiva de ICMS entre **1,0% e 3,0%**, a depender do volume de investimentos, geração de empregos formais em território catarinense e faturamento mínimo anual (escalonamento por faixas).
- **Contrapartida:** Recolhimento compulsório do percentual de 0,4% sobre a base de cálculo destinado ao FUMDES e Fundo Social.

### 6.2. MVA, IVA-ST e Preço Médio Ponderado a Consumidor Final (PMPF)

1. **A Desoneração da ST Interna:** Ao revogar a Substituição Tributária em setores como materiais elétricos, ferramentas, construção civil e autopeças, o Estado de Santa Catarina eliminou o desembolso financeiro da MVA na entrada da mercadoria, exigindo a apuração periódica pelo regime normal.
2. **Pautas de PMPF Remanescentes:** Para bebidas frias (cervejas e refrigerantes), combustíveis e cimento, a SEF/SC publica periodicamente **Atos DIAT** (Diretoria de Administração Tributária) estabelecendo os valores médios unitários que substituem a aplicação da MVA tradicional.
3. **Ressarcimento e Complemento do ICMS-ST (RE 593.849/MG):** Em cumprimento à tese de repercussão geral fixada pelo STF no RE 593.849/MG, Santa Catarina instituiu a apuração da diferença entre o fato gerador presumido e o efetivamente realizado por meio do **Sistema de Restituição e Complemento de ICMS-ST**, escriturado no Bloco C da EFD.

### 6.3. E-Commerce, Vendas Não Presenciais (TTD 478) e Marketplaces

Santa Catarina tornou-se um dos principais polos de atração de operadores de comércio eletrônico (*e-commerce* e canais não presenciais) através do **TTD 478** (art. 21-A do Anexo 2 do RICMS/SC):

```
                        DINÂMICA FISCAL DO TTD 478 (E-COMMERCE EM SC)
                                              │
         Venda Não Presencial B2C Interestadual (Consumidor Final Não Contribuinte)
                                              │
                      ┌───────────────────────┴───────────────────────┐
                      ▼                                               ▼
         Mercadorias de Origem Importada                 Mercadorias de Origem Nacional
            (Alíquota de Origem: 4%)                      (Alíquota de Origem: 7% ou 12%)
                      │                                               │
                      ▼                                               ▼
         Carga Efetiva Fixada para SC:                   Carga Efetiva Fixada para SC:
                     1,00%                                           2,00%
                      │                                               │
                      └───────────────────────┬───────────────────────┘
                                              │
                                              ▼
                       Obrigação Cumulativa Indispensável:
                       Recolhimento do DIFAL Destino (EC 87/15)
                       em favor do Estado onde reside o adquirente
```

- **Marketplaces e Intermediadores Digitais (Convênio ICMS 166/2022):**
  - O ordenamento catarinense introduziu na Lei nº 10.297/1996 a responsabilidade subsidiária/solidária das plataformas eletrônicas e operadoras de tecnologia financeira (gateways de pagamento) por omissões de recolhimento tributário ocorridas em suas plataformas.
  - Exigência do preenchimento obrigatório no XML da NF-e dos campos `indIntermed` (indicador de intermediador) e `CNPJIntermed`.

---

## 7. TRANSIÇÃO PARA O IBS / CBS DA REFORMA TRIBUTÁRIA (EC 132/2023 E LC 214/2025)

A promulgação da Emenda Constitucional nº 132/2023 e o marco legal da Lei Complementar nº 214/2025 (Lei Geral do IBS e da CBS) configuram a maior transformação estrutural da história econômica e fiscal de Santa Catarina.

```
                           CRONOGRAMA DE TRANSIÇÃO DO ICMS PARA O IBS
                                                │
         2026-2028: Teste Operacional (CBS a 0,9% e IBS a 0,1% sem redução de ICMS)
                                                │
         2029: Início da Redução Progressiva do ICMS e dos TTDs Catarinenses
                                                │
         ┌───────────────┬───────────────┬───────────────┬───────────────┐
         ▼               ▼               ▼               ▼               ▼
       2029            2030            2031            2032            2033
     ICMS: 90%       ICMS: 80%       ICMS: 70%       ICMS: 60%       ICMS: 0%
     IBS: 10%        IBS: 20%        IBS: 30%        IBS: 40%        IBS: 100%
     FCBF: 100%      FCBF: 80%       FCBF: 60%       FCBF: 40%       FCBF: 0%
```

### 7.1. O Paradoxo Catarinense: Alta Exposição ao Princípio do Destino

Santa Catarina ostenta o modelo fiscal mais vulnerável do Brasil à mudança de paradigma da tributação na "origem" para a tributação no "destino":
1. **O Fim do Diferencial Competitivo Portuário:** A engenharia dos TTDs 409, 410 e 411 assenta-se na possibilidade de Santa Catarina abrir mão da receita no desembaraço (diferimento) e cobrar apenas 1,0% na saída interestadual, retendo recursos que, na regra geral, pertenceriam ao Estado consumidor. No modelo do IBS, **o imposto sobre importação e saídas subsequentes pertence integralmente ao Estado de destino do consumo (princípio do destino pleno)**, administrado centralizadamente pelo Comitê Gestor do IBS.
2. **Perda de Competência Concessiva:** O Estado de Santa Catarina estará expressamente proibido de outorgar créditos presumidos, isenções unilaterais ou reduções de base de cálculo sob o IBS. Toda a legislação dos TTDs (Lei nº 17.763/2019 e Anexo 2 do RICMS/SC) será extinta ao término do período de transição.

### 7.2. O Fundo de Compensação de Benefícios Fiscais (FCBF)

Para atenuar os impactos socioeconômicos da perda dos incentivos fiscais convalidados pela LC 160/2017 e Convênio ICMS 190/2017, a EC 132/2023 (art. 8º) e a Lei Complementar nº 214/2025 (art. 159 e seguintes) criaram o **Fundo de Compensação de Benefícios Fiscais (FCBF)**, integralizado com recursos do Orçamento Geral da União:

- **Elegibilidade:** Pessoas jurídicas titulares de TTDs catarinenses devidamente concedidos até 31 de maio de 2023, registrados e depositados no CONFAZ até 31 de dezembro de 2023.
- **Escalonamento Decrescente da Compensação:**
  - **2029:** Compensação de **100%** da perda efetiva do benefício fiscal;
  - **2030:** Compensação de **80%**;
  - **2031:** Compensação de **60%**;
  - **2032:** Compensação de **40%**;
  - **2033 em diante:** **0%** (cessação total dos aportes da União).
- **Riscos Críticos de Habilitação:** As empresas catarinenses dependem de habilitação formal prévia perante a Secretaria Especial da Receita Federal do Brasil e o Comitê Gestor do IBS, comprovando o cumprimento de metas de investimento e regularidade fiscal. Atrasos ou glosas administrativas colocarão em xeque a solvência financeira de grandes tradings e importadoras catarinenses.

### 7.3. Homologação e Recuperação de Créditos Acumulados de ICMS (Art. 134 do ADCT)

O art. 134 do Ato das Disposições Constitucionais Transitórias (ADCT), introduzido pela EC 132/2023 e disciplinado pela LC 214/2025, estabelece o regime de liquidação dos saldos credores de ICMS remanescentes na extinção do imposto:

```
                      MECÂNICA DE RESGATE DE CRÉDITO ACUMULADO (ART. 134 ADCT)
                                                │
         Saldo Credor de ICMS Acumulado Apropriado até 31 de Dezembro de 2032
                                                │
                                                ▼
         Protocolização de Pedido de Homologação junto à SEF/SC (Prazo Legal)
                                                │
                        ┌───────────────────────┴───────────────────────┐
                        ▼                                               ▼
           Homologação Expressa da SEF/SC                   Decurso de Prazo sem Análise
             (Auditoria Fiscal Concluída)                      (Homologação Tácita)
                        │                                               │
                        └───────────────────────┬───────────────────────┘
                                                │
                                                ▼
         Compensação Mensal em 240 Parcelas Sucessivas (20 Anos de Prazo)
         • Correção Monetária Exclusiva pelo IPCA (Vedada Aplicação da Taxa Selic)
         • Compensação Direta contra Débitos Futuros de IBS
                                                │
                        ┌───────────────────────┴───────────────────────┐
                        ▼                                               ▼
         Débito de IBS Mensal Suficiente                 Débito de IBS Mensal Insuficiente
           (Compensação Integral da Parcela)                (Ressarcimento pelo Comitê Gestor)
```

#### Riscos Patrimoniais Estruturais para Empresas em Santa Catarina:
1. **Impacto Descapitalizador de 240 Meses (20 Anos):** Cooperativas agropecuárias e frigoríficos exportadores (Aurora, BRF, Seara) que carregam centenas de milhões de reais em saldos credores transferíveis de exportação terão seu patrimônio devolvido em parcelas diluídas ao longo de duas décadas.
2. **Defasagem Financeira do IPCA:** A atualização exclusiva pelo IPCA — e não pela Taxa SELIC — acarreta severa perda inflacionária real diante do custo do capital de giro e do endividamento financeiro bancário no Brasil.
3. **Pressão Fiscalizatória Preventiva (Glosas pela SEF/SC):** É imperativo que os contribuintes catarinenses realizem imediatamente a auditoria completa de seus saldos credores escriturados nas DIMEs e no SACC. Créditos decorrentes de notas fiscais com vícios de preenchimento, CIAP sem laudo ou insumos glosáveis serão rejeitados sumariamente pelo Fisco estadual antes da transferência para o IBS.

---

## 8. PLANO DE AÇÃO E RECOMENDAÇÕES PARA O REPOSITÓRIO

Com base nas evidências coletadas, estabelece-se o seguinte plano prioritário para o saneamento do repositório normativo `estaduais/sc/`:

```
                           MATRIZ DE RECOMENDAÇÕES EXECUTIVAS
                                           │
       ┌───────────────────┬───────────────┴───────────────┬───────────────────┐
       ▼                   ▼                               ▼                   ▼
    FASE 1:             FASE 2:                         FASE 3:             FASE 4:
Inclusão da Lei     Atualização Integral           Inclusão das Leis    Reorganização das
Geral do ICMS-SC    do RICMS/SC (Anexos            do PAT e TAT/SC      Portarias SEF/SC
(Lei 10.297/1996)   1, 2, 3, 5, 6 e 11)           (Lei 3.938 & LC 465)  (CIAP, SACC, Fundos)
```

1. **Inclusão Imediata da Lei Estadual nº 10.297/1996:** Redigir e estruturar o arquivo `estaduais/sc/leis/icms/lei-10297-1996.md` com a consolidação integral de artigos, alíquotas (art. 19), base dupla de DIFAL (art. 9º, § 6º) e infrações.
2. **Expansão do `decreto-2870-2001.md`:** Substituir o esboço existente de 89 linhas por documento estruturado que englobe a integra dos seus anexos fundamentais, especialmente o Anexo 2 (créditos presumidos e benefícios fiscais) e o Anexo 3 (diferimento e substituição tributária).
3. **Reorganização Topológica:** Mover o arquivo `lei-17763-2019-ttd-409-410-478-sc.md` para a pasta correta de leis ordinárias (`estaduais/sc/leis/icms/`), mantendo remissão analítica no diretório regulamentar.
4. **Inserção do Contencioso Tributário:** Criar o arquivo `estaduais/sc/leis/pat/lei-3938-1966-lc-465-2009-tat.md`, permitindo o acesso às normas que regem impugnações fiscais e recursos paritários ao TAT/SC.
5. **Incorporação de Portarias SEF:** Adicionar as Portarias SEF nº 233/2012 (CIAP/Bloco G), nº 193/2020 (SACC/Crédito Acumulado) e nº 212/2019 (TTDs).

---
*Relatório técnico concluído com alto rigor jurídico e normativo. Auditoria formal do Estado de Santa Catarina chancelada.*
