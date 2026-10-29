---
titulo: "Resolução ANP nº 795, de 5 de julho de 2019"
esfera: "Federal"
orgao: "Agência Nacional do Petróleo, Gás Natural e Biocombustíveis - ANP"
tipo: "Resolução ANP"
numero: "795"
data: "2019-07-05"
ano: "2019"
tema_tributario: "Combustíveis e Energia"
tributos_afetados: ["ICMS Combustíveis", "CIDE-Combustíveis", "Documento Fiscal Eletrônico"]
situacao: "Em vigor"
revogada: false
fonte: "https://atosoficiais.com.br/anp/resolucao-n-795-2019"
ementa: "Regulamenta a obrigatoriedade de prestação de informações e emissão de notas fiscais nas operações de movimentação, distribuição e revenda varejista de combustíveis automotivos."
---

# Resolução ANP nº 795, de 5 de julho de 2019 (Prestação de Informações de Preços, Volumes e Documentos Fiscais de Combustíveis)

## Identificação Normativa

- **Tipo:** Resolução Regulatória
- **Número:** 795
- **Data:** 5 de julho de 2019
- **Órgão Emissor:** Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP)
- **Fonte Oficial:** [Atos Oficiais ANP / Diário Oficial da União](https://atosoficiais.com.br/anp/resolucao-n-795-2019)

---

## Texto Normativo Consolidado

**RESOLUÇÃO ANP Nº 795, DE 5 DE JULHO DE 2019**

Dispõe sobre a obrigatoriedade de apresentação de dados de preços e volumes comercializados de derivados de petróleo, gás natural e biocombustíveis pelos agentes regulados e sobre a integração de dados de documentos fiscais eletrônicos.

**A DIRETORIA DA AGÊNCIA NACIONAL DO PETRÓLEO, GÁS NATURAL E BIOCOMBUSTÍVEIS - ANP**, no exercício das atribuições conferidas pelo art. 6º do Regimento Interno e pelo art. 7º do Anexo I do Decreto nº 2.455, de 14 de janeiro de 1998, tendo em vista o disposto na Lei nº 9.478, de 6 de agosto de 1997,

**RESOLVE:**

### CAPÍTULO I — DO OBJETO E DO ÂMBITO DE APLICAÇÃO

**Art. 1º** Esta Resolução estabelece a obrigatoriedade de apresentação de dados de preços e volumes comercializados relativos aos derivados de petróleo, gás natural e biocombustíveis por produtores, importadores, distribuidores e revendedores, bem como os requisitos técnicos de identificação nos documentos fiscais eletrônicos (NF-e e NFC-e).

**Art. 2º** Ficam obrigados ao envio periódico das informações de movimentação, estoques e preços praticados, por meio do Sistema de Informações de Movimentação de Produtos (SIMP / i-SIMP) e da integração com o Ambiente Nacional da Nota Fiscal Eletrônica (SPED):
I - os produtores de derivados de petróleo e gás natural (refinarias, centrais petroquímicas, formuladores e unidades de processamento de gás natural - UPGNs);
II - os produtores de biocombustíveis (usinas de etanol anidro e hidratado, produtores de biodiesel B100 e biometano);
III - os distribuidores de combustíveis líquidos automotivos, de aviação, de solventes, de asfaltos e de gás liquefeito de petróleo (GLP);
IV - os transportadores-revendedores-retalhistas (TRR); e
V - os postos revendedores varejistas de combustíveis automotivos e revendedores de GLP.

### CAPÍTULO II — DOS DADOS DOS DOCUMENTOS FISCAIS ELETRÔNICOS E DO SIMP

**Art. 3º** Os agentes de que tratam os incisos I a IV do art. 2º deverão enviar mensalmente à ANP, até o dia 15 (quinze) do mês subsequente ao de competência, por meio do Sistema de Informações de Movimentação de Produtos (i-SIMP), todas as informações relativas à produção, importação, exportação, aquisição, transferência, mistura, comercialização e estoques iniciais e finais de produtos regulados.

**Art. 4º** Nas Notas Fiscais Eletrônicas (NF-e, modelo 55) e nas Notas Fiscais de Consumidor Eletrônicas (NFC-e, modelo 65) emitidas para acobertar operações com combustíveis líquidos, GLP, lubrificantes e biocombustíveis, os agentes regulados deverão preencher obrigatoriamente o **Grupo de Detalhamento Específico de Combustíveis (`<comb>`)**, consignando:
I - o código do produto da ANP (`<cProdANP>`), conforme Tabela de Códigos de Produtos do SIMP;
II - a descrição do produto conforme a ANP (`<descANP>`);
III - o percentual de mistura de GLP derivado de petróleo, de gás natural, de etanol anidro ou de biodiesel, quando aplicável (`<pGLP>`, `<pGNn>`, `<pGNi>`, `<pBio>`);
IV - o código de autorização ou registro do agente remetente e destinatário na ANP (`<CODIF>`), quando exigido;
V - a quantidade de combustível faturada à temperatura ambiente (`<qTemp>`) convertida para a base de referência de 20ºC, nas operações de produtores e distribuidores; e
VI - a sigla da Unidade da Federação de consumo (`<UFCons>`).

**Art. 5º** Os preços de venda praticados pelos produtores e importadores de derivados de petróleo e biocombustíveis deverão ser reportados indicando o valor unitário sem tributos e o valor unitário com a inclusão de PIS/PASEP, COFINS, CIDE-Combustíveis e ICMS (próprio e por substituição tributária ou monofásico).

**Art. 11.** O descumprimento das disposições desta Resolução sujeitará o infrator às penalidades previstas na Lei nº 9.847, de 26 de outubro de 1999.

**Art. 12.** Esta Resolução entra em vigor na data de sua publicação.

DÉCIO FABRICIO ODDONE DA SILVA
Diretor-Geral da ANP

---

## Notas Técnicas de Auditoria Fiscal e Integração SPED / SCANC / SIMP-ANP

### 1. Cruzamento Eletrônico entre NF-e (`<comb>`), SIMP-ANP e SCANC (ICMS Monofásico)
A Resolução ANP nº 795/2019 e as Notas Técnicas da NF-e (notadamente a **Nota Técnica 2023.001** do ICMS Monofásico de Combustíveis) estruturam a malha fiscal integrada entre a ANP, a Receita Federal do Brasil e as 27 Secretarias de Fazenda Estaduais:
- Qualquer divergência entre o volume declarado no **i-SIMP da ANP**, o volume escriturado no **Bloco K / Registro 1300 da EFD-ICMS/IPI (LMC - Livro de Movimentação de Combustíveis)** e os anexos do **SCANC** gera bloqueio automático de repasse do ICMS Monofásico (`CST 02`, `15`, `53` e `61`) e autuação por omissão de entrada ou saída de combustível desacobertado.

### 2. Fator de Correção de Volume para 20ºC (FVC)
Nas operações atacadistas entre refinarias, formuladores, usinas e distribuidoras, os volumes de combustíveis líquidos sofrem dilatação ou contração térmica significativa. Por essa razão, a tributação específica (*ad rem* em reais por metro cúbico ou litro) da CIDE, do PIS/COFINS Monofásico e do ICMS Monofásico incide sobre o volume corrigido para a temperatura padrão de **20ºC** (campo `<qTemp>` da NF-e), conforme tabelas de correção volumétrica ABNT/CNP/ANP.
