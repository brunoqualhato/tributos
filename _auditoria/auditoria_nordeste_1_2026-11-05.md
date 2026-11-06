# Revisão documental da Região Nordeste 1 (BA, PE, CE, MA) — 05/11/2026

## Resultado e escopo

Revisados todos os 22 documentos preexistentes e acrescentadas 7 normas complementares fundamentais nas unidades federativas da Região Nordeste 1 (**Bahia, Pernambuco, Ceará e Maranhão**), totalizando **29 documentos estaduais** rigorosamente auditados, saneados e certificados. O processo de auditoria baseou-se na confrontação integral com os acervos oficiais das Assembleias Legislativas (ALBA, ALEPE, ALECE, ALEMA) e Secretarias de Estado da Fazenda (SEFAZ-BA, SEFAZ-PE, SEFAZ-CE, SEFAZ-MA), complementados por registros do Diário Oficial e jurisprudência dos Tribunais Superiores (STF/STJ).

O diagnóstico material identificou e corrigiu três classes críticas de distorções:
1. **Artigos sintéticos e interpolações apócrifas/fabricadas:** Identificados textos artificiais gerados por modelos preditivos que misturavam projetos de lei federais, Emendas Constitucionais e julgamentos do STF diretamente na redação dos artigos estaduais. Exemplos graves incluíam: artigos fictícios sobre o "Complexo Automotivo BYD em Camaçari" e "compensação de saldos em 240 parcelas mensais com o IBS" inseridos no corpo da Lei do ICMS da Bahia (Lei nº 7.014/1996); regra falsa de desempate automático pró-contribuinte no CONSEF/BA (Decreto nº 7.629/1999) atribuída indevidamente à Lei Federal nº 13.988/2020 e ADI 6784; e arquivos de 83 linhas sintéticas idênticas para ITCMD e IPVA no Ceará e Maranhão.
2. **Invenção de normas inexistentes:** Foi identificado no arquivo `lei-14527-2022-fain-fefir.md` um fundo agropecuário fabricado denominado "FEFIR/FAIN" com tributação de grãos e "Anel da Soja", inexistente no ordenamento baiano. O documento foi integralmente substituído pelo texto oficial e autêntico da Lei Estadual nº 14.527/2022 (dispensa de créditos tributários com recolhimento ao FUNCEP, alíquota de 19% e tributação monofásica de combustíveis).
3. **Ausência de alíquotas modais e códigos unificados:** No Maranhão, o Código Tributário Estadual (Lei nº 7.799/2002) é um corpo único codificado; foram delimitados os recortes estritos para ICMS (Livro I), IPVA (Título II) e ITCD (Título III). Foram pesquisadas e incorporadas as leis que fixaram as alíquotas modais atuais pós-reforma: BA (20,5%), PE (20,5%), CE (20%) e MA (22%).

Todos os 29 corpos documentais foram saneados ou substituídos por transcrições fiéis das fontes oficiais, com frontmatter canônico estruturado, notas editoriais padronizadas e conversão de fórmulas matemáticas para notação LaTeX (`$$...$$`).

---

## Inconsistências e providências

