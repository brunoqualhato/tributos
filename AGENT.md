# Diretrizes Gerais de Agentes (AGENT.md) — Acervo Tributário & Contábil

Este documento define as regras operacionais, taxonomia, padrões de engenharia de dados e protocolos de governança que qualquer agente ou desenvolvedor deve seguir ao operar neste repositório.

---

## 1. Missão do Projeto

Construir o acervo definitivo, aberto e de alta fidelidade do **Direito Tributário, Legislação Fiscal e Normas Contábeis Brasileiras** em **Markdown estruturado com metadados YAML canônicos**.

O projeto tem como padrão arquitetural a disciplina do [`ctresb/leis`](https://github.com/ctresb/leis), adaptado com foco cirúrgico nos **10 Pilares do Sistema Tributário e Contábil Nacional (1.241 Normas Catalogadas)**:
1. 🏛️ **Legislação Estruturante & Códigos**: Código Tributário Nacional (CTN Lei 5.172/66), Simples Nacional (LC 123/06), PAF Federal (Dec. 70.235/72) e Processo Tributário Estadual (PAT/PAF das Fazendas Estaduais).
2. 💰 **Dividendos & Renda do Capital**: Isenção de dividendos (Lei 9.249/95), JCP (Juros sobre Capital Próprio), IRPJ e CSLL (Lucro Real, Presumido e Arbitrado), RIR/2018 integral, Offshores e Trusts (Lei 14.754/23) e Subvenções (Lei 14.789/23).
3. 👥 **Folha de Pagamento & Encargos**: Custeio da Previdência Social (Lei 8.212/91), RPS (Dec. 3.048/99), INSS patronal, RAT/FAP, Sistema S, CPRB (Lei 14.973/24), FGTS Digital e Pasep Governamental.
4. 📦 **Produtos & Mercadorias**: Leis Orgânicas do ICMS das 27 UFs, RICMS das 27 UFs, Fundos Agropecuários (FETHAB, FUNDEINFRA, FUNDERSUL, FECOP, FAIN), Lei Kandir (LC 87/96), DIFAL (LC 190/22), Convênio ICMS-ST 142/18, IPI, PIS/COFINS regimes monofásicos e Regulamento Aduaneiro.
5. 💼 **Serviços & Retenções**: ISSQN geral (LC 116/03), CTMs e Regulamentos do ISS de todas as 26 Capitais Estaduais + DF, Retenções na Fonte (CSRF 4,65%, IRRF 1,5% e INSS 11%).
6. 🏰 **Patrimônio, Herança & Veículos**: Leis do ITCMD das 27 UFs (Res. Senado 9/92), Leis do IPVA das 27 UFs, ITR Federal, ITBI e IPTU municipais.
7. ⛽ **Combustíveis & Energia**: CIDE-Combustíveis, Lei do Petróleo, Regime Monofásico ad rem de ICMS (LC 192/22), RenovaBio e Mercado de Carbono.
8. 📈 **Tributação Financeira & IOF**: RIOF (Dec. 6.306/07), IOF Crédito/Câmbio/Títulos, Renda Fixa/Variável e Criptoativos.
9. 🚀 **Reforma Tributária & Transição**: EC 132/23, LC 214/25 (IBS/CBS/IS), LC 227/26 (Comitê Gestor), Split Payment Inteligente e Publicações Oficiais.
10. 📊 **Normas Contábeis, CARF & Jurisprudência**: Pronunciamentos Técnicos CPC (00 a 48), NBC TG do CFC (01 a 48, 1000), Súmulas Vinculantes do CARF e Precedentes Vinculantes do STF e STJ.

---

## 2. Padrão Estrito dos Documentos (.md)

Todo documento legal gerado DEVE possuir cabeçalho YAML canônico delimitado por `---`, seguido imediatamente pelo título de primeiro nível (`# `) e pelo corpo da norma em CommonMark:

```markdown
---
titulo: "Portaria Conjunta MF / CGIBS nº 14, de 2 de outubro de 2026"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil"
tipo: "Portaria Conjunta"
numero: "14"
data: "2026-10-05"
ano: "2026"
tema_tributario: "Folha de Pagamento e Encargos"
tributos_afetados: ["Cofins", "Imposto de Importação", "RAT/FAP"]
situacao: "Em vigor"
revogada: false
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/153937"
ementa: "Aprova a metodologia de cálculo da carga tributária para a fixação das alíquotas..."
---

# Portaria Conjunta MF / CGIBS nº 14, de 2 de outubro de 2026

Texto integral da norma...
```

### Regras de Qualidade Formal:
- **Zero HTML Residual:** Proibido o uso de `<div>`, `<span>`, `<br>`, `<style>`, `<font>` no corpo do Markdown. O parser [`scripts/html2md.py`](file:///Users/brunoqualhato/Documents/meus/tributos/scripts/html2md.py) deve converter tabelas para Markdown (`|---|`) e manter tachados (`~~`).
- **Limpeza de Ementa:** Tags HTML residuais em ementas devem ser completamente suprimidas.
- **Hierarquia:** Preservar a estrutura jurídica (Livros, Títulos, Capítulos, Seções, Artigos, Parágrafos, Incisos e Alíneas).

---

## 3. Política de Links de Referência Diretos Oficiais

> [!IMPORTANT]
> **Proibido o uso de links legados ou telas de busca genéricas no campo `fonte:`.** O link deve abrir a visualização direta da norma no navegador de qualquer usuário:

1. **Receita Federal (Sijut):**
   * ✅ **CORRETO:** `https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{idAto}`
   * ❌ **PROIBIDO:** `https://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action?idAto=...` (retorna tela vazia).
2. **Legislação Federal (LexML / Senado):**
   * ✅ **CORRETO:** `https://normas.leg.br/?urn={URN_LEXML}`
3. **Normas Contábeis (CPC / CFC):**
   * ✅ **CORRETO:** Link direto do portal oficial do CPC (`http://www.cpc.org.br/...`).
4. **Domínios Oficiais Permitidos:** Apenas órgãos com sufixo `.gov.br`, `.leg.br`, `.jus.br`, `.org.br` oficial registrado (como `cfc.org.br` e `cpc.org.br`).

---

## 4. O Sistema de Agentes Especialistas

O projeto conta com agentes autônomos documentados em [`.agents/agents/`](file:///Users/brunoqualhato/Documents/meus/tributos/.agents/agents):

### Especialistas de Domínio:
* `tributos_dividendos`: Gestor e auditor das normas de IRPJ/CSLL, JCP e distribuição de lucros.
* `tributos_folha`: Gestor e auditor de INSS patronal, RAT/FAP, Sistema S, CPRB e retenções trabalhistas.
* `tributos_produtos`: Gestor e auditor de ICMS, ICMS-ST, CONFAZ, IPI, Monofásicos e Reforma Tributária.
* `tributos_servicos`: Gestor e auditor de ISSQN, CSRF 4,65% e retenções federais de serviços.

### Especialistas da Esteira Operacional:
* `tax_api_collector`: Consome APIs REST oficiais (Sijut, LexML, Câmara, Senado).
* `tax_web_scraper`: Extrai dados de portais sem API com controle estrito de rate-limiting (CONFAZ, SEFAZ, CPC).
* `tax_doc_structurer`: Parser, classificador semântico e formatador de CommonMark.
* `tax_auditor`: Valida esquema e integridade de cada arquivo contra a rede (`--rede`).
* `tax_link_auditor`: Valida e higieniza concorrentemente todos os links de visualização direta.
* `tax_git_workflow`: Gestor de versionamento, PRs e documentação contínua.

---

## 5. Política de Commits Atômicos, Pull Requests Granulares e Documentação Contínua

> [!IMPORTANT]
> **Regra de Ouro:** *SEMPRE ABRA PULL REQUEST PARA NOVOS ITENS OU CORREÇÕES, UTILIZANDO COMMITS ATÔMICOS E PRS PEQUENAS E TEMÁTICAS.*

1. **Nunca commitar novos lotes diretamente na `main` sem validação.**
2. **Commits Atômicos e PRs Granulares:**
   - **Commits Atômicos:** 1 commit por norma adicionada, correção pontual ou documento estruturado, com mensagem semântica clara (ex: `feat(folha): adiciona IN RFB 2110/2022`).
   - **Pull Requests Pequenas e Focadas:** Criar PRs reduzidas (entre 3 a 15 documentos de um único tema ou pilar específico), nunca acumulando centenas de arquivos misturados em uma única PR gigante. Várias PRs menores são explicitamente desejadas para maximizar a organização e rastreabilidade.
3. **Fluxo Obrigatório para Novas Coletas:**
   1. Criar branch temática: `git checkout -b <tema>/<subtema-especifico>`
   2. Executar ingestão e estruturação dos arquivos.
   3. Executar o auditor de integridade: `python3 scripts/auditar.py --rede`. (Apenas lotes com 100% de aprovação podem avançar).
   4. Atualizar o catálogo de documentos: `python3 scripts/catalogo.py`.
   5. Recalcular o progresso: `python3 scripts/progresso.py`.
   6. Registrar marco no [`WORKLOG.md`](file:///Users/brunoqualhato/Documents/meus/tributos/WORKLOG.md).
   7. Realizar commits atômicos por documento.
   8. Enviar o branch ao GitHub: `git push -u origin <branch>`
   9. Abrir o Pull Request temático: `gh pr create --base main --title "feat(<tema>): ..." --body "..."`
