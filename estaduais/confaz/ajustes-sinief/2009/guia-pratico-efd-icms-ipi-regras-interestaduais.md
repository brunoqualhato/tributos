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

ATO COTEPE/ICMS Nº 44, DE 7 DE AGOSTO DE 2018 — GUIA PRÁTICO DA ESCRITURAÇÃO FISCAL DIGITAL (EFD-ICMS/IPI)

## 1. Estrutura de Blocos da EFD-ICMS/IPI (SPED Fiscal)

| Bloco | Nome do Bloco | Conteúdo e Finalidade Fiscal |
| :---: | :--- | :--- |
| **`0`** | Abertura, Identificação e Referências | Dados cadastrais do contribuinte (`0000`), participantes clientes/fornecedores com código de município IBGE e UF (`0150`), cadastro de itens NCM/CEST (`0200`), bens do ativo imobilizado CIAP (`0300`) e tabelas de observações (`0460`). |
| **`B`** | Escrituração e Apuração do ISS | Exclusivo para contribuintes do Distrito Federal (conjugação ICMS + ISS). |
| **`C`** | Documentos Fiscais I — Mercadorias (ICMS/IPI) | Notas Fiscais modelos `01`, `1B`, `04`, **`55` (NF-e)** e **`65` (NFC-e)**: entradas e saídas internas, interestaduais e de comércio exterior. |
| **`D`** | Documentos Fiscais II — Serviços (ICMS) | Conhecimentos de Transporte Eletrônicos (**`CT-e` modelo `57` e `CT-e OS` modelo `67`**) e Notas Fiscais de Serviços de Comunicação/Telecomunicação (**`NFCom` modelo `62`**, `21` e `22`). |
| **`E`** | **Apuração do ICMS e do IPI** | Apuração do **ICMS Próprio (`E100`/`E110`)**, do **ICMS-ST por UF (`E200`/`E210`)**, do **DIFAL EC 87/2015 e FCP por UF de destino (`E300`/`E310`)** e do **IPI (`E500`/`E520`)**. |
| **`G`** | Controle do Crédito de ICMS do Ativo Permanente (**CIAP**) | Controle e apropriação em **1/48 (um quarenta e oito avos) mensais** do crédito de ICMS (próprio + DIFAL + frete) sobre aquisições para o Ativo Imobilizado (art. 20, § 5º da LC 87/1996). |
| **`H`** | Inventário Físico | Posição física e financeira dos estoques em 31 de dezembro (ou por mudança de regime de ST). |
| **`K`** | Controle da Produção e do Estoque | Escrituração mensal da movimentação de estoques (`K200`), ordens de produção e consumo de insumos (`K230`/`K235`) e industrialização em terceiros (`K250`/`K255`). |
| **`1`** | Outras Informações | Exportações (`1100`), controle de créditos fiscais (`1200`), operações com cartões/PIX (`1600`/`1601`) e sub-apurações estaduais (`1900`). |

---

## 2. Regras de Escrituração das Operações Interestaduais nos Registros dos Blocos `C`, `D` e `E`

### 2.1. Escrituração sob o Enfoque do Declarante (Regra de Ouro da EFD-ICMS/IPI)
- **Nas Entradas Interestaduais (CFOP `2.xxx`):** Os registros `C100` (cabeçalho), `C170` (itens) e `C190` (analítico por CST/CFOP/Alíquota) devem ser escriturados **sob o enfoque do estabelecimento declarante destinatário**:
  - Se a aquisição interestadual for para **uso ou consumo (`CFOP 2.556`)** ou **ativo imobilizado (`CFOP 2.551`)**, não há apropriação direta de crédito no `C190` (o crédito do ativo vai pelo Bloco `G` em 1/48), e o valor do **DIFAL Contribuinte** é lançado mediante ajuste de débito especial ou apuração no Registro `C197` (código de ajuste da tabela 5.3 da UF) ou no Registro `E111` (tabela 5.1.1 da UF).
  - Se a aquisição interestadual estiver sujeita à **Substituição Tributária já retida pelo remetente (`CFOP 2.403`)** ou **Antecipação com encerramento na entrada**, a entrada é escriturada com CST `060`, sem crédito de ICMS próprio nem de ST no `C190`.

### 2.2. Apuração do ICMS-ST por Unidade da Federação — Registros `E200` a `E250`
- Para cada Estado de destino em que o contribuinte tenha realizado operações interestaduais com retenção de **ICMS-ST** (como substituto tributário por protocolo ou convênio, CFOP `6.401`/`6.403`/`6.404`), a EFD-ICMS/IPI deve gerar um **Registro `E200` identificando a sigla da UF de destino** (`UF`), seguido do `E210` (apuração do ICMS-ST devido àquela UF, devoluções de ST e ressarcimentos) e do `E250` (detalhamento das GNREs código `10009-9` ou `10004-8` recolhidas àquela UF).

### 2.3. Apuração do DIFAL Não Contribuinte e FCP por UF — Registros `E300` a `E316`
- Sempre que o contribuinte realizar vendas ou prestações interestaduais destinadas a consumidor final não contribuinte (`CFOP 6.107` ou `6.108`), deve gerar um **Registro `E300` para cada UF de destino**, apurando no `E310` o saldo devedor do **DIFAL** e, separadamente, do **Fundo de Combate à Pobreza (FCP)**, vinculando no `E316` as respectivas guias GNRE (`10010-2` / `10011-0` para o DIFAL e `10012-9` / `10013-7` para o FCP).
