---
titulo: "Nota Técnica CT-e nº 2025.001-RTC, versão 1.14b, de 30 de abril de 2026 (Leiaute base da Reforma Tributária do Consumo no CT-e)"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil / ENCAT - CONFAZ"
tipo: "Nota Técnica"
numero: "2025.001"
data: "2026-04-30"
ano: "2026"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.cte.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=Y0nErnoZpsg="
ementa: "Nota técnica de adequação dos leiautes do CT-e, do CT-e OS e da GTV-e à Reforma Tributária do Consumo (IBS e CBS), com as regras de validação."
data_consulta: "2026-11-27"
versao_texto: "Versão 1.14b (PDF oficial, 30/04/2026)"
---

# Nota Técnica CT-e nº 2025.001-RTC, versão 1.14b, de 30 de abril de 2026 (Leiaute base da Reforma Tributária do Consumo no CT-e)

> **Nota editorial.** Texto extraído da camada de texto do PDF oficial da Nota Técnica 2025.001, versão 1.14b, divulgado no Portal Nacional do CT-e (21 páginas), consultado em 27/11/2026. A data do documento (30/04/2026) é a de publicação da versão, lida na lista de Notas Técnicas do portal. Nenhum Ato Técnico Conjunto do acervo fixa esta versão. Foram removidos a capa, o sumário, os cabeçalhos e rodapés repetidos e a numeração de página. Os 19 títulos de primeiro nível do sumário viraram seções e o texto de cada uma, com os quadros e os leiautes, ficou em bloco de texto que mantém as colunas do PDF. Figuras e imagens do PDF não foram convertidas. Em caso de dúvida, prevalece o PDF. O portal só entrega o PDF com cookie de sessão; o link da fonte é a página de lista de Notas Técnicas, onde a versão consta como "Publicada em 30/04/2026". É a última versão da série 2025.001 do CT-e na lista do portal. Alterações posteriores do leiaute constam da NT 2026.004 do CT-e (`reforma-tributaria/documentos-fiscais-eletronicos/nota-tecnica-cte-2026-004-v1-01-reforma-tributaria.md`).

## Histórico de Alterações / Cronograma

```text
Versão                             Histórico de atualizações                            Implantação   Implantação
                                                                                       Homologação     Produção
 1.00     •   Previsão das informações do IBS/CBS no CTe
          •   Alteração de regras do CTeOS Transporte Valores exigir UF e Mun Fim
          •   Alteração das regras do CTe Simplificado para limitar em apenas um fim
              de prestação
          •   Alteração no leiaute do Dutoviário
          •   Exceção para não exigir evento de prestação em desacordo na
              substituição de tomador do EX
          •   Preparação das Expressões Regulares do CNPJ Alfa
          •   Eliminação da SVC para GTVe
          •   Inclusão da DCe nos documentos originários
          •   Ampliação do código de retorno das mensagens suportar até 4 dígitos
 1.01     •   Correções e orientações sobre aplicação das regras de validação
          •   Renumeração das regras de rejeição
          •   Ajuste no grupo de Tributação regular
          •   Ajuste na regra do CTe Complementar para Multimodal
 1.02     •   Ajustes nas regras do crédito presumido e tributação regular
          •   Ajuste nas regras para Crédito Presumido Condição Suspensiva no
              grupo do crédito presumido
 1.03     •   Ajustes nas regras de compras governamentais, redução de alíquota e
              valores de IBS/CBS
          •   Correção no schema dos eventos tipos básicos
 1.04     •   Ajustes em regras de validação e mensagens
 1.05     •   Ajuste na regra de compras governamentais e exigência do grupo de
              tributação para SN
          •   Novo grupo de informações da tributação para compras governamentais
1.05 a    •   Correção de datas no texto da introdução
 1.05b    •   Correção em nome de campos citados nas RVs
 1.06     •   Novas regras de validação complementares
          •   Inclusão do campo vIBS
          •   Ajuste na expressão regular do qrcode prevendo o CNPJ Alfa
 1.07     •   Campo vIBS passa a ser obrigatório no schema
 1.08     •   Alteração da regra de validação 004-a para verificar no cClassTrib sua
              aplicabilidade ao modelo de DFe
          •   Correção na posição do campo vIBS no schema
          •   Correção na obrigatoriedade das regras 038 e 044
1.08 a    •   Ajuste na redação da regra de total geral do DFe

1.09      •   Ajustes na regra do diferimento
          •   Altera data de exigência do grupo IBSCBS em homologação para 03/11
1.10      •   Exclusão do grupo de informações do crédito presumido por não se aplicar
              aos cClassTrib associados ao DFe
          •   Criação do indicador de doação e do grupo de Estorno de crédito vinculado
              a um novo indicador na tabela cClassTrib para esta finalidade
1.11a     •   Correção na regra de validação do CBS, permitindo alíquota zero para a CBS
              em operações específicas dentro de áreas incentivadas.

          •   Ajuste na explicação da regra de valor do tributo negativo

1.12      •   Esclarecimento do preenchimento do vTotDFe
1.12 a    •   Correção da validação da redução de alíquota                                 Já implantado   Já implantado
1.13      •   Criação de regra específica para exigir vTotDFe quando informado IBSCBS       03/02/2026      02/03/2026
1.14      •   Inclusão de campos do tipo de operação e DFe referenciado nas compras
              governamentais
1.14 a    •   Ajuste nas mensagens de validação das compras gov                             06/04/2026      04/05/2026
1.14b     •   Novas regra de validação para o CTe Aquaviário de cabotagem                   04/05/2026     Até 15/05/2026

Observação: No ambiente de produção, os campos ficam à disposição desde 20 de outubro, validados apenas se
informados. No ambiente de homologação os campos da reforma tributária estarão à disposição desde julho,
validados apenas se informados.
```

## 1 Introdução

```text
Com a promulgação da Lei Complementar nº 214/2025, foi definida, na Seção V - Disposições Transitórias,
Art. 62 I, a obrigatoriedade de que os Estados, o Distrito Federal e os Municípios adaptem os sistemas
autorizadores de Documentos Fiscais Eletrônicos (DFe) vigentes para a utilização de leiaute padronizado, de
modo a permitir que os contribuintes informem os dados relativos ao Imposto sobre Bens e Serviços (IBS), à
Contribuição sobre Bens e Serviços (CBS) e ao Imposto Seletivo (IS).

Diante disso, esta Nota Técnica substitui e complementa, no âmbito do CTe, a DFe - Nota Técnica 2024.001
- IBS/CBS v1.10, mantendo a data de implantação em ambiente de produção para 06/10/2025, de modo a viabilizar
sua efetiva operacionalização a partir de 05/01/2026.

A NT modifica o leiaute dos DFe, inserindo os grupos e campos opcionais relacionados a tributação do IBS, CBS
e IS, em atendimento à legislação vigente.

Esclarecemos que esta NT poderá ser ajustada ao longo do seu processo de execução, uma vez que as discussões
envolvendo a implantação da Reforma Tributária ainda estão em curso.

Vale destacar que, em Produção, no ano de 2025 as informações de tributação relativas ao IBS e CBS serão
opcionais e validadas apenas se forem informadas.

Esta documentação descreve as alterações aplicadas aos Documentos:
✓   Conhecimento de Transporte Eletrônico (modelo 57);
✓   Conhecimento de Transporte Eletrônico para Outros Serviços (modelo 67);
```

## 2 Tipos básicos da tributação

```text
Em busca de uma padronização entre os diversos documentos fiscais eletrônicos, esta NT introduz o arquivo
DFeTiposBasicos_v1.00.xsd ao conjunto dos arquivos que compõem do schema da DFe.

Este arquivo define de forma estruturada a previsão de campos a serem informados para o registro das
informações referentes a tributação do IBS e da CBS em um tipo complexo referenciado no leiaute padrão da DFe
conforme estrutura abaixo:
```

## 3 Alteração do leiaute do imposto do CTe