| Estado / Norma | Conteúdo anterior | Conferência e correção |
| :--- | :--- | :--- |
| **BA — ICMS Orgânica** (Lei nº 7.014/1996) | Continha Seção apócrifa do "Polo Automotivo de Camaçari e Complexo BYD" (art. 40) e art. 101 determinando transição de saldos de ICMS para IBS em 240 parcelas via LC 214/2025. | Expurgadas todas as interpolações fabricadas. Incorporado o texto autêntico consolidado oficial da SEFAZ-BA/ALBA com 54 artigos e Anexos I e II completos (195 KB, 2.314 linhas), atualizado pelas Leis nº 14.415/2021, 14.527/2022 e 14.629/2023. |
| **BA — Fundo Agro Fictício** (Lei nº 14.527/2022) | Arquivo descrevia um fictício "Fundo Estadual de Infraestrutura Rural (FEFIR/FAIN)" com cobrança de soja e milho. | Substituição total pelo texto oficial da Lei nº 14.527/2022 da ALBA/DOE: dispensa de créditos por descumprimento do art. 1º da Lei 13.564/2016 com repasse de 10% ao FUNCEP, alíquota de 19% e regime monofásico da LC 192/2022. |
| **BA — Alíquota Modal 20,5%** (Lei nº 14.629/2023) | Norma ausente no acervo baiano. | Incorporada a Lei nº 14.629/2023, que alterou o art. 15, I, da Lei 7.014/1996, fixando a alíquota modal baiana em 20,5% a partir de fevereiro de 2024. |
| **BA — CONSEF / RPAF** (Decreto nº 7.629/1999) | Apenas 15 artigos resumidos, com art. 14 instituindo empate favorável ao contribuinte pela Lei 13.988/ADI 6784. | Substituição integral pelo texto autêntico consolidado do RPAF da Bahia da SEFAZ-BA (171 KB, 2.203 linhas, 180 artigos), restabelecendo as competências originárias, Juntas de Julgamento Fiscal e Câmaras do CONSEF até o Decreto nº 23.977/2025. |
| **BA — Atacadista / DESENVOLVE** (Decreto nº 7.799/2000) | Mistura de fragmentos do Decreto 7.799/2000 com artigos da Lei 7.980/2001 (DESENVOLVE). | Substituição integral pelo texto oficial consolidado do Decreto nº 7.799/2000 da SEFAZ-BA (38 KB, 414 linhas), incluindo o Anexo Único completo de CNAEs atacadistas beneficiadas e sistemática de estorno de créditos. |
| **BA — IPVA e ITD** (Leis nº 6.348/1991 e 4.826/1989) | Resíduos de paginação PDF (`legest_1991_6348_lei_ipva` e `legest_1989_4826_lei_itd`) e ausência de notas canônicas. | Expurgados os resíduos de paginação da SEFAZ-BA, preservando o histórico integral de redações e notas de ADIs julgadas pelo STF; frontmatter canônico e nota editorial inseridos. |
| **PE — ICMS Orgânica** (Lei nº 15.730/2016) | Apenas 213 linhas em resumo sintético de 18 artigos. | Substituição completa pelo texto integral autêntico da ALEPE (290 KB, 6.496 linhas), contemplando a totalidade dos livros, alíquotas seletivas, base dupla de DIFAL, antecipação e substituição tributária. |
| **PE — Alíquota Modal 20,5%** (Lei nº 18.305/2023) | Norma ausente no acervo pernambucano. | Adicionada a Lei nº 18.305/2023 transcrita da ALEPE (102 KB, 2.583 linhas), que fixou a alíquota modal de 20,5% em Pernambuco e reestruturou benefícios fiscais. |
| **PE — PRODEPE** (Lei nº 11.675/1999) | Resumo esquemático em 80 linhas. | Substituição pelo texto integral oficial consolidado da ALEPE (130 KB, 2.545 linhas), com todos os incentivos à indústria, comércio atacadista e centrais de distribuição. |
| **PE — TATE / PAT** (Lei nº 10.654/1991) | Norma ausente no acervo. | Incorporada a Lei nº 10.654/1991 autêntica da ALEPE (299 KB, 6.789 linhas), que disciplina todo o processo administrativo-tributário e funcionamento do Tribunal Administrativo Tributário do Estado de Pernambuco (TATE/PE). |
| **PE — IPVA e ITCMD** (Leis nº 10.849/1992 e 13.974/2009) | Textos autênticos preexistentes sem metadados estritos e nota editorial canônica. | Preservadas as transcrições integrais da ALEPE (127 KB e 78 KB) e atualizados os campos de frontmatter e notas editoriais. |
| **CE — ICMS Orgânica** (Lei nº 18.665/2023) | Texto com artigos fabricados misturando transição para o IBS e menções à montadora BYD. | Substituição integral pelo texto autêntico consolidado da ALECE (305 KB, 7.672 linhas), regulando inteiramente o ICMS cearense (Lei nº 18.665/2023). |
| **CE — Alíquota Modal 20%** (Lei nº 18.305/2023) | Norma ausente no acervo cearense. | Adicionada a Lei nº 18.305/2023 da ALECE, fixando a alíquota modal cearense em 20% a contar de 01/01/2024. |
| **CE — IPVA e ITCD** (Leis nº 12.023/1992 e 15.812/2015) | Arquivos sintéticos genéricos de apenas 83 linhas com artigos inventados. | Substituição integral pelos textos oficiais da ALECE: Lei nº 12.023/1992 (13 KB) e Lei nº 15.812/2015 (32 KB, tabela progressiva de 2% a 8%). |
| **CE — CONAT / PAT** (Lei nº 15.614/2014) | Norma ausente no acervo cearense. | Incorporada a Lei nº 15.614/2014 da ALECE (109 KB, 2.680 linhas), com registro editorial de sua sucessão pela Lei nº 18.185/2022 no Conselho de Recursos Tributários do Ceará (CONAT). |
| **CE — FDI / Carga Líquida** (Lei nº 14.237/2008) | Apenas 84 linhas em resumo esquemático. | Substituído pelo texto autêntico da ALECE (38 KB, 975 linhas), disciplinando o Fundo de Desenvolvimento Industrial (FDI) e a sistemática de Carga Líquida para comércio atacadista e varejista. |
| **MA — ICMS, IPVA e ITCD** (Lei nº 7.799/2002) | Arquivos curtos artificiais de 83 a 210 linhas desvinculados do Código Tributário Estadual real. | O CTE do Maranhão é uma codificação una. Foram extraídos recortes literais oficiais do PDF da ALEMA: Livro I (ICMS, arts. 1º a 84, 90 KB), Título II (IPVA, arts. 85 a 104, 14 KB) e Título III (ITCD, arts. 105 a 120, 7,5 KB), todos com metadados de recorte explícitos. |
| **MA — Alíquota Modal 22%** (Lei nº 12.120/2023) | Norma ausente no acervo maranhense. | Incorporada a Lei nº 12.120/2023 autêntica da ALEMA (29 KB, 543 linhas), fixando a alíquota modal maranhense em 22% a partir de 2024. |
| **MA — TATE / PAT** (Lei nº 9.127/2010) | Norma ausente no acervo maranhense. | Adicionada a Lei nº 9.127/2010 da ALEMA (70 KB, 2.473 linhas), disciplinando o contencioso fiscal e o Tribunal Administrativo de Recursos Fiscais (TATE/MA). |
| **MA — FECOP** (Lei nº 8.205/2004) | Texto incompleto sem notas canônicas. | Substituição pelo texto autêntico da ALEMA (9,5 KB, 172 linhas), consolidando a alíquota adicional de 2% do Fundo de Combate à Pobreza. |
| **Regulamentos de ICMS (BA, PE, CE, MA)** | Ausência de notação científica nas fórmulas de DIFAL e MVA. | Decretos nº 13.780/2012 (BA), 44.650/2017 (PE), 33.327/2019 (CE) e 19.714/2003 (MA) padronizados com fórmulas matemáticas em LaTeX (`$$...$$`). |

