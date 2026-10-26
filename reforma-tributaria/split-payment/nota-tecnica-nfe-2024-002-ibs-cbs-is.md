---
titulo: "Nota Técnica Conjunta ENCAT / RFB nº 2024.002 (Reforma Tributária do Consumo na NF-e e NFC-e: Leiautes XML de IBS Estadual/Municipal, CBS e Imposto Seletivo)"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil / ENCAT - CONFAZ"
tipo: "Nota Técnica Conjunta"
numero: "2024.002"
data: "2024-08-01"
ano: "2024"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS", "Imposto Seletivo", "Split Payment"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY="
ementa: "Estabelece as especificações técnicas e os novos grupos de campos XML da Nota Fiscal Eletrônica (NF-e, modelo 55) e da Nota Fiscal de Consumidor Eletrônica (NFC-e, modelo 65) para apuração do Imposto sobre Bens e Serviços (IBS Estadual e Municipal), da Contribuição sobre Bens e Serviços (CBS) e do Imposto Seletivo (IS) a partir de 2026."
---



# Nota Técnica Conjunta ENCAT / RFB nº 2024.002 (Reforma Tributária do Consumo na NF-e e NFC-e: Leiautes XML de IBS Estadual/Municipal, CBS e Imposto Seletivo)

## 1. Visão Geral e Mudança de Paradigma Estrutural

A **Nota Técnica Conjunta ENCAT / Receita Federal do Brasil nº 2024.002** define as alterações no leiaute dos Documentos Fiscais Eletrônicos — especificamente a **Nota Fiscal Eletrônica (NF-e, modelo 55)** e a **Nota Fiscal de Consumidor Eletrônica (NFC-e, modelo 65)** — para viabilizar a recepção, cálculo e auditoria dos tributos instituídos pela Emenda Constitucional nº 132/2023 e pela Lei Complementar nº 214/2025.

### 1.1. Pilares Arquiteturais na Emissão do DF-e
1. **Tributação 100% no Destino:** A alíquota do IBS passa a ser exclusivamente a soma da alíquota da UF de destino (`pIBSUF`) com a alíquota do Município de destino (`pIBSMun`), extinguindo-se a cobrança de alíquotas interestaduais na origem;
2. **Cálculo Estritamente "Por Fora":** O IBS e a CBS não compõem a própria base de cálculo, incidindo estritamente sobre o valor da operação acrescido do Imposto Seletivo;
3. **Convivência Transitória dos Modelos (2026 a 2032):** Durante a transição, a nota fiscal eletrônica transportará simultaneamente os grupos tributários legados (`<ICMS>`, `<IPI>`, `<PIS>`, `<COFINS>`) e os novos grupos da Reforma (`<IBSCBS>`, `<IS>`).

---

## 2. Novos Grupos e Tags XML da Estrutura `<det>` / `<imposto>`

### 2.1. Grupo `<IS>` — Imposto Seletivo (Monofásico Federal)
* `<CSTIS>`: Código de Situação Tributária do Imposto Seletivo;
* `<cClassTribIS>`: Código de Classificação Tributária do IS (enquadramento nos anexos da lei);
* `<vBCIS>`: Base de cálculo do IS;
* `<pIS>`: Alíquota *ad valorem* percentual;
* `<qUnidIS>` e `<vAliqIS>`: Quantidade tributável e alíquota específica *ad rem* (para combustíveis, bebidas e tabaco);
* `<vIS>`: Montante calculado do Imposto Seletivo (que integrará a base de cálculo de IBS e CBS).

### 2.2. Grupo `<IBSCBS>` — Imposto sobre Bens e Serviços e Contribuição sobre Bens e Serviços
* `<CST>`: Código de Situação Tributária unificado nacional do IBS e da CBS;
* `<cClassTrib>`: Código de Classificação Tributária nacional vinculando a mercadoria ou serviço ao tratamento jurídico específico da LC 214/2025;
* `<vBC>`: Base de cálculo unificada comum;
* **Subgrupo `<gIBSUF>` (Parcela Estadual do Destino):**
  - `<pIBSUF>`: Alíquota estadual de referência;
  - `<pRedAliqUF>`: Percentual de redução (60% ou 30%);
  - `<vIBSUF>`: Valor do IBS devido ao Estado;
* **Subgrupo `<gIBSMun>` (Parcela Municipal do Destino):**
  - `<pIBSMun>`: Alíquota municipal de referência;
  - `<pRedAliqMun>`: Percentual de redução municipal;
  - `<vIBSMun>`: Valor do IBS devido ao Município;
* **Subgrupo `<gCBS>` (Parcela Federal):**
  - `<pCBS>`: Alíquota federal da CBS;
  - `<pRedAliqCBS>`: Percentual de redução da CBS;
  - `<vCBS>`: Valor da CBS devida à União.

---

## 3. Tabela Canônica de CST do Novo IVA Dual

| Código CST | Descrição da Situação Tributária | Aplicação Operacional |
| :---: | :--- | :--- |
| **01** | Tributação Integral | Operações comuns submetidas à alíquota cheia padrão de referência. |
| **02** | Alíquota Reduzida em 60% | Saúde, educação, medicamentos essenciais, produtos agropecuários in natura. |
| **03** | Alíquota Reduzida em 30% | Serviços de profissões intelectuais regulamentadas com conselho de classe. |
| **04** | Alíquota Zero (Cesta Básica Nacional) | Itens da alimentação básica e produtos prioritários com manutenção de crédito. |
| **05** | Imunidade Constitucional | Exportações de bens/serviços, templos religiosos, livros e periódicos. |
| **06** | Suspensão | Remessas industriais para industrialização, entreposto aduaneiro e ZFM. |
| **07** | Diferimento | Operações com transferência diferida da responsabilidade tributária. |
| **08** | Regime Específico Monofásico | Combustíveis, lubrificantes e energia elétrica. |
| **09** | Regime Específico de Margem | Serviços financeiros, bancos, seguradoras e intermediação. |

---

## 4. Regras de Validação e Cronograma de Homologação

1. **Ambiente de Homologação (Testes Integrados):** Disponibilizado pelas SEFAZ autorizadoras a partir do segundo semestre de 2025 para integração de sistemas de ERP e softwares emissores;
2. **Ambiente de Produção (Vigência Obrigatória):** Janeiro de 2026, com aplicação inicial das alíquotas de teste de 0,9% (CBS) e 0,1% (IBS);
3. **Interoperabilidade com Split Payment:** Geração automática da chave de amarração financeira no QR-Code da NF-e e NFC-e.