```text
  Este grupo de informações facultativas deve ser adicionado ao final do grupo imposto do CTe, CTe Simplificado e
  CTe OS.
 #       Campo             Ele   Pai                  Tipo    Ocor.   Tam.      Descrição/Observação
 #      IBSCBS             G     imp                      -   0-1     -         Grupo de informações da Tributação IBS/CBS

 1      CST                E     IBSCBS               N       1-1     3         Código da Situação Tributária do IBS/CBS

 2      cClassTrib         E     IBSCBS               N       1-1     6         Código da Classificação Tributária do IBS/CBS

 3      indDoacao          E     IBSCBS               N       0-1     1         Informar quando doação

 4      gIBSCBS            G     IBSCBS               -       0-1     -         Grupo de informações específicas do IBS/CBS

 5      vBC                E     gIBSCBS              N       1-1     13,2      Valor da Base de cálculo comum a IBS/CBS

 6      gIBSUF             G     gIBSCBS              -       1-1     -         Grupo de informações do IBS/CBS de competência
                                                                                das Unidades Federadas
 7      pIBSUF             E     gIBSUF               N       1-1     3,2/3,4   Alíquota do IBS Estadual

 8      gDif               G     gIBSUF               -       0-1     -         Grupo de campos do diferimento

 9      pDif               E     gDif                 N       1-1     3,2/3,4   Percentual de diferimento

10      vDif               E     gDif                 N       1-1     13,2      Valor do diferimento

11      gDevTrib           G     gIBSUF               -       0-1     -         Grupo de informações da devolução de tributos

12      vDevTrib           E     gDevTrib             N       1-1     13,2      Valor do tributo devolvido.
                                                                                No fornecimento de energia elétrica, água, esgoto e
                                                                                gás natural e em outras hipóteses definidas no
                                                                                regulamento

13      gRed               G     gIBSUF               -       0-1     -         Grupo de informações da redução de Alíquota

14      pRedAliq           E     gRed                 N       1-1     3,2/3,4   Percentual da redução de Alíquota do cClassTrib

15      pAliqEfet          E     gRed                 N       1-1     3,2/3,4   Alíquota efetiva do IBS de competência das UF que
                                                                                será aplicada a base de cálculo, incluindo o
                                                                                gCompraGov/pRedutor, se houver.
16      vIBSUF             E     gIBSUF               N       1-1     13,2      Valor do IBS de competência da UF

17      gIBSMun            G     gIBSCBS              -       1-1     -         Grupo de informações do IBS/CBS de competência
                                                                                do municipio
18      pIBSMun            E     gIBSMun              N       1-1     3,2/3,4   Alíquota do IBS Municipal

19      gDif               G     gIBSMun              -       0-1     -         Grupo de campos do diferimento

20      pDif               E     gDif                 N       1-1     3,2/3,4   Percentual de diferimento

21      vDif               E     gDif                 N       1-1     13,2      Valor do diferimento

22      gDevTrib           G     gIBSMun              -       0-1     -         Grupo de informações da devolução do tributo

23      vDevTrib           E     gDevTrib             N       1-1     13,2      Valor do tributo devolvido.
                                                                                No fornecimento de energia elétrica, água, esgoto e
                                                                                gás natural e em outras hipóteses definidas no
                                                                                regulamento

24      gRed               G     gIBSMun              -       0-1     -         Grupo de informações da redução de Alíquota

25      pRedAliq           E     gRed                 N       1-1     3,2/3,4   Percentual da redução de Alíquota do cClassTrib

26      pAliqEfet          E     gRed                 N       1-1     3,2/3,4   Alíquota efetiva do IBS de competência dos
                                                                                Municipios que será aplicada a base de cálculo,
                                                                                incluindo o gCompraGov/pRedutor, se houver.
26a     vIBSMun            E     gIBSMun              N       1-1     13,2      Valor do IBS de competência do município

27      vIBS               E     gIBSCBS              N       1-1     13,2      Valor do IBS (soma de vIBSUF e vIBSMun)

28      gCBS               G     gIBSCBS              -       1-1     -         Grupo de informações da CBS

29      pCBS               E     gCBS                 N       1-1     3,2/3,4   Alíquota da CBS

30   gDif                 G   gCBS             -   0-1   -         Grupo de campos do diferimento

31   pDif                 E   gDif             N   1-1   3,2/3,4   Percentual de diferimento

32   vDif                 E   gDif             N   1-1   13,2      Valor do diferimento

33   gDevTrib             G   gCBS             -   0-1   -         Grupo de informações da devolução do tributo

34   vDevTrib             E   gDevTrib         N   1-1   13,2      Valor da CBS devolvida.
                                                                   No fornecimento de energia elétrica, água, esgoto e
                                                                   gás natural e em outras hipóteses definidas no
                                                                   regulamento
35   gRed                 G   gCBS             -   0-1   -         Grupo de informações da redução de Alíquota

36   pRedAliq             E   gRed             N   1-1   3,2/3,4   Percentual da redução de Alíquota do cClassTrib

37   pAliqEfet            E   gRed             N   1-1   3,2/3,4   Alíquota efetiva da CBS que será aplicada a base
                                                                   de cálculo, incluindo o gCompraGov/pRedutor, se
                                                                   houver.
38   vCBS                 E   gCBS             N   1-1   13,2      Valor da CBS
39   gTribRegular         G   gIBSCBS          -   0-1   -         Grupo de informações da Tributação Regular.
                                                                   Informar como seria a tributação caso não cumprida
                                                                   a condição resolutória/suspensiva. Exemplo 1: Art.
                                                                   442, §4. Operações com ZFM e ALC. Exemplo 2:
                                                                   Operações com suspensão do tributo..
40   CSTReg               E   gTribRegular     N   1-1   3         Código da Situação Tributária
                                                                   Informado como seria o CST caso não cumprida a
                                                                   condição resolutória/suspensiva
41   cClassTribReg        E   gTribRegular     N   1-1   6         Código de Classificação Tributária
                                                                   Informado como seria o cClassTrib caso não
                                                                   cumprida a condição resolutória/suspensiva
42   pAliqEfetRegIBSUF    E   gTribRegular     N   1-1   3,2/3,4   Alíquota efetiva da UF
                                                                   Informado a Alíquota caso não cumprida a condição
                                                                   resolutória/suspensiva
43   vTribRegIBSUF        E   gTribRegular     N   1-1   13,2      Informado como seria o valor do Tributo da UF caso
                                                                   não cumprida a condição resolutória/suspensiva
44   pAliqEfetRegIBSMun   E   gTribRegular     N   1-1   3,2/3,4   Alíquota efetiva do Município
                                                                   Informado a Alíquota caso não cumprida a condição
                                                                   resolutória/suspensiva
45   vTribRegIBSMun       E   gTribRegular     N   1-1   13,2      Informado como seria o valor do Tributo do
                                                                   Município caso não cumprida a condição
                                                                   resolutória/suspensiva
46   pAliqEfetRegCBS      E   gTribRegular     N   1-1   3,2/3,4   Alíquota efetiva da CBS
                                                                   Informado a Alíquota caso não cumprida a condição
                                                                   resolutória/suspensiva
     vTribRegCBS          E   gTribRegular     N   1-1   13,2      Informado como seria o valor do Tributo CBS caso
                                                                   não cumprida a condição resolutória/suspensiva
57   gTribCompraGov       G   gIBSCBS          -   0-1   -         Grupo de informações da composição do valor do
                                                                   IBS e da CBS em compras governamental
58   pAliqIBSUF           E   gTribCompraGov   N   1-1   3,2/3,4   Alíquota IBS da UF utilizada

59   vTribIBSUF           E   gTribCompraGov   N   1-1   13,2      Valor do Tributo do IBS da UF
                                                                   Valor que seria devido a UF, sem aplicação do Art.
                                                                   473. da LC 214/20025

60   pAliqIBSMun          E   gTribCompraGov   N   1-1   3,2/3,4   Alíquota IBS do Município utilizada

61   vTribIBSMun          E   gTribCompraGov   N   1-1   13,2      Valor do Tributo do Município da UF
                                                                   Valor que seria devido ao Município, sem aplicação
                                                                   do Art. 473. da LC 214/20025
62   pAliqCBS             E   gTribCompraGov   N   1-1   3,2/3,4   Alíquota IBS do CBS utilizada

63   vTribCBS             E   gTribCompraGov   N   1-1   13,2      Valor do Tributo da CBS
                                                                   Valor que seria devido a CBS, sem aplicação do Art.
                                                                   473. da LC 214/20025

64   gEstornoCred         G   IBSCBS           -   0-1   -         Grupo de informações de estorno de crédito.
                                                                   Informado conforme indicador no cClassTrib

65   vIBSEstCred            E   gEstornoCred          N      1-1     13,2     Valor do IBS a ser estornado

66   vCBSEstCred            E   gEstornoCred          N      1-1     13,2     Valor do CBS a ser estornado
```

