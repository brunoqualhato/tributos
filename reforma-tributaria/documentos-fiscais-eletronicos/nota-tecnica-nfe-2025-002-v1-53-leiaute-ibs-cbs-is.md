---
titulo: "Nota Técnica NF-e/NFC-e nº 2025.002-RTC, versão 1.53, de 30 de outubro de 2026 (Reforma Tributária do Consumo: leiaute de IBS, CBS e IS)"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil / ENCAT - CONFAZ"
tipo: "Nota Técnica"
numero: "2025.002"
data: "2026-10-30"
ano: "2026"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS", "Imposto Seletivo"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY="
ementa: "Nota técnica de adequação dos leiautes da NF-e (modelo 55) e da NFC-e (modelo 65) para inclusão dos campos e das regras de validação referentes à Reforma Tributária do Consumo - RTC (IBS, CBS e Imposto Seletivo)."
data_consulta: "2026-11-27"
versao_texto: "Versão 1.53 (PDF oficial, 30/10/2026)"
---

# Nota Técnica NF-e/NFC-e nº 2025.002-RTC, versão 1.53, de 30 de outubro de 2026 (Reforma Tributária do Consumo: leiaute de IBS, CBS e IS)

> **Nota editorial.** Texto extraído da camada de texto do PDF oficial da Nota Técnica 2025.002, versão 1.53, divulgado no Portal Nacional da NF-e (96 páginas), consultado em 27/11/2026. A data do documento (30/10/2026) é a de publicação da versão, lida na lista de Notas Técnicas do portal. Versão aprovada ou ratificada pelo Ato Técnico Conjunto Sufis/CGIBS nº 10/2026 (`reguladores/rfb/outros-atos/2026/ato-154369-10-2026.md`). Foram removidos a capa, o sumário, os cabeçalhos e rodapés repetidos e a numeração de página. Os 13 títulos de primeiro nível do sumário viraram seções e o texto de cada uma, com os quadros e os leiautes, ficou em bloco de texto que mantém as colunas do PDF. O texto que antecede esses títulos e não consta do sumário ficou em seção própria (Controle de Versões). Figuras e imagens do PDF não foram convertidas. Em caso de dúvida, prevalece o PDF. O portal só entrega o PDF com cookie de sessão; o link da fonte é a página de lista de Notas Técnicas, onde a versão consta como "Publicada em 30/10/2026". Sucede a versão 1.52, aprovada pelo Ato Técnico Conjunto Sufis/CGIBS nº 8/2026 (`reguladores/rfb/outros-atos/2026/ato-153886-8-2026.md`). A seção 1 do PDF informa que esta NT substitui, no âmbito da NF-e e da NFC-e, a NT 2024.002 v1.10 (`reforma-tributaria/split-payment/nota-tecnica-nfe-2024-002-ibs-cbs-is.md`). No PDF, os Anexos I e II só trazem a indicação "Tabela a ser publicada" e os Anexos III e IV remetem à tabela publicada na aba "Documentos", opção "Diversos", do Portal Nacional da NF-e; as tabelas não constam do texto.

## Controle de Versões

```text
 Versão      Publicação              Descrição

 1.00        03/2025                 Inserção de campos de controle e criação de eventos para utilização na apuração do IBS,
                                     CBS e IS

 1.01        04/2025                 Ajustes e correções

 1.10        06/2025                 Cria campos, cria e altera regras de validação, cria eventos para apuração do IBS/CBS

 1.20        07/2025                 Detalhamentos do cronograma, novas regras de validação e ajustes diversos

 1.30        10/2025                 Novos campos, novas regras de validação, alteração no cronograma e ajustes diversos

 1.31        11/2025                 Correção em regras de validação

 1.32        11/2025                 Correção em regras de validação

 1.33        12/2025                 Correção em regras de validação e alteração da data de início de regra de validação

 1.34        12/2025                 Correção em regras de validação

 1.35        03/2026                 Postergada a aplicação das regras de validação vinculadas à Tributação Monofásica no
                                     ambiente de Homologação.

 1.36        04/2026                 Alterações previstas nos Ajustes SINIEF nº 49/25 e 8/26.

 1.40        05/2026                 Cria campos, cria e altera regras de validação e ajustes diversos

 1.50        06/2026                 Reformulação do layout da tributação monofásica de combustíveis e regras de validação

 1.51        07/2026                 Alteração de regras de validação

 1.52        09/2026                 Alteração de regras de validação

 1.53        10/2026                 Alteração de regras de validação

Histórico de Alterações / Cronograma

 Versão                            Histórico de atualizações                                Implantação        Implantação
                                                                                               Teste            Produção
                  Inserção de campos de controle e criação de eventos para
   1.01                                                                                      01/07/2025         01/10/2025
                  utilização na apuração do IBS, CBS e IS
   1.01           Aplicação das Regras de Validação                                          01/07/2025           01/2026

                  Implantação de novo schema com os campos para apuração do                 De 07/07/2025       06/10/2025
  1.10**          IBS, CBS e IS, com preenchimento opcional, conforme
                  detalhamento do cronograma abaixo.                                       até 28/07/2025*

                  Aplicação das regras de validação, conforme detalhamento do               De 07/07/2025       06/10/2025
  1.10**
                  cronograma abaixo.                                                       até 11/08/2025*
                  Implantação dos eventos para utilização na apuração do IBS, CBS
   1.10                                                                                     25/08/2025***       06/10/2025
                  e IS.

                  Detalhamentos do cronograma, novas regras de validação e
   1.20                                                                                  08/09/2025       06/10/2025
                  ajustes diversos.
                  Entrada do schema, das Regras de Validação e dos Eventos, com
   1.30                                                                                Até 29/10/2025     10/11/2025
                  exceção das Regras de Validação listadas no item a seguir.
                  Entrada das seguintes Regras de Validação: B10a-10, B10a-20,
                                                                                       Até 24/11/2025     02/02/2026
                     B10a-30, B10a-40, B10a-50, B25-110, B25-120, I05k-10, I05k-
                     20, UB112-10, UB112-20, UB112-30, UB116-10, UB116-20,
   1.30              UB116-30, UB120-10, UB120-20, UB122-10, UB123-10, UB123-
                     20, UB125-10, UB126-10, UB127-10, UB127-20, UB129-10,
                     UB130-10, UB131-10, UB131-20, UB131-30, UB131-40, UB131-
                     50, UB132-10, UB133-10, W59f-10, W59g-10
                  Início da obrigatoriedade da informação dos novos tributos (RV       Implementação    Implementação
   1.30
                  UB12-10)                                                                 futura           futura
                  Correção nas regras de validação B25-80, B25-90, B25-100, Q01-
                                                                                       Até 14/11/2025     17/11/2025
                     20, S01-20, UB56-10 e VC02-30.
   1.31
                  Inclusão de observação explicativa nas regras de validação UB27-
                     10, UB46-10 e UB65-10, sem impacto nas validações.
                  Correção nas regras de validação B25b-20, 3BA02-10, 3BA02-70
   1.32                                                                                Até 01/12/2025     04/12/2025
                  e NA01-20.
                  Correção na regra de validação UB56-10, permitindo alíquota zero
                                                                                       Até 10/12/2025   Até 15/12/2025
                     para a CBS em operações específicas dentro de áreas
                     incentivadas.
                  Ajuste para permitir a informação do grupo de Redução de
   1.33              Alíquota (gRed) somente quando a alíquota for maior que zero
                     (regras de validação: UB26-15, UB26-20, UB45-15, UB45-20,
                     UB64-15 e UB64-20).
                  Alteração da data de início da aplicação da regra de validação
                     UB12-10.
                  Regras de validação desabilitadas: UB26-15, UB45-15 e UB64-15.
   1.34                                                                                Até 10/12/2025   Até 15/12/2025
                  Regras de validação alteradas: UB26-20, UB45-20, e UB64-20.
                  Regras de validação alteradas: UB13-40, UB84a-10, UB90-10,
   1.35                                                                                Até 06/04/2026   Não se aplica
                     UB94-10, UB99-10.
                  Regras de validação incluídas: I08-141.
                                                                                       Até 01/07/2026     03/08/2026
                  Regras de validação alteradas: I08-140, I08-144, VC02-07, VC02-10,
   1.36              UB18-10, UB37-10, UB56-10, B25-80
                  Criação de novo tipo de nota de crédito: 06=Retorno por recusa
                     parcial na entrega.
                  Criação do campo para o Código Indicador do Local da Operação
                                                                                       Até 01/07/2026     03/08/2026
                     de Fornecimento (cIndOp, B25d);
                  Atualização de valores de tpEnteGov (BB02), tpOperGov (BB04) e
                     criação do campo refDFeAnt (BB05);
                  Criação do campo para Inscrição Suframa do Emitente (ISUFemit,
                     C22);
                  Atualização dos grupos de devolução de tributos (gDevTrib) -
                     cashback;
                  Criação do grupo gALCZFMCBS (UB66a);
                  Validações por cClassTrib x tipo de nota de débito e crédito;
                  Alteração da data de início da aplicação da regra de validação
   1.40
                     UB12-10.
                  Ajuste no layout do Evento 211110;
                  Eliminação do Evento 211120;
                  Regras de validação incluídas: B25d-10, B25d-20, B25d-30, BB05-
                     10, BB05-20, BB05-30, BB05-40, BB05-50, BB05-60, BB05-70,
                     BB05-80, BB05-90, BB05-100, BB05-110, BB05-120, BB05-130,
                     BB05-140, BB05-150, BB05-160, BB05-170, BB05-180, BB05-
                     190, BB05-200, C22-10, C22-20, UB14-60, UB14-70, UB14-80,
                     UB24-10, UB43-10, UB56-20, UB62-10, UB62a-10, UB63-10,
                     UB66a-10, UB66a-20, UB66c-10, UB66e-10, VC02-40, VC02-50,
                     VC03-20;

                  Regras de validação alteradas: B10a-30, BB02-10, E18-30, UB26-
                    20, UB45-20, UB56-10, UB64-20, UB82a-10, UB123-10, UB127-
                    10, UB133-10 , VB01-05, VB01-10, VB01-20, VC02-15, W07-10,
                    UB12-10.
                  Na devolução, o referenciamento passa a ser realizado
                                                                                      Até 01/07/2026      03/11/2026
                    exclusivamente no grupo “DFeReferenciado” (regra de
   1.40
                    validação VC02-14)
                  Observação: Regra atualizada na versão v1.53.

                  Reformulação do layout da tributação monofásica de                  Até 01/09/2026      03/11/2026
   1.50
                    combustíveis e regras de validação                                                    16/11/2026
                  Alteração de regras de validação: UB13-30, UB13-40, UB18-10,
                                                                                      Até 01/09/2026      05/10/2026
                     UB22-20, UB26-20, UB37-10, UB40-10, UB45-20, UB56-20, UB59-
   1.51              10, UB64-20; B25-80, I08-140, I08-144, UB13-20, UB13-40, UB22-
                     10, UB40-20, UB45-10, UB56-10, UB59-20, UB64-10, UB66a-20,
                     UB82a-30, UB112-10, UB116-10, UB131-20, VC02-14, VC02-30.
                  Alteração do cronograma de implantação das regras de validação
   1.51                                                                               Até 03/08/2026      03/08/2026
                     UB12-10
                                                                                      Até 05/10/2026    Até 03/11/2026
   1.52           Correção na RV VC02-50
                                                                                      Até 26/10/2026    Até 16/11/2026
                  Alteração da data de implantação da VC02-14 em Produção,
                                                                                            -             03/11/2026
   1.52              mudou de 05/10/2026 para 03/11/2026
                  Observação: Regra atualizada na versão v1.53.
                  Nas operações de devolução, é permitido referenciar a Chave de
                                                                                      Até 09/11/2026    Até 16/11/2026
                     Acesso no cabeçalho ou no item. O campo nItem é opcional.
   1.53           Regras de validação alteradas: UB12-10, VC02-14, VC02-20,
                    VC02-30, VC02-40, VC02-50, VC03-20, 3BA02-50, 3BA02-
                    54, 3BA02-58, 3BA02-64, 3BA02-68.
                  A devolução com Chave de Acesso referenciada no cabeçalho
                                                                                      Até 09/11/2026      16/11/2026
   1.53             passa a ser limitada a uma única ocorrência.
                  Regra de validação alterada: B25-40
* Implantação em homologação pode variar por UF neste período.
** As regras de validação serão aplicadas exclusivamente nos documentos fiscais que contenham o preenchimento dos
    campos referentes ao Imposto sobre Bens e Serviços (IBS), à Contribuição sobre Bens e Serviços (CBS) e ao Imposto
    Seletivo (IS). Isso significa que, se esses campos não estiverem preenchidos, as validações específicas para o IBS,
    CBS e IS não serão executadas.
** A validade jurídica das informações dos novos tributos se dará conforme os prazos estabelecidos na legislação,
    independentemente de já estarem preenchidos.
*** O schema dos novos Eventos será disponibilizado até dia 11/08/2025.

Detalhamento do Cronograma
Datas para CRT 3=Regime Normal:
                  Homologação                                Produção

 Julho/2025       Preenchimento dos campos IBS/CBS é         Campos do IBS/CBS ainda não implantados. Caso
                  facultativo. Se preenchidos, as RV serão   informados, ocasionará erro de schema.
                  aplicadas.

 Outubro/2025     Preenchimento dos campos IBS/CBS é         Preenchimento dos campos IBS/CBS é facultativo.
                  facultativo. Se preenchidos, as RV serão   Se preenchidos, as RV serão aplicadas.
                  aplicadas.
                                                             Sem valor jurídico para os novos tributos.

 Janeiro/2026     Preenchimento dos campos IBS/CBS é         Preenchimento dos campos IBS/CBS não será
                  facultativo. Se preenchidos, as RV serão   exigido por regra de validação, porém permanece
                  aplicadas.                                 obrigatório conforme a legislação vigente. Para as
                                                             NF-e e NFC-e com IBS/CBS as RV serão aplicadas.
                                                             Com valor jurídico para os novos tributos a partir de
                                                             01/01/2026.

 01/07/2026       Preenchimento dos campos IBS/CBS é         Preenchimento dos campos IBS/CBS não será
                  obrigatório.                               exigido por regra de validação, porém permanece
                                                             obrigatório conforme a legislação vigente. Para as
                                                             NF-e e NFC-e com IBS/CBS as RV serão aplicadas.
                                                             Com valor jurídico para os novos tributos a partir de
                                                             01/01/2026.

As orientações para CRT=1-Simples Nacional, CRT=2-Simples Nacional-Excesso de Sublimite,
CRT=4-MEI e Tributação Monofásica serão publicadas em NT futura, tendo em vista que a
tributação do IBS/CBS/IS para estes contribuintes ocorre somente a partir de 2027, conforme
disposto no Art. 348 da LC 214/25.
```

## 1. Introdução

```text
A Lei Complementar 214/2025 que institui o Imposto sobre Bens e Serviços (IBS), a Contribuição
Social sobre Bens e Serviços (CBS) e o Imposto Seletivo (IS), cria o Comitê Gestor do IBS e altera
a legislação tributária, definiu na Seção VIII – Disposições transitórias, Art. 62, a obrigatoriedade
para a União, os Estados, o Distrito Federal e os Municípios adaptarem os sistemas autorizadores
de Documentos Fiscais Eletrônicos (DFe) vigentes para utilização de leiaute padronizado, que
permita aos contribuintes informarem os dados relativos ao Imposto sobre Bens e Serviços (IBS),
Contribuição sobre Bens e Serviços (CBS) e Imposto Seletivo (IS).

Esta Nota Técnica substitui, no âmbito da NFe/NFCe, a RT NT 2024.002 - IBS/CBS v1.10, que cria
novos eventos e modifica o leiaute da NF-e e NFC-e, inserindo os grupos e campos opcionais
relacionados à tributação dos novos Impostos, em atendimento às alterações previstas na Emenda
Constitucional 132 de 20 de dezembro de 2023 e Lei Complementar 214 de 16 de janeiro de 2025
para implementação da Reforma Tributária, com data de implantação em ambiente de produção
prevista para outubro de 2025, de modo a viabilizar sua efetiva operacionalização a partir de janeiro
de 2026.

Vale destacar que, em Produção, no ano de 2025 as informações de tributação relativas ao IBS,
CBS e IS serão opcionais e somente serão validadas se forem preenchidas. A partir de janeiro de
2026, as novas regras de validação referentes à tributação do IBS e da CBS serão aplicadas.

As datas dos campos e das regras de validação estão definidas no Histórico de Alterações /
Cronograma.

Como as discussões envolvendo a implantação da Reforma Tributária ainda estão em curso,
esclarecemos que esta NT será ajustada ao longo do seu processo de execução, da mesma forma
como ocorre com as demais NT já implementadas.
```

## 2. Tipos Básicos da Tributação

```text
Em busca de uma padronização entre os diversos documentos fiscais eletrônicos existentes, esta
NT introduz o arquivo “DFeTiposBasicos_v1.00.xsd” ao conjunto dos arquivos que compõem o
“esquema XML” de todos os Documentos Fiscais Eletrônicos - DF-e, entre eles a NF-e e NFC-e.

Este arquivo define de forma estruturada a previsão de campos a serem informados para o registro
das informações referentes a tributação do IBS e da CBS em um tipo complexo referenciado no
leiaute padrão da NF-e e NFC-e conforme estrutura demonstrada no item 5, e também será utilizado
nos demais documentos fiscais eletrônicos.
```

## 3. Código de Classificação Tributária do IBS/CBS

```text
O grupo de informações do IBS, CBS e IS associado aos itens do documento fiscal contém o Código
de Situação Tributária (CST) e Código de Classificação Tributária (cClassTrib) do IBS, CBS e IS.

O Informe Técnico 2025.002 RTC divulga a publicação da tabela com esta codificação, que está
disponível no Portal Nacional da NF-e (www.nfe.fazenda.gov.br), na aba “Documentos”, opção
“Diversos”.

Cada código “cClassTrib” corresponde a um dispositivo específico da Lei Complementar 214/ 2025,
tornando objetiva a informação do contribuinte sobre como é realizada a tributação do IBS e da CBS
para cada item da NF-e. A tabela também contém indicadores que vinculam de forma dinâmica
códigos “CST-IBS/CBS” e “cClassTrib” com as Regras de Validação descritas na Nota Técnica
2025.002 – IBS/CBS/IS, ou que contêm informações necessárias para a preparação das apurações
assistidas do IBS e da CBS, em atendimento ao disposto na Lei Complementar 214/ 2025.

Destaca-se que a tabela poderá sofrer alterações em virtude de aperfeiçoamentos, novidades
introduzidas em sede de Regulamento, ou para atender a necessidades relacionadas com a
apuração assistida do IBS e da CBS.
```

## 4. Finalidade Débito e Finalidade Crédito da NF-e

```text
Notas de Débito e Crédito são nomes de instrumentos utilizados mundialmente para documentar
situações contábeis onde é necessário corrigir informações comerciais que foram registradas em
um documento, que no Brasil é a Nota Fiscal.

Esta Nota Técnica cria na NF-e modelo 55 as finalidades de emissões correspondentes. O sentido
das palavras “débito” e “crédito” sempre se referem ao ponto de vista do emissor:
  • Uma nota de débito documenta uma situação na qual o emitente registra um aumento no
     imposto devido (consequentemente, uma redução no imposto devido pelo adquirente, que é
     o destinatário);
  • Uma nota de crédito documenta uma situação na qual o emitente registra uma redução no
     imposto devido (consequentemente, um aumento no imposto devido pelo adquirente, que é o
     destinatário);

As finalidades de emissão “Nota de Ajuste” e “Nota Complementar”, já existentes, são casos
especiais de Nota de Débito; uma nota de entrada emitida para documentar, por exemplo, a
devolução de mercadoria que havia sido vendida a um consumidor final, é um caso especial de
Nota de Crédito.

A regulamentação do IBS e da CBS disporá sobre a utilização de notas de crédito e notas de débito
para lançamentos de ajuste, com a finalidade de instrumentalizar a preparação da declaração

assistida a ser oferecida para os contribuintes, de maneira automatizada, a partir de documentos
fiscais eletrônicos, em cumprimento ao que preconiza a LC 214/2025.

Nos termos do Ajuste SINIEF nº 49/2025, a NF-e passa a admitir essas finalidades em hipóteses
específicas, como instrumento formal de documentação de ajustes, produzindo reflexos no ICMS,
observado o tratamento próprio desse tributo, sendo vedada sua utilização fora das hipóteses
expressamente previstas na legislação aplicável.
```

## 5. Padrões de Numeração

```text
5.1. Protocolo de Autorização de Uso e Código do Status da Resposta
O sistema da Nota Fiscal tem atingido alguns limites, tornando necessária a ampliação dos campos de código de status de resposta e número do
protocolo de autorização.

No caso do código de status de resposta foi aumentado o campo para 4 posições, sendo que essa nova faixa de numeração passará a ser utilizada
para as rejeições exclusivas aos novos impostos (IBS, CBS, IS).

Em relação ao número do protocolo, algumas UF estão perto de atingir a capacidade máxima do campo para numeração das NFC-e durante o ano.
Ressalta-se que o protocolo de autorização é composto por:
  - 1 dígito para Tipo Autorizador;
  - 2 dígitos para o código da UF;
  - 2 dígitos para o ano;
  - 10 dígitos para o número sequencial dos documentos autorizados para o mesmo modelo de DF-e;

No caso do número do protocolo, somente as UF que estiverem perto do esgotamento da numeração vão adotar o número sequencial de documentos
autorizados no ano com 12 posições. Dessa forma, o número do protocolo poderá conter 15 ou 17 posições, conforme o modelo de DF-e e a UF.

Os próximos itens documentam a alteração dos leiautes que contém os campos alterados.

Nota: atualmente, somente a SEFAZ-SP irá adotar o protocolo com 17 posições para a NFC-e.

5.2. Protocolo de Autorização da NF-e / NFC-e – Resposta Síncrona
Alteração da seção 5.1.2 do MOC - Leiaute Mensagem de Retorno.

Schema XML: retEnviNFe_v2.00.xsd
  #      Campo   Ele Pai Tipo Ocor.       Tam.                                                  Descrição/Observação
 AR01 retEnviNFe Raiz -    -    -            -  TAG raiz da Resposta
 AR02 versao      A AR01  N    1-1        1-2v2 Versão do leiaute
 AR03 tpAmb       E AR01  N    1-1           1  Identificação do Ambiente: 1 – Produção/2 - Homologação
 AR04 verAplic    E AR01  C    1-1         1-20 Versão do Aplicativo que recebeu o Lote.
                                                A versão deve ser iniciada com a sigla da UF nos casos de WS próprio ou a sigla SVAN ou SVRS nos demais casos.
 AR05 cStat         E   AR01   N    1-1     3-4 Código do status da resposta (vide item 5.2)
 AR06 xMotivo       E   AR01   C    1-1   1-255 Descrição literal do status da resposta
 AR06a cUF          E   AR01   N    1-1      2  Código da UF que atendeu a solicitação.

   #     Campo        Ele Pai Tipo Ocor.            Tam.                                                 Descrição/Observação
 AR06b dhRecbto        E AR01  D    1-1                   Preenchido com a data e hora do processamento (informado também no caso de rejeição).
                                                          Formato: “AAAA-MM-DDThh:mm:ssTZD” (UTC - Universal Coordinated Time).
 AR07 infRec          CG AR01         -     0-1       -   Dados do Recibo do Lote (Só é gerado se o Lote for aceito e o processamento for assíncrono)
 AR08 nRec             E AR07         N     1-1      15 Número do Recibo gerado pelo Portal da Secretaria de Fazenda Estadual (vide item 5.5).
 AR10 tMed             E AR07         N     1-1     Nv1-4 Tempo médio de resposta do serviço (em segundos) dos últimos 5 minutos (vide item 5.7).
                                                          Nota: Caso o tempo médio de resposta fique abaixo de 1 (um) segundo, o tempo será informado como 1 segundo. Arre-
                                                             dondar as frações de segundos para cima.
      -x-
 AR11 protNFe         CG AR01         -     0-1       -    Dados do Protocolo de recebimento da NF-e gerado no caso do processamento síncrono do Lote de NF-e. Ver descrição
                                                           do “protNFe” no item 4.2.2.

 #        Campo           Ele Pai Tipo Ocor. Tam.                                                  Descrição/Observação
PR01 protNFe              Raiz  -   -    -     -  TAG raiz do Protocolo de recebimento da NFe
PR02 versao                 A PR01 N    1-1   2v2 Versão do leiaute das informações de Protocolo.
PR03 infProt               G PR01   -   1-1    -  Informações do Protocolo de resposta. TAG a ser assinada
PR04 Id                    ID PR03 C    0-1    -  Identificador da TAG a ser assinada, somente precisa ser informado se a UF assinar a resposta. Em caso de assinatura
                                                  da resposta pela SEFAZ preencher o campo com o Nro do Protocolo, precedido com o literal “ID”
PR05 tpAmb                  E PR03 N    1-1    1 Identificação do Ambiente: 1 – Produção/2 - Homologação
PR06 verAplic               E PR03 C    1-1  1-20 Versão do Aplicativo que processou o Lote.
                                                  A versão deve ser iniciada com a sigla da UF nos casos de WS próprio ou a sigla SVAN ou SVRS nos demais casos.
PR07 chNFe                  E PR03 N    1-1   44 Chave de Acesso da NF-e (vide item 5.4)
PR08 dhRecbto               E PR03 D    1-1    -  Preenchido com a data e hora do processamento (informado também no caso de rejeição).
                                                  Formato: “AAAA-MM-DDThh:mm:ssTZD” (UTC - Universal Coordinated Time).
PR09 nProt                  E PR03 N    0-1 15,17 Número do Protocolo da NF-e (vide item 5.8)
PR10 digVal                 E PR03 C    0-1   28 Digest Value da NF-e processada. Utilizado para conferir a integridade da NFe original.
PR11 cStat                  E PR03 N    1-1   3-4 Código do status da resposta para a NF-e (vide item 5.2).
PR12 xMotivo                E PR03 C    1-1 1-255 Descrição literal do status da resposta para a NF-e.
PR13 Signature             G PR01 xml   0-1    -  Assinatura XML do grupo identificado pelo atributo “Id”
                                                  A decisão de assinar a mensagem fica a critério da UF interessada.

5.3. Protocolo de Autorização da NF-e – Resposta Assíncrona (Consulta Recibo)
Alteração da seção 5.2.2 do MOC - Leiaute Mensagem de Retorno.

Retorno: Estrutura XML com o resultado do processamento da mensagem de envio de lote de NF-e.
  * Para cada Protocolo de uma NF-e processada teremos o seguinte leiaute:

Schema XML: retConsReciNFe_v4.00.xsd
   #            Campo          Ele    Pai    Tipo     Ocor.    Tam.                                       Descrição/Observação
  PR01          protNFe        Raiz    -       -        -        -    TAG raiz do Protocolo de recebimento da NFe

   #          Campo           Ele    Pai   Tipo   Ocor.    Tam.                                              Descrição/Observação
  PR02        versao           A    PR01    N      1-1      2v2    Versão do leiaute das informações de Protocolo.
  PR03        infProt          G    PR01     -     1-1       -     Informações do Protocolo de resposta.
                                                                   TAG a ser assinada
  PR04              Id        ID    PR03     C     0-1       -     Identificador da TAG a ser assinada, somente precisa ser informado se a SEFAZ Autorizadora assinar a
                                                                   resposta. Neste caso, preencher o campo com o Número do Protocolo, precedido com o literal “ID”
  PR05         tpAmb          E     PR03     N     1-1       1     Identificação do Ambiente: 1=Produção/2=Homologação
  PR06        verAplic        E     PR03     C     1-1      1-20   Versão do Aplicativo que processou o Lote. A versão deve ser iniciada com a sigla da UF nos casos de
                                                                   WS próprio ou a sigla SVAN ou SVRS nos demais casos.
  PR07        chNFe           E     PR03     N     1-1      44     Chave de Acesso da NF-e
  PR08       dhRecbto         E     PR03     D     1-1       -     Preenchido com a data e hora do processamento (informado também no caso de rejeição).
                                                                   Formato: “AAAA-MM-DDThh:mm:ssTZD” (UTC – Universal Coordinated Time).
  PR09            nProt       E     PR03     N     0-1     15,17   Número do Protocolo da NF-e, conforme item 4.3.5 do MOC
  PR10            digVal      E     PR03     C     0-1      28     Digest Value da NF-e processada
                                                                   Utilizado para conferir a integridade da NFe original.
  PR11        cStat           E     PR03     N     1-1      3-4    Código do status da resposta
  PR12       xMotivo          E     PR03     C     1-1     1-255   Descrição literal do status da resposta para a NF-e.
  PR13    Sequência XML       G     PR03           0-1             Grupo de informações para envio de mensagens do interesse da SEFAZ (Criado na NT 2018.005)
  PR14        cMsg            E     PR13     N     0-1      1-4    Código da Mensagem. (Criado na NT 2018.005)
  PR15        xMsg            E     PR13     C     1-1     1-200   Mensagem da SEFAZ para o emissor. (Criado na NT 2018.005)
  PR90      Signature         G     PR01    xml    0-1       -     Assinatura XML do grupo identificado pelo atributo “Id”
                                                                   A decisão de assinar a mensagem fica a critério da UF interessada.

5.4. Protocolo de Autorização do Pedido de Inutilização
Alteração da seção 5.3.2 do MOC - Leiaute Mensagem de Retorno.

Schema XML: retInutNFe_v4.00.xsd
  #         Campo          Ele Pai Tipo Ocor. Tam.                                                  Descrição/Observação
 DR01 retInutNFe           Raiz  -   -     -       -  TAG raiz da Resposta
 DR02 versao                 A DR01 N     1-1 1-2v2 Versão do leiaute
 DR03 infInut               G DR01   -    1-1      -  Dados da resposta - TAG a ser assinada
 DR04 Id                    ID DR03 C     0-1     17 Identificador da TAG a ser assinada, somente precisa ser informado se a UF assinar a resposta. Em caso de assina-
                                                      tura da resposta pela SEFAZ preencher o campo com o Nro do Protocolo, precedido com o literal “ID”.
 DR05 tpAmb                  E DR03 N     1-1      1 Identificação do Ambiente: 1 – Produção/2 – Homologação
 DR06 verAplic               E DR03 C     1-1    1-20 Versão do Aplicativo que processou o pedido de inutilização.
                                                      A versão deve ser iniciada com a sigla da UF nos casos de WS próprio ou a sigla SVAN ou SVRS nos demais casos.
 DR07 cStat                  E DR03 N     1-1     3-4 Código do status da resposta (vide item 5.2).
 DR08 xMotivo                E DR03 C     1-1 1-255 Descrição literal do status da resposta.
 DR09 cUF                    E DR03 N     1-1      2 Código da UF que atendeu a solicitação
                                     Os campos a seguir são obrigatórios no caso de homologação da inutilização cStat=102.
                                             Os campos de dhRecbto e nProt não serão preenchidos em caso de erro

  #         Campo           Ele    Pai Tipo Ocor. Tam.                                                 Descrição/Observação
 DR10 ano                    E    DR03  N    0-1    2 Ano de inutilização da numeração
 DR11 CNPJ                   E    DR03  C    0-1   14 CNPJ do emitente
 DR12 mod                    E    DR03  N    0-1    2 Modelo da NF-e
 DR13 serie                  E    DR03  N    0-1   1-3 Série da NF-e
 DR14 nNFIni                 E    DR03  N    0-1   1-9 Número da NF-e inicial a ser inutilizada
 DR15 nNFFin                 E    DR03  N    0-1   1-9 Número da NF-e final a ser inutilizada
 DR16 dhRecbto               E    DR03  D    1-1    -   Preenchido com a data e hora do processamento (informado também no caso de rejeição).
                                                        Formato: “AAAA-MM-DDThh:mm:ssTZD” (UTC - Universal Coordinated Time).
 DR17 nProt                 E     DR03  N    0-1 15, 17 Número do Protocolo de Inutilização (vide item 5.8).
 DR18 Signature             G     DR01 xml   0-1    -   Assinatura XML do grupo identificado pelo atributo “Id”. A decisão de assinar a mensagem fica a critério da UF
                                                        interessada.

5.5. Protocolo de Autorização de Evento
Alteração da seção 5.8.2 do MOC - Leiaute Mensagem de Retorno.

Schema XML: retEnvEvento_v1.00.xsd
#     Campo          Ele     Pai      Tipo   Ocor.     Tam.    Descrição / Observações
R01   retEnvEvento   Raiz     -         -      -         -     TAG raiz
R02   versão          A      R01       N      1-1       2v2    Versão do leiaute
R03   idLote          E      R01       N      1-1      1-15    Idem a mensagem de entrada
R04   tpAmb           E      R01       N      1-1        1     Idem a mensagem de entrada
R05   verAplic        E      R01       C      1-1      1-20    Versão da aplicação que processou o evento.
R06   cOrgao          E      R01       N      1-1        2     Órgão da recepção do Evento, idem a mensagem de entrada.
R07   cStat           E      R01       N      1-1       3-4    Código do status da resposta para o Lote de Eventos. Se não tiver erro, será retornado: “128-Lote de Evento
                                                               Processado“
R08   xMotivo          E     R01       C      1-1      1-255   Descrição do status da resposta
R09   retEvento       G      R01       -      0-20       -     Grupo do resultado do processamento para cada Evento
R10   versão           A     R09       N      1-1       2v2    Versão do leiaute
R11   infEvento       G      R09       -      1-1        -     Grupo de informações do registro do Evento.
R12   id              ID     R11       C      0-1      17,19   Identificador da TAG a ser assinada, somente deve ser informado se o órgão de registro assinar a resposta. No
                                                               caso de assinatura, preencher com o número do protocolo, precedido pela literal “ID”.
R13 tpAmb             E      R11       C       1-1       1     Idem a mensagem de entrada
R14 verAplic          E      R11       N       1-1      1-20   Versão da aplicação que registrou o Evento, utilizar literal que permita a identificação do órgão, como a sigla da
                                                               UF ou do órgão.
R15   cOrgao          E      R11       N       1-1       2     Idem a mensagem de entrada
R16   cStat           E      R11       N       1-1      3-4    Código do status da resposta.
R17   xMotivo         E      R11       C       1-1     1-255   Descrição do status da resposta
R18   chNFe           E      R11       N       1-1       44    Idem a mensagem de entrada
R19   tpEvento        E      R11       N       0-1       6     Idem a mensagem de entrada
R20   xEvento         E      R11       C       0-1      5-60   Idem a mensagem de entrada

#   Campo                Ele   Pai     Tipo    Ocor.     Tam.    Descrição / Observações
R21 nSeqEvento            E    R11      N       0-1       1-2    Idem a mensagem de entrada
R50 dhRegEvento           E    R11      D       1-1        -     Data e hora de registro do evento no formato AAAA-MM-DDTHH:MM:SS TZD (formato UTC). Se o evento for
                                                                 rejeitado informar a data e hora de recebimento do evento.
R51 nProt                E     R11       N       0-1     15,17   Número Protocolo do Evento 1 posição (1- Secretaria da Fazenda Estadual, 2-RFB, 3-SVRS), 2 posições para o
                                                                 código da UF, 2 posições para o ano e 10 posições para o sequencial no ano.
P91 Signature            G     R09     XML       1-1       1     Assinatura Digital do documento XML, a assinatura deverá ser aplicada no elemento infEvento.
```

## 6. Leiaute da NF-e (Modelo 55 e 65)

