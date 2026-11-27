---
titulo: "Nota Técnica NF-e/NFC-e nº 2026.006, versão 1.01, de 30 de outubro de 2026 (Vinculação com a Transação de Pagamento do DF-e, Split Payment)"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil / ENCAT - CONFAZ"
tipo: "Nota Técnica"
numero: "2026.006"
data: "2026-10-30"
ano: "2026"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS", "Split Payment"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY="
ementa: "Divulga a especificação técnica para a vinculação entre a NF-e ou a NFC-e e a transação financeira sujeita ao split payment, com o grupo de informações da vinculação e o evento de vinculação da transação de pagamento."
data_consulta: "2026-11-27"
versao_texto: "Versão 1.01 (PDF oficial, 30/10/2026)"
---

# Nota Técnica NF-e/NFC-e nº 2026.006, versão 1.01, de 30 de outubro de 2026 (Vinculação com a Transação de Pagamento do DF-e, Split Payment)

> **Nota editorial.** Texto extraído da camada de texto do PDF oficial da Nota Técnica 2026.006, versão 1.01, divulgado no Portal Nacional da NF-e (10 páginas), consultado em 27/11/2026. A data do documento (30/10/2026) é a de publicação da versão, lida na lista de Notas Técnicas do portal. Versão aprovada ou ratificada pelo Ato Técnico Conjunto Sufis/CGIBS nº 10/2026 (`reguladores/rfb/outros-atos/2026/ato-154369-10-2026.md`). Foram removidos a capa, o sumário, os cabeçalhos e rodapés repetidos e a numeração de página. Os 6 títulos de primeiro nível do sumário viraram seções e o texto de cada uma, com os quadros e os leiautes, ficou em bloco de texto que mantém as colunas do PDF. Figuras e imagens do PDF não foram convertidas. Em caso de dúvida, prevalece o PDF. O portal só entrega o PDF com cookie de sessão; o link da fonte é a página de lista de Notas Técnicas, onde a versão consta como "Publicada em 30/10/2026". Os campos têm caráter preparatório: o split payment está previsto para 2027 e não há exigência de preenchimento em produção em 2026 (item 'Histórico de Alterações / Cronograma' do PDF). Complementa a NT 2025.002 (`reforma-tributaria/documentos-fiscais-eletronicos/nota-tecnica-nfe-2025-002-v1-53-leiaute-ibs-cbs-is.md`).

## Histórico de Alterações / Cronograma

```text
    Versão                         Histórico de atualizações                   Implantação     Implantação
                                                                              Homologação       Produção
     1.00    Criação do grupo YC. Informações da vinculação da transação de    05/10/2026      03/11/2026
                 pagamento do DF-e (Split Payment) e regras de validação
                 relacionadas.

             Criação do Evento de Informações da Vinculação da Transação de
                 Pagamento do DF-e (110300).
     1.01    Alteração das datas de implantação em Homologação e Produção     Até 26/10/2026   16/11/2026

A implantação do split payment está prevista para ocorrer a partir de 2027. Dessa forma, os
campos mencionados nesta Nota Técnica têm caráter preparatório e visam permitir que os
sistemas das administrações tributárias, emissores de documentos fiscais e demais atores
envolvidos possam planejar, desenvolver e testar, com a devida antecedência, as adaptações
necessárias.

Considerações importantes:
•     Não há exigência de preenchimento ou uso dos campos de split payment em 2026 no
      ambiente de produção;
•     A ativação efetiva desses campos ocorrerá somente quando o mecanismo de split
      payment entrar em vigência, prevista para 2027;
•     Orientações adicionais e cronogramas serão divulgados oportunamente por meio dos
      canais oficiais do CGIBS e da RFB.
•     O preenchimento do grupo criado nesta Nota Técnica para Vinculação da Transação de
      Pagamento não exclui a obrigação de preenchimento dos campos dos grupos “YA.
      Informações de Pagamento” e “YB. Informações do Intermediador da Transação”, exigidos
      conforme legislação tributária estadual, mesmo que os grupos estejam preenchidos com
      os mesmos códigos do tipo de pagamento. Além disso, o Evento criado nesta Nota
      Técnica não substitui o Evento “Conciliação Financeira – ECONF” instituído pela Nota
      Técnica 2024.002, conforme legislação tributária estadual.
```