## 4 Código de Classificação Tributária do IBS/CBS

```text
O grupo de informações do IBS, CBS e IS associado aos itens do documento fiscal contém o Código de Situação
Tributária (CST) e Código de Classificação Tributária (cClassTrib) do IBS, CBS e IS. O Informe Técnico RT
2025.002 divulga a publicação da tabela com esta codificação, que está disponível no Portal Nacional da NF-e
(www.nfe.fazenda.gov.br), na aba “Documentos”, opção “Diversos” e no portal dos Documentos Fiscais Eletrônicos
(dfe-portal.svrs.rs.gov.br).

Cada código “cClassTrib” corresponde a um dispositivo específico da Lei Complementar nº 214/2025, tornando
objetiva a informação prestada pelo contribuinte quanto à forma como interpreta a tributação do IBS e da CBS para
cada DFe.

A tabela também contém indicadores que vinculam de forma dinâmica códigos “CST-IBS/CBS” e “cClassTrib” com
as Regras de Validação descritas nesta NT, ou que contêm informações necessárias para a preparação das
apurações assistidas do IBS e da CBS, em atendimento ao disposto na legislação vigente.

Vale ressaltar que a tabela poderá sofrer alterações em virtude de aperfeiçoamentos, novidades introduzidas em
sede de Regulamento, ou para atender a necessidades relacionadas à apuração assistida do IBS e da CBS.
```

## 5 Validações dos campos do IBS e CBS

