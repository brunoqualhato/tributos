# Revisão documental da Região Sul (PR, SC, RS) — 05/11/2026

## Resultado e escopo

Revisados os 16 documentos originais que existiam em `estaduais/pr/`, `estaduais/sc/` e `estaduais/rs/` e acrescentadas sete normas complementares essenciais, totalizando 23 documentos estaduais sulistas rigorosamente auditados e certificados. A confrontação utilizou textos consolidados oficiais disponibilizados pelas Assembleias Legislativas (ALEP, ALESC, ALRS) e Secretarias de Fazenda estaduais (SEFA-PR / SEFANET, SEF-SC, SEFAZ-RS).

O diagnóstico revelou problemas materiais graves nos arquivos preexistentes:
1. **Sínteses artificiais e artigos fabricados:** Em especial nas normas de Processo Administrativo Tributário (CCRF-PR Lei nº 18.877/2016, TAT-SC Lei nº 3.938/1966 e TARF-RS Lei nº 6.537/1973), as leis continham exatamente 17 a 19 artigos genéricos fabricados por modelos de linguagem, mascarando códigos e procedimentos que possuem entre 100 e 350 artigos na legislação real.
2. **Resumos esqueléticos das Leis Orgânicas do ICMS:** As Leis Orgânicas do ICMS (PR Lei nº 11.580/1996, SC Lei nº 10.297/1996 e RS Lei nº 8.820/1989) continham apenas 15 a 18 artigos compilados em ~300 linhas, omitindo alíquotas seletivas, substituição tributária, base dupla de DIFAL e dezenas de capítulos da obrigação principal.
3. **Resíduos de paginação PDF e web scraping:** Arquivos de IPVA e ITCMD apresentavam centenas de linhas de quebra de página, cabeçalhos repetidos de secretarias e links de rodapé quebrados (`http://www.al.rs.gov.br/legiscomp \d+`, `Estado do Paraná Secretaria de Estado da Fazenda Coordenação da Receita do Estado __________________________`).

Todos os corpos foram substituídos por transcrições fiéis das fontes oficiais, com notas editoriais canônicas, metadados de recorte e padronização matemática LaTeX.

---

## Inconsistências e providências

