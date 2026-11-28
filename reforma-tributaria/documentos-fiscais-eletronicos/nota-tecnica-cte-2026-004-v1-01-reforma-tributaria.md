---
titulo: "Nota Técnica CT-e nº 2026.004, versão 1.01, de 30 de outubro de 2026 (CT-e, CT-e OS e GTV-e na Reforma Tributária do Consumo: valor líquido, multa e juros, formas de emissão e crédito presumido)"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil / ENCAT - CONFAZ"
tipo: "Nota Técnica"
numero: "2026.004"
data: "2026-10-30"
ano: "2026"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.cte.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=Y0nErnoZpsg="
ementa: "Nota técnica de adequação dos leiautes do CT-e, do CT-e OS e da GTV-e à Reforma Tributária do Consumo: valor líquido da prestação, grupo de multa e juros, formas de emissão, CT-e Simplificado e evento de apropriação do crédito presumido."
data_consulta: "2026-11-27"
versao_texto: "Versão 1.01 (PDF oficial, 30/10/2026)"
---

# Nota Técnica CT-e nº 2026.004, versão 1.01, de 30 de outubro de 2026 (CT-e, CT-e OS e GTV-e na Reforma Tributária do Consumo: valor líquido, multa e juros, formas de emissão e crédito presumido)

> **Nota editorial.** Texto extraído da camada de texto do PDF oficial da Nota Técnica 2026.004, versão 1.01, divulgado no Portal Nacional do CT-e (16 páginas), consultado em 27/11/2026. A data do documento (30/10/2026) é a de publicação da versão, lida na lista de Notas Técnicas do portal. Versão aprovada ou ratificada pelo Ato Técnico Conjunto Sufis/CGIBS nº 10/2026 (`reguladores/rfb/outros-atos/2026/ato-154369-10-2026.md`). Foram removidos a capa, o sumário, os cabeçalhos e rodapés repetidos e a numeração de página. Os 8 títulos de primeiro nível do sumário viraram seções e o texto de cada uma, com os quadros e os leiautes, ficou em bloco de texto que mantém as colunas do PDF. Figuras e imagens do PDF não foram convertidas. Em caso de dúvida, prevalece o PDF. O portal só entrega o PDF com cookie de sessão; o link da fonte é a página de lista de Notas Técnicas, onde a versão consta como "Publicada em 30/10/2026". Os atos técnicos conjuntos indicam uma NT 2026.004 também para BP-e, NFCom, NF3e, NFAg e NFGas; elas são documentos próprios dos respectivos portais e não integram o acervo. A versão 1.00 deste CT-e foi aprovada pelo Ato Técnico Conjunto Sufis/CGIBS nº 8/2026 (`reguladores/rfb/outros-atos/2026/ato-153886-8-2026.md`).

## Histórico de Alterações / Cronograma

```text
Versão                             Histórico de atualizações                                Implantação     Implantação
                                                                                           Homologação       Produção
          •   Criação dos campos que representam os valores líquidos de impostos
 1.00
          •   Exceção nas regras de validação de alíquotas para o ambiente de
              homologação
          •   Ajuste na regra do valor total do DFe
          •   Criação do Campo de previsão do ICMS para antecipação de pagamento
          •   Eliminação da EPEC e FSDA
          •   Criação da emissão offline
          •   Evento de apropriação do crédito presumido pelo tomador do serviço
              prestado por TAC
          •   Alteração estrutura CTe Simplidicado
          •   Ajuste na Data de produção da NT 2026.004 e ajuste nas regras de
 1.01                                                                                      Até 26/10/2026   14/12/2026
              validação da EPEC
          •   Alteração da estrutura do CTe Simplificado
          •   A regra do valor total do DFe retorna a soma de IBS e CBS a partir de 2027
          •   Retirada orientação de inclusão de IBS e CBS na composição do vTPrest
          •   Inclusão do grupo de informações de Multa e Juros do CTe
```

## 1 Introdução

```text
Criação de campos para o valor líquido do produto

Com o objetivo de ampliar a transparência na formação do preço da operação, foi criado o campo Valor Líquido
da Prestação. Esse campo permite identificar o valor da prestação do serviço antes da incorporação dos tributos
vigentes que compõem o preço final, possibilitando distinguir, de forma clara, o valor líquido dos valores tributários
agregados ao preço.

A medida busca preservar a rastreabilidade da formação do valor informado no DFe, especialmente diante da
sistemática do IBS e da CBS.

Dessa forma, o novo campo permite evidenciar o valor líquido total da prestação do serviço, proporcionando maior
transparência ao contribuinte, ao adquirente e às Administrações Tributárias quanto à composição do preço e à
participação dos tributos no valor final da prestação.

O IBS e a CBS são tributos calculados por fora, não integrando suas próprias bases de cálculo. A base de cálculo
dos tributos deverá ser determinada de acordo com a legislação aplicável. Desta forma:
    •     No campo vPrestLiq deve ser informado o valor líquido do serviço, sem qualquer tributo;
    •     No campo vPrest deve ser informado o valor total do serviço, desconsiderados os valores de IBS e CBS;
No total do documento fiscal:
    •     No campo vTotDFe deve ser informado o valor correspondente a soma do vTPrest + IBS + CBS.

Criação de campo para informar o ICMS previsto

O novo campo “Valor do ICMS Previsto no Pagamento Antecipado” (tag: vICMSPrevisto) deverá ser informado
quando o documento fiscal emitido for referente a um pagamento realizado antes do fornecimento. O objetivo do
campo é permitir a correta tributação do IBS e da CBS no pagamento antecipado, com a identificação do valor do
ICMS que incidirá no momento do fornecimento futuro.
```

## 2 Alterações no Leiaute do DFe

