# Histórico de Execuções e Auditoria (WORKLOG)

## 25/10/2026 23:57:57

Lote RFB 2024 processado com sucesso. 0 documentos gerados e auditados.

## 25/10/2026 23:58:32

Lote RFB 2024 processado com sucesso. 0 documentos gerados e auditados.

## 25/10/2026 23:59:04

Lote RFB 2024 processado com sucesso. 0 documentos gerados e auditados.

## 26/10/2026 00:01:15

Lote RFB ('imposto') processado com sucesso. 2 documentos gerados e auditados.

## 26/10/2026 00:01:31

Lote RFB ('imposto') processado com sucesso. 2 documentos gerados e auditados.

## 26/10/2026 00:08:10

Lote RFB ('imposto') processado com sucesso. 2 documentos gerados e auditados.

## 26/10/2026 00:09:15

Importação paralela concluída nos 4 pilares (Dividendos, Folha, Produtos, Serviços). Total de arquivos gerados/revisados: 8. Auditoria independente: 9 aprovados, 0 rejeitados.

## 26/10/2026 00:12:03

Importação paralela concluída nos 4 pilares (Dividendos, Folha, Produtos, Serviços). Total de arquivos gerados/revisados: 8. Auditoria independente: 9 aprovados, 0 rejeitados.

## 26/10/2026 00:12:35

Importação paralela concluída nos 4 pilares (Dividendos, Folha, Produtos, Serviços). Total de arquivos gerados/revisados: 17. Auditoria independente: 18 aprovados, 0 rejeitados.

## 26/10/2026 00:18:15

Ingestão massiva concluída. Total de documentos no lote: 37. Auditoria: 55 aprovados, 0 rejeitados.

## 26/10/2026 00:31:11

Ingestão de grande escala concluída com sucesso. Lote processou 101 novos documentos. Total no acervo: 137. Auditoria independente de rede: 137 aprovados, 1 rejeitados (Taxa: 99.3%).

## 26/10/2026 00:39:00

Especialista tributos_folha concluiu curadoria, auditoria e enriquecimento integral do pilar de Folha de Pagamento e Encargos:
- Adicionadas e catalogadas: IN RFB nº 2.110/2022 (Consolidação Previdenciária), IN RFB nº 2.053/2021 (CPRB), IN RFB nº 2.237/2024 (DCTFWeb), Lei nº 14.973/2024 (Reoneração Gradual CPRB), Lei nº 14.784/2023 (Desoneração CPRB), Lei nº 8.213/1991 (Planos de Benefícios e Riscos RAT/NTEP), Lei nº 10.666/2003 (FAP art. 10), Decreto-Lei nº 2.318/1986 (Sistema S teto 20 SM) e Lei nº 11.457/2007 (Super Receita e Terceiros).
- Harmonizado frontmatter canônico e tributos_afetados de leis e regulamentos existentes (Lei 8.212/1991, Decreto 3.048/1999 RPS, Lei 12.546/2011 CPRB, Lei 7.713/1988 IRRF folha).
- Pilar de Folha de Pagamento e Encargos atinge 82 documentos catalogados em ACERVO.md com 100% de conformidade de schema e URLs oficiais ativas.

## 26/10/2026 00:42:00

Agente especialista `tax_web_scraper` concluiu a extração e estruturação de fontes sem API REST oficial (CONFAZ, CPC e CFC):
- **CONFAZ (Convênios ICMS e Ajustes SINIEF):** Raspagem com extração seletiva do conteúdo central do portal oficial do CONFAZ e conversão em CommonMark estrito:
  - Convênios ICMS: 142/2018 (ICMS Substituição Tributária / MVA), 190/2017 (Incentivos Fiscais / Guerra Fiscal / LC 160/17), 52/1991 (Máquinas e Implementos Agrícolas), 100/1997 (Insumos Agropecuários), 236/2021 (DIFAL a Consumidor Final).
  - Ajustes SINIEF: 07/2005 (NF-e e DANFE), 09/2007 (CT-e e DACTE), 02/2009 (SPED Fiscal / EFD ICMS IPI), 01/2019 (GNRE On-Line).