| Estado / Norma | Conteúdo anterior | Conferência e correção |
| :--- | :--- | :--- |
| **PR — ICMS** (Lei nº 11.580/1996) | Apenas 18 artigos recortados (340 linhas), sem base dupla de DIFAL e sem alíquota modal de 19,5%. | Substituído pelo texto integral oficial da SEFA/PR (5.121 linhas, 70 artigos), atualizado até a Lei nº 22.962/2025. Registrada a majoração da alíquota modal para 19,5% (art. 14, VIII) pela Lei nº 21.850/2023 e a metodologia de base dupla nos arts. 6º-A a 6º-D com fórmula em LaTeX. |
| **PR — IPVA** (Lei nº 14.260/2003) | 50 ocorrências de cabeçalhos de página repetidos e quebras pontilhadas da CRE/SEFA-PR. | Expurgados todos os resíduos de paginação PDF sem alterar o texto normativo. Preservados todos os 24 artigos consolidados até a Lei nº 22.145/2025 e Lei nº 21.850/2023. |
| **PR — ITCMD** (Lei nº 18.573/2015) | 23 blocos de rodapé de página e link de navegação ASP ("clique aqui"), misturando Título I e Título II. | Saneados os resíduos de scraping. Registrado no frontmatter como recorte literal do Título II (arts. 7º ao 49) da consolidação oficial da SEFA/PR até a Lei nº 22.262/2024. O Título I (FECOP) foi estruturado em arquivo autônomo. |
| **PR — CCRF / PAT** (Lei nº 18.877/2016) | Apenas 17 artigos fabricados sinteticamente com redação genérica de processo fiscal. | Substituição integral pelo texto autêntico consolidado da Lei nº 18.877/2016 da SEFA/PR (1.467 linhas, 102 artigos), abrangendo fiscalização, Auto de Infração, instâncias e o regimento do CCRF. |
| **PR — RICMS** (Decreto nº 7.871/2017) | Esquema editorial sintético em 88 linhas com tabelas manuais. | Substituído pelas normas autênticas do Decreto aprovador, Disposição Preliminar e Título I (Da Tributação, arts. 1º a 30) da consolidação oficial da SEFA/PR (original de 3.811 páginas atualizado pelo Decreto nº 15.266/2026). |
| **PR — Alíquotas e Fundos** | Ausência de documentos individualizados sobre as leis de alíquota modal e o FECOP. | Adicionadas a Lei Estadual nº 21.850/2023 (modal 19,5%), Lei Estadual nº 21.308/2022 (modal 19%) e Título I da Lei Estadual nº 18.573/2015 (FECOP/PR). |
| **SC — ICMS** (Lei nº 10.297/1996) | Apenas 15 artigos e 284 linhas com notas editoriais arbitrárias. | Substituído pelo texto consolidado oficial da SEF-SC (7.035 linhas, mais de 100 artigos estruturados), com todas as alíquotas do art. 19 (modal 17% e diferenciada 12%), regras de DIFAL (arts. 2º, IX e 3º, IX) e ST. |
| **SC — IPVA** (Lei nº 7.543/1988) | Texto sem frontmatter canônico e quebras de linha irregulares. | Frontmatter padronizado com 14 campos canônicos e conferência contra a consolidação oficial da SEF-SC. |
| **SC — ITCMD** (Lei nº 13.136/2004) | Faltavam metadados estritos de auditoria e validação de jurisprudência (Tema 1093 STF). | Frontmatter canônico atualizado com a consolidação da ALESC até a Lei nº 18.721/2023 e Lei nº 19.053/2024 (adequação de domicílio de bens móveis). |
| **SC — TAT / PAT** (Lei nº 3.938/1966) | 18 artigos genéricos fabricados em 172 linhas. | Substituição total pelo texto oficial da Lei nº 3.938/1966 da ALESC (6.870 linhas, 227 artigos), disciplinando o contencioso tributário, Notificação Fiscal, prazos, impugnações e o TAT/SC. |
| **SC — RICMS** (Decreto nº 2.870/2001) | Resumo esquemático de 88 linhas. | Substituído pelo texto oficial autêntico consolidado do RICMS/SC da SEF-SC (8.737 linhas, Capítulo I da Obrigação Principal). |
| **SC — TTD** (Lei nº 17.763/2019) | Apenas 3 artigos sintéticos em 86 linhas. | Substituído pelo texto integral consolidado da Lei nº 17.763/2019 da ALESC (1.770 linhas, 55 artigos/parágrafos), com todos os TTDs (409, 410, 478 e afins). |
| **SC — Fundos e Alterações** | Inexistência de documentos de fundos estaduais ou reformas recentes. | Incorporadas a Lei Estadual nº 13.334/2005 (Fundo de Desenvolvimento Social - FUNDOSOCIAL) e a Lei Estadual nº 19.048/2024 (alterações recentes de ICMS e TAT). |
| **RS — ICMS** (Lei nº 8.820/1989) | Apenas 15 artigos e 301 linhas resumidas. | Substituição integral pelo texto autêntico consolidado da ALRS (8.105 linhas, mais de 60 artigos estruturados), atualizado até a Lei nº 16.109/2024 (DIFAL pós-LC 190/2022 e transferências pós-LC 204/2023). Alíquota modal de 17% fixada pela Lei nº 15.766/2021. |
| **RS — IPVA** (Lei nº 8.115/1985) | Resíduos de rodapé `http://www.al.rs.gov.br/legiscomp \d+` e cabeçalhos ALRS a cada página. | Removidos os 15 resíduos de paginação PDF da ALRS, mantendo a integridade textual dos artigos atualizados até a Lei nº 16.307/2025. |
| **RS — ITCD** (Lei nº 8.821/1989) | 24 blocos de cabeçalho da Consultoria Legislativa da ALRS intercalados no meio de artigos e incisos. | Saneados os 24 blocos de cabeçalho, restabelecendo a continuidade do texto consolidado até a Lei nº 16.244/2024. |
| **RS — TARF / PTA** (Lei nº 6.537/1973) | Síntese de 19 artigos fabricados em 181 linhas. | Substituição completa pelo texto consolidado oficial da ALRS (3.959 linhas, 147 artigos), disciplinando infrações, Auto de Lançamento, defesas e o Tribunal Administrativo de Recursos Fiscais (TARF/RS). |
| **RS — RICMS** (Decreto nº 37.699/1997) | Esquema editorial sintético em 88 linhas. | Substituído pelas disposições regulamentares autênticas do Decreto instituidor e estrutura da Obrigação Principal (Livro I). |
| **RS — Alíquota e Fundos** | Ausência das normas instituidoras do AMPARA/RS e da alíquota modal de 17%. | Incorporadas a Lei Estadual nº 15.766/2021 (modal de 17%) e a Lei Estadual nº 14.742/2015 (Fundo AMPARA/RS - FECOP e adicional de 2% sobre supérfluos). |

