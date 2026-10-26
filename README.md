# Legislação Tributária e Normas Contábeis Brasileiras em Markdown

Um acervo de alta fidelidade contendo as normas do **Direito Tributário, Legislação Fiscal e Normas Contábeis Brasileiras**, convertidas de fontes oficiais para **Markdown estruturado** com cabeçalho YAML canônico.

Inspirado na arquitetura e no rigor de engenharia de dados do [`ctresb/leis`](https://github.com/ctresb/leis), este repositório possui foco exclusivo no ecossistema fiscal, contábil e tributário nacional.

## Documentação e Governança

* 📖 **[ACERVO.md](ACERVO.md):** Catálogo geral detalhado de todos os documentos já coletados e indexados, agrupados por pilar com links diretos oficiais.
* 🤖 **[AGENT.md](AGENT.md):** Diretrizes mestras para agentes autônomos, padrões de CommonMark, políticas de URLs diretas e protocolo obrigatório de Pull Requests.
* 📊 **[PROGRESSO.md](PROGRESSO.md):** Quadro de medição item a item das metas definidas em `scripts/plano.py`.
* 📝 **[WORKLOG.md](WORKLOG.md):** Registro cronológico auditável de todas as execuções, coletas e auditorias de rede.

---

## Estrutura do Acervo

```
tributos/
├── federal/                         # Sistema Tributário Nacional e normas federais
│   ├── constituicao/                # CF/88 (arts. 145 a 162 + EC 132/2023 - Reforma Tributária)
│   ├── leis-complementares/         # CTN (Lei 5.172/66), LC 87/96 (Kandir), LC 116/03, LC 123/06
│   ├── leis-ordinarias/             # IRPJ/CSLL, PIS/COFINS, IPI, IOF, CIDE
│   └── regulamentos/                # RIR/2018, RIPI/2010, Regulamento Aduaneiro, RPS
├── reguladores/                     # Órgãos normativos fiscais e regulatórios
│   ├── rfb/                         # Receita Federal (INs, Portarias, Soluções de Consulta COSIT/DISIT)
│   ├── carf/                        # Súmulas e Acórdãos paradigmas do CARF
│   ├── pgfn/                        # Pareceres Vinculantes PGFN e Portarias de Transação
│   ├── confaz/                      # Convênios ICMS, Protocolos ICMS e Ajustes SINIEF
│   └── cgsn/                        # Resoluções do Simples Nacional
├── contabil/                        # Normas Contábeis e Financeiras
│   ├── cfc/                         # Normas Brasileiras de Contabilidade (NBC TG, TSP, PG, PA, PP)
│   ├── cpc/                         # Pronunciamentos Técnicos CPC (00 a 50+), OCPC e ICPC
│   └── cvm/                         # Resoluções Contábeis da CVM para companhias abertas
├── estaduais/                       # Legislação dos 26 Estados e DF
│   └── UF/                          # RICMS, Leis de IPVA e ITCMD, Resoluções SEFAZ
├── municipais/                      # Direito Tributário Municipal
│   └── UF/municipio/                # Códigos Tributários Municipais (CTM) e Regulamentos do ISS (RISS)
├── tratados/                        # Tributação Internacional
│   ├── bitributacao/                # Acordos para Evitar a Dupla Tributação Internacional
│   └── precos-de-transferencia/     # Preços de Transferência (Lei 14.596/23 e normativos)
├── jurisprudencia/                  # Precedentes Fiscais Vinculantes
│   ├── stf/                         # Súmulas Vinculantes e Repercussão Geral tributárias
│   └── stj/                         # Súmulas e Recursos Especiais Repetitivos (1ª Seção)
└── scripts/                         # Código de ingestão, parsing, auditoria e agentes
    └── agentes/                     # Agentes especialistas automatizados
```

---

## Arquitetura Multiagente Especialista

A operação de coleta, higienização, estruturação e versionamento é dividida em **4 agentes especializados**:

1. 🌐 **`tax-web-scraper` (`scripts/agentes/agente_scraping.py`):**
   * Coleta páginas e acervos de portais que não possuem API REST estruturada (CONFAZ, CFC, CPC, SEFAZ estaduais e diários municipais).
   * Lida com paginação, rate-limiting, retentativas e cache comprimido local em `_fonte/scraping/`.

2. 🔌 **`tax-api-collector` (`scripts/agentes/agente_api.py`):**
   * Integra diretamente com APIs oficiais estruturadas de dados abertos (API da Receita Federal Sijut, dados abertos do Senado/Câmara `normas.leg.br`, etc.).
   * Extrai metadados completos de autoria, ementa, situação de vigência e links originais.

3. 📝 **`tax-doc-structurer` (`scripts/agentes/agente_estruturador.py`):**
   * Converte HTML e PDFs em **CommonMark rigoroso**.
   * Gera frontmatter YAML com metadados fiscais (tributos afetados, número, ano, data, órgão emissor, situação).
   * Preserva a hierarquia formal do Direito (Artigos, Parágrafos, Incisos, Alíneas) e tabelas de alíquotas.

4. 🐙 **`tax-git-workflow` (`scripts/agentes/agente_git.py`):**
   * Cria commits semânticos por norma com data histórica e signatário autêntico.
   * Gerencia branches temáticos, criação de Pull Requests e Issues via `gh` CLI.
   * Mantém atualizados o `PROGRESSO.md` e o `WORKLOG.md`.

---

## Formato Padrão dos Documentos

Todo documento do acervo contém metadados YAML canônicos:

```markdown
---
titulo: "Instrução Normativa RFB nº 2.121, de 15 de dezembro de 2022"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil"
tipo: "Instrução Normativa"
numero: "2121"
data: 2022-12-15
ano: "2022"
tributos_afetados: ["PIS/Pasep", "Cofins"]
situacao: "Em vigor"
revogada: false
fonte: "https://normas.receita.fazenda.gov.br"
ementa: "Consolida as normas sobre a apuração, a cobrança, a fiscalização, a arrecadação e a administração da Contribuição para o PIS/Pasep e da Cofins."
---

# Instrução Normativa RFB nº 2.121, de 15 de dezembro de 2022

Texto da norma em Markdown limpo...
```

---

## Como Executar

### 1. Requisitos
* Python 3.9+
* Git instalado e configurado
* GitHub CLI (`gh`) autenticado para abertura automática de PRs e Issues

### 2. Rodar a Auditoria e Medição de Progresso
```bash
# Auditar formatação e frontmatter de todos os documentos
python3 scripts/auditar.py

# Recalcular métricas de cobertura contra o scripts/plano.py
python3 scripts/progresso.py
```

### 3. Executar o Ciclo Multiagente
```bash
# Roda a esteira completa com os 4 agentes para um lote de teste
python3 scripts/orquestrador.py --ano 2024 --limite 5
```

---

## Licença

Os textos das normas jurídicas e atos administrativos são de domínio público (art. 8º, I, da Lei Federal nº 9.610/1998). Os scripts e pipelines deste repositório estão licenciados sob a **MIT License**.