```text
    Valor Líquido da Prestação do Serviço de Transporte sem tributos

    CTe e CTeOS
#       Campo                 Ele   Pai                      Tipo   Ocor.   Tam.    Descrição/Observação
...     vPrest                G     infCte                   -      1-1     -       Valores da Prestação de Serviço

        vTPrest               E     vPrest                   N      1-1     13v2    Valor Total da Prestação do Serviço

                                                                                    Observação: A partir 2027, os valores de IBS e
                                                                                    CBS compõem o Valor Total da Prestação
        vTPrestLiq            E     vPrest                   N      0-1     13v2    Valor Líquido total da Prestação SEM tributos

    CTeSimp
#       Campo                 Ele   Pai                      Tipo   Ocor.   Tam.    Descrição/Observação
...     det                   G     infCte                   -      1-999   -       Detalhamento das entregas / prestações do CTe
                                                                                    Simplificado
...

        vPrest                E     det                      N      1-1     13v2    Valor da Prestação do Serviço
                                                                                    Observação: A partir 2027, os valores de IBS e
                                                                                    CBS compõem o Valor Total da Prestação
        vPrestLiq             E     vPrest                   N      0-1     13v2    Valor Líquido da Prestação SEM tributos

        Grupo Totais do CTe Simplificado
   #        Campo                Ele    Pai                          Tipo     Ocor.        Tam.         Descrição/Observação
           vTPrest               E      total                        N        1-1          13v2         Valor Total da Prestação do Serviço

           vTPrestLiq            E      total                        N        0-1          13v2         Valor Total Líquido da Prestação do Serviço sem
                                                                                                        tributos

        Validações do total líquido
Regra de Validação                                          Aplic.       cStat      Efeito        Mensagem
Total Líquido da Prestação sem tributos (tag:               Obrig.       1054       Rej.          Rejeição: Total Líquido da prestação sem tributos
total\vTPrestLiq) difere do somatório do valor líquido da                                         difere do somatório dos itens
prestação sem tributos declarada nos itens (vPrestLiq).

        Criação de campo para informar o ICMS Previsto Pagamento Antecipado
        O novo campo 'ICMS Previsto Pagamento Antecipado' deverá ser informado quando o documento fiscal emitido
        for referente a um pagamento realizado antes do fornecimento. O objetivo do campo é permitir a correta tributação
        do pagamento antecipado, com a identificação do valor do ICMS que incidirá no momento do fornecimento futuro.
  #       Campo                          Ele    Pai                                   Tipo        Ocor.     Tam.    Descrição/Observação
  ...
          gICMSPrevistoPagtoAntecip      CG     imp/ICMS                              G           0-1       -       Grupo utilizado exclusivamente na
                                                                                                                    determinação da BC de IBS e CBS em
                                                                                                                    cenários específicos de pagamento
                                                                                                                    antecipado, informar nas hipóteses:
                                                                                                                       - tpPagAnt = 1 - Pagamento
                                                                                                                    Antecipado
                                                                                                                      - tpOperGov = 4-Recebimento do
                                                                                                                    pagamento com fornecimento
                                                                                                                    posterior.
          vICMSPrevisto                  E      gICMSPrevistoPagtoAntecip             E           1-1       13v2    Valor do ICMS a incidir no momento do
                                                                                                                    fornecimento futuro.
                                                                                                                    Observação: Em cenários onde não há
                                                                                                                    valor de ICMS devido, informar 0.

        Validações do ICMS Previsto em Pagamento Antecipado
  Regra de Validação                                         Aplic.         cStat     Efeito       Mensagem
  Se o DFe não for de compra governamental ou de             Obrig.         1051      Rej.         Rejeição: Grupo do ICMS Previsto no Pagamento
  pagamento antecipado:                                                                            Antecipado informado indevidamente
  - Grupo ICMSPrevistoPagtoAntecip não deve ser
  informado
  Se DFe for de compra governamento ou de pagamento          Obrig.         1052      Rej.         Rejeição: Grupo do ICMS Previsto no Pagamento
  antecipado:                                                                                      Antecipado informado indevidamente
  - Se tipo pagamento antecipado (tpPagAnt) for
  DIFERENTE de: 1 - Pagamento Antecipado
  E
  - Se tipo de operação (tpOperGov) com ente
  governamental for DIFERENTE de 4-Recebimento do
  pagamento com fornecimento posterior
  E informado Grupo ICMSPrevistoPagtoAntecip
  Se DFe for de compra governamento ou de pagamento          Obrig.         1053      Rej.         Rejeição: Grupo do ICMS Previsto no Pagamento
  antecipado:                                                                                      Antecipado DEVE SER informado
  - Se tipo pagamento antecipado (tpPagAnt) for IGUAL
  a 1 - Pagamento Antecipado
  OU
  - Se tipo de operação (tpOperGov) com ente
  governamental for IGUAL de 4-Recebimento do
  pagamento com fornecimento posterior
  E NÃO informado Grupo ICMSPrevistoPagtoAntecip
  Observação:
  Implantação em homologação em 01/02/2027.
  Implantação em produção em 01/03/2027.

      Criação do Grupo de informações da Multa e Juros no CTe (aplicável a CTe, CTeOS e
      CTeSimp)
      O novo grupo de informações deverá ser utilizado para lançar um CTe com multa e juros referente a um CTe
      emitido anteriormente. O CTe de multa e juros deverá apresentar os mesmos dados do CTe referenciado. A
      tributação do IBS e CBS deverá ser somente o complemento que representa a multa e o juros e o ICMS deverá
      ser declarado com CST 41.
#       Campo                       Ele    Pai                     Tipo    Ocor.     Tam.     Descrição/Observação
...
        gMultaJuros                 G      Ide                     G       0-1       -        Grupo de informações de multa e juros

        chCTeRef                    E      gMultaJuros             E       1-1       44       Chave de acesso do CTe de referenciado

      Validações da Multa e Juros
Regra de Validação                                       Aplic.    cStat    Efeito       Mensagem
Se informado grupo de Multa e Juros do CTe:              Obrig.    1072     Rej.         Rejeição: CTe de multa e juros não pode ser
                                                                                         tributado pelo ICMS
- O CST do ICMS informado deverá ser 41 (grupo
ICMS45)
Se informado grupo de Multa e Juros do CTe:              Obrig.    1073     Rej.         Rejeição: Chave de acesso do CTe referenciado em
- Validar chave de acesso do CTe Referenciado                                            Multa e Juros inválida

Retornar a primeira chave inválida e o motivo da
rejeição da Chave de Acesso: CNPJ zerado ou
inválido, Ano < 2009 ou maior que atual, Mês inválido
(0 ou > 12), Modelo diferente de 57/67, Número
zerado, Tipo de emissão inválido, UF inválida ou DV
inválido)
[chCTe:
99999999999999999999999999999999999999999999
][Motivo: XXXXXXXXXXXX]

Observação: No CTeOS essa regra deve validar
modelo 67, no CTe e CTe Simplificado deve validar
modelo 57
Se informado grupo de Multa e Juros do CTe:              Facult.   1074     Rej.         Rejeição: CTe referenciado em Multa e Juros
- Acessar BD CHAVES CTE (Chave: UF, CNPJ Emit,                                           inexistente na base de dados da SEFAZ
Modelo, Série, Nro):                                                                     [chCTe:
   - O CTe referenciado (chCTeRef) deve existir                                          999999999999999999999999999999999999999999
                                                                                         99]

Se informado grupo de Multa e Juros do CTe:              Facult.   1075     Rej.         Rejeição: CTe referenciado em Multa e Juros existe
                                                                                         com diferença de chave de acesso
-Acessar BD CHAVES CTE (Chave: UF, CNPJ Emit,                                            [chCTe:
Modelo, Série, Nro):                                                                     999999999999999999999999999999999999999999
  - O CTe referenciado (chCTeRef) não pode existir                                       99]
com diferença de chave de acesso                                                         [nProt:999999999999999][dhAut: AAAA-MM-
                                                                                         DDTHH:MM:SS TZD]
Se informado grupo de Multa e Juros do CTe:              Facult.   1076     Rej.         Rejeição: CTe referenciado em Multa e juros não
                                                                                         pode estar cancelado
-Acessar BD CHAVES CTE (Chave: UF, CNPJ Emit,
Modelo, Série, Nro):
  - O CTe referenciado (chCTeRef) não pode estar
cancelados

Se informado grupo de Multa e Juros do CTe:              Facult.   1077     Rej.         Rejeição: CTe referenciado em Multa e juros não
-Acessar BD CHAVES CTE (Chave: UF, CNPJ Emit,                                            pode estar substituído
Modelo, Série, Nro):
  - O CTe referenciado (chCTeRef) não pode estar
substituído

Se informado grupo de Multa e Juros do CTe:              Obrig.    1078     Rej.         Rejeição: O emitente do CTe referenciado deve ser
                                                                                         o mesmo do CTe de Multa e Juros
O Emitente do CTe referenciado em multa e juros deve
ser igual ao emitente do CTe de Multa e Juros
Se informado grupo de Multa e Juros do CTe:              Obrig.    1079     Rej.         Rejeição: O tomador do CTe referenciado deve ser
O Tomador do CTe referenciado em multa e juros deve                                      o mesmo do CTe de Multa e Juros
ser igual ao tomador do CTe de Multa e Juros

Observação: o indicador do tomador (toma/toma4)
também deve ser o mesmo

   Se informado grupo de Multa e Juros do CTe:              Obrig.         1080      Rej.        Rejeição: Início e fim de prestação do CTe
                                                                                                 referenciado em Multa e Juros deve ser o mesmo do
   As UF de início e fim da prestação devem ser as                                               CTe de Multa e Juros
   mesmas do CTe de Multa e Juros e do CTe
   referenciado

   Observação: Quando as UF´s estiverem informadas
   nos 2 CTe
   Se informado grupo de Multa e Juros do CTe:              Obrig.         1081      Rej.        Rejeição: Classificação tributária do CTe
                                                                                                 referenciado deve ser a mesma do CTe de Multa e
   O CST e o cClassTrib do grupo IBSCBS deve ser o                                               Juros
   mesmo do CTe referenciado

   Observação: Regra aplicável a CTe e CTeOS, para o
   CTe Simplificado não validar
   Se informado grupo de Multa e Juros do CTe:              Obrig.         1082      Rej.        Rejeição: Tipo de CTe do CTe referenciado deve
                                                                                                 ser o mesmo do CTe de Multa e Juros
   O tipo de CTe do CTe referenciado deve ser o mesmo
   do CTe de Multa e Juros

   Se informado grupo de Multa e Juros do CTe:              Obrig.         1083      Rej.        Rejeição: Tipo de Serviço do CTe referenciado deve
                                                                                                 ser o mesmo do CTe de Multa e Juros
   O tipo de Serviço do CTe referenciado deve ser o
   mesmo do CTe de Multa e Juros
```