```text
#     Regra de Validação                                         Aplic.   cStat   Efeito    Mensagem
001   Não informado grupo de imposto IBS e CBS (grupo:           Futura   310     Rej.      Rejeição: IBS / CBS não informado
      imp/IBSCBS)

      Exceção: Se o CRT informado pelo emitente for 1-
      Simples Nacional, 2- Simples Nacional, excesso
      sublimite de receita bruta ou 4 -MEI, o grupo IBSCBS
      NÃO será exigido

      IMPORTANTE: Esta regra passou para implementação
      futura, no entanto se o grupo for informado, todas as
      regras de validação serão aplicadas
002   Se CST do IBS/CBS for informado, este deve existir na      Obrig.   311     Rej.      Rejeição: CST informado inexistente
      tabela de Código de Situação Tributária (tag:
      IBSCBS/CST)
003   Se cClassTrib for informado, este deve existir na tabela   Obrig.   312     Rej.      Rejeição: Classificação Tributária informada
      de Classificação Tributária do IBS/CBS (tag:                                          inexistente
      IBSCBS/cClassTrib)
004   Verificar se o CST informado é compatível com o            Obrig.   313     Rej.      Rejeição: Classificação Tributária incompatível com
      cClassTrib                                                                            o CST informado
004   Verificar se o cClassTrib informado (tag:                  Obrig.   388     Rej.      Rejeição: Classificação Tributária do IBS/CBS não
a     IBSCBS/cClassTrib) possui indicador que não permite                                   permitida neste modelo de DFe.
      ser informado nesse modelo de DFe
005   Se o CST informado possuir indicador que VEDA              Obrig    314     Rej.      Rejeição: Grupo IBS/CBS não deve ser preenchido
      preenchimento do grupo de informações específicas do                                  para o CST informado
      IBS/CBS, este grupo NÂO DEVE estar informado
      (grupo: gIBSCBS)
006   Se o CST informado possuir indicador que EXIGE             Obrig    315     Rej.     Rejeição: Grupo IBS/CBS deve ser preenchido para o
      preenchimento do grupo de informações específicas do                                 CST informado
      IBS/CBS, este grupo DEVE estar informado (grupo:
      gIBSCBS)

      Exceção: Se o CRT informado pelo emitente for 1-
      Simples Nacional, 2- Simples Nacional, excesso
      sublimite de receita bruta ou 4 -MEI, o grupo gIBSCBS
      NÃO será exigido
007   Se informado grupo IBS de competência das Unidades         Obrig.   316     Rej.     Rejeição: Alíquota do IBS da UF inválida
      Federadas (gIBSUF):

      A alíquota de IBS da UF (pIBSUF) deverá ser:
           •    0,1% para documento com data de emissão
                no ano de 2026. (Art. 343 da LC 214/25)
           •    0.05% para documento com data de emissão
                no ano de 2027 e 2028. (Art. 344 da LC
                214/25)
           •    Alíquota de referência ou específica da UF a
                ser publicada para anos posteriores a 2028.

      Exceção: Se o cClassTrib possuir indicador de
      tributação regular o pIBSUF deve ser igual a zero
009   Se CST informado possuir indicador que EXIGE               Obrig.   366     Rej.     Rejeição: CST informado ou compras governamentais
      informação de redução de alíquota para o IBS Estadual                                obriga informação de redução de alíquota estadual
      ou informado grupo de compra governamental, o grupo
      gRed DEVE estar informado

      Exceção: A regra não se aplica para CST do IBS/CBS
      (tag: IBSCBS/CST)
      que possui indicador que não permite a informação do
      IBS/CBS
009   Se informado grupo de Redução de Alíquota para IBS         Obrig.   389     Rej.     Rejeição: Percentual de redução de alíquota da UF
a     Estadual (gIBSUF/gRed):                                                              não é válido para este cClassTrib

      Verificar se percentual de Redução de Alíquota
      (pRedAliq) é válido para o cClassTrib informado
      (gIBSCBS/cClassTrib)
009   Se informado grupo de Redução de Alíquota para IBS         Obrig.   390     Rej.     Rejeição: Valor da Alíquota Efetiva do IBS da UF
b     Estadual (gIBSUF/gRed), a Alíquota Efetiva (tag:                                     calculado incorretamente
      pAliqEfet) deve ser o resultado de:
      Se NÃO houver compra governamental (grupo
      gCompraGov não informado):

      pAliqEfet = pIBSUF × (1 - pRedAliq /100).

      Se houver compra governamental (grupo gCompraGov
      informado):
      pAliqEfet = pIBSUF × (1 - pRedAliq /100) × (1 -
      pRedutor/100).
      Observação: pRedutor é obtido no grupo
      gCompraGov

      Exemplo: Redução de 40% na alíquota:
      Alíquota vigente (A): 10%
      Redução na alíquota (R): 40%
      Redutor de compras governamentais (RG): 5%
      Alíquota Efetiva (E):
      E = A × (1 – R/100) × (1 – RG/100) = 5,7.
010   Se CST informado possuir indicador que VEDA a             Obrig.   367   Rej.   Rejeição: CST informado não permite informação de
      informação de redução de alíquota para o IBS                                    redução de alíquota estadual
      Estadual, o grupo gRed NÃO DEVE estar informado

      Exceção: Se Percentual de redução de alíquota em
      compra governamental (tag:gCompraGov/pRedutor)
      informado, este grupo é exigido e pRed deve ser igual
      a 0.
011   Se CST informado possuir indicador que EXIGE              Obrig.   319   Rej.    Rejeição: CST informado obriga informação de
      informação de Diferimento para o IBS Estadual, o                                 diferimento Estadual
      grupo gDif DEVE estar informado
012   Se CST informado possuir indicador que VEDA               Obrig.   368   Rej.    Rejeição: CST informado não permite informação de
      informação de Diferimento para o IBS Estadual, o                                 diferimento Estadual
      grupo gDif NÃO DEVE estar informado
013   Se informado grupo do Diferimento (gIBSUF/gDif):          Obrig.   320   Rej.    Rejeição: Valor do Diferimento da UF difere do
      O valor do Diferimento (vDif) deverá ser resultante de:                          calculado
      vDif = vBC x (pIBSUF/100) x (pDif/100)

      Observação: Aceitar uma tolerância de 0,01 a mais ou
      a menos
      Observação 2: Em caso de preenchimento do grupo
      de redução (gRed) a alíquota utilizada deverá ser a tag
      Alíquota Efetiva (pAliqEfet)
013   Se informado grupo IBS de competência das Unidades        Obrig.   395   Rej.    Rejeição: Valor do IBS UF não pode resultar
a     Federadas (gIBSUF):                                                              negativo
      O valor resultante da soma do diferimento (vDif) e
      Devolução (DevTrib) QUANDO INFORMADOS, NÃO
      pode ser superior a vBC x (pIBSUF/100)
      Observação: Aceitar uma tolerância de 0,01 a mais ou
      a menos
      Observação 2: Em caso de preenchimento do grupo
      de redução (gRed) a alíquota utilizada deverá ser a tag
      Alíquota Efetiva (pAliqEfet)
014   Se informado grupo IBS de competência das Unidades        Obrig.   318   Rej.    Rejeição: Valor do IBS UF difere do calculado
      Federadas (gIBSUF):
      O valor do IBS (vIBSUF) deverá ser resultante de:
      vIBSUF = vBC x (pIBSUF/100) – vDif - vDevTrib

      Observação: Aceitar uma tolerância de 0,01 a mais ou
      a menos
      Observação 2: Em caso de preenchimento do grupo
      de redução (gRed) a alíquota utilizada deverá ser a tag
      Alíquota Efetiva (pAliqEfet)
015   Se informado grupo IBS de competência dos                 Obrig.   321   Rej.    Rejeição: Alíquota do IBS do Município inválida
      Municípios (gIBSMun):
      A alíquota de IBS Municipal deverá ser:
           •    0% para documento com data de emissão no
                ano de 2026. (Art. 343 da LC 214/25)
           •    0.05% para documento com data de emissão
                no ano de 2027 e 2028. (Art. 344 da LC
                214/25)
           •    Alíquota de referência ou específica do
                Município a ser publicada para anos
                posteriores a 2028

      Exceção: Se o cClassTrib possuir indicador de
      tributação regular o pIBSMun deve ser igual a zero

017   Se CST informado possuir indicador que EXIGE             Obrig.   369   Rej.    Rejeição: CST informado ou compras
      informação de redução de alíquota para o IBS                                    governamentais obriga informação de redução de
      Municipal ou informado grupo de compra                                          alíquota municipal
      governamental, o grupo gRed DEVE estar informado

      Exceção: A regra não se aplica para CST do IBS/CBS
      (tag: IBSCBS/CST)
      que possui indicador que não permite a informação do
      IBS/CBS
017   Se informado grupo de Redução de Alíquota para IBS       Obrig.   391   Rej.    Rejeição: Percentual de redução de alíquota do
a     Municipal (gIBSMun/gRed):                                                       Município não é válido para este cClassTrib
      Verificar se percentual de Redução de Alíquota
      (pRedAliq) é válido para o cClassTrib informado
      (gIBSCBS/cClassTrib)
017   Se informado grupo de Redução de Alíquota para IBS       Obrig.   392   Rej.    Rejeição: Valor da Alíquota Efetiva do IBS do
b     Municipal (gIBSMun/gRed), a Alíquota Efetiva (tag:                              Município calculado incorretamente
      pAliqEfet) deve ser o resultado de:

      Se NÃO houver compra governamental (grupo
      gCompraGov não informado):
      pAliqEfet = pIBSMun × (1 - pRedAliq /100).

      Se houver compra governamental (grupo
      gCompraGov informado):
      pAliqEfet = pIBSMun × (1 - pRedAliq /100) × (1 -
      pRedutor/100).

      Observação: pRedutor é obtido no grupo
      gCompraGov

      Exemplo: Redução de 40% na alíquota:
      Alíquota vigente (A): 10%
      Redução na alíquota (R): 40%
      Redutor de compras governamentais (RG): 5%
      Alíquota Efetiva (E):
      E = A × (1 – R/100) × (1 – RG/100) = 5,7.
018   Se CST informado possuir indicador que VEDA a            Obrig.   381   Rej.    Rejeição: CST informado não permite informação de
      informação de redução de alíquota para o IBS                                    redução de alíquota municipal
      Municipal, o grupo gRed NÃO DEVE estar informado

      Exceção: Se Percentual de redução de alíquota em
      compra governamental (tag:gCompraGov/pRedutor)
      informado, este grupo é exigido e pRed deve ser igual
      a 0.
019   Se CST informado possuir indicador que EXIGE             Obrig.   324   Rej.   Rejeição: CST informado obriga informação de
      informação de Diferimento para o IBS Municipal, o                              diferimento Municipal
      grupo gDif DEVE estar informado
020   Se CST informado possuir indicador que VEDA              Obrig.   382   Rej.   Rejeição: CST informado não permite informação de
      informação de Diferimento para o IBS Municipal, o                              diferimento Municipal
      grupo gDif NÃO DEVE estar informado
021   Se informado grupo do Diferimento (gIBSMun/gDif):        Obrig.   325   Rej.   Rejeição: Valor do Diferimento do Município difere do
      O valor do Diferimento (vDif) deverá ser resultante de                         calculado
      vDif = vBC x (pIBSMun/100) x (pDif/100)

      Observação: Aceitar uma tolerância de 0,01 a mais
      ou a menos

      Observação 2: Em caso de preenchimento do grupo
      de redução (gRed) a alíquota utilizada deverá ser a
      tag Alíquota Efetiva (pAliqEfet)
022   Se informado grupo IBS de competência dos                Obrig.   323   Rej.   Rejeição: Valor do IBS Municipal difere do calculado
      Municípios (gIBSMun):
      O valor do IBS (vIBSMun) deverá ser resultante de:
      vIBSMun = vBC x (pIBSMun/100) – vDif - vDevTrib

      Observação: Aceitar uma tolerância de 0,01 a mais
      ou a menos

      Observação 2: Em caso de preenchimento do grupo
      de redução (gRed) a alíquota utilizada deverá ser a
      tag Alíquota Efetiva (pAliqEfet)

022   Se informado grupo IBS de competência dos               Obrig.   396   Rej.   Rejeição: Valor do IBS Municipal não pode resultar
a     Municípios (gIBSMun):                                                         negativo

      O valor resultante da soma do diferimento (vDif) e
      Devolução (DevTrib) QUANDO INFORMADOS, NÃO
      pode ser superior a vBC x (pIBSMun/100)
      Observação: Aceitar uma tolerância de 0,01 a mais
      ou a menos
      Observação 2: Em caso de preenchimento do grupo
      de redução (gRed) a alíquota utilizada deverá ser a
      tag Alíquota Efetiva (pAliqEfet)
022   Se informados grupos IBS de competência dos             Obrig.   317   Rej.   Rejeição: Total de IBS difere do calculado
b     Estados (gIBSUF) e Municípios (gIBSMun):
      O valor do total de IBS (vIBS) deverá ser a soma do
      vIBSUF e do vIBSMUn
      vIBS = vIBSUF + vIBSMun
023   Se informado grupo CBS (gCBS):                          Obrig.   326   Rej.   Rejeição: Alíquota da CBS inválida
      A alíquota de CBS deverá ser:
           •    0,90 % para documento com data de
                emissão no ano de 2026. (Art. 343 da LC
                214/25)
           •    Alíquota de referência a ser publicada para
                anos posteriores a 2026

      Exceção: Se o cClassTrib possuir indicador de
      tributação regular o pCBS deve ser igual a zero
      Exceção 2: A Alíquota da CBS (tag: pCBS) pode ser
      igual a zero quando a condição abaixo for atendida:

      CTe ou CTeOS (Não se aplica a CTe Simplificado)

      Município do Emitente, Início e Fim da Prestação do
      Serviço de transporte devem estar na mesma área
      incentivada (ou seja, dentro da ZFM, na mesma ALC),
      conforme relação abaixo:
          - ZFM: AC-Acre, AM-Amazonas, RO-Rondônia,
      RR-Roraima, AP-Amapá (só para municípios
      1600303-Macapá e 1600600-Santana);

         - ALC: conforme tabela abaixo:
       Município Início           Município Fim
       1304062-Tabatinga          1304062-Tabatinga
       1600303-Macapá             1600303-Macapá
       1600303-Macapá             1600600-Santana
       1600600-Santana            1600303-Macapá
       1600600-Santana            1600600-Santana
       1100106-Guajará-Mirim      1100106-Guajará-Mirim
       1400100-Boa Vista          1400100-Boa Vista
       1400100-Boa Vista          1400456-Paracaima
       1400456-Paracaima          1400100-Boa Vista
       1400456-Paracaima          1400456-Paracaima
       1400159-Bonfim             1400159-Bonfim
       1200104-Brasileia          1200104-Brasileia
       1200104-Brasileia          1200252-Epitaciolândia
       1200252-Epitaciolândia     1200104-Brasileia
       1200252-Epitaciolândia     1200252-Epitaciolândia
       1200203-Cruzeiro do Sul    1200203-Cruzeiro do Sul

      O Município do Emitente tem que estar também em
      uma área incentivada.
      Observação: As cores definem quais municípios são
      da mesma área incentivada, e isto será observado na
      regra de validação

024   Se CST informado possuir indicador que EXIGE              Obrig.   383   Rej.   Rejeição: CST informado ou compras
      informação de redução de alíquota para o CBS ou                                 governamentais obriga informação de redução de
      informado grupo de compra governamental, o grupo                                alíquota do CBS
      gRed DEVE estar informado

      Exceção: A regra não se aplica para CST do IBS/CBS
      (tag: IBSCBS/CST)
      que possui indicador que não permite a informação do
      IBS/CBS
024   Se informado grupo de Redução de Alíquota para            Obrig.   393   Rej.   Rejeição: Percentual de redução de alíquota da CBS
a     CBS (gCBS/gRed):                                                                não é válido para este cClassTrib

      Verificar se percentual de Redução de Alíquota
      (pRedAliq) é válido para o cClassTrib informado
      (gIBSCBS/cClassTrib)
024   Se informado grupo de Redução de Alíquota para            Obrig.   394   Rej.   Rejeição: Valor da Alíquota Efetiva da CBS calculado
b     CBS (gCBS/gRed), a Alíquota Efetiva (tag: pAliqEfet)                            incorretamente
      deve ser o resultado de:
      Se NÃO houver compra governamental (grupo
      gCompraGov não informado):
      pAliqEfet = pCBS × (1 - pRedAliq /100).

      Se houver compra governamental (grupo
      gCompraGov informado):
      pAliqEfet = pCBS × (1 - pRedAliq /100) × (1 -
      pRedutor/100).

      Observação: pRedutor é obtido no grupo
      gCompraGov

      Exemplo: Redução de 40% na alíquota:
      Alíquota vigente (A): 10%
      Redução na alíquota (R): 40%
      Redutor de compras governamentais (RG): 5%
      Alíquota Efetiva (E): E = A * (1 - R) * (1- RG)
      E = 10 * (1 - 0,4) *(1-0,05) = 5,7
025   Se CST informado possuir indicador que VEDA a             Obrig.   384   Rej.   Rejeição: CST informado não permite informação de
      informação de redução de alíquota para o CBS, o                                 redução de alíquota do CBS
      grupo gRed NÃO DEVE estar informado

      Exceção: Se Percentual de redução de alíquota em
      compra governamental (tag:gCompraGov/pRedutor)
      informado, este grupo é exigido e pRed deve ser igual
      a 0.
026   Se CST informado possuir indicador que EXIGE              Obrig.   328   Rej.   Rejeição: CST informado obriga informação de
      informação de Diferimento para o CBS, o grupo gDif                              diferimento do CBS
      DEVE estar informado
027   Se CST informado possuir indicador que VEDA               Obrig.   385   Rej.   Rejeição: CST informado não permite informação de
      informação de Diferimento para o CBS, o grupo gDif                              diferimento do CBS
      NÃO DEVE estar informado
028   Se informado grupo do Diferimento (gCBS/gDif):            Obrig.   329   Rej.   Rejeição: Valor do Diferimento do CBS difere do
      O valor do Diferimento (vDif) deverá ser resultante de:                         calculado
      vDif = vBC x (pCBS/100) x (pDif/100)

      Observação: Aceitar uma tolerância de 0,01 a mais
      ou a menos

      Observação 2: Em caso de preenchimento do grupo
      de redução (gRed) a alíquota utilizada deverá ser a
      tag Alíquota Efetiva (pAliqEfet)
028   Se informado grupo CBS (gCBS):                            Obrig.   397   Rej.   Rejeição: Valor do CBS não pode resultar negativo
a     O valor resultante da soma do diferimento (vDif) e
      Devolução (DevTrib) QUANDO INFORMADOS, NÃO
      pode ser superior a vBC x (pCBS/100)

      Observação: Aceitar uma tolerância de 0,01 a mais
      ou a menos

      Observação 2: Em caso de preenchimento do grupo
      de redução (gRed) a alíquota utilizada deverá ser a
      tag Alíquota Efetiva (pAliqEfet)

029   Se informado grupo CBS (gCBS):                           Obrig.   327   Rej.   Rejeição: Valor do CBS difere do calculado
      O valor da CBS (vCBS) deverá ser resultante de:
      vCBS = vBC x (pCBS/100) – vDif – vDevTrib

      Observação: Aceitar uma tolerância de 0,01 a mais
      ou a menos
      Observação 2: Em caso de preenchimento do grupo
      de redução (gRed) a alíquota utilizada deverá ser a
      tag Alíquota Efetiva (pAliqEfet).
030   Se cClassTrib informado possuir indicador que EXIGE      Obrig.   330   Rej.   Rejeição: Classificação Tributária informada obriga
      informação de tributação regular, o grupo                                      informação da tributação regular
      gTribRegular DEVE estar informado
030   Se cClassTrib informado NÃO POSSUIR indicador de         Obrig.   322   Rej.   Rejeição: Classificação Tributária não permite
a     informação de tributação regular, o grupo                                      informação da tributação regular
      gTribRegular NÃO DEVE estar informado
031   Se informado grupo da tributação regular                 Obrig.   331   Rej.   Rejeição: CST informado no grupo de tributação
      (gTribRegular):                                                                regular inexistente
      O CST Regular informado no grupo gTribRegular deve
      existir na tabela de Código de Situação Tributária
      (gTribRegular/CSTReg)
032   Se informado grupo da tributação regular                 Obrig.   332   Rej.   Rejeição: Classificação Tributária informada no grupo
      (gTribRegular):                                                                de tributação regular inexistente
      O cClassTrib regular for informado, este deve existir
      na tabela de Classificação Tributária do IBS/CBS (tag:
      gTribRegular/cClassTribReg)
033   Se informado grupo da tributação regular                 Obrig.   333   Rej.   Rejeição: Valor da tributação regular da UF difere do
      (gTribRegular):                                                                calculado
      O valor do tributo regular de IBS dos Estados
      (vTribRegIBSUF) deverá ser resultante de:
      vTribRegIBSUF = vBC x (pAliqEfetRegIBSUF/100)

      Observação: Aceitar uma tolerância de 0,01 a mais
      ou a menos
034   Se informado grupo da tributação regular                 Obrig.   334   Rej.   Rejeição: Valor da tributação regular do Município
      (gTribRegular):                                                                difere do calculado
      O valor do tributo regular de IBS dos Municípios
      (vTribRegIBSMun) deverá ser resultante de:
      vTribRegIBSMun = vBC x (pAliqEfetRegIBSMun/100)

      Observação: Aceitar uma tolerância de 0,01 a mais
      ou a menos
035   Se informado grupo da tributação regular                 Obrig.   335   Rej.   Rejeição: Valor da tributação regular da CBS difere
      (gTribRegular):                                                                do calculado
      O valor do tributo regular de CBS (vTribRegCBS)
      deverá ser resultante de:
      vTribRegularCBS = vBC x (pAliqEfetRegCBS/100)
      Observação: Aceitar uma tolerância de 0,01 a mais
      ou a menos
049   Se grupo compra governamental (grupo:                    Obrig.   398   Rej.   Rejeição: Grupo de informações da composição do
      gCompraGov) estiver informado, o Grupo de                                      valor do IBS e da CBS em compras governamentais
      informações da composição do valor do IBS e da CBS                             deve ser informado
      em compras governamentais (grupo:
      gTribCompraGov) DEVE ser informado.
      Exceção: A regra não se aplica para CST do IBS/CBS
      (tag: IBSCBS/CST)
      que possui indicador que não permite a informação do
      IBS/CBS
050   Se grupo compra governamental (grupo:                    Obrig.   399   Rej,   Rejeição: Grupo de informações da composição do
      gCompraGov) NÃO estiver informado, o Grupo de                                  valor do IBS e da CBS em compras governamentais
      informações da composição do valor do IBS e da CBS                             não deve ser informado
      em compras governamentais (grupo:
      gTribCompraGov) NÃO DEVE ser informado.
051   Verificar se a soma dos valores de IBS e CBS do          Obrig.   400   Rej.   Rejeição: Somas dos valores de IBS e CBS em
      grupo gTribCompraGov (vTribIBSUF + vTribIBSMun +                               compras governamentais divergente
      vTribCBS) é diferente do resultado de gIBSUF/vIBSUF
      + gIBSMun/vIBSMun + gCBS/vCBS.
052   Se o cClassTrib informado possuir indicador que          Obrig    303   Rej.   Rejeição: Grupo Estorno de Crédito não deve ser
      VEDA preenchimento do grupo de informações do                                  preenchido para o cClassTrib informado
      estorno de crédito (grupo:gEstornoCred)
053   Se o cClassTrib informado possuir indicador que          Obrig    304   Rej.   Rejeição: Grupo Estorno de Crédito deve ser
      EXIGE preenchimento do grupo de informações do                                 preenchido para o cClassTrib informado
      estorno de crédito (grupo:gEstornoCred)
```