```text
Grupo B. Identificação da Nota Fiscal eletrônica
#       ID      Campo        Descrição                                    Ele Pai      Tipo   Ocor.   Tam. Observação
14a     B10a    dPrevEntrega Data da previsão de entrega ou                E B01        D      0-1     10 Formato: “AAAA-MM-DD”
                             disponibilização do bem.                                                      Observação: Não informar este campo para a NFC-e.
  ...     ...   ...          ...                                          ...    ...    ...     ...    ... ...
16      B12     cMunFG       Código do Município de Ocorrência do Fato    E     B01     N      1-1     7   Informar o município de ocorrência do fato gerador do ICMS. Utilizar a
                             Gerador do ICMS                                                               Tabela de código de Município do IBGE
16a     B12a    cMunFGIBS    Código do Município de consumo, fato          E    B01     N      0-1     7   Informar o município de ocorrência do fato gerador do IBS / CBS.
                             gerador do IBS / CBS                                                          Campo preenchido somente quando “indPres = 5 (Operação
                                                                                                           presencial, fora do estabelecimento)”, e não estiver preenchido o
                                                                                                           endereço do destinatário (grupo: E05) nem o local de entrega (grupo:
                                                                                                           G01).
29      B25     finNFe         Finalidade de emissão da NF-e               E    B01     N      1-1     1   1=NF-e normal;
                                                                                                           2=NF-e complementar;
                                                                                                           3=NF-e de ajuste;
                                                                                                           4=Devolução de mercadoria.
                                                                                                           5=Nota de crédito;
                                                                                                           6=Nota de débito.
29.1    B25.1 tpNFDebito       Tipo de Nota de Débito                     CE B01        N      0-1     2   01=Transferência de créditos para Cooperativas;
                                                                                                           02=Anulação de Crédito por Saídas Imunes/Isentas;
                                                                                                           03=Débitos de notas fiscais não processadas na apuração;
                                                                                                           04=Multa e juros;
                                                                                                           05=Transferência de crédito na sucessão;
                                                                                                           06=Pagamento antecipado;
                                                                                                           07=Perda em estoque (Perecimento, Perda, Furto, Roubo);
                                                                                                           08=Desenquadramento do SN.
29.2    B25.2 tpNFCredito      Tipo de Nota de Crédito                    CE B01        N      0-1     2   01=Multa e juros;
                                                                                                           02=Apropriação de crédito presumido de IBS sobre o saldo devedor
                                                                                                               na ZFM (art. 450, § 1º, LC 214/25);
                                                                                                           03=Retorno por recusa total na entrega ou por não localização do
                                                                                                               destinatário na tentativa de entrega;

#      ID     Campo         Descrição                                  Ele   Pai   Tipo   Ocor.   Tam. Observação
                                                                                                       04=Redução de valores;
                                                                                                       05=Transferência de crédito na sucessão;
                                                                                                       06=Retorno por recusa parcial na entrega.
29.3   B25a   indFinal      Indica operação com Consumidor final       E     B01    N      1-1     1   0=Normal;
                                                                                                       1=Consumidor final;
29.4   B25b   indPres       Indicador de presença do comprador no      E     B01    N      1-1     1   0=Não se aplica (por exemplo, Nota Fiscal complementar ou de
                            estabelecimento comercial no momento da                                         ajuste);
                            operação                                                                   1=Operação presencial;
                                                                                                       2=Operação não presencial, pela Internet;
                                                                                                       3=Operação não presencial, Teleatendimento;
                                                                                                       4=NFC-e em operação com entrega a domicílio;
                                                                                                       5=Operação presencial, fora do estabelecimento; (incluído NT
                                                                                                            2016/002)
                                                                                                       9=Operação não presencial, outros.
29.5   B25c   indIntermed   Indicador de intermediador/marketplace     E     B01    N      0-1     1   0=Operação sem intermediador (em site ou plataforma própria)
                                                                                                       1=Operação em site ou plataforma de terceiros
                                                                                                            (intermediadores/marketplace)
                                                                                                       • Considera-se intermediador/marketplace os prestadores de
                                                                                                           serviços e de negócios referentes às transações comerciais ou de
                                                                                                           prestação de serviços intermediadas, realizadas por pessoas
                                                                                                           jurídicas inscritas no Cadastro Nacional de Pessoa Jurídica - CNPJ
                                                                                                           ou pessoas físicas inscritas no Cadastro de Pessoa Física - CPF,
                                                                                                           ainda que não inscritas no cadastro de contribuintes do ICMS.
                                                                                                       • Considera-se site/plataforma própria as vendas que não foram
                                                                                                           intermediadas (por marketplace), como venda em site próprio,
                                                                                                           teleatendimento.
                                                                                                       (Criado na NT 2020.006)
29.6   B25d   cIndOp        Código indicador do local da operação de   E     B01    N      0-1     6   Preenchimento obrigatório no caso de:
                            fornecimento                                                                - Leilão judicial ou Licitação promovida pelo poder público
                                                                                                            (cIndOp=010104)
                                                                                                        - Constatação de irregularidade pela falta de documentação fiscal ou
                                                                                                            pelo acobertamento por documentação inidônea (cIndOp=010105)
                                                                                                       Observação: Consultar tabela “Código Indicador do Local de
                                                                                                            Operação”.

Grupo BA. Documento Fiscal Referenciado
Sem alterações.

Grupo BB. Grupo de Compras Governamentais
#     ID      Campo          Descrição                                   Ele Pai Tipo Ocor. Tam. Observação
29.z1 BB01    gCompraGov     Grupo de Compra Governamental                G  B01   -   0-1
29.z2 BB02    tpEnteGov      Tipo de ente governamental                   E BB01  N    1-1   1 Para administração pública direta e suas autarquias e fundações:
                                                                                                 1=União
                                                                                                 2=Estado
                                                                                                 3=Distrito Federal
                                                                                                 4=Município
                                                                                                 5=Consórcio Público
                                                                                                 6=Comitê Gestor do IBS
29.z3 BB03    pRedutor       Percentual de redução da alíquota em         E BB01  N    1-1 3v2-4 Conforme o art. 472/370 da LC 214/2025.
                             compra governamental
29.z4 BB04    tpOperGov      Tipo de operação com o ente governamental    E    BB01     N     1-1     1    1=Fornecimento com pagamento posterior;
                                                                                                           2=Recebimento do pagamento com fornecimento já realizado;
                                                                                                           3=Fornecimento com pagamento já realizado;
                                                                                                           4=Recebimento do pagamento com fornecimento posterior;
29.z5 BB05    refDFeAnt      Chave de acesso do documento fiscal          E    BB01     C     0-99    44
                             anterior

Grupo BC. Grupo de notas de antecipação de pagamento
#     ID   Campo          Descrição                                 Ele Pai Tipo Ocor. Tam. Observação
29.y1 BC01 gPagAntecipado Grupo de notas de antecipação de           G B01    -   0-1       Informado para abater as parcelas de antecipação de
                          pagamento                                                         pagamento, conforme Art. 10. § 4º
29.y2 BC02 refNFe         Chave de acesso da NF-e de antecipação de                         Referência a uma NF-e (modelo 55) emitida anteriormente,
                                                                     E BC01 C    1-99   44
                          pagamento                                                         referente a pagamento antecipado

Grupo C. Identificação do Emitente da Nota Fiscal eletrônica
#     ID     Campo           Descrição                                   Ele   Pai    Tipo Ocor. Tam. Observação
49d   C22    ISUFEmit        Inscrição do emitente da Suframa             E    C01     C    0-1   8-9 Informar o número do Cadastro do emitente na Suframa. Campo
                                                                                                      obrigatório nas operações que se beneficiam de incentivos fiscais
                                                                                                      existentes nas áreas sob controle da SUFRAMA com alíquota zero
                                                                                                      da CBS referente aos arts. 451 e 466 da LC 214/25

Grupo I. Produtos e Serviços da NF-e
#      ID Campo                    Descrição                                    Ele Pai Tipo Ocor. Tam. Observação
104.11 I05k tpCredPresIBSZFM       Classificação para subapuração do IBS na      E I01 N      0-1   1 Classificação conforme percentuais definidos no art. 450, § 1º, da
                                   ZFM                                                                  LC 214/25 para o cálculo do crédito presumido:
                                                                                                        0 - Sem Crédito Presumido
                                                                                                        1 - Bens de consumo final (55%)
                                                                                                        2 - Bens de capital (75%)
                                                                                                        3 - Bens intermediários (90,25%)
                                                                                                        4 - Bens de informática e outros definidos em legislação (100%)
  ...       ...        ...                              ...                     ... ...  ...   ...  ...                                  ...
116c      I17c indBemMovelUsado    Indicador de fornecimento de bem móvel        E I01 N      0-1   1 Somente para fornecimentos de bem móvel usado adquirido de
                                   usado                                                                pessoa física que não seja contribuinte ou que seja inscrita como
                                                                                                        MEI.
                                                                                                        1 - Bem Móvel Usado

Grupo N01. ICMS Normal e ST
#   ID  Campo               Descrição                                         Ele   Pai   Tipo Ocor.    Tam. Observação
164 N01 ICMS                Informações do ICMS da Operação própria e ST      CG    M01     -   0-1       -  Informar apenas um dos grupos de tributação do ICMS
                                                                                                             (ICMS00, ICMS10, ...) (v2.0)

Grupo UB. Informações dos tributos IBS / CBS e Imposto Seletivo
#          ID      Campo                 Descrição                                         Ele    Pai    Tipo Ocor.   Tam. Observação
324.01     UB01    IS                    Informações do Imposto Seletivo                    G    M01       -   0-1      -
324.02     UB02    CSTIS                 Código de Situação Tributária do Imposto Seletivo  E    UB01     N    1-1     3   Utilizar tabela CST do Imposto Seletivo
324.03     UB03    cClassTribIS          Código de Classificação Tributária do Imposto      E    UB01     N    1-1     6   Utilizar tabela cClassTribIS
                                         Seletivo
324.04     UB04    -x-                   Sequência XML                                      G    UB01     -     0-1     -
324.05     UB05    vBCIS                 Valor da Base de Cálculo do Imposto Seletivo       E    UB04     N     1-1   13v2
324.06     UB06    pIS                   Alíquota do Imposto Seletivo (em percentual)       E    UB04     N     1-1   3v2-4
324.07     UB07    adRemIS               Alíquota específica por unidade de medida          E    UB04     N     0-1   3v2-4
                                         apropriada
324.08     UB08    -x-                   Sequência XML                                      G    UB04     -     0-1      -
324.09     UB09    uTrib                 Unidade de Medida Tributável                       E    UB08     C     1-1     1-6
324.10     UB10    qTrib                 Quantidade Tributável                              E    UB08     N     1-1   11v0-4
324.11     UB11    vIS                   Valor do Imposto Seletivo                          E    UB04     N     1-1    13v2
324.12     UB12    IBSCBS                Informações do Imposto de Bens e Serviços -        G    M01      -     0-1      -
                                         IBS e da Contribuição de Bens e Serviços - CBS
324.13     UB13    CST                   Código de Situação Tributária do IBS e CBS         E    UB12     N     1-1     3      Utilizar tabela CST do IBS/CBS
324.14     UB14    cClassTrib            Código de Classificação Tributária do IBS e CBS    E    UB12     N     1-1     6      Utilizar tabela cClassTrib
324.14a    UB14a   indDoacao             Indica a natureza da operação de doação,           E    UB12     N     0-1     1      Informar “1” quando doação.
                                         orientando a apuração e a geração de débitos ou
                                         estornos conforme o cenário

#         ID      Campo             Descrição                                           Ele Pai  Tipo Ocor.   Tam. Observação
324.14k   UB14k               -x-                    Sequência XML                       G UB12    -   0-1
324.15    UB15    gIBSCBS           Grupo de Informações do IBS e da CBS                CG UB14k   -   1-1
324.16    UB16    vBC               Base de cálculo do IBS e CBS                         E UB15   N    1-1    13v2
324.17    UB17    gIBSUF            Grupo de Informações do IBS para a UF                G UB15    -   1-1      -
324.18    UB18    pIBSUF            Alíquota do IBS de competência das UF (em            E UB17   N    1-1    3v2-4 Alíquota vigente do IBS da UF.
                                    percentual)                                                                     Preencher de acordo com a tabela de alíquotas do
                                                                                                                    IBS e CBS.
324.21    UB21    gDif              Grupo de Informações do Diferimento                 G   UB17   -   0-1      -   Observação: a obrigatoriedade ou vedação do
                                                                                                                        preenchimento deste grupo está condicionada
                                                                                                                        ao indicador “ind_gDif” da tabela de CST do IBS
                                                                                                                        e da CBS.
324.22    UB22    pDif              Percentual do diferimento                           E   UB21   N   1-1    3v2-4
324.23    UB23    vDif              Valor do Diferimento                                E   UB21   N   1-1    13v2
324.24    UB24    gDevTrib          Grupo de Informações da devolução de tributos       G   UB17   -   0-1      -   Grupo usado para registrar a devolução de tributos
                                                                                                                    no fornecimento de energia elétrica, água, esgoto,
                                                                                                                    gás natural e em outras hipóteses definidas no
                                                                                                                    regulamento.
324.24a   UB24a   pDevTrib          Percentual de devolução do IBS da UF                E   UB24   N   0-1    3v2-4 Percentual de devolução do IBS da UF, conforme
                                                                                                                    LC 214/25 art. 118.
324.25    UB25    vDevTrib          Valor do tributo devolvido                          E   UB24   N   1-1    13v2 Valor do tributo devolvido (“cashback” de desconto
                                                                                                                    na própria Nota Fiscal / Fatura)
324.26    UB26    gRed              Grupo de informações da redução da alíquota         G   UB17   -   0-1      -   Observação: a obrigatoriedade ou vedação do
                                                                                                                        preenchimento deste grupo está condicionada
                                                                                                                        ao indicador “ind_gRed” da tabela de CST do
                                                                                                                        IBS e da CBS.
324.27    UB27    pRedAliq          Percentual da redução de alíquota do cClassTrib     E   UB26   N   1-1    3v2-4
324.28    UB28    pAliqEfet         Alíquota Efetiva do IBS de competência das UF que   E   UB26   N   1-1    3v2-4 Alíquota efetiva, após aplicação da redução de
                                    será aplicada à Base de Cálculo (em percentual)                                 alíquota, incluindo o gCompraGov/pRedutor, se
                                                                                                                    houver.
                  -x-
324.35    UB35    vIBSUF            Valor do IBS de competência da UF                   E   UB17   N   1-1    13v2
324.36    UB36    gIBSMun           Grupo de Informações do IBS para o município        G   UB15   -   1-1      -
324.37    UB37    pIBSMun           Alíquota do IBS de competência do Município (em     E   UB36   N   1-1    3v2-4 Alíquota vigente do IBS do Município.
                                    percentual)                                                                     Preencher de acordo com a tabela de alíquotas do
                                                                                                                    IBS e CBS.
324.40    UB40    gDif              Grupo de Informações do Diferimento                 G   UB36       0-1          Observação: a obrigatoriedade ou vedação do
                                                                                                                        preenchimento deste grupo está condicionada
                                                                                                                        ao indicador “ind_gDif” da tabela de CST do IBS
                                                                                                                        e da CBS.
324.41    UB41    pDif              Percentual do diferimento                           E   UB40   N   1-1    3v2-4
324.42    UB42    vDif              Valor do Diferimento                                E   UB40   N   1-1    13v2
324.43    UB43    gDevTrib          Grupo de Informações da devolução de tributos       G   UB36       0-1          Grupo usado para registrar a devolução de tributos
                                                                                                                    no fornecimento de energia elétrica, água, esgoto,

#         ID      Campo            Descrição                                           Ele   Pai    Tipo Ocor.   Tam. Observação
                                                                                                                       gás natural e em outras hipóteses definidas no
                                                                                                                       regulamento.
324.43a   UB43a   pDevTrib         Percentual de devolução do IBS do Município         E     UB43    N    0-1    3v2-4 Percentual de devolução do IBS do Município,
                                                                                                                       conforme LC 214/25 art. 118.
324.44    UB44    vDevTrib         Valor do tributo devolvido                          E     UB43    N    1-1    13v2 Valor do tributo devolvido (“cashback” de desconto
                                                                                                                       na própria Nota Fiscal / Fatura)
324.45    UB45    gRed             Grupo de informações da redução da alíquota         G     UB36    -    0-1      -   Observação: a obrigatoriedade ou vedação do
                                                                                                                           preenchimento deste grupo está condicionada
                                                                                                                           ao indicador “ind_gRed” da tabela de CST do
                                                                                                                           IBS e da CBS.
324.46    UB46    pRedAliq         Percentual da redução de alíquota do cClassTrib     E     UB45    N    1-1    3v2-4
324.47    UB47    pAliqEfet        Alíquota Efetiva do IBS de competência do           E     UB45    N    1-1    3v2-4 Alíquota efetiva, após aplicação da redução de
                                   Município que será aplicada à Base de Cálculo (em                                   alíquota, incluindo o gCompraGov/pRedutor, se
                                   percentual)                                                                         houver.
                  -x-
324.53    UB54    vIBSMun          Valor do IBS de competência do Município            E     UB36    N    1-1    13v2
                  -x-
324.54    UB54a   vIBS             Valor do IBS                                        E     UB15    N    1-1    13v2 Valor do IBS (soma de vIBSUF e vIBSMun).
                                                                                                                       Quando houver crédito presumido com indicador
                                                                                                                       “IndDeduzCredPres=1”, o vCredPres deve ser
                                                                                                                       abatido desse valor.
324.55    UB55    gCBS             Grupo de Informações da CBS                         G     UB15    -    1-1      -
324.56    UB56    pCBS             Alíquota da CBS (em percentual)                     E     UB55    N    1-1    3v2-4 Alíquota vigente da CBS.
                                                                                                                       Preencher de acordo com a tabela de alíquotas do
                                                                                                                       IBS e CBS.
324.59    UB59    gDif             Grupo de Informações do Diferimento                 G     UB55    -    0-1          Observação: a obrigatoriedade ou vedação do
                                                                                                                           preenchimento deste grupo está condicionada
                                                                                                                           ao indicador “ind_gDif” da tabela de CST do IBS
                                                                                                                           e da CBS.
324.60    UB60    pDif             Percentual do diferimento                           E     UB59    N    1-1    3v2-4
324.61    UB61    vDif             Valor do Diferimento                                E     UB59    N    1-1    13v2
324.62    UB62    gDevTrib         Grupo de Informações da devolução de tributos       G     UB55    -    0-1          Grupo usado para registrar a devolução de tributos
                                                                                                                       no fornecimento de energia elétrica, água, esgoto,
                                                                                                                       gás natural e em outras hipóteses definidas no
                                                                                                                       regulamento.
324.62a   UB62a   pDevTrib         Percentual de devolução da CBS                      E     UB62    N    0-1    3v2-4 Percentual de devolução da CBS, conforme LC
                                                                                                                       214/25 art. 118.
324.63    UB63    vDevTrib         Valor do tributo devolvido                          E     UB62    N    1-1    13v2 Valor do tributo devolvido (“cashback” de desconto
                                                                                                                       na própria Nota Fiscal / Fatura)
324.64    UB64    gRed             Grupo de informações da redução da alíquota         G     UB55    -    0-1      -   Observação: a obrigatoriedade ou vedação do
                                                                                                                           preenchimento deste grupo está condicionada
                                                                                                                           ao indicador “ind_gRed” da tabela de CST do
                                                                                                                           IBS e da CBS.

#         ID      Campo             Descrição                                          Ele    Pai    Tipo Ocor.   Tam. Observação
324.65    UB65    pRedAliq          Percentual da redução de alíquota do cClassTrib     E    UB64     N    1-1    3v2-4
324.66    UB66    pAliqEfet         Alíquota Efetiva da CBS que será aplicada à Base    E    UB64     N    1-1    3v2-4 Alíquota efetiva, após aplicação da redução de
                                    de Cálculo (em percentual)                                                          alíquota, incluindo o gCompraGov/pRedutor, se
                                                                                                                        houver.
324.66a   UB66a   gALCZFMCBS        Grupo de operações em áreas incentivadas           G     UB55          0-1          Grupo de informações para identificação de
                                    (ALC/ZFM) - CBS (alíquota zero)                                                     operações em áreas incentivadas (ALC/ZFM)
                                                                                                                        com alíquota zero da CBS, conforme
                                                                                                                        arts. 451 e 466 da LC 214/2025, quando
                                                                                                                        fornecedor e destinatário estiverem nessas
                                                                                                                        áreas, distinguindo a existência de processo
                                                                                                                        aprovado na Suframa.
324.66b   UB66b   tpALCZFMCBS       Tipo de aplicação da alíquota zero da CBS          E     UB66a    N    1-1      1   Deve ser informado:
                                                                                                                        1 - quando o fornecedor e o destinatário estiverem
                                                                                                                        localizados em área incentivada, a operação estiver
                                                                                                                        amparada por alíquota zero da CBS e não se tratar
                                                                                                                        de operação industrial com processo aprovado na
                                                                                                                        Suframa para o item;
                                                                                                                        2 - quando o fornecedor e o destinatário estiverem
                                                                                                                        localizados em área incentivada, a operação estiver
                                                                                                                        amparada por alíquota zero da CBS e se tratar de
                                                                                                                        operação industrial com processo aprovado na
                                                                                                                        Suframa para o item.
324.66c   UB66c   nProcSuframa      Número do processo na Suframa para o item          E     UB66a    C    0-1    8-12 Inscrição específica e aprovação de projeto técnico-
                                    comercializado                                                                      econômico pelo Conselho de Administração da
                                                                                                                        Suframa, nos termos do Art. 442. II (ZFM) e Art.
                                                                                                                        459. II (ALC) da LC 214/2025.
324.66d   UB66d   pAliqEfetRegCBS   Percentual efetivo sem a redução                   E     UB66a    N    1-1    3v2-4 Alíquota efetiva de referência da CBS aplicável à
                                                                                                                        operação fora de áreas ou regimes incentivados.
324.66e   UB66e   vTribRegCBS       Valor efetivo sem a redução                        E     UB66a    N    1-1    13v2 Valor da CBS calculado para a operação fora de
                                                                                                                        áreas ou regimes incentivado
                  -x-
324.67    UB67    vCBS              Valor da CBS                                       E     UB55     N    1-1    13v2
324.68    UB68    gTribRegular      Grupo de informações da Tributação Regular         G     UB15     -    0-1      -  Grupo de informações da Tributação Regular.
                                                                                                                       Informar como seria a tributação caso não
                                                                                                                       cumprida a condição resolutória/suspensiva.
                                                                                                                       Exemplo 1: Art. 445, §4 da LC 214/2025.
                                                                                                                            Operações com ZFM e ALC.
                                                                                                                       Exemplo 2: Operações com suspensão do tributo.
                                                                                                                       Observação: a obrigatoriedade ou vedação do
                                                                                                                            preenchimento deste grupo está condicionada
                                                                                                                            ao indicador “ind_gTribRegular” da tabela de
                                                                                                                            cClassTrib do IBS e da CBS.
324.69    UB69    CSTReg            Código de Situação Tributária do IBS e CBS         E     UB68     N    1-1     3   Utilizar tabela CST do IBS/CBS

#         ID      Campo                 Descrição                                         Ele    Pai    Tipo Ocor.   Tam. Observação
324.70    UB70    cClassTribReg         Código de Classificação Tributária do IBS e CBS    E    UB68     N    1-1      6   Utilizar tabela cClassTrib
324.71    UB71    pAliqEfetRegIBSUF     Valor da alíquota do IBS da UF (em percentual)     E    UB68     N    1-1    3v2-4
324.72    UB72    vTribRegIBSUF         Valor do Tributo do IBS da UF                      E    UB68     N    1-1    13v2
324.72a   UB72a   pAliqEfetRegIBSMun    Valor da alíquota do IBS do Município (em          E    UB68     N    1-1    3v2-4
                                        percentual)
324.72b   UB72b   vTribRegIBSMun        Valor do Tributo do IBS do Município              E     UB68     N    1-1    13v2
324.72c   UB72c   pAliqEfetRegCBS       Valor da alíquota da CBS (em percentual)          E     UB68     N    1-1    3v2-4
324.72d   UB72d   vTribRegCBS           Valor do Tributo da CBS                           E     UB68     N    1-1    13v2
324.82a   UB82a   gTribCompraGov        Grupo de informações da composição do valor       G     UB15     -    0-1      -   Informar somente para compras governamentais
                                        do IBS e da CBS em compras governamentais
324.82b   UB82b   pAliqIBSUF            Alíquota do IBS de competência do Estado (em      E     UB82a    N    1-1    3v2-4
                                        percentual)
324.82c   UB82c   vTribIBSUF            Valor do Tributo do IBS da UF calculado           E     UB82a    N    1-1    13v2 Valor que seria devido a UF, sem aplicação do Art.
                                                                                                                           473. da LC 214/2025
324.82d   UB82d   pAliqIBSMun           Alíquota do IBS de competência do Município (em   E     UB82a    N    1-1    3v2-4
                                        percentual)
324.82e   UB82e   vTribIBSMun           Valor do Tributo do IBS do Município calculado    E     UB82a    N    1-1    13v2 Valor que seria devido ao município, sem aplicação
                                                                                                                           do Art. 473. da LC 214/2025
324.82f   UB82f   pAliqCBS              Alíquota da CBS (em percentual)                   E     UB82a    N    1-1    3v2-4
324.82g   UB82g   vTribCBS              Valor do Tributo da CBS calculado                 E     UB82a    N    1-1    13v2 Valor que seria devido a CBS, sem aplicação do Art.
                                                                                                                           473. da LC 214/2025
*** Tributação Monofásica: Início - layout reformulado (separação entre ad rem e ad valorem)
324.84     UB84   gIBSCBSMono              Grupo de Informações do IBS e CBS em            CG UB14k           1-1            Observação: a obrigatoriedade ou vedação do
                                           operações com imposto monofásico                                                    preenchimento deste grupo está condicionada ao
                                                                                                                               indicador “ind_gIBSCBSMono” da tabela de CST
                                                                                                                               do IBS e da CBS.
324.85    UB85    -x-                                    Sequência XML                    G     UB84     -    0-1      -
*** IBS Monofásico Ad Rem
324.85a UB85a gIBSMonoAdRem             Grupo de informações da Tributação Monofásica CG        UB85    CG    0-1           Observação: a obrigatoriedade ou vedação do
                                        Ad Rem do IBS                                                                           preenchimento deste grupo está condicionada ao
                                                                                                                                ano corrente, conforme estabelecido na
                                                                                                                                legislação.
324.86    UB86    gMonoPadrao           Grupo de informações da Tributação Monofásica G         UB85a    G    0-1           Observação: a obrigatoriedade ou vedação do
                                        Padrão                                                                                  preenchimento deste grupo está condicionada ao
                                                                                                                                indicador “ind_gMonoPadrao” da tabela de
                                                                                                                                cClassTrib do IBS e da CBS.
324.86a   UB86a   qBCMono               Quantidade tributada na monofasia                 E     UB86     N    1-1    11v0-4 Informar a BC em quantidade conforme unidade de
                                                                                                                            medida estabelecida na legislação para o produto.
324.86b   UB86b   adRemIBS              Alíquota ad rem do IBS                            E     UB86     N    1-1    3v2-4
324.86c   UB86c   vIBSMono              Valor do IBS monofásico                           E     UB86     N    1-1     13v2 O valor do imposto é obtido pela multiplicação da
                                                                                                                            alíquota ad rem pela quantidade do produto conforme
                                                                                                                            unidade de medida estabelecida na legislação.

#         ID      Campo             Descrição                                     Ele Pai Tipo Ocor.           Tam. Observação
324.87    UB87    gMonoReten        Grupo de informações da Tributação Monofásica G UB85a G     0-1                  Uso em operações com combustíveis derivados
                                    Sujeita à Retenção                                                               de petróleo (Gasolina A) [ou *Óleo Diesel A*]
                                                                                                                     para retenção do imposto sobre o
                                                                                                                     biocombustível a ser misturado. Art. 178 da LC
                                                                                                                     214/2025.
                                                                                                                     Observação: a obrigatoriedade ou vedação do
                                                                                                                         preenchimento deste grupo está condicionada ao
                                                                                                                         indicador “ind_gMonoReten” da tabela de
                                                                                                                         cClassTrib do IBS e da CBS.
324.87a   UB87a   qBCMonoReten      Quantidade tributada sujeita à retenção na        E    UB87    N    1-1   11v0-4 Informar a BC sujeita a retenção em quantidade
                                    monofasia                                                                        conforme unidade de medida estabelecida na
                                                                                                                     legislação para o produto.
324.87b   UB87b   adRemIBSReten     Alíquota ad rem do IBS sujeito à retenção         E    UB87    N    1-1   3v2-4
324.87c   UB87c   vIBSMonoReten     Valor do IBS monofásico sujeito à retenção        E    UB87    N    1-1    13v2 Valor do IBS com retenção, a ser somado ao valor de
                                                                                                                     IBS a ser recolhido.
324.88    UB88    gMonoRet          Grupo de informações da Tributação Monofásica G        UB85a   G    0-1          Tributação monofásica própria sobre
                                    Retida Anteriormente                                                             combustíveis cobrada anteriormente
                                                                                                                     Observação: a obrigatoriedade ou vedação do
                                                                                                                         preenchimento deste grupo está condicionada ao
                                                                                                                         indicador “ind_gMonoRet” da tabela cClassTrib
                                                                                                                         do IBS e da CBS.
324.88a   UB88a   vIBSMonoRet       Valor do IBS retido anteriormente                 E    UB88    N    1-1    13v2
324.89    UB89    gpBioDiferenca    Grupo de informações sobre mistura de EAC         G    UB85a   G    0-1          Referência (LC 214/2025): Art. 179, II, a e b
                                    com gasolina A em percentual inferior ou                                         (cClassTrib 620004 e 620005)
                                    superior ao obrigatório                                                          Informar caso pBio seja diferente do
                                                                                                                     pBioObrigatório.
                                                                                                                     Observação: a obrigatoriedade ou vedação do
                                                                                                                         preenchimento deste grupo está condicionada ao
                                                                                                                         indicador    “ind_gpBioDiferenca”    da   tabela
                                                                                                                         cClassTrib do IBS e da CBS.
324.89a   UB89a   qBCBioComb        Quantidade de Biocombustível (EAC) a recolher ou E     UB89    N    1-1   11v0-4
                                    a ressarcir
324.89b   UB89b   vIBSDiferenca     Valor do IBS correspondente a diferença em relação E   UB89    N    1-1   13v2 Se classTrib = 620004: valor a ser recolhido
                                    ao pBioObrigatorio                                                             Se classTrib = 620005: valor a ser ressarcido
*** IBS Monofásico Ad Valorem
324.90    UB90    gIBSMonoAdValorem Grupo de informações da Tributação Monofásica CG       UB85    CG   0-1          Observação: a obrigatoriedade ou vedação do
                                    Ad Valorem do IBS                                                                  preenchimento deste grupo está condicionada ao
                                                                                                                       ano corrente, conforme estabelecido na
                                                                                                                       legislação.
324.91    UB91    gMonoPadrao       Grupo de informações da Tributação Monofásica G        UB90    G    0-1          Observação: a obrigatoriedade ou vedação do
                                    Padrão                                                                             preenchimento deste grupo está condicionada ao
                                                                                                                       indicador “ind_gMonoPadrao” da tabela de
                                                                                                                       cClassTrib do IBS e da CBS.

#         ID      Campo            Descrição                                     Ele       Pai   Tipo Ocor.    Tam. Observação
324.91a   UB91a   vBCMono          Valor tributado na monofasia                   E       UB91    N    1-1     13v2
324.91b   UB91b   pAliqMonoUF      Alíquota ad valorem do IBS Estadual            E       UB91    N    1-1    3v2-4
324.91c   UB91c   vIBSMonoUF       Valor do IBS monofásico Estadual               E       UB91    N    1-1     13v2
324.91d   UB91d   pAliqMonoMun     Alíquota ad valorem do IBS Municipal           E       UB91    N    1-1    3v2-4
324.91e   UB91e   vIBSMonoMun      Valor do IBS monofásico do Municipal           E       UB91    N    1-1     13v2
324.91f   UB91f   vIBSMono         Valor do IBS monofásico                        R       UB91    N    1-1     13v2 Observação: vIBSMonoUF + vIBSMonoMun
324.92    UB92    gMonoReten       Grupo de informações da Tributação Monofásica G        UB90    G    0-1           Uso em operações com combustíveis derivados
                                   Sujeita à Retenção                                                                de petróleo (Gasolina A) [ou *Óleo Diesel A*] para
                                                                                                                     retenção do imposto sobre o biocombustível a
                                                                                                                     ser misturado. Art. 178 da LC 214/2025.
                                                                                                                     Observação: a obrigatoriedade ou vedação do
                                                                                                                         preenchimento deste grupo está condicionada ao
                                                                                                                         indicador “ind_gMonoReten” da tabela de
                                                                                                                         cClassTrib do IBS e da CBS.
324.92a   UB92a   vBCMonoReten     Valor tributado sujeito à retenção na monofasia   E    UB92    N    1-1     13v2
324.92b   UB92b   pAliqMonoReten   Alíquota ad valorem do IBS sujeito à retenção     E    UB92    N    1-1    3v2-4
324.92c   UB92c   vIBSMonoReten    Valor do IBS monofásico sujeito à retenção        E    UB92    N    1-1     13v2 Valor do IBS com retenção, a ser somado ao valor de
                                                                                                                     IBS a ser recolhido.
324.93    UB93    gMonoRet         Grupo de informações da Tributação Monofásica G        UB90    G    0-1           Tributação monofásica própria sobre
                                   Retida Anteriormente                                                              combustíveis cobrada anteriormente
                                                                                                                     Observação: a obrigatoriedade ou vedação do
                                                                                                                         preenchimento deste grupo está condicionada ao
                                                                                                                         indicador “ind_gMonoRet” da tabela cClassTrib
                                                                                                                         do IBS e da CBS.
324.93a   UB93a   vIBSMonoRet      Valor do IBS retido anteriormente                 E    UB93    N    1-1     13v2
324.94    UB94    gpBioDiferenca   Grupo de informações sobre mistura de EAC         G    UB90    G    0-1           Referência (LC 214/2025): Art. 179, II, a e b
                                   com gasolina A em percentual inferior ou                                          (cClassTrib 620004 e 620005)
                                   superior ao obrigatório                                                           Informar caso pBio seja diferente do
                                                                                                                     pBioObrigatório.
                                                                                                                     Observação: a obrigatoriedade ou vedação do
                                                                                                                         preenchimento deste grupo está condicionada ao
                                                                                                                         indicador    “ind_gpBioDiferenca”    da   tabela
                                                                                                                         cClassTrib do IBS e da CBS.
324.94a   UB94a   qBCBioComb       Quantidade de Biocombustível (EAC) a recolher ou E     UB94    N    1-1    11v0-4
                                   a ressarcir
324.94b   UB94b   vIBSDiferenca    Valor do IBS correspondente a diferença em relação E   UB94    N    1-1    13v2 Se classTrib = 620004: valor a ser recolhido
                                   ao pBioObrigatorio                                                              Se classTrib = 620005: valor a ser ressarcido
324.95   UB95    -x-                                 Sequência XML                    G   UB84    -    0-1      -
*** CBS Monofásica Ad Rem
324.95a UB95a gCBSMonoAdRem        Grupo de informações da Tributação Monofásica CG       UB95   CG    0-1           Observação: a obrigatoriedade ou vedação do
                                   Ad Rem da CBS                                                                       preenchimento deste grupo está condicionada ao
                                                                                                                       ano corrente, conforme estabelecido na
                                                                                                                       legislação.

#         ID      Campo            Descrição                                     Ele Pai Tipo Ocor.          Tam. Observação
324.96    UB96    gMonoPadrao      Grupo de informações da Tributação Monofásica G UB95a   G   0-1                 Observação: a obrigatoriedade ou vedação do
                                   Padrão                                                                              preenchimento deste grupo está condicionada ao
                                                                                                                       indicador “ind_gMonoPadrao” da tabela de
                                                                                                                       cClassTrib do IBS e da CBS.
324.96a   UB96a   qBCMono          Quantidade tributada na monofasia                  E   UB96    N   1-1   11v0-4 Informar a BC em quantidade conforme unidade de
                                                                                                                   medida estabelecida na legislação para o produto.
324.96b   UB96b   adRemCBS         Alíquota ad rem da CBS                             E   UB96    N   1-1   3v2-4
324.96c   UB96c   vCBSMono         Valor da CBS monofásica                            E   UB96    N   1-1    13v2 O valor do imposto é obtido pela multiplicação da
                                                                                                                   alíquota ad rem pela quantidade do produto conforme
                                                                                                                   unidade de medida estabelecida na legislação.
324.97    UB97    gMonoReten       Grupo de informações da Tributação Monofásica G        UB95a   G   0-1          Uso em operações com combustíveis derivados
                                   Sujeita à Retenção                                                              de petróleo (Gasolina A) [ou *Óleo Diesel A*]
                                                                                                                   para retenção do imposto sobre o
                                                                                                                   biocombustível a ser misturado. Art. 178 da LC
                                                                                                                   214/2025.
                                                                                                                   Observação: a obrigatoriedade ou vedação do
                                                                                                                       preenchimento deste grupo está condicionada ao
                                                                                                                       indicador “ind_gMonoReten” da tabela de
                                                                                                                       cClassTrib do IBS e da CBS.
324.97a   UB97a   qBCMonoReten     Quantidade tributada sujeita à retenção na         E   UB97    N   1-1   11v0-4 Informar a BC sujeita a retenção em quantidade
                                   monofasia                                                                       conforme unidade de medida estabelecida na
                                                                                                                   legislação para o produto.
324.97b   UB97b   adRemCBSReten    Alíquota ad rem da CBS sujeita à retenção          E   UB97    N   1-1   3v2-4
324.97c   UB97c   vCBSMonoReten    Valor da CBS monofásica sujeita à retenção         E   UB97    N   1-1    13v2 Valor da CBS com retenção, a ser somado ao valor
                                                                                                                   de CBS a ser recolhida.
324.98    UB98    gMonoRet         Grupo de informações da Tributação Monofásica G        UB95a   G   0-1          Tributação monofásica própria sobre
                                   Retida Anteriormente                                                            combustíveis cobrada anteriormente
                                                                                                                   Observação: a obrigatoriedade ou vedação do
                                                                                                                       preenchimento deste grupo está condicionada ao
                                                                                                                       indicador “ind_gMonoRet” da tabela cClassTrib
                                                                                                                       do IBS e da CBS.
324.98a   UB98a   vCBSMonoRet      Valor da CBS retida anteriormente                  E   UB98    N   1-1    13v2
324.99    UB99    gpBioDiferenca   Grupo de informações sobre mistura de EAC          G   UB95a   G   0-1          Referência (LC 214/2025): Art. 179, II, a e b
                                   com gasolina A em percentual inferior ou                                        (cClassTrib 620004 e 620005)
                                   superior ao obrigatório                                                         Informar caso pBio seja diferente do
                                                                                                                   pBioObrigatório.
                                                                                                                   Observação: a obrigatoriedade ou vedação do
                                                                                                                       preenchimento deste grupo está condicionada ao
                                                                                                                       indicador    “ind_gpBioDiferenca”    da   tabela
                                                                                                                       cClassTrib do IBS e da CBS.
324.99a   UB99a   qBCBioComb       Quantidade de Biocombustível (EAC) a recolher ou   E   UB99    N   1-1   11v0-4
                                   a ressarcir

#         ID      Campo            Descrição                                          Ele    Pai    Tipo Ocor.   Tam. Observação
324.99b   UB99b   vCBSDiferenca    Valor da CBS correspondente a diferença em          E    UB99     N    1-1    13v2 Se classTrib = 620004: valor a ser recolhido
                                   relação ao pBioObrigatorio                                                         Se classTrib = 620005: valor a ser ressarcido
*** CBS Monofásica Ad Valorem
324.100 UB100 gCBSMonoAdValorem Grupo de informações da Tributação Monofásica CG            UB95    CG    0-1            Observação: a obrigatoriedade ou vedação do
                                Ad Valorem da CBS                                                                          preenchimento deste grupo está condicionada ao
                                                                                                                           ano corrente, conforme estabelecido na
                                                                                                                           legislação.
324.101   UB101   gMonoPadrao      Grupo de informações da Tributação Monofásica G          UB100    G    0-1            Observação: a obrigatoriedade ou vedação do
                                   Padrão                                                                                  preenchimento deste grupo está condicionada ao
                                                                                                                           indicador “ind_gMonoPadrao” da tabela de
                                                                                                                           cClassTrib do IBS e da CBS.
324.101a UB101a vBCMono            Valor tributado na monofasia                       E     UB101    N    1-1    13v2
324.101b UB101b pAliqMonoCBS       Alíquota ad valorem da CBS                         E     UB101    N    1-1    3v2-4
324.101c UB101c vCBSMono           Valor da CBS monofásica                            R     UB101    N    1-1    13v2
324.102 UB102 gMonoReten           Grupo de informações da Tributação Monofásica      G     UB100    G    0-1            Uso em operações com combustíveis derivados
                                   Sujeita à Retenção                                                                    de petróleo (Gasolina A) [ou *Óleo Diesel A*] para
                                                                                                                         retenção do imposto sobre o biocombustível a
                                                                                                                         ser misturado. Art. 178 da LC 214/2025.
                                                                                                                         Observação: a obrigatoriedade ou vedação do
                                                                                                                             preenchimento deste grupo está condicionada ao
                                                                                                                             indicador “ind_gMonoReten” da tabela de
                                                                                                                             cClassTrib do IBS e da CBS.
324.102a UB102a vBCMonoReten       Valor tributado sujeito à retenção na monofasia    E     UB102    N    1-1     13v2
324.102b UB102b pAliqMonoReten     Alíquota ad valorem da CBS sujeito à retenção      E     UB102    N    1-1    3v2-4
324.102c UB102c vCBSMonoReten      Valor da CBS monofásica sujeita à retenção         E     UB102    N    1-1     13v2 Valor da CBS com retenção, a ser somado ao valor
                                                                                                                        de CBS a ser recolhida.
324.103   UB103   gMonoRet         Grupo de informações da Tributação Monofásica G          UB100    G    0-1           Tributação monofásica própria sobre
                                   Retida Anteriormente                                                                 combustíveis cobrada anteriormente
                                                                                                                        Observação: a obrigatoriedade ou vedação do
                                                                                                                            preenchimento deste grupo está condicionada ao
                                                                                                                            indicador “ind_gMonoRet” da tabela cClassTrib
                                                                                                                            do IBS e da CBS.
324.103a UB103a vCBSMonoRet        Valor da CBS retida anteriormente                  E     UB103    N    1-1     13v2
324.104 UB104 gpBioDiferenca       Grupo de informações sobre mistura de EAC          G     UB100    G    0-1           Referência (LC 214/2025): Art. 179, II, a e b
                                   com gasolina A em percentual inferior ou                                             (cClassTrib 620004 e 620005)
                                   superior ao obrigatório                                                              Informar caso pBio seja diferente do
                                                                                                                        pBioObrigatório.
                                                                                                                        Observação: a obrigatoriedade ou vedação do
                                                                                                                            preenchimento deste grupo está condicionada ao
                                                                                                                            indicador    “ind_gpBioDiferenca”    da   tabela
                                                                                                                            cClassTrib do IBS e da CBS.
324.104a UB104a qBCBioComb         Quantidade de Biocombustível (EAC) a recolher ou   E     UB104    N    1-1    11v0-4
                                   a ressarcir

#        ID     Campo                     Descrição                                          Ele Pai  Tipo Ocor.    Tam. Observação
324.104b UB104b vCBSDiferenca             Valor da CBS correspondente a diferença em          E UB104 N     1-1     13v2 Se classTrib = 620004: valor a ser recolhido
                                          relação ao pBioObrigatorio                                                     Se classTrib = 620005: valor a ser ressarcido
*** Tributação Monofásica: Totais do Item
324.105a UB105a vTotIBSMonoItem           Total de IBS Monofásico.                           E    UB84    N   1-1   13v2
324.105b UB105b vTotCBSMonoItem           Total da CBS Monofásica.                           E    UB84    N   1-1   13v2
*** Tributação Monofásica: Fim
324.106 UB106 gTransfCred                 Transferências de Crédito                          CG   UB14k       1-1
324.107 UB107 vIBS                        Valor do IBS a ser transferido                      E   UB106   N   1-1   13v2
324.108 UB108 vCBS                        Valor da CBS a ser transferida                      E   UB106   N   1-1   13v2
324.112 UB112 gAjusteCompet               Ajuste de Competência                              CG   UB14k   -   1-1     -  Observação: a obrigatoriedade ou vedação do
                                                                                                                             preenchimento deste grupo está condicionada
                                                                                                                             ao indicador “ind_gAjusteCompet” da tabela de
                                                                                                                             CST do IBS e da CBS.
324.113   UB113   competApur              Ano e mês referência do período de apuração        E    UB112   C   1-1    7   Informar período atual ou retroativo.
                                          (AAAA-MM)
324.114   UB114   vIBS                    Valor do IBS                                       E    UB112   N   1-1   13v2
324.115   UB115   vCBS                    Valor da CBS                                       E    UB112   N   1-1   13v2
324.116   UB116   gEstornoCred            Estorno de Crédito                                 G    UB12    -   0-1     -  Observação: a obrigatoriedade ou vedação do
                                                                                                                           preenchimento deste grupo está condicionada
                                                                                                                           ao indicador “ind_gEstornoCred” da tabela de
                                                                                                                           cClassTrib do IBS e da CBS.
324.117   UB117   vIBSEstCred             Valor do IBS a ser estornado                        E UB116     N   1-1   13v2
324.118   UB118   vCBSEstCred             Valor da CBS a ser estornada                        E UB116     N   1-1   13v2
324.119   UB119            -x-                             Sequência XML                      G UB12      -   0-1     -
324.120   UB120   gCredPresOper           Crédito Presumido da Operação                      CG UB119     -   1-1     -  Observação 1: a permissão ou vedação do
                                                                                                                           preenchimento deste grupo está condicionada ao
                                                                                                                           indicador “ind_gCredPresOper” da tabela de
                                                                                                                           cClassTrib do IBS e da CBS.
                                                                                                                         Observação 2: O valor "1" do indicador
                                                                                                                           “ind_gCredPresOper” significa que o contribuinte
                                                                                                                           pode utilizar o crédito presumido, sem
                                                                                                                           obrigatoriedade (permite, mas não exige).
324.121   UB121   vBCCredPres             Valor da Base de Cálculo do Crédito Presumido da   E    UB120   N   1-1   13v2
                                          Operação
324.122   UB122   cCredPres               Código de Classificação do Crédito Presumido       E    UB120   N   1-1    2     Utilizar tabela cCredPres (Anexo IV).
                                                                                                                           Exemplos:
                                                                                                                           1 - Aquisição de Produtor Rural não contribuinte.
                                                                                                                           2 - Tomador de serviço de transporte de TAC PF
                                                                                                                                não contrib.
                                                                                                                           3 - Aquisição de pessoa física com destino à
                                                                                                                                reciclagem.
                                                                                                                           4 - Aquisição de bens móveis de PF não contrib.
                                                                                                                                para revenda (veículos / brechó).

#         ID      Campo              Descrição                                            Ele    Pai    Tipo Ocor.   Tam. Observação
                                                                                                                           5 - Regime opcional para cooperativa.
324.123   UB123   gIBSCredPres       Grupo de Informações do Crédito Presumido            G     UB120    -    0-1      -   Grupo de Informações do Crédito Presumido do
                                     referente ao IBS                                                                      IBS, quando aproveitado pelo emitente do
                                                                                                                           documento.
                                                                                                                           Observação: a obrigatoriedade ou vedação do
                                                                                                                               preenchimento deste grupo está condicionada ao
                                                                                                                               indicador “ind_gIBSCredPres” da tabela de
                                                                                                                               cCredPres do IBS e da CBS.
324.124   UB124   pCredPres          Percentual do Crédito Presumido                       E UB123       N    1-1    3v2-4
324.125   UB125   vCredPres          Valor do Crédito Presumido                           CE UB123       N    1-1    13v2
324.126   UB126   vCredPresCondSus   Valor do Crédito Presumido em condição               CE UB123       N    1-1    13v2 Valor do Crédito Presumido em Condição
                                     suspensiva.                                                                           Suspensiva. Preencher apenas para cCredPres com
                                                                                                                           indicação de Condição Suspensiva.
324.127   UB127   gCBSCredPres       Grupo de Informações do Crédito Presumido            G     UB120    -    0-1          Grupo de Informações do Crédito Presumido da
                                     referente a CBS                                                                       CBS, quando aproveitado pelo emitente do
                                                                                                                           documento.
                                                                                                                           Observação: a obrigatoriedade ou vedação do
                                                                                                                               preenchimento deste grupo está condicionada ao
                                                                                                                               indicador “ind_gCBSCredPres” da tabela de
                                                                                                                               cCredPres do IBS e da CBS.
324.128   UB128   pCredPres          Percentual do Crédito Presumido                       E UB127       N    1-1    3v2-4
324.129   UB129   vCredPres          Valor do Crédito Presumido                           CE UB127       N    1-1    13v2
324.130   UB130   vCredPresCondSus   Valor do Crédito Presumido em condição               CE UB127       N    1-1    13v2 Valor do Crédito Presumido em Condição
                                     suspensiva.                                                                           Suspensiva. Preencher apenas para cCredPres com
                                                                                                                           indicação de Condição Suspensiva.
324.131   UB131   gCredPresIBSZFM    Grupo para apropriação de crédito presumido de CG UB119             -    1-1      -   Observação: a obrigatoriedade ou vedação do
                                     IBS sobre o saldo devedor na ZFM (art. 450, § 1º,                                         preenchimento deste grupo está condicionada
                                     LC 214/25)                                                                                ao indicador “ind_gCredPresIBSZFM” da tabela
                                                                                                                               de CST do IBS e da CBS.
324.132   UB132   competApur         Ano e mês referência do período de apuração           E    UB131    C    1-1      7   Informar período atual ou retroativo.
                                     (AAAA-MM)
324.133   UB133   tpCredPresIBSZFM   Tipo de classificação de acordo com o art. 450, § 1º, E    UB131    N    1-1      1    Classificação conforme percentuais definidos no art.
                                     da LC 214/25 para o cálculo do crédito presumido                                       450, § 1º, da LC 214/25 para o cálculo do crédito
                                     na ZFM                                                                                 presumido:
                                                                                                                            0 - Sem Crédito Presumido
                                                                                                                            1 - Bens de consumo final (55%)
                                                                                                                            2 - Bens de capital (75%)
                                                                                                                            3 - Bens intermediários (90,25%)
                                                                                                                            4 - Bens de informática e outros definidos em
                                                                                                                            legislação (100%)
324.134   UB134   vCredPresIBSZFM    Valor do crédito presumido calculado sobre o saldo   E     UB131    N    1-1    13v2
                                     devedor apurado

Grupo VB. Total do item da NF-e
#    ID   Campo                  Descrição                             Ele   Pai   Tipo Ocor. Tam. Observação
325h VB01 vItem                  Valor Total do Item da NF-e            E    H01    N    0-1  13v2 Valor total do Item, correspondente à sua participação no total da nota.
                                                                                                   A soma dos itens deverá corresponder ao total da nota.

Grupo VC. Referenciamento de item de outro Documento Fiscal Eletrônico - DF-e
#       ID     Campo             Descrição                                         Ele Pai Tipo Ocor. Tam. Observação
325i    VC01   DFeReferenciado   Documento Fiscal Eletrônico Referenciado           G  H01       0-1       Grupo para referenciamento de itens de outro DF-e.
325j    VC02   chaveAcesso       Chave de acesso do DF-e referenciado               E VC01  N    1-1   44 Chave de acesso do DF-e referenciado.
325k    VC03   nItem             Número do item do documento referenciado.          E VC01  N    0-1   3 Corresponde ao atributo “nItem” do elemento “det” do documento
                                                                                                           original.
                                                                                                           Observação: tag opcional apenas para Nota de Débito
                                                                                                               (tpNFDebito) = 03-Débitos de notas fiscais não processadas
                                                                                                               na apuração (RV VC03-20).

Grupo W03. Total da NF-e - IBS / CBS / IS
#        ID       Campo             Descrição                                         Ele Pai Tipo Ocor. Tam. Observação
355.1    W31      ISTot             Grupo total do imposto seletivo                    G W01    -   0-1    - O grupo de valores totais da NF-e deve ser informado com o
                                                                                                              somatório do campo correspondente dos itens.

                                                                                                                     O IS é “por fora”, portanto seu valor deve ser adicionado ao
                                                                                                                     valor total da NF.
355.3    W33      vIS               Total do imposto seletivo                          E   W31     N    1-1   13v2
355.4    W34      IBSCBSTot         Totais da NF-e com IBS e CBS                       G   W01     -    0-1     - O grupo de valores totais da NF-e deve ser informado com o
                                                                                                                   somatório do campo correspondente dos itens.

                                                                                                                     O IBS e a CBS são “por fora”, por isso seus valores devem
                                                                                                                     ser adicionados ao valor total da NF.
355.5    W35      vBCIBSCBS         Valor total da BC do IBS e da CBS                  E   W34     N    1-1   13v2
355.6    W36      gIBS              Grupo total do IBS                                 G   W34     -    0-1     -
355.7    W37      gIBSUF            Grupo total do IBS da UF                           G   W36     -    1-1     -
355.8    W38      vDif              Valor total do diferimento                         E   W37     N    1-1   13v2
355.9    W39      vDevTrib          Valor total de devolução de tributos               E   W37     N    1-1   13v2
355.11   W41      vIBSUF            Valor total do IBS da UF                           E   W37     N    1-1   13v2
355.12   W42      gIBSMun           Grupo total do IBS do Município                    G   W36     -    1-1     -
355.13   W43      vDif              Valor total do diferimento                         E   W42     N    1-1   13v2
355.14   W44      vDevTrib          Valor total de devolução de tributos               E   W42     N    1-1   13v2
355.16   W46      vIBSMun           Valor total do IBS do Município                    E   W42     N    1-1   13v2
                  -x-
355.17 W47        vIBS              Valor total do IBS                                 E   W36     N    1-1   13v2
355.18 W48        vCredPres         Valor total do crédito presumido                   E   W36     N    1-1   13v2

#      ID         Campo            Descrição                                      Ele Pai Tipo Ocor. Tam. Observação
355.19 W49        vCredPresCondSus Valor total do crédito presumido em condição    E W36 N      1-1 13v2
                                   suspensiva.
355.20 W50        gCBS             Grupo total da CBS                             G   W34    -   0-1     -
355.23 W53        vDif             Valor total do diferimento                     E   W50    N   1-1   13v2
355.24 W54        vDevTrib         Valor total de devolução de tributos           E   W50    N   1-1   13v2
355.26 W56        vCBS             Valor total da CBS                             E   W50    N   1-1   13v2
355.26a W56a      vCredPres        Valor total do crédito presumido               E   W50    N   1-1   13v2
355.26b W56b      vCredPresCondSus Valor total do crédito presumido em condição   E   W50    N   1-1   13v2
                                   suspensiva.
355.27 W57        gMono            Grupo total da Monofasia                       G   W34    -   0-1     -
355.28 W58        vIBSMono         Total do IBS monofásico                        E   W57    N   1-1   13v2
355.29 W59        vCBSMono         Total da CBS monofásica                        E   W57    N   1-1   13v2
355.29a W59a      vIBSMonoReten    Total do IBS monofásico sujeito à retenção     E   W57    N   1-1   13v2
355.29b W59b      vCBSMonoReten    Total da CBS monofásica sujeita à retenção     E   W57    N   1-1   13v2
355.29c W59c      vIBSMonoRet      Total do IBS monofásico retido anteriormente   E   W57    N   1-1   13v2
355.29d W59d      vCBSMonoRet      Total da CBS monofásica retida anteriormente   E   W57    N   1-1   13v2
355.29e W59e      gEstornoCred     Grupo total do Estorno de Crédito              G   W34    -   0-1     -
355.29f W59f      vIBSEstCred      Valor total do IBS estornado                   E   W59e   N   1-1   13v2
355.29g W59g      vCBSEstCred      Valor total da CBS estornada                   E   W59e   N   1-1   13v2
                  -x-
355.30 W60        vNFTot           Valor total da NF-e com IBS / CBS / IS         E   W01    N   0-1   13v2
```

