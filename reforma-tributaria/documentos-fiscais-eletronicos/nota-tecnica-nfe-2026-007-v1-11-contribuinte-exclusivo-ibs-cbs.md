---
titulo: "Nota Técnica NF-e/NFC-e nº 2026.007, versão 1.11, de 30 de outubro de 2026 (Emissão por Contribuinte Exclusivo do IBS/CBS)"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil / ENCAT - CONFAZ"
tipo: "Nota Técnica"
numero: "2026.007"
data: "2026-10-30"
ano: "2026"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY="
ementa: "Regras de validação e atualização de regras existentes da NF-e e da NFC-e para a verificação dos cadastros na Lista Centralizada de Contribuintes da RFB (LCC-RFB) e no Cadastro Centralizado de Contribuintes (CCC), na emissão por contribuinte exclusivo do IBS/CBS."
data_consulta: "2026-11-27"
versao_texto: "Versão 1.11 (PDF oficial, 30/10/2026)"
---

# Nota Técnica NF-e/NFC-e nº 2026.007, versão 1.11, de 30 de outubro de 2026 (Emissão por Contribuinte Exclusivo do IBS/CBS)

> **Nota editorial.** Texto extraído da camada de texto do PDF oficial da Nota Técnica 2026.007, versão 1.11, divulgado no Portal Nacional da NF-e (11 páginas), consultado em 27/11/2026. A data do documento (30/10/2026) é a de publicação da versão, lida na lista de Notas Técnicas do portal. Versão aprovada ou ratificada pelo Ato Técnico Conjunto Sufis/CGIBS nº 10/2026 (`reguladores/rfb/outros-atos/2026/ato-154369-10-2026.md`). Foram removidos a capa, o sumário, os cabeçalhos e rodapés repetidos e a numeração de página. Os 8 títulos de primeiro nível do sumário viraram seções e o texto de cada uma, com os quadros e os leiautes, ficou em bloco de texto que mantém as colunas do PDF. Figuras e imagens do PDF não foram convertidas. Em caso de dúvida, prevalece o PDF. O portal só entrega o PDF com cookie de sessão; o link da fonte é a página de lista de Notas Técnicas, onde a versão consta como "Publicada em 30/10/2026".

## Controle de Versões

```text
Versão          Publicação           Descrição

 1.00            Julho/2026          Publicação da NT.

 1.10          Setembro/2026         Alteração em Regras de Validação.

 1.11          Outubro/2026          Alteração das datas de implantação em Homologação e Produção
```

## Histórico de Alterações / Cronograma

```text
Versão                             Histórico de atualizações                          Implantação     Implantação
                                                                                         Teste         Produção
 1.00     - Criação e atualização campos e de Regras de Validação desta NT            01/09/2026      03/11/2026
                                                                                                      16/11/2026
 1.10     - Alteração em Regras de Validação para facilitar testes em Homologação.   Até 05/10/2026   03/11/2026
          - Correção na RV 1C17-04.
                                                                                     Até 26/10/2026   16/11/2026
 1.11     - Alteração das datas de implantação em Homologação e Produção             Até 26/10/2026   16/11/2026
```

## 1 Resumo

