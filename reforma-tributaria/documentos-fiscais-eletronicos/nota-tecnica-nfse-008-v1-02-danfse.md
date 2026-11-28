---
titulo: "Nota Técnica SE/CGNFS-e nº 008, versão 1.02, de 14 de julho de 2026 (Especificações técnicas do DANFSe)"
esfera: "Federal"
orgao: "Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço Eletrônica de Padrão Nacional (SE/CGNFS-e)"
tipo: "Nota Técnica SE/CGNFS-e"
numero: "008"
data: "2026-07-14"
ano: "2026"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS", "ISSQN"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/nt-008-se-cgnfse-danfse-20260714-v1-02.pdf"
ementa: "Especifica o DANFSe (Documento Auxiliar da Nota Fiscal de Serviço Eletrônica) da NFS-e de padrão nacional, com os campos e o formulário, incluindo as informações de IBS e CBS."
data_consulta: "2026-11-27"
versao_texto: "Versão 1.02 (PDF oficial, 14/07/2026)"
---

# Nota Técnica SE/CGNFS-e nº 008, versão 1.02, de 14 de julho de 2026 (Especificações técnicas do DANFSe)

> **Nota editorial.** Texto extraído da camada de texto do PDF oficial da Nota Técnica 008, versão 1.02, divulgado no Portal da NFS-e (gov.br/nfse) (26 páginas), consultado em 27/11/2026. A data do documento (14/07/2026) é a de publicação da versão, lida na capa do PDF. Versão aprovada ou ratificada pelo Ato Técnico Conjunto RFB/CGIBS nº 1/2026 (`reguladores/rfb/outros-atos/2026/ato-152654-1-2026.md`). Foram removidos a capa, o sumário, os cabeçalhos e rodapés repetidos e a numeração de página. Os 5 títulos de primeiro nível do sumário viraram seções e o texto de cada uma, com os quadros e os leiautes, ficou em bloco de texto que mantém as colunas do PDF. O texto que antecede esses títulos e não consta do sumário ficou em seção própria (Lista de Abreviaturas e Siglas). Figuras e imagens do PDF não foram convertidas. Em caso de dúvida, prevalece o PDF.

## Lista de Abreviaturas e Siglas

```text
API – Application Programming Interface (Interface de Programação de Aplicações)
ATM – Administração Tributária Municipal
BC – Base de Cálculo
BM – Benefício Municipal
CBS – Contribuição Social sobre Bens e Serviços
CEP – Código de Endereçamento Postal
cClassTrib – Código de Classificação Tributária
CNPJ – Cadastro Nacional da Pessoa Jurídica
COFINS – Contribuição para o Financiamento da Seguridade Social
CPF – Cadastro de Pessoas Físicas
CST – Código de Situação Tributária
DANFSe – Documento Auxiliar da Nota Fiscal de Serviço Eletrônica
DPS – Declaração de Prestação de Serviços
ERP – Enterprise Resource Planning (Sistema de Planejamento dos Recursos da Empresa)
IBGE – Instituto Brasileiro de Geografia e Estatística
IBS – Imposto sobre Bens e Serviços
IRRF – Imposto de Renda Retido na Fonte
ISSQN – Imposto Sobre Serviços de Qualquer Natureza
NBS – Nomenclatura Brasileira de Serviços
NIF – Número de Identificação Fiscal
NFS-e – Nota Fiscal de Serviço Eletrônica Nacional
PIS – Programa de Integração Social
SN – Simples Nacional
UF – Unidade da Federação
XML – eXtensible Markup Language (Linguagem de Marcação Extensível)
```

## HISTÓRICO DE VERSÕES

```text
Versão   Data         Alterações de Versão

1.0

1.01     30/06/2026 Alteração da data de suspensão da API de geração do DANFSe.

1.02     14/07/2026 Alteração da data de suspensão da API de geração do DANFSe;
                    Quantidade de caracteres dos campos; Ajuste no tratamento dos campos
                    vPis, vCofins e tpRetPisCofins; Outras correções pontuais.
```

## Resumo do Documento

```text
Descrição:      Este documento trata das especificações técnicas do DANFSe.

Destinação:     Empresas e desenvolvedoras de softwares de emissão de NFS-e, ERPs e sistemas
                fiscais.
```

## 1. Introdução

```text
       Este documento é parte integrante da Documentação Técnica da Nota Fiscal de Serviço
Eletrônica – NFS-e e tem por objetivo a especificação técnica do Documento Auxiliar da Nota Fiscal
de Serviço Eletrônica – DANFSe.
       Esta nota técnica servirá de base para a geração do DANFSe por meios de softwares de
emissão de NFS-e, ERPs e sistemas fiscais, motivo pelo qual, a API de geração do DANFSe
(https://adn.nfse.gov.br/danfse/docs/index.html) será sobrestada (suspensa) na data de 03 de
agosto de 2026.
       Cumpre esclarecer que, em relação às operações que serão formalizadas por NFS-e e que são
enquadradas como novos fatos geradores, no campo de incidência do IBS e da CBS, mas que não
eram operações formalizadas por documento fiscal (seção “3.a)” da Nota Técnica nº 007, de 7 de
fevereiro de 2026), será publicada uma nota técnica específica com as especificações do DANFSe
para essas operações.
```

## 2. DANFSe

