---
titulo: "Nota Técnica SE/CGNFS-e nº 010, versão 1.00, de 11 de setembro de 2026 (Leiaute da NFS-e Via e evento de Manifestação do Adquirente)"
esfera: "Federal"
orgao: "Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço Eletrônica de Padrão Nacional (SE/CGNFS-e)"
tipo: "Nota Técnica SE/CGNFS-e"
numero: "010"
data: "2026-09-11"
ano: "2026"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.gov.br/nfse/pt-br/nfs-e-via/documentacao-tecnica/notas-tecnicas/nt-010-se-cgnfse-leiaute-nfse-via-v-1.00.pdf"
ementa: "Atualiza o leiaute da Nota Fiscal de Serviço Eletrônica de Exploração de Via (NFS-e Via) de padrão nacional e cria o evento de Manifestação do Adquirente."
data_consulta: "2026-11-27"
versao_texto: "Versão 1.00 (PDF oficial, 11/09/2026)"
---

# Nota Técnica SE/CGNFS-e nº 010, versão 1.00, de 11 de setembro de 2026 (Leiaute da NFS-e Via e evento de Manifestação do Adquirente)

> **Nota editorial.** Texto extraído da camada de texto do PDF oficial da Nota Técnica 010, versão 1.00, divulgado no Portal da NFS-e (gov.br/nfse) (6 páginas), consultado em 27/11/2026. A data do documento (11/09/2026) é a de publicação da versão, lida na capa do PDF. Versão aprovada ou ratificada pelo Ato Técnico Conjunto Sufis/CGIBS nº 7/2026 (`reguladores/rfb/outros-atos/2026/ato-153887-7-2026.md`). Foram removidos a capa, o sumário, os cabeçalhos e rodapés repetidos e a numeração de página. Os 2 títulos de primeiro nível do sumário viraram seções e o texto de cada uma, com os quadros e os leiautes, ficou em bloco de texto que mantém as colunas do PDF. Figuras e imagens do PDF não foram convertidas. Em caso de dúvida, prevalece o PDF. O Manual para Emissão da NFS-e Via (versão 1.02) e o Anexo IV (Leiautes RN ADN, planilha) são publicados à parte no portal da NFS-e e foram apenas referenciados.

## 1. Introdução

```text
         Este documento contempla atualizações acerca do layout da Nota Fiscal de Serviço eletrônica de
Exploração de Via– NFS-e Via padrão nacional, complementando ou ajustando o conteúdo anteriormente
descrito nas Notas Técnicas anteriores.

         Junto a esta nota técnica, foi também publicado, na seção de documentação técnica do portal da NFS-
e (https://www.gov.br/nfse/pt-br/nfs-e-via/documentacao-tecnica), o Manual para emissão da NFS-e Via com
os ajustes para a emissão do evento de Manifestação do Adquirente e os anexos que passaram por atualização:

             •     Manual para Emissão da NFS-e Via Versão 1.02 – Inclusão das orientações para o envio do
                   Evento de Manifestação do Adquirente;
             •     Anexo IV - Leiautes RN ADN – atualização para versão 1.01 do leiaute da NFS-e Via com a
                   alteração do domínio do campo NFSeVia/infNFSeVia/valores/modPagamento; Inclusão do
                   layout do Evento de Manifestação do Adquirente.

         O documento LeiautesRN_ADN-SNNFSeVia_V1.00.04- é composto por 6 planilhas:
         1) “Leiaute_NFSeVia-ADN_NFSeVia”;
         2) “RN_NFSeVia-ADN_NFSeVia”;
         3) “LEIAUTE_EVENTO_CANC_NFS-e_Via”;
         4) “RN_EVENTO_CANC_NFS-e_Via”;
         5) “LEIAUTE_EVENTO_MANIFE_NFS-e_Via”; e
         6) “RN_EVENTO_MANIFEST_NFS-e_VIA”.
```

## 2 Atualizações