## 7. Regras de Validação

```text
Grupo B. Identificação da Nota Fiscal eletrônica
 Campo Modelo                                    Regra de Validação                                    Aplic. Msg                     Descrição Erro
 B10a-10 65   NFC-e com data de previsão de entrega (tag: dPrevEntrega, id: B10a)                      Obrig. 1153 Rejeição: NFC-e com data de previsão de entrega
 B10a-20 55   Se informado data de previsão de entrega (tag: dPrevEntrega, id: B10a):                  Obrig. 1154 Rejeição: Data de previsão de entrega posterior ao
               - Data de previsão de entrega (dPrevEntrega) superior a 3 meses a partir da data de                 permitido
                 saída da nota (tag: dhSaiEnt, id: B10)
              Observação: caso a data de saída (dhSaiEnt) não esteja preenchida, considerar a data
                 de emissão (tag: dhEmi, id: B09).
 B10a-30 55   Se informado data de previsão de entrega (tag: dPrevEntrega, id: B10a):                  Obrig. 1155 Rejeição: Data de previsão de entrega anterior ao
               - Data de previsão de entrega (dPrevEntrega) anterior a data de saída da nota (tag:                 permitido
                 dhSaiEnt, id: B10)
              Observação 01: caso a data de saída (dhSaiEnt) não esteja preenchida, considerar a
                 data de emissão (tag: dhEmi, id: B09).
              Observação 02: não considerar a hora nesta validação, somente a data.

 Campo Modelo                                      Regra de Validação                                        Aplic. Msg                       Descrição Erro
 B10a-40  55   Se informado data de previsão de entrega (tag: dPrevEntrega, id: B10a):                       Obrig. 1156 Rejeição: Data de previsão de entrega não permitida
                 - Finalidade de emissão (tag: finNFe, id: B25) difere de “1” (NF-e normal) e “4”                        para a finalidade de emissão informada
                   (Devolução de mercadoria)
 B10a-50  55   Se modalidade do frete (tag: modFrete, id: X02) igual "1" (Contratação do Frete por conta     Obrig. 1157 Rejeição: Data de previsão de entrega não permitida
                   do Destinatário - FOB), "4" (Transporte Próprio por conta do Destinatário) ou "9" (Sem                para a modalidade de frete informada
                   Ocorrência de Transporte):
                 - Proibido informar data de previsão de entrega (tag: dPrevEntrega, id: B10a)
 B25-30   55   Se NF-e complementar (tag: finNFe=2) ou NF-e de Crédito do tipo 1-Multa e Juros (tag:         Obrig.   254 Rejeição: NF-e não possui NF referenciada
               tpNFCredito=1) ou do tipo 3-Retorno (tag: tpNFCredito=3) ou do tipo 4-Redução de
               Valores (tag: tpNFCredito=4):
                 - Não informado NF referenciada (tag: NFref)
 B25-40   55   Se NF-e Complementar (tag: finNFe=2)                                                          Obrig.   255 Rejeição: NF-e possui mais de uma NF referenciada
                ou NF-e de Devolução (tag: finNFe=4)
                ou NF-e de Crédito do tipo 1-Multa e Juros (tag: tpNFCredito=1)
                ou NF-e de Crédito do tipo 3-Retorno (tag: tpNFCredito=3)
                ou NF-e de Crédito do tipo 4-Redução de Valores (tag: tpNFCredito=4):
                 - NF referenciada com mais de uma ocorrência (tag: NFref)
               Observação: implementação da alteração em Produção em 16/11/2026.
 B25-50   55   Se NF-e complementar (tag:finNFe=2) ou NF-e de Crédito do tipo 3-Retorno (tag:                Obrig.   269 Rejeição: CNPJ/CPF Emitente da NF-e difere do
               tpNFCredito=3) ou do tipo 4-Redução de Valores (tag: tpNFCredito=4):                                       CNPJ/CPF da NF Referenciada
                 - CNPJ/CPF emitente da NF Referenciada difere do CNPJ/CPF emitente desta NF-e
                   (NT 2018.001)
 B25-60   55   Se NF-e complementar (tag: finNFe=2) ou NF-e de Crédito do tipo 3-Retorno (tag:               Obrig.   678 Rejeição: NF referenciada com UF diferente desta NF-e
               tpNFCredito=3) ou do tipo 4-Redução de Valores (tag: tpNFCredito=4):
                 - UF da NF-e referenciada diferente da UF do emitente (NT 2013/003)
 B25-65   55   Se NF-e de Crédito do tipo 2-Apropriação de Crédito Presumido de IBS sobre o saldo            Obrig. 1027 Rejeição: NF referenciada informada indevidamente
               devedor na ZFM (tag: tpNFCredito=2):
                 - Informado NF referenciada (tag: NFref)
 B25-80   55   Se finalidade da NF-e igual a crédito ou débito (tag:finNFe=5 ou 6) ou tpOperGov=2-           Obrig. 1001 Rejeição: NF-e com finalidade de débito ou crédito
               Recebimento do pagamento:                                                                                 somente para IBS/CBS
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
 B25-90  55/65 Se finalidade da NF-e diferente de crédito e débito (tag:finNFe <> 5 e 6):                    Obrig. 1002 Rejeição: NF-e sem informação de ICMS / ISSQN
                 - Não informado ICMS (tag: ICMS) e não informado ISSQN (tag: ISSQN).

 Campo     Modelo                                       Regra de Validação                                    Aplic.   Msg                      Descrição Erro
                    Exceção: A regra acima não se aplica caso tpOperGov=2-Recebimento do pagamento.
 B25-100     55     Se NF-e de crédito (tag: finNFe = 5-NFe de Crédito):                                      Obrig.   1003 Rejeição: NF-e de crédito faz referência a documento
                      - NF-e referenciada (tag: NFref/refNfe) com modelo <> 55.                                             fiscal diferente de NF-e modelo 55
                    Exceção: caso tpNFCredito="03-Retorno”, permite também NFref modelo 65.
 B25-110     55     Se NF-e de crédito (tag: finNFe = 5-NFe de Crédito):                                      Obrig.   1161 Rejeição: Tipo de Operação incompatível com NF-e de
                      - Tipo de Operação diferente de “Entrada” (tag: tpNF <> 0)                                            Crédito
 B25-120     55     Se NF-e de débito (tag: finNFe = 6):                                                      Obrig.   1162 Rejeição: Tipo de Operação incompatível com NF-e de
                      - Tipo de Operação diferente de “Saída” (tag: tpNF <> “1”)                                            Débito
B25.1-10     55     Se informado tipo de nota de débito (tag: tpNFDebito)                                     Obrig.   1139 Rejeição: Tipo de nota de débito informado
                      - Finalidade <> 6-Nota de débito (tag:finNFe)                                                         indevidamente
B25.1-20     55     Se finalidade = 6-Nota de débito (tag:finNFe)                                             Obrig.   1009 Rejeição: Não informado tipo de nota de débito
                      - Não informado tipo de nota de débito (tag: tpNFDebito)
B25.2-10     55     Se informado tipo de nota de crédito (tag: tpNFCredito)                                   Obrig.   1163 Rejeição: Tipo de nota de crédito informado
                      - Finalidade <> 5-Nota de crédito (tag:finNFe)                                                        indevidamente
B25.2-20     55     Se finalidade = 5-Nota de crédito (tag:finNFe)                                            Obrig.   1164 Rejeição: Não informado tipo de nota de crédito
                      - Não informado tipo de nota de crédito (tag: tpNFCredito)
B25.2-30     55     Se tipo de nota de crédito (tag: tpNFCredito) igual a 02-Apropriação de crédito presumido Obrig.   1145 Rejeição: Tipo de nota de crédito só pode ser usado a
                    de IBS sobre o saldo devedor na ZFM (art. 450, § 1º, LC 214/25)                                         partir de janeiro/2029.
                      - Ano de emissão < 2029
B25.2-40     55     Se tipo de nota de crédito (tag: tpNFCredito) igual a 03-Retorno:                         Obrig.   1152 Rejeição: Tipo de Operação incompatível com NF-e de
                      - Tipo de Operação diferente de “Entrada” (tag: tpNF)                                                 Crédito do tipo Retorno
 B25b-20     65     NFC-e em uma operação não presencial (tag:indPres<>1, 4 e 5)                              Obrig.    717 Rejeição: NFC-e em operação não presencial
 B25b-60     65     Se informado município do fato gerador IBS (tag: cMunFGIBS)                               Obrig.   1000 Rejeição: Município do fato gerador do IBS informado
                      - Não é operação presencial fora do estabelecimento (tag: indPres <> 5)                               indevidamente
 B25b-70     65     Se não informado município do fato gerador IBS (tag: cMunFGIBS)                           Obrig.   1005 Rejeição: Operação presencial fora do estabelecimento
                      - É operação presencial fora do estabelecimento (tag: indPres = 5)                                    sem informação do município do fato gerador do IBS
 B25d-10     65     Se informado o código indicador do local da operação de fornecimento (tag: cIndOp):       Obrig.   1099 Rejeição: Não é permitido o uso do código indicador do
                      - Modelo DFe = 65-NFCe                                                                                local da operação de fornecimento na NFC-e modelo 65
 B25d-20     55     Se informado o código indicador do local da operação de fornecimento (tag: cIndOp):       Obrig.   1102 Rejeição: Código indicador do local de operação de
                      - cIndOp informado possui indicador que não permite ser utilizado na NF-e (indNFe = 0)                fornecimento não permitido neste modelo de DFe
                    Observação: Consultar tabela “Código Indicador de Local da Operação”.
 B25d-30     55     Se informado o código indicador do local da operação de fornecimento (tag: cIndOp) e      Obrig.   1110 Rejeição: Local de Retirada não informado
                    cIndOp = “010104” ou “010105”:
                      - Local de Retirada não informado (grupo: retirada, id: F01)

Grupo BB. Grupo de Compras Governamentais
 Campo Modelo                              Regra de Validação                                                Aplic. Msg                    Descrição Erro
 BB01-10 65   Informado gCompraGov na NFCe                                                                   Obrig. 1006 Rejeição: NFCe com grupo de compra governamental

 BB02-10     55     Se informado tpEnteGov (nota de compra governamental), verificar se alíquota de outros   Obrig. 1008 Rejeição: Nota de compra governamental e alíquota
                    entes está preenchida durante o período de transição:                                                dos outros entes informada incorretamente

 Campo     Modelo                                       Regra de Validação                                Aplic. Msg                     Descrição Erro
                    Se ano de emissão = 2027 a 2032, e tpEnteGov diferente de 5 e 6:
                      - Se compra da união (tag: tpEnteGov = 1)                                                        1=União
                         - Alíquota do IBS da UF (tag: pIBSUF) MAIOR QUE ZERO OU                                       2=Estado
                         - Alíquota do IBS do Município (tag: pIBSMun) MAIOR QUE ZERO                                  3=Distrito Federal
                      - Se compra estadual (tag: tpEnteGov = 2):                                                       4=Município
                         - Alíquota do IBS do Município (tag: pIBSMun) MAIOR QUE ZERO                                  5=Consórcio Público
                      - Se compra do DF (tag: tpEnteGov = 3):                                                          6=Comitê Gestor do IBS
                         - Alíquota do IBS do Município (tag: pIBSMun) MAIOR QUE ZERO
                      - Se compra municipal (tag: tpEnteGov = 4):
                         - Alíquota do IBS da UF (tag: pIBSUF) MAIOR QUE ZERO
                    Se ano de emissão = 2033 ou superior, e tpEnteGov diferente de 5 e 6:
                      - Se compra da união (tag: tpEnteGov = 1)
                         - Alíquota do IBS da UF (tag: pIBSUF) MAIOR QUE ZERO OU
                         - Alíquota do IBS do Município (tag: pIBSMun) MAIOR QUE ZERO
                      - Se compra estadual (tag: tpEnteGov = 2):
                         - Alíquota da CBS (tag: pCBS) MAIOR QUE ZERO OU
                         - Alíquota do IBS do Município (tag: pIBSMun) MAIOR QUE ZERO
                      - Se compra do DF (tag: tpEnteGov = 3):
                         - Alíquota da CBS (tag: pCBS) MAIOR QUE ZERO OU
                         - Alíquota do IBS do Município (tag: pIBSMun) MAIOR QUE ZERO
                      - Se compra municipal (tag: tpEnteGov = 4):
                         - Alíquota do IBS da UF (tag: pIBSUF) MAIOR QUE ZERO OU
                         - Alíquota da CBS (tag: pCBS) MAIOR QUE ZERO
                    Observação: Conforme Art. 473, § 1o e seus Incisos I, II, III e IV e Art. 372 da LC
                        214/2025.
 BB05-10     55     Se o tipo da operação com ente governamental for igual a 1-Fornecimento com         Obrig. 1195 Rejeição: Referenciado indevidamente DFe anterior em
                    pagamento posterior (tpOperGov=1):                                                              operação com ente governamental na operação de
                      - Chave de acesso do DFe anterior (gCompraGov/refDFeAnt) informada indevidamente              fornecimento com pagamento posterior
 BB05-20     55     Se o tipo da operação com ente governamental for igual a 2-Recebimento do pagamento Obrig. 1196 Rejeição: Não referenciado DFe anterior em operação
                    com fornecimento já realizado (tpOperGov=2):                                                    com ente governamental na operação de recebimento
                      - Chave de acesso do DFe anterior (gCompraGov/refDFeAnt) não informada                        do pagamento com fornecimento já realizado
 BB05-30     55     Se o tipo da operação com ente governamental for igual a 2-Recebimento do pagamento Obrig. 1197 Rejeição: Referenciado mais de um DFe anterior em
                    com fornecimento já realizado (tpOperGov=2):                                                    operação com ente governamental na operação de
                      - Informado indevidamente mais de uma chave de acesso do DFe anterior (refDFeAnt)             recebimento do pagamento com fornecimento já
                                                                                                                    realizado
 BB05-40     55     Se o tipo da operação com ente governamental for igual a 3-Fornecimento com         Obrig. 1198 Rejeição: Não referenciado DFe anterior em operação
                    pagamento já realizado (tpOperGov=3):                                                           com ente governamental na operação de fornecimento
                      - Chave de acesso do DFe anterior (gCompraGov/refDFeAnt) não informada                        com pagamento já realizado
 BB05-50     55     Se o tipo da operação com ente governamental for igual a 4-Recebimento do pagamento Obrig. 1199 Rejeição: Referenciado indevidamente DFe anterior em
                    com fornecimento posterior (tpOperGov=4):                                                       operação com ente governamental na operação de
                      - Chave de acesso do DFe anterior (gCompraGov/refDFeAnt) informada indevidamente              recebimento do pagamento com fornecimento posterior
 BB05-60     55     Se informado chave de acesso do documento fiscal anterior no grupo de compras       Obrig. 1203 Rejeição: DFe referenciado em operação com ente
                    governamentais (gCompraGov/refDFeAnt):                                                          governamental com tamanho inválido [nOcor:nnn]
                      - Para cada chave de acesso referenciada (refDFeAnt):

 Campo     Modelo                                       Regra de Validação                                 Aplic. Msg                    Descrição Erro
                        - Chave de acesso com tamanho diferente de 44 caracteres
 BB05-70     55     Se informado chave de acesso do documento fiscal anterior no grupo de compras          Obrig. 1204 Rejeição: DFe referenciado em operação com ente
                    governamentais (gCompraGov/refDFeAnt):                                                             governamental com Dígito Verificador inválido
                      - Para cada chave de acesso referenciada (refDFeAnt):                                            [nOcor:nnn]
                        - Dígito Verificador da Chave de Acesso inválido
 BB05-80     55     Se informado chave de acesso do documento fiscal anterior no grupo de compras          Obrig. 1205 Rejeição: DFe referenciado em operação com ente
                    governamentais (gCompraGov/refDFeAnt):                                                             governamental com UF inválida [nOcor:nnn]
                      - Para cada chave de acesso referenciada (refDFeAnt):
                        - Chave de Acesso referenciada com UF inválida
 BB05-90     55     Se informado chave de acesso do documento fiscal anterior no grupo de compras          Obrig. 1206 Rejeição: DFe referenciado em operação com ente
                    governamentais (gCompraGov/refDFeAnt):                                                             governamental com Ano inválido [nOcor:nnn]
                      - Para cada chave de acesso referenciada (refDFeAnt):
                        - Chave de Acesso referenciada com Ano Emissão < 06 ou > que o Ano corrente
BB05-100     55     Se informado chave de acesso do documento fiscal anterior no grupo de compras          Obrig. 1207 Rejeição: DFe referenciado em operação com ente
                    governamentais (gCompraGov/refDFeAnt):                                                             governamental com Mês inválido [nOcor:nnn]
                      - Para cada chave de acesso referenciada (refDFeAnt):
                        - Chave de Acesso referenciada com Mês Emissão < 01 ou > 12
BB05-110     55     Se informado chave de acesso do documento fiscal anterior no grupo de compras          Obrig. 1208 Rejeição: DFe referenciado em operação com ente
                    governamentais (gCompraGov/refDFeAnt):                                                             governamental com CNPJ/CPF inválido [nOcor:nnn]
                      - Para cada chave de acesso referenciada (refDFeAnt):
                        - Série = [0-909] e CNPJ zerado ou dígito inválido, ou
                        - Série = [910-969] e CPF zerado ou dígito inválido
                    Observação: Caso tpEmis = 3-NFF, considerar o 5º dígito do número da nota (nNF) para
                        determinar se CNPJ/CPF na Chave de Acesso:
                          CNPJ: 5º dígito do nNF = “1” , CPF: 5º dígito do nNF = “2”
BB05-120     55     Se informado chave de acesso do documento fiscal anterior no grupo de compras          Obrig. 1209 Rejeição: DFe referenciado em operação com ente
                    governamentais (gCompraGov/refDFeAnt):                                                             governamental com Modelo inválido [nOcor:nnn]
                      - Para cada chave de acesso referenciada (refDFeAnt):
                        - Modelo da NF-e referenciada diferente de 55
BB05-130     55     Se informado chave de acesso do documento fiscal anterior no grupo de compras          Obrig. 1210 Rejeição: DFe referenciado em operação com ente
                    governamentais (gCompraGov/refDFeAnt):                                                             governamental com Número inválido [nOcor:nnn]
                      - Para cada chave de acesso referenciada (refDFeAnt):
                        - Chave de Acesso referenciada com Número zerado
BB05-140     55     Se informado chave de acesso do documento fiscal anterior no grupo de compras          Obrig. 1211 Rejeição: DFe referenciado em operação com ente
                    governamentais (gCompraGov/refDFeAnt):                                                             governamental em duplicidade [nOcor:nnn]
                      - Para cada chave de acesso referenciada (refDFeAnt):
                        - Verificar duplicidade da NF-e referenciada (duplicidade de chave de acesso)
BB05-150     55     Se informado chave de acesso do documento fiscal anterior no grupo de compras          Obrig. 1212 Rejeição: DFe referenciado em operação com ente
                    governamentais (gCompraGov/refDFeAnt):                                                             governamental com a mesma Chave de Acesso da
                      - Para cada chave de acesso referenciada (refDFeAnt):                                            Nota Fiscal atual [nOcor:nnn]
                        - Nota Fiscal referenciada com a mesma Chave de Acesso da Nota Fiscal atual

 Campo Modelo                                   Regra de Validação                                       Aplic. Msg                     Descrição Erro
BB05-160 55   Se informado chave de acesso do documento fiscal anterior no grupo de compras              Obrig. 1213 Rejeição: DFe referenciado em operação com ente
              governamentais (gCompraGov/refDFeAnt):                                                                 governamental com tipo de emissão inválido
                - Para cada chave de acesso referenciada (refDFeAnt):                                                [nOcor:nnn]
                  - Se Mês-Ano da Chave de Acesso superior a Abril/11:
                    - Chave de Acesso referenciada com Tipo de Emissão Inválido (diferente de 1, 2, 3,
                      4, 5, 6, 7, 9)
BB05-170 55   Se informado chave de acesso do documento fiscal anterior no grupo de compras              Obrig. 1214 Rejeição: DFe referenciado em operação com ente
              governamentais (gCompraGov/refDFeAnt):                                                                 governamental deve existir e não estar cancelada
                - Para cada chave de acesso referenciada (refDFeAnt):                                                [nOcor:nnn]
                  - Acessar BD com Chave de Acesso referenciada:
                    - Chave de acesso deve existir e não estar cancelada
BB05-180 55   Se informado chave de acesso do documento fiscal anterior no grupo de compras              Obrig. 1215 Rejeição: DFe referenciado em operação com ente
              governamentais (gCompraGov/refDFeAnt):                                                                 governamental deve possuir o mesmo CNPJ base ou
                - Para cada chave de acesso referenciada (refDFeAnt):                                                CPF do emitente do documento [nOcor:nnn]
                  - O emitente do DFe referenciado deve ter o mesmo CNPJ Base ou CPF do emitente
                      deste documento fiscal
              Observação: No caso de Nota Fiscal Avulsa (NFA) com CNPJ da SEFAZ na Chave de
                      Acesso deve ser considerado o CNPJ Base ou CPF do Emitente.
BB05-190 55   Se o tipo da operação com ente governamental for igual a 2-Recebimento do pagamento        Obrig. 1216 Rejeição: DFe referenciado em operação com ente
              com fornecimento já realizado (tpOperGov=2):                                                           governamental deve ser de fornecimento com
                - Se informado chave de acesso do documento fiscal anterior no grupo de compras                      pagamento posterior [nOcor:nnn]
                  governamentais (gCompraGov/refDFeAnt):
                  - Para cada chave de acesso referenciada (refDFeAnt):
                    - O DFe referenciado deve ser de operação com ente governamental e possuir tipo
                      de operação igual a 1-Fornecimento com pagamento posterior (tpOperGov=1)
BB05-200 55   Se o tipo da operação com ente governamental for igual a 3-Fornecimento com                Obrig. 1217 Rejeição: DFe referenciado em operação com ente
              pagamento já realizado (tpOperGov=3):                                                                  governamental deve ser de recebimento do pagamento
                - Se informado chave de acesso do documento fiscal anterior no grupo de compras                      com fornecimento posterior [nOcor:nnn]
                  governamentais (gCompraGov/refDFeAnt):
                  - Para cada chave de acesso referenciada (refDFeAnt):
                    - O DFe referenciado deve ser de operação com ente governamental e possuir tipo
                      de operação igual a 4-Recebimento do pagamento com fornecimento posterior
                      (tpOperGov=4)

Grupo C. Identificação do Emitente da Nota Fiscal eletrônica
 Campo    Modelo                                   Regra de Validação                                    Aplic. Msg                      Descrição Erro
 C22-10    55/65 Se Inscrição do emitente na SUFRAMA (emit/ISUFemit) informada:                          Obrig. 1185 Rejeição: Município do Emitente não pertence à área
                  - Município do Emitente (tag:emit/cMun) diferente de:                                              incentivada - CBS
                     ZFM: 1302603-Manaus, 1303569-Rio Preto da Eva, 1301902-Itacoatiara
                     ALC: 1304062-Tabatinga (AM), 1600303-Macapá (AP), 1600600-Santana (AP),
                    1100106-Guajará-Mirim (RO), 1400100-Boa Vista (RR), 1400159-Bonfim (RR),
                    1200104-Brasileia (AC), 1200252-Epitaciolândia (AC), 1200203-Cruzeiro do Sul (AC)

 Campo     Modelo                                     Regra de Validação                                     Aplic. Msg                       Descrição Erro
 C22-20     55/65 Se Inscrição do emitente na SUFRAMA (emit/ISUFemit) informada:                             Obrig. 1186 Rejeição: Inscrição do emitente na Suframa com dígito
                   - Inscrição com dígito verificador inválido                                                           verificador inválido

Grupo E. Identificação do Destinatário
 Campo     Modelo                                   Regra de Validação                                       Aplic. Msg                    Descrição Erro
 E18-30      55   Se Inscrição SUFRAMA do Destinatário informada (tag:dest/ISUF):                            Obrig. 251 Rejeição: UF/Município destinatário não pertence a
                   - UF destinatário difere de AC-Acre, ou AM-Amazonas, ou RO-Rondônia, ou RR-                          SUFRAMA
                     Roraima, ou AP-Amapá (só para municípios 1600303-Macapá e 1600600-Santana)

Grupo I. Produtos e Serviços da NF-e
 Campo     Modelo                                    Regra de Validação                                      Aplic.   Msg                      Descrição Erro
 I05k-10     65   Se informada a Classificação para subapuração do IBS na ZFM (tag: tpCredPresIBSZFM, Obrig.          1165 Rejeição: Não é permitido informar a classificação para
                  id:I05k):                                                                                                subapuração do IBS na ZFM na NFC-e modelo 65
                    - Modelo igual a 65                                                                                    [nItem: 999]
 I05k-20     55   Se informada a Classificação para subapuração do IBS na ZFM (tag: tpCredPresIBSZFM, Obrig.          1166 Rejeição: Classificação para subapuração do IBS na
                  id:I05k):                                                                                                ZFM informado indevidamente. [nItem: 999]
                    - UF do Emitente difere de AC-Acre, ou AM-Amazonas, ou RO-Rondônia, ou RR-
                      Roraima, ou AP-Amapá (só para municípios 1600303-Macapá e 1600600-Santana)
 I05k-30     55   Se não informada a Classificação para subapuração do IBS na ZFM (tag:                      Obrig.   1167 Rejeição: Classificação para subapuração do IBS na
                  tpCredPresIBSZFM, id:I05k):                                                                              ZFM não informada [nItem: 999]
                    - Código da UF do Emitente do Documento Fiscal (tag:ide/cUF) igual a 13-AM e
                      emitente com inscrição de indústria incentivada.
                  Observação 01: Regra de Validação se aplica somente ao Amazonas.
                  Observação 02: Implementação futura.
                  Para NF-e com finalidade de devolução de mercadoria (tag: finNFe = 4) ou de Nota de
                  Crédito (tag: finNFe=5) do tipo “03=Retorno por Recusa Total na Entrega ou Por Não
                  Localização do Destinatário na Tentativa de Entrega” (tag: tpNFCredito=03) ou do tipo
                  “06=Retorno por Recusa Parcial na Entrega” (tag: tpNFCredito=06), somente serão
                  aceitos CFOPs de devolução de mercadoria.                                                                 Rejeição: CFOP inválido para Nota Fiscal de devolução
 I08-140     55                                                                                              Obrig.   327
                  Observação 1: Vide relação de CFOP de devolução de mercadoria na tabela de apoio                          ou de retorno de mercadoria [nItem:nnn]
                      publicada no Portal da NF-e (Tabela CFOP, indDevol=1).
                  Exceção 1: Aceitar os CFOP 1.949 e 2.949. (alterado na NT 2026.009)
                  Exceção 2: Aceitar os CFOP 5.949 e 6.949 na devolução simbólica de gás natural (NCM
                      27112100) nos termos do Ajuste SINIEF nº 22/21 (NT 2021.004)
                  Se informado CRT (id:C21) igual 4-MEI e idDest<>3:
                    - Se finalidade de devolução de mercadoria (tag:finNFe=4) ou tipo de nota de crédito
                                                                                                                           Rejeição: CFOP inválido para Nota Fiscal de devolução
                      igual a “03-Retorno por Recusa Total na Entrega ou Por Não Localização do
 I08-141     55                                                                                              Obrig.   1179 ou de retorno de mercadoria emitida por MEI
                      Destinatário na Tentativa de Entrega” (tag: tpNFCredito=03) ou igual a “06-Retorno por
                                                                                                                           [nItem:nnn]
                      Recusa Parcial na Entrega” (tag: tpNFCredito=06):
                       - Somente serão aceitos CFOP 1.202, 1.553, 2.202,2.553, 5.202 e 6.202

 Campo     Modelo                                      Regra de Validação                                   Aplic. Msg                    Descrição Erro
                    Para as NF-e que não tem a finalidade de devolução de mercadoria (tag: finNFe não é “2"
                    nem “4"), não serão aceitos CFOP de devolução de mercadoria. (NT 2013/005)
                    Exceção: Esta regra não se aplica para Nota de Crédito (tag: finNFe=5) dos tipos:
                      - 03=Retorno por Recusa Total na Entrega ou Por Não Localização do Destinatário na               Rejeição: CFOP de devolução de mercadoria para NF-e
 I08-144     55         Tentativa de Entrega” (tag: tpNFCredito=03);                                        Obrig. 328 que não é de devolução ou de retorno de mercadoria
                      - 04=Redução de valores (tag: tpNFCredito=04);                                                   [nItem:nnn]
                      - 06=Retorno por Recusa Parcial na Entrega” (tag: tpNFCredito=06).
                    Observação: Vide relação de CFOP de devolução de mercadoria na tabela de apoio
                        publicada no Portal da NF-e (Tabela CFOP, indDevol=1). (NT 2015.002)

Grupo LA. Item / Combustível
Campo Modelo                                  Regra de Validação                                        Aplic. Msg                     Descrição Erro
LA01-30 55/65 Não informado o grupo de combustível (tag: comb, id:LA01) e cClassTrib vinculado a        Obrig. 1106 Rejeição: Não informado grupo de combustível para
              combustível (cClassTrib=410013 ou cClassTrib iniciado por “620”)                                      cClassTrib de Combustível [nItem: 999]

Grupo N. Item / Tributo: ICMS
Campo Modelo                                       Regra de Validação                                  Aplic. Msg                   Descrição Erro
N11-10 55/65 Se informado o grupo “ICMS” (id: N01) e CRT (id:C21) diferente de 4 e não informado o     Obrig. 966 Rejeição: Obrigatório o preenchimento da origem da
              campo orig (ou valor "nulo") (id: N11):                                                             mercadoria [nItem:nnn]
                 - Obrigatório o preenchimento da origem da mercadoria (id: N11)
              Exceção: A regra acima não se aplica para a NF-e de Crédito (finNFe=5) e para NF-e de
                  Débito (finNFe=6).
N12-110 55/65 Se produto (tag: cProdANP) está presente na Tabela de Combustíveis Sujeitos à Tributação Obrig. 960 Rejeição: Obrigatório o preenchimento de Grupo de
              Monofásica (coluna cProdANP):                                                                       Tributação do ICMS monofásica sobre combustíveis.
                - Obrigatório o preenchimento de CST de tributação monofásica sobre combustíveis (CST=            [nItem:999]
                  02, 15, 53, 61)
              Exceção: A regra acima não se aplica para a NF-e de Crédito (finNFe=5) e NF-e de Débito
                  (finNFe=6).
              Observação 1: Tabela de Combustíveis Sujeitos à Tributação Monofásica publicada na aba
                  “Documentos”, opção “Diversos” do Portal Nacional da Nota Fiscal Eletrônica
              Observação 2: Regra válida a partir de 25/09/2023 em homologação e 30/10/2023 em
                  produção.
              Observação 3: Também poderão ser aceitos os CST 40, 41, 50 e 90.

Grupo NA. Item / ICMS para a UF de Destino
Campo Modelo                                   Regra de Validação                                          Aplic. Msg                    Descrição Erro
NA01-20 55   Não informado grupo de ICMS para a UF de Destino (tag:ICMSUFDest):                            Obrig. 694 Rejeição: Não informado o grupo de ICMS para a UF
              - Operação Interestadual (idDest=2) e                                                                   de destino [nItem: 999]
              - Operação com Consumidor Final (indFinal=1) e
              - Operação com Não Contribuinte (indIEDest=9) e

 Campo    Modelo                                       Regra de Validação                                   Aplic. Msg                 Descrição Erro
                    - Não é operação de prestação de serviços (não existe tag “ISSQN").
                   Exceção 1: Esse grupo não deve ser exigido se o Grupo de Partilha do ICMS (campo
                      ICMSPart) estiver preenchido.
                   Exceção 2: A regra de validação não se aplica, em produção, para Nota Fiscal com data de
                      emissão anterior a 01/07/2016.
                   Exceção 3: A regra de validação não se aplica para Devolução de Mercadoria (finNFe=4)
                      que referencie Nota Fiscal com chave de acesso anterior a 2016.
                   Exceção 4: A regra de validação acima não se aplica para as operações com CFOP de
                      Retorno de Mercadorias (Tabela CFOP, indRetor=1).
                   Exceção 5: A regra de validação acima não se aplica nas NF-e de entrada (tpNF=0).
                   Exceção 6: A regra de validação acima não se aplica nas operações com combustíveis
                      (tag:comb) derivados de petróleo: código ANP diferente de: 820101001, 820101010,
                      810102001, 810102004, 810102002, 810102003, 810101002, 810101001, 810101003,
                      220101003, 220101004, 220101002, 220101001, 220101005, 220101006, 560101001.
                   Exceção 7: A regra de validação acima não se aplica se informada UF do local de entrega
                      (tag: entrega/UF) igual à UF do emitente (tag: emit/enderEmit/UF).
                   Exceção 8: A regra de validação acima não se aplica para as operações com CFOP de
                      Remessa de Mercadoria (Tabela CFOP, indRemes=1).
                   Exceção 9: A regra de validação acima não se aplica para os CFOP:
                    - 6.552 - Transferência de bem do ativo imobilizado;
                    - 6.922 - Lançamento efetuado a título de simples faturamento decorrente de venda p/
                      entrega futura;
                    - 6.929 - Lançamento relativo a Cupom Fiscal.
                   Exceção 10: Esta regra de validação não se aplica nas operações isentas (CST=40-Isenta
                      ou CSOSN=103-Isento), imunes ou não tributadas (CST=41-Não tributada, ou
                      CSOSN=300-Imune, ou CSOSN=400-Não tributada pelo Simples Nacional).
                   Exceção 11: A regra de validação acima não se aplica às seguintes Finalidades de NF-e:
                    - Complementar (finNFe=2)
                    - Ajuste (finNFe=3)
                    - Crédito (finNFe=5)
                    - Débito (finNFe=6)
                    - tpOperGov=2-Recebimento do pagamento
                   Exceção 12: A regra de validação acima não se aplica para emitentes optantes pelo
                      Simples Nacional (CRT=1 ou 4). (NT 2017.002 / NT 2015.003)

Grupo Q. Item / Tributo: PIS
Campo Modelo                                   Regra de Validação                                       Aplic. Msg                   Descrição Erro
Q01-20  55   NF-e sem o grupo de tributação pelo PIS (id:Q01).                                          Obrig. 745 Rejeição: NF-e sem grupo do PIS [nItem:nnn]
             Exceção: A regra acima não se aplica para:
              - NF-e de Crédito (finNFe=5);
              - NF-e de Débito (finNFe=6);
              - tpOperGov=2-Recebimento do pagamento.

Grupo S. Item / Tributo: COFINS
Campo Modelo                                   Regra de Validação                                              Aplic. Msg                   Descrição Erro
S01-20  55   NF-e sem o grupo de tributação pela COFINS (id:S01).                                              Obrig. 748 Rejeição: NF-e sem grupo da COFINS [nItem:nnn]
             Exceção: A regra acima não se aplica para:
              - NF-e de Crédito (finNFe=5);
              - NF-e de Débito (finNFe=6);
              - tpOperGov=2-Recebimento do pagamento.

Grupo UB. Informações dos tributos IBS / CBS e Imposto Seletivo
 Campo      Modelo                                   Regra de Validação                                         Aplic. Msg                      Descrição Erro
 UB01-10     55/65 Não é permitido uso do Imposto Seletivo (grupo: imposto/IS) para este cClassTribIS.          Obrig. 1011 Rejeição: Não é permitido uso do Imposto Seletivo
                   Nota: Implementação Futura.                                                                              para esta classificação da operação [nItem: 999]
 UB01-20     55/65 É exigido uso do Imposto Seletivo (grupo: imposto/IS) para este cClassTribIS.                Obrig. 1012 Rejeição: É exigido o uso do Imposto Seletivo para
                   Nota: Implementação Futura.                                                                              esta classificação da operação [nItem: 999]
 UB01-30     55/65 É exigido uso do Imposto Seletivo (grupo: imposto/IS) para este NCM.                         Obrig. 1013 Rejeição: É exigido o uso do Imposto Seletivo para
                   Nota: Implementação Futura.                                                                              esta classificação da operação para este NCM [nItem:
                                                                                                                            999]
 UB02-10     55/65 Se CST do Imposto Seletivo for informado, este deve existir na tabela de Código de           Obrig. 1014 Rejeição: CST do Imposto Seletivo informado
                   Situação Tributária (tag: imposto/IS/CSTIS).                                                             inexistente [nItem: 999]
                   Nota: Implementação Futura.
 UB03-10     55/65 Se cClassTribIS for informado, este deve existir na tabela de Classificação Tributária do    Obrig. 1015 Rejeição: Classificação Tributária do Imposto Seletivo
                   Imposto Seletivo (tag: imposto/IS/cClassTribIS)                                                          informada inexistente [nItem: 999]
                   Nota: Implementação Futura.
 UB05-10     55/65 -Valor da Base de cálculo do Imposto Seletivo (vBCIS) deve ser igual ao somatório de:        Obrig 1103 Rejeição: Valor da Base de cálculo do Imposto
                       (+) vProd                                                                                           Seletivo difere do somatório dos valores que a
                       (+) vServ                                                                                           compõem [nItem: 999]
                       (+) vFrete
                       (+) vSeg
                       (+) vOutro
                       (+) vII
                       (-) vDesc
                       (-) vPIS
                       (-) vCOFINS
                       (-) vICMS
                       (-) vICMSUFDest
                       (-) vFCP
                       (-) vFCPUFDest
                       (-) vICMSMono
                       (-) vISSQN
                   Exceção 1: Não subtrair o valor do PIS por Substituição Tributária (PIST/vPIS) quando
                       compor o valor total da NF-e (se indSomaPISST=1);

  Campo     Modelo                                        Regra de Validação                                       Aplic.   Msg                      Descrição Erro
                     Exceção 2: Não subtrair o valor do COFINS por Substituição Tributária
                          (COFINSST/vCOFINS) quando compor o valor total da NF-e (se
                          indSomaCOFINSST=1).
                     Nota: Implementação Futura.
 UB06-10     55/65   Se CSTIS informado exigir grupo do Imposto Seletivo e exigir a alíquota (tag: pIS)            Obrig.   1016 Rejeição: CST do Imposto Seletivo obriga informação
                     diferente de Zero, mas informada alíquota (tag: pIS) do imposto seletivo igual a zero. (tag:                de alíquota de Imposto Seletivo [nItem: 999]
                     imposto/IS/pIS).
                     Nota: Implementação Futura.
 UB07-10     55-65   Se CSTIS informado exigir grupo do Imposto Seletivo e exigir a alíquota específica (tag:      Obrig.   1017 Rejeição: Obrigatório informação de alíquota
                     imposto/IS/pISEspec) diferente de Zero e NCM do item for 2401, 2402, 2403, 2404, 2203,                      específica de Imposto Seletivo [nItem: 999]
                     2204, 2205, 2206, 2208.
                     Nota: Implementação Futura.
 UB08-10     55/65   Se CSTIS informado exigir grupo do Imposto Seletivo (grupo: imposto/IS) e unidade             Obrig.   1018 Rejeição: Unidade tributável (uTrib) e Quantidade
                     tributável (tag: imposto/IS/uTrib) e quantidade tributável (tag: imposto/IS/qTrib) não                      tributável (qTrib) do imposto seletivo não informados
                     informadas ou iguais a zero.                                                                                [nItem: 999]
                     Nota: Implementação Futura.
 UB11-10     55/65   Se informado imposto seletivo (tag: imposto/IS):                                              Obrig.   1019 Rejeição: Valor do Imposto Seletivo difere do
                         Valor do IS (vIS) = BC (tag: vBCIS) * (Alq (tag: pIS) / 100)                                            calculado [nItem: 999]
                     Observação 1: Se informada alíquota específica (tag: IS/pISEspec):
                         Valor do IS (vIS) = BC (tag: vBCIS) * (Alq (tag: pIS) / 100) + qtd (tag: IS/qTrib) * (Alq
                         (tag: IS/pISEspec) / 100)
                     Observação 2: Aceitar uma tolerância de 0,01 a mais ou a menos.
                     Nota: Implementação Futura.
 UB12-10     55/65   Não informado grupo de imposto IBS e CBS (grupo: det/imposto/IBSCBS)                          Obrig.   1115 Rejeição: Grupo IBSCBS não informado [nItem: 999]
                     Exceção 1: Não se aplica à NFe de devolução de mercadorias (tag: finNFe = 4) ou NFe
                          complementar (tag: finNFe = 2) que referencia NFe com data de emissão anterior a
                          2027.
                          Nota: No caso de NF-e de Devolução de mercadorias (tag: finNFe = 4), a chave de
                          acesso pode estar referenciada no cabeçalho (grupo: NFref, id: BA01) ou no item
                          (grupo: DFeReferenciado, id: VC01).
                     Exceção 2: Não se aplica caso informado campo cProdANP (id: LA02) e produto está
                          presente na Tabela de Combustíveis Sujeitos à Tributação Monofásica (coluna
                          cProdANP).
                     Observação 1: implementação em homologação para NFe com data de emissão maior
                          ou igual a 01/07/2026 e emitente com CRT 3=Regime Normal.
                     Observação 2: implementação futura para produção.
                     Observação 3: Tabela de Combustíveis Sujeitos à Tributação Monofásica publicada na
                          aba “Documentos”, opção “Diversos” do Portal Nacional da Nota Fiscal Eletrônica.
 UB13-10     55/65   Se informada a tag CST do IBS/CBS (tag: IBSCBS/CST):                                          Obrig.   1020 Rejeição: CST do IBS/CBS informado inexistente
                        - CST inexistente                                                                                        [nItem: 999]
 UB13-20     55/65   Se CST do IBS/CBS (tag: IBSCBS/CST) informado possui indicador que não permite a              Obrig.   1021 Rejeição: Grupo gIBSCBS informado indevidamente
                     informação do IBS/CBS (ind_gIBSCBS = 0):                                                                    [nItem: 999]
                        - Grupo gIBSCBS informado indevidamente (id: UB15, grupo:
                          imposto/IBSCBS/gIBSCBS)

  Campo     Modelo                                      Regra de Validação                                   Aplic. Msg                      Descrição Erro
                     Observação 1: Consultar Tabela de Indicadores de CST do IBS e da CBS.
 UB13-30     55/65   Se CST do IBS/CBS (tag: IBSCBS/CST) informado possui indicador que exige                Obrig. 1022 Rejeição: Grupo gIBSCBS não informado [nItem: 999]
                     informação do IBS/CBS (ind_gIBSCBS = 1):
                       - Grupo gIBSCBS não informado (id: UB15, grupo: imposto/IBSCBS/gIBSCBS)
                     Exceção: Esta RV não se aplica no caso de tpNFDebito=07-Perda em estoque.
                     Observação 1: Consultar Tabela de Indicadores de CST do IBS e da CBS.
 UB13-39     55/65   Se CST do IBS/CBS (tag: IBSCBS/CST) informado possui indicador que não permite a        Obrig. 1151 Rejeição: Grupo gIBSCBSMono informado
                     informação do IBS/CBS Monofásico (ind_gIBSCBSMono = 0):                                             indevidamente [nItem: 999]
                       - Grupo gIBSCBSMono (id: UB84, grupo: imposto/IBSCBS/gIBSCBSMono) informado
                         indevidamente
                     Observação 1: Consultar Tabela de Indicadores de CST do IBS e da CBS.
 UB13-40     55/65   Se CST do IBS/CBS (tag: IBSCBS/CST) informado possui indicador que exige                Obrig. 1116 Rejeição: Grupo gIBSCBSMono não informado [nItem:
                     informação do IBS/CBS Monofásico (ind_gIBSCBSMono = 1):                                             999]
                       - Grupo gIBSCBSMono (id: UB84, grupo: imposto/IBSCBS/gIBSCBSMono) não
                         informado
                     Exceção: Esta RV não se aplica no caso de tpNFDebito=07-Perda em estoque.
                     Observação 1: Consultar Tabela de Indicadores de CST do IBS e da CBS.
                     Observação 2: Implementação futura para produção.
                     Observação 3: Implementação futura para homologação.
 UB13-44     55/65   Se CST do IBS/CBS (tag: IBSCBS/CST) possui indicador que não permite informação do      Obrig. 1131 Rejeição: Grupo de transferência de crédito informado
                     grupo de Transferência de Crédito (ind_gTransfCred = 0):                                            indevidamente [nItem: 999]
                       - Grupo gTransfCred (id: UB106, grupo: imposto/IBSCBS/gTransfCred) informado
                         indevidamente
                     Observação 1: Consultar Tabela de Indicadores de CST do IBS e da CBS.
 UB13-45     55/65   Se CST do IBS/CBS (tag: IBSCBS/CST) possui indicador que exige informação do grupo      Obrig. 1132 Rejeição: Grupo de transferência de crédito não
                     de Transferência de Crédito (ind_gTransfCred = 1):                                                  informado [nItem: 999]
                       - Grupo gTransfCred (id: UB106, grupo: imposto/IBSCBS/gTransfCred) não informado
                     Observação 1: Consultar Tabela de Indicadores de CST do IBS e da CBS.
 UB14-10     55/65   Se cClassTrib (id: UB14, tag: IBSCBS/cClassTrib) for informado:                         Obrig. 1023 Rejeição: Classificação Tributária do IBS/CBS
                       - cClassTrib inexistente                                                                          informada inexistente [nItem: 999]
 UB14-20     55/65   Se cClassTrib (id: UB14, tag: IBSCBS/cClassTrib) for informado:                         Obrig. 1024 Rejeição: Rejeição: Classificação Tributária do IBS e
                       - cClassTrib incompatível com CST (tag: IBSCBS/CST)                                               da CBS incompatível com o CST informado [nItem:
                     Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.                    999]
 UB14-25     55/65   Se informada tag cClassTrib do IBS/CBS (tag: IBSCBS/cClassTrib):                        Obrig. 1025 Rejeição: cClassTrib do IBS/CBS não permitido neste
                       - cClassTrib informado possui indicador que não permite ser utilizado no respectivo               modelo de DFe [nItem: 999]
                         modelo de DFe (indNFe = 0 para modelo 55 e indNFCe = 0 para modelo 65):
                     Observação 1: Consultar Tabela de Indicadores de cClassTrib do IBS e CBS.
 UB14-30      55     Se cClassTrib (id: UB14, tag: IBSCBS/cClassTrib) for igual a 620004:                    Obrig. 1043 Rejeição: Índice de mistura do Biocombustível inferior
                       - Percentual do índice de mistura do Etanol Anidro na Gasolina C (id: LA17, tag:                  ao obrigatório para esta Classificação Tributária do
                         comb/pBio) deve ser superior ao obrigatório correspondende ao respectivo código                 IBS e CBS [nItem: 999]
                         ANP (tag: cProdANP), observado o art. 179 IIa da LC 214/2025
                     Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.

  Campo     Modelo                                      Regra de Validação                                   Aplic.   Msg                      Descrição Erro
                     Observação 2: Consultar Tabela Índice de mistura do Biocombustível publicada na aba
                         “Documentos”, opção “Diversos” do Portal Nacional da Nota Fiscal Eletrônica.
 UB14-50      55     Se cClassTrib (id: UB14, tag: IBSCBS/cClassTrib) for igual a 620005:                    Obrig.   1059 Rejeição: Índice de mistura do Biocombustível
                       - Percentual do índice de mistura do Etanol Anidro na Gasolina C (id: LA17, tag:                    superior ao obrigatório para esta Classificação
                         comb/pBio) deve ser inferior ao obrigatório correspondende ao respectivo código                   Tributária do IBS e CBS [nItem: 999]
                         ANP (tag: cProdANP), observado o art. 179 IIb da LC 214/2025
                     Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
                     Observação 2: Consultar Tabela Índice de mistura do Biocombustível publicada na aba
                         “Documentos”, opção “Diversos” do Portal Nacional da Nota Fiscal Eletrônica.
                                                                   -- cClassTrib x tpNFCredito / tpNFDebito --
 UB14-60      55     Validar se cClassTrib é compatível com o tpNFDebito OU tpNFCredito, de acordo com a Obrig.       1202 Rejeição: cClassTrib incompatível com a finalidade da
                     tabela abaixo:                                                                                        nota ou com o tipo de Nota de Débito ou Crédito
                                              cClassTrib                         tpNFDebito tpNFCredito                    [nItem: 999]
                        410030-Estorno de crédito por perda                          07              -
                        800001-Fusão, cisão ou incorporação                          05             05
                        800002-Transferência de crédito do associado                 01              -
                        810001-Crédito presumido IBS ZFM                              -             02
                        811001-Anulação Crédito por Saída Imune/Isenta               02              -
                        811002-Débito de NF não processada na apuração               03              -
                        811003-Desenquadramento Simples Nacional                     08              -
                     -
 UB14-70      55     Se informado tipo de nota de débito (tag: tpNFDebito):                                  Obrig.   1200 Rejeição: cClassTrib incompatível com o tipo de Nota
                       - Validar se tpNFDebito é compatível com o cClassTrib, de acordo com a tabela abaixo:               de Débito [nItem: 999]
                                                     tpNFDebito                                 cClassTrib
                        01=Transferência de créditos para Cooperativas;                        800002
                        02=Anulação de Crédito por Saídas Imunes/Isentas;                      811001
                        03=Débitos de notas fiscais não processadas na apuração;               811002
                        04=Multa e juros;                                                      Não limitar
                        05=Transferência de crédito na sucessão;                               800001
                        06=Pagamento antecipado;                                               Não limitar
                        07=Perda em estoque;                                                   410030
                        08=Desenquadramento do SN;                                             811003
                     -

 Campo      Modelo                                      Regra de Validação                                 Aplic. Msg                      Descrição Erro
 UB14-80      55   Se informado tipo de nota de crédito (tag: tpNFCredito):                                Obrig. 1201 Rejeição: cClassTrib incompatível com o tipo de Nota
                      - Validar se tpNFCredito é compatível com o cClassTrib, de acordo com a tabela                   de Crédito [nItem: 999]
                        abaixo:
                                                     tpNFCredito                            cClassTrib
                       01=Multa e Juros                                                    Não limitar
                       02=Apropriação de crédito presumido de IBS sobre o saldo devedor 810001
                          na ZFM (art. 450, § 1º, LC 214/25)
                       03=Retorno por recusa total na entrega ou por não localização do    Não limitar
                          destinatário na tentativa de entrega
                       04=Redução de valores                                               Não limitar
                       05=Transferência de crédito na sucessão                             800001
                       06=Retorno por recusa parcial na entrega                            Não limitar
                   --

 UB16-10     55/65 Valor da Base de cálculo do IBS e CBS (gIBSCBS/vBC) deve ser igual ao somatório de:     Obrig. 1104 Rejeição: Valor da Base de cálculo do IBS e CBS
                       (+) vProd                                                                                       difere do somatório dos valores que a compõem
                       (+) vServ                                                                                       [nItem: 999]
                       (+) vFrete
                       (+) vSeg
                       (+) vOutro
                       (+) vII
                       (-) vDesc
                       (-) vPIS
                       (-) vCOFINS
                       (-) vICMS
                       (-) vICMSUFDest
                       (-) vFCP
                       (-) vFCPUFDest
                       (-) vICMSMono
                       (-) vISSQN
                       (+) vIS
                   Exceção 1: Não subtrair o valor do PIS por Substituição Tributária (PIST/vPIS) quando
                       compor o valor total da NF-e (se indSomaPISST=1);
                   Exceção 2: Não subtrair o valor do COFINS por Substituição Tributária
                       (COFINSST/vCOFINS) quando compor o valor total da NF-e (se
                       indSomaCOFINSST=1).
                   Nota: Implementação Futura, aguardando orientação normativa.
 UB18-10     55/65 Se informado grupo de IBS Estadual (gIBSUF):                                            Obrig. 1026 Rejeição: Alíquota do IBS da UF inválida [nItem: 999]
                   A alíquota de IBS da UF (pIBSUF) deverá ser:
                     - 0,1% para documento com data de emissão no ano de 2025 e 2026. (Art. 343 da LC
                       214/25);
                     - 0,05% para documento com data de emissão no ano de 2027 e 2028. (Art. 344 da LC
                       214/25);

  Campo     Modelo                                       Regra de Validação                                     Aplic. Msg                     Descrição Erro
                      - Alíquota de referência ou específica a ser publicada para anos posteriores a 2028.
                     Exceção 1: Se o cClassTrib possuir indicador de Tributação Regular, o pIBSUF deve ser
                        igual a zero.
                     Exceção 2: A regra não se aplica caso:
                      - Finalidade de devolução de mercadoria (tag: finNFe=4);
                      - ou Nota de Crédito do tipo “03=Retorno por Recusa Total” (tag: tpNFCredito=03);
                      - ou Nota de Crédito do tipo “04=Redução de valores” (tag: tpNFCredito=04);
                      - ou Nota de Crédito do tipo “06=Retorno por Recusa Parcial” (tag: tpNFCredito=06).
 UB22-10     55/65   Se CST possui indicador que não permite o uso de diferimento (ind_gDif = 0):               Obrig. 1029 Rejeição: CST do IBS/CBS informado não permite
                      - Grupo de Diferimento informado indevidamente (grupo: gIBSUF/gDif)                                   informação de diferimento Estadual [nItem: 999]
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.
 UB22-20     55/65   Se informado grupo gIBSCBS (id: UB15, grupo: imposto/IBSCBS/gIBSCBS):                      Obrig. 1030 Rejeição: CST do IBS/CBS informado obriga
                      - Se CST possui indicador que exige o uso de diferimento (ind_gDif = 1):                              informação de diferimento Estadual [nItem: 999]
                         - Grupo de Diferimento não informado (grupo: gIBSUF/gDif)
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.
 UB23-10     55/65   Se informado grupo do Diferimento (gIBSUF/gDif):                                           Obrig. 1031 Rejeição: Valor do Diferimento da UF difere do
                      - Valor do Diferimento (vDif) deverá ser resultante da Base de Cálculo x Percentual do                calculado [nItem: 999]
                        IBS da UF x Percentual do Diferimento:
                          vDif = vBC x (pIBSUF / 100) x (pDif / 100)
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos
                     Observação 2: Em caso de preenchimento do grupo de redução (gIBSUF/gRed) a
                        alíquota utilizada deverá ser a tag Alíquota Efetiva (gIBSUF/gRed/pAliqEfet) ao invés
                        do pIBSUF.
 UB24-10     55/65   Se informado grupo de Devolução do IBS da UF (gIBSUF/gDevTrib):                            Obrig. 1111 Rejeição: Grupo de Devolução do IBS da UF
                      - Grupo de Devolução do IBS da UF informado indevidamente                                             informado indevidamente [nItem: 999]
 UB26-10     55/65   Se CST possui indicador que não permite o uso de Redução de Alíquota (ind_gRed = 0):       Obrig. 1032 Rejeição: CST do IBS/CBS informado não permite
                      - Grupo de Redução de Alíquota informado (grupo: gIBSUF/gRed)                                         informação de redução de alíquota Estadual [nItem:
                     Exceção: Percentual de redução da alíquota em compra governamental                                     999]
                        (tag:gCompraGov/pRedutor) informado e gIBSUF/gRed/pRedAliq igual a zero.
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.
 UB26-20     55/65   Se informado grupo gIBSCBS (id: UB15, grupo: imposto/IBSCBS/gIBSCBS):                      Obrig. 1033 Rejeição: Não informado o grupo de redução de
                      - Se CST possui indicador que exige o uso de Redução de Alíquota (ind_gRed = 1), ou                   alíquota Estadual [nItem: 999]
                        foi informado o grupo de compras governamentais (tag:gCompraGov):
                          - Grupo de Redução de Alíquota Estadual não informado (grupo: gIBSUF/gRed)
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.
 UB27-10     55/65   Se informado grupo de Redução de Alíquota (gIBSUF/gRed):                                   Obrig. 1034 Rejeição: Percentual de redução de alíquota da UF
                      - Se CST possui indicador que exige o uso de Redução de Alíquota (ind_gRed = 1):                      não é válido para este cClassTrib [nItem: 999]
                         - Percentual de Redução de Alíquota (pRedAliq) não é válido para este cClassTrib
                             (gIBSCBS/cClassTrib)
                      - Se CST possui indicador que veda o uso de Redução de Alíquota (ind_gRed = 0):
                         - Percentual de redução da alíquota em compra governamental
                             (tag:gCompraGov/pRedutor) não informado ou gIBSUF/gRed/pRedAliq maior que
                             zero
                     Observação 1: Consultar Tabela de CST e de cClassTrib do IBS e CBS.

  Campo     Modelo                                         Regra de Validação                                 Aplic. Msg                     Descrição Erro
                     Observação 2: No caso de Compra Governamental, o grupo gRed deve ser informado e
                         pRedAliq deve ser igual a zero, mesmo que o CST possua indicador que veda o
                         preenchimento.
 UB28-10     55/65   Se informado grupo de Redução de Alíquota (gIBSUF/gRed):                                 Obrig. 1035 Rejeição: Valor da Alíquota Efetiva do IBS da UF
                       - Alíquota Efetiva (tag: pAliqEfet) deve ser o resultado de:                                       calculado incorretamente [nItem: 999]
                         - Se NÃO houver compra governamental (grupo gCompraGov não informado):
                         pAliqEfet = pIBSUF × (1 - pRedAliq / 100).
                         - Se houver compra governamental (grupo gCompraGov informado):
                         pAliqEfet = pIBSUF × (1 - pRedAliq / 100) × (1 - gCompraGov/pRedutor / 100).
                     Exemplo: Redução de 40% na alíquota:
                        Alíquota vigente (A): 10%
                        Redução na alíquota (R): 40%
                        Redutor de compras governamentais (RG): 5%
                        Alíquota Efetiva (E): E = A * (1 - R) * (1 - RG)
                        E = 10 * (1 - 0,4) * (1 - 0,05) = 5,7
                     Observação: O cálculo da pAliqEfet deve considerar 4 casas decimais, com
                         arredondamento na última casa decimal.
 UB35-10     55/65   Se informado grupo IBS de competência das Unidades Federadas (gIBSUF):                   Obrig. 1041 Rejeição: Valor do IBS da UF difere do calculado
                       - Valor do IBS Estadual (vIBSUF) deverá ser resultante de:                                         [nItem: 999]
                              vIBSUF = (gIBSCBS/vBC x (pIBSUF / 100)) - vDif - vDevTrib
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos
                     Observação 2: Em caso de preenchimento do grupo de redução (gIBSUF/gRed) a
                         alíquota utilizada deverá ser a tag Alíquota Efetiva (gIBSUF/gRed/pAliqEfet):
                             vIBSUF = (gIBSCBS/vBC x (pAliqEfet / 100)) - vDif - vDevTrib
 UB37-10     55/65   Se informado grupo de IBS Municipal (gIBSMun):                                           Obrig 1036 Rejeição: Alíquota do IBS do Município inválida [nItem:
                     A alíquota de IBS do Município (pIBSMun) deverá ser:                                                999]
                       - 0% para documento com data de emissão no ano de 2025 e 2026. (Art. 343 da LC
                         214/25);
                       - 0,05% para documento com data de emissão no ano de 2027 e 2028. (Art. 344 da LC
                         214/25);
                       - Alíquota de referência ou específica a ser publicada para anos posteriores a 2028.
                     Exceção 1: Se o cClassTrib possuir indicador de Tributação Regular, o pIBSMun deve
                         ser igual a zero.
                     Exceção 2: A regra não se aplica caso:
                       - Finalidade de devolução de mercadoria (tag: finNFe=4);
                       - ou Nota de Crédito do tipo “03=Retorno por Recusa Total” (tag: tpNFCredito=03);
                       - ou Nota de Crédito do tipo “04=Redução de valores” (tag: tpNFCredito=04);
                       - ou Nota de Crédito do tipo “06=Retorno por Recusa Parcial” (tag: tpNFCredito=06).
 UB40-10     55/65   Se informado grupo gIBSCBS (id: UB15, grupo: imposto/IBSCBS/gIBSCBS):                    Obrig. 1044 Rejeição: CST do IBS/CBS informado obriga
                       - Se CST possui indicador que exige o uso de diferimento (ind_gDif =1):                            informação de diferimento Municipal [nItem: 999]
                         - Grupo de Diferimento não informado (grupo: gIBSMun/gDif)
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.
 UB40-20     55/65   CST possui indicador que não permite o uso de diferimento (ind_gDif = 0):                Obrig. 1083 Rejeição: CST do IBS/CBS informado não permite
                       - Grupo de Diferimento informado indevidamente (grupo: gIBSMun/gDif)                               informação de diferimento Municipal [nItem: 999]

  Campo     Modelo                                       Regra de Validação                                    Aplic.   Msg                     Descrição Erro
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.
 UB42-10     55/65   Se informado grupo do Diferimento (gIBSMun/gDif):                                         Obrig.   1045 Rejeição: Valor do Diferimento do Município difere do
                      - Valor do Diferimento (vDif) deverá ser resultante da Base de Cálculo x Percentual do                 calculado [nItem: 999]
                        IBS do Município x Percentual do Diferimento:
                            vDif = vBC x (pIBSMun / 100) x (pDif / 100)
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                     Observação 2: Em caso de preenchimento do grupo de redução (gIBSMun/gRed) a
                        alíquota utilizada deverá ser a tag Alíquota Efetiva (gIBSMun/gRed/pAliqEfet) ao invés
                        do pIBSMun.
 UB43-10     55/65   Se informado grupo de Devolução do IBS do Município (gIBSMun/gDevTrib):                   Obrig.   1112 Rejeição: Grupo de Devolução do IBS do Município
                      - Grupo de Devolução do IBS do Município informado indevidamente                                       informado indevidamente [nItem: 999]
 UB45-10     55/65   Se CST possui indicador que não permite o uso de Redução de Alíquota (ind_gRed = 0): Obrig.        1007 Rejeição: CST do IBS/CBS informado não permite
                      - Grupo de Redução de Alíquota Informado indevidamente (grupo: gIBSMun/gRed)                           informação de redução de alíquota municipal [nItem:
                     Exceção: Percentual de redução da alíquota em compra governamental                                      999]
                        (tag:gCompraGov/pRedutor) informado e gIBSMun/gRed/pRedAliq igual a zero.
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.
 UB45-20     55/65   Se informado grupo gIBSCBS (id: UB15, grupo: imposto/IBSCBS/gIBSCBS):                     Obrig.   1074 Rejeição: Não informado o grupo de redução de
                      - Se CST possui indicador que exige o uso de Redução de Alíquota (ind_gRed = 1), ou                    alíquota Municipal [nItem: 999]
                        foi informado o grupo de compras governamentais (grupo: gCompraGov):
                         - Grupo de Redução de Alíquota Municipal não informado (grupo: gIBSMun/gRed)
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.
 UB46-10     55/65   Se informado grupo de Redução de Alíquota (gIBSMun/gRed):                                 Obrig.   1046 Rejeição: Percentual de redução de alíquota do
                      - Se CST possui indicador que exige o uso de Redução de Alíquota (ind_gRed = 1):                       Município não é válido para este cClassTrib [nItem:
                         - Percentual de Redução de Alíquota (pRedAliq) não é válido para este cClassTrib                    999]
                        (gIBSCBS/cClassTrib)
                      - Se CST possui indicador que veda o uso de Redução de Alíquota (ind_gRed = 0):
                         - Percentual de redução da alíquota em compra governamental
                             (tag:gCompraGov/pRedutor) não informado ou gIBSUF/gRed/pRedAliq maior que
                             zero
                     Observação 1: Consultar Tabela de cClassTrib do IBS e CBS.
                     Observação 2: No caso de Compra Governamental, o grupo gRed deve ser informado e
                        pRedAliq deve ser igual a zero, mesmo que o CST possua indicador que veda o
                        preenchimento.
 UB47-10     55/65   Se informado grupo de Redução de Alíquota (gIBSMun/gRed):                                 Obrig.   1047 Rejeição: Valor da Alíquota Efetiva do IBS do
                      - Alíquota Efetiva (tag: pAliqEfet) deve ser igual ao resultado de:                                    Município calculado incorretamente [nItem: 999]
                         - Se NÃO houver compra governamental (grupo gCompraGov não informado):
                            pAliqEfet = pIBSMun × (1 - pRedAliq / 100).
                         - Se houver compra governamental (grupo gCompraGov informado):
                            pAliqEfet = pIBSMun × (1 - pRedAliq / 100) × (1 - gCompraGov/pRedutor / 100).
                     Exemplo: Redução de 40% na alíquota:
                       Alíquota vigente (A): 10%
                       Redução na alíquota (R): 40%
                       Redutor de compras governamentais (RG): 5%
                       Alíquota Efetiva (E): E = A * (1 - R)*(1-RG)

  Campo     Modelo                                       Regra de Validação                                 Aplic. Msg                      Descrição Erro
                      E = 10 * (1 - 0,4) *(1-0,05) = 5,7
                   Observação: O cálculo da pAliqEfet deve considerar 4 casas decimais, com
                       arredondamento na última casa decimal.
 UB54-10     55/65 Se informado grupo IBS de competência do Município (gIBSMun):                            Obrig. 1052 Rejeição: Valor do IBS Municipal difere do calculado
                     - Valor do IBS Municipal (vIBSMun) deverá ser resultante de:                                       [nItem: 999]
                          vIBSMun = (gIBSCBS/vBC x (pIBSMun / 100)) - vDif - vDevTrib
                   Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                   Observação 2: Em caso de preenchimento do grupo de redução (gIBSMun/gRed) a
                       alíquota utilizada deverá ser a tag Alíquota Efetiva (gIBSMun/gRed/pAliqEfet):
                           vIBSMun = (gIBSCBS/vBC x (pAliqEfet / 100)) - vDif – vDevTrib
 UB54a-10    55/65 Se informado gIBSCBS:                                                                    Obrig. 1150 Rejeição: Valor do IBS do Item (vIBS) difere do
                     - Valor do IBS do Item (vIBS) deverá ser resultante da soma do vIBSUF e vIBSMun.                   calculado [nItem: 999]
                       Caso utilizado cCredPres que possui indicador de dedução do Crédito Presumido
                       (indDeduzCredPres=1), o vCredPres deve ser subtraído.
                          vIBS = vIBSUF + vIBSMun – vCredPres (se indDeduzCredPres=1)
 UB56-10     55/65 Alíquota da CBS (tag: pCBS) deve ser igual a 0,9% para documento com data de             Obrig. 1037 Rejeição: Alíquota da CBS inválida [nItem: 999]
                   emissão no ano de 2025 e 2026. Art. 346 da LC 214/2025.
                   Exceção 1: Se o cClassTrib possuir indicador de Tributação Regular (ind_gTribRegular =
                       1), o pCBS deve ser igual a zero.
                   Exceção 2: A regra não se aplica caso tpNFCredito=04-Redução de valores.
                   Exceção 3: A Alíquota da CBS (tag: pCBS) pode ser igual a zero quando as duas
                       condições abaixo forem atendidas:
                     Condição 01: NCM do Produto (tag: prod/NCM) NÃO inicia por:
                       a) 93 (armas e munições);
                       b) 24 (fumos e derivados);
                       c) 2203 a 2208 (bebidas alcoólicas);
                       d) 8703 (automóveis de passageiros);
                       e) 33, exceto 3303 a 3307 (produtos de perfumaria ou de toucador).
                     Condição 02: Emitente e destinatário devem estar na mesma área incentivada (ou
                       seja, emitente e destinatário dentro da ZFM, ou emitente e destinatário na mesma
                       ALC), conforme relação abaixo:
                                        Município Emitente               Município Destinatário
                            ZFM    1301902-Itacoatiara (AM)           1301902-Itacoatiara (AM)
                                   1301902-Itacoatiara (AM)           1302603-Manaus (AM)
                                   1301902-Itacoatiara (AM)           1303569-Rio Preto da Eva (AM)
                                   1302603-Manaus (AM)                1301902-Itacoatiara (AM)
                                   1302603-Manaus (AM)                1302603-Manaus (AM)
                                   1302603-Manaus (AM)                1303569-Rio Preto da Eva (AM)
                                   1303569-Rio Preto da Eva (AM)      1301902-Itacoatiara (AM)
                                   1303569-Rio Preto da Eva (AM)      1302603-Manaus (AM)

  Campo     Modelo                                   Regra de Validação                                     Aplic. Msg                      Descrição Erro
                                    1303569-Rio Preto da Eva (AM)      1303569-Rio Preto da Eva (AM)
                           ALC 1    1304062-Tabatinga (AM)             1304062-Tabatinga (AM)
                           ALC 2    1100106-Guajará-Mirim (RO)         1100106-Guajará-Mirim (RO)
                           ALC 3    1400100-Boa Vista (RR)             1400100-Boa Vista (RR)
                                    1400100-Boa Vista (RR)             1400159-Bonfim (RR)
                                    1400159-Bonfim (RR)                1400100-Boa Vista (RR)
                                    1400159-Bonfim (RR)                1400159-Bonfim (RR)
                           ALC 4    1600303-Macapá (AP)                1600303-Macapá (AP)
                                    1600303-Macapá (AP)                1600600-Santana (AP)
                                    1600600-Santana (AP)               1600303-Macapá (AP)
                                    1600600-Santana (AP)               1600600-Santana (AP)
                           ALC 5    1200104-Brasileia (AC)             1200104-Brasileia (AC)
                                    1200104-Brasileia (AC)             1200252-Epitaciolândia (AC)
                                    1200104-Brasileia (AC)             1200203-Cruzeiro do Sul(AC)
                                    1200252-Epitaciolândia (AC)        1200104-Brasileia (AC)
                                    1200252-Epitaciolândia (AC)        1200252-Epitaciolândia (AC)
                                    1200252-Epitaciolândia (AC)        1200203-Cruzeiro do Sul(AC)
                                    1200203-Cruzeiro do Sul(AC)        1200104-Brasileia (AC)
                                    1200203-Cruzeiro do Sul(AC)        1200252-Epitaciolândia (AC)
                                    1200203-Cruzeiro do Sul(AC)        1200203-Cruzeiro do Sul(AC)
                   Observação: Alíquota de referência a ser publicada para anos posteriores a 2026.
 UB56-20     55/65 A partir de 2027, a alíquota da CBS (tag: pCBS) deve ser igual a alíquota vigente para o Obrig. 1037 Rejeição: Alíquota da CBS inválida [nItem: 999]
                   período conforme legislação.
                   Exceção 1: Se o cClassTrib possuir indicador de Tributação Regular (ind_gTribRegular =
                       1), o pCBS deve ser igual a zero.
                   Exceção 2: A regra não se aplica caso:
                     - Finalidade de devolução de mercadoria (tag: finNFe=4);
                     - ou Nota de Crédito do tipo “03=Retorno por Recusa Total” (tag: tpNFCredito=03);
                     - ou Nota de Crédito do tipo “04=Redução de valores” (tag: tpNFCredito=04);
                     - ou Nota de Crédito do tipo “06=Retorno por Recusa Parcial” (tag: tpNFCredito=06).
                   Exceção 3: Se o grupo gALCZFMCBS estiver preenchido, o pCBS deve ser igual a zero.
                   Observação: Consultar Tabela de Alíquotas da CBS.
 UB59-10     55/65 Se informado grupo gIBSCBS (id: UB15, grupo: imposto/IBSCBS/gIBSCBS):                    Obrig. 1061 Rejeição: CST do IBS/CBS informado obriga
                     - Se CST possui indicador que exige o uso de diferimento (ind_gDif = 1):                           informação de diferimento da CBS [nItem: 999]
                       - Grupo de Diferimento não informado (grupo: gCBS/gDif)

  Campo     Modelo                                      Regra de Validação                                   Aplic.   Msg                     Descrição Erro
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.
 UB59-20     55/65   Se CST possui indicador que não permite o uso de diferimento (ind_gDif = 0):            Obrig.   1090 Rejeição: CST do IBS/CBS informado não permite
                      - Grupo de Diferimento informado indevidamente (grupo: gCBS/gDif)                                    informação de diferimento da CBS [nItem: 999]
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.
 UB61-10     55/65   Se informado grupo do Diferimento (gCBS/gDif):                                          Obrig.   1062 Rejeição: Valor do Diferimento da CBS difere do
                      - Valor do Diferimento (vDif) deverá ser resultante da Base de Cálculo x Percentual da               calculado [nItem: 999]
                        CBS x Percentual do Diferimento:
                            vDif = vBC x (pCBS / 100) x (pDif / 100)
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                     Observação 2: Em caso de preenchimento do grupo de redução (gCBS/gRed) a alíquota
                        utilizada deverá ser a tag Alíquota Efetiva (gCBS/gRed/pAliqEfet) ao invés da pCBS.
 UB62-10      65     Se informado grupo de Devolução da CBS (gCBS/gDevTrib) na NFC-e:                        Obrig.   1187 Rejeição: Grupo de Devolução da CBS informado
                      - Grupo de Devolução da CBS informado indevidamente                                                  indevidamente [nItem: 999]
 UB62a-10     55     Se informado grupo de Devolução da CBS (gCBS/gDevTrib):                                 Obrig.   1188 Rejeição: Percentual de devolução da CBS não
                      - Percentual de devolução da CBS (pDevTrib) não informado                                            informado [nItem: 999]
 UB63-10      55     Se informado grupo de Devolução da CBS (gCBS/gDevTrib):                                 Obrig.   1189 Rejeição: Valor da CBS devolvida difere do calculado
                      - Valor da CBS devolvida (vDevTrib) deverá ser resultante da Base de Cálculo x                       [nItem: 999]
                        Percentual da CBS x Percentual do tributo devolvido:
                            vDevTrib = vBC x (pCBS / 100) x (pDevTrib / 100)
                     Observação 1: Em caso de preenchimento do grupo de Redução de Alíquota
                        (gCBS/gRed) a alíquota utilizada deverá ser a tag Alíquota Efetiva
                        (gCBS/gRed/pAliqEfet) ao invés do pCBS.
                     Observação 2: Aceitar uma tolerância de 0,01 a mais ou a menos.
 UB64-10     55/65   Se CST possui indicador que não permite o uso de redução de alíquota (ind_gRed = 0):    Obrig.   1028 Rejeição: CST do IBS/CBS informado não permite
                      - Grupo de Redução de Alíquota da CBS informado indevidamente (grupo: gCBS/gRed)                     informação de redução de alíquota da CBS [nItem:
                     Exceção: Percentual de redução da alíquota em compra governamental                                    999]
                        (tag:gCompraGov/pRedutor) informado e gCBS/gRed/pRedAliq igual a zero.
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.
 UB64-20     55/65   Se informado grupo gIBSCBS (id: UB15, grupo: imposto/IBSCBS/gIBSCBS):                   Obrig.   1079 Rejeição: Não informado o grupo de redução de
                      - Se CST possui indicador que exige o uso de Redução de Alíquota (ind_gRed = 1), ou                  alíquota da CBS [nItem: 999]
                        foi informado o grupo de compras governamentais (grupo: gCompraGov):
                         - Grupo de Redução de Alíquota da CBS não informado (grupo: gCBS/gRed)
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.

 Campo    Modelo                                      Regra de Validação                                Aplic.   Msg                     Descrição Erro
 UB65-10   55/65 Se informado grupo de Redução de Alíquota (gCBS/gRed):                                 Obrig.   1063 Rejeição: Percentual de redução de alíquota da CBS
                  - Se CST possui indicador que exige o uso de Redução de Alíquota (ind_gRed = 1):                    não é válido para este cClassTrib [nItem: 999]
                     - Percentual de Redução de Alíquota (pRedAliq) não é válido para este cClassTrib
                    (IBSCBS/cClassTrib)
                  - Se CST possui indicador que veda o uso de Redução de Alíquota (ind_gRed = 0):
                     - Percentual de redução da alíquota em compra governamental
                         (tag:gCompraGov/pRedutor) não informado ou gIBSUF/gRed/pRedAliq maior que
                         zero
                 Observação: Consultar Tabela de cClassTrib do IBS e CBS.
                 Observação 2: No caso de Compra Governamental, o grupo gRed deve ser informado e
                    pRedAliq deve ser igual a zero, mesmo que o CST possua indicador que veda o
                    preenchimento.
 UB66-10   55/65 Se informado grupo de Redução de Alíquota (gCBS/gRed):                                 Obrig.   1064 Rejeição: Valor da Alíquota Efetiva da CBS calculado
                  - Alíquota Efetiva (tag: pAliqEfet) deve ser o resultado de:                                        incorretamente [nItem: 999]
                     - Se NÃO houver compra governamental (grupo gCompraGov não informado):
                        pAliqEfet = pCBS × (1 - pRedAliq / 100).
                     - Se houver compra governamental (grupo gCompraGov informado):
                        pAliqEfet = pCBS × (1 - pRedAliq / 100) × (1 - gCompraGov/pRedutor / 100).
                 Exemplo: Redução de 40% na alíquota:
                   Alíquota vigente (A): 10%
                   Redução na alíquota (R): 40%
                   Redutor de compras governamentais (RG): 5%
                   Alíquota Efetiva (E): E = A * (1 - R)*(1-RG)
                   E = 10 * (1 - 0,4) *(1-0,05) = 5,7
                 Observação: O cálculo da pAliqEfet deve considerar 4 casas decimais, com
                    arredondamento na última casa decimal.
 UB66a-10 55/65 Se informado gCBS/gALCZFMCBS:                                                           Obrig.   1190 Rejeição: Inscrição do emitente na Suframa não
                  - Inscrição do emitente na Suframa (tag:emit/ISUFemit) não informada                                informado
 UB66a-20 55/65 Se informado gCBS/gALCZFMCBS:                                                           Obrig.   1191 Rejeição: Grupo de operações em áreas incentivadas
                  - NCM do Produto (tag: prod/NCM) inicia por:                                                        (ALC/ZFM) - CBS (alíquota zero) não permitido [nItem:
                     a) 93 (armas e munições);                                                                        999]
                     b) 24 (fumos e derivados);
                     c) 2203 a 2208 (bebidas alcoólicas);
                     d) 8703 (automóveis de passageiros);
                     e) 33, exceto 3303 a 3307 (produtos de perfumaria ou de toucador).
                  - OU Emitente e destinatário não estão na mesma área incentivada (ou seja, emitente e
                    destinatário não estão dentro da ZFM, ou emitente e destinatário não estão na mesma
                    ALC), conforme relação abaixo:
                                        Município Emitente              Município Destinatário
                            ZFM    1301902-Itacoatiara (AM)          1301902-Itacoatiara (AM)
                                   1301902-Itacoatiara (AM)          1302603-Manaus (AM)
                                   1301902-Itacoatiara (AM)          1303569-Rio Preto da Eva (AM)

  Campo     Modelo                                  Regra de Validação                                   Aplic. Msg                     Descrição Erro
                                   1302603-Manaus (AM)                1301902-Itacoatiara (AM)
                                   1302603-Manaus (AM)                1302603-Manaus (AM)
                                   1302603-Manaus (AM)                1303569-Rio Preto da Eva (AM)
                                   1303569-Rio Preto da Eva (AM)      1301902-Itacoatiara (AM)
                                   1303569-Rio Preto da Eva (AM)      1302603-Manaus (AM)
                                   1303569-Rio Preto da Eva (AM)      1303569-Rio Preto da Eva (AM)
                           ALC 1   1304062-Tabatinga (AM)             1304062-Tabatinga (AM)
                           ALC 2   1100106-Guajará-Mirim (RO)         1100106-Guajará-Mirim (RO)
                           ALC 3   1400100-Boa Vista (RR)             1400100-Boa Vista (RR)
                                   1400100-Boa Vista (RR)             1400159-Bonfim (RR)
                                   1400159-Bonfim (RR)                1400100-Boa Vista (RR)
                                   1400159-Bonfim (RR)                1400159-Bonfim (RR)
                           ALC 4   1600303-Macapá (AP)                1600303-Macapá (AP)
                                   1600303-Macapá (AP)                1600600-Santana (AP)
                                   1600600-Santana (AP)               1600303-Macapá (AP)
                                   1600600-Santana (AP)               1600600-Santana (AP)
                           ALC 5   1200104-Brasileia (AC)             1200104-Brasileia (AC)
                                   1200104-Brasileia (AC)             1200252-Epitaciolândia (AC)
                                   1200104-Brasileia (AC)             1200203-Cruzeiro do Sul(AC)
                                   1200252-Epitaciolândia (AC)        1200104-Brasileia (AC)
                                   1200252-Epitaciolândia (AC)        1200252-Epitaciolândia (AC)
                                   1200252-Epitaciolândia (AC)        1200203-Cruzeiro do Sul(AC)
                                   1200203-Cruzeiro do Sul(AC)        1200104-Brasileia (AC)
                                   1200203-Cruzeiro do Sul(AC)        1200252-Epitaciolândia (AC)
                                   1200203-Cruzeiro do Sul(AC)        1200203-Cruzeiro do Sul(AC)
                   Observação: Esta RV verifica se contribuinte preenche os requisitos do art. 451 ou 466
                       LCP 214/25 para a alíquota zero da CBS.
 UB66c-10    55/65 Se informado gCBS/gALCZFMCBS/tpALCZFMCBS = 2:                                          Obrig. 1192 Rejeição: Número do processo na Suframa não
                    - Número do processo na Suframa (tag:gALCZFMCBS/nProcSuframa) não informado ou                    informado [nItem: 999]
                       preenchido com zeros
 UB66e-10    55/65 Se informado gCBS/gALCZFMCBS:                                                          Obrig. 1218 Rejeição: Valor da CBS para operação fora de áreas
                     - vTribRegCBS (id: UB66e) deverá ser resultante de:                                              ou regimes incentivado difere do calculado [nItem:
                                                                                                                      999]

  Campo     Modelo                                     Regra de Validação                                   Aplic. Msg                      Descrição Erro
                           vTribRegCBS = gIBSCBS/vBC x (gALCZFMCBS/pAliqEfetRegCBS (id: UB66d) /
                            100)
 UB67-10     55/65   Se informado grupo CBS (gCBS):                                                         Obrig. 1069 Rejeição: Valor da CBS difere do calculado [nItem:
                      - Valor da CBS (vCBS) deverá ser resultante de:                                                   999]
                           vCBS = (gIBSCBS/vBC x (pCBS / 100)) - vDif - vDevTrib
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                     Observação 2: Se informado grupo de redução (gCBS/gRed) a alíquota utilizada deverá
                        ser a tag Alíquota Efetiva (gCBS/gRed/pAliqEfet):
                            vCBS = (gIBSCBS/vBC x (pAliqEfet / 100)) - vDif - vDevTrib
 UB68-10     55/65   Se não informado grupo da Tributação Regular (gIBSCBS/gTribRegular):                   Obrig. 1065 Rejeição: Classificação Tributária do IBS e da CBS
                      - Informado cClassTrib (tag: IBSCBS/cClassTrib) com indicador que exige informação                informada obriga informação da tributação regular
                        do grupo de Tributação Regular (ind_gTribRegular = 1)                                           [nItem: 999]
                     Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB68-11     55/65   Se informado grupo da Tributação Regular (gIBSCBS/gTribRegular):                       Obrig. 1114 Rejeição: Classificação Tributária do IBS e da CBS
                      - Informado cClassTrib (tag: IBSCBS/cClassTrib) com indicador que não permite                     informada não permite informação da tributação
                        informação do grupo de Tributação Regular (ind_gTribRegular = 0)                                regular [nItem: 999]
                     Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB69-10     55/65   Se informado grupo da Tributação Regular (gIBSCBS/gTribRegular):                       Obrig. 1066 Rejeição: CST do IBS e da CBS informado no grupo
                      - CST Regular (tag: gTribRegular/CSTReg) inexistente                                              de tributação regular inexistente [nItem: 999]
                     Observação: Consultar Tabela de Indicadores de CST do IBS e CBS.
 UB70-10     55/65   Se informado grupo da Tributação Regular (gIBSCBS/gTribRegular):                       Obrig. 1067 Rejeição: Classificação Tributária do IBS e da CBS
                      - cClassTrib Regular (tag: gTribRegular/cClassTribReg) inexistente                                informada no grupo de tributação regular inexistente
                     Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.                   [nItem: 999]
 UB72-10     55/65   Se informado grupo da Tributação Regular (gIBSCBS/gTribRegular):                       Obrig. 1040 Rejeição: Valor do Tributo Regular da UF difere do
                      - Valor do Tributo Regular do IBS Estadual (vTribRegIBSUF) deve ser resultante da                 calculado [nItem: 999]
                        Base de Cálculo x Alíquota Efetiva Regular do IBS do Estado:
                           vTribRegIBSUF = gIBSCBS/vBC x (gTribRegular/pAliqEfetRegIBSUF / 100)
                     Observação: Aceitar uma tolerância de 0,01 a mais ou a menos
 UB72b-10    55/65   Se informado o grupo Tributação Regular (gIBSCBS/gTribRegular):                        Obrig. 1051 Rejeição: Valor do Tributo Regular do Município difere
                      - Valor do Tributo Regular do IBS Municipal (vTribRegIBSMun) deve ser resultante da               do calculado [nItem: 999]
                        Base de Cálculo x Alíquota Efetiva Regular do IBS do Município:
                           vTribRegIBSMun = gIBSCBS/vBC x (gTribRegular/pAliqEfetRegIBSMun / 100)
                     Observação: Aceitar uma tolerância de 0,01 a mais ou a menos.
 UB72d-10    55/65   Se informado grupo da Tributação Regular (gIBSCBS/gTribRegular):                       Obrig. 1068 Rejeição: Valor do Tributo Regular da CBS difere do
                      - Valor do Tributo Regular da CBS (vTribRegCBS) deve ser resultante da Base de                    calculado [nItem: 999]
                        Cálculo x Alíquota Efetiva Regular da CBS:
                           vTribRegCBS = gIBSCBS/vBC x (gTribRegular/pAliqEfetRegCBS / 100)
                     Observação: Aceitar uma tolerância de 0,01 a mais ou a menos
 UB82a-10     55     Se grupo Compra Governamental (grupo: gCompraGov) informado:                           Obrig. 1141 Rejeição: Grupo de informações da composição do
                      - Grupo de informações da composição do valor do IBS e da CBS em compras                          valor do IBS e da CBS em compras governamentais
                        governamentais (ID:UB82a, grupo: gTribCompraGov) não informado.                                 não informado [nItem: 999]
                     Exceção: A regra não se aplica para CST do IBS/CBS (tag: IBSCBS/CST) que possui
                        indicador que não permite a informação do IBS/CBS (ind_gIBSCBS = 0)

   Campo Modelo                                       Regra de Validação                                Aplic. Msg                   Descrição Erro
 UB82a-20      55   Se grupo gTribCompraGov informado:                                                  Obrig. 1142 Rejeição: Soma dos valores de IBS e CBS em
                      - Soma dos valores de IBS e CBS do grupo gTribCompraGov (vTribIBSUF +                         compras governamentais divergente [nItem: 999]
                        vTribIBSMun + vTribCBS) difere do resultado de tag:gIBSUF/vIBSUF +
                        tag:gIBSMun/vIBSMun + tag:gCBS/vCBS.
                    Observação: Aceitar uma tolerância de 0,04 a mais ou a menos
 UB82a-30      55   Se grupo compra governamental (grupo: gCompraGov) não informado:                    Obrig. 1144 Rejeição: Grupo de informações da composição do
                      - Grupo de informações da composição do valor do IBS e da CBS em compras                      valor do IBS e da CBS em compras governamentais
                        governamentais (ID:UB82a, grupo: gTribCompraGov) informado indevidamente                    informado indevidamente [nItem: 999]
*** Tributação Monofásica: IBS Ad Rem
 UB85a-10 55/65 Se informado o grupo de Tributação Monofásica do IBS e CBS (id: UB84, grupo:            Obrig. 1219 Rejeição: Tributação Monofásica Ad Rem do IBS
                    gIBSCBSMono):                                                                                   informada indevidamente [nItem: 999]
                      - Se ano da data de emissão (id: B09, tag: dhEmi) menor ou igual a 2028:
                        - Informado indevidamente o grupo gIBSMonoAdRem (id: UB85a)                                 Observação: Tributação Monofásica do IBS e CBS:
                                                                                                                              Ano        IBS           CBS
                                                                                                                               2026 AdValorem AdValorem
                                                                                                                               2027 AdValorem AdRem
                                                                                                                               2028 AdValorem AdRem
                                                                                                                               2029 AdRem          AdRem
 UB85a-20    55/65 Se informado o grupo de Tributação Monofásica do IBS e CBS (id: UB84, grupo:         Obrig. 1220 Rejeição: Não informada Tributação Monofásica Ad
                   gIBSCBSMono):                                                                                    Rem do IBS [nItem: 999]
                     - Se ano da data de emissão (id: B09, tag: dhEmi) maior que 2028:
                       - Se cClassTrib possui ind_gMonoPadrao=1 ou ind_gMonoReten=1 ou                              Observação: Vide tabela acima
                          ind_gMonoRet=1 ou ind_gpBioDiferenca=1:
                          - Não informado o grupo gIBSMonoAdRem (id: UB85a)
                   Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB86-10     55/65 Se informado o grupo gIBSMonoAdRem (id: UB85a):                                      Obrig. 1125 Rejeição: Não informada a Tributação Monofásica
                     - Se cClassTrib possui indicador que exige Tributação Monofásica Padrão de                     Padrão de Combustível do IBS Ad Rem [nItem: 999]
                       Combustível (ind_gMonoPadrao = 1):
                       - Não informado o grupo gMonoPadrao do IBS Ad Rem (id: UB86, grupo:
                       gIBSMonoAdRem/gMonoPadrao)
                   Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB86-20     55/65 Se informado o grupo gIBSMonoAdRem (id: UB85a):                                      Obrig. 1126 Rejeição: Informada indevidamente a Tributação
                     - Se cClassTrib possui indicador que não permite Tributação Monofásica Padrão de               Monofásica Padrão de Combustível do IBS Ad Rem
                       Combustível (ind_gMonoPadrao = 0):                                                           [nItem: 999]
                        - Informado indevidamente o grupo gMonoPadrao do IBS Ad Rem (id: UB86, grupo:
                            gIBSMonoAdRem/gMonoPadrao).
                   Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB86c-10    55/65 Se informado o grupo gMonoPadrao do IBS Ad Rem (id: UB86, grupo:                     Obrig. 1221 Rejeição: Valor do IBS Monofásico Padrão Ad Rem
                   gIBSMonoAdRem/gMonoPadrao):                                                                      difere do calculado [nItem: 999]
                     - vIBSMono do IBS Ad Rem (id: UB86c, tag:
                       gIBSMonoAdRem/gMonoPadrao/vIBSMono) deve ser resultante de:
                        vIBSMono (id: UB86c) = qBCMono (id: UB86a) × adRemIBS (id: UB86b)
                   Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.

 Campo    Modelo                                   Regra de Validação                                 Aplic. Msg                     Descrição Erro
 UB87-10   55/65 Se informado o grupo gIBSMonoAdRem (id: UB85a):                                      Obrig. 1127 Rejeição: Não informada a Tributação Monofásica de
                  - Se cClassTrib possui indicador que exige Tributação Monofásica com Retenção                   Combustível com Retenção do IBS Ad Rem [nItem:
                    (ind_gMonoReten = 1):                                                                         999]
                     - Não informado o grupo gMonoReten do IBS Ad Rem (id: UB87, grupo:
                          gIBSMonoAdRem/gMonoReten)
                 Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB87-20   55/65 Se informado o grupo gIBSMonoAdRem (id: UB85a):                                      Obrig. 1128 Rejeição: Informada indevidamente a Tributação
                  - Se cClassTrib possui indicador que não permite Tributação Monofásica de                       Monofásica de Combustível com Retenção do IBS Ad
                    Combustível com Retenção (ind_gMonoReten = 0):                                                Rem [nItem: 999]
                     - Informado indevidamente o grupo gMonoReten do IBS Ad Rem (id: UB87, grupo:
                          gIBSMonoAdRem/gMonoReten)
                 Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB87c-10 55/65 Se informado o grupo gMonoReten do IBS Ad Rem (id: UB87, grupo:                       Obrig. 1222 Rejeição: Valor do IBS Monofásico Ad Rem com
                    gIBSMonoAdRem/gMonoReten)                                                                     Retenção difere do calculado [nItem: 999]
                  - vIBSMonoReten do IBS Ad Rem (id: UB87c, tag:
                    gIBSMonoAdRem/gMonoReten/vIBSMonoReten) deve ser resultante de:
                     vIBSMonoReten (id: UB87c) = qBCMonoReten (id: UB87a) × adRemIBSReten (id:
                           UB87b)
                 Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
 UB88-10   55/65 Se informado o grupo gIBSMonoAdRem (id: UB85a):                                      Obrig. 1108 Rejeição: Não informada a Tributação Monofásica
                  - Se cClassTrib possui indicador que exige Tributação Monofásica de Combustível                 Retida Anteriormente do IBS Ad Rem [nItem: 999]
                    cobrada anteriormente (ind_gMonoRet = 1):
                      - Não informado o grupo gMonoRet do IBS Ad Rem (id: UB88, grupo:
                          gIBSMonoAdRem/gMonoRet)
                 Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB88-20   55/65 Se informado o grupo gIBSMonoAdRem (id: UB85a):                                      Obrig. 1109 Rejeição: Informada indevidamente a Tributação
                  - Se cClassTrib possui indicador que não permite Tributação Monofásica de                       Monofásica Retida Anteriormente do IBS Ad Rem
                    Combustível cobrada anteriormente (ind_gMonoRet = 0):                                         [nItem: 999]
                       - Informado indevidamente o grupo gMonoRet do IBS Ad Rem (id: UB88, grupo:
                          gIBSMonoAdRem/gMonoRet)
                 Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.

  Campo Modelo                                      Regra de Validação                                  Aplic.   Msg                      Descrição Erro
 UB88a-10       Se informado o grupo gMonoRet do IBS Ad Rem (id: UB88, grupo:                           Obrig.   1223 Rejeição: Valor do IBS Monofásico Ad Rem retido
                gIBSMonoAdRem/gMonoRet):                                                                              anteriormente difere do calculado [nItem: 999]
                  - vIBSMonoRet do IBS Ad Rem (id: UB88a) deve ser resultante de:
                    - Se cProdANP igual a Gasolina C ou suas variações (cProdANP consta na lista
                    abaixo):
                        vIBSMonoRet = (qCombPetro × adRemIBSCombPetro) + (qBioComb ×
                        adRemIBSBioComb), onde:
                            qCombPetro = qTrib × (1 - pBio)
                            qBioComb = qTrib × (1 - pBio) × pBioObrig / (1 - pBioObrig).
                    - Se cProdANP diferente de Gasolina C e suas variações (cProdANP não consta na
                    lista abaixo):
                        vIBSMonoRet = qTrib × adRemIBS
                cProdANP Gasolina C = 320102001, 320102002, 320102003, 320102005, 320103001,
                    320103002, 320103003, 320301001, 320301002.
                Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                Observação 2: Consultar Tabela de Combustíveis Sujeitos à Tributação Monofásica do
                    IBS e CBS conforme produto (adRemIBSCombPetro, adRemIBSBioComb,
                    adRemIBS) (a ser publicada).
                Observação 3: Consultar Tabela de Código de Índice de Biocombustível do IBS e CBS
                    conforme produto (pBioObrig).
                Observação 4: Implementação Futura.
 UB89-10  55/65 Se informado o grupo gIBSMonoAdRem (id: UB85a):                                         Obrig.   1224 Rejeição: Não informado o grupo de informações
                  - Se cClassTrib possui indicador que exige o grupo de informações sobre mistura de                  sobre mistura de EAC com gasolina A em percentual
                    EAC com gasolina A em percentual inferior ou superior ao obrigatório                              inferior ou superior ao obrigatório do IBS Monofásico
                    (ind_gpBioDiferenca = 1):                                                                         Ad Rem [nItem: 999]
                      - Não informado o grupo gpBioDiferenca do IBS Ad Rem (id: UB89, grupo:
                          gIBSMonoAdRem/gpBioDiferenca)
                Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB89-20  55/65 Se informado o grupo gIBSMonoAdRem (id: UB85a):                                         Obrig.   1225 Rejeição: Informado indevidamente o grupo de
                  - Se cClassTrib possui indicador que não permite o grupo de informações sobre mistura               informações sobre mistura de EAC com gasolina A em
                    de EAC com gasolina A em percentual inferior ou superior ao obrigatório                           percentual inferior ou superior ao obrigatório do IBS
                    (ind_gpBioDiferenca = 0):                                                                         Monofásico Ad Rem [nItem: 999]
                       - Informado indevidamente o grupo gpBioDiferenca do IBS Ad Rem (id: UB89, grupo:
                          gIBSMonoAdRem/gpBioDiferenca)
                Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB89a-10 55/65 Se informado o grupo gpBioDiferenca do IBS Ad Rem (id: UB89, grupo:                     Obrig.   1226 Rejeição: Quantidade de Biocombustível (EAC) a
                    gIBSMonoAdRem/gpBioDiferenca):                                                                    recolher ou a ressarcir do IBS Monofásico Ad Rem
                  - qBCBioComb do IBS Ad Rem (id: UB89a) deve ser resultante de:                                      difere do calculado [nItem: 999]
                    - Se classTrib = 620004:
                        qBCBioComb = qTrib × (pBio - pBioObrig) / (1 - pBioObrig)
                    - Se classTrib = 620005:
                        qBCBioComb = qTrib × (pBioObrig - pBio) / (1 - pBioObrig)
                Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.

  Campo     Modelo                                    Regra de Validação                                 Aplic. Msg                      Descrição Erro
                    Observação 2: Consultar pBioObrig na tabela Índice de Mistura de Biocombustível
                        usando o cProdANP (id: LA02) do item.
 UB89b-10 55/65 Se informado o grupo gpBioDiferenca do IBS Ad Rem (id: UB89, grupo:                      Obrig. 1227 Rejeição: Valor do IBS Monofásico Ad Rem
                        gIBSMonoAdRem/gpBioDiferenca):                                                               correspondente a diferença em relação ao
                      - vIBSDiferenca do IBS Ad Rem (id: UB89b) deve ser resultante de:                              pBioObrigatorio difere do calculado [nItem: 999]
                        vIBSDiferenca = qBCBioComb (id: UB89a) × adRemIBSBioComb
                    Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                    Observação 2: Consultar Tabela de Combustíveis Sujeitos à Tributação Monofásica do
                        IBS e CBS conforme produto (a ser publicada).
*** Tributação Monofásica: IBS Ad Valorem
  UB90-10     55/65 Se informado o grupo de Tributação Monofásica do IBS e CBS (id: UB84, grupo:         Obrig. 1228 Rejeição: Tributação Monofásica Ad Valorem do IBS
                    gIBSCBSMono):                                                                                    informada indevidamente [nItem: 999]
                      - Se ano da data de emissão (id: B09, tag: dhEmi) maior que 2028:
                        - Informado indevidamente o grupo gIBSMonoAdValorem (id: UB90)                               Observação: Tributação Monofásica do IBS e CBS:
                                                                                                                               Ano        IBS           CBS
                                                                                                                                2026 AdValorem AdValorem
                                                                                                                                2027 AdValorem AdRem
                                                                                                                                2028 AdValorem AdRem
                                                                                                                                2029 AdRem          AdRem
 UB90-20     55/65 Se informado o grupo de Tributação Monofásica do IBS e CBS (id: UB84, grupo:          Obrig. 1229 Rejeição: Não informada Tributação Monofásica Ad
                   gIBSCBSMono):                                                                                     Valorem do IBS [nItem: 999]
                     - Se ano da data de emissão (id: B09, tag: dhEmi) menor ou igual a 2028:
                       - Se cClassTrib possui ind_gMonoPadrao=1 ou ind_gMonoReten=1 ou                                Observação: Vide tabela acima
                          ind_gMonoRet=1 ou ind_gpBioDiferenca=1:
                          - Não informado o grupo gIBSMonoAdValorem (id: UB90)
                   Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB91-10     55/65 Se informado o grupo gIBSMonoAdValorem (id: UB90):                                    Obrig. 1230 Rejeição: Não informada a Tributação Monofásica
                     - Se cClassTrib possui indicador que exige Tributação Monofásica Padrão de                      Padrão de Combustível do IBS Ad Valorem [nItem:
                       Combustível (ind_gMonoPadrao = 1):                                                            999]
                       - Não informado o grupo gMonoPadrao do IBS Ad Valorem (id: UB91, grupo:
                          gIBSMonoAdValorem/gMonoPadrao)
                   Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB91-20     55/65 Se informado o grupo gIBSMonoAdValorem (id: UB90):                                    Obrig. 1231 Rejeição: Informada indevidamente a Tributação
                     - Se cClassTrib possui indicador que não permite Tributação Monofásica Padrão de                Monofásica Padrão de Combustível do IBS Ad
                       Combustível (ind_gMonoPadrao = 0):                                                            Valorem [nItem: 999]
                        - Informado indevidamente o grupo gMonoPadrao do IBS Ad Valorem (id: UB91,
                            grupo: gIBSMonoAdValorem/gMonoPadrao)
                   Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB91c-10    55/65 Se informado o grupo gMonoPadrao do IBS Ad Valorem (id: UB91, grupo:                  Obrig. 1232 Rejeição: Valor do IBS Monofásico Padrão Ad
                   gIBSMonoAdValorem/gMonoPadrao):                                                                   Valorem Estadual difere do calculado [nItem: 999]
                     - vIBSMonoUF do IBS Ad Valorem (id: UB91c, tag:
                       gIBSMonoAdValorem/gMonoPadrao/vIBSMonoUF) deve ser resultante de:
                        vIBSMonoUF (id: UB91c) = qBCMono (id: UB91a) × pAliqMonoUF (id: UB91b)

  Campo     Modelo                                      Regra de Validação                                Aplic.   Msg                     Descrição Erro
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
 UB91e-10    55/65   Se informado o grupo gMonoPadrao do IBS Ad Valorem (id: UB91, grupo:                 Obrig.   1233 Rejeição: Valor do IBS Monofásico Padrão Ad
                     gIBSMonoAdValorem/gMonoPadrao):                                                                    Valorem Municipal difere do calculado [nItem: 999]
                       - vIBSMonoMun do IBS Ad Valorem (id: UB91e, tag:
                         gIBSMonoAdValorem/gMonoPadrao/vIBSMonoMun) deve ser resultante de:
                         vIBSMonoMun (id: UB91e) = qBCMono (id: UB91a) × pAliqMonoMun (id: UB91d)
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
 UB91f-10    55/65   Se informado o grupo gMonoPadrao do IBS Ad Valorem (id: UB91, grupo:                 Obrig.   1234 Rejeição: Valor do IBS Monofásico Padrão Ad
                     gIBSMonoAdValorem/gMonoPadrao):                                                                    Valorem difere do calculado [nItem: 999]
                       - vIBSMono do IBS Ad Valorem (id: UB91f, tag:
                         gIBSMonoAdValorem/gMonoPadrao/vIBSMono) deve ser resultante de:
                          vIBSMono (id: UB91f) = vIBSMonoUF (id: UB91c) + vIBSMonoMun (id: UB91e)
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
 UB92-10     55/65   Se informado o grupo gIBSMonoAdValorem (id: UB90):                                   Obrig.   1235 Rejeição: Não informada a Tributação Monofásica de
                       - Se cClassTrib possui indicador que exige Tributação Monofásica com Retenção                    Combustível com Retenção do IBS Ad Valorem
                         (ind_gMonoReten = 1):                                                                          [nItem: 999]
                         - Não informado o grupo gMonoReten do IBS Ad Valorem (id: UB92, grupo:
                              gIBSMonoAdValorem/gMonoReten)
                     Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB92-20     55/65   Se informado o grupo gIBSMonoAdValorem (id: UB90):                                   Obrig.   1236 Rejeição: Informada indevidamente a Tributação
                       - Se cClassTrib possui indicador que não permite Tributação Monofásica de                        Monofásica de Combustível com Retenção do IBS Ad
                         Combustível com Retenção (ind_gMonoReten = 0):                                                 Valorem [nItem: 999]
                         - Informado indevidamente o grupo gMonoReten do IBS Ad Valorem (id: UB92, grupo:
                              gIBSMonoAdValorem/gMonoReten)
                     Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB92c-10    55/65   Se informado o grupo gMonoReten do IBS Ad Valorem (id: UB92, grupo:                  Obrig.   1237 Rejeição: Valor do IBS Monofásico Ad Valorem com
                         gIBSMonoAdValorem/gMonoReten)                                                                  Retenção difere do calculado [nItem: 999]
                       - vIBSMonoReten do IBS Ad Valorem (id: UB92c, tag:
                         gIBSMonoAdValorem/gMonoReten/vIBSMonoReten) deve ser resultante de:
                          vIBSMonoReten (id: UB92c) = vBCMonoReten (id: UB92a) × pAliqMonoReten (id:
                               UB92b)
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
 UB93-10     55/65   Se informado o grupo gIBSMonoAdValorem (id: UB90):                                   Obrig.   1238 Rejeição: Não informada a Tributação Monofásica
                       - Se cClassTrib possui indicador que exige Tributação Monofásica de Combustível                  Retida Anteriormente do IBS Ad Valorem [nItem: 999]
                         cobrada anteriormente (ind_gMonoRet = 1):
                          - Não informado o grupo gMonoRet do IBS Ad Valorem (id: UB93, grupo:
                              gIBSMonoAdValorem/gMonoRet)
                     Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB93-20     55/65   Se informado o grupo gIBSMonoAdValorem (id: UB90):                                   Obrig.   1239 Rejeição: Informada indevidamente a Tributação
                       - Se cClassTrib possui indicador que não permite Tributação Monofásica de                        Monofásica Retida Anteriormente do IBS Ad Valorem
                         Combustível cobrada anteriormente (ind_gMonoRet = 0):                                          [nItem: 999]
                           - Informado indevidamente o grupo gMonoRet do IBS Ad Valorem (id: UB93, grupo:
                              gIBSMonoAdValorem/gMonoRet)
                     Observação 1: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.

  Campo Modelo                                      Regra de Validação                                    Aplic. Msg                      Descrição Erro
 UB93a-10       Se informado o grupo gMonoRet do IBS Ad Valorem (id: UB93, grupo:                         Obrig. 1240 Rejeição: Valor do IBS Monofásico Ad Valorem retido
                gIBSMonoAdValorem/gMonoRet):                                                                          anteriormente difere do calculado [nItem: 999]
                  - vIBSMonoRet do IBS Ad Valorem (id: UB93a) deve ser resultante de:
                    - Se cProdANP igual a Gasolina C ou suas variações (cProdANP consta na lista
                    abaixo):
                        vIBSMonoRet = (qCombPetro × vRefCombPetro × pAliqIBSCombPetro) +
                        (qBioComb × vRefBioComb × pAliqIBSBioComb), onde:
                            qCombPetro = qTrib × (1 - pBio)
                            qBioComb = qTrib × (1 - pBio) × pBioObrig / (1 - pBioObrig).
                    - Se cProdANP diferente de Gasolina C e suas variações (cProdANP não consta na
                    lista abaixo):
                        vIBSMonoRet = qTrib × pAliqIBS
                cProdANP Gasolina C = 320102001, 320102002, 320102003, 320102005, 320103001,
                    320103002, 320103003, 320301001, 320301002.
                Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                Observação 2: Consultar Tabela de Combustíveis Sujeitos à Tributação Monofásica do
                    IBS e CBS conforme produto (pAliqIBSCombPetro, pAliqIBSBioComb, pAliqIBS) (a
                    ser publicada).
                Observação 3: Consultar Tabela de Código de Índice de Biocombustível do IBS e CBS
                    conforme produto (pBioObrig).
                Observação 4: Consultar Tabela de Valores de Referência da Tributação Monofásica do
                    IBS e CBS conforme produto (vRefCombPetro e vRefBioComb) (a ser publicada).
                Observação 5: Implementação Futura.
 UB94-10  55/65 Se informado o grupo gIBSMonoAdValorem (id: UB90):                                        Obrig. 1241 Rejeição: Não informado o grupo de informações
                  - Se cClassTrib possui indicador que exige o grupo de informações sobre mistura de                  sobre mistura de EAC com gasolina A em percentual
                    EAC com gasolina A em percentual inferior ou superior ao obrigatório                              inferior ou superior ao obrigatório do IBS Monofásico
                    (ind_gpBioDiferenca = 1):                                                                         Ad Valorem [nItem: 999]
                      - Não informado o grupo gpBioDiferenca do IBS Ad Valorem (id: UB94, grupo:
                          gIBSMonoAdValorem/gpBioDiferenca)
                Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB94-20  55/65 Se informado o grupo gIBSMonoAdValorem (id: UB90):                                        Obrig. 1242 Rejeição: Informado indevidamente o grupo de
                  - Se cClassTrib possui indicador que não permite o grupo de informações sobre mistura               informações sobre mistura de EAC com gasolina A em
                    de EAC com gasolina A em percentual inferior ou superior ao obrigatório                           percentual inferior ou superior ao obrigatório do IBS
                    (ind_gpBioDiferenca = 0):                                                                         Monofásico Ad Valorem [nItem: 999]
                       - Informado indevidamente o grupo gpBioDiferenca do IBS Ad Valorem (id: UB94,
                          grupo: gIBSMonoAdValorem/gpBioDiferenca)
                Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.

   Campo Modelo                                       Regra de Validação                                  Aplic. Msg                      Descrição Erro
 UB94a-10 55/65 Se informado o grupo gpBioDiferenca do IBS Ad Valorem (id: UB94, grupo:                   Obrig. 1243 Rejeição: Quantidade de Biocombustível (EAC) a
                         gIBSMonoAdValorem/gpBioDiferenca):                                                           recolher ou a ressarcir do IBS Monofásico Ad Valorem
                      - qBCBioComb do IBS Ad Valorem (id: UB94a) deve ser resultante de:                              difere do calculado [nItem: 999]
                         - Se classTrib = 620004:
                            qBCBioComb = qTrib × (pBio - pBioObrig) / (1 - pBioObrig)
                        - Se classTrib = 620005:
                            qBCBioComb = qTrib × (pBioObrig - pBio) / (1 - pBioObrig)
                    Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                    Observação 2: Consultar pBioObrig na tabela Índice de Mistura de Biocombustível
                         usando o cProdANP (id: LA02) do item.
 UB94b-10 55/65 Se informado o grupo gpBioDiferenca do IBS Ad Valorem (id: UB94, grupo:                   Obrig. 1244 Rejeição: Valor do IBS Monofásico Ad Valorem
                         gIBSMonoAdValorem/gpBioDiferenca):                                                           correspondente a diferença em relação ao
                      - vIBSDiferenca do IBS Ad Valorem (id:UB94b) deve ser resultante de:                            pBioObrigatorio difere do calculado [nItem: 999]
                         vIBSDiferenca = qBCBioComb (id: UB94a) × vRefBioComb × pAliqIBSBioComb
                    Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                    Observação 2: Consultar Tabela de Combustíveis Sujeitos à Tributação Monofásica do
                         IBS e CBS conforme produto (a ser publicada).
                    Observação 3: Consultar Tabela de Valores de Referência da Tributação Monofásica do
                         IBS e CBS conforme produto (vRefBioComb) (a ser publicada).
                    Observação 4: Implementação Futura.
*** Tributação Monofásica: CBS Ad Rem
 UB95a-10 55/65 Se informado o grupo de Tributação Monofásica do IBS e CBS (id: UB84, grupo:              Obrig. 1245 Rejeição: Tributação Monofásica Ad Rem da CBS
                    gIBSCBSMono):                                                                                     informada indevidamente [nItem: 999]
                      - Se ano da data de emissão (id: B09, tag: dhEmi) menor ou igual a 2026:
                         - Informado indevidamente o grupo gCBSMonoAdRem (id: UB95a)                                  Observação: Tributação Monofásica do IBS e CBS:
                    Exceção: Essa regra não se aplica para a CBS no ambiente de Homologação.                                    Ano        IBS           CBS
                                                                                                                                 2026 AdValorem AdValorem
                                                                                                                                 2027 AdValorem AdRem
                                                                                                                                 2028 AdValorem AdRem
                                                                                                                                 2029 AdRem          AdRem
 UB95a-20    55/65 Se informado o grupo de Tributação Monofásica do IBS e CBS (id: UB84, grupo:           Obrig. 1246 Rejeição: Não informada Tributação Monofásica Ad
                   gIBSCBSMono):                                                                                      Rem da CBS [nItem: 999]
                     - Se ano da data de emissão (id: B09, tag: dhEmi) maior que 2026:
                       - Se cClassTrib possui ind_gMonoPadrao=1 ou ind_gMonoReten=1 ou                                 Observação: Vide tabela acima
                          ind_gMonoRet=1 ou ind_gpBioDiferenca=1:
                         - Não informado o grupo gCBSMonoAdRem (id: UB95a)
                   Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB96-10     55/65 Se informado o grupo gCBSMonoAdRem (id: UB95a):                                        Obrig. 1247 Rejeição: Não informada a Tributação Monofásica
                     - Se cClassTrib possui indicador que exige Tributação Monofásica Padrão de                       Padrão de Combustível da CBS Ad Rem [nItem: 999]
                       Combustível (ind_gMonoPadrao = 1):
                       - Não informado o grupo gMonoPadrao da CBS Ad Rem (id: UB96, grupo:
                       gCBSMonoAdRem/gMonoPadrao)
                   Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.

 Campo    Modelo                                   Regra de Validação                                 Aplic. Msg                    Descrição Erro
 UB96-20   55/65 Se informado o grupo gCBSMonoAdRem (id: UB95a):                                      Obrig. 1248 Rejeição: Informada indevidamente a Tributação
                  - Se cClassTrib possui indicador que não permite Tributação Monofásica Padrão de                Monofásica Padrão de Combustível da CBS Ad Rem
                    Combustível (ind_gMonoPadrao = 0):                                                            [nItem: 999]
                      - Informado indevidamente o grupo gMonoPadrao da CBS Ad Rem (id: UB96, grupo:
                          gCBSMonoAdRem/gMonoPadrao).
                 Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB96c-10 55/65 Se informado o grupo gMonoPadrao da CBS Ad Rem (id: UB96, grupo:                      Obrig. 1249 Rejeição: Valor da CBS Monofásica Padrão Ad Rem
                 gCBSMonoAdRem/gMonoPadrao):                                                                      difere do calculado [nItem: 999]
                  - vCBSMono da CBS Ad Rem (id: UB96c, tag:
                    gCBSMonoAdRem/gMonoPadrao/vCBSMono) deve ser resultante de:
                     vCBSMono (id: UB96c) = qBCMono (id: UB96a) × adRemCBS (id: UB96b)
                 Observação: Aceitar uma tolerância de 0,01 a mais ou a menos.
 UB97-10   55/65 Se informado o grupo gCBSMonoAdRem (id: UB95a):                                      Obrig. 1250 Rejeição: Não informada a Tributação Monofásica de
                  - Se cClassTrib possui indicador que exige Tributação Monofásica com Retenção                   Combustível com Retenção da CBS Ad Rem [nItem:
                    (ind_gMonoReten = 1):                                                                         999]
                     - Não informado o grupo gMonoReten da CBS Ad Rem (id: UB97, grupo:
                          gCBSMonoAdRem/gMonoReten)
                 Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB97-20   55/65 Se informado o grupo gCBSMonoAdRem (id: UB95a):                                      Obrig. 1251 Rejeição: Informada indevidamente a Tributação
                  - Se cClassTrib possui indicador que não permite Tributação Monofásica de                       Monofásica de Combustível com Retenção da CBS Ad
                    Combustível com Retenção (ind_gMonoReten = 0):                                                Rem [nItem: 999]
                     - Informado indevidamente o grupo gMonoReten da CBS Ad Rem (id: UB97, grupo:
                          gCBSMonoAdRem/gMonoReten)
                 Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB97c-10 55/65 Se informado o grupo gMonoReten da CBS Ad Rem (id: UB97, grupo:                       Obrig. 1252 Rejeição: Valor da CBS Monofásica Ad Rem com
                    gCBSMonoAdRem/gMonoReten)                                                                     Retenção difere do calculado [nItem: 999]
                  - vCBSMonoReten da CBS Ad Rem (id: UB97c, tag:
                    gCBSMonoAdRem/gMonoReten/vCBSMonoReten) deve ser resultante de:
                     vCBSMonoReten (id: UB97c) = qBCMonoReten (id: UB97a) × adRemCBSReten (id:
                           UB97b)
                 Observação : Aceitar uma tolerância de 0,01 a mais ou a menos.
 UB98-10   55/65 Se informado o grupo gCBSMonoAdRem (id: UB95a):                                      Obrig. 1253 Rejeição: Não informada a Tributação Monofásica
                  - Se cClassTrib possui indicador que exige Tributação Monofásica de Combustível                 Retida Anteriormente da CBS Ad Rem [nItem: 999]
                    cobrada anteriormente (ind_gMonoRet = 1):
                      - Não informado o grupo gMonoRet da CBS Ad Rem (id: UB98, grupo:
                          gCBSMonoAdRem/gMonoRet)
                 Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB98-20   55/65 Se informado o grupo gCBSMonoAdRem (id: UB95a):                                      Obrig. 1254 Rejeição: Informada indevidamente a Tributação
                  - Se cClassTrib possui indicador que não permite Tributação Monofásica de                       Monofásica Retida Anteriormente da CBS Ad Rem
                    Combustível cobrada anteriormente (ind_gMonoRet = 0):                                         [nItem: 999]
                       - Informado indevidamente o grupo gMonoRet da CBS Ad Rem (id: UB98, grupo:
                          gCBSMonoAdRem/gMonoRet)
                 Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.

  Campo Modelo                                     Regra de Validação                                    Aplic. Msg                     Descrição Erro
 UB98a-10       Se informado o grupo gMonoRet da CBS Ad Rem (id: UB98, grupo:                            Obrig. 1255 Rejeição: Valor da CBS Monofásica Ad Rem retido
                gCBSMonoAdRem/gMonoRet):                                                                             anteriormente difere do calculado [nItem: 999]
                 - vCBSMonoRet da CBS Ad Rem (id: UB98a) deve ser resultante de:
                    - Se cProdANP igual a Gasolina C ou suas variações (cProdANP consta na lista
                   abaixo):
                       vCBSMonoRet = (qCombPetro × adRemCBSCombPetro) + (qBioComb ×
                       adRemCBSBioComb), onde:
                           qCombPetro = qTrib × (1 - pBio)
                           qBioComb = qTrib × (1 - pBio) × pBioObrig / (1 - pBioObrig).
                    - Se cProdANP diferente de Gasolina C e suas variações (cProdANP não consta na
                   lista abaixo):
                       vCBSMonoRet = qTrib × adRemCBS
                cProdANP Gasolina C = 320102001, 320102002, 320102003, 320102005, 320103001,
                   320103002, 320103003, 320301001, 320301002.
                Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                Observação 2: Consultar Tabela de Combustíveis Sujeitos à Tributação Monofásica do
                   IBS e CBS conforme produto (adRemCBSCombPetro, adRemCBSBioComb,
                   adRemCBS) (a ser publicada).
                Observação 3: Consultar Tabela de Código de Índice de Biocombustível do IBS e CBS
                   conforme produto (pBioObrig).
                Observação 4: Implementação Futura.
 UB99-10  55/65 Se informado o grupo gCBSMonoAdRem (id: UB95a):                                          Obrig. 1148 Rejeição: Não informado o grupo de informações
                 - Se cClassTrib possui indicador que exige o grupo de informações sobre mistura de                  sobre mistura de EAC com gasolina A em percentual
                   EAC com gasolina A em percentual inferior ou superior ao obrigatório                              inferior ou superior ao obrigatório da CBS Monofásica
                   (ind_gpBioDiferenca = 1):                                                                         Ad Rem [nItem: 999]
                     - Não informado o grupo gpBioDiferenca da CBS Ad Rem (id: UB99, grupo:
                         gCBSMonoAdRem/gpBioDiferenca)
                Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB99-20  55/65 Se informado o grupo gCBSMonoAdRem (id: UB95a):                                          Obrig. 1149 Rejeição: Informado indevidamente o grupo de
                 - Se cClassTrib possui indicador que não permite o grupo de informações sobre mistura               informações sobre mistura de EAC com gasolina A em
                   de EAC com gasolina A em percentual inferior ou superior ao obrigatório                           percentual inferior ou superior ao obrigatório da CBS
                   (ind_gpBioDiferenca = 0):                                                                         Monofásica Ad Rem [nItem: 999]
                      - Informado indevidamente o grupo gpBioDiferenca da CBS Ad Rem (id: UB99,
                         grupo: gCBSMonoAdRem/gpBioDiferenca)
                Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB99a-10 55/65 Se informado o grupo gpBioDiferenca da CBS Ad Rem (id: UB99, grupo:                      Obrig. 1256 Rejeição: Quantidade de Biocombustível (EAC) a
                   gCBSMonoAdRem/gpBioDiferenca):                                                                    recolher ou a ressarcir da CBS Monofásica Ad Rem
                 - qBCBioComb da CBS Ad Rem (id: UB99a) deve ser resultante de:                                      difere do calculado [nItem: 999]
                    - Se classTrib = 620004:
                       qBCBioComb = qTrib × (pBio - pBioObrig) / (1 - pBioObrig)
                    - Se classTrib = 620005:
                       qBCBioComb = qTrib × (pBioObrig - pBio) / (1 - pBioObrig)
                Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.

  Campo     Modelo                                    Regra de Validação                                 Aplic. Msg                      Descrição Erro
                    Observação 2: Consultar pBioObrig na tabela Índice de Mistura de Biocombustível
                        usando o cProdANP (id: LA02) do item.
 UB99b-10 55/65 Se informado o grupo gpBioDiferenca da CBS Ad Rem (id: UB99, grupo:                      Obrig. 1257 Rejeição: Valor da CBS Monofásica Ad Rem
                        gCBSMonoAdRem/gpBioDiferenca):                                                               correspondente a diferença em relação ao
                      - vCBSDiferenca da CBS Ad Rem (id: UB99b) deve ser resultante de:                              pBioObrigatorio difere do calculado [nItem: 999]
                        vCBSDiferenca = qBCBioComb (id: UB99a) × adRemCBSBioComb
                    Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                    Observação 2: Consultar Tabela de Combustíveis Sujeitos à Tributação Monofásica do
                        IBS e CBS conforme produto (a ser publicada).
*** Tributação Monofásica: CBS Ad Valorem
 UB100-10 55/65 Se informado o grupo de Tributação Monofásica do IBS e CBS (id: UB84, grupo:             Obrig. 1258 Rejeição: Tributação Monofásica Ad Valorem da CBS
                    gIBSCBSMono):                                                                                    informada indevidamente [nItem: 999]
                      - Se ano da data de emissão (id: B09, tag: dhEmi) maior que 2026:
                        - Informado indevidamente o grupo gCBSMonoAdValorem (id: UB100)                              Observação: Tributação Monofásica do IBS e CBS:
                                                                                                                               Ano        IBS           CBS
                                                                                                                                2026 AdValorem AdValorem
                                                                                                                                2027 AdValorem AdRem
                                                                                                                                2028 AdValorem AdRem
                                                                                                                                2029 AdRem          AdRem
 UB100-20    55/65 Se informado o grupo de Tributação Monofásica do IBS e CBS (id: UB84, grupo:          Obrig. 1259 Rejeição: Não informada Tributação Monofásica Ad
                   gIBSCBSMono):                                                                                     Valorem da CBS [nItem: 999]
                     - Se ano da data de emissão (id: B09, tag: dhEmi) menor ou igual a 2026:
                       - Se cClassTrib possui ind_gMonoPadrao=1 ou ind_gMonoReten=1 ou                                Observação: Vide tabela acima
                          ind_gMonoRet=1 ou ind_gpBioDiferenca=1:
                          - Não informado o grupo gCBSMonoAdValorem (id: UB100)
                   Exceção: Essa regra não se aplica para a CBS no ambiente de Homologação caso o
                       grupo gCBSMonoAdRem (id: UB95a) esteja informado.
                   Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB101-10    55/65 Se informado o grupo gCBSMonoAdValorem (id: UB100):                                   Obrig. 1260 Rejeição: Não informada a Tributação Monofásica
                     - Se cClassTrib possui indicador que exige Tributação Monofásica Padrão de                      Padrão de Combustível da CBS Ad Valorem [nItem:
                       Combustível (ind_gMonoPadrao = 1):                                                            999]
                       - Não informado o grupo gMonoPadrao da CBS Ad Valorem (id: UB101, grupo:
                          gCBSMonoAdValorem/gMonoPadrao)
                   Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB101-20    55/65 Se informado o grupo gCBSMonoAdValorem (id: UB100):                                   Obrig. 1261 Rejeição: Informada indevidamente a Tributação
                     - Se cClassTrib possui indicador que não permite Tributação Monofásica Padrão de                Monofásica Padrão de Combustível da CBS Ad
                       Combustível (ind_gMonoPadrao = 0):                                                            Valorem [nItem: 999]
                        - Informado indevidamente o grupo gMonoPadrao da CBS Ad Valorem (id: UB101,
                            grupo: gCBSMonoAdValorem/gMonoPadrao)
                   Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
UB101c-10    55/65 Se informado o grupo gMonoPadrao da CBS Ad Valorem (id: UB101, grupo:                 Obrig. 1262 Rejeição: Valor da CBS Monofásica Padrão Ad
                   gCBSMonoAdValorem/gMonoPadrao):                                                                   Valorem difere do calculado [nItem: 999]

  Campo     Modelo                                      Regra de Validação                              Aplic. Msg                    Descrição Erro
                      - vCBSMono da CBS Ad Valorem (id: UB101c, tag:
                        gCBSMonoAdValorem/gMonoPadrao/vCBSMono) deve ser resultante de:
                         vCBSMono (id: UB101c) = vBCMono (id: UB101a) × pAliqMono (id: UB101b)
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
 UB102-10    55/65   Se informado o grupo gCBSMonoAdValorem (id: UB100):                                Obrig. 1263 Rejeição: Não informada a Tributação Monofásica de
                      - Se cClassTrib possui indicador que exige Tributação Monofásica com Retenção                 Combustível com Retenção da CBS Ad Valorem
                        (ind_gMonoReten = 1):                                                                       [nItem: 999]
                         - Não informado o grupo gMonoReten da CBS Ad Valorem (id: UB102, grupo:
                              gCBSMonoAdValorem/gMonoReten)
                     Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB102-20    55/65   Se informado o grupo gCBSMonoAdValorem (id: UB100):                                Obrig. 1264 Rejeição: Informada indevidamente a Tributação
                      - Se cClassTrib possui indicador que não permite Tributação Monofásica de                     Monofásica de Combustível com Retenção da CBS Ad
                        Combustível com Retenção (ind_gMonoReten = 0):                                              Valorem [nItem: 999]
                         - Informado indevidamente o grupo gMonoReten da CBS Ad Valorem (id: UB102,
                              grupo: gCBSMonoAdValorem/gMonoReten)
                     Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
UB102c-10    55/65   Se informado o grupo gMonoReten da CBS Ad Valorem (id: UB102, grupo:               Obrig. 1265 Rejeição: Valor da CBS Monofásica Ad Valorem com
                        gCBSMonoAdValorem/gMonoReten)                                                               Retenção difere do calculado [nItem: 999]
                      - vCBSMonoReten da CBS Ad Valorem (id: UB102c, tag:
                        gCBSMonoAdValorem/gMonoReten/vCBSMonoReten) deve ser resultante de:
                         vCBSMonoReten (id: UB102c) = vBCMonoReten (id: UB102a) × pAliqMonoReten (id:
                               UB102b)
                     Observação: Aceitar uma tolerância de 0,01 a mais ou a menos.
 UB103-10    55/65   Se informado o grupo gCBSMonoAdValorem (id: UB100):                                Obrig. 1266 Rejeição: Não informada a Tributação Monofásica
                      - Se cClassTrib possui indicador que exige Tributação Monofásica de Combustível               Retida Anteriormente da CBS Ad Valorem [nItem: 999]
                        cobrada anteriormente (ind_gMonoRet = 1):
                          - Não informado o grupo gMonoRet da CBS Ad Valorem (id: UB103, grupo:
                              gCBSMonoAdValorem/gMonoRet)
                     Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB103-20    55/65   Se informado o grupo gCBSMonoAdValorem (id: UB100):                                Obrig. 1267 Rejeição: Informada indevidamente a Tributação
                      - Se cClassTrib possui indicador que não permite Tributação Monofásica de                     Monofásica Retida Anteriormente da CBS Ad Valorem
                        Combustível cobrada anteriormente (ind_gMonoRet = 0):                                       [nItem: 999]
                           - Informado indevidamente o grupo gMonoRet da CBS Ad Valorem (id: UB103,
                              grupo: gCBSMonoAdValorem/gMonoRet)
                     Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
UB103a-10            Se informado o grupo gMonoRet da CBS Ad Valorem (id: UB103, grupo:                 Obrig. 1268 Rejeição: Valor da CBS Monofásica Ad Valorem retido
                     gCBSMonoAdValorem/gMonoRet):                                                                   anteriormente difere do calculado [nItem: 999]
                      - vCBSMonoRet da CBS Ad Valorem (id: UB103a) deve ser resultante de:
                         - Se cProdANP igual a Gasolina C ou suas variações (cProdANP consta na lista
                        abaixo):
                            vCBSMonoRet = (qCombPetro × vRefCombPetro × pAliqCBSCombPetro) +
                            (qBioComb × vRefBioComb × pAliqCBSBioComb), onde:
                                qCombPetro = qTrib × (1 - pBio)
                                qBioComb = qTrib × (1 - pBio) × pBioObrig / (1 - pBioObrig).

  Campo     Modelo                                      Regra de Validação                                    Aplic. Msg                      Descrição Erro
                         - Se cProdANP diferente de Gasolina C e suas variações (cProdANP não consta na
                         lista abaixo):
                             vCBSMonoRet = qTrib × pAliqCBS
                     cProdANP Gasolina C = 320102001, 320102002, 320102003, 320102005, 320103001,
                         320103002, 320103003, 320301001, 320301002.
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                     Observação 2: Consultar Tabela de Combustíveis Sujeitos à Tributação Monofásica do
                         IBS e CBS conforme produto (pAliqCBSCombPetro, pAliqCBSBioComb, pAliqCBS) (a
                         ser publicada).
                     Observação 3: Consultar Tabela de Código de Índice de Biocombustível do IBS e CBS
                         conforme produto (pBioObrig).
                     Observação 4: Consultar Tabela de Valores de Referência da Tributação Monofásica do
                         IBS e CBS conforme produto (vRefCombPetro e vRefBioComb) (a ser publicada).
                     Observação 5: Implementação Futura.
 UB104-10    55/65   Se informado o grupo gCBSMonoAdValorem (id: UB100):                                      Obrig. 1269 Rejeição: Não informado o grupo de informações
                      - Se cClassTrib possui indicador que exige o grupo de informações sobre mistura de                  sobre mistura de EAC com gasolina A em percentual
                         EAC com gasolina A em percentual inferior ou superior ao obrigatório                             inferior ou superior ao obrigatório da CBS Monofásica
                         (ind_gpBioDiferenca = 1):                                                                        Ad Valorem [nItem: 999]
                           - Não informado o grupo gpBioDiferenca da CBS Ad Valorem (id: UB104, grupo:
                               gCBSMonoAdValorem/gpBioDiferenca)
                     Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
 UB104-20    55/65   Se informado o grupo gCBSMonoAdValorem (id: UB100):                                      Obrig. 1270 Rejeição: Informado indevidamente o grupo de
                      - Se cClassTrib possui indicador que não permite o grupo de informações sobre mistura               informações sobre mistura de EAC com gasolina A em
                         de EAC com gasolina A em percentual inferior ou superior ao obrigatório                          percentual inferior ou superior ao obrigatório da CBS
                         (ind_gpBioDiferenca = 0):                                                                        Monofásica Ad Valorem [nItem: 999]
                            - Informado indevidamente o grupo gpBioDiferenca da CBS Ad Valorem (id: UB104,
                               grupo: gCBSMonoAdValorem/gpBioDiferenca)
                     Observação: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
UB104a-10    55/65   Se informado o grupo gpBioDiferenca da CBS Ad Valorem (id: UB104, grupo:                 Obrig. 1271 Rejeição: Quantidade de Biocombustível (EAC) a
                         gCBSMonoAdValorem/gpBioDiferenca):                                                               recolher ou a ressarcir da CBS Monofásica Ad
                      - qBCBioComb da CBS Ad Valorem (id: UB104a) deve ser resultante de:                                 Valorem difere do calculado [nItem: 999]
                         - Se classTrib = 620004:
                             qBCBioComb = qTrib × (pBio - pBioObrig) / (1 - pBioObrig)
                        - Se classTrib = 620005:
                             qBCBioComb = qTrib × (pBioObrig - pBio) / (1 - pBioObrig)
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.
                     Observação 2: Consultar pBioObrig na tabela Índice de Mistura de Biocombustível
                         usando o cProdANP (id: LA02) do item.
UB104b-10    55/65   Se informado o grupo gpBioDiferenca da CBS Ad Valorem (id: UB104, grupo:                 Obrig. 1272 Rejeição: Valor da CBS Monofásica Ad Valorem
                         gCBSMonoAdValorem/gpBioDiferenca):                                                               correspondente a diferença em relação ao
                      - vCBSDiferenca da CBS Ad Valorem (id:UB104b) deve ser resultante de:                               pBioObrigatorio difere do calculado [nItem: 999]
                         vCBSDiferenca = qBCBioComb (id: UB104a) × vRefBioComb × pAliqCBSBioComb
                     Observação 1: Aceitar uma tolerância de 0,01 a mais ou a menos.

  Campo     Modelo                                      Regra de Validação                                  Aplic.   Msg                     Descrição Erro
                    Observação 2: Consultar Tabela de Combustíveis Sujeitos à Tributação Monofásica do
                         IBS e CBS conforme produto (a ser publicada).
                    Observação 3: Consultar Tabela de Valores de Referência da Tributação Monofásica do
                         IBS e CBS conforme produto (vRefBioComb) (a ser publicada).
                    Observação 4: Implementação Futura.
*** Tributação Monofásica: Totais
UB105a-10 55/65 Se informado grupo do IBS e CBS monofásico (grupo: gIBSCBSMono):                            Obrig.   1070 Rejeição: Valor do IBS monofásico difere do calculado
                       - Valor total do IBS Monofásico do item (tag: vTotIBSMonoItem) deverá ser resultante               [nItem: 999]
                         de:
                          vTotIBSMonoItem = vIBSMono + vIBSMonoReten
                    Observação 01: Aceitar uma tolerância de 0,01 a mais ou a menos.
                    Observação 02: Implementação futura.
UB105b-10 55/65 Se informado grupo do IBS e CBS monofásico (grupo: gIBSCBSMono):                            Obrig.   1071 Rejeição: Valor da CBS monofásico difere do
                       - O valor total da CBS Monofásica do item (tag: vTotCBSMonoItem) deverá ser                        calculado [nItem: 999]
                         resultante de:
                          vTotCBSMonoItem = vCBSMono + vCBSMonoReten
                    Observação 01: Aceitar uma tolerância de 0,01 a mais ou a menos.
                    Observação 02: Implementação futura.
*** Tributação Monofásica: Fim
 UB106-30      55   Se informado grupo IBSCBS\gTransfCred:                                                  Obrig    1133 Rejeição: Finalidade de Emissão da Nota Fiscal
                       - finNFe <> 6-Nota de Débito                                                                       incompatível com o CST [nItem: 999]
 UB106-31      55   Se informado grupo IBSCBS\gTransfCred:                                                  Obrig    1168 Rejeição: Tipo de Nota de Débito incompatível com o
                       - tpNFDebito <> ”05-Transferência de crédito de sucessão” e tpNFDebito <> “01-                     CST [nItem: 999]
                         Transferência de créditos para Cooperativas”
 UB106-40      55   Se informado grupo IBSCBS\gTransfCred:                                                  Obrig.   1129 Rejeição: Valor do IBS ou da CBS deve ser maior que
                      - O valor do IBS (tag: gTransfCred\vIBS) ou da CBS (tag: gTransfCred\vCBS) deve ser                 zero na transferência de crédito. [nItem: 999]
                         maior que 0.
 UB112-10 55/65 Se CST possui indicador que veda o preenchimento do grupo de ajuste de competência Obrig.            1169 Rejeição: Grupo de Ajuste de Competência informado
                    (ind_gAjusteCompet = 0):                                                                              indevidamente [nItem: 999]
                       - Grupo “gAjusteCompet” (id: UB112) informado indevidamente
                    Observação: Consultar tabela de CST.
 UB112-20      55   Se CST possui indicador que obriga o preenchimento do grupo de ajuste de competência: Obrig.     1170 Rejeição: Grupo de Ajuste de Competência não
                    (ind_gAjusteCompet = 1):                                                                              informado [nItem: 999]
                       - Não informado grupo “gAjusteCompet” (id: UB112)
                    Observação: Consultar tabela de CST.
 UB112-30      55   Se informado grupo “gAjusteCompet” (id: UB112):                                         Obrig.   1171 Rejeição: Valor do IBS ou da CBS deve ser maior que
                       - Valor do IBS (gAjusteCompet/vIBS, id: UB114) ou Valor da CBS (gAjusteCompet/vCBS,                zero no ajuste de competência [nItem: 999]
                         id: UB115) deve ser maior que zero.
 UB116-10 55/65 Se cClassTrib possui indicador que veda o preenchimento do grupo de informações do Obrig.            1172 Rejeição: Grupo de Estorno de Crédito informado
                    estorno de crédito (ind_gEstornoCred = 0):                                                            indevidamente [nItem: 999]
                       - Grupo “gEstornoCred” (id: 116) informado indevidamente
                    Exceção: Esta RV não se aplica no caso de tpNFDebito=07-Perda em estoque.
                    Observação: Consultar tabela de cClassTrib.

  Campo Modelo                                     Regra de Validação                                 Aplic.   Msg                    Descrição Erro
 UB116-20 55   Se cClassTrib possui indicador que obriga o preenchimento do grupo de informações do Obrig.     1173 Rejeição: Grupo de Estorno de Crédito não informado
               estorno de crédito (ind_gEstornoCred = 1), ou tpNFDebito=07-Perda em estoque:                        [nItem: 999]
                  - Não informado grupo “gEstornoCred” (id: 116)
               Observação: Consultar tabela de cClassTrib.
 UB116-30 55   Se informado grupo “gEstornoCred” (id: 116):                                           Obrig.   1174 Rejeição: Valor do IBS ou da CBS deve ser maior que
                  - Valor do IBS (gEstornoCred /vIBS, id: UB117) ou Valor da CBS (gEstornoCred/vCBS,                zero no estorno de crédito [nItem: 999]
                    id: UB118) deve ser maior que zero.
               Exceção: Esta RV não se aplica no caso de tpNFDebito=07-Perda em estoque.
 UB120-10 65   Se informado grupo de Crédito Presumido da Operação (tag: IBSCBS/gCredPresOper):       Obrig.   1049 Rejeição: Não é permitido o uso de Crédito Presumido
                  - Modelo DFe = 65-NFCe                                                                            na NFC-e modelo 65 [nItem: 999]
 UB120-20 55   Se cClassTrib possui indicador que não permite o uso de crédito presumido na operação Obrig.    1175 Rejeição: Grupo de Crédito Presumido na Operação
               (ind_gCredPresOper = 0):                                                                             informado indevidamente [nItem: 999]
                  - Crédito presumido na operação informado indevidamente (grupo:
                    IBSCBS/gCredPresOper)
               Exceção: Essa regra não se aplica no fornecimento de bem móvel usado (tag:
                    indBemMovelUsado=1).
               Observação 01: Consultar Tabela de Código de Classificação Tributária do IBS e CBS.
               Observação 02: O valor "1" do indicador ind_gCredPresOper significa que o contribuinte
               pode utilizar o crédito presumido, sem obrigatoriedade (permite, mas não exige).
 UB122-10 55   Se informado cCredPres da operação (tag: IBSCBS/gCredPresOper/cCredPres, id:           Obrig.   1055 Rejeição: Código de Crédito Presumido (cCredPres)
               UB122):                                                                                              da Operação inexistente [nItem: 999]
                  - cCredPres inexistente
               Observação: Consultar tabela de Crédito Presumido do IBS e da CBS.
 UB123-10 55   Se cCredPres (id: UB122) possui indicador que não permite o uso de crédito presumido   Obrig.   1053 Rejeição: Crédito Presumido para o IBS informado
               para o IBS (ind_gIBSCredPres = 0):                                                                   indevidamente [nItem: 999]
                  - Crédito presumido para o IBS informado indevidamente (grupo:
                    IBSCBS/gCredPresOper/gIBSCredPres)
               Observação 01: Consultar Tabela de Crédito Presumido do IBS e da CBS.
 UB123-20 55   Se cCredPres (id: UB122) possui indicador que exige o uso de crédito presumido para o Obrig.    1054 Rejeição: Crédito Presumido para o IBS não
               IBS (ind_gIBSCredPres = 1):                                                                          informado [nItem: 999]
                  - Crédito presumido para o IBS não informado (grupo:
                    IBSCBS/gCredPresOper/gIBSCredPres)
               Observação 01: Consultar Tabela de Crédito Presumido do IBS e da CBS.
 UB125-10 55   Se informado Valor do Crédito Presumido do IBS (tag: gIBSCredPres/vCredPres) e         Obrig.   1107 Rejeição: Valor do Crédito Presumido do IBS não
               cCredPres = “4-Aquisição de bens móveis de PF não contrib. para revenda (exemplo:                    pode ser superior a vProd [nItem: 999]
               veículos / brechó):
                  - Valor do Crédito Presumido (tag: vCredPres) não pode ser superior a vProd
 UB126-10 55   Se informado Valor do Crédito Presumido em condição suspensiva                         Obrig.   1056 Rejeição: Valor do Crédito Presumido em condição
               (tag:gIBSCredPres/vCredPresCondSus):                                                                 suspensiva do IBS informado indevidamente [nItem:
                  - Ano de emissão < 2033; ou                                                                       999]
                  - Código de classificação do crédito presumido (tag: gIBSCredPres/cCredPres) <> “4-
                    Aquisição de bens móveis de PF não contrib. para revenda (exemplo: veículos /
                    brechó)”
               Observação: Somente deverá ser informado a partir de 2033.

  Campo Modelo                                     Regra de Validação                                         Aplic. Msg                     Descrição Erro
 UB127-10 55   Se cCredPres (id: UB122) possui indicador que não permite o uso de crédito presumido           Obrig. 1050 Rejeição: Crédito Presumido para a CBS informado
               para a CBS (ind_gCBSCredPres = 0):                                                                         indevidamente [nItem: 999]
                  - Crédito presumido para a CBS informado indevidamente (grupo:
                    IBSCBS/gCredPresOper/gCBSCredPres)
               Observação 01: Consultar Tabela de Crédito Presumido do IBS e da CBS.
 UB127-20 55   Se cCredPres (id: UB122) possui indicador que exige o uso de crédito presumido para a          Obrig. 1058 Rejeição: Crédito Presumido para a CBS não
               CBS (ind_gCBSCredPres = 1):                                                                                informado [nItem: 999]
                  - Crédito presumido para a CBS não informado (grupo:
                    IBSCBS/gCredPresOper/gCBSCredPres)
               Observação 01: Consultar Tabela de Crédito Presumido do IBS e da CBS.
 UB129-10 55   Se informado Valor do Crédito Presumido da CBS (tag: gCBSCredPres/vCredPres) e                 Obrig. 1124 Rejeição: Valor do Crédito Presumido da CBS não
               cCredPres = “4-Aquisição de bens móveis de PF não contrib. para revenda (exemplo:                          pode ser superior a vProd [nItem: 999]
               veículos / brechó):
                  - Valor do Crédito Presumido (tag: vCredPres) não pode ser superior a vProd
 UB130-10 55   Se informado Valor do Crédito Presumido em condição suspensiva (tag:                           Obrig. 1060 Rejeição:   Valor do Crédito Presumido da CBS
               gCBSCredPres/vCredPresCondSus):                                                                            informado indevidamente [nItem: 999]
                  - Ano de emissão < 2027; ou
                  - Código de classificação do crédito presumido (tag: gCBSCredPres/cCredPres) <> “4-
                    Aquisição de bens móveis de PF não contrib. para revenda (veículos / brechó)”
               Observação: Somente deverá ser informado a partir de 2027.
 UB131-10 65   Se informado grupo do IBS da ZFM (grupo: gCredPresIBSZFM):                                         Obrig. 1138 Rejeição: Não é permitido o uso de Crédito Presumido
                  - Modelo DFe = 65-NFCe                                                                                      ZFM na NFC-e modelo 65 [nItem: 999]
 UB131-20 55   Se CST possui indicador que não permite o uso de crédito presumido para a ZFM                      Obrig. 1134 Rejeição: CST do IBS/CBS informado não permite
               (ind_gCredPresIBSZFM = 0):                                                                                     informação do grupo para apropriação de crédito
                  - Grupo gCredPresIBSZFM (id: UB131) informado indevidamente                                                 presumido de IBS sobre o saldo devedor na ZFM
                                                                                                                              [nItem: 999]
 UB131-30     55    Se CST possui indicador que obriga o uso de crédito presumido para a ZFM                      Obrig. 1135 Rejeição: CST do IBS/CBS informado exige a
                    (ind_gCredPresIBSZFM = 1):                                                                                informação do grupo para apropriação de crédito
                       - Não informado grupo gCredPresIBSZFM (id: UB131)                                                      presumido de IBS sobre o saldo devedor na ZFM
                                                                                                                              [nItem: 999]
 UB131-40     55    Se informado grupo do IBS da ZFM (grupo: gCredPresIBSZFM):                                    Obrig. 1158 Rejeição: Tipo de Nota de Crédito não permite o grupo
                        - Tipo de Nota de Crédito (tag: tpNFCredito) diferente de 02 - Apropriação de crédito                 para apropriação de crédito presumido de IBS sobre o
                         presumido de IBS sobre o saldo devedor na ZFM (art. 450, § 1º, LC 214/25)                            saldo devedor na ZFM [nItem: 999]
 UB131-50     55    Se não informado grupo do IBS da ZFM (grupo: gCredPresIBSZFM):                                Obrig. 1159 Rejeição: Tipo de Nota de Crédito exige o grupo para
                       - Tipo de Nota de Crédito (tag: tpNFCredito) igual a 02 - Apropriação de crédito presumido             apropriação de crédito presumido de IBS sobre o
                         de IBS sobre o saldo devedor na ZFM (art. 450, § 1º, LC 214/25)                                      saldo devedor na ZFM [nItem: 999]
 UB132-10     55    Se informado Ano e mês referência do período de apuração (ID: UB132, tag: Obrig. 1160 Rejeição: Ano e mês referência do período de
                    gCredPresIBSZFM/competApur):                                                                              apuração superior ao ano e mês atual [nItem: 999]
                       - Ano/Mês informado superior ao Ano/Mês atual.
 UB133-10     55    Se informado grupo gCredPresIBSZFM (id: UB131):                                               Obrig. 1136 Rejeição: Não é possível repetir o Tipo de
                       - Há dois ou mais itens com o mesmo Tipo de Classificação para o cálculo do crédito                    Classificação para o cálculo do crédito presumido na
                         presumido na ZFM (mesmo valor na tag tpCredPresIBSZFM, id: UB133)                                    ZFM neste DFe [nItem: 999]

Grupo VB. Total do item da NF-e
Campo Modelo                                      Regra de Validação                                  Aplic.   Msg                      Descrição Erro
VB01-05 55/65 Se informado grupo gIBSCBS:                                                             Obrig.   1137 Rejeição: Valor total do Item (vItem) não informado
               - vItem não informado.                                                                               [nItem: 999]
              Observação 1: Implementação Futura.
VB01-10 55/65 Se vItem informado:                                                                     Obrig.   1105 Rejeição: Valor total do Item (vItem) difere do
               Se não é operação de Faturamento Direto para veículos novos (tpOp = nulo ou tpOp <> 2,               somatório dos valores que o compõem [nItem: 999]
                 id:J02):
               - Valor total do Item (vItem) deve ser igual ao somatório:
                 (+) vProd
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
              Observação 1: Implementação Futura.
VB01-20  55   Se vItem informado:                                                                     Obrig.   1105 Rejeição: Valor total do Item (vItem) difere do
               Se informada operação de Faturamento Direto para veículos novos (tpOp = 2, id:J02):                  somatório dos valores que o compõem [nItem: 999]
               - Valor total do Item (vItem) deve ser igual ao somatório:
                 (+) vProd
                 (-) vDesc
                 (-) vICMSDeson, se indDeduzDeson=1
                 (+) vFrete
                 (+) vSeg
                 (+) vOutro
                 (+) vII
                 (+) vIPI

 Campo    Modelo                                     Regra de Validação                              Aplic. Msg                      Descrição Erro
                      (+) vServ
                      (+) vPIS (id: R06, campo: PISST/vPIS), se indSomaPISST=1
                      (+) vCofins (id: T06, campo: COFINSST/vCOFINS), se indSomaCOFINSST =1 (NT
                          2020.005)
                      (+) vIBS
                      (+) vCBS
                      (+) vIS
                   Exceção 1: Em 2025 e 2026 não somar vIBS, vCBS, vIS
                   Observação 1: Implementação Futura.

Grupo VC. Referenciamento de item de outro Documento Fiscal Eletrônico - DF-e
Campo Modelo                                   Regra de Validação                                   Aplic. Msg                       Descrição Erro
VC02-04 65   Se item possui DFe referenciado (tag: DFeReferenciado/chaveAcesso):                    Obrig. 708 Rejeição: NFC-e não pode referenciar documento fiscal
              - NFC-e não pode referenciar outros documentos                                                    [nItem: 999]
VC02-05 55   Se item possui DFe referenciado (tag: DFeReferenciado/chaveAcesso):                    Obrig. 1010 Rejeição: NF-e com referenciamento de documento a
              - Existe documento referenciado a nível de nota (tag: NFref)                                      nível de nota e a nível de item [nItem: 999]
VC02-07 55   Se finNFe=5-Nota de crédito:                                                           Obrig. 1042 Rejeição: NF-e com referenciamento a nível de item
              - Informado referenciamento a nível de item (tag: DFeReferenciado)                                informado indevidamente
             Exceção: Essa regra não se aplica para tpNFCredito=”06-Retorno por recusa parcial na
                entrega”.
VC02-10 55   Se tpNFDebito=”03-Débitos de notas fiscais não processadas na apuração” ou             Obrig. 1038 Rejeição: DFeReferenciado não informado [nItem: 999]
                tpNFDebito=”04-Multa e Juros” ou tpNFCredito=”06-Retorno por recusa parcial na
                entrega:
              - DF-e Referenciado (tag: DFeReferenciado/chaveAcesso) não informado
VC02-14 55   Se NF-e de devolução de mercadoria (tag: finNFe = 4):                                  Obrig.   321 Rejeição: NF-e de devolução de mercadoria não possui
              - Se não informado documento fiscal referenciado no cabeçalho (tag: refNFe):                       documento fiscal referenciado por item [nItem: 999]
                 - Não informado documento fiscal referenciado a nível de no item (tag:
                    DFeReferenciado/chaveAcesso)
             Exceção: não aplicar esta regra para os CFOP 5.921 e 6.921. (NT 2013/005 v1.20)
             Observação 1: Fica proibido o referenciamento da Nota na tag “refNFe” na devolução,
                devendo referenciar no grupo “DFeReferenciado”.
             Observação 1: Na Nota de Devolução é exigido o referenciamento ou no cabeçalho (tag:
                refNFe) ou no Item (grupo: DFeReferenciado), mas não é permitido informar os dois
                simultaneamente.
             Observação 2: Implementação em produção a partir de 05/10/2026 03/11/2026.
VC02-20 55   DFe/Item referenciado em duplicidade:                                                  Obrig. 1072 Rejeição: DFe/Item referenciado em duplicidade [nItem:
             Se item possui DFe referenciado (tag: DFeReferenciado/chaveAcesso):                                999]
              - Informado mais de uma vez uma mesma chave de acesso (tag:
                DFeReferenciado/chaveAcesso) e item (tag: DFeReferenciado/nItem).
             Observação 1: Caso nItem não informado, considerar somente a chaveAcesso.
             Observação 2: Implementação futura.
VC02-30 55   Um único documento fiscal deve ser referenciado:                                       Obrig. 1130 Rejeição: Mais de um documento fiscal referenciado
             Se item possui DFe referenciado (tag: DFeReferenciado/chaveAcesso):                                [nItem: 999]

 Campo    Modelo                                     Regra de Validação                                   Aplic. Msg                      Descrição Erro
                    - Informadas chaves de acesso diferentes em documento referenciado (tag:
                      DFeReferenciado/chaveAcesso).
                   Exceção 1: RV não se aplica caso:
                    - tpNFDebito=”03-Débitos de notas fiscais não processadas na apuração”;
                    - tpNFDebito=“07-Perda em estoque (Perecimento, Perda, Furto, Roubo)”;
                    - finNFe=”4-Devolução”.
VC02-40      55    Se item possui DFe referenciado (tag: DFeReferenciado/chaveAcesso):                    Obrig. 1193 Rejeição: Emitente das NFe Referenciadas deve ser o
                    - Se NF-e de devolução de mercadoria (tag: finNFe = 4):                                           mesmo em todos os itens [nItem: 999]
                       - CNPJ Base ou CPF do Emitente do DFeReferenciado deve ser igual em todos os
                           itens da NFe
                   Observação: No caso de Nota Fiscal Avulsa (NFA) com CNPJ da SEFAZ na Chave de
                      Acesso, considerar o CNPJ Base ou CPF do Emitente.
VC02-50      55    Se item possui DFe referenciado (tag: DFeReferenciado/chaveAcesso):                    Obrig. 1194 Rejeição: Destinatário da NF-e deve ser o igual ao
                    - Se NF-e de devolução de mercadoria (tag: finNFe = 4) e tpNF=1-Saída:                            Emitente da NF referenciada [nItem: 999]
                       - Se o DFeReferenciado for de saída (tpNF=1-Saída):
                         - CNPJ Base ou CPF do Emitente do DFeReferenciado deve ser igual ao CNPJ
                              Base ou CPF do Destinatário da NF-e atual
                   Observação: No caso de Nota Fiscal Avulsa (NFA) com CNPJ da SEFAZ na Chave de
                      Acesso, considerar o CNPJ Base ou CPF do Emitente.
VC03-10      55    Se tpNFDebito=”03-Débitos de notas fiscais não processadas na apuração”:               Obrig. 1039 Rejeição: nItem do DFeReferenciado informado
                    - nItem (tag: DFeReferenciado/nItem) informado indevidamente                                      indevidamente [nItem: 999]
VC03-20      55    Se informado referenciamento a nível de item (tag: DFeReferenciado/chaveAcesso):       Obrig. 1048 Rejeição: nItem do DFeReferenciado não informado
                   Se item possui DFe referenciado (tag: DFeReferenciado/chaveAcesso):                                [nItem: 999]
                    - Se tpNFDebito<>”03-Débitos de notas fiscais não processadas na apuração”:
                       - nItem (tag: DFeReferenciado/nItem) não informado
                   Observação: Implementação futura.

Grupo W03. Total da NF-e - IBS / CBS / IS
 Campo    Modelo                                      Regra de Validação                                  Aplic. Msg                     Descrição Erro
 W07-10    55/65 Total dos Produtos e Serviços (id:W07) difere do somatório do valor dos itens (id:I11)   Obrig. 564 Rejeição: Total do Produto / Serviço difere do somatório
                 sujeitos ao ICMS ou IBS/CBS/IS. Considerar somente os valores dos itens com a TAG                   dos itens
                 indTot (id:I17b) = 1 (NT 2011/004)
 W31-10    55/65 Se grupo de totais do IS (tag: total/ISTot) informado:                                   Obrig. 1073 Rejeição: Total de IS informado indevidamente
                   - Nenhum item possui Imposto Seletivo informado
 W31-20    55/65 Se grupo de totais do IS (tag: total/ISTot) não informado:                               Obrig. 1117 Rejeição: Total de IS não informado
                   - Pelo menos um item possui Imposto Seletivo informado
 W33-10    55/65 O total do Imposto Seletivo (tag: total/ISTot) deverá ser a soma dos campos vIS          Obrig. 1075 Rejeição: Total do Imposto Seletivo difere da soma dos
                 informados nos itens (tag: det/imposto/IS/vIS).                                                      itens
                 Nota: Implementação Futura.
 W34-10    55/65 Se grupo de totais do IBS e da CBS (tag: total/IBSCBSTot) informado:                     Obrig. 1118 Rejeição: Total de IBS e CBS informado indevidamente
                    - Nenhum item possui IBS / CBS informado (id: UB12, tag: IBSCBS)
 W34-20    55/65 Se grupo de totais do IBS e da CBS (tag: total/IBSCBSTot) não informado:                 Obrig. 1119 Rejeição: Total de IBS e CBS não informado

 Campo     Modelo                                      Regra de Validação                                 Aplic.   Msg                    Descrição Erro
                      - Pelo menos um item possui IBS / CBS informado (id: UB12, tag: IBSCBS)
 W35-10    55/65    O total da BC do IBS e da CBS de deverá ser a soma dos campos vBC (tag:               Obrig. 1076 Rejeição: Total da BC do IBS e da CBS difere da soma
                    gIBSCBS/vBC) informados nos itens                                                                 dos itens
 W38-10    55/65    O total do diferimento do IBS UF deverá ser a soma do campo vDif do IBS UF informados Obrig. 1077 Rejeição: Total de Diferimento do IBS UF difere da
                    nos itens                                                                                         soma dos itens
 W39-10    55/65    O total devolvido do IBS UF deverá ser a soma do campo vDevTrib do IBS UF informados Obrig.  1078 Rejeição: Total Devolvido do IBS UF difere da soma
                    nos itens                                                                                         dos itens
 W41-10    55/65    O total do IBS UF deverá ser a soma do campo vIBSUF informados nos itens              Obrig. 1080 Rejeição: Total de IBS UF difere da soma dos itens
 W43-10    55/65    O total do Diferimento do IBS Municipal deverá ser a soma do campo vDif do IBS        Obrig. 1081 Rejeição: Total de Diferimento do IBS Municipal difere
                    Municipal informados nos itens                                                                    da soma dos itens
 W44-10    55/65    O total devolvido do IBS Municipal deverá ser a soma do campo vDevTrib do IBS         Obrig. 1082 Rejeição: Total Devolvido do IBS Municipal difere da
                    Municipal informados nos itens                                                                    soma dos itens
 W46-10    55/65    O total do IBS Municipal deverá ser a soma do campo vIBSMun informados nos itens      Obrig. 1084 Rejeição: Total de IBS Municipal difere da soma dos
                                                                                                                      itens
 W47-10    55/65 O total do IBS deverá ser a soma do valor do IBS (tag: gIBSCBS/vIBS) informado nos       Obrig. 1085 Rejeição: Total do IBS difere da soma do vIBS dos itens
                 itens
 W48-10    55/65 O total do Crédito Presumido do IBS deverá ser a soma do campo vCredPres do IBS          Obrig. 1086 Rejeição: Total de Crédito Presumido do IBS UF difere
                 informados nos itens                                                                                 da soma dos itens
 W53-10    55/65 O total do Diferimento da CBS deverá ser a soma do campo vDif da CBS informados nos      Obrig. 1088 Rejeição: Total de Diferimento da CBS difere da soma
                 itens                                                                                                dos itens
 W54-10    55/65 O total devolvido da CBS deverá ser a soma do campo vDevTrib da CBS informados nos       Obrig. 1089 Rejeição: Total Devolvido da CBS difere da soma dos
                 itens                                                                                                itens
W56-10     55/65 O total da CBS deverá ser a soma do campo vCBS informados nos itens                      Obrig. 1091 Rejeição: Total de CBS difere da soma dos itens
W56a-10    55/65 O total do Crédito Presumido da CBS deverá ser a soma do campo vCredPres da CBS          Obrig. 1087 Rejeição: Total de Crédito Presumido da CBS difere da
                 informados nos itens                                                                                 soma dos itens
 W58-10    55/65 O total do IBS monofásico deverá ser a soma dos campos vIBSMono informados nos           Obrig. 1092 Rejeição: Total do IBS monofásico difere da soma dos
                 itens                                                                                                itens
 W59-10    55/65 O total da CBS monofásica deverá ser a soma dos campos vCBSMono informados nos           Obrig. 1093 Rejeição: Total da CBS monofásica difere da soma dos
                 itens                                                                                                itens
W59a-10    55/65 O total do IBS monofásico sujeito à retenção deverá ser a soma dos campos                Obrig. 1120 Rejeição: Total do IBS monofásico sujeito à retenção
                 vIBSMonoReten informados nos itens                                                                   difere da soma dos itens
W59b-10    55/65 O total da CBS monofásica sujeita à retenção deverá ser a soma dos campos                Obrig. 1121 Rejeição: Total da CBS monofásica sujeita à retenção
                 vCBSMonoReten informados nos itens                                                                   difere da soma dos itens
W59c-10    55/65 O total do IBS monofásico retido anteriormente deverá ser a soma dos campos              Obrig. 1122 Rejeição: Total do IBS monofásico retido anteriormente
                 vIBSMonoRet informados nos itens                                                                     difere da soma dos itens
W59d-10    55/65 O total da CBS monofásica retida anteriormente deverá ser a soma dos campos              Obrig. 1123 Rejeição: Total da CBS monofásica retida
                 vCBSMonoRet informados nos itens                                                                     anteriormente difere da soma dos itens
 W59f-10   55/65 O total do IBS estornado deverá ser a soma dos campos “gEstornoCred/vIBS” informados     Obrig. 1176 Rejeição: Total do IBS estornado difere da soma dos
                 nos itens                                                                                            itens
W59g-10    55/65 O total da CBS estornada deverá ser a soma dos campos “gEstornoCred/vCBS”                Obrig. 1177 Rejeição: Total da CBS estornada difere da soma dos
                 informados nos itens                                                                                 itens

 Campo    Modelo                                   Regra de Validação                                     Aplic. Msg                       Descrição Erro
 W60-05    55/65 Se informado grupo IBSCBSTot:                                                            Obrig. 1004 Rejeição: Valor total da NF-e com IBS / CBS / IS
                  - vNFTot não informado.                                                                             (vNFTot) não informado
                 Observação: Implementação futura.
 W60-10    55/65 Se vNFTot informado:                                                                     Obrig. 1094 Rejeição: Total da NFe difere da soma do total dos
                  - O total geral do DFe (tag: vNFTot) deverá ser a soma do total dos itens (vItem, tag               itens da Nota
                    VB01).
                 Observação: Implementação futura.

Grupo 3A. Banco de Dados: NF-e Referenciada
 Campo Modelo                                      Regra de Validação                                   Aplic. Msg                   Descrição Erro
3BA02-10 55   Para cada NF-e referenciada (tag:refNFe), se a UF da Chave de Acesso referenciada for     Obrig. 267 Rejeição: Chave de Acesso referenciada inexistente
              igual a UF do Emitente:                                                                              [nRef: xxx]
                - Acessar BD NFE com Chave de Acesso referenciada (se mod=55)
                   - NF-e referenciada inexistente
              Exceção: A NF-e referenciada pode não existir no caso de Emissão em Contingência
                  (tpEmis = 2, 4 ou 5) (NT 2013/003) ou NFF (tpEmis=3), desde que a Chave de Acesso
                  da NF-e referenciada tenha o Ano-Mês de Emissão inferior a 1 mês da data atual ou
                  desde que exista o EPEC (NT 2021.004).
              Observação 1: A exceção acima não se aplica para:
                - “finNFe=2" (NF-e Complementar)
                - “tpNFCredito=”01” (Multa e juros)
                - “tpNFCredito=”03” (Retorno)
3BA02-50 55   Se NF-e de Devolução (finNFe = 4): (NT 2022.005)                                          Obrig. 545 Rejeição: NF-e de devolução com valor total superior
                - Se informado documento fiscal referenciado no cabeçalho (tag: refNFe):                           a NF-e devolvida
                   - Valor total da NF-e de Devolução (tag: vNF, id:W16) maior que o somatório do valor
                  correspondente das NF-e referenciadas
              Exceção 1: A RV somente será aplicada se todas as NF-e referenciadas existirem no BD
                  da SEFAZ.
              Exceção 2: A RV poderá não ser aplicada, se existirem documentos fiscais referenciados
                  com modelo diferente de 55.
              Exceção 3: A RV não será aplicada se existirem NF de Produtor referenciada,
                  inviabilizando a identificação do valor devolvido;
              Exceção 4: A RV não será aplicada à NF-e de Devolução no caso de Comércio Exterior
                  (idDest=3);
              Observação 1: Se a NF-e de devolução tiver muitas NF-e referenciadas, a conferência do
                  valor pode prejudicar a performance do Ambiente de Autorização. Nesses casos, a
                  SEFAZ Autorizadora poderá não aplicar essa RV. Por exemplo, limitar a aplicação da
                  RV somente para as NF-e de devolução com até 5 NF-e referenciadas e/ou com NF-e
                  referenciadas de até 3 meses anteriores.
              Observação 2: A devolução pode ocorrer para muitos itens de diferentes NF-e, Considerar
              uma tolerância de até R$ 1,00 na validação.
3BA02-54 55   Se NF-e de Devolução (finNFe = 4): (NT 2022.005)                                          Obrig. 546 Rejeição: NF-e de devolução com valor do ICMS
                - Se informado documento fiscal referenciado no cabeçalho (tag: refNFe):                           superior a NF-e devolvida

  Campo    Modelo                                       Regra de Validação                                  Aplic. Msg                   Descrição Erro
                       - Valor total do ICMS da NF-e de Devolução (tag: vICMS, id:W04) maior que o
                       somatório do valor correspondente das NF-e referenciadas
                    Exceção 1: A RV somente será aplicada se todas as NF-e referenciadas existirem no BD
                       da SEFAZ.
                    Exceção 2: A RV poderá não ser aplicada, se existirem documentos fiscais referenciados
                       com modelo diferente de 55;
                    Exceção 3: A RV não será aplicada se existirem NF de Produtor referenciada,
                       inviabilizando a identificação do valor devolvido;
                    Observação 1: Se a NF-e de devolução tiver muitas NF-e referenciadas, a conferência do
                       valor pode prejudicar a performance do Ambiente de Autorização. Nesses casos, a
                       SEFAZ Autorizadora poderá não aplicar essa RV. Por exemplo, limitar a aplicação da
                       RV somente para as NF-e de devolução com até 5 NF-e referenciadas e/ou com NF-e
                       referenciadas de até 3 meses anteriores.
                    Observação 2: A devolução pode ocorrer para muitos itens de diferentes NF-e, Considerar
                       uma tolerância de até R$ 1,00 na validação.
3BA02-58      55    Se NF-e de Devolução (finNFe = 4): (NT 2022.005)                                        Obrig. 566 Rejeição: NF-e de devolução com valor do FCP
                     - Se informado documento fiscal referenciado no cabeçalho (tag: refNFe):                          superior a NF-e devolvida
                       - Valor total do FCP da NF-e de Devolução (tag: vFCP, id:W04h) maior que o somatório
                       do valor correspondente das NF-e referenciadas
                    Exceção 1: A RV somente será aplicada se todas as NF-e referenciadas existirem no BD
                       da SEFAZ.
                    Exceção 2: A RV poderá não ser aplicada, se existirem documentos fiscais referenciados
                       com modelo diferente de 55;
                    Exceção 3: A RV não será aplicada se existirem NF de Produtor referenciada,
                       inviabilizando a identificação do valor devolvido;
                    Observação 1: Se a NF-e de devolução tiver muitas NF-e referenciadas, a conferência do
                       valor pode prejudicar a performance do Ambiente de Autorização. Nesses casos, a
                       SEFAZ Autorizadora poderá não aplicar essa RV. Por exemplo, limitar a aplicação da
                       RV somente para as NF-e de devolução com até 5 NF-e referenciadas e/ou com NF-e
                       referenciadas de até 3 meses anteriores.
                    Observação 2: A devolução pode ocorrer para muitos itens de diferentes NF-e, Considerar
                    uma tolerância de até R$ 1,00 na validação.
3BA02-64      55    Se NF-e de Devolução (finNFe = 4): (NT 2022.005)                                        Obrig. 567 Rejeição: NF-e de devolução com valor do ICMS da
                     - Se informado documento fiscal referenciado no cabeçalho (tag: refNFe):                          UF Destino superior a NF-e devolvida
                       - Valor total do ICMS interestadual da NF-e de Devolução (tag: vICMSUFDest,
                       id:W04e) maior que o somatório do valor correspondente das NF-e referenciadas
                    Exceção 1: A RV somente será aplicada se todas as NF-e referenciadas existirem no BD
                       da SEFAZ.
                    Exceção 2: A RV poderá não ser aplicada, se existirem documentos fiscais referenciados
                       com modelo diferente de 55;
                    Exceção 3: A RV não será aplicada se existirem NF de Produtor referenciada,
                       inviabilizando a identificação do valor devolvido;
                    Observação 1: Se a NF-e de devolução tiver muitas NF-e referenciadas, a conferência do
                       valor pode prejudicar a performance do Ambiente de Autorização. Nesses casos, a

  Campo    Modelo                                       Regra de Validação                                       Aplic. Msg                   Descrição Erro
                       SEFAZ Autorizadora poderá não aplicar essa RV. Por exemplo, limitar a aplicação da
                       RV somente para as NF-e de devolução com até 5 NF-e referenciadas e/ou com NF-e
                       referenciadas de até 3 meses anteriores.
                    Observação 2: A devolução pode ocorrer para muitos itens de diferentes NF-e, Considerar
                       uma tolerância de até R$ 1,00 na validação.
3BA02-68      55    Se NF-e de Devolução (finNFe = 4): (NT 2022.005)                                             Obrig. 581 Rejeição: NF-e de devolução com valor do FCP da
                     - Se informado documento fiscal referenciado no cabeçalho (tag: refNFe):                               UF Destino superior a NF-e devolvida
                       - Valor total do FCP interestadual da NF-e de Devolução (tag: vFCPUFDest, id:W04c)
                       maior que o somatório do valor correspondente das NF-e referenciadas
                    Exceção 1: A RV somente será aplicada se todas as NF-e referenciadas existirem no BD
                       da SEFAZ.
                    Exceção 2: A RV poderá não ser aplicada, se existirem documentos fiscais referenciados
                       com modelo diferente de 55;
                    Exceção 3: A RV não será aplicada se existirem NF de Produtor referenciada,
                       inviabilizando a identificação do valor devolvido;
                    Observação 1: Se a NF-e de devolução tiver muitas NF-e referenciadas, a conferência do
                       valor pode prejudicar a performance do Ambiente de Autorização. Nesses casos, a
                       SEFAZ Autorizadora poderá não aplicar essa RV. Por exemplo, limitar a aplicação da
                       RV somente para as NF-e de devolução com até 5 NF-e referenciadas e/ou com NF-e
                       referenciadas de até 3 meses anteriores.
                    Observação 2: A devolução pode ocorrer para muitos itens de diferentes NF-e, Considerar
                       uma tolerância de até R$ 1,00 na validação.
3BA02-70      55    Se NF-e de crédito (tag: finNFe=5) e tpNFCredito=”01-Multa e juros” ou tpNFCredito=”03- Obrig. 1095 Rejeição: Chave de acesso referenciada deve existir e
                    Retorno”:                                                                                               não estar cancelada [nRef: xxx]
                     - Para cada NF-e referenciada (tag:refNFe):
                       - Acessar BD NFE com Chave de Acesso referenciada (se mod=55)
                          - Chave de acesso referenciada deve existir e não estar cancelada.
                    Nota Explicativa: Em operação entre empresas, o fornecedor pode cobrar multa e juros do
                       cliente e no valor cobrado de juros e multas, incide o IBS e a CBS. O fornecedor deve
                       emitir uma nota de débito do tipo “multa e juros” para que o adquirente do regime regular
                       possa se creditar do valor pago. Caso o fornecedor não emita a nota de débito, o
                       adquirente tem como alternativa emitir uma nota de crédito, do tipo ”01-Multa e juros”
                       para se creditar. Esse crédito é condicionado à emissão do evento “Aceite de débito na
                       apuração por emissão de nota de crédito” pelo fornecedor e a quitação do débito
                       correspondente em sua apuração.

Grupo 11. Banco de Dados: Notas de antecipação de pagamento
 Campo    Modelo                                  Regra de Validação                                  Aplic.   Msg                     Descrição Erro
11BC01-10   65   Se modelo = 65 (NFC-e):                                                              Obrig.   1146 Rejeição: NF-e referenciada de pagamento
                   - Informado NF-e referenciada de pagamento antecipado (tag: gPagAntecipado\refNFe)               antecipado informada indevidamente
11BC01-20   55   Se informado NF-e referenciada de pagamento antecipado (tag: gPagAntecipado\refNFe): Obrig.   1147 Rejeição: NF-e referenciada de pagamento
                  - NF-e referenciada de pagamento antecipado inexistente                                           antecipado inexistente
                 Exceção 01: NF-e referenciada de pagamento antecipado pode não existir se UF da
                    Chave Acesso diverge da Sefaz Autorizadora.
                 Exceção 2: A NF-e referenciada de pagamento antecipado pode não existir no caso de
                    Emissão em Contingência (tpEmis = 2, 4 ou 5), desde que a Chave de Acesso da NF-
                    e referenciada tenha o Ano-Mês de Emissão inferior a 1 mês da data atual ou desde
                    que exista o EPEC.
11BC01-30   55   Se informado NF-e referenciada de pagamento antecipado (tag: gPagAntecipado\refNFe): Obrig.   1143 Rejeição: NF-e referenciada de pagamento
                  - NF-e referenciada de pagamento antecipado é diferente de nota de débito do tipo                 antecipado deve ser do tipo débito, pagamento
                    06=Pagamento antecipado (tag: tpNFDebito)                                                       antecipado
                 Observação: Implementação Futura
```