```text
Essa Nota Técnica divulga novas regras de validação e atualiza regras existentes da NF-e/NFC-e para
verificação dos cadastros na Lista Centralizada de Contribuintes da RFB (LCC-RFB) e no Cadastro
Centralizado de Contribuintes (CCC).

Também faz parte do escopo desta NT permitir que contribuintes exclusivos do IBS/CBS (não
contribuintes do ICMS) possam emitir NF-e sem a informação da Inscrição Estadual (IE).

A identificação do contribuinte exclusivo do IBS/CBS passa a ser realizada pela ausência da
informação da Inscrição Estadual do emitente (tag: emit/IE não informada), complementada pela
verificação, no CCC, da inexistência de inscrição estadual de contribuinte do ICMS habilitada para o
CNPJ/CPF do emitente.

A LCC-RFB é uma base nacional de dados cadastrais de pessoas jurídicas, disponibilizada pela
Receita Federal do Brasil (RFB) às Secretarias de Fazenda Estaduais. Seu objetivo é manter as
administrações tributárias sincronizadas com o cadastro oficial de CNPJ da RFB, permitindo a
validação tempestiva da existência, situação cadastral e demais informações relevantes dos
contribuintes durante a autorização e o processamento dos Documentos Fiscais Eletrônicos (DF-e).

Esta Nota Técnica deverá ser observada por todos os emissores de NF-e abrangidos pelas alterações
introduzidas pela Reforma Tributária do Consumo, como contribuintes do ISS e demais pessoas
contribuintes do IBS/CBS, que em razão do Regulamento do IBS/CBS e da Lei Complementar nº
214/2025, passem a emitir Nota Fiscal Eletrônica (modelo 55) para documentar operações sujeitas aos
novos tributos.

Dentre essas operações, destacam-se, exemplificativamente, a alienação de bens do ativo imobilizado,
as transferências de bens entre estabelecimentos, inclusive de bens de uso e consumo e do ativo
imobilizado, bem como outras operações para as quais a legislação da Reforma Tributária exija ou
autorize a emissão de NF-e para fins de documentação fiscal, controle, apuração ou apropriação de
créditos relativos ao IBS e à CBS.

As orientações constantes nesta Nota Técnica visam garantir a correta emissão do documento fiscal,
a interoperabilidade entre os sistemas autorizadores e a adequada aplicação das regras previstas na
Lei Complementar nº 214/2025 e nos atos regulamentares do IBS e da CBS, assegurando a
conformidade das operações realizadas no âmbito da Reforma Tributária.
```

## 2 Visão Geral

```text
Para fins desta Nota Técnica, considera-se Contribuinte Exclusivo do IBS/CBS o emitente que,
simultaneamente:

        •   não informe a tag emit/IE;
        •   possua CNPJ com situação Cadastral “Ativa” na Receita Federal;
        •   não possua Inscrição Estadual habilitada para ICMS na UF do emitente, conforme consulta ao
            CCC.
A autorização da NF-e por parte dos contribuintes exclusivos da tributação do IBS/CBS será realizada
de forma centralizada, somente pela Sefaz Virtual do Rio Grande do Sul (SVRS). As URLs dos Web
Services da NF-e se encontram no Portal Nacional da NF-e e no Portal DFe, mantidos pela Receita
Federal e Rio Grande do Sul, respectivamente.

        •   Portal Nacional NF-e RFB - https://www.nfe.fazenda.gov.br/portal/
        •   DF-e Portal RS - https://dfe-portal.svrs.rs.gov.br/

        •   Para pesquisar se empresa é classificada como Simples Nacional ou SIMEI (MEI), consulte:
            https://www8.receita.fazenda.gov.br/simplesnacional/aplicacoes.aspx?id=21
        •   A mensagem de “Situação Irregular na Receita Federal” significa que o CNPJ se encontra na
            situação cadastral “Nula”, “Suspensa”, “Inapta” ou “Baixada”. Para pesquisar qual a situação
            cadastral da empresa na Receita Federal/LCC, consulte:
            https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/
```

## 3 Descrição das alterações

