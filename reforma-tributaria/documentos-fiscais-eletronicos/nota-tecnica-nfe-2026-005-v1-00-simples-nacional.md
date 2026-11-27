---
titulo: "Nota Técnica NF-e/NFC-e nº 2026.005, versão 1.00, de 30 de outubro de 2026 (Simples Nacional na Reforma Tributária do Consumo)"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil / ENCAT - CONFAZ"
tipo: "Nota Técnica"
numero: "2026.005"
data: "2026-10-30"
ano: "2026"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS", "Simples Nacional"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY="
ementa: "Atualizações para o Simples Nacional na NF-e e na NFC-e: informações de IBS e CBS dos optantes e regras de validação correspondentes."
data_consulta: "2026-11-27"
versao_texto: "Versão 1.00 (PDF oficial, 30/10/2026)"
---

# Nota Técnica NF-e/NFC-e nº 2026.005, versão 1.00, de 30 de outubro de 2026 (Simples Nacional na Reforma Tributária do Consumo)

> **Nota editorial.** Texto extraído da camada de texto do PDF oficial da Nota Técnica 2026.005, versão 1.00, divulgado no Portal Nacional da NF-e (12 páginas), consultado em 27/11/2026. A data do documento (30/10/2026) é a de publicação da versão, lida na lista de Notas Técnicas do portal. Versão aprovada ou ratificada pelo Ato Técnico Conjunto Sufis/CGIBS nº 10/2026 (`reguladores/rfb/outros-atos/2026/ato-154369-10-2026.md`). Foram removidos a capa, o sumário, os cabeçalhos e rodapés repetidos e a numeração de página. Os 5 títulos de primeiro nível do sumário viraram seções e o texto de cada uma, com os quadros e os leiautes, ficou em bloco de texto que mantém as colunas do PDF. O texto que antecede esses títulos e não consta do sumário ficou em seção própria (Controle de Versões). Figuras e imagens do PDF não foram convertidas. Em caso de dúvida, prevalece o PDF. O portal só entrega o PDF com cookie de sessão; o link da fonte é a página de lista de Notas Técnicas, onde a versão consta como "Publicada em 30/10/2026".

## Controle de Versões

```text
 Versão       Publicação              Descrição

 1.00         10/2026                 Criação de campos relacionados a tributação do Simples Nacional

Histórico de Alterações / Cronograma

Versão                             Histórico de atualizações                              Implantação       Implantação
                                                                                             Teste           Produção
 1.00     Criação de campos relacionados a tributação do Simples Nacional                 Até 26/10/2026     16/11/2026
 1.00     Criação do Evento Tributação do Simples Nacional                               Implementação     Implementação
                                                                                              Futura           Futura
```

## 1. Introdução

```text
Esta Nota Técnica tem por objetivo disciplinar as adequações adicionais nos leiautes da NF‑e e da
NFC‑e (modelos 55 e 65), necessárias à implementação das disposições decorrentes da Reforma
Tributária do Consumo, regulamentada pela Lei Complementar nº 214/2025, aplicáveis às
operações realizadas por contribuintes optantes pelo Simples Nacional.

As alterações apresentadas visam viabilizar a apuração assistida do Simples Nacional, por meio da
captura estruturada, em nível de item do documento fiscal eletrônico, das informações
indispensáveis ao cálculo da Receita Bruta do Simples Nacional (RBSN) e da Receita Bruta Total
acumulada nos últimos 12 meses (RBT12), bem como ao cálculo do Imposto sobre Bens e Serviços
(IBS) e da Contribuição sobre Bens e Serviços (CBS) no âmbito desse regime.

Para atender a esse objetivo, esta Nota Técnica estabelece a inclusão de novos campos e regras
de validação destinados a identificar:
    •   a situação cadastral e o enquadramento do contribuinte no âmbito do Simples Nacional;
    •   a atividade econômica vinculada a cada item da NF‑e/NFC‑e;
    •   a adequada classificação tributária das operações para fins de incidência do IBS e da CBS;
    •   informações do IBS e da CBS para tributação pelo Simples Nacional.

Adicionalmente, esta Nota Técnica cria o evento fiscal específico denominado “Evento de
Tributação    do   Simples    Nacional”   (tpEvento   =   412140).   Este   evento   será   gerado
automaticamente pela Administração Tributária, com a finalidade de apoiar ações de conformidade
das informações fiscais.
```