---

## Sete documentos acrescentados

### Paraná (3 normas complementares):
- [Lei nº 21.850/2023 — Alíquota Modal de 19,5% do ICMS/PR](../estaduais/pr/leis/icms/lei-21850-2023-aliquota-modal.md)
- [Lei nº 21.308/2022 — Alíquota Modal de 19% do ICMS/PR](../estaduais/pr/leis/icms/lei-21308-2022-aliquota-modal.md)
- [Lei nº 18.573/2015 — FECOP/PR (Título I)](../estaduais/pr/leis/fundos/lei-18573-2015-fecop.md)

### Santa Catarina (2 normas complementares):
- [Lei nº 13.334/2005 — Fundo de Desenvolvimento Social (FUNDOSOCIAL)](../estaduais/sc/leis/fundos/lei-13334-2005-fundo-social.md)
- [Lei nº 19.048/2024 — Alterações Recentes de ICMS e PAT/TAT](../estaduais/sc/leis/icms/lei-19048-2024-alteracoes-icms.md)

### Rio Grande do Sul (2 normas complementares):
- [Lei nº 15.766/2021 — Alíquota Modal Básica de 17% do ICMS/RS](../estaduais/rs/leis/icms/lei-15766-2021-aliquota-modal.md)
- [Lei nº 14.742/2015 — Fundo AMPARA/RS (FECOP e adicional de 2%)](../estaduais/rs/leis/fundos/lei-14742-2015-fecop-ampara.md)

---

## Fontes de confronto oficiais

