# Revisão documental da Região Sudeste (SP, MG, RJ, ES) — 05/11/2026

## Resultado e escopo

Foram revisados os 21 documentos preexistentes em `estaduais/sp/`, `estaduais/mg/`, `estaduais/rj/` e `estaduais/es/`, e acrescentadas 11 normas complementares estratégicas (leis de alíquota modal do ICMS, leis de processo administrativo tributário e leis instituidoras de fundos estaduais de equilíbrio fiscal e combate à pobreza), perfazendo um total consolidado de **32 documentos estaduais**.

A auditoria material identificou que os arquivos anteriores eram constituídos por resumos sintéticos e articulações fictícias/editoriais (geradas por scripts de templateização), as quais inseriam jurisprudência do STF (Temas 708, 863, 1214), emendas constitucionais (EC 132/2023) e referências a projetos de lei complementar (PLP 108/2024) diretamente dentro do texto legal dos artigos como se fizessem parte da redação sancionada pelos governadores. Todos os corpos foram saneados e substituídos por transcrições autênticas e fiéis extraídas diretamente dos portais oficiais das Assembleias Legislativas (ALSP, ALMG, ALERJ, ALES) e Secretarias de Estado de Fazenda (SEFAZ-SP, SEF-MG, SEFAZ-RJ, SEFAZ-ES).

Distribuição dos 32 documentos:
- **São Paulo (`estaduais/sp/`)**: 7 documentos (5 saneados + 2 adicionados)
- **Minas Gerais (`estaduais/mg/`)**: 8 documentos (6 saneados + 2 adicionados)
- **Rio de Janeiro (`estaduais/rj/`)**: 9 documentos (5 saneados + 4 adicionados)
- **Espírito Santo (`estaduais/es/`)**: 8 documentos (5 saneados + 3 adicionados)

---

## Inconsistências materiais identificadas e providências

