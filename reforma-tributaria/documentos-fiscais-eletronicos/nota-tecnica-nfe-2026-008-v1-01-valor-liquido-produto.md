---
titulo: "Nota Técnica NF-e/NFC-e nº 2026.008, versão 1.01, de 30 de outubro de 2026 (Valor Líquido do Produto)"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil / ENCAT - CONFAZ"
tipo: "Nota Técnica"
numero: "2026.008"
data: "2026-10-30"
ano: "2026"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY="
ementa: "Divulga a criação de campos para o valor líquido do produto e para o ICMS previsto no pagamento antecipado na NF-e e na NFC-e, com as regras de validação correspondentes."
data_consulta: "2026-11-27"
versao_texto: "Versão 1.01 (PDF oficial, 30/10/2026)"
---

# Nota Técnica NF-e/NFC-e nº 2026.008, versão 1.01, de 30 de outubro de 2026 (Valor Líquido do Produto)

> **Nota editorial.** Texto extraído da camada de texto do PDF oficial da Nota Técnica 2026.008, versão 1.01, divulgado no Portal Nacional da NF-e (8 páginas), consultado em 27/11/2026. A data do documento (30/10/2026) é a de publicação da versão, lida na lista de Notas Técnicas do portal. Versão aprovada ou ratificada pelo Ato Técnico Conjunto Sufis/CGIBS nº 10/2026 (`reguladores/rfb/outros-atos/2026/ato-154369-10-2026.md`). Foram removidos a capa, o sumário, os cabeçalhos e rodapés repetidos e a numeração de página. Os 4 títulos de primeiro nível do sumário viraram seções e o texto de cada uma, com os quadros e os leiautes, ficou em bloco de texto que mantém as colunas do PDF. Figuras e imagens do PDF não foram convertidas. Em caso de dúvida, prevalece o PDF. O portal só entrega o PDF com cookie de sessão; o link da fonte é a página de lista de Notas Técnicas, onde a versão consta como "Publicada em 30/10/2026".

## Histórico de Alterações / Cronograma

```text
Versão                        Histórico de atualizações                          Implantação      Implantação
                                                                                Homologação        Produção
 1.00    - Criação dos campos que representam os valores líquidos do produto.     05/10/2026       03/11/2026
         - Criação do campo para informar o ICMS previsto no Pagamento          Até 26/10/2026     16/11/2026
              Antecipado.
         - Regras de validação incluídas: I11c-10, I11c-20, NB01-10, NB01-20,
              W01a-10, W01a-20.
         - Regras de validação alteradas: B25-80, VB01-10, VB01-20.
         - Regras de validação removidas: UB16-10.
 1.00    - Regra de validação incluída: NB01-30.                                  01/02/2027       01/03/2027
 1.01    - Alteração das datas de implantação em Homologação e Produção         Até 26/10/2026     16/11/2026
              (exceto RV NB01-30)
 1.01    - Retirado item “Composição do valor do produto com informações de           -                -
              IBS e CBS”.
 1.01    - Regras de validação alteradas: VB01-10, VB01-20.                     Implementação    Implementação
                                                                                    Futura           Futura
```

## 1. Introdução

