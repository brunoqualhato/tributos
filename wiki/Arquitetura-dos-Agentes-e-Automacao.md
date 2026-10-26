# 🤖 Arquitetura dos Agentes, Auditoria e Automação Local

## 1. Visão Geral da Arquitetura
O repositório **Tributos** adota o paradigma de agentes autônomos especializados, operando de forma concorrente sobre a base de conhecimento sob as diretrizes do Antigravity.

## 2. Mapa dos Agentes do Sistema
- **Orquestração e Agendamento:**
  - Daemon Cron de 2h agendado internamente no Antigravity (`task-606`).
  - Script orquestrador local: `scripts/rotina_ciclica_2h.py`.
- **Agentes Especialistas de Domínio:**
  - `tributos_dividendos`: IRPJ, Lucro Real, JCP, RIR/2018 integral, Offshores e Subvenções.
  - `tributos_folha`: INSS Patronal, CPRB (Lei 14.973/24), RAT/FAP, Sistema S, DCTFWeb.
  - `tributos_produtos`: ICMS (LC 87/96), DIFAL (LC 190/22), CONFAZ (ICMS-ST), IPI e PIS/Cofins Monofásicos.
  - `tributos_servicos`: ISSQN (LC 116/03), Legislação de SP, RJ e BH, Retenções CSRF, IRRF e INSS.
  - `tributos_patrimonio`: ITCMD (Res. Senado 9/92), IPVA, ITR (Lei 9.393/96) e IPTU/ITBI (DL 57/66).
  - `tributos_combustiveis`: CIDE-Combustíveis (Lei 10.336/01), ICMS monofásico *ad rem* (LC 192/22) e Convênios.
  - `tributos_financeiro`: IOF (Dec. 6.306/07), Câmbio, Criptoativos (IN 1.888/19).
  - `tributos_reforma`: EC 132/23, PLP 68/24, PLP 108/24, Split Payment e Comitê Gestor.
- **Agentes Operacionais e de Qualidade:**
  - `tax_api_collector`: Mineração contínua de APIs Sijut/RFB e LexML em série histórica.
  - `tax_web_scraper`: Extração de portais sem API (CONFAZ, CPC, CFC).
  - `tax_doc_structurer`: Normalização para CommonMark estrito e frontmatter YAML canônico.
  - `tax_link_auditor`: Saneamento de URLs para visualização direta oficial.
  - `tax_auditor`: Portão independente de auditoria com validação ativa de rede (`--rede`).
  - `tax_git_workflow`: Versionamento atômico e criação de Pull Requests via `gh`.

## 3. Diretrizes Inegociáveis de Qualidade e Governança
1. **Sempre Abrir PR:** Nenhuma ingestão de lote é commitada diretamente na branch `main`. Toda expansão gera uma branch temática e abre uma Pull Request via `gh pr create`.
2. **Auditoria de Rede Obrigatória (`scripts/auditar.py --rede`):** Nenhum documento é integrado se não possuir link oficial ativo com resposta HTTP válida de órgãos governamentais permitidos (`normas.leg.br`, `normasinternet2.receita.fazenda.gov.br`, `confaz.fazenda.gov.br`, `cpc.org.br`, `cfc.org.br`).
3. **Links Oficiais Diretos e Navegáveis:** É terminantemente proibido o uso de URLs legadas de busca em branco (como `sijut2consulta/consulta.action`). Todas as normas da Receita Federal apontam para o SPA visual direto `https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{idAto}`.
4. **Documentação Viva e Sincronizada:** A cada lote, [`ACERVO.md`](../ACERVO.md), [`PROGRESSO.md`](../PROGRESSO.md) e [`WORKLOG.md`](../WORKLOG.md) são automaticamente recalculados e atualizados.