| UF / Tributo | Conteúdo anterior (sintético/editorial) | Conferência e correção oficial |
| :--- | :--- | :--- |
| **SP — IPVA**<br>(Lei 13.296/2008) | Artigos renumerados e modificados; inserção editorial do Tema 708 do STF e da Súmula 585 do STJ no texto legal; menção fictícia ao § 6º da CF/88 no art. 1º. | Substituído pelo texto integral oficial do Repositório da ALSP (125 KB HTML). Restabelecida a redação autêntica dos arts. 1º ao 67, com histórico de alterações por leis subsequentes e ADIs. |
| **SP — ITCMD**<br>(Lei 10.705/2000) | Artigos fabricados misturando Tema 1214 do STF (VGBL/PGBL), EC 132/2023 e suposta LC 227/2026 nos arts. 2º e 3º. | Transcrição autêntica da Lei nº 10.705/2000 da ALSP (49 KB HTML), preservando alíquota de 4%, hipóteses legais estritas de isenção em UFESP e sistemática de partilha. |
| **SP — ICMS**<br>(Lei 6.374/1989) | Resumo sintético em 300 linhas com capítulos reconstruídos ("Crédito CIAP 1/48", "e-CredAc", "Tema 863 do STF"). | Incorporação do texto oficial consolidado da ALSP (874 KB HTML, mais de 500.000 caracteres de texto legal autêntico), contendo todos os artigos, livros, tabelas e notas de vigência. |
| **SP — PAT / TIT**<br>(Lei 13.457/2009) | Texto bruto fragmentado com resíduos de tags e quebras desconexas. | Higienização da estrutura do contencioso administrativo do Tribunal de Impostos e Taxas (TIT/SP), mantendo os 115 artigos integrais e redações históricas da Lei nº 16.498/2017. |
| **SP — RICMS**<br>(Dec. 45.490/2000) | Quadro sinóptico de 88 linhas elaborado por template genérico. | Substituído pela íntegra oficial do Decreto nº 45.490/2000 (3,3 MB HTML) aprovando o regulamento e suas disposições introdutórias e anexos essenciais. |
| **MG — IPVA**<br>(Lei 14.937/2003) | Artigo 2º-A inventado com tese do Tema 708 do STF; alíquotas com notas editoriais embutidas nos incisos. | Transcrição fiel via endpoint de compilação oficial da ALMG (`print.html`), restabelecendo os arts. 1º a 22, notas de vigência e remissões a decretos regulamentares. |
| **MG — ITCD**<br>(Lei 14.941/2003) | Texto sintético atribuindo alíquota de 5% progressiva ao texto de 2003 com base na EC 132/2023; inclusão de precedentes jurisprudenciais nos artigos. | Transcrição integral da compilação da ALMG (arts. 1º a 29), com preservação da alíquota autêntica de 5%, regras de avaliação contraditória e responsabilidade solidária. |
| **MG — ICMS**<br>(Lei 6.763/1975) | Recorte parcial e sintetizado com foco restrito no art. 1º e 2º. | Incorporada a consolidação integral oficial da Lei nº 6.763/1975 da ALMG (998 KB HTML, quase 740.000 caracteres), cobrindo ICMS, taxas estaduais, TFRM, FEM e infrações/penalidades. |
| **MG — PAT / RPTA**<br>(Dec. 44.747/2008) | Resumo enxuto de 190 linhas. | Substituído pelo Regulamento do Processo e dos Procedimentos Tributários Administrativos (RPTA/CCMG) compilado pela ALMG (270 KB HTML, mais de 215.000 caracteres de texto puro). |
| **MG — RICMS**<br>(Dec. 48.589/2023) | Ficha sumária de 88 linhas. | Incorporado o texto oficial compilado do Decreto nº 48.589/2023 da ALMG (446 KB HTML), com preservação adicional do recorte de TTS e e-commerce com nota editorial canônica. |
| **RJ — IPVA**<br>(Lei 2.877/1997) | Mistura de EC 132/2023 e Tema 708 nos arts. 1º e 2º-A; supressão das redações históricas da ALERJ. | Transcrição autêntica direta da base Lotus Notes da ALERJ, mantendo o histórico de redações revogadas/tachadas (`~~...~~`) e as redações vigentes de veículos terrestres, alíquotas e isenções. |
| **RJ — ITD**<br>(Lei 7.174/2015) | Artigos fabricados com citações doutrinárias e do STF (Tema 1214) nos parágrafos. | Texto autêntico da ALERJ (arts. 1º a 46), com a tabela progressiva oficial de alíquotas de 4% a 8%, regras de avaliação pela SEFAZ-RJ e prazos recursais. |
| **RJ — ICMS**<br>(Lei 2.657/1996) | Resumo padronizado de 264 linhas omitindo dezenas de capítulos da lei orgânica. | Incorporado o texto consolidado da Lei nº 2.657/1996 da ALERJ (660 KB HTML, quase 400.000 caracteres de texto legal), incluindo substituição tributária e penalidades. |
| **RJ — PAT / CTE**<br>(DL 5/1975) | Recorte editorial informal. | Recorte oficial literal do Livro Terceiro do Código Tributário Estadual (Decreto-Lei nº 5/1975), cobrindo o Processo Administrativo-Tributário, Junta de Revisão Fiscal e CCRF-RJ, com nota editorial canônica. |
| **ES — IPVA**<br>(Lei 6.999/2001) | Template com referências artificiais a convênios CONFAZ e jurisprudência interestadual vinculante. | Transcrição oficial da ALES (363 KB HTML em UTF-16), com todos os artigos sobre fato gerador, base FIPE, alíquotas (1% e 2%) e isenções para PcD e frotistas. |
| **ES — ITCMD**<br>(Lei 10.011/2013) | Artigo 2º fabricado com subitens numerados para regras interestaduais; inserção do Tema 1214. | Transcrição autêntica da ALES (208 KB HTML em UTF-16), contendo a redação oficial dos arts. 1º a 28, com alíquota única estadual de 4% e procedimento administrativo. |
| **ES — ICMS**<br>(Lei 7.000/2001) | Versão resumida com perda de centenas de artigos sobre substituição e crédito. | Incorporada a íntegra consolidada oficial da ALES (4,1 MB HTML, quase 600.000 caracteres), preservando a totalidade dos livros e anexos normativos da lei orgânica do ICMS capixaba. |
| **ES — COMPETE/INVEST**<br>(Lei 10.568/2016) | Resumo genérico de 80 linhas. | Transcrição oficial integral da Lei nº 10.568/2016 da ALES (469 KB HTML), cobrindo todos os regimes de desenvolvimento econômico (COMPETE-ES e INVEST-ES). |

