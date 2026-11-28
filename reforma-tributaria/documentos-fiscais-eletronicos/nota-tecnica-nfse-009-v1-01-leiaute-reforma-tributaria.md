---
titulo: "Nota Técnica SE/CGNFS-e nº 009, versão 1.01, de 11 de setembro de 2026 (Leiaute da NFS-e na Reforma Tributária do Consumo)"
esfera: "Federal"
orgao: "Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço Eletrônica de Padrão Nacional (SE/CGNFS-e)"
tipo: "Nota Técnica SE/CGNFS-e"
numero: "009"
data: "2026-09-11"
ano: "2026"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS", "ISSQN"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/nota-tecnica-009-se-cgnfs-e-v-1-01.pdf"
ementa: "Atualiza o leiaute da Nota Fiscal de Serviço Eletrônica (NFS-e) de padrão nacional para a Reforma Tributária do Consumo: notas de ajuste de IBS/CBS, grupos do IBS e da CBS, Simples Nacional, bens imóveis, comércio exterior, eventos e condomínios."
data_consulta: "2026-11-27"
versao_texto: "Versão 1.01 (PDF oficial, 11/09/2026)"
---

# Nota Técnica SE/CGNFS-e nº 009, versão 1.01, de 11 de setembro de 2026 (Leiaute da NFS-e na Reforma Tributária do Consumo)

> **Nota editorial.** Texto extraído da camada de texto do PDF oficial da Nota Técnica 009, versão 1.01, divulgado no Portal da NFS-e (gov.br/nfse) (23 páginas), consultado em 27/11/2026. A data do documento (11/09/2026) é a de publicação da versão, lida na capa do PDF. Versão aprovada ou ratificada pelo Ato Técnico Conjunto Sufis/CGIBS nº 7/2026 (`reguladores/rfb/outros-atos/2026/ato-153887-7-2026.md`). Foram removidos a capa, o sumário, os cabeçalhos e rodapés repetidos e a numeração de página. Os 2 títulos de primeiro nível do sumário viraram seções e o texto de cada uma, com os quadros e os leiautes, ficou em bloco de texto que mantém as colunas do PDF. Figuras e imagens do PDF não foram convertidas. Em caso de dúvida, prevalece o PDF. Os Anexos VI (Leiautes e Regras de Negócio da NFS-e, versão 1.04) e VII (Tabela de Indicadores da Operação, versão 1.02) são planilhas .xlsx publicadas no portal da NFS-e (https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica) e foram apenas referenciados, sem conversão. Complementa ou ajusta as Notas Técnicas anteriores da NFS-e, entre elas a nota técnica nacional com IBS e CBS (`reforma-tributaria/cbs-receita-federal/nota-tecnica-nfse-nacional-ibs-cbs.md`). A atualização do portal de 25/11/2026 ainda não tem nota técnica numerada e não consta deste documento.

## 1. Introdução

```text
        Este documento contempla atualizações relativas ao layout da Nota Fiscal de Serviço
eletrônica - NFS-e padrão nacional, complementando ou ajustando o conteúdo anteriormente descrito nas
Notas Técnicas anteriores.
         Junto a esta nota técnica, serão publicados, na seção de documentação técnica do portal da NFS-e
(https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica), atualizações dos dois anexos listados
abaixo:
        •   AnexoVI-LeiautesRN_RTC_IBSCBS-V1.04.01 – NT009.xlsx
            Este anexo possui o layout da NFS-e com as atualizações consolidadas para os ajustes do padrão
            nacional, incluindo os novos grupos referentes ao IBS e à CBS (“Leiaute DPS_NFS-e - RT”) e
            regras de negócio da NFS-e (esse novo layout, ao entrar em Produção, passará a ser identificado
            como ANEXO_I-SEFIN_ADN-DPS_NFSe-SNNFSe, com a devida identificação de versão);
        •   AnexoVII-IndOp_IBSCBS_V1.02.01.xlsx
            Composto por uma tabela com os códigos indicadores da operação que são referenciados no campo
            “cIndOp” da DPS. A tabela foi baseada no art. 11 da Lei Complementar – LC Nº 214, de 16 de
            janeiro de 2025.
        Todas as atualizações dos anexos acima, em relação às suas versões anteriores, listadas nos próximos
tópicos desta NT, em estão destacadas na cor laranja.
        Será publicado no portal da NFS-e o cronograma de implantação das funcionalidades e evoluções
presentes nesta Nota Técnica.
```

## 2. Atualizações