## 6 Criação do grupo de compras governamentais no grupo ide

```text
      #       Campo                Ele   Pai                      Tipo     Ocor.    Tam.     Descrição/Observação

      #       gCompraGov           G     ide                       -       0-1      -

              tpEnteGov            E     gCompraGov               N        1-1      1        Para administração pública direta e suas autarquias
                                                                                             e fundações:
                                                                                             1=União
                                                                                             2=Estados
                                                                                             3=Distrito Federal
                                                                                             4=Municípios
                                                                                             5=Consórcio Público
                                                                                             6=Comitê Gestor do IBS
              pRedutor             E     gCompraGov               N        1-1      3v2-4    Percentual de redução de alíquota em compra
                                                                                             governamental
                                                                                             Conforme LC 214/25: TÍTULO II
                                                                                             DAS COMPRAS GOVERNAMENTAIS, Art. 472
              tpOperGov            E     gCompraGov               N        1-1      1        Tipo da operação com ente governamental:
                                                                                             1 – Fornecimento com pagamento posterior;
                                                                                             2 - Recebimento do pagamento com fornecimento já
                                                                                             realizado;
                                                                                             3 – Fornecimento com pagamento já realizado;
                                                                                             4 – Recebimento do pagamento com fornecimento
                                                                                             posterior;
              refDFeAnt            E     gCompraGov               C        0-n      44       Chave de acesso do documento fiscal anterior.
                                                                                             Deverá ser informado para tpOperGov 2 e 3 e
                                                                                             vedado para os tipos 1 e 4
                                                                                             Obs: a chave de acesso deverá ser de um emitente
                                                                                             com o mesmo CNPJ base

#     Regra de Validação                                       Aplic.    cStat     Efeito   Mensagem
001   Se informado o grupo de informações de compra            Obrig.    347       Rej.     Rejeição: DFe de compra governamental e alíquota
      governamental (grupo:ide\gCompraGov) e tipo do Ente                                   dos outros entes diferentes de zero.
      (gCompraGov\tpEntGov) diferente de 5 e 6, o DFe de
      compra governamental deve ter alíquota de outros
      entes igual a zero.
      De 2027 até 2032
      Para compra da união (tag: tpEnteGov = 1):
            •    Alíquota do IBS da UF (tag: pIBSUF) deve
                 ser igual a zero.
            •    Alíquota do IBS do Município (tag: pIBSMun)
                 deve ser igual a zero.
      Para compra estadual (tag: tpEnteGov = 2):
           •     Alíquota do IBS do Município (tag: pIBSMun)
                 deve ser igual a zero.
      Para compra do DF (tag: tpEnteGov = 3)
           •     Alíquota do IBS do Município (tag: pIBSMun)
                 deve ser igual a zero.
      Para compra municipal (tag: tpEnte = 4)
           •     Alíquota do IBS da UF (tag: pIBSUF) deve
                 ser igual a zero.
      A partir de 2033:
      Para compra da união (tag: tpEnteGov = 1):
           •     Alíquota do IBS da UF (tag: pIBSUF) deve
                 ser igual a zero.
           •     Alíquota do IBS do Município (tag: pIBSMun)
                 deve ser igual a zero.
      Para compra estadual (tag: tpEnteGov = 2):
           •     Alíquota do IBS do Município (tag: pIBSMun)
                 deve ser igual a zero.
           •     Alíquota do CBS (tag: pCBS) deve ser igual
                 a zero.
      Para compra do DF (tag: tpEnteGov = 3)
           •     Alíquota do IBS do Município (tag: pIBSMun)
                 deve ser igual a zero.
           •     Alíquota do CBS (tag: pCBS) deve ser igual
                 a zero.
      Para compra municipal (tag: tpEnte = 4)
           •     Alíquota do IBS da UF (tag: pIBSUF) deve
                 ser igual a zero.

           •       Alíquota do CBS (tag: pCBS) deve ser igual
                   a zero.
      Observação: Conforme Art. 473, § 1o e seus Incisos I,
          II, III e IV da LC 214/2025.
002   Se o tipo da operação com ente governamental for          Obrig    1004   Rej    Rejeição: Chave de acesso referenciada não deve
      igual a Fornecimento com pagamento posterior                                     ser informada para tipo de operação de
      (tpOperGov=1)                                                                    Fornecimento em compras governamentais
      A chave de acesso do DFe anterior (refDFeAnt) NÃO
      DEVE ser informada

003   Se o tipo da operação com ente governamental for          Obrig    1005   Rej    Rejeição: Deverá ser informada uma chave de
      igual a Recebimento do pagamento com fornecimento                                acesso de DFe referenciado para tipo de operação
      já realizado (tpOperGov=2)                                                       de Recebimento do pagamento com fornecimento
                                                                                       realizado em compras governamentais
      Deve ser informada UMA chave de acesso de DFe
      referenciado

      Observação: Se forem informadas múltiplas chaves de
      acesso ou nenhuma chave causará essa rejeição

004   Se o tipo da operação com ente governamental for          Obrig    1006   Rej    Rejeição: Pelo menos uma Chave de acesso de
      igual a Fornecimento com pagamento já realizado                                  DFe referenciado deve ser informada para tipo de
      (tpOperGov=3)                                                                    operação fornecimento com pagamento já realizado
                                                                                       em compras governamentais
      Uma ou mais chaves de acesso de DFe anteriores
      (refDFeAnt) DEVEM ser informadas

005   Se o tipo da operação com ente governamental for          Obrig    1007   Rej    Rejeição: Chave de acesso referenciada não deve
      igual a Recebimento do pagamento com fornecimento                                ser informada para tipo de operação recebimento do
      posterior (tpOperGov=4)                                                          pagamento com fornecimento posterior em compras
                                                                                       governamentais
      A chave de acesso do DFe anterior (refDFeAnt) NÃO
      DEVE ser informada

006   Se informado documento anterior no grupo de compras       Obrig.   1008   Rej.   Rejeição: Chave de acesso referenciada em
      governamentais (gCompraGov/refDFeAnt), para cada                                 compras governamentais inválida
      chave informada:
      - Validar chave de acesso do DFe referenciado.
      Retornar motivo da rejeição da Chave de Acesso:
      CNPJ zerado ou inválido, Ano, Mês inválido (0 ou >
      12), Modelo de DFe diferente, Número zerado, Tipo de
      emissão inválido, UF inválida ou DV inválido)
      [Motivo: XXXXXXXXXXXX]
007   Se informado documento anterior no grupo de compras       Obrig    1009   Rej    Rejeição: DFe referenciado em compras
      governamentais (gCompraGov/refDFeAnt):                                           governamentais inexistente
      - O DFe referenciado deve existir, acesso BD (Chave:
      CNPJ Emit, Modelo, Série, Nro)

008   Se informado documento anterior no grupo de compras       Obrig.   1010   Rej.   Rejeição: DFe referenciado em compras
      governamentais (gCompraGov/refDFeAnt), para cada                                 governamentais com diferença de Chave de Acesso
      chave informada:
      - DFe referenciado não pode existir com diferença na
      Chave de Acesso
      Retornar a chave de acesso já autorizada, o número do
      protocolo e data de autorização do DFe
      [chDFe:
      99999999999999999999999999999999999999999999
      ]
      [nProt:999999999999999][dhAut: AAAA-MM-
      DDTHH:MM:SS TZD]
009   Se informado documento anterior no grupo de compras       Obrig.   1011   Rej    Rejeição: DFe referenciado em compras
      governamentais (gCompraGov/refDFeAnt), para cada                                 governamentais em situação inválida
      chave informada:
      - O DFe referenciado deve estar em situação
      Autorizado o Uso

      Observação: Rejeitar se documento estiver cancelado
      ou substituído na base de dados do ambiente de
      autorização

010     Se informado documento anterior no grupo de compras        Obrig.          1012          Rej          Rejeição: DFe referenciado em compras
        governamentais (gCompraGov/refDFeAnt), para cada                                                      governamentais deve possuir mesmo CNPJ base do
        chave informada:                                                                                      emitente do documento
        - O emitente do DFe referenciado deve ter o mesmo
        CNPJ Base do emitente do documento fiscal
        Exceção: os casos de alteração do CNPJ da empresa
        por motivo de aquisição, fusão, incorporação deve ser
        tratados no ambiente de autorização

011     Se informado documento anterior no grupo de compras        Obrig.          1013          Rej.         Rejeição: DFe referenciado em compras
        governamentais (gCompraGov/refDFeAnt) e tipo de                                                       governamentais deve ser de Fornecimento com
        operação for Recebimento do pagamento com                                                             pagamento posterior
        fornecimento já realizado; (tpOperGov = 2), para cada
        chave informada:
        - O DFe referenciado deve ser de compras
        governamentais e possuir o tipo de operação
        Fornecimento com pagamento posterior (tpOperGov =
        1)

012     Se informado documento anterior no grupo de compras        Obrig.          1014          Rej.         Rejeição: DFe referenciado em compras
        governamentais (gCompraGov/refDFeAnt) e tipo de                                                       governamentais deve ser de operação de
        operação for de Fornecimento com pagamento já                                                         Recebimento do pagamento com fornecimento
        realizado (tpOperGov = 3), para cada chave informada:                                                 posterior
        - O DFe referenciado deve ser de compras
        governamentais e possuir o tipo de operação
        Recebimento do pagamento com fornecimento
        posterior (tpOperGov = 4)
```