---

## Documentos auditados e estruturados por estado

### Bahia (8 documentos):
- [Lei nº 7.014/1996 — Lei Geral do ICMS](../estaduais/ba/leis/icms/lei-7014-1996.md) (Consolidada SEFAZ-BA/ALBA)
- [Lei nº 14.629/2023 — Alíquota Modal de 20,5% do ICMS](../estaduais/ba/leis/icms/lei-14629-2023-aliquota-modal.md)
- [Lei nº 6.348/1991 — Lei do IPVA](../estaduais/ba/leis/ipva/lei-6348-1991.md) (Consolidada SEFAZ-BA)
- [Lei nº 4.826/1989 — Lei do ITD](../estaduais/ba/leis/itcmd/lei-4826-1989.md) (Consolidada SEFAZ-BA)
- [Lei nº 14.527/2022 — FUNCEP, Créditos e ICMS](../estaduais/ba/leis/fundos/lei-14527-2022-fain-fefir.md)
- [Decreto nº 7.629/1999 — RPAF e CONSEF/BA](../estaduais/ba/leis/pat/decreto-7629-1999-consef-ba.md) (Consolidado SEFAZ-BA)
- [Decreto nº 7.799/2000 — Regime Especial de Atacadista](../estaduais/ba/ricms/decreto-7799-2000-atacadista-desenvolve-ba.md) (Consolidado SEFAZ-BA)
- [Decreto nº 13.780/2012 — Regulamento do ICMS (RICMS/BA)](../estaduais/ba/ricms/decreto-13780-2012.md)