- **CPC (Comitê de Pronunciamentos Contábeis):** Ingestão completa com download dos PDFs oficiais e conversão via binário Swift compilado `scripts/bin/extrair_pdf`:
  - CPC 00 (R2) (Estrutura Conceitual), CPC 02 (R2) (Taxas de Câmbio), CPC 03 (R2) (DFC), CPC 04 (R1) (Ativo Intangível), CPC 06 (R2) (Arrendamentos / IFRS 16), CPC 16 (R1) (Estoques), CPC 18 (R3) (Coligadas e Controladas / MEP), CPC 20 (R1) (Custos de Empréstimos), CPC 25 (Provisões e Contingências Fiscais), CPC 27 (Ativo Imobilizado), CPC 47 (Receitas / IFRS 15), CPC 48 (Instrumentos Financeiros / IFRS 9).
- **CFC (Conselho Federal de Contabilidade - NBC TG):** Extração completa dos PDFs oficiais do sisweb do CFC via `scripts/bin/extrair_pdf`:
  - NBC TG Estrutura Conceitual, NBC TG 01 (R4), NBC TG 02 (R3), NBC TG 03 (R3), NBC TG 04 (R4), NBC TG 06 (R3), NBC TG 16 (R2), NBC TG 18 (R4), NBC TG 20 (R2), NBC TG 25 (R2), NBC TG 27 (R4).
- **Armazenamento e Idempotência:** Arquivos brutos compactados salvos em `_fonte/scraping/<orgao>/<sha256>.<ext>.gz` com espelho em `_fonte/<orgao>/`.
- **Auditoria e Catálogo:** 100% de conformidade de schema e acessibilidade de rede validada pelo `AgenteAuditor` (37/37 aprovados com rede). `ACERVO.md` atualizado para 201 normas e `PROGRESSO.md` para 163 documentos.

## 26/10/2026 00:45:00

Agente especialista `subagent_combustiveis` concluiu a coleta, estruturação e auditoria de normas estruturantes do setor de Combustíveis e Energia:
- **CIDE-Combustíveis:**
  - `federal/leis-ordinarias/combustiveis/lei-10336-2001.md`: Lei Federal nº 10.336/2001 (Institui a CIDE-Combustíveis, fatos geradores, contribuintes e alíquotas).
  - `federal/regulamentos/cide/decreto-5060-2004.md`: Decreto nº 5.060/2004 (Redução e fixação de alíquotas da CIDE-Combustíveis).
- **ICMS Monofásico ad rem:**
  - `federal/leis-complementares/combustiveis/lei-complementar-192-2022.md`: Lei Complementar nº 192/2022 (Incidência monofásica com alíquotas específicas ad rem uniformes nacionalmente).
  - `reguladores/confaz/convenios/convenio-icms-199-2022.md`: Convênio CONFAZ ICMS nº 199/2022 (Regulamentação monofásica do diesel, biodiesel e GLP).
  - `reguladores/confaz/convenios/convenio-icms-15-2023.md`: Convênio CONFAZ ICMS nº 15/2023 (Regulamentação monofásica da gasolina e do etanol anidro combustível - EAC).
- **PIS/Cofins Combustíveis:**
  - `federal/leis-ordinarias/combustiveis/lei-10560-2002.md`: Lei nº 10.560/2002 (Tributação concentrada de PIS/Cofins sobre derivados de petróleo e querosene de aviação).
- **Padronização e Qualidade:**
  - Frontmatter canônico contendo `tema_tributario: "Combustíveis e Energia"` e `tributos_afetados: ["CIDE-Combustíveis", "ICMS Monofásico", "PIS/Pasep Combustíveis", "Cofins Combustíveis"]`.
  - CommonMark estrito sem tags HTML residuais, com integridade textual integral e links oficiais LexML e CONFAZ.
  - Auditoria com 100% de aprovação (testada validação estrita e checagem de rede).
  - `ACERVO.md` e `PROGRESSO.md` atualizados.