## 8. Eventos

```text
Os eventos descritos neste item integram as obrigações acessórias do Imposto sobre Bens e Serviços (IBS) e da Contribuição sobre Bens e Serviços
(CBS). Esses eventos são indispensáveis para a correta apuração dos tributos e de créditos de imposto. Eles visam garantir a integridade e a
rastreabilidade das operações realizadas pelos contribuintes, servindo como base de dados para o controle e a transparência do novo modelo tributário.

De acordo com o artigo 348, §1º, da Emenda Constitucional, os contribuintes estarão dispensados do recolhimento do IBS e da CBS relativamente
aos fatos geradores ocorridos entre 1º de janeiro e 31 de dezembro de 2026, desde que cumpram integralmente as obrigações acessórias previstas
na legislação.

Nesse contexto, a apresentação correta e tempestiva dos eventos mencionados neste item é condição essencial para que o contribuinte possa usufruir
da dispensa do recolhimento dos tributos nesse período de transição. O não cumprimento dessas obrigações poderá implicar na perda desse benefício,
sujeitando o contribuinte ao recolhimento normal dos tributos devidos.

Portanto, os eventos devem ser registrados, a partir de janeiro/2026, sempre que a situação concreta exigir, respeitando os critérios e prazos
estabelecidos pela legislação, como forma de garantir o direito à dispensa e de contribuir para a efetividade do novo sistema tributário.

8.1. Lista de eventos
Esta NT cria os eventos a seguir para a apuração do IBS e da CBS.

Esses eventos serão autorizados na SVRS – SEFAZ VIRTUAL DO RIO GRANDE DO SUL. As URLs de produção e homologação podem ser
encontradas no Portal Nacional da NFe, na aba Serviços, Relação de Serviços Web.

 CÓDIGO                                                 EVENTO                                                        Autor
  112110 Informação de efetivo pagamento integral para liberar crédito presumido do adquirente                Emitente
  112120 Importação em ALC/ZFM não convertida em isenção                                                      Emitente
  112130 Perecimento, perda, roubo ou furto durante o transporte contratado pelo fornecedor                   Emitente
  112140 Fornecimento não realizado com pagamento antecipado                                                  Emitente
  112150 Atualização da Data de Previsão de Entrega                                                           Emitente
  211110 Solicitação de Apropriação de crédito presumido                                                      Emitente/Destinatário
  211124 Perecimento, perda, roubo ou furto durante o transporte contratado pelo adquirente                   Destinatário
  211128 Aceite de débito na apuração por emissão de nota de crédito                                          Destinatário
  211130 Imobilização de Item                                                                                 Destinatário
  211140 Solicitação de Apropriação de Crédito de Combustível                                                 Destinatário
  211150 Solicitação de Apropriação de Crédito para bens e serviços que dependem de atividade do adquirente   Destinatário
  212110 Manifestação sobre Pedido de Transferência de Crédito de IBS em Operações de Sucessão                Sucessora
  212120 Manifestação sobre Pedido de Transferência de Crédito de CBS em Operações de Sucessão                Sucessora
  412120 Manifestação do Fisco sobre Pedido de Transferência de Crédito de IBS em Operações de Sucessão       Fisco
  412130 Manifestação do Fisco sobre Pedido de Transferência de Crédito de CBS em Operações de Sucessão       Fisco

Criado também um código de Evento de Cancelamento genérico que será utilizado para o cancelamento de qualquer um dos Eventos citados
anteriormente nesta Nota Técnica. Neste Evento deve ser informado o código do Evento a ser cancelado.
 CÓDIGO            EVENTO                                  Autor
  110001 Cancelamento de Evento Idem ao Autor do Evento que está sendo cancelado

8.2. Registro de Eventos
O Web Service de Registro de Evento possui uma parte geral, complementada por uma área específica para cada tipo de evento.

A parte geral se mantém a mesma para envio de todos os eventos e está especificada na seção 5.8 do Manual de Orientação do Contribuinte (MOC)
e na seção Web Service – NFeRecepcaoEvento – Parte Geral do MOC Online.

A mensagem de retorno será modificada, conforme apresentado na seção Leiaute Mensagem de Retorno e o leiaute das partes específicas dos
novos eventos está detalhado nas seções seguintes.

Importante:
  Atualmente a empresa pode montar um Lote com até 20 Eventos em cada requisição enviada para o Web Service de Eventos. O uso de Lote de
  documentos a serem autorizados pode resultar em uma dificuldade operacional para as empresas e uma potencial perda de controle, principalmente
  no caso de rejeição de algum evento dentro do Lote. Nesse sentido, futuramente, deverá ser eliminada a possibilidade de uso de Lote para o envio
  dos Eventos.

   Para esses novos Eventos vinculados a Reforma Tributária, orientamos as empresas a não compor Lote, enviando cada Evento individualmente.

8.3. Evento: Informação de efetivo pagamento integral para liberar crédito presumido do adquirente
Função: Permitir que o emitente da NFe informe o efetivo pagamento integral da operação a fim de liberar crédito presumido do adquirente
Modelo: NF-e modelo 55
Autor do Evento: Emitente da NFe
Código do Tipo de Evento: 112110

8.3.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e112110_v1.00.xsd
#     Campo             Ele   Pai Tipo Ocor. Tam. Descrição/Observação
P17   detEvento          G    P06       1-1    - Detalhes do Evento
P18   versao             A    P17 N     1-1   2v2 Versão do leiaute do evento (P16)
P19   descEvento         E    P17 C     1-1   85 Descrição do evento: "Informação de efetivo pagamento integral para liberar crédito presumido do adquirente"
P20   cOrgaoAutor        E    P17 N     1-1    2 Código do Órgão Autor do Evento. Informar o Código da UF para este Evento.
P21   tpAutor            E    P17 N     1-1    1 Informar 1=Empresa emitente.
                                                  Valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros Órgãos.
P22 verAplic             E    P17 N     1-1  1-20 Versão do aplicativo do autor do evento.
P23 indQuitacao          E    P17 N     1-1    1 Indicador de efetiva quitação do pagamento integral da operação referente a NFe referenciada. Valor deve ser igual a
                                                  "1"

8.3.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.4. Evento: Solicitação de Apropriação de crédito presumido
Função: Evento a ser gerado pelo destinatário da NF-e em relação às notas fiscais de aquisição de emissão de terceiros e que lhe gerem o direito à
  apropriação de crédito presumido, ou pelo emitente quando a informação não tiver sido incluída na NF-e ou necessitar correção.
Autor: Emitente ou Destinatário da NFe
Modelo: NF-e modelo 55
Código do Tipo de Evento: 211110

8.4.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e211110_v1.00.xsd
#     Campo                           Ele   Pai Tipo Ocor. Tam. Descrição/Observação
P17   detEvento                        G    P06       1-1       Detalhes do Evento
P18   versao                           A    P17 N     1-1   2v2 Versão do leiaute do evento (P16)
P19   descEvento                       E    P17 C     1-1   47 Descrição do evento: "Solicitação de Apropriação de crédito presumido"
P20   cOrgaoAutor                      E    P17 N     1-1    2 Código do Órgão Autor do Evento. Informar o Código da UF para este Evento.
P21   tpAutor                          E    P17 N     1-1    1 Informar 1=Empresa Emitente ou 2=Empresa destinatária.
                                                                Valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros
                                                                Órgãos.
P22 verAplic                           E    P17 N     1-1  1-20 Versão do aplicativo do autor do evento.
P23 gCredPresOper                      G    P17      1-990      Informações de crédito presumido por item
P24 nItem                              A    P23 N     1-1   1-3 Corresponde ao atributo “nItem” do elemento “det” do documento referenciado.
P25 vBCCredPres                        E    P23 N     1-1 13v2 Valor do base de cálculo do item
P25a cCredPres                         E    P23 N     1-1    2 Código de Classificação do Crédito presumido, conforme tabela cCredPres (Anexo IV)
P26 gIBSCredPres                       G    P23       0-1       Grupo de Informações do Crédito Presumido do IBS
P28 pCredPres                          E    P26 N     1-1 3v2-4 Percentual do Crédito Presumido
P29 vCredPres                          E    P26 N     1-1 13v2 Valor do Crédito Presumido
P30 gCBSCredPres                       G    P23       0-1       Grupo de Informações do Crédito Presumido da CBS
P32 pCredPres                          E    P30 N     1-1 3v2-4 Percentual do Crédito Presumido
P33 vCredPres                          E    P30 N     1-1 13v2 Valor do Crédito Presumido

8.4.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.4.3. Validação das Regras de Negócio – Específicas
Serão aplicadas as regras de validação gerais apresentadas no item 5.8.4 do MOC e as regras de negócio específicas listadas a seguir.

#       Regra de Validação                                                                           Aplic. Msg Descrição Erro
Banco de Dados: NF-e
2P12-10 Modelo DFe = 65-NFCe                                                                         Obrig. 1049 Rejeição: Não é permitido o uso de Crédito Presumido na
                                                                                                                 NFC-e modelo 65
2P21-05 Se tpAutor=1-Empresa Emitente:                                                               Obrig. 574 Rejeição: Autor do evento diverge do emitente da NF-e
            - CNPJ/CPF do Autor diverge do CNPJ/CPF do Emitente da NF-e
2P21-10 Se tpAutor=2-Empresa Destinatário:                                                           Obrig.   575 Rejeição: Autor do evento diverge do destinatário da NF-e
            - CNPJ/CPF do Autor diverge do CNPJ/CPF do Destinatário da NF-e
2P24-05 Atributo “nItem” duplicado                                                                   Obrig.  -- Observação: Validação realizada pelo Schema XML
2P24-10 Acessar BD e verificar se número do item do evento (tag: gCredPres/nItem) informado existe   Obrig. 1096 Rejeição: Número de item não existe na NFe
         na NFe referenciada (tag: det/nItem)
2P25a-10 Se informado cCredPres da operação (tag: gCredPresOper/cCredPres):                          Obrig. 1055 Rejeição: Código de Crédito Presumido (cCredPres) da
            - cCredPres inexistente                                                                              Operação inexistente [nItem: 999]
         Observação: Consultar tabela de Crédito Presumido do IBS e da CBS.
2P26-10 Se cCredPres possui indicador que não permite o uso de crédito presumido para o IBS          Obrig. 1053 Rejeição: Crédito Presumido para o IBS informado
         (ind_gIBSCredPres = 0):                                                                                 indevidamente [nItem: 999]
            - Crédito presumido para o IBS informado indevidamente (grupo:
              gCredPresOper/gIBSCredPres)
         Observação 01: Consultar Tabela de Crédito Presumido do IBS e da CBS.
2P26-20 Se cCredPres possui indicador que exige o uso de crédito presumido para o IBS                Obrig. 1054 Rejeição: Crédito Presumido para o IBS não informado
         (ind_gIBSCredPres = 1):                                                                                 [nItem: 999]
            - Crédito presumido para o IBS não informado (grupo: gCredPresOper/gIBSCredPres)
         Observação 01: Consultar Tabela de Crédito Presumido do IBS e da CBS.
2P30-10 Se cCredPres possui indicador que não permite o uso de crédito presumido para a CBS          Obrig. 1050 Rejeição: Crédito Presumido para a CBS informado
         (ind_gCBSCredPres = 0):                                                                                 indevidamente [nItem: 999]
            - Crédito presumido para a CBS informado indevidamente (grupo:
              gCredPresOper/gCBSCredPres)
         Observação 01: Consultar Tabela de Crédito Presumido do IBS e da CBS.
2P30-20 Se cCredPres (id: UB122) possui indicador que exige o uso de crédito presumido para a CBS    Obrig. 1058 Rejeição: Crédito Presumido para a CBS não informado
         (ind_gCBSCredPres = 1):                                                                                 [nItem: 999]
            - Crédito presumido para a CBS não informado (grupo:
              IBSCBS/gCredPresOper/gCBSCredPres)
         Observação 01: Consultar Tabela de Crédito Presumido do IBS e da CBS.

8.5. Evento: Aceite de débito na apuração por emissão de nota de crédito
Função: Permitir ao destinatário informar que concorda com os valores constantes em nota de crédito emitida pelo fornecedor ou pelo adquirente que
  serão lançados a débito na apuração assistida de IBS e CBS
Modelo: NF-e modelo 55
Autor do Evento: Destinatário da NF-e
Código do Tipo de Evento: 211128

8.5.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e211128_v1.00.xsd
#     Campo          Ele   Pai Tipo Ocor.   Tam. Descrição/Observação
P17   detEvento       G    P06      1-1          Detalhes do Evento
P18   versao          A    P17 N 1-1         2v2 Versão do leiaute do evento (P16)
P19   descEvento      E    P17 C 1-1         85 Descrição do evento: "Aceite de débito na apuração por emissão de nota de crédito"
P20   cOrgaoAutor     E    P17 N 1-1          2 Código da UF do emitente do Evento
P21   tpAutor         E    P17 N 1-1          1 Informar 2=Empresa destinatária.
P22   verAplic        E    P17 N 1-1        1-20 Versão do aplicativo do autor do evento.
P23   indAceitacao    E    P17 N 1-1          1 Indicador de concordância com o valor da nota de crédito que lançaram IBS e CBS na apuração assistida. Valores: 0 = não
                                                 aceite; 1 = aceite.

8.5.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.6. Evento: Imobilização de Item
Função: Evento a ser gerado pelo adquirente de bem, quando este for integrado ao seu ativo imobilizado, a fim de viabilizar a adequada identificação,
  pelos sistemas da administração tributária, de prazo-limite para apreciação de eventuais pedidos de ressarcimento do respectivo crédito, nos termos
  do art. 40, I da LC 214/2025.
Modelo: NF-e modelo 55
Autor do Evento: Destinatário da NF-e (Adquirente)
Código do Tipo de Evento: 211130

8.6.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e211130_v1.00.xsd
#     Campo               Ele   Pai Tipo Ocor. Tam. Descrição/Observação
P17   detEvento            G    P06       1-1        Detalhes do Evento
P18   versao               A    P17 N     1-1   2v2 Versão do leiaute do evento (P16)
P19   descEvento           E    P17 C     1-1  5-60 Descrição do evento: "Imobilização de Item"
P20   cOrgaoAutor          E    P17 N     1-1    2   Código da UF do emitente do Evento
P21   tpAutor              E    P17 N     1-1    1   Informar 2=Empresa destinatária.
P22   verAplic             E    P17 N     1-1  1-20 Versão do aplicativo do autor do evento.
P23   gImobilizacao        G    P17      1-990       Informações de itens integrados ao ativo imobilizado
P24   nitem                A    P23 N     1-1   1-3 Corresponde ao atributo “nItem” do elemento “det” do documento referenciado.
P25   vIBS                 E    P23 N     1-1  13v2 Valor do IBS relativo à imobilização
P26   vCBS                 E    P23 N     1-1  13v2 Valor da CBS relativo à imobilização
P27   gControleEstoque     G    P23       1-1        Informações de crédito presumido por item
P28   qImobilizado         E    P27 N     1-1 11v0-4 Informar a quantidade do item a ser imobilizado
P29   uImobilizado         E    P27 C     1-1  1 - 6 Informar a unidade relativa ao campo qImobilizado

8.6.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.6.3. Validação das Regras de Negócio – Específicas
Serão aplicadas as regras de validação gerais apresentadas no item 5.8.4 do MOC e as regras de negócio específicas listadas a seguir.

#       Regra de Validação                                                                        Aplic. Msg Descrição Erro
Banco de Dados: NF-e
2P21-10 Se tpAutor=2-Empresa Destinatário:                                                        Obrig.   575 Rejeição: Autor do evento diverge do destinatário da NF-e
            - CNPJ/CPF do Autor diverge do CNPJ/CPF do Destinatário da NF-e
2P24-10 Acessar BD e verificar se número do item do evento (tag: gImobilizacao/nItem) informado   Obrig. 1096 Rejeição: Número de item não existe na NFe
        existe na NFe referenciada (tag: det/nItem)

#       Regra de Validação                                                                         Aplic. Msg Descrição Erro
2P25-10 Acessar BD e verificar se valor do IBS do evento (tag: gImobilizacao/vIBS) é maior que o   Obrig. 1097 Rejeição: O valor do IBS do item não pode ser maior que o valor
        valor do IBS do item informado na NFe                                                                  do IBS do respectivo item na NFe.
2P26-10 Acessar BD e verificar se valor da CBS do evento (tag: gImobilizacao /vCBS) é maior que o Obrig. 1098 Rejeição: O valor da CBS do item não pode ser maior que o
        valor da CBS do item informado na NFe                                                                  valor da CBS do respectivo item na NFe.
2P29-10 Se unidade for igual a unidade da nota, acessar BD e verificar se a quantidade imobilizada Obrig. 1100 Rejeição: A quantidade imobilizada não pode ser maior que a
        do item informado (tag: gControleEstoque/qImobilizada) é maior que a quantidade no item                quantidade do respectivo item na NFe (qCom)
        da NFe (tag: det/prod/qCom)

8.7. Evento: Solicitação de Apropriação de Crédito de Combustível
Função: Evento a ser gerado pelo adquirente de combustível listado no art. 172 da LC 214/2025 e que pertença à cadeia produtiva desses
  combustíveis, para solicitar a apropriação de crédito referente à parcela que for consumida em sua atividade comercial, observada exceção do art.
  180 da LC 214/2025.
Modelo: NF-e modelo 55
Autor do Evento: Destinatário da NF-e (Adquirente de combustível que faça parte da cadeia produtiva de combustíveis)
Código do Tipo de Evento: 211140

8.7.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e211140_v1.00.xsd
#     Campo              Ele Pai Tipo Ocor. Tam.      Descrição/Observação
P17   detEvento           G P06        1-1 -          Detalhes do Evento
P18   versao              A P17 N      1-1 2v2        Versão do leiaute do evento (P16)
P19   descEvento          E P17 C      1-1 52         Descrição do evento: "Solicitação de Apropriação de Crédito de Combustível"
P20   cOrgaoAutor         E P17 N      1-1 2          Código da UF do emitente do Evento
P21   tpAutor             E P17 N      1-1 1          Informar 2=Empresa destinatária.
                                                      Valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros Órgãos.
P22   verAplic             E   P17    N    1-1 1-20   Versão do aplicativo do autor do evento.
P23   gConsumoComb         G   P17        1-990       Informações de consumo de combustíveis
P24   nitem                A   P23    N    1-1 1-3    Corresponde ao atributo “nItem” do elemento “det” do documento referenciado.
P25   vIBS                 E   P23    N    1-1 13v2   Valor do IBS relativo ao consumo de combustível na nota de aquisição
P26   vCBS                 E   P23    N    1-1 13v2   Valor da CBS relativo ao consumo de combustível na nota de aquisição
P27   gControleEstoque     G   P23         1-1        Informações de quantidade por item
P28   qComb                E   P27    N    1-1 11v0-4 Informar a quantidade de consumo do item

#   Campo                Ele Pai Tipo Ocor. Tam.        Descrição/Observação
P29 uComb                 E P27 C      1-1 1-6          Informar a unidade relativa ao campo qComb

8.7.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.7.3. Validação das Regras de Negócio – Específicas
Serão aplicadas as regras de validação gerais apresentadas no item 5.8.4 do MOC e as regras de negócio específicas listadas a seguir.

   #                                          Regra de Validação                                     Aplic.   Msg                       Descrição Erro
Banco de Dados: NF-e
2P21-10 Se tpAutor=2-Empresa Destinatário:                                                           Obrig.   575 Rejeição: Autor do evento diverge do destinatário da NF-e
            - CNPJ/CPF do Autor diverge do CNPJ/CPF do Destinatário da NF-e
2P24-10 Acessar BD e verificar se número do item do evento (tag: gConsumoComb/nItem) informado       Obrig.   1096 Rejeição: Número de item não existe na NFe
        existe na NFe referenciada (tag: det/nItem)
2P25-10 Acessar BD e verificar se valor do IBS do evento (tag: gConsumoComb/vIBS) é maior que o      Obrig.   1097 Rejeição: O valor do IBS do item não pode ser maior que o
        valor do IBS do item informado na NFe                                                                      valor do IBS do respectivo item na NFe.
2P26-10 Acessar BD e verificar se valor da CBS do evento (tag: gConsumoComb/vCBS) é maior que o      Obrig.   1098 Rejeição: O valor da CBS do item não pode ser maior que o
        valor da CBS do item informado na NFe                                                                      valor da CBS do respectivo item na NFe.
2P28-10 Se unidade de consumo for igual a unidade da nota, acessar BD e verificar se a quantidade de Obrig.   1101 Rejeição: A quantidade do item a ser consumido não pode
        consumo do item informado (tag: gConsumoComb/qComb) é maior que a quantidade no item da                    ser maior que a quantidade do respectivo item na NFe
        NFe (tag: det/prod/qCom)                                                                                   (qCom)

8.8. Evento: Solicitação de Apropriação de Crédito para bens e serviços que dependem de atividade do
     adquirente
Função: Evento a ser gerado pelo adquirente para apropriação de crédito de bens e serviços que dependam da sua atividade
Modelo: NF-e modelo 55
Autor do Evento: Destinatário da NFe (adquirente).
Código do Tipo de Evento: 211150

8.8.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e211150_v1.00.xsd
#      Campo         Ele   Pai   Tipo Ocor. Tam. Descrição/Observação
P17    detEvento     G     P06        1-1        Detalhes do Evento
P18    versao        A     P17   N    1-1   2v2  Versão do leiaute do evento (P16)
P19    descEvento    E     P17   C    1-1   98   Descrição do evento: "Solicitação de Apropriação de Crédito para bens e serviços que dependem de atividade do adquirente"
P20    cOrgaoAutor   E     P17   N    1-1   2    Código da UF do emitente do Evento
P21    tpAutor       E     P17   N    1-1   1    Informar 2=Empresa destinatária.
                                                 Valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 8= Empresa sucessora; 9=Outros
                                                 Órgãos.
P22    verAplic      E     P17   N    1-1   1-20 Versão do aplicativo do autor do evento.
P23    gCredito      G     P17        1-990      Informações de crédito
P24    nitem         A     P23   N    1-1   1-3  Corresponde ao atributo “nItem” do elemento “det” do documento referenciado.
P25    vCredIBS      E     P23   N    1-1   13v2 Valor da solicitação de crédito a ser apropriado de IBS
P26    vCredCBS      E     P23   N    1-1   13v2 Valor da solicitação de crédito a ser apropriado de CBS

8.8.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.8.3. Validação das Regras de Negócio – Específicas
Serão aplicadas as regras de validação gerais apresentadas no item 5.8.4 do MOC e as regras de negócio específicas listadas a seguir.

   #    Regra de Validação                                                                             Aplic. Msg Descrição Erro
Banco de Dados: NF-e
2P21-10 Se tpAutor=2-Empresa Destinatário:                                                             Obrig.   575 Rejeição: Autor do evento diverge do destinatário da NF-e
            - CNPJ/CPF do Autor diverge do CNPJ/CPF do Destinatário da NF-e
2P24-10 Acessar BD e verificar se número do item do evento (tag: gCredito/nItem) informado existe na   Obrig. 1096 Rejeição: Número de item não existe na NFe
        NFe referenciada (tag: det/nItem)
2P25-10 Acessar BD e verificar se valor do crédito de IBS do evento (tag: gCredito/vCredIBS) é maior   Obrig. 1097 Rejeição: O valor do crédito de IBS do item não pode ser
        que o valor do IBS do item informado na NFe                                                                maior que o valor do IBS do respectivo item na NFe.
2P26-10 Acessar BD e verificar se valor do crédito de CBS do evento (tag: gCredito/vCredCBS) é maior   Obrig. 1098 Rejeição: O valor do crédito de CBS do item não pode ser
        que o valor da CBS do item informado na NFe                                                                maior que o valor da CBS do respectivo item na NFe.

8.9. Evento: Manifestação sobre Pedido de Transferência de Crédito de IBS em Operações de Sucessão
Função: Evento a ser gerado pela sucessora em relação às notas fiscais de transferência de crédito de outra sucessora da mesma empresa sucedida
  para informar aceite da transferência de crédito de IBS.
Autor: Empresa sucessora
Modelo: NF-e modelo 55
Código do Tipo de Evento: 212110

8.9.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e212110.00.xsd
#     Campo         Ele   Pai Tipo Ocor.   Tam. Descrição/Observação
P17   detEvento      G    P06      1-1          Detalhes do Evento
P18   versao         A    P17 N 1-1         2v2 Versão do leiaute do evento (P16)
P19   descEvento     E    P17 C 1-1         85 Descrição do evento: "Manifestação sobre Pedido de Transferência de Crédito de IBS em Operações de Sucessão"
P20   cOrgaoAutor    E    P17 N 1-1          2 Código da UF do emitente do Evento
P21   tpAutor        E    P17 N 1-1          1 Informar 8=Empresa sucessora.
                                                Valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 8= Empresa sucessora; 9=Outros Órgãos.
P22 verAplic        E     P17   N   1-1    1-20 Versão do aplicativo do autor do evento.
P23 indAceitacao    E     P17   N   1-1      1 Indicador de aceitação do valor de transferência para a empresa que emitiu a nota referenciada.
                                                Valores: 0=Não Aceite; 1=Aceite.

8.9.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.10. Evento: Manifestação sobre Pedido de Transferência de Crédito de CBS em Operações de Sucessão
Função: Evento a ser gerado pela sucessora em relação às notas fiscais de transferência de crédito de outra sucessora da mesma empresa sucedida
  para informar aceite da transferência de crédito de CBS.
Autor: Empresa sucessora

Modelo: NF-e modelo 55
Código do Tipo de Evento: 212120

8.10.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e212120_v1.00.xsd
#     Campo          Ele   Pai Tipo Ocor. Tam. Descrição/Observação
P17   detEvento       G    P06       1-1       Detalhes do Evento
P18   versao          A    P17 N     1-1   2v2 Versão do leiaute do evento (P16)
P19   descEvento      E    P17 C     1-1   82 Descrição do evento: "Manifestação sobre Pedido de Transferência de Crédito de CBS em Operações de Sucessão"
P20   cOrgaoAutor     E    P17 N     1-1    2 Código da UF do emitente do Evento
P21   tpAutor         E    P17 N     1-1    1 Informar 8=Empresa sucessora.
P22   verAplic        E    P17 N     1-1 1-20 Versão do aplicativo do autor do evento.
P23   indAceitacao    E    P17 N     1-1    1 Indicador de aceitação do valor de transferência para a empresa que emitiu a nota referenciada.
                                               Valores: 0=Não Aceite; 1=Aceite.

8.10.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.11. Evento: Manifestação do Fisco sobre Pedido de Transferência de Crédito de IBS em Operações de
    Sucessão
Função: Evento a ser gerado pelo fisco em relação às notas fiscais de transferência de crédito para informar aceite ou não aceite da transferência de
  crédito de IBS.
Autor: Fisco
Modelo: NF-e modelo 55
Código do Tipo de Evento: 412120

8.11.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e412120_v1.00.xsd
#     Campo            Ele   Pai Tipo Ocor. Tam. Descrição/Observação
P17   detEvento         G    P06       1-1       Detalhes do Evento
P18   versao            A    P17 N     1-1   2v2 Versão do leiaute do evento (P16)
P19   descEvento        E    P17 C     1-1    94 Descrição do evento: "Manifestação do Fisco sobre Pedido de Transferência de Crédito de IBS em Operações de Sucessão"
P20   cOrgaoAutor       E    P17 N     1-1    2 Código da UF do emitente do Evento
P21   tpAutor           E    P17 N     1-1    1 Informar 5=Fisco
P22   verAplic          E    P17 N     1-1 1-20 Versão do aplicativo do autor do evento.
P23   indDeferimento    E    P17 N     1-1    1 Indicador de aceitação do valor de transferência para a empresa que emitiu a nota referenciada.
                                                 Valores: 0=Não Aceite; 1=Aceite.
P24 cMotivo            E     P17 N     1-1    1 1–Falta de manifestação de todas as sucessoras; 2 – Outros.
P25 xMotivo            E     P17 C     1-1   500

8.11.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.12. Evento: Manifestação do Fisco sobre Pedido de Transferência de Crédito de CBS em Operações de
    Sucessão
Função: Evento a ser gerado pelo fisco em relação às notas fiscais de transferência de crédito para informar aceite ou não aceite da transferência de
  crédito de CBS.
Autor: Fisco
Modelo: NF-e modelo 55
Código do Tipo de Evento: 412130

8.12.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e412130_v1.00.xsd
#     Campo            Ele   Pai Tipo Ocor. Tam. Descrição/Observação
P17   detEvento         G    P06       1-1       Detalhes do Evento
P18   versao            A    P17 N     1-1   2v2 Versão do leiaute do evento (P16)
P19   descEvento        E    P17 C     1-1    94 Descrição do evento: "Manifestação do Fisco sobre Pedido de Transferência de Crédito de CBS em Operações de Sucessão"
P20   cOrgaoAutor       E    P17 N     1-1    2 Código da UF do emitente do Evento
P21   tpAutor           E    P17 N     1-1    1 Informar 5=Fisco.
P22   verAplic          E    P17 N     1-1 1-20 Versão do aplicativo do autor do evento.
P23   indDeferimento    E    P17 N     1-1    1 Indicador de aceitação do valor de transferência para a empresa que emitiu a nota referenciada.
                                                 Valores: 0=Não Aceite; 1=Aceite.
P24 cMotivo            E     P17 N     1-1    1 1 – Falta de manifestação de todas as sucessoras; 2 – Outros.
P25 xMotivo            E     P17 C     1-1   500

8.12.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.13. Evento: Cancelamento de Evento
Função: Permitir que o autor de um Evento já autorizado possa proceder o seu cancelamento.
Modelo: NF-e modelo 55
Autor do Evento: O mesmo Autor do Evento que está sendo cancelado.
Tipo de Evento (Código - Descrição): 110001 - Cancelamento de Evento

8.13.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML - parte genérica: envEventoNFe_v9.99.xsd
#     Campo            Ele    Pai   Tipo   Ocor.   Tam. Descrição/Observação
P04   evento            G     P01   xml    1-20      -  Evento, um lote pode conter até 20 eventos
P05   versao            A     P04    N      1-1     2v2 Versão do leiaute do evento
P06   infEvento         G     P04     -     1-1      -  Grupo de informações do registro do Evento
P07   Id               ID     P06    C      1-1     54 Identificador da TAG a ser assinada, formado por “ID” + tpEvento + Chave da NF-e + nSeqEvento
P08   cOrgao            E     P06    N      1-1      2  Informar o código da UF para este evento

#     Campo           Ele   Pai   Tipo     Ocor.   Tam. Descrição/Observação
P09   tpAmb            E    P06    N        1-1      1  Identificação do Ambiente: 1- Produção; 2- Homologação;
P10   CNPJ            CE    P06    N        1-1     14 CNPJ do autor do evento
P11   CPF             CE    P06    N        1-1     11 CPF do autor do evento
P12   chNFe            E    P06    N        1-1     44 Chave de Acesso da NF-e à qual o evento será vinculado
P13   dhEvento         E    P06    D        1-1      -  Data e hora do evento no formato AAAA-MM-DD-Thh:mm:ssTZD (UTC – Universal Coordinated Time)
P14   tpEvento         E    P06    N        1-1      6  Informar “110001”
P15   nSeqEvento       E    P06    N        1-1     1-2 Informar o número de sequência do Evento a ser cancelado
P16   verEvento        E    P06    N        1-1     2v2 Versão do grupo de detalhe do evento.

Schema XML - parte específica: e110001_v1.00.xsd
#     Campo           Ele   Pai   Tipo     Ocor.   Tam. Descrição/Observação
P17   detEvento        G    P06     -       1-1          Detalhes do Evento
P18   versao           A    P17    N        1-1     2v2 Versão do leiaute do evento (P16)
P19   descEvento       E    P17    C        1-1     22 Informar “Evento de Cancelamento”
P20   cOrgaoAutor      E    P17    N        1-1      2   Código da UF do autor do Evento
P22   verAplic         E    P17    C        1-1    1-20 Versão do aplicativo do autor do evento.
P23   tpEventoAut      E    P17    N        1-1      6   Código do evento autorizado a ser cancelado. Por este evento poderão ser cancelados todos os Eventos previstos nesta
                                                         NT, exceto o próprio Evento de Cancelamento (110001).
P24   nProtEvento      E    P17    N        1-1    15,17 Informar o número do Protocolo de Autorização do Evento a ser cancelado

8.13.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.13.3. Validação das Regras de Negócio – Específicas
Serão aplicadas as regras de validação gerais apresentadas no item 5.8.4 do MOC e as regras de negócio específicas listadas a seguir.

     #                                         Regra de Validação                                         Aplic. Msg                   Descrição Erro
P23-10     - Tipo do evento a ser cancelado não pode ser “110001”, “110111”, “110112”, ...                Obrig.  - Validação pelo esquema XML
*** Banco de Dados: Evento
1P06-10 Acesso BD de Eventos (Chave: Chave de Acesso, tpEventoAut, nSeqEvento):                           Obrig.   459   Rejeição: Cancelamento de Evento inexistente
           - Evento inexistente
1P10-10    - CNPJ/CPF do Autor do Evento de Cancelamento diverge do CNPJ/CPF do Autor do Evento a         Obrig. 1113 Rejeição: Autor do Evento de Cancelamento diverge do
             ser cancelado                                                                                            Autor do Evento a ser cancelado
1P20-10    - cOrgaoAutor do Evento de Cancelamento diverge do cOrgaoAutor do Evento a ser cancelado       Obrig. 1178 Rejeição: Órgão do Autor do Evento de Cancelamento
                                                                                                                      diverge do órgão do Autor do Evento a ser cancelado
1P24-10    - Número do Protocolo diverge                                                                  Obrig. 460 Rejeição: Protocolo do Evento difere do cadastrado

8.14. Evento: Importação em ALC/ZFM não convertida em isenção
Função: Permitir que o adquirente das regiões incentivadas (ALC/ZFM) informe que a tributação na importação não se converteu em isenção de um
  determinado item por não atender as condições da legislação.
Modelo: NF-e modelo 55
Autor do Evento: emitente da NFe (adquirente)
Código do Tipo de Evento: 112120

8.14.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e112120_v1.00.xsd
#     Campo                   Ele   Pai Tipo   Ocor.    Tam. Descrição/Observação
P17   detEvento                G    P06         1-1           Detalhes do Evento
P18   versao                   A    P17 N       1-1      2v2 Versão do leiaute do evento (P16)
P19   descEvento               E    P17 C       1-1      47 Descrição do evento: "Importação em ALC/ZFM não convertida em isenção"
P20   cOrgaoAutor              E    P17 N       1-1       2   Código do Órgão Autor do Evento. Informar o Código da UF para este Evento.
P21   tpAutor                  E    P17 N       1-1       1   Caso NF-e de Importação, informar 1=Empresa Emitente.
P22   verAplic                 E    P17 N       1-1     1-20 Versão do aplicativo do autor do evento.
P23   gConsumo                 G    P17        1-990          Informações por item da NF-e de importação
                                                              Nota: a quantidade de ocorrências não pode ser maior que a quantidade de itens da NF-e de aquisição.
P24   nItem                    A    P23   N     1-1      1-3 Corresponde ao atributo “nItem” do elemento “det” da NF-e de importação
P25   vIBS                     E    P23   N     1-1     13v2 Valor do IBS correspondente à quantidade que não atendeu aos requisitos para a conversão em isenção
P26   vCBS                     E    P23   N     1-1     13v2 Valor do CBS correspondente à quantidade que não atendeu aos requisitos para a conversão em isenção
P27   gControleEstoque         G    P23         1-1           Informações de quantidade de estoque influenciadas pelo evento
P28   qtde                     E    P27   N     1-1    11v0-4 Informar a quantidade que não atendeu os requisitos para a conversão em isenção
P29   unidade                  E    P27   C     1-1     1 - 6 Informar a unidade relativa ao campo gConsumo

8.14.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.15. Evento: Perecimento, perda, roubo ou furto durante o transporte contratado pelo adquirente
Função: Permitir ao adquirente informar quando uma aquisição for objeto de roubo, perda, furto ou perecimento.
Observação: O evento atual está relacionado aos bens que foram objeto de perecimento, perda, roubo ou furto em trânsito, em fornecimentos com
  frete FOB.
Modelo: NF-e modelo 55
Autor do Evento: Destinatário da NF-e em notas de saída
Código do Tipo de Evento: 211124

8.15.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e211124_v1.00.xsd
#     Campo              Ele   Pai Tipo Ocor.  Tam. Descrição/Observação
P17   detEvento           G    P06       1-1         Detalhes do Evento
P18   versao              A    P17 N     1-1    2v2 Versão do leiaute do evento (P16)
P19   descEvento          E    P17 C     1-1    82 Descrição do evento: “Perecimento, perda, roubo ou furto durante o transporte contratado pelo adquirente"
P20   cOrgaoAutor         E    P17 N     1-1     2   Código do Órgão Autor do Evento. Informar o Código da UF para este Evento.
P21   tpAutor             E    P17 N     1-1     1   Informar 2=Empresa destinatária.
                                                     Valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros Órgãos.
P22   verAplic           E     P17   N    1-1  1-20 Versão do aplicativo do autor do evento.
P23   gPerecimento       G     P17       1-990       Informações por item da Nota de Aquisição
P24   nItem              A     P23   N    1-1   1-3 Corresponde ao atributo “nItem” do elemento “det” do documento referenciado.
P25   vIBS               E     P23   N    1-1  13v2 Valor do IBS na Nota de Aquisição correspondente à quantidade que foi objeto de roubo, perda, furto ou perecimento
P26   vCBS               E     P23   N    1-1  13v2 Valor da CBS na Nota de Aquisição correspondente à quantidade que foi objeto de roubo, perda, furto ou perecimento
P27   gControleEstoque   G     P23        1-1        Informações de quantidade de estoque influenciadas pelo evento
P28   qPerecimento       E     P27   N    1-1 11v0-4 Informar a quantidade que foi objeto de roubo, perda, furto ou perecimento
P29   uPerecimento       E     P27   C    1-1   1-6 Informar a unidade relativa ao campo qPerecimento

8.15.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.16. Evento: Perecimento, perda, roubo ou furto durante o transporte contratado pelo fornecedor
Função: Permitir ao fornecedor informar quando um bem for objeto de roubo, perda, furto ou perecimento antes da entrega, durante o transporte
  contratado pelo fornecedor.
Observação: O evento atual está relacionado aos bens móveis materiais que foram objeto de perecimento, perda, roubo ou furto em trânsito, em
  fornecimentos com frete CIF.
Modelo: NF-e modelo 55
Autor do Evento: emitente da NF-e em notas de saída.
Código do Tipo de Evento: 112130

8.16.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e112130_v1.00.xsd
#     Campo              Ele   Pai Tipo Ocor.  Tam. Descrição/Observação
P17   detEvento           G    P06       1-1         Detalhes do Evento
P18   versao              A    P17 N     1-1    2v2 Versão do leiaute do evento (P16)
P19   descEvento          E    P17 C     1-1    82 Descrição do evento: "Perecimento, perda, roubo ou furto durante o transporte contratado pelo fornecedor"
P20   cOrgaoAutor         E    P17 N     1-1     2   Código do Órgão Autor do Evento. Informar o Código da UF para este Evento.
P21   tpAutor             E    P17 N     1-1     1   Informar 1=Empresa emitente.
                                                     Valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros Órgãos.
P22   verAplic           E     P17   N    1-1  1-20 Versão do aplicativo do autor do evento.
P23   gPerecimento       G     P17       1-990       Informações por item da Nota de Fornecimento
P24   nItem              A     P23   N    1-1   1-3 Corresponde ao atributo “nItem” do elemento “det” na nota de fornecimento
P25   vIBS               E     P23   N    1-1  13v2 Valor do IBS na Nota de Fornecimento correspondente à quantidade que foi objeto de roubo, perda, furto ou
                                                     perecimento.
P26 vCBS                 E     P23   N    1-1  13v2 Valor da CBS na Nota de Fornecimento correspondente à quantidade que foi objeto de roubo, perda, furto ou
                                                     perecimento.
P27   gControleEstoque   G     P23        1-1        Informações de quantidade de estoque influenciadas pelo evento
P28   qPerecimento       E     P27   N    1-1 11v0-4 Informar a quantidade que foi objeto de roubo, perda, furto ou perecimento
P29   uPerecimento       E     P27   C    1-1   1-6 Informar a unidade relativa ao campo qPerecimento
P30   Sequência XML      G     P27        1-1        Informações do crédito a ser estornado de IBS/CBS referente às aquisições para este item
P31   vIBS               E     P30   N    1-1  13v2 Valor do crédito IBS referente às aquisições a ser estornado correspondente à quantidade que foi objeto de roubo,
                                                     perda, furto ou perecimento
P32 vCBS                 E     P30   N    1-1  13v2 Valor do crédito CBS referente às aquisições a ser estornado correspondente à quantidade que foi objeto de roubo,
                                                     perda, furto ou perecimento

8.16.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.17. Evento: Fornecimento não realizado com pagamento antecipado
Função: Permitir ao fornecedor informar que um pagamento antecipado não teve o respectivo fornecimento realizado.
Modelo: NF-e modelo 55
Autor do Evento: emitente da NF-e de nota de débito do tipo 06 = Pagamento antecipado

Código do Tipo de Evento: 112140

8.17.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e112140_v1.00.xsd
#     Campo            El   Pai Tipo Ocor.   Tam. Descrição/Observação
                       e
P17   detEvento        G    P06        1-1        Detalhes do Evento
P18   versao           A    P17   N    1-1    2v2 Versão do leiaute do evento (P16)
P19   descEvento       E    P17   C    1-1    51  Descrição do evento: "Fornecimento não realizado com pagamento antecipado"
P20   cOrgaoAutor      E    P17   N    1-1     2  Código do Órgão Autor do Evento. Informar o Código da UF para este Evento.
P21   tpAutor          E    P17   N    1-1     1  Informar 1=Empresa Emitente
                                                  Valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros Órgãos.
P22   verAplic          E P17     N    1-1  1-20 Versão do aplicativo do autor do evento.
P23   gItemNaoFornecido G P17         1-990       Informações por item da Nota de Pagamento antecipado
P24   nItem             A P23     N    1-1   1-3 Corresponde ao atributo “nItem” do elemento “det” do documento referenciado.
P25   vIBS              E P23     N    1-1  13v2 Valor do IBS na nota de débito de pagamento antecipado correspondente à quantidade que não foi fornecida
P26   vCBS              E P23     N    1-1  13v2 Valor da CBS na nota de débito de pagamento antecipado correspondente à quantidade que não foi fornecida
P27   gControleEstoque  G P23          1-1        Informações de quantidade de estoque influenciadas pelo evento
P28   qNaoFornecida     E P27     N    1-1 11v0-4 Informar a quantidade que não foi fornecida e teve o imposto antecipado
P29   uNaoFornecida     E P27     C    1-1   1-6 Informar a unidade relativa ao campo qNaoFornecida

8.17.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.

8.18. Evento: Atualização da Data de Previsão de Entrega
Função: Permitir ao fornecedor atualizar a data da previsão de entrega ou disponibilização do bem ao adquirente, de forma a remover o débito do
  mês em que foi previsto inicialmente.
Modelo: NF-e modelo 55
Autor do Evento: emitente da NF-e
Código do Tipo de Evento: 112150

8.18.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e112150_v1.00.xsd
#     Campo            Ele   Pai Tipo Ocor.   Tam. Descrição/Observação
P17   detEvento         G    P06       1-1         Detalhes do Evento
P18   versao            A    P17 N     1-1     2v2 Versão do leiaute do evento (P16)
P19   descEvento        E    P17 C     1-1     42 Descrição do evento: "Atualização da Data de Previsão de Entrega"
P20   cOrgaoAutor       E    P17 N     1-1      2  Código do Órgão Autor do Evento. Informar o Código da UF para este Evento.
P21   tpAutor           E    P17 N     1-1      1  Informar 1=Empresa Emitente
                                                   Valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros Órgãos.
P22 verAplic            E    P17   N   1-1    1-20 Versão do aplicativo do autor do evento.
P23 dPrevEntrega        E    P17   D   1-1     10 Data da previsão de entrega ou disponibilização do bem. Formato: “AAAA-MM-DD”.

8.18.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado
no item 5.8.2 do MOC.
```

## 9. DANFE

```text
Alterações no DANFE para exibir informações relativas aos novos tributos estão em estudo, e serão publicadas em uma nova versão desta Nota
Técnica.
```

## ANEXO I - NCM DO IMPOSTO SELETIVO

```text
Tabela a ser publicada.
```

## ANEXO II - CÓDIGO DE CLASSIFICAÇÃO TRIBUTÁRIA DO IMPOSTO SELETIVO (cClassTribIS)

```text
Tabela a ser publicada.
```

## ANEXO III - CÓDIGO DE CLASSIFICAÇÃO TRIBUTÁRIA DO IBS E DA CBS (cClassTrib)

```text
Tabela publicada na aba “Documentos”, opção “Diversos” do Portal Nacional da Nota Fiscal Eletrônica
```

## ANEXO IV - CÓDIGO DE CLASSIFICAÇÃO DO CRÉDITO PRESUMIDO (cCredPres)

```text
Tabela publicada na aba “Documentos”, opção “Diversos” do Portal Nacional da Nota Fiscal Eletrônica
```