### Pernambuco (7 documentos):
- [Lei nº 15.730/2016 — Lei Geral do ICMS](../estaduais/pe/leis/icms/lei-15730-2016.md) (Consolidada ALEPE)
- [Lei nº 18.305/2023 — Alíquota Modal de 20,5% do ICMS](../estaduais/pe/leis/icms/lei-18305-2023-aliquota-modal.md) (ALEPE)
- [Lei nº 10.849/1992 — Lei do IPVA](../estaduais/pe/leis/ipva/lei-10849-1992.md) (Consolidada ALEPE)
- [Lei nº 13.974/2009 — Lei do ICD](../estaduais/pe/leis/itcmd/lei-13974-2009.md) (Consolidada ALEPE)
- [Lei nº 10.654/1991 — Processo Fiscal e TATE/PE](../estaduais/pe/leis/pat/lei-10654-1991-tate-pat.md) (Consolidada ALEPE)
- [Lei nº 11.675/1999 — PRODEPE](../estaduais/pe/ricms/lei-11675-1999-prodepe-pe.md) (Consolidada ALEPE)
- [Decreto nº 44.650/2017 — Regulamento do ICMS (RICMS/PE)](../estaduais/pe/ricms/decreto-44650-2017.md)

### Ceará (7 documentos):
- [Lei nº 18.665/2023 — Lei Geral do ICMS](../estaduais/ce/leis/icms/lei-18665-2023.md) (Consolidada ALECE)
- [Lei nº 18.305/2023 — Alíquota Modal de 20% do ICMS](../estaduais/ce/leis/icms/lei-18305-2023-aliquota-modal.md) (ALECE)
- [Lei nº 12.023/1992 — Lei do IPVA](../estaduais/ce/leis/ipva/lei-12023-1992.md) (Consolidada ALECE)
- [Lei nº 15.812/2015 — Lei do ITCD](../estaduais/ce/leis/itcmd/lei-15812-2015.md) (Consolidada ALECE)
- [Lei nº 15.614/2014 — PAT e CONAT/CE](../estaduais/ce/leis/pat/lei-15614-2014-conat-pat.md) (Consolidada ALECE)
- [Lei nº 14.237/2008 — Carga Líquida e FDI](../estaduais/ce/ricms/lei-14237-2008-carga-liquida-fdi-ce.md) (Consolidada ALECE)
- [Decreto nº 33.327/2019 — Regulamento do ICMS (RICMS/CE)](../estaduais/ce/ricms/decreto-33327-2019.md)

### Maranhão (7 documentos):
- [Lei nº 7.799/2002 — ICMS (Livro I do CTE-MA)](../estaduais/ma/leis/icms/lei-7799-2002.md) (ALEMA)
- [Lei nº 12.120/2023 — Alíquota Modal de 22% do ICMS](../estaduais/ma/leis/icms/lei-12120-2023-aliquota-modal.md) (ALEMA)
- [Lei nº 7.799/2002 — IPVA (Título II do CTE-MA)](../estaduais/ma/leis/ipva/lei-7799-2002.md) (ALEMA)
- [Lei nº 7.799/2002 — ITCD (Título III do CTE-MA)](../estaduais/ma/leis/itcmd/lei-7799-2002.md) (ALEMA)
- [Lei nº 9.127/2010 — PAT e TATE/MA](../estaduais/ma/leis/pat/lei-9127-2010-tate-pat.md) (ALEMA)
- [Lei nº 8.205/2004 — FECOP/MA](../estaduais/ma/leis/fundos/lei-8205-2004-fecop.md) (ALEMA)
- [Decreto nº 19.714/2003 — Regulamento do ICMS (RICMS/MA)](../estaduais/ma/ricms/decreto-19714-2003.md)

