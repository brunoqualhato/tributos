---
titulo: "Ato COTEPE/ICMS nº 44, de 7 de agosto de 2018 (Guia Prático da EFD-ICMS/IPI — SPED Fiscal: Blocos e Registros para Operações Internas e Interestaduais)"
esfera: "Estadual / CONFAZ"
orgao: "Conselho Nacional de Política Fazendária - CONFAZ / Receita Federal do Brasil"
tipo: "Ato COTEPE/ICMS"
numero: "44"
data: "2018-08-07"
ano: "2018"
tema_tributario: "Produtos e Mercadorias"
tributos_afetados: ["ICMS", "ICMS-ST", "IPI"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.confaz.fazenda.gov.br/legislacao/ajustes/2009/AJ_002_09"
ementa: "Institui o Manual de Orientação do Leiaute da Escrituração Fiscal Digital - EFD ICMS/IPI (SPED Fiscal) e o Guia Prático da EFD-ICMS/IPI, detalhando a escrituração de documentos fiscais, apuração própria, Substituição Tributária por UF (Registro E200) e DIFAL/FCP por UF (Registro E300)."
---

# Ato COTEPE/ICMS nº 44, de 7 de agosto de 2018 (Guia Prático da EFD-ICMS/IPI — SPED Fiscal: Blocos e Registros para Operações Internas e Interestaduais)

ATO COTEPE/ICMS Nº 44, DE 7 DE AGOSTO DE 2018 — GUIA PRÁTICO DA ESCRITURAÇÃO FISCAL DIGITAL (EFD-ICMS/IPI) E AJUSTE SINIEF Nº 02/2009

Institui o Manual de Orientação do Leiaute da Escrituração Fiscal Digital - EFD ICMS/IPI e o Guia Prático da EFD-ICMS/IPI, em cumprimento ao disposto no Ajuste SINIEF nº 2, de 3 de abril de 2009.

## 1. Estrutura Completa de Blocos da EFD-ICMS/IPI (SPED Fiscal)

| Bloco | Nome do Bloco | Conteúdo e Finalidade Fiscal |
| :---: | :--- | :--- |
| **`0`** | Abertura, Identificação e Referências | Dados cadastrais do contribuinte (`0000`), participantes clientes/fornecedores com código de município IBGE e UF (`0150`), unidades de medida (`0190`), cadastro de itens NCM/CEST (`0200`), bens do ativo imobilizado CIAP (`0300`), natureza da operação (`0400`), informações complementares (`0450`) e observações do lançamento fiscal (`0460`). |
| **`B`** | Escrituração e Apuração do ISS | Exclusivo para contribuintes domiciliados no Distrito Federal (conjugação ICMS + ISSQN). |
| **`C`** | Documentos Fiscais I — Mercadorias (ICMS/IPI) | Notas Fiscais modelos `01`, `1B`, `04`, **`55` (NF-e)** e **`65` (NFC-e)**: entradas e saídas internas, interestaduais e de comércio exterior, incluindo registros analíticos (`C190`), ajustes de documento (`C197`) e obrigações a recolher (`C112`). |
| **`D`** | Documentos Fiscais II — Serviços (ICMS) | Conhecimentos de Transporte Eletrônicos (**`CT-e` modelo `57` e `CT-e OS` modelo `67`**), Bilhete de Passagem Eletrônico (`BP-e` modelo `63`) e Notas Fiscais de Serviços de Comunicação/Telecomunicação (**`NFCom` modelo `62`**, `21` e `22`). |
| **`E`** | **Apuração do ICMS e do IPI** | Apuração do **ICMS Próprio (`E100`/`E110`/`E111`/`E116`)**, do **ICMS-ST por UF (`E200`/`E210`/`E250`)**, do **DIFAL EC 87/2015 e FCP por UF de destino (`E300`/`E310`/`E316`)** e do **IPI (`E500`/`E510`/`E520`)**. |
| **`G`** | Controle do Crédito de ICMS do Ativo Permanente (**CIAP**) | Controle e apropriação em **1/48 (um quarenta e oito avos) mensais** do crédito de ICMS (próprio + DIFAL + frete) sobre aquisições para o Ativo Imobilizado (art. 20, § 5º da LC 87/1996), ponderado pelo coeficiente de saídas tributadas/exportação sobre o total de saídas (`G110` a `G140`). |
| **`H`** | Inventário Físico | Posição física e financeira dos estoques em 31 de dezembro (entregue até o 2º mês subsequente) ou na data de alteração de regime tributário (inclusão/exclusão da Substituição Tributária — `H005`, `H010`, `H020`). |
| **`K`** | Controle da Produção e do Estoque | Escrituração mensal da movimentação de estoques (`K200`), desmontagem (`K210`), reprocessamento (`K220`), ordens de produção e consumo de insumos (`K230`/`K235`), industrialização em terceiros (`K250`/`K255`) e correções de apontamento (`K270`/`K280`). |
| **`1`** | Outras Informações | Exportações (`1100`), controle de créditos fiscais (`1200`), movimentação diária de combustíveis (`1300`), operações com cartões de crédito/débito e PIX (`1600`/`1601`) e sub-apurações estaduais (`1900`). |
| **`9`** | Controle e Encerramento do Arquivo Digital | Totalizadores de registros por bloco (`9900`) e assinatura digital de encerramento do arquivo (`9999`). |

---

## 2. Regras de Escrituração das Operações Interestaduais nos Registros dos Blocos `C`, `D` e `E`

### 2.1. Escrituração sob o Enfoque do Declarante (Regra de Ouro da EFD-ICMS/IPI)
- **Nas Entradas Interestaduais (CFOP `2.xxx`) e Internas (`1.xxx`):** Os registros `C100` (cabeçalho do documento), `C170` (itens do documento, obrigatório nas entradas de NF-e de terceiros quando não dispensado pela UF) e `C190` (resumo analítico por combinação de CST + CFOP + Alíquota) devem ser escriturados **estritamente sob o enfoque do estabelecimento declarante destinatário**:
  - **Aquisição para Industrialização (`CFOP 2.101`) ou Comercialização (`CFOP 2.102`) no Regime Normal:** Escritura-se no `C170`/`C190` com `CST 000` (ou `020` com redução de BC) e apropriação do crédito correspondente ao ICMS destacado pelo remetente (respeitados os limites das alíquotas interestaduais de 4%, 7% ou 12% e eventuais glosas de benefícios fiscais não convalidados nos termos da LC 160/2017).
  - **Aquisição para Uso ou Consumo (`CFOP 2.556`) ou Ativo Imobilizado (`CFOP 2.551`):** Não há apropriação direta de crédito de ICMS nos campos `VL_BC_ICMS` e `VL_ICMS` do Registro `C190` (que devem ser preenchidos com zero). O crédito do ativo imobilizado é apropriado exclusivamente por meio do **Bloco `G` (CIAP)** à razão de 1/48 ao mês, gerado no Registro `E111` (ou `C197`). O valor do **DIFAL Contribuinte** devido na entrada interestadual é lançado mediante ajuste de débito especial ou apuração em separado no Registro `C197` (código da Tabela 5.3 da UF) ou no Registro `E111` (código da Tabela 5.1.1 da UF), recolhido ou compensado conforme o RICMS estadual.
  - **Aquisição Sujeita à Substituição Tributária (`CFOP 2.403` ou `1.403`):** Quando o imposto já foi retido anteriormente pelo remetente substituto ou recolhido por antecipação na entrada com encerramento de tributação, o adquirente substituído escritura a entrada com `CST 060`, zerando os campos de base de cálculo e valor do ICMS próprio e do ICMS-ST no Registro `C190` (informando o imposto retido apenas nos campos informativos ou registros de ressarcimento quando cabível).

### 2.2. Exceção nas Saídas com NF-e de Emissão Própria (Dispensa do `C170`)
- Nas **saídas acobertadas por NF-e (modelo 55) ou NFC-e (modelo 65) de emissão própria**, a regra geral do Guia Prático veda o preenchimento do Registro `C170` (itens), exigindo apenas o cabeçalho `C100` e o resumo analítico `C190` (salvo exceções específicas em que a UF exige o `C170` na saída para controle de incentivos fiscais ou itens específicos).

### 2.3. Apuração do ICMS-ST por Unidade da Federação — Registros `E200` a `E250`
- Para cada Estado de destino em que o contribuinte tenha realizado operações interestaduais com retenção de **ICMS-ST** (como substituto tributário por protocolo ou convênio, CFOP `6.401`/`6.403`/`6.404`), ou operações internas sujeitas à ST (`CFOP 5.401`/`5.403`), a EFD-ICMS/IPI deve gerar um **Registro `E200` identificando a sigla da UF de destino** (`UF`), seguido de:
  - **Registro `E210`:** Apuração do ICMS de Substituição Tributária (devolução de mercadorias com ST, ressarcimentos, retenções por saída, ajustes a débito/crédito e saldo devedor a recolher);
  - **Registro `E220`:** Ajustes/Benefícios/Incentivos da apuração do ICMS-ST (utilizando códigos da Tabela 5.1.1);
  - **Registro `E250`:** Detalhamento das obrigações do ICMS-ST recolhido ou a recolher (informando o código de receita da GNRE `10009-9` por operação ou `10004-8` por apuração mensal, data de vencimento e valor).

### 2.4. Apuração do DIFAL Não Contribuinte e FCP por UF — Registros `E300` a `E316`
- Sempre que o contribuinte realizar vendas ou prestações interestaduais destinadas a consumidor final não contribuinte (`CFOP 6.107`, `6.108` ou `6.357`), deve gerar um **Registro `E300` para cada UF de destino** onde houve movimentação ou saldo no período:
  - **Registro `E310`:** Apuração segregada do **DIFAL** (campos de débitos por saída, créditos por devolução e saldo devedor) e do **Fundo de Combate à Pobreza (FCP)** (campos próprios de débito, crédito e saldo devedor de FCP);
  - **Registro `E311` a `E313`:** Ajustes da apuração do DIFAL/FCP e identificação dos documentos fiscais relacionados aos ajustes;
  - **Registro `E316`:** Obrigações recolhidas ou a recolher, vinculando as respectivas guias GNRE (`10010-2` ou `10011-0` para o DIFAL e `10012-9` ou `10013-7` para o FCP).

---

## 3. Tabelas Externas de Ajustes da EFD-ICMS/IPI (item 5 do Guia Prático)

| Código da Tabela | Nome da Tabela | Registro de Aplicação |
| :---: | :--- | :--- |
| **Tabela `5.1.1`** | Tabela de Códigos de Ajustes da Apuração do ICMS | Registros `E111` (ICMS Próprio), `E220` (ICMS-ST) e `E311` (DIFAL/FCP). Formato `UF + 6 dígitos` (ex.: `SP000207`, `MG020001`). |
| **Tabela `5.2`** | Tabela de Informações Adicionais da Apuração — Valores Declaratórios | Registro `E115` (valores informativos sobre benefícios fiscais, créditos presumidos, sub-apurações e fundos estaduais). |
| **Tabela `5.3`** | Tabela de Ajustes e Informações de Valores Provenientes de Documento Fiscal | Registros `C197` e `D197` (ajustes vinculados diretamente ao documento fiscal e ao item/observação `0460`). Formato `UF + 8 dígitos`. |