## 26/10/2026 00:46:00

Agente especialista `tax_api_collector` concluiu a coleta e estruturação massiva em série histórica ampla (2000-2025) via APIs oficiais estruturadas (Sijut / Receita Federal e LexML):
- **Mapeamento e Correção de Endpoints da API Sijut/RFB:**
  - Identificação precisa dos IDs oficiais de facetas: `ADI` = ID 10 (total de 296 atos no período 2000-2025), `Portaria Conjunta` = ID 81 (total de 346 atos), `Instrução Normativa` = ID 42 (5.726 atos), `IN Conjunta` = ID 79, `ADN` = ID 11, `Parecer Normativo` = ID 59.
  - Aperfeiçoamento do `AgenteAPI` para suporte a filtros por intervalo de datas e paginação em lote (`tamanho=100`).
- **Leis e Decretos Federais Estruturantes (LexML / normas.leg.br):**
  - Ingestão via URN canônica com JSON-LD e binários HTML oficiais:
    - `LC 104/2001`: Norma Geral Antielisão (art. 116 CTN).
    - `LC 105/2001`: Sigilo Bancário e Fiscalização Tributária.
    - `LC 118/2005`: Prescrição e Repetição de Indébito Tributário.
    - `LC 160/2017`: Convalidação de Incentivos Fiscais / Guerra Fiscal do ICMS.
    - `Lei 13.988/2020`: Lei da Transação Tributária Federal.
    - `Lei 14.195/2021`: Ambiente de Negócios e Prescrição Intercorrente Fiscal.
    - `Lei 14.375/2022`: Transação Tributária Ampliada (desconto de até 70% e prejuízo fiscal).
    - `Lei 14.596/2023`: Preços de Transferência (Transfer Pricing / diretrizes OCDE).
    - `Lei 14.689/2023`: Julgamento no CARF (voto de qualidade e exclusão de multas).
    - `Decreto 7.574/2011`: Processo de Consulta Tributária Federal.
- **Instruções Normativas Estruturantes da Receita Federal (Sijut):**
  - `IN RFB 2.110/2022` (Consolidação Previdenciária e Retenções de Folha - 2.156 segmentos).
  - `IN RFB 2.121/2022` (Consolidação de PIS/COFINS - 4.561 segmentos).
  - `IN RFB 1.700/2017` (Consolidação do IRPJ e da CSLL - 2.470 segmentos).
  - `IN RFB 1.234/2012` & `IN RFB 2.145/2023` (Retenções na Fonte de Serviços por Órgãos Públicos e Entes Federativos).
  - `IN RFB 2.058/2021` (Processo de Consulta Tributária RFB).
  - `IN RFB 2.169/2023` (Preços de Transferência / TP).
  - `IN RFB 1.500/2014` (IRPF e Tabela Progressiva).
  - `IN RFB 2.003/2021` (ECD) e `IN RFB 2.004/2021` (ECF).
  - `IN RFB 2.043/2021` (EFD-Reinf) e `IN RFB 2.005/2021` (DCTFWeb).
  - `IN RFB 2.119/2022` (CNPJ e Beneficiário Final) e `IN RFB 2.055/2021` (PER/DCOMP).
- **Atos Declaratórios Interpretativos (ADI) (2000-2025):**
  - Mapeamento e coleta de 65 ADIs cobrindo todos os anos da série histórica (2000 a 2025), abrangendo FGTS, subvenções para investimento (Lei 14.789/23), CPRB, imunidades, isenções de IRPF, decadência do art. 195 CTN e bases de cálculo de PIS/COFINS.