## 3 Validações dos campos do IBS e CBS

```text
Regra de Validação                                       Aplic.      cStat        Efeito     Mensagem
Se informado grupo IBS de competência das Unidades       Obrig.      316          Rej.      Rejeição: Alíquota do IBS da UF inválida
Federadas (gIBSUF):
A alíquota de IBS da UF (pIBSUF) deverá ser:
      •   0,1% para documento com data de emissão
          no ano de 2026. (Art. 343 da LC 214/25)
      •   0.05% para documento com data de emissão
          no ano de 2027 e 2028. (Art. 344 da LC
          214/25)
      •   Alíquota de referência ou específica da UF a
          ser publicada para anos posteriores a 2028.
Exceção: Se o cClassTrib possuir indicador de
tributação regular o pIBSUF deve ser igual a zero

EXCEÇÂO: Em 2026 será permitido informar as
alíquotas de 2026 e 2027 APENAS no AMBIENTE DE
HOMOLOGAÇÃO (tpAmb=2) viabilizando testes das
empresas.
Se informado grupo IBS de competência dos                Obrig.      321          Rej.       Rejeição: Alíquota do IBS do Município inválida
Municípios (gIBSMun):
A alíquota de IBS Municipal deverá ser:
      •   0% para documento com data de emissão no
          ano de 2026. (Art. 343 da LC 214/25)
      •   0.05% para documento com data de emissão
          no ano de 2027 e 2028. (Art. 344 da LC
          214/25)
      •   Alíquota de referência ou específica do
          Município a ser publicada para anos
          posteriores a 2028
Exceção: Se o cClassTrib possuir indicador de
tributação regular o pIBSMun deve ser igual a zero

EXCEÇÂO: Em 2026 será permitido informar as
alíquotas de 2026 e 2027 APENAS no AMBIENTE DE
HOMOLOGAÇÃO (tpAmb=2) viabilizando testes das
empresas.
VÁLIDA PARA 2026:                                        Obrig.       326          Rej.               Rejeição: Alíquota da CBS inválida
Se informado grupo CBS (gCBS), a alíquota de CBS
deverá ser de 0,90 % para documento com data de
emissão no ano de 2026. (Art. 346 da LC 214/25)
Exceção: Se o cClassTrib possuir indicador de
tributação regular o pCBS deve ser igual a zero

Exceção 2: A Alíquota da CBS (tag: pCBS) pode ser
igual a zero quando as condições abaixo forem
atendidas:
- Código de Classificação do Produto (cClass) permitir
alíquota zero para CBS em zona incentivada.
- Município do Fato Gerador (cMunFG) e emitente
devem pertencer a um município da ZFM
Cod. IBGE Nome Município
1302603 Manaus
1303569        Rio Preto da Eva
1301902        Itacoatiara
OU
- Município do Fato Gerador (cMunFG) e Município do
Emitente devem estar localizados nos municípios pares
da mesma ALC.
ALC
             Município Início                Município Fim
 1
      1304062-Tabatinga (AM)         1304062-Tabatinga (AM)
 2
      1100106-Guajará-Mirim (RO)     1100106-Guajará-Mirim (RO)
 3
      1400100-Boa Vista (RR)         1400100-Boa Vista (RR)

      1400100-Boa Vista (RR)         1400159-Bonfim (RR)

      1400159-Bonfim (RR)            1400100-Boa Vista (RR)

      1400159-Bonfim (RR)            1400159-Bonfim (RR)
 4
      1600303-Macapá (AP)            1600303-Macapá (AP)

      1600303-Macapá (AP)            1600600-Santana (AP)

      1600600-Santana (AP)           1600303-Macapá (AP)

      1600600-Santana (AP)           1600600-Santana (AP)
 5
      1200104-Brasileia (AC)         1200104-Brasileia (AC)

      1200104-Brasileia (AC)         1200252-Epitaciolândia (AC)

      1200104-Brasileia (AC)         1200203-Cruzeiro do Sul (AC)

      1200252-Epitaciolândia (AC)    1200104-Brasileia (AC)

      1200252-Epitaciolândia (AC)    1200252-Epitaciolândia (AC)

      1200252-Epitaciolândia (AC)    1200203-Cruzeiro do Sul (AC)

      1200203-Cruzeiro do Sul (AC)   1200104-Brasileia (AC)

      1200203-Cruzeiro do Sul (AC)   1200252-Epitaciolândia (AC)

      1200203-Cruzeiro do Sul (AC)   1200203-Cruzeiro do Sul (AC)
Observação: As cores definem quais municípios são da
mesma área incentivada, e isto será observado na
regra de validação
EXCEÇÂO: Até que seja publicada a alíquota de
referência da CBS para 2027, deverá ser informada a
alíquota de 2026, inclusive para testes de simulação de
2027 no AMBIENTE DE HOMOLOGAÇÃO (tpAmb=2),
quando a alíquota de 2027 estiver publicada, ela
também será aceita para testes ainda em 2026
Se informado o indicador de Doação (indDoacao=1), o                 Obrig.   1055   Rej.   Rejeição: Doação com CNPJ/CPF do emitente igual
CNPJ-Base/CPF do emitente deve ser diferente do                                            do tomador do serviço
CNPJ-Base/CPF do tomador do serviço

Se o cClassTrib informado possuir indicador que VEDA                Obrig    1056   Rej.   Rejeição: O cClassTrib é incompatível com o campo
uso de doação, o campo indDoacao não pode ser                                              de indicador de doação preenchido
informado.

Se o cClassTrib informado possuir indicador que                     Obrig    1057   Rej.   Rejeição: O cClassTrib informado necessita que o
EXIGE indicação de doação, o campo indDoacao                                               indicador de doação seja preenchido
DEVE ser informado.
```