```text
3.1 Versão 1.00
        1. Campo C17 – Ocorrência alterada para 0-1. Permitindo que emitente contribuinte exclusivo do
            IBS/CBS (não contribuinte do ICMS) não informe a IE.
        2. RV B25-90 – Incluída a exceção 2 para não aplicar regra para contribuinte exclusivo do
            IBS/CBS (sem a IE do emitente)
        3. RV C17-10 – Regra de validação excluída, porque a ausência da IE do emitente deixa de ser
            motivo de rejeição na NF-e (modelo 55), passando a caracterizar o emitente como contribuinte
            exclusivo do IBS/CBS, sujeito à verificação no CCC. Para a NFC-e (modelo 65), a ausência da
            IE do emitente passa a ser rejeitada pela regra C17-42. A IE informada preenchida com zeros
            permanece rejeitada pela regra C17-20 (rejeição 209 – IE do emitente inválida).
        4. 5E17-70 – Regra de validação excluída, por ter sido substituída pelas regras da LCC-RFB.
        5. RV B02-10, C12-10 e P12-40 – Regras alteradas: incluída exceção para que a divergência
            entre a UF do emitente/Chave de Acesso e a UF do Web Service não seja rejeitada na SVRS
            quando se tratar de contribuinte exclusivo do IBS/CBS (NF-e sem a IE do emitente).
        6. RV C17-11, C17-42, C17-43, C18-50 – Regras incluídas: autorização exclusiva na SVRS,
            vedação de NFC-e até 2033, obrigatoriedade de CNPJ e vedação de IEST para o contribuinte
            exclusivo do IBS/CBS.
        7. RV I08-191 – Regra incluída: restrição de CFOP conforme tabela IT 2023.002 (coluna
            indExcIBSCBS).
        8. RV N01-10 e UB12-11 – Regras incluídas: tratamento dos grupos de tributos (ICMS proibido e
            IBS/CBS obrigatório) conforme a condição do emitente.
        9. RV 12C02-10/20, 12C21-20, 1P10-30 e 1P10-32 – Regras incluídas: verificações do cadastro
            LCC-RFB (emitente, destinatário, locais de retirada e entrega, e eventos).
        10. RV 5AF15-10/11/12, 5AF17-10/20/30, 5BG15-10/11/12 e 5BG17-10/20 – Verificações no CCC
            dos locais de retirada e de entrega.
        11. RV 1P10-40 – Regra incluída: direcionamento dos eventos de autoria do emitente contribuinte
            exclusivo do IBS/CBS para a SVRS.

3.2 Versão 1.10
        1. Orientação para sempre utilizar a LCC-RFB do ambiente de Produção, mesmo nos Web
           Services de Homologação.
        2. RV 12C02-10, 12C02-20, 12C21-20, 1P10-30 e 1P10-32 – Regras Alteradas: Ajuste nas
           validações do emitente (NF-e e eventos) na LCC-RFB para permitir testes no ambiente de
           Homologação em diferentes UF por empresas desenvolvedoras com CNPJ de teste no CCC.
        3. RV 12E02-10, 12E02-20, 12F02-10, 12F02-20, 12G02-10, 12G02-20: Ajuste nas validações do
           destinatário, local de retirada e entrega na LCC-RFB para permitir testes no ambiente de
           Homologação com UF diferente da que consta na LCC-RFB para o CNPJ informado.
        4. RV C17-20: Melhoria na redação da regra.
        5. 1C17-04: Correção.

3.3 Versão 1.11
        1. Alteração das datas de implantação em Homologação e Produção.
```

## 4 Leiaute

```text
4.1 Grupo C. Identificação do Emitente da Nota Fiscal eletrônica
     #       ID         Campo                                 Descrição                          Ele     Pai     Tipo   Ocor.      Tam.                            Observação
    30      C01          emit         Identificação do emitente da NF-e                           G      A01             1-1
    ...      ...          ...         ...                                                        ...      ...             ...
    46      C17           IE          Inscrição Estadual do Emitente                              E      C01      C      0-1       2-14    Informar somente os algarismos, sem os caracteres de
                                                                                                                                           formatação (ponto, barra, hífen, etc.).
                                                                                                                                           Observação 1: No caso de NF-e Avulsa (Série 890-919), pode
                                                                                                                                               ser informada a IE emitente como “ISENTO”;
                                                                                                                                           Observação 2: Para emitente contribuinte exclusivo do
                                                                                                                                               IBS/CBS sem Inscrição Estadual na UF (não contribuinte
                                                                                                                                               do ICMS), não informar a IE.
```

## 5 Detalhamento das Regras de Validação – Autorização

