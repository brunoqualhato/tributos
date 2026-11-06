# Revisão Documental e Auditoria de Fidelidade — Região Nordeste 2 (PB, RN, AL, PI, SE) — 05/11/2026

## 1. Resultado e Escopo

Esta auditoria e revisão documental cobriu exaustivamente a legislação tributária estadual dos cinco estados da Região Nordeste 2:
- **Paraíba (PB)**: `estaduais/pb/`
- **Rio Grande do Norte (RN)**: `estaduais/rn/`
- **Alagoas (AL)**: `estaduais/al/`
- **Piauí (PI)**: `estaduais/pi/`
- **Sergipe (SE)**: `estaduais/se/`

Foram auditados, saneados e padronizados **33 documentos** (6 normas principais por estado, acrescidas de preservação canônica para referências históricas e cruzadas).

A auditoria baseou-se diretamente nos portais e repositórios oficiais dos Poderes Legislativo e Executivo estaduais:
- **PB**: Secretaria de Estado da Fazenda (SEFAZ-PB) e Assembleia Legislativa da Paraíba (ALPB).
- **RN**: Gabinete Civil / Sistema de Legislação Estadual (GAC-RN / ADCON) e Assembleia Legislativa do Rio Grande do Norte (ALRN).
- **AL**: Secretaria de Estado da Fazenda (SEFAZ-AL) e Assembleia Legislativa de Alagoas (ALEAL).
- **PI**: Sistema de Apoio ao Processo Legislativo (SAPL ALEPI) e Diário Oficial do Estado do Piauí (DOE-PI).
- **SE**: Procuradoria-Geral do Estado de Sergipe (LegisOn PGE-SE) e Secretaria de Estado da Fazenda (SEFAZ-SE).

---

## 2. Inconsistências Materiais Identificadas e Saneadas

O problema mais grave identificado no acervo anterior era de ordem material e de integridade jurídica:
1. **Artigos Fabricados e Falsas Redações Legais (ITCMD e IPVA):**
   - Nas leis de ITCMD e IPVA de múltiplos estados (PB, RN, AL, PI e SE), havia sido introduzida uma redação genérica idêntica e artificial, com artigos renumerados (ex: Arts. 1º a 3º) incorporando julgamentos do STF (Tema 708 - RE 1016605), Convênios ICMS (como Convênio ICMS 64/2006) e diretrizes da Emenda Constitucional nº 132/2023 como se fossem texto legal aprovado pelas Assembleias Legislativas nas décadas de 1980 e 1990.
   - **Correção executada:** Expurgadas integralmente todas as cláusulas doutrinárias e disposições apócrifas. Todos os diplomas foram substituídos pelo texto legal autêntico, extraído dos Diários Oficiais e consolidações oficiais vigentes.
2. **Capítulos Fictícios no ICMS do Piauí:**
   - Em `estaduais/pi/leis/icms/lei-4257-1989.md`, a lei primitiva de 92 artigos havia sido reduzida a um resumo de 19 artigos que incluía capítulos artificiais sobre *"Polo do MATOPIBA"* e *"Parques Solares e Eólicos"*, inexistentes na Lei nº 4.257/1989.
   - **Correção executada:** Transcrita a íntegra autêntica dos 92 artigos da Lei nº 4.257/1989 a partir do Diário Oficial do Estado nº 05 de 06/01/1989 (SAPL ALEPI ID 1689).
3. **Inadequação de Referências de Leis de PAT e Alíquota Modal:**
   - **Piauí (PAT):** A referência preliminar apontava "Lei 5.025/1998". A verificação documental comprovou que a Lei 5.025/1998 cuidou de abertura de crédito suplementar; a lei em vigor que disciplina o PAT, o TARF e a consulta fiscal é a **Lei Estadual nº 6.949/2017** (SAPL ALEPI ID 4094), transcrita na íntegra.
   - **Piauí (Alíquota Modal):** A referência "Lei 7.907/2022" correspondia a uma declaração de utilidade pública (SAPL ID 5456); a norma que aprovou a alíquota modal de 21% no art. 23 da Lei 4.257/1989 foi a **Lei Complementar Estadual nº 269/2022** (publicada no DOE de 08/12/2022, SAPL ID 5431), transcrita na íntegra e documentada em ambas as entradas.
   - **Sergipe (Alíquota Modal):** A menção à "Lei 9.151/2022" cuidou de doação imobiliária ao Município de Propriá; a fixação da alíquota modal de 19% no art. 18 da Lei 3.796/1996 decorreu da **Lei Estadual nº 9.176/2023** (publicada no DOE de 31/03/2023, LegisOn ID 23510), transcrita na íntegra.
4. **Resíduos de Web/Navegação e Padronização Matemática:**
   - Removidos cabeçalhos repetitivos de paginação ASP/HTML ("clique aqui", "topo", etc.).
   - Fórmulas de cálculo de DIFAL por base dupla foram transcritas e estruturadas em notação matemática LaTeX ($$...$$).