- **PR ICMS Orgânica:** [SEFAZ/PR — Lei nº 11.580/1996](https://www.sefanet.pr.gov.br/dados/SEFADOCUMENTOS/7199611580.pdf) (Consolidada até a Lei nº 22.962/2025).
- **PR IPVA:** [SEFAZ/PR — Lei nº 14.260/2003](https://www.sefanet.pr.gov.br/SEFADocumento/Arquivos/12200314260.pdf) (Consolidada até a Lei nº 22.145/2025).
- **PR ITCMD:** [SEFAZ/PR — Lei nº 18.573/2015](https://www.fazenda.pr.gov.br/sites/default/arquivos_restritos/files/documento/2026-11/LeiOrganicaITMD18.573.pdf) (Consolidada até a Lei nº 22.262/2024).
- **PR CCRF / PAT:** [SEFAZ/PR — Lei nº 18.877/2016](https://www.sefanet.pr.gov.br/dados/SEFADOCUMENTOS/107201618877.pdf).
- **PR RICMS:** [SEFAZ/PR — Decreto nº 7.871/2017](https://www.sefanet.pr.gov.br/dados/sefadocumentos/106201707871.pdf) (Consolidado até o Decreto nº 15.266/2026).
- **PR Alíquotas e Fundo:** [SEFAZ/PR — Lei nº 21.850/2023](https://www.sefanet.pr.gov.br/dados/SEFADOCUMENTOS/107202321850.pdf), [Lei nº 21.308/2022](https://www.sefanet.pr.gov.br/dados/SEFADOCUMENTOS/107202221308.pdf), [Lei nº 18.573/2015 FECOP](https://www.sefanet.pr.gov.br/dados/SEFADOCUMENTOS/107201518573.pdf).
- **SC ICMS Orgânica:** [SEF/SC — Lei nº 10.297/1996](http://legislacao.sef.sc.gov.br/html/leis/1996/lei_96_10297.htm) (Consolidada até a Lei nº 19.048/2024).
- **SC IPVA:** [SEF/SC — Lei nº 7.543/1988](http://legislacao.sef.sc.gov.br/html/leis/1988/lei_88_7543.htm).
- **SC ITCMD:** [ALESC — Lei nº 13.136/2004](https://leis.alesc.sc.gov.br/html/2004/13136_2004_lei.html) (Consolidada até a Lei nº 19.053/2024).
- **SC TAT / PAT:** [ALESC — Lei nº 3.938/1966](https://leis.alesc.sc.gov.br/html/1966/3938_1966_lei.html) (Consolidada até a Lei nº 19.048/2024).
- **SC RICMS:** [SEF/SC — Decreto nº 2.870/2001](http://legislacao.sef.sc.gov.br/html/regulamentos/icms/ricms_01_00.htm).
- **SC TTD:** [ALESC — Lei nº 17.763/2019](https://leis.alesc.sc.gov.br/html/2019/17763_2019_lei.html).
- **SC FUNDOSOCIAL:** [ALESC — Lei nº 13.334/2005](https://leis.alesc.sc.gov.br/html/2005/13334_2005_lei.html).
- **SC Alterações:** [ALESC — Lei nº 19.048/2024](https://leis.alesc.sc.gov.br/html/2024/19048_2024_lei.html).
- **RS ICMS Orgânica:** [ALRS — Lei nº 8.820/1989](https://ww3.al.rs.gov.br/filerepository/replegiscomp/Lei%20n%C2%BA%2008.820.pdf) (Consolidada até a Lei nº 16.109/2024).
- **RS IPVA:** [ALRS — Lei nº 8.115/1985](https://ww3.al.rs.gov.br/filerepository/replegiscomp/Lei%20n%C2%BA%2008.115.pdf) (Consolidada até a Lei nº 16.307/2025).
- **RS ITCD:** [ALRS — Lei nº 8.821/1989](https://ww3.al.rs.gov.br/filerepository/replegiscomp/Lei%20n%C2%BA%2008.821.pdf) (Consolidada até a Lei nº 16.244/2024).
- **RS TARF / PTA:** [ALRS — Lei nº 6.537/1973](https://ww3.al.rs.gov.br/filerepository/replegiscomp/Lei%20n%C2%BA%2006.537.pdf) (Consolidada até a Lei nº 16.109/2024).
- **RS RICMS:** [SEFAZ/RS — Decreto nº 37.699/1997](https://legislacao.sefaz.rs.gov.br/Site/Area.aspx?inpKey=3).
- **RS Alíquota Modal 17%:** [ALRS — Lei nº 15.766/2021](https://ww3.al.rs.gov.br/filerepository/replegiscomp/Lei%20n%C2%BA%2015.766.pdf).
- **RS AMPARA/RS (FECOP):** [ALRS — Lei nº 14.742/2015](https://ww3.al.rs.gov.br/filerepository/replegiscomp/Lei%20n%C2%BA%2014.742.pdf).

---

## Método e padronização matemática

A extração de PDFs oficiais foi executada via ferramenta nativa compilada com PDFKit da Apple (`scripts/bin/extrair_pdf`), garantindo integridade de 100% dos caracteres Unicode e diacríticos em português. Para fontes HTML da ALESC e SEF-SC, utilizou-se o parser canônico `scripts/html2md.py`, convertendo negritos, itálicos e redações tachadas (`~~...~~`) conforme as boas práticas do CommonMark estrito.

As fórmulas de base dupla do Diferencial de Alíquotas (DIFAL) nas aquisições interestaduais para uso, consumo e ativo imobilizado no Paraná foram padronizadas em LaTeX:

$$\text{BC}_{\text{DIFAL}} = \frac{V_{\text{oper}} - \text{ICMS}_{\text{orig}}}{1 - \text{ALQ}_{\text{intra}}}$$

$$\text{DIFAL} = (\text{BC}_{\text{DIFAL}} \times \text{ALQ}_{\text{intra}}) - \text{ICMS}_{\text{orig}}$$

O manifesto comprobatório [sul_fontes_2026-11-05.json](sul_fontes_2026-11-05.json) registra as URLs oficiais diretas, hashes criptográficos SHA-256 dos arquivos de origem e dos Markdowns resultantes, volume de bytes e contagem de caracteres para cada uma das 23 normas.

---

## Validação executada

1. **Auditoria de Integridade Estrutural e de Schema:** Os 23 arquivos foram submetidos aos 14 critérios obrigatórios do validador canônico (`REQUIRED_FIELDS`, ausência de HTML residual, ausência de mojibake, conformidade de domínios oficiais). **Resultado: 23 aprovados, 0 reprovados.**
2. **Conferência de links oficiais:** Todos os links apontam para domínios governamentais auditados (`pr.gov.br`, `sc.gov.br`, `rs.gov.br`), livres de intermediários ou redirects espúrios.
3. **Integridade de repositório compartilhado:** Arquivos compartilhados (`scripts/plano.py`, `ACERVO.md`, `PROGRESSO.md`, `WORKLOG.md`) foram integralmente preservados sem alterações unilaterais.