## 1. Introdução

```text
A vinculação entre DF-e e transação financeira sujeita ao split payment é estritamente
necessária para a correta apuração dos débitos do fornecedor e concessão de créditos ao
adquirente.

No split payment, há duas formas de o contribuinte indicar a vinculação entre o documento
fiscal e a transação financeira sujeita ao split payment:
  i.    transmitindo a chave do documento fiscal ao prestador de serviço de pagamento, no
        início da transação financeira;
  ii.   informando os dados da transação financeira em campos ou em Evento de DF-e.

Esta Nota Técnica detalha a forma (ii), de vinculação por meio da inserção de dados da
transação financeira em campos de documento fiscal ou Evento.

Atenção: O vínculo indicado pelo contribuinte não necessariamente representa um
   pagamento efetuado e liquidado. Indica uma expectativa de pagamento que pode ou não
   se concretizar. Por exemplo: um boleto pode ser emitido e não pago.

Nas transações sujeitas ao procedimento padrão do split payment e originadas por
fornecedor/recebedor, a vinculação se faz necessária antes mesmo da liquidação financeira,
com o propósito de viabilizar o split payment superinteligente. Cumpre destacar que, quanto
mais tempo o fornecedor/recebedor demorar para reportar o vínculo entre DF-e e transação
financeira, menores serão as chances de o split superinteligente ser executado. Em caso de
impossibilidade de execução do split superinteligente, será executado o split inteligente offline,
com posterior devolução de valores retidos a maior no prazo de 3 (três) dias úteis.

São exemplos, não exaustivos, de possíveis cenários de vinculação por meio da inserção de
dados da transação financeira em campos ou em Evento de DF-e:

Ex. 1. O fornecedor emite um boleto para o adquirente antes da emissão do DF-e. Uma vez
que o boleto foi emitido sem chave de DF-e, a vinculação fica inicialmente pendente. Após a
emissão do boleto, o fornecedor emite o DF-e preenchendo os campos relativos à transação
financeira, viabilizando assim a vinculação.

Ex. 2. O fornecedor emite um DF-e. Em seguida, o fornecedor emite QR code Pix dinâmico
para a empresa adquirente, informando valores de IBS e CBS, mas sem a chave do DF-e
previamente emitido (nos termos do § 2º-A do Art. 32 da LC 214/2025, com redação dada
pela LC 227/2026). O vínculo fica inicialmente pendente, em razão da ausência da chave DF-
e na transação de pagamento. Para finalmente efetivar a vinculação, o fornecedor emite
Evento atrelado ao DF-e, com os dados do Pix dinâmico.

Ex. 3. O fornecedor emite um DF-e antes do início da transação financeira. A empresa
adquirente efetua o pagamento via TED informando a chave do DF-e, porém comete um erro

neste preenchimento, o que impede a correta vinculação entre transação financeira e DF-e.
A fim de resolver o problema, o fornecedor emite um Evento atrelado ao DF-e com os dados
da transação financeira.

NFCe/NFe – Vinculação com a Transação de Pagamento do DF-e
```

## 2. Leiaute da NF-e (Modelo 55 e 65)