## 4 Total Geral do Documento Fiscal Eletrônico

```text
      #          Campo                Ele         Pai                     Tipo       Ocor.      Tam.        Descrição/Observação

      01         vTotDFe              E           imp (CTe/CTeOS) e        E           0-1        13,2        Valor total do documento fiscal
                                                  total (CTeSimp)
                                                                                                              vTPrest + total do IBS + total da CBS

#           Regra de Validação                                    Aplic.         cStat          Efeito     Mensagem

01          O total geral do DFe deverá ser INFORMADO com         Obrig.         365           Rej.      Rejeição: Total do DFe inválido
            a soma do total da prestação + IBS + CBS
            vTotDFe = vPrest/vTPrest + gIBSCBS/vIBS +
            gCBS/vCBS
            Exceção: Em 2026 não somar IBS e CBS, usando
            a fórmula:
            vTotDFe = vPrest/vTPrest
            O total geral do DFe deverá ser informado
            REPETINDO o valor de vTPrest
```

## 5 Alteração nas Formas de Emissão do CTe, CTeOS e CTe Simplificado

```text
             O tipo de emissão (tpEmis) deixa de aceitar o valor 5 – Contingência FSDA, por consequência, todas as regras de
             validação relacionadas a FSDA deixam de ser aplicadas.
             O evento EPEC deixa de ser aceito pelo ambiente de autorização, mas o CTe com tipo de emissão EPEC continua
             sendo recepcionado para que os eventos já registrados possam ser conciliados.
             Novo tipo de emissão Contingência OffLine (tpEmis=2) passa a ser aceito no CTe de forma imediata.
           Campo                 Ele        Pai                  Tipo       Ocor.        Tam.         Descrição/Observação

           tpEmis                 E         Ide                       E        1-1        1              Preencher com:
                                                                                                         1 - Normal;
                                                                                                         3 - Regime Especial NFF;
                                                                                                         2 - Contingência Offline;
                                                                                                         4 - EPEC pela SVC (em desativação);
                                                                                                         5 - Contingência FSDA;
                                                                                                         7 - Autorização pela SVC-RS;
                                                                                                         8 - Autorização pela SVC-SP
             Os eventos EPEC (110113) e Liberação de EPEC (24160) deixam de fazer parte da listagem de eventos aceitos
             no ambiente de autorização, se eventos destes tipos forem enviados, deverá ocorrer a rejeição de 629 - Rejeição:
             O tpEvento informado inválido.
             Todo bloco de especificação destes eventos fica revogado do MOC do CTe.

             Alteração em Regras de validação (Grupo G CTe / Grupo H CTeOS)
    G008      Se forma de emissão do CTe for diferente de 2                Obrig.        586      Rej     Rejeição: Data e Justificativa de entrada em
    H004      (Contingência OffLine) 5 (FS-DA):                                                   .       contingência não devem ser informadas para
              dhCont e xJust não devem ser informados                                                     tipo de emissão diferente de Contingência
                                                                                                          Offline FS-DA.
    G009      Se forma de emissão do CTe for igual a 2                     Obrig.        587      Rej     Rejeição: Data e Justificativa de entrada em
    H005      (Contingência OffLine) 5 (FS-DA):                                                   .       contingência devem ser informadas
              dhCont e xJust devem ser informados
    G008a     Com a mudança de schema impedindo FSDA a regra               Obrig         928      Rej     Rejeição: Tipo de emissão FS-DA não é
    H004a     fica obsoleta:                                                                      .       permitido
              Rejeitar tipo de emissão (tag:tpEmis) igual a 5 (FS-
              DA)
              Exceção: A exceção permite-se uso do FS-DA para
              CTe emitidos da SEFAZ Minas Gerais
    G103      Se tipo de emissão for diferente de Contingência             Obrig.        228      Rej     Rejeição: Data de Emissão muito atrasada
    H077      OffLine (tpEmis=2) e EPEC (tpEmis=4):                                               .
              Data-Hora de Emissão com atraso superior a 168
              horas em relação ao horário de recepção na SEFAZ
              Autorizadora.
              Exceção: Esta regra mantem a redação somente para
              SEFAZ MG
              Exceção: CTe com Data de Emissão muito atrasada
              será aceito, desde que tenha sido emitido em

        contingência Off-Line (tag:tpEmis=2) ou EPEC. O CTe
        transmitido para a SEFAZ Autorizadora após o prazo
        de 168 horas deve retornar: cStat=”150- Autorizado
        Uso de CTe, autorização fora de prazo”.

        Exceção 2: Essa regra não será aplicada se
        informado grupo de Juros e Multa (gMultaJuros) ou
        grupo de Antecipação de Pagamento
        (gPagAntecipado)
G215    Se tipo de emissão for igual a Contingência OffLine     Obrig.    853     Rej   Rejeição: Parâmetro sign não informado no QR
H131    (tpEmis=2) ou EPEC (tpEmis=4):                                            .     Code para emissão em contingência
        O parâmetro sign deve informado no QR-Code
        Exceção: Esta regra mantem a redação somente para
        SEFAZ MG
G217    Se tipo de emissão for igual Contingência OffLine       Obrig.    855     Rej   Rejeição: Assinatura do QR-Code difere do
H133    (tpEmis=2) ou EPEC (tpEmis=4):                                            .     calculado
        Valor da assinatura (sign) do QR-Code difere do valor
        calculado
        Exceção: Esta regra mantem a redação somente para
        SEFAZ MG

       Alteração nas regras de validação de Eventos
N09     Se ambiente de Autorização SVC:                                  Obrig.   530     Rej.     Rejeição: Se ambiente SVC, rejeitar
                                                                                                   eventos diferentes de EPEC,
        - Rejeitar se Tipo de Evento for diferente de EPEC (110113) ou                             Liberação EPEC e Cancelamento
        Cancelamento (110111)
```