```text
Criação de campos para o valor líquido do produto
Com o objetivo de ampliar a transparência na formação do preço da operação, foram criados
os campos Valor Líquido Unitário e Valor Líquido do Produto. Esses campos permitem
identificar o valor da mercadoria ou do serviço antes da incorporação dos tributos vigentes
que compõem o preço final, possibilitando distinguir, de forma clara, o valor líquido da
operação dos valores tributários agregados ao preço.

A medida busca preservar a rastreabilidade da formação do valor informado na NF-e,
especialmente diante da sistemática do IBS e da CBS.

Dessa forma, os novos campos permitem evidenciar tanto o valor líquido unitário quanto o
valor líquido total do item, proporcionando maior transparência ao contribuinte, ao
adquirente e às Administrações Tributárias quanto à composição do preço e à participação
dos tributos no valor final da operação.

O IBS e a CBS são tributos calculados por fora, não integrando suas próprias bases de
cálculo. A base de cálculo dos tributos deverá ser determinada de acordo com a legislação
aplicável. Desta forma, em cada item:
  •   No campo vProdLiq deve ser informado o valor líquido do produto ou serviço, sem
      qualquer tributo;
  •   No campo vProd deve ser informado o valor total do produto ou serviço,
      desconsiderados os valores de IBS, CBS e IS;
  •   No campo vItem deve ser informado o valor total do item, incluindo todos os tributos.
No total do documento fiscal:
  •   No campo vNFTot deve ser informado o valor correspondente a soma do valor total dos
      itens (vItem).

Criação de campo para informar o ICMS previsto
O novo campo “Valor do ICMS Previsto no Pagamento Antecipado” (tag: vICMSPrevisto)
deverá ser informado quando o documento fiscal emitido for referente a um pagamento
realizado antes do fornecimento. O objetivo do campo é permitir a correta tributação do IBS e
da CBS no pagamento antecipado, com a identificação do valor do ICMS que incidirá no
momento do fornecimento futuro.
```

## 2. Leiaute da NF-e (Modelo 55 e 65)

```text
Grupo I. Produtos e Serviços da NF-e
#       ID Campo                Descrição                                  Ele Pai Tipo Ocor.        Tam. Observação
110     I11 vProd               Valor Total Bruto dos Produtos ou           E I01 N      1-1         13v2 O valor do ICMS faz parte do Valor Total Bruto, exceto nas notas de
                                Serviços.                                                                   importação (NT 2020.005)
                                                                                                            Observação: A partir de 2027, os valores de IBS, CBS e IS
                                                                                                                compõem o Valor Total Bruto, exceto nas notas de importação.
110.01 I11a         -x-         Sequência XML                                  G I01          0-1           Observação: Futuramente essa sequência será obrigatória.
110.02 I11b vUnComLiq           Valor Líquido Unitário do Produto ou           E I11a    N    1-1   11v0-10 Valor unitário de comercialização do produto ou serviço, sem a
                                Serviço (sem tributos)                                                      inclusão de tributos.
110.03 I11c vProdLiq            Valor Líquido do Produto ou Serviço (sem       E I11a    N    1-1    13v2 Valor líquido do produto ou serviço, sem a inclusão de tributos.
                                tributos)

Grupo NB. ICMS Previsto no Pagamento Antecipado
#      ID   Campo                    Descrição                                   Ele    Pai Tipo Ocor. Tam. Observação
245b.0 NB01 ICMSPrevistoPagtoAntecip Grupo do ICMS Previsto no                   CG     N01       1-1       Grupo utilizado exclusivamente em cenários específicos
1                                    Pagamento Antecipado                                                   de pagamento antecipado para auxiliar na correta
                                                                                                            tributação do IBS e da CBS:
                                                                                                              - tpNFDebito = 06-Pagamento antecipado;
                                                                                                              - tpOperGov = 4-Recebimento do pagamento com
                                                                                                                fornecimento posterior.
245b.02 NB02 vICMSPrevisto              Valor do ICMS Previsto                   E     NB01 N     1-1 13v2 Valor do ICMS que incidirá no momento do fornecimento
                                                                                                            futuro.
                                                                                                            Observação 1: Em cenários onde não haverá valor de ICMS
                                                                                                                devido no fornecimento, informar 0.

Grupo W. Total da NF-e
#       ID   Campo              Descrição                                        Ele Pai Tipo Ocor. Tam. Observação
326a    W01a vProdLiqTot        Valor Total Líquido dos Produtos ou Serviços      E W01 N      0-1 13v2 Soma dos valores líquidos dos produtos ou serviços, sem a
                                (sem tributos)                                                           inclusão de tributos.
```