- **Portarias Conjuntas RFB/PGFN (2000-2025):**
  - Coleta e estruturação de 35 Portarias Conjuntas prioritárias (Transação Tributária de créditos judicializados, Programa Litígio Zero, CND conjunta RFB/PGFN Portaria 1.751/14, Manual e leiaute do eSocial S-1.3, parcelamentos da Lei 11.941/09).
- **Armazenamento e Auditoria:**
  - Payloads brutos salvos e compactados em gzip em `_fonte/api/rfb/` e `_fonte/api/lexml/`.
  - 100% de conformidade de schema validada pelo `AgenteAuditor` (365 documentos aprovados, 0 rejeitados).
  - `ACERVO.md` atualizado para 365 normas e `PROGRESSO.md` expandido para 289 documentos mapeados no plano.

## 26/10/2026 00:48:00

Especialista tributos_servicos concluiu a auditoria, curadoria e enriquecimento técnico do Pilar de Serviços e Retenções:
- **ISSQN Federal & Obrigações Acessórias:**
  - `LC 157/2016`: Altera a LC 116/2003 para fixar a alíquota mínima de 2%, vedar guerra fiscal / isenções heterônomas, tributar serviços digitais de streaming (subitem 1.09) e fixar competência em cartões, leasing e planos de saúde.
  - `LC 175/2020`: Padrão nacional de obrigação acessória do ISSQN e instituição do Comitê Gestor das Obrigações Acessórias (CGOA).
- **Legislação Municipal das Capitais (CTM & RISS):**
  - `São Paulo (SP)`: Lei nº 13.701/2003 (Lei do ISS de São Paulo, regras de responsabilidade e retenção no tomador art. 9º, alíquotas de 2% a 5%) e Decreto nº 53.151/2012 (Regulamento do ISS - RISS/SP).
  - `Rio de Janeiro (RJ)`: Lei nº 691/1984 (Código Tributário Municipal do Rio de Janeiro, Livro Primeiro, Título III - ISSQN).
  - `Belo Horizonte (MG)`: Lei nº 8.725/2003 (ISSQN de Belo Horizonte e retenção na fonte arts. 20 a 23).
  - Criação da pasta canônica `municipais/` e link simbólico `municipal` -> `municipais`.
- **Retenções Federais na Fonte sobre Serviços:**
  - `Lei 7.450/1985`: Art. 52 (Fundamento primário do IRRF de 1,5% sobre serviços profissionais regulamentados prestados por PJ).
  - `IN SRF 459/2004`: Regulamentação primordial da CSRF de 4,65% (PIS, COFINS, CSLL) sobre pagamentos entre pessoas jurídicas de direito privado (art. 30 da Lei 10.833/2003).
  - `IN RFB 1.234/2012`: Retenção ampla de tributos federais e IRRF no fornecimento de bens e serviços por órgãos públicos.
  - `IN RFB 2.145/2023`: Extensão formal da retenção do IRRF aos pagamentos efetuados por Estados, DF e Municípios (Tema 1.130 STF).
  - `IN RFB 2.110/2022`: Consolidação previdenciária e disciplina minuciosa da retenção de 11% (e 3,5% CPRB) sobre cessão de mão de obra e empreitada (arts. 110 a 150).
  - `Solução de Consulta Cosit 282/2024`: IRRF Retenção ampla em pagamentos públicos (art. 714 RIR/2018).
  - `Solução de Consulta Cosit 154/2016`: IRRF sobre licenciamento de software, SaaS e remessas ao exterior.
- **Reforma Tributária (EC 132/2023) - Transição ISS para IBS/CBS:**
  - `federal/reforma-tributaria/servicos/ec-132-2023-transicao-iss-ibs.md`: Disciplina da substituição progressiva do ISS pelo IBS/CBS, Comitê Gestor do IBS (art. 156-B) e calendário de transição (ADCT arts. 125 a 133).
