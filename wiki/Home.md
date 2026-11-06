# 📚 Wiki do Acervo Tributário e Contábil Brasileiro

Bem-vindo à Wiki oficial do repositório **Tributos** — a base aberta, hiperestruturada e canônica da legislação tributária, fiscal e contábil brasileira, com auditoria automatizada e links de visualização direta oficial (**1.303 normas catalogadas e auditadas nos 10 pilares**).

## 🗺️ Mapa de Navegação da Wiki

### Os 10 Pilares do Sistema Tributário Nacional

| Pilar | Tema Central | Principais Tributos / Normas | Guia da Wiki |
| :---: | :--- | :--- | :--- |
| **01** | **Dividendos e Renda do Capital** | IRPJ, CSLL, IRPF, JCP, RIR/2018, Offshores, Pilar 2 OCDE | [Ver Guia](Pilar-1-Dividendos-e-Renda-do-Capital.md) |
| **02** | **Folha de Pagamento e Encargos** | INSS Patronal, RAT/FAP, Sistema S, CPRB, FGTS Digital, Pasep | [Ver Guia](Pilar-2-Folha-de-Pagamento-e-Encargos.md) |
| **03** | **Produtos, Mercadorias e Indústria** | ICMS 27 UFs, Fundos Agro (Art. 136 ADCT), DIFAL, IPI, Monofásicos | [Ver Guia](Pilar-3-Produtos-Mercadorias-e-ICMS.md) |
| **04** | **Serviços e Retenções na Fonte** | ISSQN das 26 Capitais + DF, Retenções CSRF, IRRF e INSS | [Ver Guia](Pilar-4-Servicos-e-Retencoes.md) |
| **05** | **Patrimônio, Herança e Veículos** | ITCMD 27 UFs, IPVA 27 UFs, ITR, IPTU, ITBI | [Ver Guia](Pilar-5-Patrimonio-Heranca-e-Veiculos.md) |
| **06** | **Combustíveis e Energia** | CIDE, ICMS Monofásico *ad rem*, RenovaBio e Mercado de Carbono | [Ver Guia](Pilar-6-Combustiveis-e-Energia.md) |
| **07** | **Tributação Financeira e Câmbio** | IOF Crédito/Câmbio/Seguro/Títulos, RIOF, Criptoativos | [Ver Guia](Pilar-7-Tributacao-Financeira-e-IOF.md) |
| **08** | **Reforma Tributária & Split Payment** | EC 132/23, LC 214/25 (IBS/CBS/IS), LC 227/26 (CG-IBS), Split Payment | [Ver Guia](Pilar-8-Reforma-Tributaria-e-Split-Payment.md) |
| **09** | **Normas Contábeis (CPC e CFC)** | Pronunciamentos CPC 00 a 48, NBC TG, ICPC, OCPC, CTG e ITG | [Ver Guia](Pilar-9-Normas-Contabeis-CPC-e-CFC.md) |
| **10** | **Precedentes Vinculantes e Processo** | Súmulas Vinculantes STF, Repetitivos STJ, Súmulas CARF e PAT Estadual | [Ver Guia](Pilar-10-Jurisprudencia-Vinculante-e-Processo-Fiscal.md) |

## ⚙️ Arquitetura, Governança e Automação
- [Arquitetura dos Agentes, Auditoria e Rotina Periódica Local](Arquitetura-dos-Agentes-e-Automacao.md)
- [Catálogo Completo das 1.303 Normas Catalogadas (`ACERVO.md`)](../ACERVO.md)
- [Quadro de Metas e Cobertura dos 10 Pilares (`PROGRESSO.md`)](../PROGRESSO.md)
- [Manual de Governança dos Agentes (`AGENT.md`)](../AGENT.md)

## 🏛️ Diretrizes de Qualidade dos Documentos
1. **CommonMark Puro:** Zero tags HTML residuais (`table`, `div`, `span`).
2. **Frontmatter YAML Canônico:** Todo documento possui metadados com título, órgão, número, ano, data, situação, tema tributário e tributos afetados.
3. **Links Oficiais Diretos:** 100% dos links da Receita Federal apontam para o SPA visual direto (`https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{idAto}`) e Leis Federais apontam para o LexML (`https://normas.leg.br/?urn={URN}`).