```text
      YC. Informações da Vinculação com a Transação de Pagamento do DF-e (Split Payment)

Este grupo de informações deverá ser informado sempre que a transação de pagamento for iniciada antes da emissão do DF-e. Exemplos: boleto gerado
antes da emissão do DF-e; QR Code dinâmico Pix gerado antes da emissão do DF-e. Neste caso, o DF-e deverá reportar os dados das transações
financeiras previamente iniciadas, ainda que estejam pendentes de efetivo pagamento e liquidação.

  #       ID  Campo             Descrição                                            Ele   Pai    Tipo Ocor. Tam.                          Observação
398.50   YC01 gPgtoVinc         Grupo de informações da Vinculação com a              G    A01      -   0-1    -
                                Transação de Pagamento
398.51   YC02 gPgto             Dados de cada pagamento previsto para o DF-e         G     YC01    -   1-99    -
398.52   YC03 nPag              Atributo numerador único de cada ocorrência de       A     YC02    N    1-1    3    Observação: O schema impede nPag duplicado
                                pagamento
398.53   YC04 idTransacao       Atributo identificador da transação financeira, de   A     YC02    C    1-1   2-35 Observação: O schema impede idTransacao duplicado
                                acordo com a transação de pagamento
398.54   YC05 tpMeioPgto        Código do meio de pagamento                          E     YC02    N    1-1    2    Observação: consultar Tabela Nacional de Códigos de Meios
                                                                                                                        de Pagamento (Informe Técnico 2026.001 dos DF-e).
398.55   YC06 CNPJReceb         CNPJ completo do recebedor do pagamento              E     YC02    C    1-1   14    Indicar o CNPJ responsável pelo recebimento dos valores do
                                (fornecedor, plataforma, ou outra entidade que                                      adquirente na transação de pagamento. É possível que o
                                receba o pagamento do adquirente)                                                   CNPJ do recebedor seja diferente do CNPJ do fornecedor
                                                                                                                    constante no documento fiscal.
398.56   YC07 CNPJBasePSP       CNPJ base da instituição financeira ou de            E     YC02    C    1-1    8
                                pagamento utilizada pelo recebedor do pagamento
                                (fornecedor, plataforma, ou outra entidade que
                                receba o pagamento do adquirente)
```

## 3. Regras de Validação

```text
Campo Modelo                                    Regra de Validação                                     Aplic. Msg                        Descrição Erro
YC03-10 55/65 Se informado grupo de Vinculação com a Transação de Pagamento (grupo: gPgtoVinc):        Obrig. 215 Rejeição: Falha no esquema XML
               - Atributo “nPag” duplicado                                                                        Observação: Validação realizada pelo Schema XML
YC04-20 55/65 Se informado grupo de Vinculação com a Transação de Pagamento (grupo: gPgtoVinc):        Obrig. 215 Rejeição: Falha no esquema XML
               - Atributo “idTransacao” duplicado                                                                 Observação: Validação realizada pelo Schema XML

Campo Modelo                                  Regra de Validação                                  Aplic. Msg                       Descrição Erro
YC05-10 55/65 Se informado grupo de Vinculação com a Transação de Pagamento (grupo: gPgtoVinc):   Obrig 1273 Rejeição: Meio de pagamento inválido [nPag: 999]
               - Para cada ocorrência de pagamento vinculado (grupo: gPgto):
                  - Código do meio de pagamento inválido (tag: tpMeioPgto)
              Observação: consultar Tabela Nacional de Códigos de Meios de Pagamento (Informe
                 Técnico 2026.001 dos DF-e).
YC06-10 55/65     - CNPJ do recebedor do pagamento inválido (tag: CNPJReceb)                      Obrig 1274 Rejeição: CNPJ do recebedor do pagamento inválido [nPag:
                                                                                                             999]
```

## 4. Evento de Vinculação da Transação de Pagamento no DF-e