## 2. Orientações gerais

```text
2.1 Criação do campo tpRegimeIBSCBS (tag: C21a)
Os contribuintes do Simples Nacional (CRT = 1 ou 2) que tenham optado pelo Regime Regular
do IBS/CBS devem informar:
    •   tpRegimeIBSCBS = 1.

Os contribuintes do Regime Normal (CRT = 3) que tenham solicitado opção pelo Simples
Nacional e cujo pedido tenha sido indeferido, estando este indeferimento em discussão na esfera
administrativa ou judicial, devem informar:
    •   tpRegimeIBSCBS = 2, se for optante pendente do Simples Nacional (CRT = 1) e não optante
        do regime regular do IBS e da CBS;
    •   tpRegimeIBSCBS = 3, se for optante pendente do Simples Nacional, excesso sublimite de
        receita bruta (CRT = 2) e não optante do regime regular do IBS e da CBS;
    •   tpRegimeIBSCBS = 4, se for optante pendente do Simples Nacional (vai migrar para CRT =
        1 ou 2) e optante do regime regular do IBS e da CBS.

Contribuintes nessa situação serão considerados, para todos os fins (inclusive quanto à
transferência de crédito, devolução e apuração), como pertencentes ao regime regular.

A tag não deve ser informada para situações diversas das mencionadas acima.

2.2 Criação do campo cAtivSN (tag: I17d)

Os contribuintes optantes pelo Simples Nacional (CRT = 1 ou 2), bem como os contribuintes do
Regime Normal com solicitação pendente de opção pelo Simples Nacional (CRT = 3 e
tpRegimeIBSCBS = 2, 3 ou 4), devem informar, para cada item da NF-e/NFC-e, o código de
atividade do Simples Nacional (cAtivSN).

2.3. Orientação de preenchimento do grupo IBSCBS no fornecimento

O preenchimento das informações de tributação do IBS e da CBS serão conforme a tabela abaixo,
exceto no caso de Tributação Monofásica de Combustíveis (art. 172 da LC 214/25).

              Regime de Apuração do Emitente                                               Como Preencher
                                                            CRT      tpRegimeIBSCBS   cAtivSN           gIBSCBS (*)               gTribSN
Simples Nacional com Regime Regular do IBS/CBS               1      Informar “1”      Informar Informar:                        Não informar
                                                                                                - gIBSUF
                                                                                                - gIBSMun
                                                                                                - gCBS
Simples Nacional, excesso sublimite de receita bruta          2     Informar “1”      Informar Informar:                        Não informar
com Regime Regular do IBS/CBS                                                                   - gIBSUF
                                                                                                - gIBSMun
                                                                                                - gCBS
Simples Nacional sem Regime Regular do IBS/CBS                1     Não informar      Informar Não informar                     Informar:
                                                                                                                                 - gIBSSN
                                                                                                                                 - gCBSSN
Simples Nacional, excesso sublimite de receita bruta          2     Não informar      Informar   Informar:                      Informar:
sem Regime Regular do IBS/CBS                                                                     - gIBSUF                       - gCBSSN
                                                                                                  - gIBSMun
                                                                                                  - gCBS, com alíquota zerada
Contribuinte do Regime Normal com opção pendente              3     Informar “2”      Informar   Informar:                      Informar:
pelo CRT=”1-Simples Nacional” sem regime regular                                                  - gIBSUF                       - gIBSSN
do IBS e da CBS                                                                                   - gIBSMun                      - gCBSSN
                                                                                                  - gCBS
Contribuinte do Regime Normal com opção pendente              3     Informar “3”      Informar   Informar:                      Informar:
pelo CRT=”2-Simples Nacional, excesso sublimite de                                                - gIBSUF                       - gCBSSN
receita bruta” sem regime regular do IBS e da CBS                                                 - gIBSMun
                                                                                                  - gCBS
Contribuinte do Regime Normal com opção pendente              3     Informar “4”      Informar   Informar:                      Não informar
pelo Simples Nacional (CRT=1 ou 2), com regime                                                    - gIBSUF
regular do IBS e da CBS                                                                           - gIBSMun
                                                                                                  - gCBS
              (*) informar o grupo gIBSCBS caso seja exigido pelo CST.

Caso seja informado CST = 620-Tributação Monofásica de Combustíveis, o grupo gIBSCBSMono
deve ser preenchido, e o grupo gTribSN não deve ser preenchido.

O Simples Nacional - Microempreendedor Individual - MEI (CRT = 4) não deve informar o grupo
IBSCBS.

2.4. Preenchimento do grupo IBSCBS na devolução/retorno por recusa

Nas notas com as finalidades e tipos apresentados a seguir, o grupo de tributação IBSCBS do item
deve ser espelho do item da nota de fornecimento referenciada.
    •   Nota de Devolução de mercadoria (tag: finNFe = 4);
    •   Nota de Crédito (tag: finNFe=5) do tipo “03=Retorno por Recusa Total na Entrega ou Por
        Não Localização do Destinatário na Tentativa de Entrega” (tag: tpNFCredito=03);
    •   Nota de Crédito (tag: finNFe=5) do tipo “06=Retorno por Recusa Parcial na Entrega” (tag:
        tpNFCredito=06);
    •   Nota de Débito (tag: finNFe=6) do tipo tpNFDebito=”09-Retorno por recusa parcial na
        entrega.
```