---

## 11 documentos acrescentados

### São Paulo
1. [Lei nº 16.006/2015 — FECOEP/SP](../estaduais/sp/leis/fundos/lei-16006-2015-fecoep.md): Institui o Fundo Estadual de Combate e Erradicação da Pobreza no Estado de São Paulo.
2. [Lei nº 17.293/2020 — Ajuste Fiscal e Alíquotas](../estaduais/sp/leis/icms/lei-17293-2020-ajuste-fiscal-aliquotas.md): Estabelece medidas de equilíbrio fiscal, renovação e redução de benefícios fiscais do ICMS, IPVA e ITCMD.

### Minas Gerais
3. [Lei nº 19.990/2011 — FEM/MG](../estaduais/mg/leis/fundos/lei-19990-2011-fem.md): Cria o Fundo de Erradicação da Miséria - FEM no Estado de Minas Gerais.
4. [Lei nº 24.475/2023 — Alíquota Modal e Adicional do FEM](../estaduais/mg/leis/icms/lei-24475-2023-aliquota-fem.md): Altera a Lei nº 6.763/1975 e restabelece o adicional de alíquota do ICMS destinado ao FEM sobre supérfluos.

### Rio de Janeiro
5. [Lei nº 10.253/2023 — Alíquota Modal do ICMS (20%)](../estaduais/rj/leis/icms/lei-10253-2023-aliquota-modal.md): Fixa a alíquota modal interna do ICMS no Rio de Janeiro em 20% (carga de 22% com FECP).
6. [Lei nº 8.645/2019 — FOT/RJ](../estaduais/rj/leis/fundos/lei-8645-2019-fot.md): Institui o Fundo Orçamentário Temporário em substituição ao FEEF no âmbito do Regime de Recuperação Fiscal.
7. [Lei nº 7.428/2016 — FEEF/RJ](../estaduais/rj/leis/fundos/lei-7428-2016-feef.md): Instituidor original do Fundo Estadual de Equilíbrio Fiscal no Rio de Janeiro (Convênio ICMS 42/2016).
8. [Lei nº 4.056/2002 — FECP/RJ](../estaduais/rj/leis/fundos/lei-4056-2002-fecp.md): Norma fundamental instituidora do Fundo Estadual de Combate à Pobreza e Desigualdades Sociais.

### Espírito Santo
9. [Lei nº 12.020/2023 — Manutenção da Alíquota Modal em 17%](../estaduais/es/leis/icms/lei-12020-2023-aliquota-modal.md): Revogou a Lei nº 11.981/2023, mantendo expressamente a alíquota geral interna do ICMS em 17%.
10. [Lei nº 7.001/2001 — Taxas e Contencioso Administrativo](../estaduais/es/leis/pat/lei-7001-2001-taxas-cerf-es.md): Disciplina o regime de taxas estaduais e normas gerais do contencioso fiscal.
11. [Lei nº 10.370/2015 — CERF/ES](../estaduais/es/leis/pat/lei-10370-2015-cerf-es.md): Lei orgânica e regimento do Conselho Estadual de Recursos Fiscais e do PAT capixaba.

---

## Fontes oficiais de confronto

- **São Paulo**:
  - Repositório de Legislação da Assembleia Legislativa do Estado de São Paulo: `https://www.al.sp.gov.br/repositorio/legislacao/`
  - Portal da Legislação da Secretaria da Fazenda e Planejamento de São Paulo: `https://legislacao.fazenda.sp.gov.br`