## 7 Total Geral do Documento Fiscal Eletrônico

```text
             Deverá ser criada a tag Valor Total do DFe (vTotDFe).
             No CTe, CTe Simplificado, CTe OS essa tag aparecerá dentro do grupo imp, após o grupo IBSCBS.
         #       Campo                 Ele   Pai                        Tipo       Ocor.         Tam.         Descrição/Observação

         01      vTotDFe                E     imp                        E           0-1           13,2        Valor total do documento fiscal
                                                                                                               vTPrest + total do IBS + total da CBS

#        Regra de Validação                                   Aplic.         cStat        Efeito         Mensagem

01       A tag de Total do Documento Fiscal Eletrônico        Obrig.         360          Rej.           Rejeição: Total do DFe de preenchimento obrigatório
         deverá ser informada (tag: imp\vTotDFe) sempre
         que existir informação no grupo IBSCBS (grupo:
         imp\IBSCBS)

02       O total geral do DFe deverá ser INFORMADO            Obrig.      365             Rej.           Rejeição: Total do DFe inválido
         com a soma do total da prestação + IBS + CBS
         vTotDFe = vPrest/vTPrest + gIBSCBS/vIBS +
         gCBS/vCBS
         Exceção: Em 2026 não somar IBS e CBS, usando
         a fórmula:
         vTotDFe = vPrest/vTPrest
```