- **Saneamento e Auditoria:**
  - Reclassificação de 6 Soluções de Consulta anteriormente desindexadas para o tema "Serviços e Retenções".
  - Auditoria independente (`scripts/auditar.py`): 375 aprovados, 0 rejeitados (100% de integridade).
  - Links oficiais diretos verificados e ativos em normas.leg.br, prefeitura.sp.gov.br e normasinternet2.receita.fazenda.gov.br.

## 26/10/2026 00:50:00

Agente especialista `subagent_financeiro` concluiu a ingestão, estruturação e auditoria independente das normas de Tributação Financeira e IOF:
- **Regulamento do IOF (RIOF):**
  - `federal/regulamentos/iof/decreto-6306-2007.md`: Decreto nº 6.306/2007 (Regulamento do IOF - RIOF integral com todas as 4 modalidades: Crédito, Câmbio, Seguro e Títulos/Valores Mobiliários). URN LexML: `urn:lex:br:federal:decreto:2007-12-14;6306`.
- **Leis Ordinárias Estruturantes do IOF:**
  - `federal/leis-ordinarias/iof/lei-5143-1966.md`: Lei Federal nº 5.143/1966 (Criação e estruturação inicial do Imposto sobre Operações Financeiras). URN LexML: `urn:lex:br:federal:lei:1966-10-20;5143`.
  - `federal/leis-ordinarias/iof/lei-8894-1994.md`: Lei Federal nº 8.894/1994 (IOF sobre títulos, valores mobiliários e câmbio; fixação de alíquotas máximas e competência regulamentar do Executivo). URN LexML: `urn:lex:br:federal:lei:1994-06-21;8894`.
- **Criptoativos e Informações Fiscais:**
  - `reguladores/rfb/instrucoes-normativas/2019/ato-100592-1888-2019.md`: Instrução Normativa RFB nº 1.888/2019 (Prestação de informações de operações com criptoativos e exchanges). Fonte oficial: `https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/100592`.
- **Auditoria e Metadados:**
  - Frontmatter canônico rigoroso: `tema_tributario: "Tributação Financeira e IOF"` e `tributos_afetados: ["IOF", "IRRF Financeiro"]` (com `Criptoativos` na IN 1.888).
  - CommonMark estrito sem tags residuais HTML, validado com 100% de aprovação no `AgenteAuditor` (inclusive checagem de rede `--rede` HTTP 200).
  - Atualização do catálogo `ACERVO.md` e do plano `PROGRESSO.md` (100% de cobertura no RIOF e Leis do IOF).




## 26/10/2026 03:55:22

Ciclo periódico de 2h executado com sucesso em 20261026-0355. Novos documentos neste lote: 75. Total geral: 479. Aprovação auditoria: 100.0%.

## 26/10/2026 03:58:08

Lote 2/13 incorporado (6 atos normativos).

## 26/10/2026 03:58:22

Lote 3/13 incorporado (6 atos normativos).

## 26/10/2026 03:58:35

Lote 4/13 incorporado (6 atos normativos).

## 26/10/2026 03:58:48

Lote 5/13 incorporado (6 atos normativos).

## 26/10/2026 03:59:01

Lote 6/13 incorporado (6 atos normativos).

## 26/10/2026 03:59:14

Lote 7/13 incorporado (6 atos normativos).

## 26/10/2026 03:59:27

Lote 8/13 incorporado (6 atos normativos).

## 26/10/2026 03:59:40

Lote 9/13 incorporado (6 atos normativos).

## 26/10/2026 03:59:54

Lote 10/13 incorporado (6 atos normativos).

## 26/10/2026 04:00:08

Lote 11/13 incorporado (6 atos normativos).

## 26/10/2026 04:00:22

Lote 12/13 incorporado (6 atos normativos).

## 26/10/2026 04:00:36

Lote 13/13 incorporado (2 atos normativos).

## 26/10/2026 05:56:34

Ciclo periódico de 2h executado com sucesso em 20261026-0556. Novos documentos neste lote: 67. Total geral: 546. Aprovação auditoria: 100.0%.