```text
    •   Função: Este Evento deverá ser gerado pelo emitente do DF-e sempre que se desejar vincular uma ou mais transações financeiras a um
        documento fiscal previamente autorizado. Obs.: É possível que a transação financeira vinculada esteja em situação iniciada, ainda pendente de
        pagamento e/ou liquidação (ex. boleto emitido ou QR code Pix gerado).
    •   Autor: Emitente da NFe/NFCe
    •   Modelo: NF-e modelo 55/65
    •   Código do Tipo de Evento: 110300

4.1.1. Leiaute Mensagem de Entrada
Estrutura XML da parte específica do Evento, a ser inserida na tag detEvento (P17) da Parte Geral do Web Service de Registro de Eventos especificada
na seção 5.8 do MOC.

Schema XML: envEventoNFe_v9.99.xsd
Schema XML - parte específica: e110300_v1.00.xsd
  # Campo                         Ele   Pai Tipo   Ocor.   Tam. Descrição/Observação
 P17 detEvento                     G    P06   -     1-1      -  Detalhes do Evento
 P18 versao                        A    P17  N      1-1     2v2 Versão do leiaute do Evento (P16)
 P19 descEvento                    E    P17  C      1-1     20 Descrição do Evento: “Vinculação Pagamento”
 P20 cOrgaoAutor                   E    P17  N      1-1      2  Código do Órgão Autor do Evento.
 P21 tpAutor                       E    P17  N      1-1      1  Informar: 1=Empresa Emitente
                                                                Valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros Órgãos.
 P22 verAplic                     E     P17   N     1-1    1-20 Versão do aplicativo do autor do Evento
 P23 nProt                        E     P17   N     1-1     15 Número do protocolo de autorização do DF-e
 P24 gPgto                        G     P17   -     1-1      -  Dados de cada pagamento previsto para o DF-e
 P25 idTransacao                  A     P24   C     1-1    2-35 Atributo Identificador da transação financeira, de acordo com a transação de pagamento.
 P26 tpMeioPgto                   E     P24   N     1-1      2  Código do meio de pagamento.
                                                                Observação: consultar Tabela Nacional de Códigos de Meios de Pagamento (Informe Técnico 2026.001 dos
                                                                    DF-e).
 P27 CNPJReceb                    E     P24   C     1-1     14 CNPJ completo do recebedor do pagamento (fornecedor, plataforma, ou outra entidade que receba o
                                                                pagamento do adquirente).
                                                                Observação: indicar o CNPJ responsável pelo recebimento dos valores do adquirente na transação de
                                                                    pagamento. É possível que o CNPJ do recebedor seja diferente do CNPJ do fornecedor constante no
                                                                    documento fiscal.
 P28 CNPJBasePSP                  E     P24   C     1-1      8  CNPJ base da instituição financeira ou de pagamento utilizada pelo recebedor do pagamento (fornecedor,
                                                                plataforma, ou outra entidade que receba o pagamento do adquirente).

4.1.2. Leiaute Mensagem de Retorno
Estrutura XML com a mensagem do resultado da transmissão, conforme retorno do Web Service de Registro de Eventos – Parte Geral, especificado no
item 5.8.2 do MOC.

4.1.3. Validação das Regras de Negócio – Específicas
Serão aplicadas as regras de validação gerais apresentadas no item 5.8.4 do MOC e as regras de negócio específicas listadas a seguir.

   #                                       Regra de Validação                              Aplic. Msg                        Descrição Erro
P21-10   Tipo do Autor difere de “1=Empresa Emitente”                                      Obrig. 466 Rejeição: Evento com Tipo de Autor incompatível
P26-10   Código do meio de pagamento inválido (tag: tpMeioPgto)                            Obrig 1273 Rejeição: Meio de pagamento inválido
         Observação: consultar Tabela Nacional de Códigos de Meios de Pagamento (Informe
            Técnico 2026.001 dos DF-e).
P27-10   CNPJ do recebedor do pagamento inválido (tag: CNPJReceb)                          Obrig. 1274 Rejeição: CNPJ do recebedor do pagamento inválido
```

## 5. Cancelamento do Evento

```text
O cancelamento do Evento de Vinculação da Transação de Pagamento no DF-e será feito por meio do Evento de cancelamento genérico 110001 -
Cancelamento de Evento, especificado na NT 2025.002 - RTC.
```
