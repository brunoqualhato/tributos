---
titulo: "Portaria Conjunta MTE / RFB nº 33, de 28 de dezembro de 2023"
esfera: "Federal"
orgao: "Ministério do Trabalho e Emprego / Secretaria Especial da Receita Federal do Brasil"
tipo: "Portaria Conjunta"
numero: "33"
data: "2023-12-28"
ano: "2023"
tema_tributario: "Folha de Pagamento e Encargos"
tributos_afetados: ["eSocial", "FGTS Digital", "DCTFWeb"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.gov.br/trabalho-e-emprego/pt-br"
ementa: "Estabelece o cronograma definitivo de implantação do FGTS Digital e substituição da GFIP pelo eSocial para todos os grupos de empregadores."
---

# Portaria Conjunta MTE / RFB nº 33, de 28 de dezembro de 2023 (Cronograma de Implantação do FGTS Digital e Substituição da GFIP pelo eSocial)

## Identificação Normativa

- **Tipo:** Portaria Conjunta Interinstitucional
- **Número:** 33
- **Data de Assinatura:** 28 de dezembro de 2023
- **Órgãos Emissores:** Ministério do Trabalho e Emprego (MTE) e Secretaria Especial da Receita Federal do Brasil (RFB)
- **Fonte Oficial:** [Normas RFB — Ato nº 135510](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/135510)

---

## Texto Normativo Consolidado

Estabelece o cronograma definitivo de implantação do Fundo de Garantia do Tempo de Serviço Digital (**FGTS Digital**) e disciplina a substituição da Guia de Recolhimento do FGTS e de Informações à Previdência Social (**GFIP**) pelo Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (**eSocial**) para todos os grupos de empregadores.

O MINISTRO DE ESTADO DO TRABALHO E EMPREGO e o SECRETÁRIO ESPECIAL DA RECEITA FEDERAL DO BRASIL, no uso das atribuições que lhes conferem o art. 87, parágrafo único, inciso II, da Constituição Federal, o Decreto nº 8.373, de 11 de dezembro de 2014, e os arts. 17 e 17-A da Lei nº 8.036, de 11 de maio de 1990, com a redação dada pela Lei nº 14.438, de 24 de agosto de 2022, resolvem:

### CAPÍTULO I — DO CRONOGRAMA DE OPERAÇÃO EFETIVA DO FGTS DIGITAL

**Art. 1º** O sistema **FGTS Digital**, conjunto de sistemas informatizados integrados destinados à gestão da arrecadação, cobrança, fiscalização, apuração, lançamento e prestação de informações do Fundo de Garantia do Tempo de Serviço (FGTS), entra em operação efetiva para todos os grupos de empregadores obrigados ao eSocial a partir de **1º de março de 2024** (competência março de 2024), sucedendo o período de operação limitada de testes (produção restrita / homologação) realizado entre agosto de 2023 e janeiro de 2024.

**Art. 2º** A partir da competência **março de 2024**, ficam **definitivamente substituídas**:
I - a **Guia de Recolhimento do FGTS e de Informações à Previdência Social (GFIP)**, gerada pelo Sistema Empresa de Recolhimento do FGTS e Informações à Previdência Social (**SEFIP**), pelo **eSocial**, no que se refere às informações trabalhistas e remuneratórias que constituem base de cálculo do FGTS;
II - a **Guia de Recolhimento do FGTS (GRF)** mensal e a **Guia de Recolhimento Rescisório do FGTS (GRRF)** pela **Guia do FGTS Digital (GFD)**, gerada exclusivamente no portal do FGTS Digital (`fgtsdigital.gov.br`).

### CAPÍTULO II — FLUXO DE INTEGRAÇÃO ENTRE ESOCIAL, FGTS DIGITAL E DCTFWEB

**Art. 3º** Para os fatos geradores ocorridos a partir de **1º de março de 2024**, a apuração dos valores devidos ao FGTS observará o seguinte fluxo automatizado de integração:
I - **Transmissão dos Eventos ao eSocial:** o empregador transmite ao ambiente nacional do eSocial os eventos de tabelas (`S-1010` — Tabela de Rubricas, com o código de incidência de FGTS parametrizado no campo `codIncFGTS`), os eventos não periódicos (`S-2200` — Admissão, `S-2299` — Desligamento e `S-2399` — Término de TSVE) e os eventos periódicos (`S-1200` — Remuneração de trabalhador vinculado ao RGPS);
II - **Cálculo Instantâneo pelo eSocial (Totalizador `S-5003`):** o eSocial processa as rubricas remuneratórias e retorna imediatamente ao empregador o evento totalizador **`S-5003` (Informações do FGTS por Trabalhador)** e, no fechamento da folha (`S-1299`), o evento **`S-5013` (Informações do FGTS Consolidadas por Contribuinte)**, sem necessidade de fechamento da folha para que os dados individuais alimentem o FGTS Digital;
III - **Recepção pelo FGTS Digital:** o FGTS Digital recebe em tempo real os dados dos eventos `S-5003`, calcula os encargos devidos (8% mensal, 2% aprendiz, indenização compensatória de 40% ou 20% sobre o histórico da conta vinculada) e disponibiliza a emissão da **Guia do FGTS Digital (GFD)** com código QR para pagamento exclusivo via **PIX**.

**Art. 4º** A substituição da GFIP para fins previdenciários pela **Declaração de Débitos e Créditos Tributários Federais Previdenciários e de Outras Entidades e Fundos (DCTFWeb)**, disciplinada pela Instrução Normativa RFB nº 2.005, de 29 de janeiro de 2021 (posteriormente consolidada pela IN RFB nº 2.237/2024), passa a operar de forma plena e sincronizada com a substituição da GFIP para fins de FGTS, extinguindo-se a duplicidade de declarações sobre a folha de pagamento.

### CAPÍTULO III — REGRAS DE TRANSIÇÃO PARA COMPETÊNCIAS ANTERIORES A MARÇO DE 2024

**Art. 5º** Permanece obrigatória a utilização do sistema **SEFIP/GFIP** e do **Conectividade Social (GRRF)** exclusivamente para:
I - declaração, retificação e recolhimento de débitos de FGTS mensal referentes a competências **até fevereiro de 2024 (02/2024)**; e
II - apuração e recolhimento de FGTS rescisório relativo a desligamentos cuja data de rescisão contratual tenha ocorrido **até 29 de fevereiro de 2024**.

**Art. 6º** Esta Portaria Conjunta entra em vigor na data de sua publicação.

---

## Quadro de Correlação dos Eventos do eSocial com o FGTS Digital e a DCTFWeb

| Evento do eSocial | Descrição Técnica do Evento | Sistema Destinatário e Efeito Tributário / Trabalhista |
| :--- | :--- | :--- |
| **`S-1010`** | Tabela de Rubricas da Folha de Pagamento | Parametriza a incidência de INSS (`codIncCP`), IRRF (`codIncIRRF`) e **FGTS (`codIncFGTS`)**. |
| **`S-1200`** | Remuneração de Trabalhador vinculado ao RGPS | Gera o totalizador **`S-5003`** que alimenta imediatamente a guia mensal no **FGTS Digital**. |
| **`S-2299` / `S-2399`** | Desligamento / Término de Trabalhador Sem Vínculo | Alimenta o módulo rescisório do **FGTS Digital** (multa de 40% ou 20%) e habilita o saque na CAIXA. |
| **`S-1299`** | Fechamento dos Eventos Periódicos | Gera o totalizador **`S-5013`** (FGTS Consolidado) e transmite os débitos de INSS e IRRF para a **DCTFWeb**. |
| **`S-5003`** | Informações do FGTS por Trabalhador (Retorno do eSocial) | Espelha a base de cálculo e o valor de FGTS apurado por CPF para conferência com o **FGTS Digital**. |