## 8 Alteração em Regra do CTe Simplificado

```text
G101a      O município de fim de prestação em todos os itens do    Obrig.        370             Rej.     Rejeição: O CTe Simplificado deve ter a
           CTe Simplificado (det:cMunFim) devem ser iguais                                                prestação terminada em apenas um
                                                                                                          município
```

## 9 Alterações no Layout do Modal Dutoviário

```text
            Foram criados campos no schema específico do Modal Dutoviário.
  #        Campo                   Nível Descrição                                 Ele     Tipo Ocorr. Tam Observações
      1    duto                      0 Informações do modal Dutoviário               G           1-1
      2     vTar                     1 Valor da tarifa                               E       C   0 - 1 9, 6 15 posições, sendo 9 inteiras e 6
                                                                                                            casas decimais.
      3      dIni                    1   Data de Início da prestação do serviço      E       D   1 - 1 10
      4      dFim                    1   Data de Fim da prestação do serviço         E       D   1 - 1 10
      5      classDuto               1   Classificação Dutoviário                    E       N   0-1    1 Informar:
                                                                                                            1 – Gasoduto;
                                                                                                            2 – Mineroduto ou
                                                                                                            3 - Oleoduto
      6      tpContratacao           1   Tipo de contratação do serviço de           E       N   0-1    1 Informar:
                                         transporte (apenas para gasoduto)                                  0 – Ponto a ponto
                                                                                                            1 – Capacidade de Entrada ou
                                                                                                            2 – Capacidade de Saída
      7      codPontoEntrada         1   Código do Ponto de Entrada                  E       C   0-1 20
      8      codPontoSaida           1   Código do Ponto de Saída                    E       C   0-1 20
      9      nContrato               1   Número do Contrato de Capacidade            E       C   0-1 20

#         Regra de Validação                                       Aplic.    cStat       Efeito     Mensagem
001       Se informado classificação do dutoviário = Gasoduto      Obrig.    371         Rej.       Rejeição: Tipo de contratação deve ser informado
          (tag: classDuto = 1), o tipo de contratação deve ser                                      para tipo de dutoviário gasoduto
          informado (tag: tpContratacao)
002       Se Tipo de contratação for ponto a ponto (tag:           Obrig.    372         Rej.       Rejeição: Dutoviário com tipo de contratação ponto
          tpContratacao=0), os campos do código dos pontos de                                       a ponto deve informar Código dos pontos de entrada
          entrada e saída devem ser informados                                                      e saída

003       Se Tipo de contratação for capacidade de entrada        Obrig.     373         Rej.     Rejeição: Dutoviário com tipo de contratação
          (tag: tpContratacao=1), o campo do código do ponto                                      capacidade de entrada deve informar Código do ponto
          de entrada deve ser informado                                                           de entrada

004       Se Tipo de contratação for capacidade de saída (tag:    Obrig.     374         Rej.     Rejeição: Dutoviário com tipo de contratação
          tpContratacao=2), o campo do código do ponto de                                         capacidade de saída deve informar Código do ponto
          saída deve ser informado                                                                de saída
```

## 10 Criação do grupo de informações da DCe nos documentos originários

