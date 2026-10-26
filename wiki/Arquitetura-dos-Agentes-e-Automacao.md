---

## 2. Mapa dos Agentes do Sistema

```mermaid
flowchart TD
    subgraph Orquestração e Agendamento
        SCHED["Daemon Cron de 2h (Antigravity local)"]
        ROTINA["scripts/rotina_ciclica_2h.py"]
        SCHED --> ROTINA
    end

    subgraph Agentes Especialistas de Domínio
        A1["tributos_dividendos: IRPJ, Lucro Real, JCP, RIR/18"]
        A2["tributos_folha: INSS, CPRB, RAT/FAP, Sistema S"]
        A3["tributos_produtos: ICMS, ICMS-ST, DIFAL, IPI"]
        A4["tributos_servicos: ISS, CSRF 4,65%, IRRF 1,5%"]
        A5["tributos_patrimonio: ITCMD, IPVA, ITR, IPTU"]
        A6["tributos_combustiveis: CIDE, ICMS ad rem LC 192/22"]
        A7["tributos_financeiro: IOF, Criptoativos, Câmbio"]
        A8["tributos_reforma: IBS, CBS, Split Payment, CG-IBS"]
    end

    subgraph Agentes Operacionais e de Qualidade
        O1["tax_api_collector: Consumo Sijut/RFB e LexML"]
        O2["tax_web_scraper: Portais sem API (CONFAZ, CPC, CFC)"]
        O3["tax_doc_structurer: Conversão CommonMark e Frontmatter"]
        O4["tax_link_auditor: Saneamento Concorrente de URLs"]
        O5["tax_auditor: Auditoria Independente de Rede"]
        O6["tax_git_workflow: Commits Atômicos e Pull Requests"]
    end

    ROTINA --> A1 & A2 & A3 & A4 & A5 & A6 & A7 & A8
    ROTINA --> O1 & O2 & O3
    O3 --> O4 --> O5 --> O6
```

---

## 3. Diretrizes Inegociáveis de Qualidade e Governança

1. **Sempre Abrir PR:** Nenhuma ingestão de lote é commitada diretamente na branch `main`. Toda expansão gera uma branch temática e abre uma Pull Request via `gh pr create`.
2. **Auditoria de Rede Obrigatória (`scripts/auditar.py --rede`):** Nenhum documento é integrado se não possuir link oficial ativo com resposta HTTP válida de órgãos governamentais permitidos (`normas.leg.br`, `normasinternet2.receita.fazenda.gov.br`, `confaz.fazenda.gov.br`, `cpc.org.br`, `cfc.org.br`).
3. **Links Oficiais Diretos e Navegáveis:** É terminantemente proibido o uso de URLs legadas de busca em branco (como `sijut2consulta/consulta.action`). Todas as normas da Receita Federal apontam para o SPA visual direto `https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{idAto}`.
4. **Documentação Viva e Sincronizada:** A cada lote, [`ACERVO.md`](file:///Users/brunoqualhato/Documents/meus/tributos/ACERVO.md), [`PROGRESSO.md`](file:///Users/brunoqualhato/Documents/meus/tributos/PROGRESSO.md) e [`WORKLOG.md`](file:///Users/brunoqualhato/Documents/meus/tributos/WORKLOG.md) são automaticamente recalculados e atualizados.