## 3. Regras de Validação

```text
Grupo B. Identificação da Nota Fiscal eletrônica
 Campo        Modelo                                    Regra de Validação                                          Aplic. Msg                    Descrição Erro
 B25-80         55   Se finalidade da NF-e igual a crédito ou débito (tag: finNFe=5 ou 6) ou tpOperGov=2-           Obrig. 1001 Rejeição: NF-e com finalidade de débito ou crédito
                        Recebimento do pagamento:                                                                               somente para IBS/CBS
                      - Informado ICMS (tag: ICMS), ISSQN (tag: ISSQN), IPI (tag: IPI), II (tag: II), PIS (tag:
                        PIS), PIS ST (tag: PISST), COFINS (tag: COFINS), COFINS ST (tag: COFINSST),
                        ICMS UF Destino (tag: ICMSUFDest) ou Imposto Devolvido (tag: impostoDevol).
                     Exceção 1: a regra acima não se aplica para:
                      - tpNFCredito=03-Retorno por Recusa Total na Entrega ou Por Não Localização do
                        Destinatário na Tentativa de Entrega;
                      - tpNFCredito=04-Redução de valores;
                      - tpNFCredito=06-Retorno por recusa parcial na entrega;
                      - tpNFDebito=07-Perda em estoque;
                     Exceção 2: tpNFDebito=”06-Pagamento Antecipado” permite a informação do PIS,
                        PISST, COFINS e COFINSST em NF-e com data de emissão em 2026.
                     Exceção 3: tpNFDebito=”06-Pagamento Antecipado” permite a informação do IPI.
                     Exceção 4: tpNFDebito=”06-Pagamento Antecipado” permite a informação do grupo
                        ICMS/ICMSPrevistoPagtoAntecip (id: NB01).

Grupo I. Produtos e Serviços da NF-e
 Campo Modelo                                    Regra de Validação                                               Aplic. Msg                       Descrição Erro
I11c-10 55/65 Se vProdLiq (id:I11c) não informado:                                                                Obrig. 1278 Rejeição: Valor Líquido do Produto não informado [nItem:
               - vProdLiq (id:I11c) não informado                                                                             999]
              Observação: Implementação futura.
I11c-20 55/65 Se informado vProdLiq (id:I11c) e NF-e Normal (tag: finNFe=1):                                      Obrig. 1279 Rejeição: Valor Líquido do Produto difere do calculado
               - vProdLiq (id:I11c) difere de vUnComLiq (id:I11b) * qCom (id:I10)                                             [nItem: 999]
              Observação: Aceitar uma tolerância de 0,01 a mais ou a menos.

Grupo NB. ICMS Previsto no Pagamento Antecipado
 Campo Modelo                                  Regra de Validação                                  Aplic. Msg                      Descrição Erro
NB01-10  65   Se grupo ICMSPrevistoPagtoAntecip (id:NB01) informado:                               Obrig. 1280 Rejeição: Grupo do ICMS Previsto no Pagamento
                - Modelo igual a 65                                                                            Antecipado informado indevidamente [nItem: 999]
NB01-20  55   Se tpNFDebito diferente de “06-Pagamento Antecipado” (tag: tpNFDebito <> 06) e       Obrig. 1280 Rejeição: Grupo do ICMS Previsto no Pagamento
              tpOperGov diferente de “4-Recebimento do pagamento com fornecimento posterior” (tag:             Antecipado informado indevidamente [nItem: 999]
              tpOperGov <> 4):
                - Grupo ICMSPrevistoPagtoAntecip (id:NB01) informado indevidamente

 Campo Modelo                                 Regra de Validação                                    Aplic. Msg                     Descrição Erro
NB01-30  55   Se tpNFDebito igual a “06-Pagamento Antecipado” (tag: tpNFDebito = 06) ou tpOperGov Obrig. 1281 Rejeição: Grupo do ICMS Previsto no Pagamento
              igual a “4-Recebimento do pagamento com fornecimento posterior” (tag: tpOperGov = 4):            Antecipado não informado [nItem: 999]
                - Grupo ICMSPrevistoPagtoAntecip (id:NB01) não informado
              Observação 1: Implantação em homologação em 01/02/2027.
              Observação 2: Implantação em produção em 01/03/2027.

Grupo VB. Total do item da NF-e
Campo Modelo                                      Regra de Validação                                  Aplic. Msg                      Descrição Erro
VB01-10 55/65 Se vItem informado:                                                                     Obrig. 1105 Rejeição: Valor total do Item (vItem) difere do
               Se não é operação de Faturamento Direto para veículos novos (tpOp = nulo ou tpOp <> 2,             somatório dos valores que o compõem [nItem: 999]
                 id:J02):
               - Valor total do Item (vItem) deve ser igual ao somatório:
                 (+) vProd (contém vIBS, vCBS e vIS)
                 (-) vDesc
                 (-) vICMSDeson, se indDeduzDeson=1
                 (+) vICMSST
                 (+) vICMSMonoReten
                 (+) vFCPST
                 (+) vFrete
                 (+) vSeg
                 (+) vOutro
                 (+) vII
                 (+) vIPI
                 (+) vIPIDevol
                 (+) vServ
                 (+) vPIS (id: R06, campo: PISST/vPIS), se indSomaPISST=1
                 (+) vCofins (id: T06, campo: COFINSST/vCOFINS), se indSomaCOFINSST =1 (NT
                      2020.005)
                 (+) vIBS
                 (+) vCBS
                 (+) vIS
                 (+) vTotIBSMonoItem
                 (+) vTotCBSMonoItem
              Exceção 1: Em 2025 e 2026 não somar vIBS, vCBS, vIS, vTotIBSMonoItem,
                 vTotCBSMonoItem.
              Exceção 2: Esta regra não se aplica nas operações de importação (CFOP inicia com “3").
              Observação: Implementação Futura.

Campo Modelo                                     Regra de Validação                                    Aplic. Msg                      Descrição Erro
VB01-20 55   Se vItem informado:                                                                       Obrig. 1105 Rejeição: Valor total do Item (vItem) difere do
              Se informada operação de Faturamento Direto para veículos novos (tpOp = 2, id:J02):                  somatório dos valores que o compõem [nItem: 999]
              - Valor total do Item (vItem) deve ser igual ao somatório:
                (+) vProd (contém vIBS, vCBS e vIS)
                (-) vDesc
                (-) vICMSDeson, se indDeduzDeson=1
                (+) vFrete
                (+) vSeg
                (+) vOutro
                (+) vII
                (+) vIPI
                (+) vServ
                (+) vPIS (id: R06, campo: PISST/vPIS), se indSomaPISST=1
                (+) vCofins (id: T06, campo: COFINSST/vCOFINS), se indSomaCOFINSST =1 (NT
                     2020.005)
                (+) vIBS
                (+) vCBS
                (+) vIS
             Exceção 1: Em 2025 e 2026, não somar vIBS, vCBS, vIS.
             Exceção 2: Esta regra não se aplica nas operações de importação (CFOP inicia com “3").
             Observação: Implementação Futura.

Grupo W. Total da NF-e
Campo Modelo                                    Regra de Validação                                    Aplic. Msg                      Descrição Erro
W01a-10 55/65 Se informado vProdLiq (id:I11c) em um dos itens:                                        Obrig. 1282 Rejeição: Total Líquido não informado
               - vProdLiqTot (id:W01a) não informado
W01a-20       55/65 Se informado vProdLiqTot (id:W01a):                                               Obrig. 1283 Rejeição: Total Líquido difere do somatório dos itens
                     - vProdLiqTot (id:W01a) difere do somatório do vProdLiq (id:I11c) dos itens
```