```text
       O DANFSe é o documento auxiliar da NFS-e impresso em papel com os objetivos de:

           a) Facilitar a consulta resumida dos dados da NFS-e, provendo a necessidade de
              representações impressas previstas na legislação; e
           b) Auxiliar os processos administrativos e financeiros do destinatário não credenciado
              como emissor de NFS-e.

       O DANFSe será impresso:

           a) Em condições normais, em qualquer tipo de papel, exceto papel jornal; e
           b) Em uma única via, salvo quando houver disposição expressa em outro sentido.

       O DANFSe emitido para representar NFS-e gerada para fins de teste em ambiente de produção
restrita (tag <tpAmb> = 2 – Homologação) sempre deverá conter a expressão “NFS-e SEM
VALIDADE JURÍDICA” no cabeçalho, abaixo do título “Documento Auxiliar da NFS-e”,
observando o descrito no item 2.4.3.
       Os “TOTAIS APROXIMADOS DE TRIBUTOS” calculados pela empresa, correspondente a
totalidade dos tributos federais, estaduais e municipais, conforme disposto na Lei nº 12.741/2012,
cuja incidência influa na formação do respectivo preço de venda, constará no campo de “Informações
Complementares”.

   2.1.        Campos do DANFSe
       Os campos do DANFSe deverão representar o conteúdo das respectivas TAG XML da NFS-e
emitida. Não poderão ser impressas informações que não constem do arquivo da NFS-e.
       Em alguns casos, o conteúdo dos campos poderá ser impresso em mais de uma linha desde
que a leitura possa ser feita de forma clara.
       O item 2.4.5 deste manual traz a sugestão de tamanhos a serem seguidos para cada campo,
que garantem a legibilidade prevista na legislação. Embora os tamanhos descritos no item 2.4.5 não
sejam obrigatórios, o DANFSe deverá ser impresso conforme o modelo permitido (conforme o item
2.2.4) e utilizando-se os tamanhos mínimos de fonte descritos no item 2.4 e seguintes.
       No mesmo sentido, a quantidade de caracteres para cada campo sugerida no item 2.4.5 não
tem caráter obrigatório, podendo-se utilizar quantidade diversa, acrescido de reticências (...), quando
o campo não suportar a totalidade de caracteres do texto a ser inserido.

   2.1.1       Chave de Acesso
       A chave de acesso será impressa em único bloco contendo 50 dígitos.

   2.1.2       Dados de Identificação da NFS-e
       Deverá conter a identificação da NFS-e, composta, além do cabeçalho descrito no item 2.4.3,
por no mínimo:

           •   Chave de Acesso da NFS-e;
           •   Número da NFS-e;
           •   Competência da NFS-e;
           •   Data e Hora da emissão da NFS-e;
           •   Número da DPS;
           •   Série da DPS;
           •   Data e Hora da emissão da DPS;
           •   Emitente da NFS-e;
           •   Situação da NFS-e; e
           •   Finalidade.

   2.1.3       Dados do Prestador/Fornecedor
      Deverá conter a identificação do prestador/fornecedor do serviço/operação, composta no
mínimo por:

           •   CNPJ / CPF / NIF;
           •   Indicador Municipal (Inscrição);
           •   Telefone;
           •   Nome / Nome empresarial;
           •   Município / Sigla UF;
           •   Código IBGE / CEP
           •   Endereço (logradouro, número, complemento e bairro)*;
           •   Email*;
           •   Informação sobre o Simples Nacional da Data de Competência;
           •   Regime de Apuração Tributária pelo SN; e

      * Ver nota 1.

   2.1.4       Dados do Tomador/Adquirente
      Deverá conter a identificação do tomador/adquirente do serviço/operação, composta no
mínimo por:

           •   CNPJ / CPF / NIF;
           •   Indicador Municipal (Inscrição);
           •   Telefone;
           •   Nome / Nome empresarial;
           •   Município / Sigla UF;
           •   Código IBGE / CEP
           •   Endereço (logradouro, número, complemento e bairro)*;
           •   eEmail*;

      * Ver nota 1.

   2.1.5       Dados do Destinatário da Operação
      Deverá conter a identificação do destinatário da operação, composta no mínimo por:

           •   CNPJ / CPF / NIF;

        •   Telefone;
        •   Nome / Nome empresarial;
        •   Município / Sigla UF;
        •   Código IBGE / CEP
        •   Endereço (logradouro, número, complemento e bairro)*; e
        •   Email*;

   * Ver nota 1.

2.1.6       Dados do Intermediário da Operação
   Deverá conter a identificação do intermediário da operação, composta no mínimo por:

        •   CNPJ / CPF / NIF;
        •   Indicador Municipal (Inscrição);
        •   Telefone;
        •   Nome / Nome empresarial;
        •   Município / Sigla UF;
        •   Código IBGE / CEP
        •   Endereço (logradouro, número, complemento e bairro)*; e
        •   Email*;

   * Ver nota 1.

2.1.7       Dados do Serviço Prestado
   Deverá conter a identificação do serviço prestado, composta no mínimo por:

        •   Código de Tributação Nacional / Municipal;
        •   Código da NBS;
        •   Local da Prestação / Sigla UF / País;
        •   Descrição do Código de Tributação Nacional / Municipal; e
        •   Descrição do Serviço;

2.1.8       Dados da Tributação Municipal (ISSQN)
   Deverá conter os dados da tributação municipal, compostos no mínimo por:

        •   Tipo de Tributação do ISSQN;
        •   Município / Sigla UF / País de Incidência do ISSQN;

         •   Regime Especial de Tributação do ISSQN*;
         •   Tipo de Imunidade do ISSQN*;
         •   Suspensão da Exigibilidade do ISSQN*;
         •   Número Processo Suspensão*;
         •   Benefício Municipal*;
         •   Cálculo do BM*;
         •   Total Deduções/Reduções*;
         •   Desconto Incondicionado*;
         •   BC ISSQN;
         •   Alíquota Aplicada;
         •   Retenção do ISSQN; e
         •   ISSQN Apurado;

   * Ver nota 5.

2.1.9        Dados da Tributação Federal (Exceto CBS)
   Deverá conter os dados da tributação federal, compostos no mínimo por:

         •   IRRF;
         •   Contribuição Previdenciária – Retida;
         •   Contribuições Sociais – Retidas;
         •   PIS – Débito Apuração Própria*;
         •   COFINS – Débito Apuração Própria*; e
         •   Descrição das Contribuições Sociais – Retidas*;

   * Ver nota 6.

2.1.10       Dados da Tributação IBS/CBS
   Deverá conter os dados da tributação do IBS/CBS, compostos por:

         •   Código da Situação Tributária – CST / Classificação da Situação Tributária –
             cClassTrib;
         •   Indicador de Operação / Código IBGE do município de Incidência / Município de
             Incidência / Sigla UF;
         •   Exclusões e Reduções da Base de Cálculo;
         •   Base de Cálculo Após Exclusões e Reduções;

            •   Reduções da Alíquota do IBS / Reduções da Alíquota da CBS;
            •   Alíquota do IBS Estadual / IBS Municipal;
            •   Alíquota Efetiva do IBS Municipal;
            •   Valor Apurado do IBS Municipal;
            •   Alíquota Efetiva do IBS Estadual;
            •   Valor Apurado do IBS Estadual;
            •   Valor Total Apurado do IBS;
            •   Alíquota da CBS;
            •   Alíquota Efetiva da CBS; e
            •   Valor Total Apurado da CBS;

   2.1.11       Dados do Valor Total da NFS-E
       Deverá conter os dados do valor total da NFS-e, compostos por:

            •   Valor da Operação / Serviço;
            •   Desconto Incondicionado;
            •   Desconto Condicionado;
            •   Total das Retenções (ISSQN / Federais);
            •   Valor Líquido da NFS-e;
            •   Total do IBS/CBS; e
            •   Valor Líquido da NFSe-e + IBS/CBS;

   2.1.12       Dados de Informações Complementares
       Deverá conter os dados de informações complementares da NFS-e, compostos, quando
preenchidos, entre outros, por:

            •   Dados do bloco Imóvel;
            •   Dados do bloco Obra;
            •   Dados do bloco Evento;
            •   Dados do bloco Informações Complementares;
            •   Informações Complementares de uso da Administração Municipal; e
            •   Totais Aproximados dos Tributos;

   2.1.13       Canhoto (Opcional)
       Deverá conter os seguintes campos:

            •   Data de cientificação;
            •   Identificação e Assinatura;
            •   Nº da NFS-e / Chave da NFS-e;
   2.2.         Formulário
       Para a impressão do DANFSe poderá ser utilizado qualquer tipo de papel, com exceção de
papel jornal, desde que seja garantido o contraste necessário para assegurar leitura do código de barras
bidimensional (QR Code) sem problemas.
       O DANFSe deverá ser impresso, obrigatoriamente, em uma única página.

   2.2.1        Tamanho do Papel
       A impressão do DANFSe deverá ser efetuada em modo retrato, utilizando-se formulários de
tamanho mínimo A4 (210 x 297mm).

   2.2.2        Margem Lateral no Formulário
       As margens entre o corpo impresso do DANFSe e o final do formulário deverão ter, no
mínimo, 0,15cm e no máximo 0,20cm em cada lateral (inclusive nas margens superior e inferior).

   2.2.3        Espessura das Linhas e Sombreamento
       As linhas divisórias dos blocos de conteúdo do DANFSe deverão ter 0,5 (meio) ponto de
espessura. Além disso, página deverá ter borda de 1 (um) ponto de espessura.
       O cabeçalho, os títulos de cada bloco de campos e os campos “Emitente da NFS-e” e “Valor
Líquido da NFS-e + IBS/CBS” devem ter sombreamento (fundo) na cor cinza claro (5% de
densidade), para contraste, mantendo-se o fundo branco (0% de densidade) para os demais
campos/dados.

   2.2.4        Modelo de DANFSe Permitido
       Deverá ser utilizado o modelo de DANFSe conforme Anexo I, devendo a disposição de
campos obrigatoriamente obedecer ao disposto no respectivo anexo.

   2.3.         Supressões e Modificações Permitidas
       Poderão ser feitas as seguintes supressões/alterações no DANFSe:

   2.3.1     Bloco “Tomador/Adquirente da Operação”, “Destinatário da Operação”,
       “Intermediário da Operação” e “Tributação Municipal (ISSQN)”
       Caso não sejam preenchidos ou não se apliquem à operação, pode-se suprimir os campos dos
blocos “Tomador/Adquirente da Operação”, “Destinatário da Operação”, “Intermediário da
Operação” e/ou “Tributação Municipal (ISSQN)” e efetuar os seguintes ajustes:

           •   Informar, nos respectivos blocos, apenas: "TOMADOR/ADQUIRENTE DA
               OPERAÇÃO NÃO IDENTIFICADO NA NFS-e",                          "DESTINATÁRIO DA
               OPERAÇÃO NÃO IDENTIFICADO NA NFS-e", "INTERMEDIÁRIO DA
               OPERAÇÃO NÃO IDENTIFICADO NA NFS-e" e/ou                           “TRIBUTAÇÃO
               MUNICIPAL (ISSQN) - OPERAÇÃO NÃO SUJEITA AO ISSQN”, respectivamente,
               observado o tamanho mínimo do bloco, conforme item 2.4.5, notas 2 e 4;
           •   Aumentar a altura do quadro “Descrição do Serviço” e/ou “Informações
               Complementares” no mesmo valor da redução obtida com a redução dos campos dos
               referidos blocos.

   2.3.2    Bloco “Destinatário da Operação” quando o destinatário for o próprio
       Tomador/Adquirente
       Caso o destinatário da operação seja o próprio tomador/adquirente, pode-se suprimir os
campos do bloco “Destinatário da Operação” e efetuar os seguintes ajustes:

           •   Informar, no respectivo bloco, apenas: “O DESTINATÁRIO É O PRÓPRIO
               TOMADOR/ADQUIRENTE DA OPERAÇÃO”, observado o tamanho mínimo do
               bloco, conforme item 2.4.5, nota 3;
           •   Aumentar a altura do bloco “Descrição do Serviço” e/ou “Informações
               Complementares” no mesmo valor da redução obtida com a redução dos campos do
               referido bloco.

   2.3.3       Bloco de Canhoto
       Caso o emitente opte por não utilizar o bloco de “Canhoto”, poderá aumentar o bloco
“Descrição do Serviço” e/ou “Informações Complementares” suprimindo os campos do referido
bloco e deslocando para baixo os campos seguintes. Os ajustes deverão ser feitos no mesmo valor da
supressão realizada.

   2.4.       Padrões de Caracteres (Tipos de Fontes)
       Todos os caracteres deverão estar impressos nas fontes Arial para os títulos/labels e Microsoft
Sans Serif para os conteúdos, em preto sólido (K100) e espaçamento normal.

   2.4.1      Títulos (labels) dos Blocos de Campos
       Deverá ter tamanho de sete (7) pontos, impresso em negrito e caixa alta (maiúsculo),
observada a regra do item 2.4.

   2.4.2      Títulos (labels) dos Campos
       Deverá ter tamanho de seis (6) pontos, impresso em negrito, com a primeira letra de cada
palavra maiúscula e o restante minúsculo, observada a regra do item 2.4.
       Os títulos (labels) dos campos dispostos no item 2.1.2 (Dados de Identificação da NFS-e)
deverão ter tamanho de sete (7) pontos, impressos em negrito, todos em caixa alta (maiúsculo),
observada a regra do item 2.4.

   2.4.3      Conteúdo do Bloco de Campos de Identificação do Documento
       O conteúdo dos campos de identificação do DANFSe deverá observar:

              •   o cabeçalho deverá conter:
                      o no       canto   esquerdo,   a   logomarca   da    NFS-e,   disponível    em:
                         https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/logos-da-
                         nfs-e/Logo%20-%20NFS-e%20-%20Horizontal.png/view
                      o ao centro, a descrição “DANFSe v2.0” e, logo abaixo, a identificação
                         “Documento Auxiliar da NFS-e”, impressas em negrito, com tamanho de
                         nove (9) pontos e fonte Arial.
                      o no canto direito, a identificação (nome) do município do emitente, impressa
                         em formato normal, com tamanho de 8 (oito) pontos; o ambiente gerador
                         da NFS-e; e o tipo de ambiente do Sistema Nacional NFS-e, impressos em
                         formato normal, com tamanho de 6 (seis) pontos; todos com fonte
                         Microsoft Sans Serif;
              •   o conteúdo dos campos deverá ter tamanho de sete (7) pontos, impresso em
                  formato normal, observada a regra do item 2.4;
              •   à direita dos campos de identificação, dispor código de barras bidimensional (QR
                  Code), para consulta rápida via dispositivos móveis, indicando o endereço:

              “https://www.nfse.gov.br/ConsultaPublica/?tpc=1&chave=”, adicionando, após o
              sinal de igual (=), a Chave de Acesso da respectiva NFS-e;
          •   o QR Code deverá ter dimensões mínimas de 1,52 cm x 1,52 cm; e coordenadas
              (X/Y): X: 17,48 cm e Y: 1,67 cm;
          •   abaixo do QR Code, a descrição complementar: “A autenticidade desta NFS-e
              pode ser verificada pela leitura deste código QR ou pela consulta da chave de
              acesso no portal nacional da NFS-e”, disposta em 3 (três) linhas, com tamanho de
              seis (6) pontos, impressa em formato normal e fonte Microsoft Sans Serif.

   Observação: no cabeçalho, apenas no caso de NFS-e gerada para fins de teste em
   ambiente de produção restrita (tag <tpAmb> = 2 – Homologação) deve ser incluída a
   expressão “NFS-e SEM VALIDADE JURÍDICA”, impressa em negrito, com tamanho de
   nove (9) pontos, fonte Arial e em vermelho sólido (M100/Y100), abaixo do título “Documento
   Auxiliar da NFS-e”, conforme modelo abaixo:

2.4.4     Conteúdo dos Campos dos Demais Blocos
   O conteúdo dos campos dos demais blocos do DANFSe deverá observar:

          •   os títulos (labels) dos campos deverão observar a regra do item 2.4.2;
          •   o conteúdo dos campos deverá ter tamanho de sete (7) pontos, impresso em
              formato normal, observada a regra do item 2.4.

   2.4.5 Tamanho dos Campos
           Esta seção apresenta a sugestão de tamanho e posição de cada campo. Todas as medidas estão em
centímetros:
                                                                                    Posição c/
                  NOME                                              Tamanhos                                                              Tam. do
                                                                                     relação à      Outros Campos / Observações
                                     Caminho no XML      Campo       Mínimos                                                              Campo
 BLOCO                                                                                margem
   CAMPO                                                            Alt.   Larg.    Esq.    Sup.
 CABEÇALHO                                                          1,16    20,40    0,30    0,30
   LOGOMARCA DA NFSe                                                0,85     4,00    0,49    0,44
   QUADRO DA DESCRIÇÃO "DANFSe..."                                  1,16    10,19    5,41    0,30     Centralizar o texto no quadro.
   QUADRO DA IDENT.
                                                                    1,16    5,09    15,62    0,30
   MUNICÍPIO/AMBIENTE
                                                                                                     Concatenar os dois campos. Ex.
                                                                                                         Município / UF. Informar
                                     NFSe/infNFSe/ +
                                                         xLocEmi                                        "Município: CCCC / CC".
   MUNICÍPIO                         NFSe/infNFSe/emi               0,64    5,09    15,62    0,30                                            37
                                                          + UF                                        Obs.: Não exibir, quando o
                                     t/enderNac/
                                                                                                      item do cód. de tributação
                                                                                                      nacional informado for 99.
   AMBIENTE GERADOR                  NFSe/infNFSe/       ambGer     0,24    5,09    15,62    0,97                                            1
                                     NFSe/infNFSe/DPS
   TIPO DE AMBIENTE                                       tpAmb     0,24    5,09    15,62    1,22                                            1
                                     /infDPS/
 DADOS DA NFS-e                                                     2,84   20,40     0,30    1,48
                                                                                                      Informar o id da NFS-e sem o
   CHAVE DE ACESSO DA NFS-E          NFSe/infNFSe/          id      0,77   15,30     0,30    1,48                                            50
                                                                                                             prefixo "NFS".
   NÚMERO DA NFS-e                   NFSe/infNFSe/        nNFSe     0,67    5,09     0,30    2,27                                            13
                                     NFSe/infNFSe/DPS
   COMPETÊNCIA DA NFS-e                                  dCompet    0,67    5,09     5,41    2,27             DD/MM/AAAA                     10
                                     /infDPS/
   DATA E HORA DA EMISSÃO DA NFS-E   NFSe/infNFSe/       dhProc     0,67    5,09    10,51    2,27        DD/MM/AAAA hh:mm:ss                 19
                                     NFSe/infNFSe/DPS
   NÚMERO DA DPS                                          nDPS      0,67    5,09     0,30    2,96                                            15
                                     /infDPS/
                                     NFSe/infNFSe/DPS
   SÉRIE DA DPS                                           serie     0,67    5,09     5,41    2,96                                            5
                                     /infDPS/
                                     NFSe/infNFSe/DPS
   DATA E HORA DA EMISSÃO DA DPS                          dhEmi     0,67    5,09    10,51    2,96        DD/MM/AAAA hh:mm:ss                 19
                                     /infDPS/
                                                                                                     Leiaute prevê 3 opções, que são
                                     NFSe/infNFSe/DPS                                                 indicadas pelos números 1 a 3.
   EMITENTE DA NFS-E                                      tpEmit    0,67    5,09     0,30    3,65                                            13
                                     /infDPS/                                                       Utilizar a descrição destas opções.
                                                                                                               Ex.: Prestador.
                                                                                                      Utilizar a descrição das opções
                                                                                                      previstas no leiaute. Preencher
                                                                                                        com reticências (...), caso a
   SITUAÇÃO DA NFS-E                 NFSe/infNFSe/        cStat     0,67    5,09     5,41    3,65                                            40
                                                                                                     descrição supere 37 caracteres.
                                                                                                    Ex.: NFS-e de Decisão Judicial ou
                                                                                                                 Administ...
                                                                                                      Utilizar a descrição das opções
                                                                                                      previstas no leiaute. Preencher
                                     NFSe/infNFSe/DPS
   FINALIDADE                                            finNFSe    0,67    5,09    10,51    3,65       com reticências (...), caso a        40
                                     /infDPS/IBSCBS/
                                                                                                     descrição supere 37 caracteres.
                                                                                                             Ex.: NFS-e regular.
   QUADRO DO QR CODE                                                1,52    1,52    17,48    1,67
   QUADRO COMPLEMENTO QR CODE                                       0,68    4,72    15,80    3,36
 PRESTADOR / FORNECEDOR                                             0,63    5,09     0,30    4,34
                                                          CNPJ /
                                     NFSe/infNFSe/DPS                                                     nn.nnn.nnn/nnnn-nn /            18 / 14 /
   CNPJ / CPF / NIF                                       CPF /     0,63    5,09     5,41    4,34
                                     /infDPS/prest/                                                       nnn.nnn.nnn-nn / nnn               40
                                                           NIF
                                     NFSe/infNFSe/DPS
   INDICADOR MUNICIPAL (INSCRIÇÃO)                         IM       0,63    5,09    10,51    4,34                                            15
                                     /infDPS/prest/
                                     NFSe/infNFSe/DPS
   TELEFONE                                                fone     0,63    5,09    15,62    4,34                                            20
                                     /infDPS/prest/
                                                                                                     Preencher com reticências (...),
                                     NFSe/infNFSe/DPS
   NOME / NOME EMPRESARIAL                               xNome      0,63   10,19     0,30    4,98      caso a descrição supere 77            80
                                     /infDPS/prest/
                                                                                                               caracteres.
                                                                                                      Leiaute prevê a informação do
                                     NFSe/infNFSe/DPS
                                                                                                    código do município com 7 dígitos
                                     /infDPS/prest/end
                                                                                                       da Tabela do IBGE. Utilizar a
                                     /endNac/ ou         cMun ou
   MUNICÍPIO / SIGLA UF                                             0,63    5,09    10,51    4,98       descrição destes códigos.            37
                                     NFSe/infNFSe/DPS    xCidade
                                                                                                     Concatenar o nome do município
                                     /infDPS/prest/end
                                                                                                        com a respectiva UF. Ex.:
                                     /endExt/
                                                                                                              Município / UF.
                                     NFSe/infNFSe/DPS
                                     /infDPS/prest/end
                                                          cMun +                                         Concatenar os campos.
                                     /endNac/ ou
   CÓDIGO IBGE / CEP                                      CEP ou    0,63    5,09    15,62    4,98    Ex.: nnnnnnn / nn.nnn-nnn ou            21
                                     NFSe/infNFSe/DPS
                                                         cEndPost                                    nnnnnnn / nnnnnnnnnnn (ext)
                                     /infDPS/prest/end
                                     /endExt/
                                                                                                    Concatenar todos os campos do
                                                          xLgr,
                                     NFSe/infNFSe/DPS                                               endereço. Ex.: ccc, ccc, ccc, ccc.
                                                          nro,
   ENDEREÇO                          /infDPS/prest/end              0,63   10,19     0,30    5,62   Preencher com reticências (...),         80
                                                          xCpl,
                                     /                                                                caso a descrição supere 77
                                                         xBairro
                                                                                                          caracteres. Nota 1
                                     NFSe/infNFSe/DPS
   EMAIL                                                  email     0,63   10,19    10,51    5,62                Nota 1                      80
                                     /infDPS/prest/

                                                                                                   Leiaute prevê 3 opções, que são
                                                                                                    indicadas pelos números 1 a 3.
                                    NFSe/infNFSe/DPS
  SIMPLES NACIONAL NA DATA DE                           opSimpN                                   Utilizar a descrição destas opções.
                                    /infDPS/prest/reg              0,63    5,09    0,30    6,28                                            40
  COMPETÊNCIA                                              ac                                      Preencher com reticências (...),
                                    Trib/
                                                                                                       caso a descrição supere 37
                                                                                                     caracteres. Ex.: Não Optante.
                                                                                                   Leiaute prevê 3 opções, que são
                                                                                                    indicadas pelos números 1 a 3.
                                                                                                  Utilizar a descrição destas opções.
                                    NFSe/infNFSe/DPS
  REGIME DE APURAÇÃO TRIBUTÁRIA                         regApTri                                   Preencher com reticências (...),
                                    /infDPS/prest/reg              0,63   10,19   10,51    6,28                                            80
  PELO SN                                                 bSN                                          caso a descrição supere 77
                                    Trib/
                                                                                                      caracteres. Ex.: Regime de
                                                                                                   apuração dos tributos federais e
                                                                                                   municipal pelo Simples Nacional.
TOMADOR / ADQUIRENTE                                               0,63    5,09    0,30    6,92                 Nota 2
                                                         CNPJ /
                                    NFSe/infNFSe/DPS                                                    nn.nnn.nnn/nnnn-nn /            18 / 14 /
  CNPJ / CPF / NIF                                       CPF /     0,63    5,09    5,41    6,92
                                    /infDPS/toma/                                                       nnn.nnn.nnn-nn / nnn               40
                                                          NIF
                                    NFSe/infNFSe/DPS
  INDICADOR MUNICIPAL (INSCRIÇÃO)                         IM       0,63    5,09   10,51    6,92                                            15
                                    /infDPS/toma/
                                    NFSe/infNFSe/DPS
  TELEFONE                                                fone     0,63    5,09   15,62    6,92                                            20
                                    /infDPS/toma/
                                                                                                   Preencher com reticências (...),
                                    NFSe/infNFSe/DPS
  NOME / NOME EMPRESARIAL                               xNome      0,63   10,19    0,30    7,56       caso a descrição supere 77           80
                                    /infDPS/toma/
                                                                                                              caracteres.
                                                                                                    Leiaute prevê a informação do
                                    NFSe/infNFSe/DPS
                                                                                                  código do município com 7 dígitos
                                    /infDPS/toma/end
                                                                                                     da Tabela do IBGE. Utilizar a
                                    /endNac/ ou         cMun ou
  MUNICÍPIO / SIGLA UF                                             0,63    5,09   10,51    7,56        descrição destes códigos.           37
                                    NFSe/infNFSe/DPS    xCidade
                                                                                                   Concatenar o nome do município
                                    /infDPS/toma/end
                                                                                                       com a respectiva UF. Ex.:
                                    /endExt/
                                                                                                            Município / UF.
                                    NFSe/infNFSe/DPS
                                    /infDPS/toma/end
                                                         cMun +                                        Concatenar os campos.
                                    /endNac/ ou
  CÓDIGO IBGE / CEP                                      CEP ou    0,63    5,09   15,62    7,56    Ex.: nnnnnnn / nn.nnn-nnn ou            21
                                    NFSe/infNFSe/DPS
                                                        cEndPost                                   nnnnnnn / nnnnnnnnnnn (ext)
                                    /infDPS/toma/end
                                    /endExt/
                                                                                                  Concatenar todos os campos do
                                                         xLgr,
                                    NFSe/infNFSe/DPS                                              endereço. Ex.: ccc, ccc, ccc, ccc.
                                                         nro,
  ENDEREÇO                          /infDPS/toma/end               0,63   10,19    0,30    8,22   Preencher com reticências (...),         80
                                                         xCpl,
                                    /                                                               caso a descrição supere 77
                                                        xBairro
                                                                                                        caracteres. Nota 1
                                    NFSe/infNFSe/DPS
  E-MAIL                                                 email     0,63   10,19   10,51    8,22                Nota 1                      80
                                    /infDPS/toma/
DESTINATÁRIO DA OPERAÇÃO                                           0,63    5,09    0,30    8,86           Nota 2 e Nota 3
                                    NFSe/infNFSe/DPS     CNPJ /
                                                                                                        nn.nnn.nnn/nnnn-nn /            18 / 14 /
  CNPJ / CPF / NIF                  /infDPS/IBSCBS/d     CPF /     0,63    5,09    5,41    8,86
                                                                                                        nnn.nnn.nnn-nn / nnn               40
                                    est/                  NIF
                                    NFSe/infNFSe/DPS
  TELEFONE                          /infDPS/IBSCBS/d      fone     0,63    5,09   15,62    8,86                                            20
                                    est/
                                    NFSe/infNFSe/DPS                                               Preencher com reticências (...),
  NOME / NOME EMPRESARIAL           /infDPS/IBSCBS/d    xNome      0,63   10,19    0,30    9,50       caso a descrição supere 77           80
                                    est/                                                                      caracteres.
                                    NFSe/infNFSe/DPS                                                Leiaute prevê a informação do
                                    /infDPS/IBSCBS/d                                              código do município com 7 dígitos
                                    est/end/endNac/                                                  da Tabela do IBGE. Utilizar a
                                                        cMun ou
  MUNICÍPIO / SIGLA UF              ou                             0,63    5,09   10,51    9,50        descrição destes códigos.           37
                                                        xCidade
                                    NFSe/infNFSe/DPS                                               Concatenar o nome do município
                                    /infDPS/IBSCBS/d                                                   com a respectiva UF. Ex.:
                                    est/end/endExt/                                                         Município / UF.
                                    NFSe/infNFSe/DPS
                                    /infDPS/IBSCBS/d
                                    est/end/endNac/      cMun +                                        Concatenar os campos.
  CÓDIGO IBGE / CEP                 ou                   CEP ou    0,63    5,09   15,62    9,50    Ex.: nnnnnnn / nn.nnn-nnn ou            21
                                    NFSe/infNFSe/DPS    cEndPost                                   nnnnnnn / nnnnnnnnnnn (ext)
                                    /infDPS/IBSCBS/d
                                    est/end/endExt/
                                                                                                  Concatenar todos os campos do
                                                         xLgr,
                                    NFSe/infNFSe/DPS                                              endereço. Ex.: ccc, ccc, ccc, ccc.
                                                         nro,
  ENDEREÇO                          /infDPS/IBSCBS/d               0,63   10,19    0,30   10,16   Preencher com reticências (...),         80
                                                         xCpl,
                                    est/end/                                                        caso a descrição supere 77
                                                        xBairro
                                                                                                        caracteres. Nota 1
                                    NFSe/infNFSe/DPS
  E-MAIL                            /infDPS/IBSCBS/d     email     0,63   10,19   10,51   10,16                Nota 1                      80
                                    est/
INTERMEDIÁRIO DA OPERAÇÃO                                          0,63    5,09    0,30   10,80                Nota 2
                                                         CNPJ /
                                    NFSe/infNFSe/DPS                                                    nn.nnn.nnn/nnnn-nn /            18 / 14 /
  CNPJ / CPF / NIF                                       CPF /     0,63    5,09    5,41   10,80
                                    /infDPS/interm/                                                     nnn.nnn.nnn-nn / nnn               40
                                                          NIF
                                    NFSe/infNFSe/DPS
  INDICADOR MUNICIPAL (INSCRIÇÃO)                         IM       0,63    5,09   10,51   10,80                                            15
                                    /infDPS/interm/
                                    NFSe/infNFSe/DPS
  TELEFONE                                                fone     0,63    5,09   15,62   10,80                                            20
                                    /infDPS/interm/
                                                                                                   Preencher com reticências (...),
                                    NFSe/infNFSe/DPS
  NOME / NOME EMPRESARIAL                               xNome      0,63   10,19    0,30   11,44       caso a descrição supere 77           80
                                    /infDPS/interm/
                                                                                                              caracteres.
                                    NFSe/infNFSe/DPS                                                Leiaute prevê a informação do
                                                        cMun ou
  MUNICÍPIO / SIGLA UF              /infDPS/interm/en              0,63    5,09   10,51   11,44   código do município com 7 dígitos        37
                                                        xCidade
                                    d/endNac/ ou                                                     da Tabela do IBGE. Utilizar a

                                     NFSe/infNFSe/DPS                                                     descrição destes códigos.
                                     /infDPS/interm/en                                                 Concatenar o nome do município
                                     d/endExt/                                                            com a respectiva UF. Ex.:
                                                                                                               Município / UF.
                                     NFSe/infNFSe/DPS
                                     /infDPS/interm/en
                                                            cMun +                                          Concatenar os campos.
                                     d/endNac/ ou
  CÓDIGO IBGE / CEP                                         CEP ou     0,63    5,09   15,62   11,44     Ex.: nnnnnnn / nn.nnn-nnn ou           21
                                     NFSe/infNFSe/DPS
                                                           cEndPost                                     nnnnnnn / nnnnnnnnnnn (ext)
                                     /infDPS/interm/en
                                     d/endExt/
                                                                                                       Concatenar todos os campos do
                                                             xLgr,
                                     NFSe/infNFSe/DPS                                                  endereço. Ex.: ccc, ccc, ccc, ccc.
                                                             nro,
  ENDEREÇO                           /infDPS/interm/en                 0,63   10,19    0,30   12,09    Preencher com reticências (...),        80
                                                             xCpl,
                                     d/                                                                  caso a descrição supere 77
                                                            xBairro
                                                                                                             caracteres. Nota 1
                                     NFSe/infNFSe/DPS
  E-MAIL                                                    email      0,63   10,19   10,51   12,09                 Nota 1                     80
                                     /infDPS/interm/
SERVIÇO PRESTADO                                                       0,63    5,09    0,30   12,74
                                     NFSe/infNFSe/DPS
                                                           cTribNac
  CÓDIGO DE TRIBUTAÇÃO NACIONAL /    /infDPS/serv/cSer
                                                               +       0,63    5,09    5,41   12,74             nn.nn.nn / nnn                 14
  MUNICIPAL                          v/ +
                                                           cTribMun
                                     NFSe/infNFSe/
                                     NFSe/infNFSe/DPS
  CÓDIGO DA NBS                      /infDPS/serv/cSer      cNBS       0,63    5,09   10,51   12,74              n.nnnn.nn.nn                   9
                                     v/
                                                                                                      Concatenar o nome do município,
                                                                                                      a respectiva UF da Tabela do IBGE
                                     NFSe/infNFSe/ +       xLocPres
                                                                                                      e o nome do País. Ex.: Município /
  LOCAL DA PRESTAÇÃO / SIGLA UF /    NFSe/infNFSe/DPS       tacao +
                                                                       0,63    5,09   15,62   12,74     UF / País. Com relação ao país,        42
  PAÍS                               /infDPS/serv/locPr    cPaisPres
                                                                                                         utilizar o código de 2 dígitos,
                                     est/                    tacao
                                                                                                      conforme a Tabela de Países ISO.
                                                                                                                     Ex.: BR
                                                                                                           SE xTribMun <> “” ENTAO
                                                                                                          Descrição Municipal SENAO
                                     NFSe/infNFSe/DPS
                                                           xTribNac                                       Descrição Nacional. Utilizar
  DESCRIÇÃO DO CÓDIGO DE             /infDPS/serv/cSer
                                                               +       0,38   20,40    0,30   13,39    reticências (...), caso a descrição     170
  TRIBUTAÇÃO NACIONAL / MUNICIPAL    v/ +
                                                           xTribMun                                          supere 167 caracteres.
                                     NFSe/infNFSe/
                                                                                                         Obs.: Não há título (label)
                                                                                                          deste campo no DANFSe
                                     NFSe/infNFSe/DPS
                                                           xDescSer                                    Utilizar reticências (...), caso a
  DESCRIÇÃO DO SERVIÇO               /infDPS/serv/cSer                 0,63   20,40    0,30   13,79                                           1300
                                                              v                                       descrição supere 1297 caracteres.
                                     v/
TRIBUTAÇÃO MUNICIPAL (ISSQN)                                           0,63    5,09    0,30   14,43                    Nota 4
                                                                                                        Leiaute prevê 4 opções, que são
                                     NFSe/infNFSe/DPS
                                                           tribISSQ                                      indicadas pelos números 1 a 4.
  TIPO DE TRIBUTAÇÃO DO ISSQN        /infDPS/valores/tri               0,63    5,09    0,30   14,43                                            21
                                                               N                                       Utilizar a descrição destas opções.
                                     b/tribMun/
                                                                                                            Ex.: Operação Tributável.
                                                                                                       Concatenar o nome do município,
                                                                                                      a respectiva UF da Tabela do IBGE
                                     NFSe/infNFSe/ +       xLocInci
                                                                                                       e o nome do País. Ex.: Município /
  MUNICÍPIO / SIGLA UF / PAÍS DA     NFSe/infNFSe/DPS        d+
                                                                       0,63   10,19    5,41   14,43      UF / País. Com relação ao país,       42
  INCIDÊNCIA DO ISSQN                /infDPS/valores/tri   cPaisRes
                                                                                                          utilizar o código de 2 dígitos,
                                     b/tribMun/               ult
                                                                                                       conforme a Tabela de Países ISO.
                                                                                                                      Ex.: BR
                                                                                                        Leiaute prevê 8 opções, que são
                                     NFSe/infNFSe/DPS
  REGIME ESPECIAL DE TRIBUTAÇÃO DO                         regEspTri                                  indicadas pelos números 0 a 6 e 9.
                                     /infDPS/prest/reg                 0,63    5,09    0,30   15,08                                            27
  ISSQN                                                        b                                       Utilizar a descrição destas opções.
                                     Trib/
                                                                                                             Ex.: Estimativa. Nota 5
                                                                                                        Leiaute prevê 5 opções, que são
                                                                                                         indicadas pelos números 1 a 5.
                                     NFSe/infNFSe/DPS                                                  Utilizar a descrição destas opções.
                                                           tpImunid
  TIPO DE IMUNIDADE DO ISSQN         /infDPS/valores/tri               0,63    5,09    5,41   15,08      Utilizar reticências (...), caso a    40
                                                              ade
                                     b/tribMun/                                                          descrição supere 37 caracteres.
                                                                                                       Ex.: Livros, jornais, periódicos e o
                                                                                                                  papel... Nota 5
                                                                                                       Se for o caso, utilizar as seguintes
                                                                                                      descrições: Exigibilidade Suspensa
                                     NFSe/infNFSe/DPS
                                                                                                       por Decisão Judicial; Exigibilidade
  SUSPENSÃO DA EXIGIBILIDADE DO      /infDPS/valores/tri
                                                            tpSusp     0,63    5,09   10,51   15,08           Suspensa por Processo            40
  ISSQN                              b/tribMun/exigSus
                                                                                                         Administrativo. Preencher com
                                     p/
                                                                                                        reticências (...), caso a descrição
                                                                                                          supere 37 caracteres. Nota 5
                                     NFSe/infNFSe/DPS
                                     /infDPS/valores/tri   nProcess
  NÚMERO PROCESSO SUSPENSÃO                                            0,63    5,09   15,62   15,08                 Nota 5                     30
                                     b/tribMun/exigSus        o
                                     p/
                                                                                                       Leiaute prevê 4 opções, que são
                                     NFSe/infNFSe/valo                                                  indicadas pelos números 1 e 4.
  BENEFÍCIO MUNICIPAL                                        tpBM      0,63    5,09    0,30   15,73                                            40
                                     res/                                                             Utilizar a descrição destas opções.
                                                                                                             Ex.: Isenção. Nota 5
                                     NFSe/infNFSe/valo
                                                           vCalcBM
                                     res/ ou
                                                              ou
  CÁLCULO DO BM                      NFSe/infNFSe/DPS                  0,63    5,09    5,41   15,73                  Nota 5                   1-15V2
                                                           vRedBCB
                                     /infDPS/valores/tri
                                                              M
                                     b/tribMun/BM/
                                     NFSe/infNFSe/DPS
                                     /infDPS/valores/v      vDR ou
                                     DedRed/ ou            vCalcDR
  TOTAL DEDUÇÕES/REDUÇÕES            NFSe/infNFSe/valo        +        0,63    5,09   10,51   15,73                  Nota 5                   1-15V2
                                     res/ +                vCalcRee
                                     NFSe/infNFSe/IBS       RepRes
                                     CBS/valores/

                                     NFSe/infNFSe/DPS
                                                           vDescInc
  DESCONTO INCONDICIONADO            /infDPS/valores/v                 0,63    5,09   15,62   15,73                 Nota 5                  1-15V2
                                                             ond
                                     DescCondIncond/
                                     NFSe/infNFSe/valo
  BC ISSQN                                                   vBC       0,63    5,09    0,30   16,37                                         1-15V2
                                     res/
                                     NFSe/infNFSe/valo     pAliqApli
  ALÍQUOTA APLICADA                                                    0,63    5,09    5,41   16,37                                         1-2V2
                                     res/                      c
                                                                                                       Leiaute prevê 3 opções, que são
                                     NFSe/infNFSe/DPS
                                                                                                        indicadas pelos números 1 a 3.
  RETENÇÃO DO ISSQN                  /infDPS/valores/tri   tpRetISS    0,63    5,09   10,51   16,37                                          25
                                                                                                       Utilizar descrição destas opções.
                                     b/tribMun/               QN
                                                                                                                Ex.: Não Retido.
                                     NFSe/infNFSe/valo
  ISSQN APURADO                                            vISSQN      0,63    5,09   15,62   16,37                                         1-2V2
                                     res/
TRIBUTAÇÃO FEDERAL (EXCETO CBS)                                        0,63    5,09    0,30   17,02
                                     NFSe/infNFSe/DPS
  IRRF                               /infDPS/valores/tri   vRetIRRF    0,63    5,09    5,41   17,02                                         1-15V2
                                     b/tribFed/
                                     NFSe/infNFSe/DPS
  CONTRIBUIÇÃO PREVIDENCIÁRIA -
                                     /infDPS/valores/tri    vRetCP     0,63    5,09   10,51   17,02                                         1-15V2
  RETIDA
                                     b/tribFed/
                                     NFSe/infNFSe/DPS
                                     /infDPS/valores/tri
                                     b/tribFed/

                                     ou                    vRetCSL
                                                              L                                           Quando tpRetPisCofins = 1
                                     NFSe/infNFSe/DPS                                                 (PIS/COFINS Retido), este campo
                                     /infDPS/valores/tri      ou                                      retornará o somatório dos valores
  CONTRIBUIÇÕES SOCIAIS - RETIDAS    b/tribFed/ +                      0,63    5,09   15,62   17,02   informados nos campos vRetCSLL        1-15V2
                                     NFSe/infNFSe/DPS      vRetCSL                                       ,vPis e vCofins. Nos demais
                                     /infDPS/valores/tri   L + vPis                                     casos, o campo retornará o
                                     b/tribFed/piscofins      +                                       valor informado em vRetCSLL.
                                     /+                    vCofins
                                     NFSe/infNFSe/DPS
                                     /infDPS/valores/tri
                                     b/tribFed/piscofins
                                     /
                                                                                                         Quando tpRetPisCofins = 1
                                                                                                      (PIS/COFINS Retido), este campo
                                     NFSe/infNFSe/DPS                                                    retornará 0,00 (zero). Nos
                                     /infDPS/valores/tri                                                  demais casos, o campo
  PIS - DÉBITO APURAÇÃO PRÓPRIA                              vPis      0,63    5,09    0,30   17,67                                         1-15V2
                                     b/tribFed/piscofins                                               retornará o valor informado
                                     /                                                                           em vPis.

                                                                                                                   Nota 6
                                                                                                         Quando tpRetPisCofins = 1
                                                                                                      (PIS/COFINS Retido), este campo
                                     NFSe/infNFSe/DPS                                                    retornará 0,00 (zero). Nos
                                     /infDPS/valores/tri                                                  demais casos, o campo
  COFINS - DÉBITO APURAÇÃO PRÓPRIA                         vCofins     0,63    5,09    5,41   17,67                                         1-15V2
                                     b/tribFed/piscofins                                               retornará o valor informado
                                     /                                                                          em vCofins.

                                                                                                                    Nota 6
                                                                                                       Leiaute prevê 10 opções, que são
                                     NFSe/infNFSe/DPS
                                                                                                        indicadas pelos números 1 a 9.
  DESCRIÇÃO CONTRIB. SOCIAIS -       /infDPS/valores/tri
                                                           tpRetPis    0,63   10,19   10,51   17,67   Utilizar a descrição destas opções.    35
  RETIDAS                            b/tribFed/piscofins
                                                            Cofins                                    Ex.: PIS/COFINS/CSLL Não Retido.
                                     /
                                                                                                                    Nota 6
TRIBUTAÇÃO IBS / CBS                                                   0,63    5,09    0,30   18,32
                                     NFSe/infNFSe/DPS
                                                            CST +
                                     /infDPS/IBSCBS/v
  CST / CCLASSTRIB                                         cClassTri   0,63    5,09    5,41   18,32             nnn / nnnnnn                 12
                                     alores/trib/gIBSCB
                                                               b
                                     S/
                                                            cIndOp
                                     NFSe/infNFSe/DPS
                                                               +
                                     /infDPS/IBSCBS/                                                    Concatenar todos os campos:
                                                           cLocalida
  INDICADOR DE OPERAÇÃO / CÓDIGO     +                                                                  nnnnnn / nnnnnnn / ccc / CC.
                                                            deIncid
  IBGE INCIDÊNCIA / MUNICÍPIO        NFSe/infNFSe/IBS                  0,63   10,19   10,51   18,32   Concatenar o nome do município         56
                                                               +
  INCIDÊNCIA / SIGLA UF              CBS/ +                                                           com a respectiva UF da Tabela do
                                                           xLocalida
                                     NFSe/infNFSe/IBS                                                    IBGE. Ex.: Município / UF.
                                                            deIncid
                                     CBS/
                                                               +
                                     NFSe/infNFSe/DPS
                                     /infDPS/valores/v
                                     DescCondIncond/
                                     +
                                     NFSe/infNFSe/IBS      vDescInc
                                     CBS/valores/ +          ond +
                                     NFSe/infNFSe/valo     vCalcRee
  EXCLUSÕES E REDUÇÕES DA BASE DE    res/ +                 RepRes
                                                                       0,63    5,09    0,30   18,96   Somatório de todos estes campos.      1-15V2
  CÁLCULO                            NFSe/infNFSe/DPS          +
                                     /infDPS/valores/tri    vISSQN
                                     b/tribFed/piscofins   + vPIS +
                                     /+                    vCOFINS
                                     NFSe/infNFSe/DPS
                                     /infDPS/valores/tri
                                     b/tribFed/piscofins
                                     /
  BASE DE CÁLCULO APÓS EXCLUSÕES E   NFSe/infNFSe/IBS
                                                             vBC       0,63    5,09    5,41   18,96                                         1-15V2
  REDUÇÕES                           CBS/valores/

                                      NFSe/infNFSe/IBS
                                                            pRedAliq
                                      CBS/valores/uf/ +
                                                              UF +
                                      NFSe/infNFSe/IBS                                                                                       1-2V2 /
  RED. ALÍQUOTA IBS / RED. ALÍQUOTA                         pRedAliq
                                      CBS/valores/mun/                  0,63    5,09   10,51   18,96              %/%/%                      1-2V2 /
  CBS                                                        Mun +
                                      +                                                                                                       1-2V2
                                                            pRedAliq
                                      NFSe/infNFSe/IBS
                                                              CBS
                                      CBS/valores/fed/
                                      NFSe/infNFSe/IBS
                                                             pIBSUF
                                      CBS/valores/uf/ +                                                                                      1-2V2 /
  ALÍQUOTA - IBS UF / IBS MUN                                   +       0,63    5,09   15,62   18,96                 %/%
                                      NFSe/infNFSe/IBS                                                                                        1-2V2
                                                            pIBSMun
                                      CBS/valores/mun/
                                      NFSe/infNFSe/IBS      pAliqEfet
  ALÍQ. EFETIVA MUNICIPAL - IBS                                         0,63    5,09    0,30   19,61                                         1-2V2
                                      CBS/valores/mun/        Mun
                                      NFSe/infNFSe/IBS
  VALOR APURADO MUNICIPAL - IBS       CBS/totCIBS/gIBS      vIBSMun     0,63    5,09    5,41   19,61                                         1-15V2
                                      /gIBSMunTot/
                                      NFSe/infNFSe/IBS      pAliqEfet
  ALÍQ. EFETIVA ESTADUAL - IBS                                          0,63    5,09   10,51   19,61                                         1-2V2
                                      CBS/valores/uf/          UF
                                      NFSe/infNFSe/IBS
  VALOR APURADO ESTADUAL - IBS        CBS/totCIBS/gIBS      vIBSUF      0,63    5,09   15,62   19,61                                         1-15V2
                                      /gIBSUFTot/
                                      NFSe/infNFSe/IBS
  VALOR TOTAL APURADO - IBS           CBS/totCIBS/gIBS      vIBSTot     0,63    5,09    0,30   20,26                                         1-15V2
                                      /
                                      NFSe/infNFSe/IBS
  ALÍQUOTA - CBS                                             pCBS       0,63    5,09    5,41   20,26                                         1-2V2
                                      CBS/valores/fed/
                                      NFSe/infNFSe/IBS      pAliqEfet
  ALÍQUOTA EFETIVA - CBS                                                0,63    5,09   10,51   20,26                                         1-2V2
                                      CBS/valores/fed/        CBS
                                      NFSe/infNFSe/IBS
  VALOR TOTAL APURADO - CBS           CBS/totCIBS/gCB        vCBS       0,63    5,09   15,62   20,26                                         1-15V2
                                      S/
VALOR TOTAL DA NFS-E                                                    0,67    5,09    0,30   20,90
                                      NFSe/infNFSe/DPS
  VALOR DA OPERAÇÃO / SERVIÇO         /infDPS/valores/v      vServ      0,67    5,09    5,41   20,90                                         1-15V2
                                      ServPrest/
                                      NFSe/infNFSe/DPS
                                                            vDescInc
  DESCONTO INCONDICIONADO             /infDPS/valores/v                 0,67    5,09   10,51   20,90                                         1-15V2
                                                              ond
                                      DescCondIncond/
                                      NFSe/infNFSe/DPS
                                                            vDescCo
  DESCONTO CONDICIONADO               /infDPS/valores/v                 0,67    5,09   15,62   20,90                                         1-15V2
                                                              nd
                                      DescCondIncond/
  TOTAL DAS RETENÇÕES (ISSQN /        NFSe/infNFSe/valo     vTotalRe
                                                                        0,67    5,09    0,30   21,59                                         1-15V2
  FEDERAIS)                           res/                     t
                                      NFSe/infNFSe/valo
  VALOR LÍQUIDO DA NFS-e                                      vLiq      0,67    5,09    5,41   21,59                                         1-15V2
                                      res/
                                      NFSe/infNFSe/IBS
                                      CBS/totCIBS/gIBS
                                      /+                    vIBSTot
  TOTAL DO IBS/CBS                                                      0,67    5,09   10,51   21,59                                         1-15V2
                                      NFSe/infNFSe/IBS      + vCBS
                                      CBS/totCIBS/gCB
                                      S/
                                      NFSe/infNFSe/IBS
  VALOR LÍQUIDO DA NFS-e + IBS/CBS                           vTotNF     0,67    5,09   15,62   21,59                                         1-15V2
                                      CBS/totCIBS/
INFORMAÇÕES COMPLEMENTARES                                              0,39   20,40    0,30   22,27
                                      NFSe/infNFSe/DPS
                                      /infDPS/serv/infoC
                                      ompl/ +
                                      NFSe/infNFSe/DPS       xInfCom
                                      /infDPS/subst +            p+
                                                                                                          União de todos os campos de
                                      NFSe/infNFSe/DPS      chSubstd
                                                                                                         informações complementares.
                                      /infDPS/serv/infoC         a+
                                      ompl/ +               docRef +
                                                                                                           As informações devem ser
                                      NFSe/infNFSe/DPS       cObra +
                                                                                                       descritas e dispostas na seguinte
                                      /infDPS/serv/obra     inscImob
                                                                                                          ordem: Inf. Cont.:; NFS-e
                                      /+                       Fisc +
                                                                                                        Subst.: (Nota 7); Doc. Ref.:;
                                      NFSe/infNFSe/DPS       idAtvEvt
                                                                                                         Cod. Obra: (Nota 8); Insc.
                                      /infDPS/IBSCBS/i            +
                                                                                                         Imob.: (Nota 8); Cod. Evt.:
                                      movel/ +              idDocTec
                                                                                                         (Nota 9); Doc. Tec.:; Núm.
                                      NFSe/infNFSe/DPS            +
                                                                                                        Ped.:; Item Ped.:; Inf. A. T.
                                      /infDPS/serv/atvE       xPed +
                                                                                                                    Mun.:;
                                      vento/ +               xItemPe
  INFORMAÇÕES COMPLEMENTARES          NFSe/infNFSe/DPS           d+     0,39   20,40    0,30   22,68                                          2000
                                                                                                       Obrigatoriamente, deve-se constar
                                      /infDPS/serv/infoC      xOutInf
                                                                                                            a informação de Totais
                                      ompl/ +                     +
                                                                                                         Aproximados dos Tributos
                                      NFSe/infNFSe/DPS      vTotTribF
                                                                                                                   (Nota 10).
                                      /infDPS/serv/infoC         ed,
                                      ompl/ +                vTotTrib
                                                                                                           As informações devem ser
                                      NFSe/infNFSe/DPS          Est e
                                                                                                           separadas por pipes ( | ).
                                      /infDPS/serv/infoC     vTotTrib
                                      ompl/gItemPed/ +         Mu ou
                                                                                                        Utilizar reticências (...), caso a
                                      NFSe/infNFSe/ +        pTotTrib
                                                                                                       descrição supere 1997 caracteres,
                                      NFSe/infNFSe/DPS          Fed,
                                                                                                        sem prejuízo à linha de “Totais
                                      /infDPS/valores/tri    pTotTrib
                                                                                                       Aproximados dos Tributos”, que é
                                      b/totTrib/vTotTrib        Est e
                                                                                                                       fixa.
                                      / ou                   pTotTrib
                                      NFSe/infNFSe/DPS           Mu
                                      /infDPS/valores/tri
                                      b/totTrib/pTotTrib
                                      /
CANHOTO                                                                 0,67   20,40    0,30   28,10                Nota 11
  DATA CIENTIFICAÇÃO                                                    0,67    5,09    0,30   28,10

   IDENTIFICAÇÃO E ASSINATURA                               0,67    5,09    5,41   28,10
                                                  nNFSe +                                  Informar o id da NFS-e sem o
   Nº NFS-E / CHAVE NFS-E       NFSe/infNFSe/               0,67   10,19   10,51   28,10                                   66
                                                     id                                    prefixo "NFS". Ex.: nnn / nnn

   Notas:

        1. Esta linha poderá ser suprimida, ainda que existam dados dos respectivos campos no arquivo
XML.
        2. Caso não sejam informados dados de tomador/adquirente, destinatário e/ou intermediário da
operação, informar, nos respectivos blocos, apenas: "TOMADOR/ADQUIRENTE DA OPERAÇÃO
NÃO IDENTIFICADO NA NFS-e", "DESTINATÁRIO DA OPERAÇÃO NÃO IDENTIFICADO NA
NFS-e"      e/ou     "INTERMEDIÁRIO             DA OPERAÇÃO                NÃO       IDENTIFICADO                 NA NFS-e",
respectivamente. A altura mínima do bloco é de 0,32cm e a largura mínima é de 20,40cm. As coordenadas
(X/Y) dos blocos devem ser ajustada conforme as informações preenchidas na NFS-e;
        3. Caso o destinatário da operação seja o próprio tomador/adquirente, informar, no bloco do
destinatário da operação, apenas: “O DESTINATÁRIO É O PRÓPRIO TOMADOR/ADQUIRENTE DA
OPERAÇÃO”. A altura mínima do bloco é de 0,32cm e a largura mínima é de 20,40cm. As coordenadas
(X/Y) dos blocos devem ser ajustada conforme as informações preenchidas na NFS-e;
        4. Para as operações às quais não haja a incidência do ISSQN, informar, no bloco “Tributação
Municipal (ISSQN)”, apenas: “TRIBUTAÇÃO MUNICIPAL (ISSQN) - OPERAÇÃO NÃO SUJEITA
AO ISSQN”. A altura mínima do bloco é de 0,32cm e a largura mínima é de 20,40cm. As coordenadas
(X/Y) dos blocos devem ser ajustada conforme as informações preenchidas na NFS-e;
        5. Esta linha poderá ser suprimida caso não existam dados em todos os campos da mesma linha
no arquivo XML;
        6. Esta linha será impressa para as NFS-e emitidas com data de competência até o final do ano-
calendário de 2026.
        7. Em caso de substituição da NFS-e, deve-se informar, no campo de informações
complementares, a chave de acesso da NFS-e substituída, conforme campo “chSubstda”, do leiaute da
DPS/NFS-e. Esta informação deverá ser disposta da seguinte forma: NFS-e Subst.: + chave de acesso da
NFS-e substituída.
        8. Nos casos de obrigatoriedade de preenchimento do grupo de Obra/Imóvel, deverão constar, no
campo de informações complementares, o número de identificação da obra e/ou a inscrição imobiliária
fiscal, conforme campos “cObra” e “inscImobFisc”, respectivamente, do leiaute da DPS/NFS-e. Estas
informações deverão ser dispostas da seguinte forma: Cod. Obra: e Insc. Imob.: + respectivas
informações;

       9. Nos casos de obrigatoriedade de preenchimento do grupo de Evento, deverá constar, no campo
de informações complementares, a identificação da atividade de evento, conforme campos “idAtvEvt”,
do leiaute da DPS/NFS-e. Esta informação deverá ser disposta da seguinte forma: Cod. Evt.: + respectiva
informação;
       10. Deve-se constar, obrigatoriamente, a informação de totais aproximados de tributos, que pode
ser em preenchida com valores monetários OU percentuais, disposta da seguinte forma: "Totais
Aproximados dos Tributos cfe. Lei nº 12.741/2012: Federais: R$ ou % ; Estaduais: R$ ou % ; Municipais:
R$ ou %";
       11. Bloco opcional;
       12. Os campos sem informações no XML devem ser preenchidos com um traço (-);

   2.4.5.1       Exemplos
       Nota 2:

       Nota 3:

       Nota 4:

   2.5.       Outros
   2.5.1      Cancelamento da NFS-e
       Quando do cancelamento da NFS-e, deverá constar no DANFSe marca d’água com a
descrição “CANCELADA”.
       A marca d’água será disposta na diagonal, impressa em formato normal, com tamanho
mínimo de cinquenta (50) pontos, fonte Arial e em cinza (K35), conforme modelo abaixo:

   2.5.2      Substituição da NFS-e
       Quando da substituição da NFS-e, deverá constar no DANFSe marca d’água com a
descrição “SUBSTITUÍDA”.
       A marca d’água será disposta na diagonal, impressa em formato normal, com tamanho
mínimo de cinquenta (50) pontos, fonte Arial e em cinza (K35), conforme modelo abaixo:

   2.5.3      Limitações da Impressora
       Se for necessária a utilização de uma margem superior ou inferior maior, devido às
limitações da impressora, a redução necessária poderá ser feita somente na altura do bloco de
“Informações Complementares” deslocando os campos seguintes para baixo pelo valor desta
redução.

                             CARLOS EDUARDO BURKLE
                         Auditor Fiscal de Tributos – Londrina/PR
  Secretário-Executivo da Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço
                       Eletrônica de Padrão Nacional (SE/CGNFS-e)
```

## Anexo I – Modelo de DANFSe

```text
OBS: Não imprimir os asteriscos. Eles são somente indicadores das notas abaixo.
* Esta linha poderá ser suprimida, ainda que existam dados dos respectivos campos no
arquivo XML.

** Esta linha poderá ser suprimida caso não existam dados em todos os campos da mesma
linha no arquivo XML
*** Esta linha será impressa para as NFS-e emitidas com data de competência até o final do
ano-calendário de 2026.
**** Bloco de Canhoto. Opcional.
```