- **Minas Gerais**:
  - Portal da Legislação Mineira da Assembleia Legislativa do Estado de Minas Gerais: `https://www.almg.gov.br/legislacao-mineira/`
  - Sistema de Impressão e Compilação da ALMG: `https://www.almg.gov.br/atividade-parlamentar/leis/legislacao-mineira/lei/texto/print.html`
- **Rio de Janeiro**:
  - Base de Legislação da Assembleia Legislativa do Estado do Rio de Janeiro (Lotus Notes Oficial): `http://alerjln1.alerj.rj.gov.br/`
  - Secretaria de Estado de Fazenda do Rio de Janeiro: `https://www.fazenda.rj.gov.br`
- **Espírito Santo**:
  - Acervo Digital de Legislação da Assembleia Legislativa do Estado do Espírito Santo: `https://www3.al.es.gov.br/Arquivo/Documents/legislacao/html/`
  - Legislação da Secretaria de Estado da Fazenda do Espírito Santo: `https://internet.sefaz.es.gov.br/legislacao/`

---

## Método e limites

1. **Captura direta e decodificação rigorosa**:
   - Para SP, extração do HTML compilado em Latin-1/UTF-8 nos endpoints estáticos oficiais da ALSP.
   - Para MG, utilização do serviço oficial de compilação pura da ALMG (`print.html`), eliminando menus, scripts e iframes de navegação do portal principal.
   - Para RJ, acesso aos documentos oficiais no Lotus Notes (`alerjln1.alerj.rj.gov.br`), decodificando a formatação e preservando o tachado histórico (`~~...~~`) das alterações legislativas.
   - Para ES, tratamento de encoding UTF-16-LE com Byte Order Mark (`\xff\xfe`) nas normas da ALES, permitindo a extração integral e fiel dos arquivos gerados pelo Microsoft Word no portal legislativo.

2. **Conversão e estruturação para CommonMark estrito**:
   - Remoção de tags HTML residuais (`<p>`, `<div>`, `<span>`, `<br>`, etc.) vedadas pelas diretrizes do repositório.
   - Conversão de tabelas HTML para sintaxe GFM (`| ... |`).
   - Eliminação de resíduos de navegação na web ("voltar ao topo", "clique aqui", "ficha informativa", etc.).
   - Aplicação de frontmatter YAML canônico contendo todas as propriedades obrigatórias (`data_consulta: "2026-11-05"`, `natureza_conteudo`).
   - Aplicação de nota editorial padronizada (`## Nota editorial de conferência — 05/11/2026`) para os recortes temáticos oficiais (DL 5/1975 Livro do PAT, TTS RICMS/MG, Lei 7.001/2001 Taxas).

3. **Geração de manifesto de integridade**:
   - O arquivo [_auditoria/sudeste_fontes_2026-11-05.json](sudeste_fontes_2026-11-05.json) registra para cada um dos 32 documentos: URL direta oficial, hash SHA-256 do HTML original baixado, volume de bytes do HTML, quantidade de caracteres alfanuméricos de texto legal, status de fidelidade textual normalizada e hash SHA-256 do arquivo Markdown gerado.

---

## Validação executada

- **Auditoria de integridade estrutural e de schema**: 32 de 32 documentos aprovados pelo `AgenteAuditor` independente (`scripts/agentes/agente_auditor.py`).
- **Verificação de tags residuais**: 0 tags HTML proibidas em todos os 32 arquivos.
- **Validação de links**: URLs diretas e oficiais atribuídas no campo `fonte`.
- **Compatibilidade de repositório**: Nenhuma alteração efetuada nos arquivos compartilhados restritos (`scripts/plano.py`, `ACERVO.md`, `PROGRESSO.md`, `WORKLOG.md`), assegurando conformidade estrita com o papel delegado ao subagente da Região Sudeste.