## 3. Leiaute da NF-e (Modelo 55 e 65)

```text
Grupo C. Identificação do Emitente da Nota Fiscal eletrônica
#         ID    Campo            Descrição                        Ele Pai     Tipo   Ocor.   Tam. Observação
    49b    C21a tpRegimeIBSCBS   Tipo de Regime de Apuração do     E C01       N      0-1     1   1=Contribuinte do Simples Nacional (CRT=1 ou 2)
                                 IBS e da CBS                                                       com opção pelo regime regular do IBS e da CBS;
                                                                                                  2=Contribuinte do Regime Normal (CRT=3)
                                                                                                    com opção pendente pelo CRT=”1-Simples Nacional” sem regime
                                                                                                     regular do IBS e da CBS;
                                                                                                  3=Contribuinte do Regime Normal (CRT=3)
                                                                                                    com opção pendente pelo CRT=”2-Simples Nacional, excesso
                                                                                                     sublimite de receita bruta” sem regime regular do IBS e da CBS;
                                                                                                  4=Contribuinte do Regime Normal (CRT=3)
                                                                                                    com opção pendente pelo Simples Nacional (CRT=1 ou 2), com
                                                                                                     regime regular do IBS e da CBS.

Grupo I. Produtos e Serviços da NF-e
#    ID        Campo             Descrição                        Ele   Pai   Tipo   Ocor.   Tam. Observação
116d I17d      cAtivSN           Código de atividade do Simples    E    I01    C      0-1     2   Código de atividade do Simples Nacional para cálculo dos tributos
                                 Nacional                                                         IBS/CBS.
                                                                                                  01=Revenda de mercadorias, venda de mercadorias industrializadas
                                                                                                     pelo contribuinte - Anexo I.
                                                                                                  02=Operações com os demais bens materiais, sem incidência de
                                                                                                     ICMS – Anexo I.
                                                                                                  03=Venda de mercadorias industrializadas pelo contribuinte, com
                                                                                                     industrialização incentivada na Zona Franca de Manaus - Anexo II.
                                                                                                  04=Operações com os demais bens materiais, com industrialização
                                                                                                     incentivada na Zona Franca de Manaus, sem incidência de ICMS -
                                                                                                     Anexo II.
                                                                                                  90=Operações não Tributáveis.
                                                                                                  Observação: informar somente quando o emitente for optante do
                                                                                                     Simples Nacional ou estiver com opção pendente.

Grupo UB. Informações dos tributos IBS / CBS e Imposto Seletivo
#        ID     Campo Descrição                                   Ele    Pai     Tipo Ocor. Tam. Observação
324.115a UB115a gTribSN Grupo de informações da composição         G    UB12       -   0-1
                        do valor do IBS e da CBS para o
                        Simples Nacional
324.115b UB115b gIBSSN Grupo de informações da composição         G     UB115a    -    0-1
                        do valor do IBS para o Simples
                        Nacional
324.115c UB115c pIBSSN Alíquota efetiva do IBS para os Optantes   E     UB115b    N    1-1   3v2-4 Observação: nos anos de 2027 e 2028, no caso de Compra
                        do Simples                                                                    Governamental:
                                                                                                    - se tpEnteGov igual a ”1-União”, pIBSSN deve ser zero;
                                                                                                    - se tpEnteGov diferente de ”1-União”, pIBSSN deve ser a alíquota
                                                                                                      efetiva do Simples Nacional para o IBS.
324.115d UB115d vIBSSN Valor do IBS para os Optantes do           E     UB115b    N    1-1   13v2
                       Simples Nacional
324.115e UB115e gCBSSN Grupo de informações da composição         G     UB115a    -    1-1
                       do valor da CBS para o Simples
                       Nacional
324.115f UB115f pCBSSN Alíquota efetiva da CBS para os Optantes   E     UB115e    N    1-1   3v2-4 Observação: nos anos de 2027 e 2028, no caso de Compra
                       do Simples                                                                     Governamental:
                                                                                                    - se tpEnteGov igual a ”1-União”, pCBSSN deve ser a soma das
                                                                                                      alíquotas efetivas de IBS e CBS para o Simples Nacional;
                                                                                                    - se tpEnteGov diferente de ”1-União”, pCBSSN deve ser a alíquota
                                                                                                      efetiva do Simples Nacional para a CBS.
324.115g UB115g vCBSSN Valor da CBS para os Optantes do           E     UB115e    N    1-1   13v2
                       Simples Nacional

Grupo W03. Total da NF-e - IBS / CBS / IS
#         ID      Campo Descrição                                 Ele    Pai     Tipo Ocor. Tam. Observação
355.29h   W59h    gTribSN Grupo de totais da composição do         G     W34       -   0-1
                          valor do IBS e da CBS para o Simples
                          Nacional
355.29i   W59i    vIBSSN Valor Total do IBS para os Optantes do   E     W59h      N    1-1   13v2
                          Simples Nacional
355.29j   W59j    vCBSSN Valor Total da CBS para os Optantes do   E     W59h      N    1-1   13v2
                          Simples Nacional
```