---

## 3. Matriz de Documentos Auditados e Saneados

| UF | Tema / Tributo | Arquivo Markdown | Diploma Legal | Fonte Oficial Direta | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PB** | ICMS (Geral) | `estaduais/pb/leis/icms/lei-6379-1996.md` | Lei nº 6.379/1996 | SEFAZ-PB / ALPB | Saneado (Texto autêntico) |
| **PB** | RICMS | `estaduais/pb/ricms/decreto-18930-1997.md` | Decreto nº 18.930/1997 | SEFAZ-PB (atua. Dec. 49.005/2026) | Saneado (Recorte oficial) |
| **PB** | ITCMD | `estaduais/pb/leis/itcmd/lei-5123-1989.md` | Lei nº 5.123/1989 | SEFAZ-PB / ALPB | Saneado (Texto integral) |
| **PB** | IPVA | `estaduais/pb/leis/ipva/lei-11007-2017.md` | Lei nº 11.007/2017 | SEFAZ-PB (atua. Lei 14.747/2026) | Saneado (Texto integral) |
| **PB** | PAT | `estaduais/pb/leis/pat/lei-10094-2013.md` | Lei nº 10.094/2013 | SEFAZ-PB / ALPB | Adicionado (Texto integral) |
| **PB** | Alíquota Modal | `estaduais/pb/leis/icms/lei-12788-2023-aliquota-modal.md` | Lei nº 12.788/2023 | DOE-PB / ALPB | Adicionado (Texto integral) |
| **RN** | ICMS (Geral) | `estaduais/rn/leis/icms/lei-6968-1996.md` | Lei nº 6.968/1996 | ALRN / GAC-RN | Saneado (Texto integral) |
| **RN** | RICMS | `estaduais/rn/ricms/decreto-31825-2022.md` | Decreto nº 31.825/2022 | GAC-RN (ADCON) | Saneado (Recorte oficial) |
| **RN** | ITCMD | `estaduais/rn/leis/itcmd/lei-9993-2015.md` | Lei nº 9.993/2015 | ALRN / GAC-RN | Saneado (Texto integral) |
| **RN** | IPVA | `estaduais/rn/leis/ipva/lei-6967-1996.md` | Lei nº 6.967/1996 | DOE-RN / ALRN | Saneado (OCR oficial) |
| **RN** | Fundo (FCP) | `estaduais/rn/leis/fundos/lei-5887-1989-fcp.md` | Lei nº 5.887/1989 | GAC-RN / ADCON | Saneado (Texto integral) |
| **RN** | Alíquota Modal | `estaduais/rn/leis/icms/lei-11314-2022-aliquota-modal.md` | Lei nº 11.314/2022 | ALRN / GAC-RN | Adicionado (Texto integral) |
| **AL** | ICMS (Geral) | `estaduais/al/leis/icms/lei-5900-1996.md` | Lei nº 5.900/1996 | ALEAL / SEFAZ-AL | Saneado (Texto integral) |
| **AL** | RICMS | `estaduais/al/ricms/decreto-35245-1991.md` | Decreto nº 35.245/1991 | SEFAZ-AL | Saneado (Recorte oficial) |
| **AL** | ITCMD | `estaduais/al/leis/itcmd/lei-5077-1989.md` | Lei nº 5.077/1989 | CTE-AL / SEFAZ-AL | Saneado (Recorte oficial) |
| **AL** | IPVA | `estaduais/al/leis/ipva/lei-6555-2004.md` | Lei nº 6.555/2004 | ALEAL / SEFAZ-AL | Saneado (Texto integral) |
| **AL** | PAT | `estaduais/al/leis/pat/lei-6771-2006.md` | Lei nº 6.771/2006 | ALEAL / SEFAZ-AL | Adicionado (Texto integral) |
| **AL** | Alíquota Modal | `estaduais/al/leis/icms/lei-8779-2022-aliquota-modal.md` | Lei nº 8.779/2022 | DOE-AL / ALEAL | Adicionado (Texto integral) |
| **PI** | ICMS (Geral) | `estaduais/pi/leis/icms/lei-4257-1989.md` | Lei nº 4.257/1989 | SAPL ALEPI (ID 1689) | Saneado (Texto integral) |
| **PI** | RICMS | `estaduais/pi/ricms/decreto-21866-2023.md` | Decreto nº 21.866/2023 | DOE-PI (07/03/2023) | Saneado (Recorte oficial) |
| **PI** | ITCMD | `estaduais/pi/leis/itcmd/lei-4261-1989.md` | Lei nº 4.261/1989 | SAPL ALEPI (ID 2235) | Saneado (Texto integral) |
| **PI** | IPVA | `estaduais/pi/leis/ipva/lei-4548-1992.md` | Lei nº 4.548/1992 | SAPL ALEPI (ID 2732) | Saneado (Texto integral) |
| **PI** | PAT | `estaduais/pi/leis/pat/lei-5025-1998.md` | Lei nº 6.949/2017 | SAPL ALEPI (ID 4094) | Saneado (Vigente integral) |
| **PI** | PAT (Vigente) | `estaduais/pi/leis/pat/lei-6949-2017.md` | Lei nº 6.949/2017 | SAPL ALEPI (ID 4094) | Adicionado (Canônico) |
| **PI** | Alíquota Modal | `estaduais/pi/leis/icms/lei-7907-2022-aliquota-modal.md` | LC nº 269/2022 | SAPL ALEPI (ID 5431) | Saneado (Texto integral) |
| **PI** | Alíquota Modal (LC) | `estaduais/pi/leis/icms/lei-complementar-269-2022-aliquota-modal.md` | LC nº 269/2022 | SAPL ALEPI (ID 5431) | Adicionado (Canônico) |
| **SE** | ICMS (Geral) | `estaduais/se/leis/icms/lei-3796-1996.md` | Lei nº 3.796/1996 | LegisOn PGE-SE (ID 11895) | Saneado (Consolidação oficial) |
| **SE** | RICMS | `estaduais/se/ricms/decreto-21400-2002.md` | Decreto nº 21.400/2002 | LegisOn PGE-SE (ID 31521) | Saneado (Recorte oficial) |
| **SE** | ITCMD | `estaduais/se/leis/itcmd/lei-7724-2013.md` | Lei nº 7.724/2013 | LegisOn PGE-SE (ID 17290) | Saneado (Consolidação oficial) |
| **SE** | IPVA | `estaduais/se/leis/ipva/lei-7655-2013.md` | Lei nº 7.655/2013 | LegisOn PGE-SE (ID 17294) | Saneado (Consolidação oficial) |
| **SE** | PAT | `estaduais/se/leis/pat/lei-7651-2013.md` | Lei nº 7.651/2013 | LegisOn PGE-SE (ID 17293) | Adicionado (Consolidação oficial) |
| **SE** | Alíquota Modal | `estaduais/se/leis/icms/lei-9151-2022-aliquota-modal.md` | Lei nº 9.176/2023 | LegisOn PGE-SE (ID 23510) | Saneado (Texto integral) |
| **SE** | Alíquota Modal (9176) | `estaduais/se/leis/icms/lei-9176-2023-aliquota-modal.md` | Lei nº 9.176/2023 | LegisOn PGE-SE (ID 23510) | Adicionado (Canônico) |

