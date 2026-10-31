---
titulo: "Portaria Conjunta RFB / MPS / MTE nº 44, de 11 de agosto de 2023 (Leiautes do eSocial e Substituição da DIRF)"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil / Ministério do Trabalho e Emprego"
tipo: "Portaria Conjunta"
numero: "44 (eSocial)"
data: "2023-08-11"
ano: "2023"
tema_tributario: "Folha de Pagamento e Encargos"
tributos_afetados: ["INSS Patronal", "IRRF", "FGTS"]
situacao: "Em vigor"
revogada: false
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/132906"
ementa: "Aprova a versão S-1.2 do leiaute do Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (eSocial), integrando a escrituração do IRRF sobre rendimentos do trabalho à DCTFWeb."
---

# Portaria Conjunta RFB / MPS / MTE nº 44, de 11 de agosto de 2023 (Leiautes do eSocial S-1.2, IRRF na DCTFWeb e Substituição da DIRF)

**PORTARIA CONJUNTA RFB/MPS/MTE Nº 44, DE 11 DE AGOSTO DE 2023**

Aprova a versão S-1.2 do leiaute do Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (**eSocial**).

O SECRETÁRIO ESPECIAL DA RECEITA FEDERAL DO BRASIL, o SECRETÁRIO DE REGIME GERAL DE PREVIDÊNCIA SOCIAL DO MINISTÉRIO DA PREVIDÊNCIA SOCIAL e o SECRETÁRIO DE INSPEÇÃO DO TRABALHO DO MINISTÉRIO DO TRABALHO E EMPREGO, no uso das atribuições que lhes conferem o Decreto nº 8.373, de 11 de dezembro de 2014, e a Portaria Interministerial MTP/ME nº 3, de 15 de março de 2022, resolvem:

## CAPÍTULO I — APROVAÇÃO DA VERSÃO S-1.2 DO LEIAUTE DO ESOCIAL

**Art. 1º** Fica aprovada a **versão S-1.2** do leiaute do Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (**eSocial**), disponível no Portal do eSocial no endereço eletrônico `https://www.gov.br/esocial`, estruturando os eventos periódicos e não periódicos para:
I - a apuração e confissão automatizada do **Imposto sobre a Renda Retido na Fonte (IRRF)** incidente sobre os rendimentos do trabalho assalariado e não assalariado diretamente na **DCTFWeb** (em cumprimento à Instrução Normativa RFB nº 2.005/2021, alterada pela IN RFB nº 2.137/2023, para fatos geradores ocorridos a partir de maio de 2023);
II - a prestação das informações anuais e mensais necessárias à **substituição da Declaração do Imposto sobre a Renda Retido na Fonte (DIRF)** e ao pré-preenchimento da Declaração de Ajuste Anual do IRPF (DAA) pelo binômio **eSocial + EFD-Reinf**; e
III - a integração estrutural das bases de cálculo remuneratórias e rescisórias com o sistema **FGTS Digital** e com a escrituração de Reclamatórias Trabalhistas (Série `S-2500` e `S-2501`).

## CAPÍTULO II — ESTRUTURA TÉCNICA DOS EVENTOS PARA APURAÇÃO DO IRRF E SUBSTITUIÇÃO DA DIRF

**Art. 2º** Na versão S-1.2 (e atualizações evolutivas S-1.3), a escrituração dos rendimentos do trabalho e das respectivas deduções e retenções de IRRF observa a seguinte arquitetura de eventos:

I - **Evento `S-1200` (Remuneração de Trabalhador vinculado ao RGPS), `S-1202` (RPPS) e `S-1207` (Benefícios de Entes Públicos):**
a) registram a competência de apuração dos rendimentos pelo **regime de competência** (folha de pagamento) e detalham no grupo `infoIRComplem` as informações complementares para fins de DIRF e DAA:
- Identificação dos **dependentes** de IRRF (`cpfDep`, `tpDep`, `depIRRF`);
- Deduções de **pensão alimentícia** descontada em folha por beneficiário (`penAlim`, com CPF do alimentando e valor deduzido);
- Deduções de **previdência complementar** (`previdCompl`: PGBL, FAPI, Funpresp e entidades fechadas de previdência complementar, identificadas pelo CNPJ da entidade);
- Descontos de **planos privados de assistência à saúde** coletivos empresariais (`planSaude`: CNPJ da operadora, registro ANS e valores separados entre titular e cada dependente, para alimentação direta da ficha de Pagamentos Efetuados da DAA); e
- Reembolsos de despesas médicas e odontológicas (`infoReembMed`);