## 4. Regras de Validação

```text
Grupo W03. Total da NF-e - IBS / CBS / IS
Campo Modelo                                     Regra de Validação                                    Aplic. Msg                     Descrição Erro
W59h-10 55/65 Se não informado grupo de totais do IBS e da CBS para o Simples Nacional (tag:           Obrig. 1275 Rejeição: Grupo de totais do IBS e da CBS para o
              total/IBSCBSTot/gTribSN):                                                                            Simples Nacional não informado
                - Pelo menos um item possui o grupo gTribSN (id: UB115a) informado
W59h-20 55/65 Se informado grupo de totais do IBS e da CBS para o Simples Nacional (tag:               Obrig. 1276 Rejeição: Grupo de totais do IBS e da CBS para o
              total/IBSCBSTot/gTribSN):                                                                            Simples Nacional informado indevidamente
                - Nenhum item possui o grupo gTribSN (id: UB115a) informado
W59i-10 55/65 Se informado grupo de totais do IBS e da CBS para o Simples Nacional (tag:               Obrig. 1277 Rejeição: Total do IBS para o Simples Nacional difere
              total/IBSCBSTot/gTribSN):                                                                            da soma dos itens
                - O total do IBS para os Optantes do Simples Nacional (id: W59i) deve ser a soma dos
                  campos vIBSSN (id: UB115d) informados nos itens
W59j-10 55/65 Se informado grupo de totais do IBS e da CBS para o Simples Nacional (tag:               Obrig. 1284 Rejeição Total da CBS para o Simples Nacional difere
              total/IBSCBSTot/gTribSN):                                                                            da soma dos itens
                - O total da CBS para os Optantes do Simples Nacional (id: W59j) deve ser a soma dos
                  campos vCBSSN (id: UB115g) informados nos itens
```

## 5. Evento: Tributação do Simples Nacional