---

## 4. Métodos, Tecnologia de Captura e OCR de Alta Fidelidade

1. **Extração Vetorial Nativa:**
   - Criado e compilado o utilitário nativo macOS `scripts/bin/extrair_pdf` (baseado em PDFKit / Swift), permitindo extrair textos com alta velocidade e preservação de caracteres diacríticos e estruturais.
2. **Apple Neural Engine OCR (Vision Framework):**
   - Para os documentos digitalizados em microfilme ou scanner óptico antigo (como Diários Oficiais das décadas de 1980 e 1990 da ALRN e ALEPI), desenvolveu-se e compilou-se a ferramenta nativa `scripts/bin/ocr_pdf` (baseada em `VNRecognizeTextRequest` em Swift).
   - O reconhecimento foi executado com nível de acurácia máxima (`.accurate`) e suporte à ortografia em língua portuguesa, viabilizando o resgate literal e autêntico de diplomas completos de dezenas de páginas sem distorções.
3. **Conversão HTML para CommonMark:**
   - Para portais com texto HTML estruturado (SEFAZ-PB e SEFAZ-AL), aplicou-se `scripts/html2md.py` combinado com pré-limpeza de tags e tabelas ASP/Word.
4. **Manifesto Criptográfico:**
   - Gerado o arquivo `_auditoria/nordeste_2_fontes_2026-11-05.json`, contendo a relação completa dos 33 documentos, seus hashes SHA-256, tamanhos em bytes e URLs das fontes oficiais.

---

## 5. Validação Executada e Conformidade Estrita

- **Validação de Schema:** Todos os 33 arquivos Markdown contêm frontmatter YAML válido com os 15 campos canônicos obrigatórios (`titulo`, `esfera: "Estadual"`, `orgao`, `tipo`, `numero`, `data`, `ano`, `tema_tributario`, `tributos_afetados`, `situacao`, `revogada: false`, `fonte`, `ementa`, `data_consulta: "2026-11-05"`, `natureza_conteudo`).
- **Integridade de Arquivos Compartilhados:** Em cumprimento rigoroso às diretrizes orquestradoras, **nenhum** arquivo compartilhado (`scripts/plano.py`, `ACERVO.md`, `PROGRESSO.md`, `WORKLOG.md`) foi modificado.
- **Isolamento de Escopo:** Todas as alterações limitaram-se aos diretórios sob jurisdição do agente (`estaduais/pb/`, `estaduais/rn/`, `estaduais/al/`, `estaduais/pi/`, `estaduais/se/`) e à pasta de evidências `_auditoria/`.