---

## Fontes de confronto oficiais

- **Bahia:**
  - [SEFAZ-BA — Lei Geral do ICMS nº 7.014/1996](http://mbusca.sefaz.ba.gov.br/DITRI/leis/leis_estaduais/legest_1996_7014.pdf)
  - [ALBA — Lei Estadual nº 14.629/2023 (Alíquota Modal 20,5%)](https://www.al.ba.gov.br/atividade-legislativa-nova/proposicao/PL.-25091-2023)
  - [SEFAZ-BA — Lei do IPVA nº 6.348/1991](http://mbusca.sefaz.ba.gov.br/DITRI/leis/leis_estaduais/legest_1991_6348_lei_ipva.pdf)
  - [SEFAZ-BA — Lei do ITD nº 4.826/1989](http://mbusca.sefaz.ba.gov.br/DITRI/leis/leis_estaduais/legest_1989_4826_lei_itd.pdf)
  - [ALBA — Lei Estadual nº 14.527/2022](https://www.al.ba.gov.br/atividade-legislativa-nova/proposicao/PL.-24676-2022)
  - [SEFAZ-BA — RPAF / CONSEF Decreto Estadual nº 7.629/1999](http://mbusca.sefaz.ba.gov.br/DITRI/decretos/decretos_estaduais/decest_1999_7629_rpaf.pdf)
  - [SEFAZ-BA — Regime Atacadista Decreto Estadual nº 7.799/2000](http://mbusca.sefaz.ba.gov.br/DITRI/decretos/decretos_estaduais/decest_2000_7799.pdf)
  - [SEFAZ-BA — RICMS Decreto Estadual nº 13.780/2012](http://mbusca.sefaz.ba.gov.br/DITRI/decretos/decretos_estaduais/decest_2012_13780_ricms.pdf)
- **Pernambuco:**
  - [ALEPE — Lei Geral do ICMS nº 15.730/2016](https://legis.alepe.pe.gov.br/texto.aspx?tiponorma=1&numero=15730&complemento=0&ano=2016&tipo=&url=)
  - [ALEPE — Lei nº 18.305/2023 (Alíquota Modal 20,5%)](https://legis.alepe.pe.gov.br/texto.aspx?tiponorma=1&numero=18305&complemento=0&ano=2023&tipo=&url=)
  - [ALEPE — Lei do IPVA nº 10.849/1992](https://legis.alepe.pe.gov.br/texto.aspx?tiponorma=1&numero=10849&complemento=0&ano=1992&tipo=&url=)
  - [ALEPE — Lei do ICD nº 13.974/2009](https://legis.alepe.pe.gov.br/texto.aspx?tiponorma=1&numero=13974&complemento=0&ano=2009&tipo=&url=)
  - [ALEPE — PAT e TATE/PE Lei nº 10.654/1991](https://legis.alepe.pe.gov.br/texto.aspx?tiponorma=1&numero=10654&complemento=0&ano=1991&tipo=&url=)
  - [ALEPE — PRODEPE Lei nº 11.675/1999](https://legis.alepe.pe.gov.br/texto.aspx?tiponorma=1&numero=11675&complemento=0&ano=1999&tipo=&url=)
  - [SEFAZ-PE — RICMS Decreto nº 44.650/2017](https://www.sefaz.pe.gov.br)
- **Ceará:**
  - [ALECE — Lei Geral do ICMS nº 18.665/2023](https://www2.al.ce.gov.br/legislativo/legislacao5/leis2023/18665.htm)
  - [ALECE — Lei nº 18.305/2023 (Alíquota Modal 20%)](https://www2.al.ce.gov.br/legislativo/legislacao5/leis2023/18305.htm)
  - [ALECE — Lei do IPVA nº 12.023/1992](https://www2.al.ce.gov.br/legislativo/tramitando/lei/12023.htm)
  - [ALECE — Lei do ITCD nº 15.812/2015](https://www2.al.ce.gov.br/legislativo/legislacao5/leis2015/15812.htm)
  - [ALECE — PAT e CONAT/CE Lei nº 15.614/2014](https://www2.al.ce.gov.br/legislativo/legislacao5/leis2014/15614.htm)
  - [ALECE — Carga Líquida e FDI Lei nº 14.237/2008](https://www2.al.ce.gov.br/legislativo/legislacao5/leis2008/14237.htm)
  - [SEFAZ-CE — RICMS Decreto nº 33.327/2019](https://www.sefaz.ce.gov.br)
- **Maranhão:**
  - [ALEMA — Código Tributário Estadual (Lei nº 7.799/2002)](https://arquivos.al.ma.leg.br:8443/ged/legislacao/LEI_7799)
  - [ALEMA — Lei nº 12.120/2023 (Alíquota Modal 22%)](https://arquivos.al.ma.leg.br:8443/ged/legislacao/LEI_12120)
  - [ALEMA — FECOP/MA Lei nº 8.205/2004](https://arquivos.al.ma.leg.br:8443/ged/legislacao/LEI_8205)
  - [ALEMA — PAT e TATE/MA Lei nº 9.127/2010](https://arquivos.al.ma.leg.br:8443/ged/legislacao/LEI_9127)
  - [SEFAZ-MA — RICMS Decreto nº 19.714/2003](https://sistemas1.sefaz.ma.gov.br/portalsefaz/jsp/legislacao/)

---

## Método e limites

1. **Expurgo de interpolações:** Todas as reconstruções artificiais que mesclavam projetos de lei federais (ex.: PLP 108/2024), súmulas vinculantes, decisões de ADIs e supostos tratamentos especiais corporativos foram expurgadas do texto normativo positivo, sendo alocadas exclusivamente nas notas editoriais quando estritamente pertinentes ao contexto hermenêutico.
2. **Preservação textual literal:** Nas normas transcritas das Assembleias Legislativas e Secretarias de Fazenda, mantiveram-se as redações originais e históricas com notas da própria fonte oficial.
3. **Conversão e notação LaTeX:** Todas as fórmulas e cálculos de DIFAL e MVA Ajustada foram convertidos para notação padronizada LaTeX (`$$...$$`), sem resíduos de HTML proprietário ou imagens rasterizadas.
4. **Manifesto de auditoria:** O manifesto [_auditoria/nordeste_1_fontes_2026-11-05.json](nordeste_1_fontes_2026-11-05.json) reúne a totalidade dos 29 arquivos, hashes SHA-256 de integridade e metadados de fidelidade textual normalizada.

---

## Validação executada

- **Auditoria de integridade total (`scripts/auditar.py`):** 1.291 documentos aprovados, zero rejeitados em todo o acervo nacional.
- **Conformidade de Frontmatter:** 100% dos 29 documentos contêm os campos canônicos obrigatórios, incluindo `esfera: "Estadual"`, `situacao`, `revogada: false`, `data_consulta: "2026-11-05"`, `natureza_conteudo` e link oficial direto.
- **Conformidade Estrutural:** Todos os 29 documentos iniciam com cabeçalho `# ` (H1) seguido imediatamente de `## Nota editorial de conferência — 05/11/2026`.
- **Rastreabilidade de fontes:** Todos os links externos apontam diretamente para repositórios oficiais governamentais (ALBA, ALEPE, ALECE, ALEMA, SEFAZ-BA, SEFAZ-PE, SEFAZ-CE, SEFAZ-MA).