```text
5.1 B. Identificação da Nota Fiscal eletrônica
     #         Modelo                                          Regra de Validação                                            Aplic. Msg    Efeito                     Descrição Erro
   B02-10      55/65 Código da UF do Emitente difere da UF do Web Service                                                    Obrig. 226     Rej.    Rejeição: Código da UF do Emitente diverge da UF
                      Exceção: Na SVRS, a regra acima não se aplica para modelo 55 quando não informada a IE do emitente                            autorizadora
                          (contribuinte exclusivo do IBS/CBS).
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.
   B25-90      55/65 Se a finalidade da NF-e for diferente de Nota de Crédito e Nota de Débito (tag: finNFe<>5 e finNFe<>6): Obrig. 1002    Rej.    Rejeição: NF-e sem informação de ICMS / ISSQN
                       - Não informado ICMS (tag: ICMS) e não informado ISSQN (tag: ISSQN)
                      Exceção 1: a regra acima não se aplica no caso de tpOperGov=2-Recebimento do pagamento.
                      Exceção 2: Para modelo 55, na SVRS, a regra acima não se aplica quando não informada a IE do
                          emitente (tag: emit/IE) - contribuinte exclusivo do IBS/CBS.
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.

5.2 C. Identificação do Emitente
     #         Modelo                                        Regra de Validação                                           Aplic.   Msg     Efeito                      Descrição Erro
   C12-10      55/65 Sigla da UF do Emitente difere da UF do Web Service                                                  Obrig.   247      Rej.    Rejeição: Sigla da UF do Emitente diverge da UF
                      Exceção: Na SVRS, a regra acima não se aplica para modelo 55, quando não informada a IE do emitente                           autorizadora
                         (contribuinte exclusivo do IBS/CBS)
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.
   C17-10      55/65 IE Emitente com zeros ou nulo                                                                        Obrig.   229      Rej.    Rejeição: IE do emitente não informada
                      Observação: Regra de validação excluída para todas as SEFAZ Autorizadoras.

   C17-11        55     Se não informada a IE do emitente (tag: emit/IE):                                                        Obrig.   166    Rej.    Rejeição: UF de autorização não permitida para
                         - Web Service de autorização deve ser o da SVRS                                                                                 contribuinte exclusivo do IBS/CBS
                        Observação 1: Para contribuintes exclusivos do IBS/CBS (sem a IE do emitente) a autorização será na
                            SVRS
                        Observação 2: Regra de validação para todas as SEFAZ Autorizadoras.
   C17-20       55/65   Se informada a IE do Emitente e IE diferente de “ISENTO", validar a Inscrição Estadual:                  Obrig.   209    Rej.    Rejeição: IE do emitente inválida
                         - IE Emitente inválida para a UF: erro no tamanho, na composição da IE, ou no dígito verificador (*2)
                            (NT 2018.001)
   C17-42        65     Se não informada a IE do emitente (tag: emit/IE):                                                        Obrig.   156    Rej.    Rejeição: NFC-e não pode ser emitida por
                         - Proibido emitir NFC-e (modelo 65)                                                                                             contribuinte exclusivo do IBS/CBS.
                        Exceção: Regra de validação NÃO se aplica a partir de 2033.
                        Observação 1: Contribuinte sem IE não pode emitir NFC-e.
                        Observação 2: Regra de validação para todas as SEFAZ Autorizadoras.
   C17-43        55     Se não informada a IE do emitente (tag: emit/IE):                                                        Obrig.   157    Rej.    Rejeição: Obrigatório informar CNPJ do emitente
                         - Obrigatório informar CNPJ do emitente (tag: emit/CNPJ)                                                                        para contribuinte exclusivo do IBS/CBS.
                        Observação: Regra de validação exclusiva da SVRS.
   C18-50        55     Se não informada a IE do emitente (tag: emit/IE):                                                        Obrig.   158    Rej.    Rejeição: Proibido informar IEST para contribuinte
                         - Proibido informar a IE do Substituto Tributário (tag: emit/IEST)                                                              exclusivo do IBS/CBS
                        Observação: Regra de validação exclusiva da SVRS.

5.3 Grupo I. Produtos e Serviços da NF-e
      #        Modelo                                         Regra de Validação                                                 Aplic.   Msg   Efeito                     Descrição Erro
   I08-191      55    Se não informada a IE do emitente (tag: emit/IE):                                                          Obrig.   159    Rej.    Rejeição: Operação não permitida para
                       - Consultar tabela de CFOP permitidos para emitentes exclusivos do IBS/CBS (coluna: indExcIBSCBS)                                       contribuinte exclusivo do IBS/CBS.
                          publicada no Portal Nacional da NF-e.                                                                                                [nItem:999]
                      Exceção 1: a regra acima não se aplica no caso de finalidade da NF-e igual a devolução (tag:finNFe=4).
                      Exceção 2: a regra acima não se aplica no caso Tipo de Nota de Crédito igual a “03=Retorno por Recusa
                          Total na Entrega ou Por Não Localização do Destinatário na Tentativa de Entrega” (tag:
                          tpNFCredito=03).
                      Observação: Regra de validação exclusiva da SVRS.

5.4 N. Item / Tributo: ICMS
     #         Modelo                                         Regra de Validação                                              Aplic.      Msg   Efeito                     Descrição Erro
   N01-10       55    Se não informada a IE do emitente (tag: emit/IE):                                                       Obrig.      161    Rej.    Rejeição: Proibido informar ICMS para
                       - Proibido informar ICMS (tag: ICMS); e                                                                                              contribuinte exclusivo do IBS/CBS [nItem:999]
                       - Proibido informar o ICMS Interestadual (tag: ICMSUFDest)
                      Exceção 1: a regra acima não se aplica no caso de finalidade da NF-e igual a devolução (tag: finNFe=4).
                      Exceção 2: A regra acima não se aplica no caso Tipo de Nota de Crédito igual a “03=Retorno por Recusa
                          Total na Entrega ou Por Não Localização do Destinatário na Tentativa de Entrega” (tag:
                          tpNFCredito=03).
                      Observação: Regra de validação exclusiva da SVRS.

5.5 UB. Informações dos tributos IBS / CBS e Imposto Seletivo
      #        Modelo                                         Regra de Validação                                                    Aplic.   Msg   Efeito                     Descrição Erro
   UB12-11      55    Se não informada a IE do emitente (tag: emit/IE):                                                             Obrig.   162    Rej.    Rejeição: Grupo IBS/CBS obrigatório para
                       - Não informado grupo de imposto IBS e CBS (tag: det/imposto/IBSCBS).                                                                   contribuinte exclusivo do IBS/CBS [nItem:999]
                      Observação: Regra de validação exclusiva da SVRS.

5.6 Banco de Dados: Emitente
      #        Modelo                                        Regra de Validação                                             Aplic.           Msg   Efeito                    Descrição Erro
   1C17-02      55    Se não informada a IE do emitente (tag: emit/IE) OU informada a IE do emitente igual a “ISENTO” (tag: Obrig.           163    Rej.    Rejeição: Emitente possui inscrição estadual ativa
                      emit/IE=ISENTO):                                                                                                                         no cadastro da UF
                         - Acessar o CCC (chave: CNPJ/CPF do emitente + UF do emitente. Desconsiderar CCC.cSitIE=9-Exclusão
                            lógica):
                           - Situação do Contribuinte habilitado na UF (cSitIE=1) e Tipo de IE de contribuinte do ICMS (tpIE=1-IE
                                normal ou tpIE=5-Produtor Rural).
                        Observação: Regra de validação exclusiva da SVRS.
   1C17-04       55     Se não informada a IE do emitente (tag: emit/IE) OU informada a IE do emitente igual a “ISENTO” (tag: Obrig.         164    Rej.    Rejeição: Emitente com situação irregular na UF
                        emit/IE=ISENTO):
                         - Acessar o CCC (chave: CNPJ/CPF do emitente + UF do emitente. Desconsiderar CCC.cSitIE=9-Exclusão
                            lógica)
                           - Situação do Contribuinte = “0-Não habilitado na UF” (cSitIE=0) e Situação do CNPJ (cSitCNPJ) igual a
                                “2-Bloqueado como Destinatário na UF” ou “3-Vedado como Destinatário na UF”
                        Observação: Regra de validação exclusiva da SVRS.

5.7 Banco de Dados: Destinatário
      #        Modelo                                         Regra de Validação                                           Aplic.            Msg   Efeito                    Descrição Erro
   5E17-70      55    Mensagens opcionais se informada IE do destinatário e IE não vinculada ao CNPJ/CPF e tpEmis <> 3-NFF Obrig.            246    Rej.    Rejeição: CNPJ Destinatário não cadastrado
                            (NT 2021.002):
                      - Acessar Cadastro de Pessoa Jurídica ou Pessoa Física:
                      - CNPJ destinatário não cadastrado (NT 2019.001)
                      Observação: Regra de validação excluída para todas as SEFAZ Autorizadoras.

5.8 Banco de Dados: Local de Retirada
     #         Modelo                                           Regra de Validação                                                  Aplic.   Msg   Efeito                   Descrição Erro
  5AF15-10      55    Se informada IE do Local de Retirada e tpEmis <> 3-NFF:                                                       Obrig.   942    Rej. Rejeição: IE do local de retirada não cadastrada
                       - Acessar CCC (Chave: UF Retirada, IE Retirada. (Desconsiderar CCC.cSitIE=9-Exclusão lógica)
                         - IE do local de retirada não cadastrada
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.

  5AF15-11        55        - IE do Local de Retirada com situação irregular na UF (CCC.cSitCNPJ = “2-Bloqueado” ou “3-Vedado”)   Obrig.   165         Rej.      Rejeição: IE do Local de Retirada com situação
                         Observação: Regra de validação para todas as SEFAZ Autorizadoras.                                                                          irregular na UF
  5AF15-12        55         - IE do local de retirada não está ativa na UF (CCC.cSitIE=0-Não habilitado)                         Obrig.   167         Rej.      Rejeição: IE do local de retirada não está ativa na
                         Observação: Regra de validação para todas as SEFAZ Autorizadoras.                                                                           UF
  5AF17-10        55     Se IE do Local de Retirada não informada e informado CNPJ do local de retirada e tpEmis <> 3-NFF:        Obrig.   168         Rej.      Rejeição: IE do local de retirada não informada
                          - Acessar CCC (Chave: UF Retirada, CNPJ Retirada. (Desconsiderar CCC.cSitIE=9-Exclusão lógica)
                             - Local de retirada possui IE ativa na UF (CCC.cSitIE=”1-Habilitado”) e CCC.IndIEDestOpc = “0-
                                 Obrigatório”.
                         Observação: Regra de validação para todas as autorizadoras.
  5AF17-20        55         - CNPJ do Local de Retirada com situação irregular na UF (CCC.cSitCNPJ = “2-Bloqueado” ou “3-        Obrig.   169         Rej.      Rejeição: CNPJ do Local de Retirada com situação
                                 Vedado”)                                                                                                                            irregular na UF
                         Observação: Regra de validação para todas as autorizadoras.

5.9 Banco de Dados: Local de Entrega
     #         Modelo                                              Regra de Validação                                                Aplic.   Msg        Efeito                 Descrição Erro
  5BG15-10      55    Se informada IE do Local de Entrega e tpEmis <> 3-NFF:                                                         Obrig.   171         Rej. Rejeição: IE do local de entrega não cadastrada
                        - Acessar CCC (Chave: UF Entrega , IE Entrega. Desconsiderar CCC.cSitIE=9-Exclusão lógica)
                          - IE do local de Entrega não cadastrada
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.
  5BG15-11      55     - IE do Local de Entrega com situação irregular na UF (CCC.cSitCNPJ = “2-Bloqueado” ou “3-Vedado”)            Obrig.      173          Rej.   Rejeição: IE do Local de Entrega com situação
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.                                                                                 irregular na UF
  5BG15-12      55        - IE do local de Entrega não está ativa na UF (CCC.cSitIE=0-Não habilitado)                                Obrig.      175          Rej.   Rejeição: IE do local de Entrega não está ativa
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.                                                                                 na UF
  5BG17-10      55    Se IE do Local de Entrega não informada e informado CNPJ do local de Entrega e tpEmis <> 3-NFF:                Obrig.      176          Rej.   Rejeição: IE do local de Entrega não informada
                        - Acessar CCC (Chave: UF Entrega, CNPJ Entrega. (Desconsiderar CCC.cSitIE=9-Exclusão lógica)
                          - CNPJ do Local de Entrega possui IE ativa na UF (CCC.cSitIE=1-Habilitado) e CCC.IndIEDestOpc=”0-
                              Obrigatório”
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.
  5BG17-20      55      - CNPJ do Local de Entrega com situação irregular na UF (CCC.cSitCNPJ = “2-Bloqueado” ou “3-Vedado”)         Obrig.      177          Rej.   Rejeição: CNPJ do Local de Entrega com
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.                                                                                 situação irregular na UF

5.10 Banco de Dados: Validação Cadastro LCC-RFB
5.10.1 Grupo C. Identificação do Emitente
    #        Modelo                                             Regra de Validação                                                     Aplic. Msg Efeito                Descrição Erro
 12C02-10    55/65 Se informado CNPJ do Emitente (tag: C02):                                                                           Obrig. 178  Rej. Rejeição: CNPJ [XX.XXX.XXX/XXXX-DV] do
                     - Acessar LCC-RFB (*1) (Chave: UF Emitente, CNPJ Emitente. Desconsiderar LCC.cSitCNPJ=99-Exclusão Lógica):                            emitente não cadastrado na Receita Federal
                       - CNPJ Emitente não cadastrado.
                    Exceção: Em Homologação, não rejeitar se CCC.indContribTeste=1.
                    Observação: Regra de validação para todas as SEFAZ Autorizadoras.

 12C02-20     55/65       - Situação do CNPJ do Emitente (cSitCNPJ) diferente de 02-Ativa                                           Obrig. 179    Rej.    Rejeição: CNPJ [XX.XXX.XXX/XXXX-DV] do
                      Exceção: Em Homologação, não rejeitar se CCC.indContribTeste=1.                                                                        emitente com situação irregular na Receita
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.                                                                      Federal
 12C21-20     55/65    - Verificar a compatibilidade entre o Código de Regime Tributário informado na NF-e (tag: emit/CRT) e o      Obrig. 180    Rej.    Rejeição: Código Regime Tributário do
                           Regime de Tributação do CNPJ do Emitente cadastrado na LCC-RFB (campo regTrib), conforme a tabela                                 emitente diverge do cadastro na Receita
                           abaixo:                                                                                                                           Federal
                      CRT na NF-e                                               regTrib na LCC-RFB
                      1=Simples Nacional                                        1=Empresa optante pelo Simples Nacional;
                      2=Simples Nacional, excesso sublimite de receita bruta    1=Empresa optante pelo Simples Nacional;
                      3=Regime Normal                                           9=Outros Regime de Tributação
                      4=Simples Nacional - Microempreendedor Individual - MEI 2=Empresa optante pelo MEI
                      Exceção: Em Homologação, não rejeitar se CCC.indContribTeste=1.
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.
   (*1) Utilizar a LCC-RFB do ambiente de Produção, mesmo no Web Service de Homologação.

5.10.2 Grupo E. Identificação do Destinatário
    #        Modelo                                             Regra de Validação                                                  Aplic. Msg Efeito                Descrição Erro
 12E02-10    55/65 Se informado CNPJ do Destinatário (tag: E02):                                                                    Obrig. 181  Rej. Rejeição: CNPJ [XX.XXX.XXX/XXXX-DV] do
                     - Acessar LCC-RFB (*1) (Chave: UF Destinatário, CNPJ Destinatário. Desconsiderar LCC.cSitCNPJ=99-Exclusão                          destinatário não cadastrado na Receita
                        Lógica):                                                                                                                        Federal
                       - CNPJ Destinatário não cadastrado
                    Exceção: Em Homologação, não rejeitar se for informado um CNPJ alfanumérico.
                    Observação: Regra de validação para todas as SEFAZ Autorizadoras.
 12E02-20    55/65 Situação do CNPJ do Destinatário (cSitCNPJ) diferente de 02-Ativa                                                Obrig. 182    Rej.    Rejeição: CNPJ [XX.XXX.XXX/XXXX-DV] do
                    Exceção: Em Homologação, não rejeitar se for informado um CNPJ alfanumérico.                                                             Destinatário com situação irregular na
                    Observação: Regra de validação para todas as SEFAZ Autorizadoras.                                                                        Receita Federal
   (*1) Utilizar a LCC-RFB do ambiente de Produção, mesmo no Web Service de Homologação.

5.10.3 Grupo F. Identificação do Local de Retirada
    #        Modelo                                             Regra de Validação                                                Aplic.   Msg   Efeito                   Descrição Erro
 12F02-10     55    Se informado CNPJ do Local de Retirada (tag: F02):                                                            Obrig.   183    Rej.    Rejeição: CNPJ [XX.XXX.XXX/XXXX-DV] do
                      - Acessar LCC-RFB (*1) (Chave: UF Local de Retirada, CNPJ Local de Retirada. Desconsiderar LCC.cSitCNPJ=99-                            Local de Retirada não cadastrado na
                         Exclusão Lógica):                                                                                                                   Receita Federal
                        - CNPJ do Local de Retirada não cadastrado
                    Exceção: Em Homologação, não rejeitar se for informado um CNPJ alfanumérico.
                    Observação: Regra de validação para todas as SEFAZ Autorizadoras.
 12F02-20     55     - Situação do CNPJ do Local de Retirada (cSitCNPJ) diferente de 02-Ativa                                     Obrig.   184    Rej.    Rejeição: CNPJ [XX.XXX.XXX/XXXX-DV] do Local
                    Exceção: Em Homologação, não rejeitar se for informado um CNPJ alfanumérico.                                                             de Retirada com situação irregular na
                    Observação: Regra de validação para todas as SEFAZ Autorizadoras.                                                                        Receita Federal
   (*1) Utilizar a LCC-RFB do ambiente de Produção, mesmo no Web Service de Homologação.

5.10.4 Grupo G. Identificação do Local de Entrega
    #        Modelo                                              Regra de Validação                                              Aplic.     Msg   Efeito                   Descrição Erro
 12G02-10     55    Se informado CNPJ do Local de Entrega (tag: G02):                                                            Obrig.     185    Rej.    Rejeição: CNPJ [XX.XXX.XXX/XXXX-DV] do
                       - Acessar LCC-RFB (*1) (Chave: UF Local de Entrega, CNPJ Local de Entrega. Desconsiderar LCC.cSitCNPJ=99-                              Local de Entrega não cadastrado na Receita
                          Exclusão Lógica):                                                                                                                   Federal
                         - CNPJ do Local de Entrega não cadastrado
                    Exceção: Em Homologação, não rejeitar se for informado um CNPJ alfanumérico.
                    Observação: Regra de validação para todas as SEFAZ Autorizadoras.
 12G02-20     55     - Situação do CNPJ do Local de Entrega (cSitCNPJ) diferente de 02-Ativa                                     Obrig.     186    Rej.    Rejeição: CNPJ [XX.XXX.XXX/XXXX-DV] do
                    Exceção: Em Homologação, não rejeitar se for informado um CNPJ alfanumérico.                                                              Local de Entrega com situação irregular na
                    Observação: Regra de validação para todas as SEFAZ Autorizadoras.                                                                         Receita Federal
   (*1) Utilizar a LCC-RFB do ambiente de Produção, mesmo no Web Service de Homologação.
```

