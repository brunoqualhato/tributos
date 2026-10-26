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