```text
                                              Validações dos Documentos Transportados
G045a    Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e         Obrig.  601    Rej.   Rejeição: Quantidade de documentos
         informado grupo informação de documentos (infDoc):                             informados no remetente excede limite de
         Quantidade de documentos informados                                            2000
         (infNF/infNFe/infOutros/infDCe) não pode ultrapassar
         2000 documentos
G045b    Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e         Obrig.  375    Rej.   Rejeição: DCe duplicada no CTe
         informados grupos de informações de documentos                                 [chDCe:
         (infDoc) e DCe (infDCe)                                                        9999999999999999999999999999999999
         - Verificar se existe alguma chave de acesso de DCe                            9999999999]
         duplicada no CTe
         Retornar a chave duplicada
G045c    Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e         Obrig.  376    Rej.   Rejeição: Chave de acesso da DCe
         informados grupos de informações de documentos                                 transportada inválida
         (infDoc) e DCe (infDCe), para cada uma das DCe´s
         relacionadas:
         - Validar chave de acesso
         Retornar a primeira chave inválida e o motivo da
         rejeição da Chave de Acesso: CNPJ / CPF zerado ou
         inválido, Ano < 2025 ou maior que atual, Mês inválido (0
         ou > 12), Modelo diferente de 99, Número zerado, Tipo
         de emissão inválido, UF inválida ou DV inválido)
         [chDCe:
         99999999999999999999999999999999999999999999]
         [Motivo: XXXXXXXXXXXX]
G045d    Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e         Facult. 377    Rej.   Rejeição: DCe inexistente na base de
         informados grupos de informações de documentos                                 dados da SEFAZ
         (infDoc) e DCe (infDCe), para cada uma das DCe´s
         relacionadas:
          - Acessar BD CHAVES DCE (Chave: UF, CNPJ/CPF
         Emit, Modelo, Série, Nro):
                  - A DCe deve existir
         Retornar a primeira chave de acesso de DCe
         inexistente.
         Exceção: DCe em contingência fica dispensada dessa
         validação (verificar tpEmis da chave de acesso da DCe)
G045e    Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e         Facult. 378    Rej.   Rejeição: DCe com diferença de Chave de
         informados grupos de informações de documentos                                 Acesso
         (infDoc) e DCe (infDCe), para cada uma das DCe´s
         relacionadas:
          - Acessar BD CHAVES DCE (Chave: UF, CNPJ/CPF
         Emit, Modelo, Série, Nro):
                  - A DCe não pode existir com diferença de chave
         de acesso
         Retornar a primeira chave de acesso de DCe com
         situação inválida.
G045f    Se Tipo do CTe= 0 (Normal) ou 3 (Substituição) e         Facult. 379    Rej.   Rejeição: DCe não pode estar cancelada
         informados grupos de informações de documentos                                 ou denegada
         (infDoc) e DCe (infDCe), para cada uma das DCe´s
         relacionadas:
          - Acessar BD CHAVES DCE (Chave: UF, CNPJ/CPF
         Emit, Modelo, Série, Nro):
                  - A DCe não pode estar cancelada
         Retornar a primeira chave de acesso de DCe com
         situação inválida.

        As regras G45d, G45e e G45f dependem do ambiente de autorização possuir acesso a base de dados de DCe.
```

## 11 Exceção para Substituição sem exigência do evento de prestação em desacordo para tomador Exterior

```text
        A exigência do registro do tomador de prestação de serviço em desacordo para permitir a substituição de um CTe
        se torna impeditiva quando o tomador for pessoa do exterior, uma vez que esta não tem meios para autorizar o
        evento.
G084/    Se Tipo do CTe=3 (Substituição):                           Obrig    739    Rej.     Rejeição: O CTe substituído deve possuir
H067     - O CTe substituído deve possuir evento de Prestação do    .                        evento de Prestação do Serviço em
         Serviço em Desacordo em situação autorizado.                                        Desacordo

         Observação: Eventos de Cancelamento do Evento de
         Prestação em desacordo anulam eventos de Prestação
         em Desacordo
         Exceção: O evento não será exigido para CTe com
         tomador do exterior
```

## 12 Ajuste na regra que define prazo para CTe Complementar

```text
G161a    Se Tipo do CTe= 1 (Complementar), para cada chave         Obrig.    933    Rej.     Rejeição: Chave de acesso do CTe
H102a    de CTe informado:                                                                   complementado muito antiga
         Verificar se o Ano/Mês da chave de acesso são                                       [chCTe:
         anteriores a 12 meses da Data de Autorização do CTe                                 99999999999999999999999999999999999
                                                                                             999999999]
         Exceção: Em caso de modal ferroviário ou multimodal
         permitir até 24 meses da Data de Autorização do CTe
```

## 13 Eliminar as opções de contingência SVC da GTVe no Leiaute (Schema)

```text
A GTVe já possui previsão de emissão offline, portanto não há necessidade do schema e do ambiente de
autorização suportar emissão em contingência SVC
Alteração: tag tpEmis aceita apenas os valores 1 – Normal e 2- Contingência offline
```

## 14 Nova regra para CTe OS de Transporte de Valores

```text
        Devido a apuração do imposto na reforma tributária ser em razão da UF e município de destino, o CTe OS de
        Transporte de Valores deverá passar a exigir essas informações.
H020a    Se tipo de serviço = Transporte de Valores                 Obrig.    380     Rej.    Rejeição: UF e Município de Fim da
         - UF de fim e Município de Fim da prestação devem estar                              prestação devem estar preenchidas para
         preenchidos                                                                          Transporte de Valores
         Observação: Esta regra será aplicada em produção
         somente a partir de 05/01/2026
```

## 15 Ajuste em regras de validação do tomador Contribuinte Isento de IE

```text
G024     Rejeitar quando informado tomador como Contribuinte Obrig.           617    Rej.         Rejeição: UF do tomador não aceita
         Isento de Inscrição Estadual (indIEToma=2) em UF que                                     ISENTO com Inscrição Estadual
         não permite esta situação, conforme abaixo:
         AM, BA, CE, GO, MG, MS, MT, PE, RN, SE, SP, PI, PA, RJ
H093     Rejeitar quando informado tomador como Contribuinte Obrig.           617    Rej.         Rejeição: UF do tomador não aceita
         Isento de Inscrição Estadual (indIEToma=2) em UF que                                     ISENTO com Inscrição Estadual
         não permite esta situação, conforme abaixo:
         AM, BA, CE, GO, MG, MS, MT, PE, RN, SE, SP, PI, PA, RJ
I15                                                                 Obrig.
         Rejeitar quando informado tomador como Contribuinte Isento de        617
                                                                       Inscrição    Rej.        Rejeição: UF do tomador não aceita
         Estadual                                                                               ISENTO com Inscrição Estadual
         (indIEToma=2) em UF que não permite esta situação, conforme abaixo:
          AM, BA, CE, GO, MG, MS, MT, PE, RN, SE, SP, PI, PA, RJ
```

## 16 Nova regra de validação para o Aquaviário no CTe modelo 57

```text
Se CTe (modal) = 03-Aquaviário, Tipo de Navegação (tpNav)= 1   Obrig.   759   Rej.   Rejeição: O CST deve ser 00 para CTe
Cabotagem, e CNPJ do Emitente ou Remetente ou Tomador                                Aquaviário de cabotagem com CFOP 5352 ou
for igual ao CNPJ do Destinatário e CFOP=5352 ou 6352:                               6352, quando CNPJ do Emitente ou
- CST deve ser = 00                                                                  Remetente ou Tomador for igual ao CNPJ do
                                                                                     Destinatário
```

## 17 Preparação das expressões regulares do CTe para o futuro CNPJ Alfanumérico

```text
As alterações serão feitas no arquivo de tipos gerais e aplicam-se automaticamente a todos campos do tipo CNPJ
e Chave de acesso em qualquer um dos schemas do projeto CTe, entretanto, até que seja publicada uma Nota
Técnica que modifica as validações desses campos, as letras não devem ser utilizadas.

A expressão regular que valida um campo do tipo CNPJ é: [0-9]{14}
Alteração: a Expressão regular do CNPJ passa a aceitar letras maiúsculas nas primeiras 12 posições:
[A-Z0-9]{12}[0-9]{2}

Expressão Regular Atual da Chave de Acesso é: [0-9]{44}
Alteração: a expressão regular passa a suportar letras maiúsculas nas 12 primeiras posições que correspondem
ao CNPJ dentro da chave de acesso: [0-9]{6}[A-Z0-9]{12}[0-9]{26}
A expressão regular do QR Code também seguirá essa regra de formação na parte da chave de acesso.
```

## 18 Ampliação do cStat de retorno para 4 dígitos

```text
A expressão regular que define a tag cStat dos schemas de retorno de todos os serviços passa a suportar até
códigos com 4 dígitos.

Nova expressão regular para o tipo TStat do arquivo Tipos Geral: [0-9]{3,4}
```