```text
             a. Layout da NFS-e Via – Versão 1.01

                 Domínio do campo “modPagamento” do leiaute da NFS-e ViaAtualização do campo de modalidade
        de pagamento (modPagamento) do Layout da NFS-e Via, para inclusão do domínio “6. Sem cobrança”:

                                    Layout da NFS-e Via – Versão 1.01
  CAMINHO NO XML              CAMPO       ELE   TIPO   OCOR.    TAM.   DESCRIÇÃO
                                                                       Modalidade de pagamento:

                                                                       1. Débito ou pix
NFSeVia/infNFSeVia/valor    modPagamen                                 2. Crédito
                                           E      C     1-1        1
es/                         to                                         3. Dinheiro
                                                                       4. Eletrônico
                                                                       5. Pagamento posterior
                                                                       6. Sem cobrança

              b. Evento de Manifestação do Adquirente
                    Inclusão do layout do Evento de Manifestação do Adquirente:
                    Os grupos infEventoMiaA e infEventoMiaR são mutuamente excludentes, devendo ser informado
          apenas um deles por evento.

                                 Layout do Evento de Manifestação da NFS-e Via – Versão 1.00
                                                  TIP   OCOR
  CAMINHO NO XML               CAMPO       ELE                   TAM.                           DESCRIÇÃO
                                                   O      .
                               evento      Raiz    -      -        -                             TAG raiz
evento/                        versao       A      C     1-1     1-4V2    Versão do leiaute do evento
evento/                      infEvento      G      -     1-1       -      c
                                                                          O identificador do evento é composto pela
                                                                          concatenação de campos que constam no leiaute.

                                                                          A formação deste identificador considera o literal
                                                                          ""EVT"" associado a outras 59 posições numéricas,
                                                                          conforme descrito abaixo:

                                                                          ""EVT"" +
                                                                          Chave de acesso da NFS-e Via (50) + Código do Evento
evento/infEvento/                 id        ID     C     1-1       62
                                                                          (06) +
                                                                          Número sequencial do evento (nSeqEvento) (03)

                                                                          O código do evento de Manifestaçao corresponde ao
                                                                          valor tag infEvento sem a primeira posição:
                                                                          Manifestação do Adquirente da NFS-e Via - Aceite - tag
                                                                          e203202 - código do evento 203202
                                                                          Manifestação do Adquirente da NFS-e Via - Rejeição -
                                                                          tag e203204 - código do evento 203204

evento/infEvento/              verAplic     E      C     0-1      1-20    Versão do aplicativo que gerou o evento.
                                                                          Número sequencial do evento para o mesmo tipo de
                                                                          evento.

evento/infEvento/            nSeqEvento     E      N     1-1       3
                                                                          Para os eventos que possam existir mais de um evento
                                                                          do mesmo tipo o ambiente gerador deverá numerar de
                                                                          forma sequencial.

evento/infEvento/            chNFSeVia      CE     N     1-1       50     Identificador da NFS-e a qual o evento será vinculada.
                                                                          Data e hora do evento no formato AAAA-MM-
                                                                          DDThh:mm:ssTZD (UTC - Universal Coordinated Time,
                                                                          onde TZD pode ser -02:00 (Fernando de Noronha), -
evento/infEvento/             dhEvento      E      D     1-1       -
                                                                          03:00 (Brasília) ou -04:00 (Manaus), no horário de
                                                                          verão serão -01:00, -02:00 e -03:00. Ex.: 2010-08-
                                                                          19T13:00:15-03:00.

                                                                    Tipo de ambiente:

evento/infEvento/            tpAmb        E    N   1-1      1
                                                                    1 - Produção;
                                                                    2 - Homologação;
                                                                    Parte Específica do Registro de Evento
evento/infEventoMiaA/      e203202        CG   -   1-1      -
                                                                    de Manifestação de NFS-e Via - Com Aceite.
                                                                    Descrição do evento:
evento/infEvento/e20320                                             "Manifestação de Informação do Adquirente da NFS-e
                             xDesc        E    C   1-1    5-60
2/
                                                                    Via - Com Aceite"
                                                                    Tipo de Identificação do Adquirente:

evento/infEvento/e20320
                              tpNi        E    N   1-1      1
2/                                                                  1 - CPF
                                                                    2 - CNPJ
                                                                    Para pessoa jurídica, informar o CNPJ do Adquirente da
                                                                    NfS-e Via, conforme padrão vigente da Receita Federal
evento/infEvento/e20320
                            CNPJCPF       E    C   1-1   11 ou 14
2/
                                                                    Para pessoa física, informar o CPF do Adquirente da
                                                                    NfS-e Via, conforme padrão vigente da Receita Federal
evento/infEvento/e20320                                             Nome ou Razão Social do Adquirente.
                          xRazaoSocial    E    C   1-1    02-60
2/
                                                                    Parte Específica do Registro de Evento
evento/infEventoMiaR/      e203204        CG   -   1-1      -
                                                                    de Manifestação de NFS-e Via - Com Rejeição.
                                                                    Descrição do evento:
evento/infEvento/e20320                                             "Manifestação de Informação do Adquirente da NFS-e
                             xDesc        E    C   1-1    5-60
4/
                                                                    Via - Com Rejeição"
                                                                    Tipo de Identificação do Adquirente:

evento/infEvento/e20320
                              tpNi        E    N   1-1      1
4/                                                                  1 - CPF
                                                                    2 - CNPJ
evento/infEvento/e20320                                             CNPJ ou CNPF do Adquirente da NFS-e Via.
                            CNPJCPF       E    C   1-1    11-14
4/
evento/infEvento/e20320                                             Nome ou Razão Social do Adquirente.
                          xRazaoSocial    E    C   1-1    02-60
4/
                                                                    Motivo da Rejeição da NFS-e Via:

                                                                    1 - NFS-e Via em duplicidade;
                                                                    2 - Não ocorrência da passagem do veículo;
                                                                    3 – Data da passagem do veículo;
evento/infEvento/e20320                                             4 – Categoria do Veículo;
                            cMotivo       E    N   1-1      1
4/
                                                                    5 - Placa do veículo;
                                                                    6 – Valor do serviço;
                                                                    7 – Modo de Pagamento;
                                                                    8 – Valor das deduções;
                                                                    99 - Outros;
                                                                    Descrição para explicar o Motivo da Rejeição da NFS-e
evento/infEvento/e20320   xMotivoRejeit
                                          E    C   0-1    15-55
4/                              a                                   Via pelo adquirente do Serviço de Exploração de via.
                                                                    Assinatura do registro segundo o Padrão XML
evento/                    Signature      G    -   1-1      -
                                                                    Digital Signature.

        Data/Hora da recepção do Evento de NFS-e Via.
        Data e hora no formato UTC (Universal Coordinated
        Time):
        AAAA-MM-DDThh:mm:ssTZD
dhReg
        "Número do Registro" do Evento da NFS-e Via
nReg
```