II - **Evento `S-1210` (Pagamentos de Rendimentos do Trabalho):**
a) registra a data do **efetivo pagamento** dos rendimentos líquidos apurados nos eventos `S-1200`, `S-1202`, `S-1207`, `S-2299` e `S-2399`, determinando o fato gerador do **IRRF pelo regime de caixa**;

III - **Eventos Totalizadores de Retorno do IRRF (`S-5002` e `S-5012`):**
a) **`S-5002` (Imposto de Renda Retido na Fonte por Trabalhador):** evento gerado automaticamente pelo eSocial após o processamento do `S-1210`, consolidando por CPF as bases de cálculo, deduções legais (INSS oficial, dependentes, pensão alimentícia, previdência complementar ou **desconto simplificado mensal** de 25% do limite de isenção da Lei nº 14.663/2023, o que for mais benéfico ao trabalhador) e o IRRF retido;
b) **`S-5012` (Imposto de Renda Retido na Fonte Consolidado por Contribuinte):** gerado no fechamento dos eventos periódicos (`S-1299`), agrupando os valores de IRRF por **Código de Receita (CR)** e transmitindo-os automaticamente para a **DCTFWeb Mensal**.

### CAPÍTULO III — RECLAMATÓRIAS TRABALHISTAS (EVENTOS `S-2500`, `S-2501` E `S-5501`)

**Art. 3º** Os processos trabalhistas com decisões transitadas em julgado ou acordos homologados na Justiça do Trabalho (ou nas Comissões de Conciliação Prévia e Núcleos Intersindicais) são escriturados por meio dos eventos:
I - **`S-2500` (Processo Trabalhista):** cadastra os dados cadastrais e contratuais do processo e as bases de cálculo mensais de contribuição previdenciária e FGTS; e
II - **`S-2501` (Informações dos Tributos Decorrentes de Processo Trabalhista):** informa os valores de contribuições previdenciárias, contribuições destinadas a Terceiros e o **IRRF incidente sobre rendimentos do trabalho recebidos acumuladamente (RRA - código `1889-01`)** ou no ano-calendário (`0561-07`), alimentando a **DCTFWeb Reclamatória Trabalhista**.

**Art. 4º** Esta Portaria Conjunta entra em vigor na data de sua publicação, produzindo efeitos em produção a partir de **20 de novembro de 2023** (ambiente de produção restrita em 18 de setembro de 2023).

---

## Tabela de Códigos de Receita (CR) de IRRF Gerados pelo eSocial na DCTFWeb

| Código de Receita (CR) na DCTFWeb | Descrição da Hipótese de Incidência do IRRF no eSocial (`S-5012`) | Prazo de Vencimento do DARF Numerado |
| :---: | :--- | :--- |
| **`0561-15`** | IRRF — Rendimento do Trabalho Assalariado (empregados CLT, servidores e dirigentes) | Até o **dia 20 do mês subsequente** ao do pagamento (`S-1210`). |
| **`0588-07`** | IRRF — Rendimento do Trabalho Sem Vínculo Empregatício (autônomos, pró-labore, conselheiros e cooperados) | Até o **dia 20 do mês subsequente** ao do pagamento (`S-1210`). |
| **`3562-02`** | IRRF — Participação nos Lucros ou Resultados (**PLR** — tabela progressiva exclusiva da Lei nº 10.101/2000) | Até o **dia 20 do mês subsequente** ao do pagamento. |
| **`0473-04`** | IRRF — Rendimentos do Trabalho pagos a Residentes ou Domiciliados no Exterior | Até o **dia 20 do mês subsequente** (unificado na DCTFWeb pela IN RFB nº 2.137/2023). |
| **`1889-01`** | IRRF — Rendimentos Recebidos Acumuladamente (**RRA** — art. 12-A da Lei nº 7.713/1988, inclusive via `S-2501`) | Até o **dia 20 do mês subsequente** ao pagamento. |