```text
4.1 Visão Geral

O evento “Tributação do Simples Nacional” (tpEvento = 412140) será gerado automaticamente pela Administração Tributária, com base nas NF-e e
NFC-e recebidas e emitidas por contribuintes enquadrados no Simples Nacional ou por contribuintes do Regime Normal que estejam com a opção
pelo Simples Nacional pendente. O CGIBS e RFB usarão os mesmos algoritmos para cálculo dos tributos e conformidade.

O Web Service de Registro de Evento possui uma parte geral, complementada por uma área específica para cada tipo de evento.

A parte geral se mantém a mesma para envio de todos os eventos e está especificada na seção 5.8 do Manual de Orientação do Contribuinte (MOC)
e na seção Web Service – NFeRecepcaoEvento – Parte Geral do MOC Online.

A mensagem de retorno será a padrão, especificada no Web Service de Registro de Eventos – Parte Geral, especificado no item 5.8.2 do MOC.

4.2 Especificação do Evento
      •     Função: Evento do fisco com informações da tributação do Simples Nacional para fins de composição da receita bruta, confissão de dívida e
            eventual geração de crédito de IBS/CBS nos termos do art. 23 da LC 123/06. O CGIBS e RFB usarão os mesmos algoritmos para cálculo
            dos tributos e conformidade.
      •     Autor: Administração Tributária
      •     Modelo: NF-e modelo 55/65
      •     Código do Tipo de Evento: 412140

4.2.1 Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e412140_v1.00.xsd
#         Campo                      Ele   Pai Tipo Ocor. Tam. Descrição/Observação
P17       detEvento                   G    P06   -   1-1    -  Detalhes do Evento
P18       versao                      A    P17 N     1-1   2v2 Versão do leiaute do evento (P16)
P19       descEvento                  E    P17 C     1-1   47 Descrição do evento: "Tributação do Simples Nacional"
P20       cOrgaoAutor                 E    P17 N     1-1    2 Código do Órgão Autor do Evento.
P21       tpAutor                     E    P17 N     1-1    1 Informar 5=Fisco.
                                                               Valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros Órgãos.

#     Campo                      Ele   Pai Tipo Ocor. Tam. Descrição/Observação
P22   verAplic                    E    P17 N     1-1  1-20 Versão do aplicativo do autor do evento.
P23   gTribItemSN                 G    P17   -  1-990   -   Detalhamento dos tributos por item. Múltiplas ocorrências (máximo = 990)
P24   nItem                       A    P23 N     1-1  1 - 3 Número do item (1-990)
P26   vRBSNitem                   E    P23 N     1-1 13v2 Valor da receita bruta do Simples Nacional atribuída ao item
P27   tpRBSN                      E    P23 N     1-1    1 Tipo de Receita Bruta do Simples Nacional referente ao cClassTrib do item:
                                                            0=Não é receita bruta;
                                                            1=Receita bruta - interna;
                                                            2=Receita bruta - interna sem cálculo de IBS e CBS;
                                                            3=Receita bruta - exportação direta;
                                                            4=Receita bruta - exportação indireta;
                                                            5=Receita bruta - mercado interno e exportação;
                                                            9=Fornecimento incompatível com SN.
P28   pIBSSN                      E    P23 N     0-1 3v2-4 Alíquota aplicável de cálculo do IBS referente ao item
P29   vIBSSN                      E    P23 N     0-1 13v2 Valor do IBS devido pelo Simples Nacional
P30   pCBSSN                      E    P23 N     0-1 3v2-4 Alíquota aplicável de cálculo da CBS referente ao item
P31   vCBSSN                      E    P23 N     0-1 13v2 Valor da CBS devida pelo Simples Nacional
P32   vIBSPendSusp                E    P23 N     0-1 13v2 Valor do IBS pendente ou suspenso referente ao item
P33   vCBSPendSusp                E    P23 N     0-1 13v2 Valor da CBS pendente ou suspenso referente ao item
P34   gTotalSN                    G    P17   -   1-1    -   Totais da NF-e
P35   vRBSNtot                    E    P34 N     1-1 13v2 Valor total da receita bruta do Simples Nacional, correspondente ao somatório dos valores atribuídos aos
                                                            itens da NF-e.
P36 vIBSSNtot                     E    P34 N     0-1 13v2 Valor total do IBS devido pelo Simples Nacional apurado no documento
P37 vIBSSNtotPendSusp             E    P34 N     0-1 13v2 Valor total do IBS devido pelo Simples Nacional cuja apropriação encontra-se pendente ou com exigibilidade
                                                            suspensa
P38 vCBSSNtot                     E    P34 N     0-1 13v2 Valor total da CBS devida pelo Simples Nacional apurada no documento
P39 vCBSSNtotPendSusp             E    P34 N     0-1 13v2 Valor total da CBS devida pelo Simples Nacional cuja apropriação encontra-se pendente ou com
                                                            exigibilidade suspensa

4.2 Cancelamento do Evento
O cancelamento do evento Tributação do Simples Nacional será feito por meio do evento de cancelamento genérico 110001 - Cancelamento de
Evento.
```
