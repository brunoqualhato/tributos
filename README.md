# ⚖️ Legislação Tributária e Normas Contábeis Brasileiras em Markdown

[![Auditoria de Rede](https://img.shields.io/badge/Auditoria%20de%20Integridade-100%25%20Aprovada-brightgreen.svg)](#auditoria-e-integridade)
[![Normas Catalogadas](https://img.shields.io/badge/Normas%20Catalogadas-1.241-blue.svg)](ACERVO.md)
[![Cobertura do Plano](https://img.shields.io/badge/Cobertura%20do%20Plano-100%25%20(1.241%2F1.241)-brightgreen.svg)](PROGRESSO.md)
[![Wiki Oficial](https://img.shields.io/badge/Documentação-Wiki%20dos%20Pilares-orange.svg)](wiki/Home.md)
[![Licença](https://img.shields.io/badge/Licença-Dados%20Abertos%20Oficiais-lightgrey.svg)](#licença)

Um acervo de alta fidelidade contendo as normas do **Direito Tributário, Legislação Fiscal e Normas Contábeis Brasileiras**, convertidas de fontes oficiais para **Markdown estruturado** com cabeçalho YAML canônico, auditoria independente de integridade e links de visualização direta oficial.

Inspirado na arquitetura e rigor de dados do [`ctresb/leis`](https://github.com/ctresb/leis), este repositório possui foco exclusivo no ecossistema fiscal, contábil e tributário nacional, cobrindo as 27 Unidades da Federação e as 26 Capitais Municipais (+ DF).

---

## 🧭 Os 10 Pilares do Sistema Tributário e Contábil Nacional

A base de conhecimento está organizada rigorosamente em torno dos 10 pilares estruturados em [`scripts/plano.py`](scripts/plano.py) e mapeados em [`Home.md`](Home.md):

1. 🏛️ **Legislação Estruturante & Códigos** — Código Tributário Nacional (CTN Lei 5.172/66), Simples Nacional (LC 123/06), Processo Administrativo Fiscal (Dec. 70.235/72) e Processo Administrativo Tributário (PAT/PAF) das Fazendas Estaduais (TIT/SP, CCRJ, CCMG, CCRF/PR, TAT/SC, TARF/RS, CAT/GO e CONSEF/BA).
2. 💰 **[Dividendos, JCP e Renda do Capital](wiki/Pilar-1-Dividendos-e-Renda-do-Capital.md)** — IRPJ, CSLL, Lucro Real, Presumido e Arbitrado, JCP, RIR/2018 integral (Decreto 9.580/18), Offshores e Trusts (Lei 14.754/23) e Subvenções (Lei 14.789/23).
3. 👥 **[Folha de Pagamento e Encargos Previdenciários](wiki/Pilar-2-Folha-de-Pagamento-e-Encargos.md)** — Plano de Custeio da Seguridade Social (Lei 8.212/91), RPS (Dec. 3.048/99), INSS Patronal (20%), RAT/FAP, Sistema S, CPRB (Leis 12.546/11 e 14.973/24), FGTS Digital (Lei 8.036/90), Pasep Governamental e PIS Folha.
4. 📦 **[Produtos, Mercadorias e Indústria](wiki/Pilar-3-Produtos-Mercadorias-e-ICMS.md)** — Leis Matrizes do ICMS de todas as 27 UFs, Regulamentos do ICMS (RICMS das 27 UFs), Fundos Agropecuários e de Infraestrutura Estaduais (FETHAB/MT, FUNDEINFRA/GO, FUNDERSUL/MS, FECOP/MA, FAIN/BA), Lei Kandir (LC 87/96), DIFAL (LC 190/22), Convênio ICMS-ST 142/18, IPI (RIPI/2010 e TIPI), Regimes Monofásicos de PIS/Cofins e Regulamento Aduaneiro (Dec. 6.759/09).
5. 🛠️ **[Serviços e Retenções na Fonte](wiki/Pilar-4-Servicos-e-Retencoes.md)** — ISSQN geral (LC 116/03, LC 157/16, LC 175/20), Códigos Tributários Municipais (CTM) e Regulamentos do ISS de todas as 26 Capitais Estaduais e DF, Retenções Federais na Fonte (CSRF 4,65% - Lei 10.833/03; IRRF 1,5% e INSS 11%).
6. 🏰 **[Patrimônio, Herança e Veículos](wiki/Pilar-5-Patrimonio-Heranca-e-Veiculos.md)** — Leis Estaduais do ITCMD de todas as 27 UFs (Res. Senado 9/92), Leis Estaduais do IPVA de todas as 27 UFs, ITR Federal (Lei 9.393/96 e Dec. 4.382/02), ITBI e IPTU municipais.
7. ⛽ **[Combustíveis e Energia](wiki/Pilar-6-Combustiveis-e-Energia.md)** — CIDE-Combustíveis (Lei 10.336/01 e Dec. 5.060/04), Lei do Petróleo (Lei 9.478/97), Regime Monofásico *ad rem* de ICMS (LC 192/22, Convênios 199/22 e 15/23), RenovaBio, Combustíveis do Futuro (Lei 14.993/24) e Mercado de Carbono (Lei 15.042/24).
8. 📈 **[Tributação Financeira e IOF](wiki/Pilar-7-Tributacao-Financeira-e-IOF.md)** — Regulamento do IOF (RIOF Dec. 6.306/07), Leis Matrizes 5.143/66 e 8.894/94, Cronograma de redução do IOF-Câmbio (Portaria MF 204/22), Renda Fixa, Renda Variável, Derivativos e Criptoativos (IN RFB 1.888/19).
9. 🚀 **[Reforma Tributária e Transição](wiki/Pilar-8-Reforma-Tributaria-e-Split-Payment.md)** — Emenda Constitucional nº 132/2023, LC 214/2025 (Lei Geral do IBS, CBS e Imposto Seletivo), LC 227/2026 (Comitê Gestor do IBS e Contencioso), Split Payment Operacional, Nota Técnica NFS-e Nacional IBS/CBS e Publicações Oficiais (TCU, RFB e ANA).
10. 📊 **[Normas Contábeis, CARF e Jurisprudência](wiki/Pilar-9-Normas-Contabeis-CPC-e-CFC.md)** — Pronunciamentos Técnicos CPC (CPC 00 a 48, ICPC e OCPC), Normas Brasileiras de Contabilidade do CFC (NBC TG 01 a 48, 1000, CTG, ITG), Precedentes Vinculantes do STF e STJ (Súmulas Vinculantes, Temas de Repercussão Geral e Recursos Repetitivos) e Súmulas Vinculantes do CARF.

---

## 📑 Governança e Catálogo Geral

* 📖 **[ACERVO.md](ACERVO.md):** Catálogo geral detalhado de todos os **1.241 documentos catalogados e auditados**, agrupados por tema com metadados e links oficiais diretos.
* 🤖 **[AGENT.md](AGENT.md):** Diretrizes mestras para agentes autônomos, taxonomia, padrões de CommonMark e protocolo de Pull Requests.
* 📊 **[PROGRESSO.md](PROGRESSO.md):** Quadro comparativo item a item das metas definidas em `scripts/plano.py` (**100,0% de cobertura nos 10 pilares**).
* 📝 **[WORKLOG.md](WORKLOG.md):** Registro cronológico auditável de coletas, saneamentos de links e execuções de auditoria.
* 🧭 **[Home.md](Home.md):** Painel central de navegação no formato Obsidian MOC (Map of Content).

---

## 🏛️ Estrutura de Pastas do Repositório

```
tributos/
├── Home.md                          # 🧭 Dashboard central e MOCs de navegação
├── ACERVO.md                        # 📖 Catálogo geral dos 1.241 documentos
├── PROGRESSO.md                     # 📊 Relatório de metas e cobertura do plano
├── AGENT.md                         # 🤖 Protocolo e governança de agentes
├── WORKLOG.md                       # 📝 Histórico cronológico auditável
├── wiki/                            # 📚 Wiki estruturada com guias temáticos
├── federal/                         # Sistema Tributário Nacional e normas federais
│   ├── constituicao/                # CF/88 (arts. 145 a 162 + EC 132/2023)
│   ├── decretos-leis/               # Dec-Lei 57/66 (IPTU/ITR), DL 288/67 (ZFM), DL 1598/77
│   ├── leis-complementares/         # CTN, LC 87/96 (Kandir), LC 116/03, LC 123/06, LC 190/22, LC 192/22
│   ├── leis-ordinarias/             # IRPJ/CSLL, PIS/COFINS, IPI, CPRB, CIDE, ITR, Transação, Combustíveis
│   ├── resolucoes-senado/           # Resoluções do Senado nº 9/92 (ITCMD), 22/89, 95/96 e 13/12 (ICMS)
│   └── regulamentos/                # RIR/2018, RIPI/2010, Aduana, RPS Previdenciário, PAF, IOF
├── reforma-tributaria/              # 🚀 Novo Sistema Tributário sobre o Consumo (IBS/CBS/IS)
│   ├── split-payment/               # Modelo Operacional e Nota Técnica do Split Payment
│   ├── cbs-receita-federal/         # Portarias e Nota Técnica NFS-e Nacional IBS/CBS
│   ├── publicacoes/                 # Publicações institucionais (TCU, RFB, ANA)
│   ├── emenda-constitucional-132-2023.md
│   ├── lei-complementar-214-2025.md # Lei Geral do IBS, CBS e Imposto Seletivo
│   └── lei-complementar-227-2026.md # Comitê Gestor e Processo Administrativo IBS
├── estaduais/                       # 🌐 Legislação das 27 Unidades da Federação (26 Estados + DF)
│   ├── <uf>/leis/icms/              # Leis Orgânicas e Matrizes do ICMS das 27 UFs
│   ├── <uf>/leis/itcmd/             # Leis Estaduais do ITCMD das 27 UFs
│   ├── <uf>/leis/ipva/              # Leis Estaduais do IPVA das 27 UFs
│   ├── <uf>/leis/pat/               # Processo Administrativo Tributário (Tribunais de Fazenda)
│   ├── <uf>/leis/fundos/            # Fundos do Agronegócio (FETHAB, FUNDEINFRA, FUNDERSUL, etc.)
│   ├── <uf>/ricms/                  # Regulamentos do ICMS (RICMS) das 27 UFs
│   └── confaz/                      # Convênios ICMS 142/18 (ICMS-ST), 109/24, 199/22 e Ajustes SINIEF
├── municipais/                      # 🏙️ Legislação Municipal (26 Capitais Estaduais + DF)
│   ├── <uf>/servicos-iss/           # Códigos Tributários Municipais (CTM) e Regulamentos do ISS
│   └── <uf>/leis/                   # IPTU e ITBI das principais capitais
├── jurisprudencia/                  # ⚖️ Precedentes Vinculantes e Jurisprudência Pacífica
│   └── precedentes-vinculantes/     # STF (Súmulas Vinculantes e Temas RG) e STJ (Recursos Repetitivos)
├── reguladores/                     # Órgãos reguladores fiscais e contencioso administrativo
│   ├── rfb/                         # Receita Federal (INs gerais, financeiro, outros atos e SC COSIT)
│   ├── carf/sumulas/                # Súmulas Vinculantes e Enunciados Pacíficos do CARF
│   └── anp/                         # Resoluções da Agência Nacional do Petróleo
├── contabil/                        # 📊 Normas Contábeis Oficiais
│   ├── cpc/                         # Pronunciamentos CPC 00 a 48, ICPC e OCPC
│   └── cfc/                         # Normas Brasileiras de Contabilidade NBC TG (CFC)
├── obsidian/                        # 🧠 Mapas de Conteúdo (MOCs) e Canvas Interativo do Sistema
├── _auditoria/                      # 🛡️ Relatórios de conformidade de schema, integridade e hashes
└── scripts/                         # Código de auditoria, catálogo, progresso e esteira de automação
```

---

## 🤖 Arquitetura Multiagente Especialista

A operação de coleta, higienização, estruturação e versionamento é dividida entre agentes autônomos:

| Agente | Tipo | Responsabilidade Técnica |
| :--- | :---: | :--- |
| **`tributos_dividendos`** | Domínio | IRPJ, CSLL, Lucro Real/Presumido, JCP, RIR/2018, Offshores e Subvenções. |
| **`tributos_folha`** | Domínio | INSS Patronal, RAT/FAP, CPRB (Lei 14.973/24), Sistema S, FGTS e Pasep. |
| **`tributos_produtos`** | Domínio | ICMS 27 UFs, DIFAL, CONFAZ (ICMS-ST), IPI, TIPI e PIS/Cofins Monofásicos. |
| **`tributos_servicos`** | Domínio | ISSQN municipal (26 capitais + DF), Retenções CSRF (4,65%), IRRF e INSS. |
| **`tributos_patrimonio`** | Domínio | ITCMD 27 UFs (Res. Senado 9/92), IPVA 27 UFs, ITR (Lei 9.393/96) e IPTU/ITBI. |
| **`tributos_combustiveis_energia`** | Domínio | CIDE-Combustíveis, ICMS monofásico *ad rem* (LC 192/22), Petróleo e Carbono. |
| **`tributos_financeiro`** | Domínio | IOF (Dec. 6.306/07), Câmbio, Criptoativos (IN 1.888/19) e Renda Fixa/Variável. |
| **`tributos_reforma_transicao`** | Domínio | EC 132/23, LC 214/25, LC 227/26, Split Payment e Comitê Gestor IBS/CBS. |
| **`tax_api_collector`** | Operacional | Mineração massiva das APIs oficiais Sijut/RFB, LexML, Câmara e Senado. |
| **`tax_web_scraper`** | Operacional | Extração de portais sem API (CONFAZ, CPC, CFC/NBC TG, SEFAZ). |
| **`tax_doc_structurer`** | Operacional | Conversão para CommonMark estrito e frontmatter YAML canônico. |
| **`tax_link_auditor`** | Auditoria | Saneamento e validação de URLs oficiais de visualização direta. |
| **`tax_auditor`** | Auditoria | Validação cruzada de conformidade de schema e teste ativo de rede (`--rede`). |
| **`tax_git_workflow`** | Versionamento | Commits atômicos, gerenciamento de branches e abertura de PRs via GitHub CLI. |

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
