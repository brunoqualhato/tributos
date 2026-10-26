# ⚖️ Legislação Tributária e Normas Contábeis Brasileiras em Markdown

[![Auditoria de Rede](https://img.shields.io/badge/Auditoria%20de%20Rede-100%25%20Aprovada-brightgreen.svg)](#auditoria-e-integridade)
[![Normas Catalogadas](https://img.shields.io/badge/Normas%20Catalogadas-370%2B-blue.svg)](ACERVO.md)
[![Wiki Oficial](https://img.shields.io/badge/Documentação-Wiki%20dos%209%20Pilares-orange.svg)](wiki/Home.md)
[![Licença](https://img.shields.io/badge/Licença-Dados%20Abertos%20Oficiais-lightgrey.svg)](#licença)

Um acervo de alta fidelidade contendo as normas do **Direito Tributário, Legislação Fiscal e Normas Contábeis Brasileiras**, convertidas de fontes oficiais para **Markdown estruturado** com cabeçalho YAML canônico, auditoria independente de rede e links de visualização direta oficial.

Inspirado na arquitetura e rigor de dados do [`ctresb/leis`](https://github.com/ctresb/leis), este repositório possui foco exclusivo no ecossistema fiscal, contábil e tributário nacional.

---

## 📚 [Acesse a Wiki do Repositório](wiki/Home.md)

Nossa **Wiki** contém guias temáticos e tabelas comparativas detalhadas para cada um dos 9 pilares do Direito Tributário nacional:

1. 💰 **[Pilar 1: Dividendos, JCP e Renda do Capital](wiki/Pilar-1-Dividendos-e-Renda-do-Capital.md)** — IRPJ, Lucro Real, JCP, RIR/2018, Offshores (Lei 14.754/23) e Subvenções (Lei 14.789/23).
2. 👥 **[Pilar 2: Folha de Pagamento e Encargos](wiki/Pilar-2-Folha-de-Pagamento-e-Encargos.md)** — INSS Patronal (20%), RAT/FAP, Sistema S, CPRB (Lei 14.973/24), FGTS e IRRF.
3. 📦 **[Pilar 3: Produtos, Mercadorias e Indústria](wiki/Pilar-3-Produtos-Mercadorias-e-ICMS.md)** — ICMS (LC 87/96), DIFAL (LC 190/22), ICMS-ST (Convênio 142/18), IPI (RIPI/2010 e TIPI), PIS/Cofins Monofásico.
4. 🛠️ **[Pilar 4: Serviços e Retenções na Fonte](wiki/Pilar-4-Servicos-e-Retencoes.md)** — ISSQN (LC 116/03), Retenções CSRF (4,65%), IRRF (1,5%) e INSS (11%).
5. 🏰 **[Pilar 5: Patrimônio, Herança e Veículos](wiki/Pilar-5-Patrimonio-Heranca-e-Veiculos.md)** — ITCMD (Res. Senado 9/92), IPVA, ITR (Lei 9.393/96) e IPTU/ITBI (Dec-Lei 57/66).
6. ⛽ **[Pilar 6: Combustíveis e Energia](wiki/Pilar-6-Combustiveis-e-Energia.md)** — CIDE-Combustíveis (Lei 10.336/01), ICMS Monofásico *ad rem* (LC 192/22) e Convênios CONFAZ.
7. 📈 **[Pilar 7: Tributação Financeira e IOF](wiki/Pilar-7-Tributacao-Financeira-e-IOF.md)** — IOF Crédito, Câmbio, Seguro e Títulos (Dec. 6.306/07) e Criptoativos (IN 1.888/19).
8. 🚀 **[Pilar 8: Reforma Tributária & Split Payment](wiki/Pilar-8-Reforma-Tributaria-e-Split-Payment.md)** — EC 132/23, IBS, CBS, Imposto Seletivo, **Split Payment Inteligente** (PLP 68/24) e Comitê Gestor (PLP 108/24).
9. 📊 **[Pilar 9: Normas Contábeis (CPC e CFC)](wiki/Pilar-9-Normas-Contabeis-CPC-e-CFC.md)** — Pronunciamentos CPC 00 a 48 e Normas Brasileiras de Contabilidade NBC TG.
10. 🤖 **[Arquitetura dos Agentes e Automação Local](wiki/Arquitetura-dos-Agentes-e-Automacao.md)** — Funcionamento dos agentes, auditoria e rotina de 2 horas.

---

## 📑 Governança e Catálogo Geral

* 📖 **[ACERVO.md](ACERVO.md):** Catálogo geral detalhado de todos os 370+ documentos catalogados, agrupados por tema com links oficiais diretos.
* 🤖 **[AGENT.md](AGENT.md):** Diretrizes mestras para agentes autônomos, padrões de CommonMark e protocolo de Pull Requests.
* 📊 **[PROGRESSO.md](PROGRESSO.md):** Quadro comparativo item a item das metas definidas em `scripts/plano.py`.
* 📝 **[WORKLOG.md](WORKLOG.md):** Registro cronológico auditável de coletas, saneamentos de links e execuções de auditoria.

---

## 🏛️ Estrutura de Pastas do Repositório

```
tributos/
├── wiki/                            # 📚 Wiki estruturada com guias de todos os 9 pilares
├── federal/                         # Sistema Tributário Nacional e normas federais
│   ├── constituicao/                # CF/88 (arts. 145 a 162 + EC 132/2023 - Reforma Tributária)
│   ├── decretos-leis/               # Dec-Lei 57/66 (IPTU/ITR), Dec-Lei 37/66 (II/Aduana), DL 1598/77
│   ├── leis-complementares/         # CTN, LC 87/96 (Kandir), LC 116/03, LC 123/06, LC 190/22, LC 192/22
│   ├── leis-ordinarias/             # IRPJ/CSLL, PIS/COFINS, IPI, CPRB, CIDE, ITR, Transação
│   ├── resolucoes-senado/           # Resolução do Senado nº 9/1992 (Teto ITCMD 8%)
│   └── regulamentos/                # RIR/2018 (39k linhas), RIPI/2010, Aduana, RPS Previdenciário, PAF, IOF
├── reforma-tributaria/              # 🚀 Novo Sistema Tributário sobre o Consumo
│   ├── split-payment/               # Arquitetura e Modelo Operacional do Split Payment Inteligente
│   ├── plp-68-2024.md               # Lei Geral do IBS, CBS e Imposto Seletivo
│   └── plp-108-2024.md              # Comitê Gestor do IBS e Contencioso Administrativo
├── reguladores/                     # Órgãos normativos fiscais e regulatórios
│   ├── rfb/                         # Receita Federal (INs 1700, 2110, 2121, ADIs, Portarias, SC COSIT)
│   ├── carf/                        # Súmulas e Acórdãos paradigmas do CARF
│   ├── pgfn/                        # Pareceres Vinculantes PGFN e Portarias Conjuntas
│   ├── confaz/                      # Convênios ICMS 142/18, 199/22, 15/23 e Ajustes SINIEF
│   └── cgsn/                        # Resoluções do Simples Nacional
├── contabil/                        # Normas Contábeis e Financeiras
│   ├── cpc/                         # Pronunciamentos Técnicos CPC 00 a 48 (extraídos via PDFKit Swift)
│   └── cfc/                         # Normas Brasileiras de Contabilidade (NBC TG)
├── estaduais/                       # Legislação dos 26 Estados e DF (RICMS SP, RJ, MG)
├── municipais/                      # Direito Tributário Municipal (CTM e RISS)
├── .agents/                         # Definições dos agentes autônomos setoriais
└── scripts/                         # Código de ingestão, rotina periódica de 2h, parsing e auditoria
```

---

## 🤖 Arquitetura Multiagente Especialista

A operação de coleta, higienização, estruturação e versionamento é dividida entre agentes autônomos:

| Agente | Tipo | Responsabilidade Técnica |
| :--- | :---: | :--- |
| **`tributos_dividendos`** | Domínio | IRPJ, Lucro Real/Presumido, JCP, RIR/2018, Offshores e Subvenções. |
| **`tributos_folha`** | Domínio | INSS Patronal, RAT/FAP, CPRB (Lei 14.973/24), Sistema S, FGTS. |
| **`tributos_produtos`** | Domínio | ICMS, DIFAL, ICMS-ST (Convênio 142/18), IPI, TIPI e PIS/Cofins Monofásicos. |
| **`tributos_servicos`** | Domínio | ISSQN municipal (LC 116/03), Retenções CSRF (4,65%), IRRF e INSS. |
| **`tributos_patrimonio`** | Domínio | ITCMD (Res. Senado 9/92), IPVA, ITR (Lei 9.393/96) e IPTU/ITBI. |
| **`tributos_combustiveis`** | Domínio | CIDE-Combustíveis, ICMS monofásico *ad rem* (LC 192/22) e Convênios. |
| **`tributos_financeiro`** | Domínio | IOF (Dec. 6.306/07), Câmbio, Criptoativos (IN 1.888/19) e Fundos. |
| **`tributos_reforma`** | Domínio | EC 132/23, PLP 68/24, PLP 108/24, Split Payment e Comitê Gestor. |
| **`tax_api_collector`** | Operacional | Mineração massiva multianual das APIs Sijut/RFB e LexML/Senado. |
| **`tax_web_scraper`** | Operacional | Extração de portais sem API (CONFAZ, CPC, CFC/NBC TG). |
| **`tax_doc_structurer`** | Operacional | Conversão para CommonMark estrito e frontmatter canônico. |
| **`tax_link_auditor`** | Auditoria | Saneamento de URLs oficiais apontando para o SPA visual da RFB. |
| **`tax_auditor`** | Auditoria | Validação cruzada com checagem ativa de rede (`--rede`). |
| **`tax_git_workflow`** | Versionamento | Commits atômicos, gerenciamento de branches e abertura de PRs. |

---

## ⏱️ Rotina Periódica Local (a cada 2 horas)
O repositório possui uma rotina automatizada agendada internamente no Antigravity (`task-606`, cron `0 */2 * * *` com `isDaemon: true`).
A cada 2 horas, o script [`scripts/rotina_ciclica_2h.py`](scripts/rotina_ciclica_2h.py) é executado na máquina local:
1. Avança a paginação nas APIs oficiais da Receita Federal e LexML em todos os pilares;
2. Higieniza links diretos com `tax_link_auditor`;
3. Valida a integridade dos schemas e respostas de rede com `tax_auditor --rede`;
4. Atualiza `ACERVO.md`, `PROGRESSO.md` e `WORKLOG.md`;
5. Cria branch temática com timestamp e abre Pull Request no GitHub.

---

## 📄 Licença
Dados públicos e textos de leis são de domínio público, nos termos da Lei nº 9.610/1998 (Lei de Direitos Autorais, art. 8º, IV).
Os scripts de automação, parsing e ferramentas de auditoria estão sob a licença MIT.