## 6 Regras de Validação Genéricas Para Todos os Eventos

```text
6.1 Regras de Validação Genéricas Para Todos os Eventos
     #       Modelo                                            Regra de Validação                                                  Aplic.   Msg   Efeito                Descrição Erro
   P12-40     55    • UF da Chave de Acesso diverge da UF Autorizadora                                                             Obrig.   249    Rej. Rejeição: UF da Chave de Acesso diverge da UF
                    Exceção: Na SVRS, a regra acima não se aplica para contribuintes exclusivos do IBS/CBS (não informada a tag                            autorizadora
                       “emit/IE” da NF-e da chave de acesso)
                    Observação: Regra de validação para todas as SEFAZ Autorizadoras.

6.2 Banco de Dados: Emitente
     #                                                            Regra de Validação                                               Aplic.   Msg   Efeito                Descrição Erro
  1P10-30     55/65   Se informado CNPJ do Autor do Evento:                                                                        Obrig.   187    Rej. Rejeição: CNPJ [XX.XXX.XXX/XXXX-DV] do
                       - Acessar LCC-RFB (*1) (Chave: UF Autor, CNPJ Autor. Desconsiderar LCC.cSitCNPJ=99-Exclusão Lógica):                                Autor de Evento não cadastrado na Receita
                          - CNPJ do Autor do Evento não cadastrado.                                                                                        Federal
                      Exceção: Em Homologação, não rejeitar se CCC.indContribTeste=1.
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.
  1P10-32     55/65       - Situação do CNPJ do Autor do Evento diferente de 02-Ativa                                              Obrig.   170    Rej.    Rejeição: CNPJ do Autor de Evento com
                      Exceção: Em Homologação, não rejeitar se CCC.indContribTeste=1.                                                                          situação irregular na Receita Federal
                      Observação: Regra de validação para todas as SEFAZ Autorizadoras.
  1P10-40      55     Se o CNPJ/CPF do autor do evento for igual ao CNPJ/CPF do emitente da NF-e vinculada à chave de acesso e a   Obrig.   188    Rej.    Rejeição: Evento de NF-e de contribuinte
                      NF-e não possuir a tag emit/IE:                                                                                                         exclusivo do IBS/CBS deve ser autorizado
                       - O Web Service receptor do evento deve ser o da SVRS.                                                                                 na SVRS
                      Exceção 1: regra de validação não se aplica para a chave de acesso com série entre a faixa 890-919.
                      Observação 1: Eventos de autoria de emitente sem IE devem ser registrados na SVRS.
                      Observação 2: Regra de validação para todas as SEFAZ Autorizadoras.
   (*1) Utilizar a LCC-RFB do ambiente de Produção, mesmo no Web Service de Homologação.
```