```text
                   2.1 CNPJ Alfanumérico

                   Atualização dos campos “CNPJ” para o “TIPO” caractere (C) para contemplar o novo formato
                   alfanumérico do Cadastro Nacional de Pessoas Jurídicas a ser implementado a partir de julho de 2026.
                   Todos os campos CNPJ tiveram seus tipos alterados: de numérico (N) para caractere (C).

                   2.2 Notas de Ajuste de IBS/CBS

                   •   Atualizações nas ocorrências (coluna “OCOR.”) de alguns grupos e campos para contemplar as
                       possibilidades de notas de ajuste (débito ou crédito) que serão formalizadas por NFS-e, as quais,
                       no AnexoVI-LeiautesRN_RTC_IBSCBS-V1.04.00 – NT009, estão marcadas na cor azul.
                       Exemplo abaixo no grupo “valores”:
NFSe/infNFSe/                     valores        G    -   0-1     -             Grupo de valores referentes ao serviço prestado

                   •   Criação da planilha “NFS-e_AJUSTE_LEIAUTE” com os tipos de notas de ajuste que serão
                       possíveis no contexto da NFS-e e seus respectivos grupos/campos: marcados com X quando não
                       deverão ser informados (DPS) ou não existirão no documento ou com V quando poderão ser

                           informados, entrando nas regras gerais. A planilha é um norteador dos campos que serão
                           necessários para cada um dos tipos de NFS-e de ajuste;
                      •    Criação do grupo “gIBSCBSAjuste”, para informação, na DPS, dos valores de ajuste de IBS e de
                           CBS referentes às NFS-e de ajuste de crédito e de débito:
NFSe/infNFSe/DPS/infDPS/I
                                  gIBSCBSAjuste     G    -    0-1           -               Grupo de informações para as Notas de Ajuste
BSCBS/valores/trib/
NFSe/infNFSe/DPS/infDPS/IBSCB
                                       vIBS         E    N    1-1      1-15V2                           Valor do IBS a ser ajustado.
S/valores/trib/gIBSCBSAjuste/
NFSe/infNFSe/DPS/infDPS/IBSCB
                                       vCBS         E    N    1-1      1-15V2                          Valor da CBS a ser ajustado.
S/valores/trib/gIBSCBSAjuste/

                      •    Deslocamento e atualização do domínio do campo “finNFSe”, bem como a inserção dos campos
                           “tpNFSeDebito” e “tpNFSeCredito”, a fim de contemplar as opções relativas às NFS-e de ajuste
                           de crédito e de débito:
                                                                                              Indicador da finalidade da emissão de NFS-e

NFSe/infNFSe/DPS/infDPS/              finNFSe       E    N   1-1      1                                    0 - NFS-e regular
                                                                                                         1 - NFS-e de crédito
                                                                                                         2 - NFS-e de débito
                                                                                Indicador do tipo de NFS-e de Ajuste de Débito (indicado apenas quando
                                                                                                              finNFSe = 2)

                                                                                            01 - Transferência de créditos para Cooperativas
NFSe/infNFSe/DPS/infDPS/           tpNFSeDebito     E    N   0-1      2                   02 - Anulação de Crédito por Saídas Imunes/Isentas
                                                                                       03 - Débitos de notas fiscais não processadas na apuração
                                                                                                            04 - Multa e juros
                                                                                                05 - Transferência de crédito na sucessão
                                                                                                       06 - Pagamento Antecipado
                                                                                Indicador do tipo de NFS-e de Ajuste de Crédito (indicado apenas quando
                                                                                                              finNFSe = 1)
NFSe/infNFSe/DPS/infDPS/           tpNFSeCredito    E    N   0-1      2
                                                                                                           01 - Multa e juros
                                                                                               05 - Transferência de crédito na sucessão

                      Obs.: Algumas regras relacionadas às notas de ajuste foram inseridas na planilha RN DPS_NFS-e,
                      mas foram tachadas uma vez que essas regras ainda estão em evolução e deverão passar por alterações.
                      Optou-se por mantê-las na planilha, mesmo tachadas, para uma melhor compreensão da sistemática
                      de obrigatoriedade dos campos e grupos que será implementada.

                      2.3 Reestruturação ou merge dos grupos “vDedRed” e “gReeRepRes”

                      Na DPS:

                      •    Os grupos “vDedRed” e “gReeRepRes”, que continham informações relativas aos valores de
                           ajuste (dedução/redução) das bases de cálculo do ISSQN, do IBS e da CBS (esses dois últimos
                           apenas ajustes por documentos), passaram por uma unificação, sendo agora denominado
                           “vAjusteBC”. A alteração visa maior clareza, economia e concentração de campos com o mesmo
                           teor informacional:
                      •
NFSe/infNFSe/DPS/infDPS/v                                                       Grupo de informações relativas aos valores para ajuste dos valores
                                    vAjusteBC       G    -   0-1      -
alores/                                                                                                   de base de cálculo.
NFSe/infNFSe/DPS/infDPS/valore                                                    Valor percentual padrão para ajuste dos valores de base de cálculo do
                                  pAjusteBCISSQN    E    N   0-1    1-3V2
s/vAjusteBC/                                                                                                     ISSQN.
NFSe/infNFSe/DPS/infDPS/valore                                                    Valor monetário padrão para ajuste dos valores de base de cálculo do
                                  vAjusteBCISSQN    E    N   0-1    1-15V2
s/vAjusteBC/                                                                                                     ISSQN

NFSe/infNFSe/DPS/infDPS/v                                                     Grupo de informações de documento utilizado para ajuste dos
                                  documentos      G    -    0-1     -
alores/vAjusteBC/                                                                  valores de base de cálculo (ISSQN e/ou IBS/CBS).
NFSe/infNFSe/DPS/infDPS/v                                   1-
alores/vAjusteBC/documento        docAjusteBC               10                Grupo de informações de documento utilizado para ajuste dos
s                                                 G    -    00      -              valores de base de cálculo (ISSQN e/ou IBS/CBS).
                                                                                                     Tipo de Ajuste:

                                                                                               1 – Alimentação e bebidas/frigobar;
                                                                                                               2 – Materiais;
                                                                                                         3 - Produção Externa;
                                                                                                     4 - Reembolso de despesas;
                                                                                                        5 – Repasse consorciado;
                                                                                                      6 – Repasse plano de saúde;
                                                                                                               7 – Serviços;
                                                                                                 8 – Subempreitada de mão de obra;
                                                                                                         9 - Profissional parceiro;
                                                                                            99 – Outras deduções exclusivas do ISSQN;
                                   tpAjusteBC                                101 – Repasse de remuneração por intermediação de imóveis a demais
                                                                                                   corretores envolvidos na operação
                                                                                  102 – Repasse de valores a fornecedor relativo a fornecimento
                                                                                                 intermediado por agência de turismo
                                                                            103 – Reembolso ou ressarcimento recebido por agência de propaganda e
                                                                           publicidade por valores pagos relativos a serviços de produção externa por
                                                                                                        conta e ordem de terceiro
                                                                            104 – Reembolso ou ressarcimento recebido por agência de propaganda e
                                                                              publicidade por valores pagos relativos a serviços de mídia por conta e
                                                                                                             ordem de terceiro
NFSe/infNFSe/DPS/infDPS/valore                                                                     105 – Glosa de Serviços de Saúde
s/vAjusteBC/documentos/docAjus                                               199 – Outros reembolsos ou ressarcimentos recebidos por valores pagos
teBC/                                             E    N    1-1    1-3                  relativos a operações por conta e ordem de terceiro
                                                                            Descrição do ajuste quando o tipo informado (tpAjusteBC) é "99 – Outras
NFSe/infNFSe/DPS/infDPS/valore                                                                      deduções exclusivas do ISSQN"
s/vAjusteBC/documentos/docAjus    xTpAjusteBC     E    C    0-1   0-150                                              ou
teBC/                                                                       "199 – Outros reembolsos ou ressarcimentos recebidos por valores pagos
                                                                                       relativos a operações por conta e ordem de terceiro".
NFSe/infNFSe/DPS/infDPS/valore                                                         Valor monetário total do documento informado (R$).
s/vAjusteBC/documentos/docAjus      vTotDoc                                  Este é o valor total no documento informado que é passível de ajuste de
teBC/                                             E    N    1-1   1-15V2                                    base(s) de cálculo.
NFSe/infNFSe/DPS/infDPS/valore                                             Valor monetário efetivamente utilizado para ajuste de base(s) de cálculo do
s/vAjusteBC/documentos/docAjus    vAjusteAplic                                        valor do serviço da NFS-e que está sendo emitida (R$).
teBC/                                             E    N    1-1   1-15V2         Deve ser menor ou igual ao valor total do documento (vTotDoc).
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus     dtEmiDoc                                                Data da emissão do documento dedutível.
teBC/                                             E    D    0-1     -                           Ano, mês e dia (AAAA-MM-DD)
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus     dtCompDoc                                             Data da competência do documento dedutível.
teBC/                                             E    D    0-1     -                           Ano, mês e dia (AAAA-MM-DD)
NFSe/infNFSe/DPS/infDPS/v
alores/vAjusteBC/documento        dFeNacional                                Grupo de informações de documentos fiscais eletrônicos que se
s/docAjusteBC/                                    CG   CG   1-1     -                        encontram no repositório nacional.
                                                                           Documento fiscal a que se refere a chaveDfe que seja um dos documentos
                                                                                                     do Repositório Nacional:
                                                                                                           1 = NFS-e;
                                  tipoChaveDFe
NFSe/infNFSe/DPS/infDPS/valore                                                                              2 = NF-e;
s/vAjusteBC/documentos/docAjus                                                                              3 = CT-e;
teBC/dFeNacional/                                 E    N    1-1     1                                      9 = Outro;
NFSe/infNFSe/DPS/infDPS/valore                                             Descrição da DF-e a que se refere a chaveDfe que seja um dos documentos
s/vAjusteBC/documentos/docAjus   xTipoChaveDFe                             do Repositório Nacional. Deve ser preenchido apenas quando tipoChaveDFe
teBC/dFeNacional/                                 E    C    0-1   1-255                                   = 9 (Outro).
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus     chaveDFe                                Chave do Documento Fiscal eletrônico do repositório nacional referenciado
teBC/dFeNacional/                                 E    C    1-1    1-50                  para os casos de operações já tributadas.
NFSe/infNFSe/DPS/infDPS/v
alores/vAjusteBC/documento       docFiscalOutro                            Grupo de informações de documento fiscais, eletrônicos ou não, que
s/docAjusteBC/                                    CG   CG   1-1     -                   não se encontram no repositório nacional.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus   cMunDocFiscal                              Código do município emissor do documento fiscal que não se encontra no
teBC/docFiscalOutro/                              E    N    1-1     7                                repositório nacional
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus     nDocFiscal
teBC/docFiscalOutro/                              E    C    1-1   1-255     Número do documento fiscal que não se encontra no repositório nacional
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus     xDocFiscal
teBC/docFiscalOutro/                              E    C    1-1   1-255                          Descrição do documento fiscal
NFSe/infNFSe/DPS/infDPS/v
alores/vAjusteBC/documento         docOutro
s/docAjusteBC/                                    CG   CG   1-1     -                 Grupo de informações de documento não fiscal.

NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus      nDoc
teBC/docOutro/                                 E    C   1-1   1-255                       Número do documento não fiscal.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus      xDoc
teBC/docOutro/                                 E    C   1-1   1-255                      Descrição do documento não fiscal.
NFSe/infNFSe/DPS/infDPS/v
alores/vAjusteBC/documento         fornec
s/docAjusteBC/                                 G    -   0-1     -          Grupo de informações do fornecedor do serviço prestado
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus      CNPJ
teBC/fornec/                                   CE   C   1-1    14           Número da inscrição federal (CNPJ) do fornecedor de serviço.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus      CPF
teBC/fornec/                                   CE   N   1-1    11            Número da inscrição federal (CPF) do fornecedor do serviço.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus      NIF                               Este elemento só deverá ser preenchido para fornecedores não residentes
teBC/fornec/                                   CE   C   1-1    40                                    no Brasil.
                                                                                        Motivo para não informação do NIF:

NFSe/infNFSe/DPS/infDPS/valore    cNaoNIF                                               0 - Não informado na nota de origem;
s/vAjusteBC/documentos/docAjus                                                                 1 - Dispensado do NIF;
teBC/fornec/                                   CE   N   1-1    1                              2 - Não exigência do NIF;
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus     xNome
teBC/fornec/                                   E    C   1-1   150                        Nome / Razão Social do fornecedor.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus      end
teBC/fornec/                                   G    -   0-1     -                 Grupo de informações do endereço do fornecedor.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus     endNac
teBC/fornec/end/                               CG   -   1-1     -                   Grupo de informações do endereço nacional.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus      cMun                                           Código do município do endereço do fornecedor.
teBC/fornec/end/endNac/                        E    N   1-1    7                                 (Tabela do IBGE)
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus      CEP                                       Código numérico do Endereçamento Postal nacional (CEP)
teBC/fornec/end/endNac/                        E    C   1-1    8                            do endereço do fornecedor.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus     endExt
teBC/fornec/end/                               CG   -   1-1     -                  Grupo de informações do endereço no exterior.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus      cPais                                      Código do país do endereço do prestador do fornecedor.
teBC/fornec/end/endExt/                        E    C   1-1    2                               (Tabela de Países ISO)
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus    cEndPost
teBC/fornec/end/endExt/                        E    C   1-1   1-11     Código alfanumérico do Endereçamento Postal no exterior do fornecedor.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus    xCidade
teBC/fornec/end/endExt/                        E    C   1-1   1-60                   Nome da cidade no exterior do fornecedor.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus   xEstProvReg
teBC/fornec/end/endExt/                        E    C   1-1   1-60         Estado, província ou região da cidade no exterior do fornecedor.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus      xLgr
teBC/fornec/                                   E    C   1-1   1-255            Tipo e nome do logradouro do endereço do fornecedor.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus       nro
teBC/fornec/                                   E    C   1-1   1-60               Número no logradouro do endereço do fornecedor.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus      xCpl
teBC/fornec/                                   E    C   0-1   1-156                   Complemento do endereço do fornecedor.
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus     xBairro
teBC/fornec/                                   E    C   1-1   1-60                       Bairro do endereço do fornecedor.
                                                                                         Número do telefone do fornecedor.
NFSe/infNFSe/DPS/infDPS/valore                                                  (Preencher com o Código DDD + número do telefone.
                                    fone
s/vAjusteBC/documentos/docAjus                                        Nas operações com exterior é permitido informar o código do país + código
teBC/fornec/                                   E    N   0-1   6-20                      da localidade + número do telefone)
NFSe/infNFSe/DPS/infDPS/valore
s/vAjusteBC/documentos/docAjus      email
teBC/fornec/                                   E    C   0-1   1-80                              E-mail do fornecedor.

                      •   Para melhor compreensão acerca do novo grupo, foi criada, no AnexoVI-
                          LeiautesRN_RTC_IBSCBS-V1.04.00 – NT009, a tabela “AJUSTE_BC_REPERCUSSÃO”

                            com os tipos de ajuste e os seus respectivos efeitos nas bases de cálculo do ISSQN, do IBS/CBS e
                            na Receita Bruta do Simples Nacional;

                        •   Os tipos de ajuste a seguir, presentes anteriormente em “vDedRed/documentos/docDedRed/
                            tpDedRed” foram descontinuados na unificação em “vAjusteBC”, pelas seguintes razões:
                               o    “1 – Alimentação e bebidas/frigobar”: nos serviços de hotéis e motéis, quando esses
                                    valores não integram o valor do serviço da diária ou hospedagem (base de cálculo do
                                    ISSQN), alguns Municípios permitiam sua inclusão junto com o valor do serviço
                                    propriamente dito, com “vServ” representando o valor total da operação (valor total
                                    recebido) para entrega do documento ao tomador, com sua respectiva dedução da base de
                                    cálculo do tributo municipal (ainda assim, evidentemente, era necessária a emissão dos
                                    documentos de fornecimento de mercadorias). Ocorre que essa inclusão, por conta do IBS
                                    e da CBS, não pode se dar na NFS-e, pois, afetariam a operacionalização do cálculo desses
                                    tributos para esses fornecimentos (repita-se: de alimentos e bebidas), já registrados em
                                    outros documentos fiscais eletrônicos de emissão desse mesmo fornecedor;
                               o    “3 - Produção Externa”: para ter reflexo também no IBS e na CBS, esse tipo de operação
                                    deve ser registrado pelo valor de ajuste “103”, que melhor o descreve, logo, foi suprimido
                                    por estar redundante;
                               o    “4 - Reembolso de despesas”: os tipos que possuem reflexo também no IBS e na CBS
                                    estão refletidos nos tipos ajuste “103”, “104” ou “199”, logo, foram suprimidos por
                                    estarem redundantes e melhor representados nesses outros tipos. Caso algum outro
                                    reembolso seja admitido pelo Município e não compreendido nos tipos acima descritos,
                                    deve-se utilizar, com autorização municipal e apenas com reflexo na base de cálculo do
                                    ISSQN, o tipo de ajuste “99”.

                        Na NFS-e:

                        •   Alteração do nome do campo “vCalcDR” para “vCalcAjusteBCISSQN” visando maior clareza na
                            descrição e na fórmula da base de cálculo do ISSQN, uma vez que o campo passará a contemplar
                            os ajustes (deduções/reduções) por percentual ou por documentos incidentes sobre a base de
                            cálculo deste tributo:

                                                                             Valor monetário (R$) do ajuste (dedução/redução) da base de cálculo (BC) do
NFSe/infNFSe/valores/            vCalcAjusteBCISSQN   E   N   0-1   1-15V2
                                                                                                               ISSQN.

                        OBS: Importante esclarecer que, em razão das evoluções trazidas neste tópico, a fórmula do cálculo
                        do “vCalcAjusteBCISSQN” passou também por uma evolução em relação à fórmula de “vCalcDR”
                        (antigo campo). Na nova fórmula, se levará em consideração todas as deduções que terão repercussão
                        na base de cálculo do ISSQN (percentual + documentos, desde que o tipo de ajuste por documentos
                        possa ser informado em concomitância com o ajuste percentual). Para mais detalhes, observar as notas
                        explicativas do Anexo e, na planilha de regras de negócio “RN DPS_NFS-e”, a fórmula e as demais
                        informações dispostas.
                        •   Atualização da fórmula de base de cálculo do ISSQN (NFSe/infNFSe/valores/vBC):

                                                                                               Valor da Base de Cálculo do ISSQN (R$) = Valor do Serviço - Desconto
                                                                                                Incondicionado - Ajustes (Deduções/Reduções) - Benefício Municipal
NFSe/infNFSe/valores/                     vBC               E       N       0-1    1-15V2
                                                                                               vBC = vServ - descIncond - (vAjusteBCISSQN + vCalcAjusteBCISSQN) -
                                                                                                                     (vRedBCBM ou VCalcBM)
                        •   Alteração do nome do campo “vCalcReeRepRes” para “vCalcAjusteBCIBSCBS” visando maior
                            clareza na descrição e na fórmula da base de cálculo do IBS e da CBS, que passa a contemplar os
                            ajustes (deduções/reduções ou reembolso, repasse ou ressarcimento) incidentes sobre a base de
                            cálculo destes tributos:
                                                                                                Valor monetário (R$) total relativo a glosa de serviços de saúde ou a
                                                                                             operações de terceiros, objeto de reembolso, repasse ou ressarcimento pelo
NFSe/infNFSe/IBSCBS/valores/      vCalcAjusteBCIBSCBS       E       N       0-1    1-15V2
                                                                                               recebedor, devidamente referenciados, e que não integram da base de
                                                                                                                    cálculo (BC) do IBS e da CBS.

                        •   No mesmo sentido, alteração do título do campo “vCalcDedRedIBSCBS” para
                            “vCalcAjusteBCLocImoveis” que passa a contemplar tão-somente os ajustes (deduções/reduções)
                            da base de cálculo do IBS e da CBS referentes às operações de locação, cessão onerosa ou
                            arrendamento de bens imóveis (subitem 99.03):
                                                                                              Valor monetário (R$) total relativo aos valores de ajuste (dedução/redução)
                                                                                                da Base de Cálculo do IBS e da CBS referentes às operações de locação,
NFSe/infNFSe/IBSCBS/valores/      vCalcAjusteBCLocImoveis       E       N    0-1    1-15V2
                                                                                              cessão onerosa ou arrendamento de bens imóveis. Apenas para os subitens
                                                                                                                                  99.03.

                        •   Atualização da fórmula de base de cálculo do IBS/CBS (NFSe/infNFSe/IBSCBS/valores/vBC):
                                                                                              Valor da base de cálculo (BC) do IBS/CBS antes das reduções para cálculo
                                                                                                                          do tributo bruto.

                                                                                                       vBC = vServ - descIncond – vCalcAjusteBCIBSCBS ou
                                                                                                 vCalcAjusteBCLocImoveis – vISSQN – vPIS - vCOFINS (até 2026)
NFSe/infNFSe/IBSCBS/valores/               vBC                  E       N    1-1    1-15V2
                                                                                                                                  ou

                                                                                                       vBC = vServ - descIncond – vCalcAjusteBCIBSCBS ou
                                                                                                     vCalcAjusteBCLocImoveis – vISSQN (de 2027 até 2032)

                        2.4 Evoluções para o Simples Nacional

                        Para o correto destaque de alíquotas e valores de IBS/CBS na NFS-e, quando esses tributos são
                        apurados pelo Simples Nacional, o layout do documento fiscal passou por evoluções e pelas adaptações
                        que se seguem:

                        Na DPS:

                        •   Atualização do domínio do campo “opSimpNac” para inclusão da opção “4 – Optante Pendente”,
                            buscando atender à situação em que o prestador de serviços tem sua opção pelo regime do Simples
                            Nacional ainda pendente de regularização/julgamento:
                                                                                                                  Situação perante Simples Nacional:

NFSe/infNFSe/DPS/infDPS/prest/r                                                                                            1 - Não Optante;
                                        opSimpNac               E       N    1-1       1
egTrib/                                                                                                   2 - Optante - Microempreendedor Individual (MEI);
                                                                                                 3 - Optante - Microempresa ou Empresa de Pequeno Porte (ME/EPP);
                                                                                                                       4 - Optante Pendente;

                       •   Inserção do campo “regApIBSCBSSN” que permitirá a indicação do regime de apuração tributária
                           do IBS e da CBS para o prestador de serviços optante pelo regime do Simples Nacional ou cuja
                           opção esteja pendente:

                                                                                Regime de Apuração Tributária pelo Simples Nacional para IBS e CBS.
NFSe/infNFSe/DPS/infDPS/prest/r
                                     regApIBSCBSSN     E   N   0-1     1                           1 - IBS e CBS apurados pelo SN;
egTrib/
                                                                                     2 - CBS apurada pelo SN e IBS apurado pelo regime regular;
                                                                                             3 - IBS e CBS apurados pelo regime regular

                       •   Inserção do campo “cAtvSN” a fim de que o prestador de serviços optante pelo regime do Simples
                           Nacional ou cuja opção esteja pendente indique o enquadramento de sua atividade no regime do
                           Simples Nacional, conforme a Lei Complementar nº 123/2006:
                                                                              Código da atividade do Simples Nacional, conforme a Lei Complementar nº
                                                                                                             123/2006:

                                                                                7 - Prestação de serviços, cessão de direitos, de uso ou de espaço com
                                                                                      incidência do ISS, tributados exclusivamente pelo Anexo III.
                                                                              8 - Prestação de serviços contábeis autorizados a pagar o ISS em valor fixo
                                                                                                      em guia do Município - Anexo III.
                                                                                   9 - Prestação de serviços - Sujeitos ao Fator “R” – Anexo III ou V.
                                                                              10 - Prestação de serviços de transporte municipal rodoviário, metroviário,
NFSe/infNFSe/DPS/infDPS/serv/c
                                         cAtvSN        E   N   0-1     2       ferroviário e aquaviário de passageiros relacionados no subitem 16.01 da
Serv/
                                                                                                  lista anexa à LC 116/2003 - Anexo III.
                                                                               11 - Locação de bens móveis e operações com serviços, bens imateriais e
                                                                                direitos, inclusive com bens imóveis, sem incidência de ISS - Anexo III.
                                                                                12 - Prestação de serviços da área da construção civil relacionados nos
                                                                                     subitens 7.02 e 7.05 da lista anexa à LC 116/2003 - Anexo III.
                                                                                13 - Prestação de serviços da área da construção civil relacionados nos
                                                                                     subitens 7.02 e 7.05 da lista anexa à LC 116/2003 - Anexo IV.
                                                                                                  14 - Prestação de serviços - Anexo IV.
                                                                                                       90 - Operações não tributadas.

                       OBS: Em observância à padronização das informações constantes nos documentos fiscais de padrão
                       nacional, manteve-se a numeração ordinal da relação de códigos da atividade do Simples Nacional,
                       conforme a Lei Complementar nº 123/2006, adotando-se, no domínio do referido campo, apenas
                       aqueles aplicáveis às operações abrangidas pela NFS-e.
                           o      Foram realizados ajustes nas regras de negócio do campo Código da Atividade do Simples
                                  Nacional (“cAtvSN”), com o objetivo de garantir que a obrigatoriedade/validação das
                                  informações seja bicondicional, ou seja, a primeira informação só é válida se a segunda
                                  informação também for, e vice-versa.

                       Na NFS-e:

                       •   Inserção do campo “vReceitaBrutaSN” que representará o valor da receita bruta para os optantes
                           pelo regime do Simples Nacional e servirá de base para a apuração dos tributos abarcados por este
                           regime:
                                                                                    Valor da Receita Bruta para os Optantes do Simples Nacional.

                                                                                   vReceitaBrutaSN = vServ - descIncond - vCalcAjusteBCIBSCBS -
NFSe/infNFSe/IBSCBS/valores/         vReceitaBrutaSN   E   N   0-1   1-15V2                           vCalcAjusteBCISSQN*

                                                                                    *apenas quando o valor calculado se referir à soma a partir de
                                                                                     docAjusteBC/tpAjusteBC do tipo = "9 - Profissional parceiro"

                             o    Alteração da descrição do campo e das notas explicativas, juntamente com ajustes nas regras
                                  de negócio, de forma a contemplar, na montagem da referida base de cálculo
                                  (“vReceitaBrutaSN”), a segregação entre Receita Interna e Externa, que se dará através do
                                  indicador “tpRBSN”, presente junto ao cClassTrib informado (de acordo com os indicadores
                                  vinculados ao respectivo código);

     Valor da Receita Bruta para os Optantes do Simples Nacional.                   A segregação entre Receita Interna e Externa se dará pelo indicador "tpRBSN" do
                                                                                                             cClassTrib, descritos abaixo:
     Se o indicador tpRBSN para o código da classificação tributária
    (cClassTrib) informado for igual a 0 (Não é receita bruta), então                                           1 - Receita bruta - interna
                         vReceitaBrutaSN = 0.                                                     2 - Receita bruta - interna sem cálculo de IBS e CBS
                                                                                                          3 - Receita bruta - exportação direta
     Se o indicador tpRBSN para o código da classificação tributária                                     4 - Receita bruta - exportação indireta
  (cClassTrib) informado for diferente de 0 (Não é receita bruta), então                       5 - Receita Bruta - mercado interno e exportação (50/50)
    vReceitaBrutaSN = vServ - descIncond - vCalcAjusteBCIBSCBS -                                                  0 - Não é receita bruta
                         vCalcAjusteBCISSQN*                                                             9 - Fornecimento incompatível com SN

     *apenas quando o valor calculado se referir à soma a partir de              Deve-se deduzir da receita bruta os valores informados pelo salão quando tpAjusteBC =
      docAjusteBC/tpAjusteBC do tipo = "9 - Profissional parceiro"                                              9 ("Profissional parceiro")

                    • Criação do grupo “gTribSN” que conterá as informações da composição do valor do IBS e da CBS
                      para os optantes pelo regime do Simples Nacional com regime de apuração da CBS e/ou do IBS por
                      esse regime de apuração:
NFSe/infNFSe/IBSCBS/totCIB                                                                   Grupo de informações da composição do valor do IBS e da CBS para
                                           gTribSN             G    -      0-1        -
S/                                                                                                                      o Simples Nacional
NFSe/infNFSe/IBSCBS/totCIBS/g                                                                   Alíquota do IBS Total calculada apenas para os Optantes do Simples
                                           pIBSSN              E    N      0-1      1-2V2
TribSN/                                                                                                                       Nacional.
NFSe/infNFSe/IBSCBS/totCIBS/g
                                           vIBSSN              E    N      0-1     1-15V2                Valor do IBS para os Optantes do Simples Nacional
TribSN/
NFSe/infNFSe/IBSCBS/totCIBS/g
                                           pCBSSN              E    N      1-1      1-2V2          Alíquota da CBS apenas para os Optantes do Simples Nacional.
TribSN/
NFSe/infNFSe/IBSCBS/totCIBS/g
                                           vCBSSN              E    N      1-1     1-15V2                Valor da CBS para os Optantes do Simples Nacional
TribSN/

                             o    Dadas as alterações promovidas nas regras do campo “vReceitaBrutaSN”, as regras de negócio
                                  aplicadas aos campos “vIBSSN” e vCBSSN” também foram ajustadas, visando, da mesma
                                  forma, atender às regras de segregação entre Receita Interna e Externa:
                        OBS: Em razão da necessidade de criação do grupo acima para o correto destaque do IBS e da CBS
                        para os optantes ou pendentes com regime de apuração desses tributos pelo Simples Nacional, foi
                        necessária a mudança da ocorrência (OCOR.) em alguns campos/grupos na NFS-e que antes eram
                        obrigatórios, são eles: “vIBSTot”, “gIBSUFTot”, “gIBSMunTot”, “pCredPresCBS”, “vCredPresCBS”
                        e “vCBS".

                        2.5 Reinserção do campo “indFinal”

                        Reinserção do campo “indFinal” para indicação de operações que se configurem como de uso ou
                        consumo pessoal, na forma do art. 57, da Lei Complementar 214/2025:
                                                                                                       Indica operação de uso ou consumo pessoal. (art. 57)
NFSe/infNFSe/DPS/infDPS/IBSCB
                                           indFinal            E      N    0-1        1
S/                                                                                                                            0 - Não
                                                                                                                              1 - Sim

                        2.6 Reestruturação das Informações de Operações com Bens Imóveis

                     As informações relativas a operações envolvendo bens imóveis — exceto obras —, que serão
                     formalizadas por meio de NFS-e, tanto aquelas situadas no campo de incidência do ISSQN quanto as
                     enquadradas como novos fatos geradores (locação, cessão onerosa ou arrendamento de bens imóveis),
                     passaram por um conjunto de evoluções. As principais alterações são as seguintes:
                     Na DPS:

                     Reestruturação do grupo “imovel”:
                     •    Criação do grupo “gLocacao” referente às informações decorrentes, exclusivamente, de operações
                          de locação, cessão onerosa ou arrendamento de bens imóveis, que servirão de base para a definição
                          dos valores de “vServ”, “vDescIncond” e “vDescCond”, do grupo de valores do serviço prestado
                          na DPS;
                     •    Criação do grupo “gUnidImob” que permitirá a informação das unidades imobiliárias envolvidas
                          nas operações. Neste grupo poderão ser relacionados até 99 (noventa e nove) registros, permitindo
                          a emissão de uma única NFS-e em operações que envolvam 2 (duas) ou mais unidades imobiliárias
                          que estejam num mesmo contexto: mesmos atores (Prestador/Fornecedor e Tomador/Adquirente),
                          mesmo município (cMun) e mesmo percentual de copropriedade (“pCopropriedade”);
                     •    Alteração do nome do grupo “gDedRedIBSCBS” para “gAjusteBCLocImoveis”, assim como dos
                          nomes dos campos relacionados (“tpAjusteBCLocImoveis”, “xTpAjusteBCLocImoveis” e
                          “vAjusteBCLocImoveis”), de forma a melhor identificar os grupos/campos de informações de
                          ajustes (deduções/reduções) relacionados às operações de locação, cessão onerosa ou
                          arrendamento de bens imóveis. As informações constantes no grupo “gAjusteBCLocImoveis” irão
                          compor, na NFS-e, o campo “vCalcAjusteBCLocImoveis” que irá deduzir a base de cálculo do
                          IBS/CBS dessas operações, conforme descrito no tópico 2.3;
NFSe/infNFSe/DPS/infDPS/I                                                         Grupo de informações de operações relacionadas a bens
                                     imovel         G    -    0-1       -
BSCBS/                                                                                            imóveis, exceto obras.
NFSe/infNFSe/DPS/infDPS/IBSCB                                                              Código do município do endereço do imóvel
                                      cMun          E    N     1-1      7
S/imovel/                                                                                              (Tabela do IBGE)

                                                                              Grupo de informações relativas às operações de locação, cessão
NFSe/infNFSe/DPS/infDPS/IBSCB       gLocacao        G    -    0-1       -
                                                                                        onerosa ou arrendamento de bens imóveis
S/imovel/
                                                                                                   Percentual de Copropriedade
NFSe/infNFSe/DPS/infDPS/IBSCB
                                  pCopropriedade    E    N     1-1    1-3V2        (Caso só haja um locador, cedente ou arrendador, informar o
S/imovel/gLocacao/
                                                                                              Percentual de Copropriedade de 100%)
                                                                                             Valor total da operação com bem imóvel
                                                                                (Informar o valor total da operação de locação, cessão onerosa ou
                                                                                  arrendamento de bens imóveis, associado ao aluguel, renda ou
NFSe/infNFSe/DPS/infDPS/IBSCB
                                    vTotOper        E    N     1-1   1-15V2              equivalente, conforme art. 255 da LC 214/2025).
S/imovel/gLocacao/
                                                                                   Não deverá ser inserido neste campo o valor proporcional do
                                                                                                          coproprietário.
                                                                                             Valor total do Desconto Incondicionado
NFSe/infNFSe/DPS/infDPS/IBSCB
                                  vDescIncondTot    E    N     0-1   1-15V2     (Informar o valor total do desconto incondicionado na operação de
S/imovel/gLocacao/
                                                                                   locação, cessão onerosa ou arrendamento de bens imóveis)

                                                                                              Valor total do Desconto Condicionado
NFSe/infNFSe/DPS/infDPS/IBSCB
                                  vDescCondTot      E    N     0-1   1-15V2     (Informar o valor total do desconto incondicionado na operação de
S/imovel/gLocacao/
                                                                                   locação, cessão onerosa ou arrendamento de bens imóveis)

                                                                                                   Data de vencimento original
                                                                                                  Ano, Mês e Dia (AAAA-MM-DD)
NFSe/infNFSe/DPS/infDPS/IBSCB
                                    dVencOrig       E    D     0-1      -     (Informar data de vencimento original do aluguel, renda ou equivalente
S/imovel/gLocacao/
                                                                                 na operação de locação, cessão onerosa ou arrendamento de bens
                                                                                                             imóveis)
NFSe/infNFSe/DPS/infDPS/I                                                     Grupo de informações relativas às unidades imobiliárias objeto
                                   gUnidImob        G    -    0-99      -
BSCBS/imovel/                                                                                         da operação

                                                                                                           Inscrição imobiliária fiscal
NFSe/infNFSe/DPS/infDPS/IBSCB
                                     inscImobFisc        E    C    0-1     1-30      (código fornecido pela prefeitura para a identificação da obra ou para
S/imovel/gUnidImob/
                                                                                                        fins de recolhimento do IPTU)
NFSe/infNFSe/DPS/infDPS/IBSCB
                                         cCIB            CE   C    1-1       8                  Código do Cadastro Imobiliário Brasileiro - CIB
S/imovel/gUnidImob/
NFSe/infNFSe/DPS/infDPS/I
                                         end             CG   -    1-1       -                Grupo de informações do endereço do imóvel.
BSCBS/imovel/gUnidImob/
                                                                                    Código numérico do Endereçamento Postal nacional (CEP) do endereço
NFSe/infNFSe/DPS/infDPS/IBSCB
                                         CEP             E    N    1-1       8                                  do imóvel.
S/imovel/gUnidImob/end/
                                                                                                   (Informar os zeros não significativos)
NFSe/infNFSe/DPS/infDPS/IBSCB
                                         xLgr            E    C    1-1     1-255              Tipo e nome do logradouro do endereço do imóvel.
S/imovel/gUnidImob/end
NFSe/infNFSe/DPS/infDPS/IBSCB
                                          nro            E    C    1-1      1-60                Número no logradouro do endereço do imóvel.
S/imovel/gUnidImob/end
NFSe/infNFSe/DPS/infDPS/IBSCB
                                         xCpl            E    C    0-1     1-156                    Complemento do endereço do imóvel.
S/imovel/gUnidImob/end
NFSe/infNFSe/DPS/infDPS/IBSCB
                                        xBairro          E    C    0-1      1-60                        Bairro do endereço do imóvel.
S/imovel/gUnidImob/end
                                                                                           Grupo de informações relativas a valores de ajuste
NFSe/infNFSe/DPS/infDPS/I        gAjusteBCLocImovei                                      (dedução/redução) da Base de Cálculo do IBS e da CBS
                                                         G    -    0-10      -
BSCBS/imovel/gUnidImob/                   s                                              referentes às operações de locação, cessão onerosa ou
                                                                                                      arrendamento de bens imóveis
                                                                                      Tipo de parcela não integrante da base de cálculo do IBS e da CBS

                                                                                          01 = Tributos inclusos no aluguel ou equivalente (Ex.: IPTU,
                                                                                         Contribuição de melhoria) - apenas para NBS 1.1002.10.00 ou
NFSe/infNFSe/DPS/infDPS/IBSCB                                                                                    1.1002.20.00
S/imovel/gUnidImob/gAjusteBCLo   tpAjusteBCLocImoveis    E    N    1-1       2      02 = Emolumento incluso no aluguel ou equivalente - apenas para NBS
cImoveis/                                                                                                1.1002.10.00 ou 1.1002.20.00
                                                                                    03 = Condomínio incluso no aluguel ou equivalente - apenas para NBS
                                                                                                         1.1002.10.00 ou 1.1002.20.00
                                                                                            04 = Redutor Social - apenas para a NBS 1.1002.10.00
                                                                                            99 = Outras parcelas inclusas no aluguel ou equivalente
NFSe/infNFSe/DPS/infDPS/IBSCB                                                       Descrição do tipo de parcela não integrante da base de cálculo do IBS e
S/imovel/gUnidImob/gAjusteBCLo   xTpAjusteBCLocImoveis   E    C    0-1     0-150     da CBS quando a opção for "99 = Outras parcelas inclusas no aluguel
cImoveis/                                                                                                       ou equivalente".
                                                                                    Valor monetário utilizado para não inclusão na base de cálculo do IBS e
NFSe/infNFSe/DPS/infDPS/IBSCB                                                                    da CBS da NFS-e que está sendo emitida (R$).
S/imovel/gUnidImob/gAjusteBCLo    vAjusteBCLocImoveis    E    N    1-1     1-15V2    (Informar o valor total da parcela não integrante da base de cálculo -
cImoveis/                                                                             IPTU, Condomínio, Redutor social, etc. -, não devendo ser inserido o
                                                                                                      valor proporcional do coproprietário)

                      •    Em razão da criação do grupo “gLocacao” em “imovel”, foram promovidas alterações nas regras
                           de validação dos campos “vServ”, “vDescIncond” e “vDescCond”:
                                                                                                       Valor monetário do serviço (R$).
NFSe/infNFSe/DPS/infDPS/valore
                                        vServ            E    N    1-1     1-15V2
s/vServPrest/                                                                         (Para os códigos de tributação nacional do subitem 99.03, vServ =
                                                                                                         pCopropriedade x vTotOper)
NFSe/infNFSe/DPS/infDPS/v                                                            Grupo de informações relativas aos descontos condicionados e
                                  vDescCondIncond        G    -    0-1       -
alores/                                                                                                     incondicionados
                                                                                             Valor monetário do desconto incondicionado (R$).
NFSe/infNFSe/DPS/infDPS/valore
                                     vDescIncond         E    N    0-1     1-15V2
s/vDescCondIncond/                                                                  (Para os códigos de tributação nacional do subitem 99.03, vDescIncond
                                                                                                     = pCopropriedade x vDescIncondTot)
                                                                                               Valor monetário do desconto condicionado (R$).
NFSe/infNFSe/DPS/infDPS/valore
                                      vDescCond          E    N    0-1     1-15V2
s/vDescCondIncond/                                                                  (Para os códigos de tributação nacional do subitem 99.03, vDescCond =
                                                                                                       pCopropriedade x vDescCondTot)

                      2.7 Alteração do nome do grupo “gLocBensMoveis” para “bensMoveis”

                      A alteração objetiva padronizar os nomes dos grupos relacionados aos novos fatos geradores (“imovel"
                      e “bensMoveis”). Além disso, o grupo passou a permitir a inserção de até 1.000 (mil) registros:
NFSe/infNFSe/DPS/infDPS/I                                                             Grupo de informações relativas aos bens móveis objetos de
                                     bensMoveis          G    -   0-1000     -
BSCBS/                                                                                                         locação

                     2.8 Criação do grupo “gPgtoVinc”

                     Grupo responsável pelas informações da vinculação da NFS-e à transação de pagamento relacionada,
                     quando essas informações puderem ser disponibilizadas até o momento da emissão do documento
                     fiscal (evento com mesma estrutura será implementado para que seja registrado nos casos em que a
                     informação de pagamento só poderá ser informada após a emissão do documento fiscal). Poderão ser
                     vinculadas até 99 (noventa e nove) transações de pagamento para uma mesma NFS-e:
NFSe/infNFSe/DPS/infDPS/I                                                               Grupo de informações da vinculação com a transação de
                                  gPgtoVinc       G       -         0-1       -
BSCBS/                                                                                                       pagamento
NFSe/infNFSe/DPS/infDPS/I
                                     pgto         G       -     1-99          -                Dados dos pagamentos vinculados à NFS-e
BSCBS/gPgtoVinc/
NFSe/infNFSe/DPS/infDPS/IBSCB
                                     nPag         E    N            1-1       3                     Numerador único de cada pagamento
S/gPgtoVinc/pgto/
NFSe/infNFSe/DPS/infDPS/IBSCB                                                          Identificador específico da transação financeira, de acordo com o
                                  idTransacao     E       C         1-1      2-35
S/gPgtoVinc/pgto/                                                                                                  pagamento.
                                                                                                    Código do meio de pagamento utilizado:

                                                                                                                15 = Boleto
NFSe/infNFSe/DPS/infDPS/IBSCB                                                                            17 = Pix QRCode dinâmico
                                  tpMeioPgto      E    N            1-1       2
S/gPgtoVinc/pgto/                                                                                                18 = TED
                                                                                                     20 = PIX chave ou QRCode estático
                                                                                                            23 = Pix automático
                                                                                                          24 = TEF / booktransfer
NFSe/infNFSe/DPS/infDPS/IBSCB                                                       CNPJ completo do recebedor do pagamento (fornecedor, plataforma, ou
                                  CNPJReceb       E       C         1-1      14
S/gPgtoVinc/pgto/                                                                          outra entidade que receba o pagamento do adquirente).

                                                                                      CNPJ base da instituição financeira ou de pagamento utilizada pelo
NFSe/infNFSe/DPS/infDPS/IBSCB                                                        recebedor do pagamento (fornecedor, plataforma, ou outra entidade
                                 CNPJBasePSP      E       C         1-1       8
S/gPgtoVinc/pgto/                                                                                                     que
                                                                                                    receba o pagamento do adquirente).

                     2.9 Inserção do campo “verCalcIBSCBS” na NFS-e

                     A alteração tem por objetivo destacar, no documento fiscal, informação acerca da versão da
                     Calculadora de Tributos (IBS/CBS) utilizada na geração da NFS-e. Trata-se de informação que será
                     gerada pela SEFIN Nacional da NFS-e, ou seja, notas autorizadas/geradas a partir dos emissores
                     públicos nacionais (“ambGer” = 2). Dessa forma, essa informação não será exigida para notas
                     autorizadas em ambientes próprios municipais e posteriormente compartilhadas com o repositório
                     nacional (ADN).

NFSe/infNFSe/                    verCalcIBSCBS    E   C       0-1     1-20          Versão da Calculadora de Tributos (IBS/CBS) que gerou a NFS-e.

                     2.10 Inclusão de regras de validação dos endereços do Tomador/Adquirente e do Destinatário
                     e repercussão na definição do local de incidência do ISSQN em operações com o código de
                     tributação nacional 17.05

                     Na Sefin Nacional, os endereços do Tomador/Adquirente e do Destinatário deverão ser validados com
                     base nas informações constantes dos cadastros CNPJ/CPF. Essa exigência advém do art. 11 da Lei
                     Complementar nº 214/2025, bem como dos arts. 12 dos regulamentos do IBS e da CBS: Resolução
                     CGIBS nº 6, de 30 de abril de 2026; e Decreto nº 12.955, de 29 de abril de 2026, respectivamente.
                     Em razão dessa necessidade e com o objetivo de assegurar maior conformidade no tratamento de
                     operações classificadas sob o código 17.05 da Lista de Serviços prevista na Lei Complementar nº
                     116/2003, referente ao fornecimento de mão de obra, inclusive em caráter temporário, mediante
                     disponibilização de empregados, trabalhadores avulsos ou temporários contratados pelo prestador de

serviços, cujo local de incidência do ISSQN corresponde ao local do estabelecimento do tomador
do serviço, ficam estabelecidas as regras a seguir.
As alterações visam contemplar situações em que, especialmente em operações envolvendo entes
governamentais, o documento fiscal seja emitido para um estabelecimento central responsável pela
contratação do serviço (Tomador/Adquirente), enquanto o serviço seja efetivamente usufruído por
outro estabelecimento da mesma entidade/titularidade (Destinatário), ao qual poderá ser atribuída a
incidência do ISSQN, a depender da respectiva legislação municipal.
       1. Validação cadastral para Todas as Operações

               Para todas as operações (todos os subitens), a DPS, ou a NFS-e no caso dos
       compartilhamentos pelos municípios, deverá ser rejeitada quando o código IBGE do município
       informado divergir daquele constante no respectivo cadastro do Tomador/Adquirente e/ou do
       Destinatário.

       2. Definição do local de incidência do ISSQN para os Serviços do Subitem 17.05

           2.1 Utilização do endereço do Tomador/Adquirente

                   O município do endereço do Tomador/Adquirente será definido como local de
           incidência do ISSQN nas seguintes situações:
               •       quando o Destinatário não for informado (ele é o próprio adquirente);
               •       quando o Destinatário for identificado por CNPJ e a raiz do seu CNPJ
               (primeiros 8 dígitos) for diferente da raiz do CNPJ do Tomador/Adquirente;
               •       quando o Destinatário for identificado por CPF e o CPF informado for
               diferente do CPF do Tomador/Adquirente.
           2.2 Utilização do endereço do Destinatário

                  O município do endereço do Destinatário será utilizado como local de incidência
           do ISSQN nas seguintes situações:
               •       quando o Destinatário for identificado por CNPJ e a raiz do seu CNPJ
               (primeiros 8 dígitos) for igual à raiz do CNPJ do Tomador/Adquirente;
               •     quando o Destinatário for identificado por CPF e o CPF informado for o
               mesmo do Tomador/Adquirente.
Para o subitem 17.05, exclusivamente nas hipóteses previstas nesse item (2.2), acima, será
permitida ao emitente a alteração do endereço do Destinatário, constituindo exceção à regra geral
de validação cadastral. Nesses casos, não deverá ocorrer rejeição da DPS (ou da NFS-e) em razão de
divergência entre o código IBGE informado para o endereço do Destinatário e aquele constante em
seu cadastro.

2.11   Reposicionamento do campo “indDest” e do grupo “dest” para o grupo “infDPS”

Reposicionamento do campo indicador do destinatário (“indDest”) e do grupo de informações relativas
ao destinatário dos serviços/operações (“dest”) para inseri-los na raiz do grupo de informações da

                      Declaração de Prestação de Serviços – DPS (“infDPS”), logo após os campos relativos ao
                      tomador/adquirente (“toma”), visando melhor adequar o layout à lógica sistêmica atual das “Pessoas”
                      participantes da NFS-e.
                                                                                                  A respeito do Destinatário dos serviços:

                                                                                  0 – o destinatário é o próprio tomador/adquirente identificado na NFS-e
NFSe/infNFSe/DPS/infDPS/                       indDest     E    N   1-1    1                          (tomador=adquirente=destinatário);
                                                                                  1 – o destinatário não é o próprio adquirente, podendo ser outra pessoa,
                                                                                   física ou jurídica (ou equiparada), ou um estabelecimento diferente do
                                                                                         indicado como tomador (tomador=adquirente≠destinatário);
NFSe/infNFSe/DPS/infDPS/                        dest       G    -   0-1     -                 Grupo de informações relativas ao Destinatário
                                                                                  Número da inscrição no Cadastro Nacional de Pessoa Jurídica (CNPJ) do
NFSe/infNFSe/DPS/infDPS/dest/                   CNPJ       CE   C   1-1    14
                                                                                                            destinatário de serviço
                                                                                     Número da inscrição no Cadastro Nacional de Pessoa Física (CPF) do
NFSe/infNFSe/DPS/infDPS/dest/                   CPF        CE   N   1-1    11
                                                                                                            destinatário do serviço
                                                                                     Número de identificação fiscal fornecido por órgão de administração
NFSe/infNFSe/DPS/infDPS/dest/                    NIF       CE   C   1-1    40
                                                                                                             tributária no exterior
                                                                                                      Motivo para não informação do NIF:

NFSe/infNFSe/DPS/infDPS/dest/                  cNaoNIF     CE   N   1-1    1                        0 - Não informado na nota de origem;
                                                                                                            1 - Dispensado do NIF;
                                                                                                           2 - Não exigência do NIF;
NFSe/infNFSe/DPS/infDPS/dest/                  xNome        E   C   1-1   1-150                   Nome / Nome Empresarial do destinatário
NFSe/infNFSe/DPS/infDPS/dest/                    end        G   -   0-1     -           Grupo de informações do endereço do destinatário do serviço.
NFSe/infNFSe/DPS/infDPS/dest/end/              endNac      CG   -   1-1     -                    Grupo de informações do endereço nacional.
                                                                                         Código do município do endereço do destinatário do serviço.
NFSe/infNFSe/DPS/infDPS/dest/end/endNac/        cMun       E    N   1-1    7
                                                                                                                (Tabela do IBGE)
                                                                                  Código numérico do Endereçamento Postal nacional (CEP) do endereço do
NFSe/infNFSe/DPS/infDPS/dest/end/endNac/        CEP        E    N   1-1    8                                destinatário do serviço.
                                                                                                    (Informar os zeros não significativos)
NFSe/infNFSe/DPS/infDPS/dest/end/              endExt      CG   -   1-1     -                  Grupo de informações do endereço no exterior.
                                                                                           Código do país do endereço do destinatário do serviço.
NFSe/infNFSe/DPS/infDPS/dest/end/endExt/        cPais      E    C   1-1    2
                                                                                                             (Tabela de Países ISO)
                                                                                  Código alfanumérico do Endereçamento Postal no exterior do destinatário
NFSe/infNFSe/DPS/infDPS/dest/end/endExt/      cEndPost     E    C   1-1   1-11
                                                                                                                  do serviço.
NFSe/infNFSe/DPS/infDPS/dest/end/endExt/       xCidade     E    C   1-1   1-60             Nome da cidade no exterior do destinatário do serviço.
                                                                                     Estado, província ou região da cidade no exterior do destinatário do
NFSe/infNFSe/DPS/infDPS/dest/end/endExt/     xEstProvReg   E    C   1-1   1-60
                                                                                                                    serviço.
NFSe/infNFSe/DPS/infDPS/dest/end/               xLgr       E    C   1-1   1-255      Tipo e nome do logradouro do endereço do destinatário do serviço.
NFSe/infNFSe/DPS/infDPS/dest/end/                nro       E    C   1-1    1-60        Número no logradouro do endereço do destinatário do serviço.
NFSe/infNFSe/DPS/infDPS/dest/end/               xCpl       E    C   0-1   1-156             Complemento do endereço do destinatário do serviço.
NFSe/infNFSe/DPS/infDPS/dest/end/              xBairro     E    C   1-1    1-60                 Bairro do endereço do destinatário do serviço.
                                                                                                     Número do telefone do destinatário.
                                                                                    (Preencher com o Código DDD + número do telefone. Nas operações
NFSe/infNFSe/DPS/infDPS/dest/                   fone       E    N   0-1   6-20
                                                                                  com exterior é permitido informar o código do país + código da localidade
                                                                                                            + número do telefone)
NFSe/infNFSe/DPS/infDPS/dest/                   email      E    C   0-1   1-80                              E-mail do destinatário.

                      2.12 Inclusão de novos campos e atualizações do grupo de informações sobre transações entre
                      residentes ou domiciliados no Brasil com residentes ou domiciliados no exterior (“comExt”)

                      Por exigência dos regulamentos do IBS e da CBS (Resolução CGIBS Nº 6, de 30 de abril de 2026, e
                      Decreto Nº 12.955, de 29 de abril de 2026), foram criados os campos “nFatura”, “vFatura” e
                      “nContCambio”, de forma a permitir a inclusão do número da fatura ou de documento que comprove
                      a transação de comércio exterior, seu respectivo valor, além do número do contrato de câmbio ou
                      documento que acobertou o pagamento da operação.
                      Por outro lado, foram atualizados os campos “mdPrestacao”, para incluir o domínio “5 - Consumo
                      concomitante no território nacional e exterior”, hipótese em que será observada as seguintes regras
                      de emissão:
                                •          Na Importação: informar no campo “vServ” da DPS apenas a parcela consumida no
                                país;

                               •      Na Exportação: informar no campo “vServ” da DPS apenas a parcela exportada.
                               Nesse caso, uma outra NFS-e deve ser emitida para a parcela consumida no país (esta não se
                               enquadrando como exportação).
                      Na mesma esteira, os campos “nDI” e “nRE” foram renomeados para “nDUIMP” e “nDUE”,
                      respectivamente, visando atualizar o layout às novas terminologias aplicadas às declarações relativas
                      ao comércio exterior.
                      Já o campo “tpMoeda” passará a ter validação das informações inseridas, conforme a tabela de moedas
                      do Banco Central do Brasil.
                      Por fim, a partir de 01/01/2027, o domínio "Desconhecido (tipo não informado na nota de origem)"
                      previsto atualmente em alguns campos que compõem o grupo “comExt”, p. ex. “mdPrestacao” e
                      “vincPrest”, não será admitido nas NFS-e compartilhadas pelos municípios ao Ambiente de
                      Dados Nacional (ADN). Todas as informações compartilhadas deverão conter valor válido dentre os
                      domínios definidos para o respectivo campo, conforme layout vigente. A medida visa elevar a
                      consistência, a padronização e a qualidade dos dados compartilhados nacionalmente.
                                                                               Grupo de informações sobre transações entre residentes ou
NFSe/infNFSe/DPS/infDPS/serv/            comExt      G   -   0-1     -
                                                                             domiciliados no Brasil com residentes ou domiciliados no exterior
                                                                                                     Modo de Prestação:

                                                                                 0 - Desconhecido (tipo não informado na nota de origem);
                                                                                                      1 - Transfronteiriço;
NFSe/infNFSe/DPS/infDPS/serv/comExt/   mdPrestacao   E   N   1-1     1
                                                                                                    2 - Consumo no Brasil;
                                                                                         3 - Movimento Temporário de Pessoas Físicas;
                                                                                                   4 - Consumo no Exterior;
                                                                                5 - Consumo concomitante no território nacional e exterior;
                                                                                              Vínculo entre as partes no negócio:

                                                                                              0 - Sem vínculo com o Tomador/Prestador
                                                                                                             1 - Controlada;
                                                                                                            2 - Controladora;
NFSe/infNFSe/DPS/infDPS/serv/comExt/     vincPrest   E   N   1-1     1
                                                                                                               3 - Coligada;
                                                                                                                4 - Matriz;
                                                                                                          5 - Filial ou sucursal;
                                                                                                            6 - Outro vínculo;
                                                                                  9 - Desconhecido (tipo não informado na nota de origem);
                                                                                              Identifica a moeda da transação comercial.
NFSe/infNFSe/DPS/infDPS/serv/comExt/     tpMoeda     E   N   1-1     3
                                                                                             O usuário deve informar o código da moeda.
                                                                                Número da identificação da fatura de serviços ou do documento que
NFSe/infNFSe/DPS/infDPS/serv/comExt/     nFatura     E   N   0-1    1-20    comprove a transação (DECRETO Nº 12.955, DE 29 DE ABRIL DE 2026, Art.
                                                                                                                 74 § 1º )
                                                                                 Valor total da fatura de serviços ou do documento que comprove a
NFSe/infNFSe/DPS/infDPS/serv/comExt/     vFatura     E   N   0-1   1-15V2      transação, expresso na moeda identificada em tpMoeda (DECRETO Nº
                                                                                          12.955, DE 29 DE ABRIL DE 2026, Art. 74, §1º).
                                                                             Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador
                                                                                                                do serviço:

                                                                                 00 - Desconhecido (tipo não informado na nota de origem);
                                                                                                          01 - Nenhum;
                                                                            02 - ACC - Adiantamento sobre Contrato de Câmbio – Redução a Zero do IR
                                                                                                             e do IOF;
NFSe/infNFSe/DPS/infDPS/serv/comExt/   mecAFComexP   E   N   1-1     2
                                                                              03 - ACE – Adiantamento sobre Cambiais Entregues - Redução a Zero do
                                                                                                           IR e do IOF;
                                                                                           04 - BNDES-Exim Pós-Embarque – Serviços;
                                                                                            05 - BNDES-Exim Pré-Embarque - Serviços;
                                                                                            06 - FGE - Fundo de Garantia à Exportação;
                                                                                                   07 - PROEX - EQUALIZAÇÃO
                                                                                                   08 - PROEX - Financiamento;
                                                                             Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo tomador
                                                                                                            do serviço:

                                                                                 00 - Desconhecido (tipo não informado na nota de origem);
                                                                                                           01 - Nenhum;
NFSe/infNFSe/DPS/infDPS/serv/comExt/   mecAFComexT   E   N   1-1     2
                                                                                              02 - Adm. Pública e Repr. Internacional;
                                                                                  03 - Aluguéis e Arrend. Mercantil de maquinas, equip., embarc. e
                                                                                                             aeronaves;
                                                                            04 - Arrendamento Mercantil de aeronave para empresa de transporte aéreo
                                                                                                              público;

                                                                                                05 - Comissão a agentes externos na exportação;
                                                                                    06 - Despesas de armazenagem, mov. e transporte de carga no exterior;
                                                                                                          07 - Eventos FIFA (subsidiária);
                                                                                                                 08 - Eventos FIFA;
                                                                                       09 - Fretes, arrendamentos de embarcações ou aeronaves e outros;
                                                                                                             10 - Material Aeronáutico;
                                                                                                        11 - Promoção de Bens no Exterior;
                                                                                                   12 - Promoção de Dest. Turísticos Brasileiros;
                                                                                                        13 - Promoção do Brasil no Exterior;
                                                                                                        14 - Promoção Serviços no Exterior;
                                                                                                                    15 - RECINE;
                                                                                                                   16 - RECOPA;
                                                                                          17 - Registro e Manutenção de marcas, patentes e cultivares;
                                                                                                                  18 - REICOMP;
                                                                                                                     19 - REIDI;
                                                                                                                   20 - REPENEC;
                                                                                                                    21 - REPES;
                                                                                                                  22 - RETAERO;
                                                                                                                     23 - RETID;
                                                                                          24 - Royalties, Assistência Técnica, Científica e Assemelhados;
                                                                                   25 - Serviços de avaliação da conformidade vinculados aos Acordos da OMC;
                                                                                                                      26 - ZPE;
                                                                                            Vínculo da Operação à Movimentação Temporária de Bens:

                                                                                           0 - Desconhecido (tipo não informado na nota de origem);
NFSe/infNFSe/DPS/infDPS/serv/comExt/    movTempBens     E   N   1-1        1
                                                                                                                        1 - Não;
                                                                                                   2 - Vinculada - Declaração Única de Importação;
                                                                                                    3 - Vinculada - Declaração Única de Exportação;
NFSe/infNFSe/DPS/infDPS/serv/comExt/         nDUIMP     E   C   0-1       15                     Número da Declaração Única de Importação (DUIMP)
NFSe/infNFSe/DPS/infDPS/serv/comExt/          nDUE      E   C   0-1       14                      Número da Declaração Única de Exportação (DU-E)
                                                                                               Indicador se a NFS-e deverá ser disponibilizada ao MDIC.
NFSe/infNFSe/DPS/infDPS/serv/comExt/          mdic      E   N   1-1        1
                                                                                                             0 - Não enviar para o MDIC;
                                                                                                               1 - Enviar para o MDIC;
                                                                                         Número da identificação do contrato de câmbio ou do documento que
                                                                                       comprove o pagamento (Art. 74, § 1º, do DECRETO Nº 12.955, DE 29 DE
NFSe/infNFSe/DPS/infDPS/serv/comExt/     nContCambio    E   N   0-1       1-20
                                                                                         ABRIL DE 2026, que Regulamenta a Contribuição Social sobre Bens e
                                                                                                     Serviços – CBS e dá outras providências.)

                      2.13     Criação do campo “vAjusteBCIBSCBSComExt”

                      Com o objetivo de viabilizar o correto cálculo da base de cálculo do IBS e da CBS em situações
                      específicas previstas na legislação, foi criado no layout da NFS-e o campo
                      “vAjusteBCIBSCBSComExt”.
                      O referido campo destina-se a registrar ajustes positivos ou negativos aplicáveis exclusivamente à
                      apuração da base de cálculo do IBS e da CBS, em operações de comércio exterior, sem alteração
                      do valor do serviço/operação (“vServ”) constante do documento fiscal.
                                              vAjusteBCIBSCBSComE                                  Valor monetário padrão para ajuste dos valores de base de
NFSe/infNFSe/DPS/infDPS/valores/vAjusteBC/                            E   N      0-1    1-15V2
                                                        xt                                            cálculo do IBS/CBS nos casos de Comércio Exterior.

                      Hipóteses de Utilização:
                      a) Divergência de taxa de conversão de moeda estrangeira
                           Nas situações em que o valor da operação esteja originalmente expresso em moeda estrangeira, a
                           legislação do IBS e da CBS determina que a conversão para moeda nacional seja realizada com
                           base na taxa de câmbio divulgada pelo Banco Central do Brasil (PTAX), observados os critérios
                           legais aplicáveis ao momento da ocorrência do fato gerador.
                           Entretanto, para fins de emissão da NFS-e e apuração do ISSQN, poderá ser utilizada regra diversa
                           de conversão cambial, prevista na legislação tributária municipal ou nacional.

                           Como o valor do serviço (“vServ”) informado na NFS-e é atualmente utilizado tanto para a
                           apuração do ISSQN quanto do IBS e da CBS, torna-se necessária a utilização do campo
                           “vAjusteBCIBSCBSComExt” para registrar, quando ocorrer, a diferença decorrente da conversão
                           monetária, ajustando a base de cálculo do IBS e da CBS ao valor efetivamente exigido pela
                           legislação desses tributos.
                           O valor informado poderá ser:
                                         •       positivo, quando a base de cálculo do IBS e da CBS for superior ao valor
                                         convertido utilizado na NFS-e; ou
                                         •       negativo, quando a base de cálculo do IBS e da CBS for inferior ao valor
                                         convertido utilizado na NFS-e.

                      b) Aplicação de fator de redução na importação de serviços financeiros
                           Nos casos de importação de serviços financeiros sujeitos à tributação baseada em margem, a
                           legislação prevê a aplicação de fator de redução destinado a contemplar uma margem presumida.
                           Para viabilizar essa sistemática, o contribuinte deverá informar o valor correspondente à redução
                           da base de cálculo do IBS e da CBS resultante da aplicação do fator de redução definido na
                           legislação vigente no campo “vAjusteBCIBSCBSComExt”.
                      c) Tributação de parcela excedente ao valor de mercado em operações entre partes relacionadas
                           Nas hipóteses de importação de serviços financeiros realizadas com partes relacionadas, quando
                           aplicável a regra de alíquota zero prevista na legislação, permanece sujeita à tributação a parcela
                           do valor da operação que exceder os preços e taxas usualmente praticados em condições de
                           mercado.
                           Nessas situações, o campo “vAjusteBCIBSCBSComExt” será utilizado para registrar o ajuste
                           necessário à determinação da parcela efetivamente sujeita à incidência do IBS e da CBS,
                           correspondente ao montante que exceder o valor de mercado praticado.
                      Em decorrência da criação desse campo, foram revistas as fórmulas de cálculo da base de cálculo do
                      IBS e da CBS (“vBC”):
                                                              Valor da base de cálculo (BC) do IBS/CBS antes das reduções para cálculo do tributo bruto.

                                                             vBC = vServ - descIncond – (vCalcAjusteBCIBSCBS ou vCalcAjusteBCLocImoveis) – vISSQN +
                                                                             (vAjusteBCIBSCBSComExt) – vPIS - vCOFINS (até 2026)
NFSe/infNFSe/IBSCBS/valores/   vBC   E    N   1-1   1-15V2
                                                                                                         ou

                                                             vBC = vServ - descIncond – (vCalcAjusteBCIBSCBS ou vCalcAjusteBCLocImoveis) – vISSQN +
                                                                              (vAjusteBCIBSCBSComExt) (a partir de 2027 até 2032)

                      2.14     Atualizações no grupo de informações relativas às atividades de eventos

                      Inserção do campo “cMun” no grupo de informações relativas às atividades de eventos de forma a
                      permitir, exclusivamente em operações com os subitens 12.13 e 17.10 do código nacional de
                      tributação (“cTribNac”), a informação do local do evento quando este for diverso do local da
                      prestação do serviço (“cLocPrestacao”).
                      A necessidade da inclusão se justificou, pois o local de incidência do IBS/CBS para os serviços
                      acima citados é o local do evento e não o local da prestação.

                                                                                 Código do município da localidade do Evento.
NFSe/infNFSe/DPS/infDPS/serv/atvEvento/   cMun     E   N    0-1   7
                                                                                             (Tabela do IBGE)

                      Obs.: Para os demais casos, o local do evento será o próprio local da prestação do serviço, não havendo
                      necessidade de informação do referido campo.
                      Por força dessa alteração, passa-se a exigir a informação do grupo “atvEvento” para
                      serviços/operações do subitem 17.10. Assim, as regras de negócio de obrigatoriedade da informação
                      do grupo “atvEvento” foram atualizadas.

                      2.15     Inserção do grupo de informações relativas às operações de condomínios

                      Considerando a previsão contida no art. 26, § 2º, inciso I, da Lei Complementar nº 214/2025, foram
                      incorporadas ao layout da NFS-e de padrão nacional evoluções que possibilitarão emissão do
                      documento fiscal para formalização das operações de condomínios relacionadas aos respectivos rateios
                      de despesas.
                      Além das operações previstas e contempladas na Nota Técnica SE/CGNFS-e nº 005, fatos geradores
                      do IBS/CBS, mas não do Imposto Sobre Serviço de Qualquer Natureza – ISSQN, foi criado código
                      específico para essa nova operação. Importante frisar que essa nova operação se submeterá às mesmas
                      diretrizes conceituais e operacionais detalhadas no tópico 3.a) da Nota Técnica SE/CGNFS-e nº 007:
                      emissão exclusiva pelos emissores públicos nacionais e todas as pessoas jurídicas autorizadas a emitir.
                      Dessa forma, para identificação específica dessas operações, será incluído o código “99.05.01 –
                      Operações Condominiais (taxas e demais valores cobrados pelo condomínio edilício, desde que
                      não caracterizem operações enquadradas em outros códigos de tributação nacional da NFS-e)”
                      na tabela de classificação de operações da NFS-e, conforme destacado abaixo. A utilização desse
                      código permitirá o adequado tratamento das informações decorrentes dos rateios condominiais
                      previstos na legislação tributária vigente.
                                                 Código                                        Descrição
                                                                           Outros serviços sem a incidência de ISSQN e
                                                 99.01.01
                                                                                              ICMS.
                                                                               Operações com Bens Imateriais Não
                                                 99.02.01
                                                                                Classificados em Itens Anteriores
                                                 99.03.01                           Locação de Bens Imóveis
                                                 99.03.02                        Cessão Onerosa de Bens Imóveis
                                                 99.03.03                        Arrendamento de Bens Imóveis
                                                                          Servidão, Cessão de Uso ou de Espaço de Bens
                                                 99.03.04                  Imóveis (quando não caracterizem operações
                                                                                     tributáveis pelo ISSQN)
                                                                           Permissão de Uso ou Direito de Passagem de
                                                 99.03.05                    Bens Imóveis (quando não caracterizem
                                                                                operações tributáveis pelo ISSQN)
                                                 99.04.01                            Locação de Bens Móveis
                                                                            Operações Condominiais (taxas e demais
                                                                           valores cobrados pelo condomínio edilício,
                                                 99.05.01                    desde que não caracterizem operações
                                                                          enquadradas em outros códigos de tributação
                                                                                       nacional da NFS-e)

                      Dessa forma, evidenciou-se a necessidade de criação de grupo específico e exclusivo a ser informado
                      nos documentos fiscais que formalizarão essas operações com o objetivo de permitir a sua
                      discriminação através de tipos de cobranças aplicáveis.
                                                                                              Grupo de informações relativas às operações de
NFSe/infNFSe/DPS/infDPS/IBSCBS/                       condominios      G   -   0-1     -
                                                                                                                  condomínios.
                                                                                                           Data de vencimento original
                                                                                                          Ano, Mês e Dia (AAAA-MM-DD)
NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/             dVencOrig      E   D   1-1     -
                                                                                               (Informar a data de vencimento original das taxas e
                                                                                              demais valores condominiais cobrados do condômino)
                                                                                              Grupo de informações das cobranças das taxas e
                                                                               1-
NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/            gCobranca       G   -           -          demais valores condominiais cobrados do
                                                                               20
                                                                                                                   condômino.
                                                                                                            01 - Condomínio Ordinário
                                                                                                            02 - Condomínio Privativo
NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/gCobran                                                 03 - Fundo De Promoção E Propaganda (FPP)
                                                        tpCobranca     E   N   1-1     2
ca/                                                                                                           04 - Impostos e Taxas
                                                                                                              05 - Fundo de Reserva
                                                                                                               99 - Outra Cobrança
NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/gCobran
                                                       xTpCobranca     E   C   0-1   1-150               Descrição do tipo da cobrança.
ca/
NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/gCobran
                                                        vCobranca      E   N   1-1   1-15V2                Valor da cobrança em R$.
ca/
NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/                                    0-             Grupo de informações relativas ao detalhamento
                                                      gDetCobranca     G   -           -
gCobranca/                                                                     20                                das cobranças.
                                                                                                            001 - Cond. Comum CRD
                                                                                                             002 - Cond. Comum M2
                                                                                                            003 - Cond. Comum Fixo
                                                                                                          004 - Cond. Comum Fração
                                                                                                        005 - Cond. Comum Percentual
                                                                                                             006 - Condomínio CMM
                                                                                                              007 - Energia Elétrica
                                                                                                                    008 - Água
                                                                                                              009 - Ar Condicionado
                                                                                                                  010 - Telefone
                                                                                                                  011 - Internet
                                                                                                            012 - Controle de Pragas
                                                                                                                  013 - Exaustão
                                                                                                                     014 - Gás
                                                                                                                    015 - IPTU
                                                                                                                 016 - Taxa Área
                                                                                                                017 - Manutenção
                                                                                                                    018 - Multa
NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/gCobran
                                                      tpDetCobranca    E   N   1-1     3                           019 - Seguro
ca/gDetCobranca/
                                                                                                              020 - Taxa Bombeiro
                                                                                                           021 - Taxa Administração
                                                                                                                 022 - Taxa Foro
                                                                                                                  023 - Limpeza
                                                                                                               024 - Taxa de Lixo
                                                                                                                  025 - Tapume
                                                                                                            026 - Instalação Alarme
                                                                                                                 027 - Segurança
                                                                                                    028 - Fundo de Promoção e Propaganda
                                                                                                            029 - Análise de Projeto
                                                                                                             030 - Fundo de Reserva
                                                                                                            031 - Laudos e Vistorias
                                                                                                           032 - Detecção de Fumaça
                                                                                                           033 - Reanálise de Projeto
                                                                                                                 034 - Taxa Extra
                                                                                                                 035 - Área Vaga
                                                                                                        036 - Condomínio Irrecuperável
                                                                                                                    999 - Outro
NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/gCobran
                                                      xTpDetCobranca   E   C   0-1   1-150       Descrição do tipo de detalhamento da cobrança.
ca/gDetCobranca/
NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/gCobran                                              Valor detalhado da cobrança em R$ que irá compor
                                                       vDetCobranca    E   N   1-1   1-15V2
ca/gDetCobranca/                                                                                                    vCobranca.
                                                                                               Grupo de informações dos descontos concedidos
                                                                               0-
NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/             gDesconto      G   -           -      das taxas e demais valores condominiais cobrados
                                                                               10
                                                                                                                  do condômino.
NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/gDescont                                                         1 - Desconto Incondicionado
                                                        tpDesconto     E   N   1-1     1
o/                                                                                                           2 - Desconto Condicionado
NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/gDescont
                                                        vDesconto      E   N   1-1   1-15V2                Valor do desconto em R$.
o/

NFSe/infNFSe/DPS/infDPS/IBSCBS/condominios/gDescont
                                                         xTpDesconto        E    C    1-1      1-150    Descrição do tipo do desconto aplicado pelo Condomínio.
o/

                       Nesse sentido, foram realizadas as seguintes atualizações nas fórmulas dos campos “vServ”,
                       “vDescIncond” e “vDescCond”, bem como nas respectivas regras de negócio:
                                                                                                                Valor monetário do serviço (R$).

                                                                                                 OBS1: Para os códigos de tributação nacional do subitem 99.03
NFSe/infNFSe/DPS/infDPS/valores/vServPrest/             vServ       E   N       1-1   1-15V2     (locações e equiparados), vServ = pCopropriedade x vTotOper

                                                                                                 OBS2: Para os códigos de tributação nacional do subitem
                                                                                                       99.05 (condomínios), vServ = ∑ vCobranca.
                                                                                                      Valor monetário do desconto incondicionado (R$).

                                                                                                 OBS1: Para os códigos de tributação nacional do subitem 99.03,
                                                                                                       vDescIncond = pCopropriedade x vDescIncondTot
NFSe/infNFSe/DPS/infDPS/valores/vDescCondIncond/   vDescIncond      E   N       0-1   1-15V2
                                                                                                 OBS2: Para os códigos de tributação nacional do subitem
                                                                                                 99.05 (condomínios), vDescIncond = ∑ vDesconto do tipo
                                                                                                        (tpDesconto) 1 - Desconto Incondicionado.
                                                                                                        Valor monetário do desconto condicionado (R$).

                                                                                                 OBS1: Para os códigos de tributação nacional do subitem 99.03,
                                                                                                        vDescCond = pCopropriedade x vDescCondTot)
NFSe/infNFSe/DPS/infDPS/valores/vDescCondIncond/      vDescCond     E   N       0-1   1-15V2
                                                                                                 OBS2: Para os códigos de tributação nacional do subitem
                                                                                                 99.05 (condomínios), vDescCond = ∑ vDesconto do tipo
                                                                                                        (tpDesconto) 2 - Desconto Condicionado.

                       Por último, foi incluída a regra de negócio que trata da obrigatoriedade da informação do grupo
                       “imovel” quando o serviço informado for relacionado a operações de condomínios.

                       2.16 Reposicionamento dos campos “CST” e “cClassTrib” e Adequação das Regras de
                       Ocorrência dos Grupos IBS/CBS

                       Com o objetivo de adequar o layout da NFS-e às diferentes hipóteses de tributação previstas para o
                       IBS e a CBS, os campos ‘CST’ e ‘cClassTrib’ foram reposicionados, passando a localizarem-se
                       previamente ao grupo “gIBSCBS”.
                                                                                            Grupo de informações relativas aos valores do serviço prestado
NFSe/infNFSe/DPS/infDPS/IBSCBS/                         valores     G   -       1-1   -
                                                                                                                    para IBS e CBS
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/                   trib      G   -       1-1   -       Grupo de informações relacionados aos tributos IBS e CBS
                                                                                                               Código de Situação Tributária do
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/              CST       E   N       1-1   3
                                                                                                                     IBS e da CBS
                                                                                                            Código de Classificação Tributária
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/           cClassTrib   E   N       1-1   6
                                                                                                                    do IBS e da CBS
NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/           gIBSCBS      G   -       0-1   -           Grupo de informações relacionadas ao IBS e à CBS

                       Essa alteração decorre da necessidade de permitir a identificação prévia do enquadramento tributário
                       da operação por meio do CST e, consequentemente, possibilitando definir se as informações detalhadas
                       do grupo de tributação do IBS/CBS deverão ou não ser informadas. As regras que relacionam quando
                       determinado CST exige ou não o grupo de tributação do IBS/CBS estão evidenciadas no indicador de
                       tributação IBS/CBS (“ind_gIBSCBS”), relacionado na Tabela CST e Classificação Tributária
                       (cClassTrib), conforme Informe Técnico 2025.002 v.1.60 - Publicado em 23/06/2026, disponível em
                       https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=jxTMMQeEVM8= .
                       A modificação torna especialmente viável o correto tratamento dos casos em que não há exigência de
                       preenchimento das informações de tributação do IBS/CBS, em particular para os seguintes códigos de
                       situação tributária:

  •     CST 400 – Isenção;
  •     CST 410 – Imunidade e não incidência;
  •     CST 820 – Tributação em documento específico.
Em decorrência dessa alteração estrutural, determinados campos e grupos relacionados ao IBS/CBS
passaram a possuir ocorrência facultativa (OCOR. 0-1), uma vez que suas obrigatoriedades passam a
depender do valor do indicador “ind_gIBSCBS” presente na Tabela CST e Classificação Tributária
(cClassTrib) e derivado do CST informado:

  •     Na NFS-e:
        NFSe/infNFSe/IBSCBS/cLocalidadeIncid
        NFSe/infNFSe/IBSCBS/xLocalidadeIncid
        NFSe/infNFSe/IBSCBS/valores
        NFSe/infNFSe/IBSCBS/valores/vBC
        NFSe/infNFSe/IBSCBS/totCIBS/gIBS
        NFSe/infNFSe/IBSCBS/totCIBS/gCBS
  •     Na DPS:
        NFSe/infNFSe/DPS/infDPS/IBSCBS/cIndOp
        NFSe/infNFSe/DPS/infDPS/IBSCBS/valores/trib/gIBSCBS
Dessa forma, os grupos e campos relacionados ao detalhamento da tributação do IBS/CBS somente
deverão ser informados quando o “ind_gIBSCBS” presente na Tabela CST e Classificação Tributária
(cClassTrib), determinado pelo CST informado, indicar a existência de tributação a ser declarada. Nos
demais casos, tais informações não deverão ser preenchidas, em conformidade com as regras de
validação estabelecidas pelo layout.
Com o objetivo de facilitar o entendimento e o correto preenchimento dos Documentos Fiscais
Eletrônicos (DF-e), a Tabela CST e Classificação Tributária (cClassTrib) está disponível nos Portais
Nacionais de DF-e em formato online e interativo também incorporada na Calculadora de Tributos:

Tabelas CST e Classificação Tributária (cClassTrib):
https://consumo.tributos.gov.br/servico/calcular-tributos-consumo/calculadora/classificacoes-
tributarias
https://dfe-portal.svrs.rs.gov.br/DFE/ClassificacaoTributaria

Calculadora de Tributos:
A Calculadora é o motor de cálculo oficial dos tributos da Reforma Tributária sobre o Consumo.
Projetada para auxiliar os contribuintes na correta emissão dos documentos fiscais, está disponível em
duas modalidades: versão online, na Plataforma da Reforma Tributária, e offline, em código aberto,
para ser embarcado nos ERP’s dos contribuintes via API. Além de calcular os valores de CBS, IBS e

IS, esta ferramenta disponibiliza a memória de cálculo, com a respectiva base legal, e gera os grupos
XML referentes à operação de consumo. Na NFS-e, no processo de autorização/geração do documento,
há uma integração online com a calculadora para validação de campos, verificação de regras e retorno
de valores em conformidade.
  •   Calculadora Online:
https://consumo.tributos.gov.br/servico/calcular-tributos-consumo/calculadora/regime-geral
  •   Calculadora Offline:
https://consumo.tributos.gov.br/servico/calcular-tributos-consumo/calculadora/calculadora-offline

                          CARLOS EDUARDO BURKLE
                      Auditor Fiscal de Tributos – Londrina/PR
Secretário-Executivo da Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço
                       Eletrônica de Padrão Nacional (SE/CGNFS-e)
```