## 6 Mudança na estrutura do CTe Simplificado

```text
Atualmente, o CTe Simplificado agrupa diversas prestações (viagens) para um único tomador, mas com a
tributação do IBS e da CBS centralizada no corpo do documento (imp/IBSCBS). Esta NT propõe descentralizar
essas informações para o nível de item (det/nItem), possibilita-se que cada viagem ou trecho tenha sua própria
situação tributária, alíquota efetiva ou classificação tributária no contexto da Reforma Tributária, mantendo os
dados de ICMS centralizados no documento.
A razão para a mudança é ampliar o alcance do CTe Simplificado, como originalmente ele foi projetado. Como o
IBS e a CBS são calculados e destinados com base no local de término da prestação de serviços, centralizar a
tributação no cabeçalho criou um gargalo técnico: o sistema autorizador precisava de um destino unificado para
validar e destinar o tributo de forma correta. Por esse motivo, o fisco foi obrigado a criar a regra de validação
G101a (Rejeição 370), que estabelece:
    •     “O município de fim de prestação em todos os itens do CTe Simplificado (det:cMunFim) devem ser iguais”.
Essa restrição reduziu drasticamente a utilidade do CTe Simplificado, forçando o transportador a emitir documentos
diferentes para cada município de destino, mesmo que o tomador do serviço fosse o mesmo.
Ao realocar o grupo de IBS e CBS no detalhamento das viagens, o CTe pode ser utilizado novamente para retratar
prestações com diversos destinos, mantendo a ideia de único tomador do serviço.

         Alterações nas regras de validação do CTe Simplificado

         Com a mudança da localização do grupo IBSCBS, as regras de validação previstas nas NTs da Reforma Tributária
         passam a atuar neste tipo de CTe no nível do item (det), em caso de rejeição deverá ser retornado o [nItem] em
         que foi detectada a rejeição.
         Revoga-se a regra de validação:
G101a       O município de fim de prestação em todos os itens do   Obrig.     370       Rej.   Rejeição: O CTe Simplificado deve ter a
            CTe Simplificado (det:cMunFim) devem ser iguais                                    prestação terminada em apenas um
                                                                                               município

         Alteração no grupo total do CTe Simplificado

         Deverá ser adicionado ao grupo de totais do CTe Simplificado, um grupo de totalização do IBS/CBS
         em relação ao declarado nos itens (det).
   #        Campo                  Ele   Pai                       Tipo     Ocor.   Tam.       Descrição/Observação

   ...

   #        IBSCBSTot              G     total                         -    0-1     -          Grupo de informações para apuração do IBS e
                                                                                               CBS declarado pelo contribuinte
   1        vBCIBSCBS              E     IBSCBSTot                 N        1-1     13,2       Total da Base de cálculo do IBS/CBS

   2        gIBS                   G     IBSCBSTot                 -        1-1     -          Totalização do IBS

   3        gIBSUF                 G     gIBS                      -        1-1     -          Totalização do IBS de competência da UF

   4        vDif                   E     gIBSUF                    N        1-1     13,2       Total do Diferimento

   5        vDevTrib               E     gIBSUF                    N        1-1     13,2       Total de Devolução de Tributo IBS UF

   6        vIBSUF                 E     gIBSUF                    N        1-1     13,2       Total do IBS UF

   7        gIBSMun                G     gIBS                      -        1-1     -          Totalização do IBS de competência Municipal

   8        vDif                   E     gIBSMun                   N        1-1     13,2       Total do Diferimento

   9        vDevTrib               E     gIBSMun                   N        1-1     13,2       Total de Devolução de Tributo IBS Municipal

   10       vIBSMun                E     gIBSMun                   N        1-1     13,2       Total do IBS Municipal

   11       vIBS                   E     gIBS                      N        1-1     13,2       Total do IBS (IBS UF + IBS Mun)

   14       gCBS                   G     IBSCBSTot                 -        1-1     -          Total do CBS

   15       vDif                   E     gCBS                      N        1-1     13,2       Total do Diferimento

   16       vDevTrib               E     gCBS                      N        1-1     13,2       Total de Devolução do tributo CBS

   17       vCBS                   E     gCBS                      N        1-1     13,2       Total do CBS

      18    gEstornoCred           G      IBSCBSTot                 -     0-1    -             Total do Estorno de crédito

      19    vIBSEstCred            E      gEstornoCred              N     1-1    13,2          Total do Estorno de crédito IBS

      20    vCBSEstCred            E      gEstornoCred              N     1-1    13,2          Total do Estorno de crédito CBS

       Regras de Validação do Grupo de Totais IBS e CBS no CTe Simplificado
#          Regra de Validação                                   Aplic.   cStat       Efeito     Mensagem

001        O grupo de totais do IBS e CBS (IBSCBSTot) só        Obrig.   348         Rej.       Rejeição: Total de IBS/CBS só deve ser informado
           deve ser informado se existir pelo menos uma                                         se existir IBS/CBS declarado nos itens do DFe
           ocorrência de IBS/CBS nos itens

002        O grupo de totais do IBS e CBS (IBSCBSTot)           Obrig.   349         Rej.       Rejeição: Total de IBS/CBS deve ser informado se
           deve ser informado se existir pelo menos uma                                         existir IBS/CBS declarado nos itens do DFe
           ocorrência de IBS/CBS nos itens

003        O total do Diferimento do IBS UF deverá ser a        Obrig.   350         Rej.       Rejeição: Total de Diferimento do IBS UF difere da
           soma do campo vDif do IBS UF informados nos                                          soma dos itens
           itens

004        O total Devolvido do IBS UF deverá ser a soma do     Obrig.   351         Rej.       Rejeição: Total Devolvido do IBS UF difere da soma
           campo vDevTrib do IBS UF informados nos itens                                        dos itens

005        O total do IBS UF deverá ser a soma do campo         Obrig.   352         Rej.       Rejeição: Total de IBS UF difere da soma dos itens
           vIBSUF informados nos itens
006        O total do Diferimento do IBS Municipal deverá ser   Obrig.   353         Rej.       Rejeição: Total de Diferimento do IBS Municipal
           a soma do campo vDif do IBS Municipal                                                difere da soma dos itens
           informados nos itens
007        O total Devolvido do IBS Municipal deverá ser a      Obrig.   354         Rej.       Rejeição: Total Devolvido do IBS Municipal difere da
           soma do campo vDevTrib do IBS Municipal                                              soma dos itens
           informados nos itens
008        O total do IBS Municipal deverá ser a soma do        Obrig.   355         Rej.       Rejeição: Total de IBS Municipal difere da soma dos
           campo vIBSMun informados nos itens                                                   itens

009        O Total do IBS deverá ser a soma do IBS das UF       Obrig.   356         Rej.       Rejeição: Total do IBS difere da soma do IBS UF e
           e do IBS Municipal (vIBSUF + vIBSMun)                                                IBS Municipal

010        O total do Diferimento do CBS deverá ser a soma      Obrig.   357     Rej.         Rejeição: Total de Diferimento do CBS difere da soma
           do campo vDif do CBS informados nos itens                                          dos itens

011        O total Devolvido do CBS deverá ser a soma do        Obrig.   358     Rej.         Rejeição: Total Devolvido do CBS difere da soma dos
           campo vDevTrib do CBS informados nos itens                                         itens

012        O total do CBS deverá ser a soma do campo vCBS       Obrig.   359     Rej.         Rejeição: Total de CBS difere da soma dos itens
           informados nos itens

013        Se informado grupo de estorno de crédito nos itens   Obrig.   305     Rej.         Rejeição: Total de IBS estornado difere da soma dos
           (gEstornoCred) o total do IBS estornado deverá                                     itens
           ser igual a soma campo valor do IBS estornado
           nos itens (gEstornoCred/vIBS)

014        Se informado grupo de estorno de crédito nos itens   Obrig.   306     Rej.         Rejeição: Total de CBS estornada difere da soma dos
           (gEstornoCred) o total da CBS estornada deverá                                     itens
           ser igual a soma campo valor da CBS estornada
           nos itens (gEstornoCred/vCBS)
```

