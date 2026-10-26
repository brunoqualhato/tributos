# Diretrizes Gerais de Agentes (AGENT.md) — Acervo Tributário & Contábil

Este documento define as regras operacionais, taxonomia, padrões de engenharia de dados e protocolos de governança que qualquer agente ou desenvolvedor deve seguir ao operar neste repositório.

---

## 1. Missão do Projeto

Construir o acervo definitivo, aberto e de alta fidelidade do **Direito Tributário, Legislação Fiscal e Normas Contábeis Brasileiras** em **Markdown estruturado com metadados YAML canônicos**.

O projeto tem como padrão arquitetural a disciplina do [`ctresb/leis`](https://github.com/ctresb/leis), adaptado com foco cirúrgico nos **4 Pilares Tributários Fundamentais + Contabilidade**:
1. 💰 **Dividendos & Renda do Capital**: Isenção de dividendos (Lei 9.249/95), JCP (Juros sobre Capital Próprio), IRPJ e CSLL (Lucro Real, Presumido e Arbitrado), RIR/2018, Offshores e Trusts (Lei 14.754/23) e Subvenções (Lei 14.789/23).
2. 👥 **Folha de Pagamento & Encargos**: Custeio da Previdência Social (Lei 8.212/91), INSS patronal, RAT/FAP, Contribuições ao Sistema S, Retenção do IRPF na folha, PLR (Lei 10.101/00), Desoneração da Folha (CPRB - Lei 12.546/11) e FGTS (Lei 8.036/90).
3. 📦 **Produtos & Mercadorias**: ICMS (Lei Kandir LC 87/96 e LC 190/22 DIFAL), Convênios e Protocolos CONFAZ (Substituição Tributária - ICMS-ST Convênio 142/18), IPI (Lei 4.502/64 e RIPI/2010), PIS/COFINS regimes monofásicos e concentrados, Regulamento Aduaneiro e Imposto Seletivo (EC 132/23).
4. 💼 **Serviços & Retenções**: ISSQN (Lei Complementar 116/2003 e CTMs das capitais), Retenções na Fonte sobre serviços tomados (CSRF 4,65% - art. 30 da Lei 10.833/03; IRRF 1,5% serviços regulamentados; Retenção INSS 11% cessão de mão de obra) e transição para o IBS/CBS.
5. 📊 **Normas Contábeis & Jurisprudência**: Pronunciamentos Técnicos CPC (CPC 00 R2, CPC 32 Tributos sobre o Lucro), Normas Brasileiras de Contabilidade do CFC (NBC TG), Súmulas e Acórdãos do CARF, Súmulas Vinculantes e Temas Tributários do STF/STJ.

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

## 5. Política de Commits, Pull Requests e Documentação Contínua

> [!IMPORTANT]
> **Regra de Ouro:** *SEMPRE ABRA PULL REQUEST PARA NOVOS ITENS OU CORREÇÕES.*

1. **Nunca commitar novos lotes diretamente na `main` sem validação.**
2. **Fluxo Obrigatório para Novas Coletas:**
   1. Criar branch temática: `git checkout -b coleta/<nome-do-lote>`
   2. Executar ingestão e estruturação dos arquivos.
   3. Executar o auditor de integridade: `python3 scripts/auditar.py --rede`. (Apenas lotes com 100% de aprovação podem avançar).
   4. Atualizar o catálogo de documentos: `python3 scripts/catalogo.py`.
   5. Recalcular o progresso: `python3 scripts/progresso.py`.
   6. Registrar marco no [`WORKLOG.md`](file:///Users/brunoqualhato/Documents/meus/tributos/WORKLOG.md).
   7. Commitar as alterações no branch.
   8. Enviar o branch ao GitHub: `git push -u origin <branch>`
   9. Abrir o Pull Request automaticamente: `gh pr create --base main --title "..." --body "..."`