## 7 Evento de Apropriação do Crédito Presumido

```text
Função: Evento a ser gerado pelo tomador do serviço de transporte realizado por:
      •    Transportador Autônomo de Cargas (TAC) em CTe com tipo de emissão Nota Fiscal Fácil (tpEmis=3)
           ou Emissão pelo PAA (procEmi=4)
          •   Transportador MEI (CRT=4)

Autor do Evento: Tomador do Serviço do CTe emitido pelo TAC (NFF ou PAA) e pelo MEI (CRT=4)

Modelo: CTe (modelo 57)

Código do Tipo de Evento: 211110 (Este serviço exige CTe autorizado)

Autorização do Evento: Exclusiva no ambiente da SVRS

Schema: evApropriaCredPres.xsd
#   Campo                 Ele    Pai                  Tipo   Ocor.   Tam.    Descrição/Observação
#   evApropriaCredPres    Raiz   detEvento            G      1-1             Schema XML de validação do evento de 211110

    descEvento            E      evApropriaCredPres   C      1-1     29      Apropriação Credito Presumido

    vBCCredPres           E      evApropriaCredPres   N      1-1     13v2    Valor da base de cálculo do item
                                                                             Valor total da base de cálculo da operação do
                                                                             crédito presumido
                                                                             Valor total do crédito presumido do IBS. Informar
                                                                             zero quando não houver crédito presumido de
                                                                             IBS.
                                                                             Valor total do crédito presumido da CBS. Informar
                                                                             zero quando não houver crédito presumido de
                                                                             CBS.

    cCredPres             E      evApropriaCredPres   N      1-1     2       Código de Classificação do Crédito presumido,
                                                                             conforme tabela cCredPres (Anexo IV)

    gIBSCredPres          G      evApropriaCredPres   G      0-1             Grupo de Informações do Crédito Presumido do
                                                                             IBS

    pCredPres             E      gIBSCredPres         N      1-1     3v2-4   Percentual do Crédito Presumido

    vCredPres             E      gIBSCredPres         N      1-1     13v2    Valor do Crédito Presumido

    gCBSCredPres          G      evApropriaCredPres   G      0-1             Grupo de Informações do Crédito Presumido da
                                                                             CBS

    pCredPres             E      gCBSCredPres         N      1-1     3v2-4   Percentual do Crédito Presumido

    vCredPres             E      gCBSCredPres         N      1-1     13v2    Valor do Crédito Presumido

    xDecPag               E      evApropriaCredPres   C      0-1     -       Declaração de Pagamento ao TAC/MEI.
                                                                              Preencher conforme exigência do indicador
                                                                             ind_xDecPag da tabela cCredPres, mediante o
                                                                             uso de um dos literais apresentados a seguir:
                                                                             “Declaro, para fins de apropriação do crédito
                                                                             presumido solicitado, relativo à operação
                                                                             registrada no documento fiscal eletrônico a que se
                                                                             refere este evento: I – já ter efetuado o pagamento
                                                                             integral do valor da prestação do serviço ao
                                                                             transportador, nos termos do art. 126, § 5º, II, da
                                                                             Lei Complementar nº 214, de 16 de janeiro de
                                                                             2025; II – estar ciente de que a prestação de
                                                                             declaração falsa sujeita-me às penalidades
                                                                             administrativas e sanções penais previstas na
                                                                             legislação, sem prejuízo do estorno do crédito
                                                                             indevidamente apropriado com os acréscimos
                                                                             legais.” (texto com acentuação)
                                                                             ou
                                                                             “Declaro, para fins de apropriacao do credito
                                                                             presumido solicitado, relativo a operacao

                                                                                     registrada no documento fiscal eletronico a que se
                                                                                     refere este evento: I – ja ter efetuado o pagamento
                                                                                     integral do valor da prestacao do servico ao
                                                                                     transportador, nos termos do art. 126, paragrafo
                                                                                     5o, II, da Lei Complementar no 214, de 16 de
                                                                                     janeiro de 2025; II – estar ciente de que a
                                                                                     prestacao de declaracao falsa sujeita-me as
                                                                                     penalidades administrativas e sancoes penais
                                                                                     previstas na legislacao, sem prejuizo do estorno
                                                                                     do credito indevidamente apropriado com os
                                                                                     acrescimos legais.” (texto sem acentuação)

#      Regra de Validação                                    Aplic    cStat   Efeito     Mensagem
01     Verificar se o nSeqEvento é maior que o valor         Obrig.   636     Rej.       Rejeição: O número sequencial do
       permitido (1)                                                                     evento é maior que o permitido
02     Verificar se CTe já está cancelado                    Obrig.   218     Rej.       Rejeição: CTe já está cancelado na
                                                                                         base de dados da SEFAZ
                                                                                         [nProt:999999999999999][dhCanc:
                                                                                         AAAA-MM-DDTHH:MM:SS TZD].
03     Verificar se CTe possui CTe de substituição           Obrig.   664     Rej.       Rejeição: Evento não permitido
       associado                                                                         para CTe Substituído
04     - Verificar se o CNPJ/CPF do Autor é diferente do     Obrig.   755     Rej.       Rejeição: Autor do evento deve ser
       CNPJ/CPF do tomador do CTe                                                        o tomador do serviço do CTe
05     Verificar se o CTe é do tipo de emissão Nota Fiscal   Obrig.   1060    Rej.       Rejeição: Apropriação de crédito
       Fácil (tpEmis=3), gerado pelo Provedor de                                         presumido permitida apenas para
       Assinatura e Autorização – PAA (procEmi=4) ou se                                  CTe emitido por TAC ou MEI.
       o CRT informado pelo emitente é igual a MEI
       (CRT=4)
06     O código de crédito Presumido informado deve          Obrig.   1061    Rej.       Rejeição: Código de Crédito
       existir                                                                           Presumido (cCredPres) inexistente
       Observação: Consultar tabela de Crédito
       Presumido do IBS e da CBS.
07     O cCredPres informado deve permitir apropriação       Obrig.   1062    Rej.       Rejeição: Código de Crédito
       via evento                                                                        Presumido (cCredPres) não aceita
                                                                                         apropriação por evento
08     O cCredPres informado deve possuir indicador de       Obrig,   1063    Rej.       Rejeição: Código de Crédito
       utilização com CTe                                                                Presumido (cCredPres) não
                                                                                         permitido para CTe
09     Se cCredPres possui indicador que NÃO                 Obrig.   1064    Rej.       Rejeição: Crédito Presumido para o
       PERMITE o uso de crédito presumido para o IBS,                                    IBS informado indevidamente
       o grupo gIBSCredPres NÃO DEVE ser informado.
10     Se cCredPres possui indicador que EXIGE o uso         Obrig,   1065    Rej.       Rejeição: Crédito Presumido para o
       de crédito presumido para o IBS, o grupo                                          IBS não informado
       gCredPresIBS DEVERÁ SER INFORMADO
11     Se informado gIBSCredPres:                            Obrig,   1066    Rej.       Rejeição: Valor do crédito
        - O valor de gIBSCredPres/vCredPres deve                                         presumido do IBS difere do
       corresponder ao resultado de vBCCredPres                                          calculado
       multiplicado por gIBSCredPres/pCredPres.
       Observação: Aceitar uma tolerância de 0,01 a
       mais ou a menos.
12     Se cCredPres possui indicador que NÃO                 Obrig.   1067    Rej.       Rejeição: Crédito Presumido para a
       PERMITE o uso de crédito presumido para o CBS,                                    CBS informado indevidamente
       o grupo gCBSCredPres NÃO DEVE ser informado.
13     Se cCredPres possui indicador que EXIGE o uso         Obrig.   1068    Rej.       Rejeição: Crédito Presumido para a
       de crédito presumido para o CBS, o grupo                                          CBS não informado
       gCredPresCBS DEVERÁ SER INFORMADO
14     Se informado gCBSCredPres:                            Obrig,   1069    Rej.       Rejeição: Valor do crédito
        - O valor de gCBSCredPres/vCredPres deve                                         presumido da CBS difere do
       corresponder ao resultado de vBCCredPres                                          calculado
       multiplicado por gCBSCredPres/pCredPres.
       Observação: Aceitar uma tolerância de 0,01 a
       mais ou a menos.
15     Se o cCredPres possuir indicador que EXIGE o          Obrig.   1070    Rej.       Rejeição: Declaração de
       preenchimento da Declaração de Pagamento ao                                       Pagamento ao Fornecedor não
       Fornecedor:                                                                       informada
       A Declaração de Pagamento ao Fornecedor
       DEVERÁ SER informada. (campo: xDecPag)

16   Se o cCredPres possuir indicador que NÃO            Obrig.   1071   Rej.     Rejeição: Declaração de
     PERMITE o preenchimento da Declaração de                                     Pagamento ao Fornecedor
     Pagamento ao Fornecedor:                                                     informada indevidamente
     A Declaração de Pagamento ao Fornecedor NÃO
     DEVERÀ SER INFORMADA. (campo: xDecPag)

 Final do Processamento

 Se o evento de apropriação de crédito presumido do DFe for homologado o status de retorno deverá ser cStat=135.
```
