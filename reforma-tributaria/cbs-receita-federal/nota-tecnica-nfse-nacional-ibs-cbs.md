---
titulo: "Nota Técnica Nacional da NFS-e (Padrão ADN): Leiaute do IBS e da CBS sobre Serviços, Grupos IBSCBS, cTribNac, cClassTrib e Integração com Split Payment (LC nº 214/2025)"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil (RFB) / Comitê Gestor da NFS-e de Padrão Nacional (CGNFS-e)"
tipo: "Nota Técnica / Documentação Fiscal Eletrônica"
numero: "NT SE/CGNFS-e IBS/CBS"
data: "2025-01-31"
ano: "2025"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS", "ISSQN", "PIS/Pasep", "Cofins"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.gov.br/nfse/pt-br"
ementa: "Dispõe sobre a adequação do Leiaute da Declaração de Prestação de Serviços (DPS) e da Nota Fiscal de Serviços Eletrônica de Padrão Nacional (NFS-e Nacional / Ambiente de Dados Nacional - ADN) para a escrituração do Imposto sobre Bens e Serviços (IBS) e da Contribuição Social sobre Bens e Serviços (CBS), instituindo os grupos XML IBSCBS, os códigos de tributação nacional (cTribNac), os códigos de situação tributária (CST-IBS/CBS), a classificação tributária (cClassTrib) e a integração com o Split Payment nos termos da Lei Complementar nº 214/2025."
---

# Nota Técnica Nacional da NFS-e (Padrão ADN): Adequação do Leiaute da Nota Fiscal de Serviços Eletrônica para o IBS e a CBS

## Identificação Normativa e Técnica

- **Órgãos Emissores:** Secretaria Especial da Receita Federal do Brasil (RFB), Comitê Gestor da Nota Fiscal de Serviços Eletrônica de Padrão Nacional (CGNFS-e) e Comitê Gestor do Imposto sobre Bens e Serviços (CGIBS)
- **Base Legal Constitucional e Complementar:** Emenda Constitucional nº 132, de 20 de dezembro de 2023 (art. 156-A e art. 195, V, da CF/1988), Lei Complementar nº 199, de 1º de agosto de 2023 (Estatuto Nacional de Simplificação de Obrigações Tributárias Acessórias), e **Lei Complementar nº 214, de 16 de janeiro de 2025** (arts. 60 a 66)
- **Sistema Nacional:** Sistema Nacional da NFS-e — Ambiente de Dados Nacional (**ADN**) e Emissor Público Nacional (Web e API)
- **Fonte Oficial:** [Portal Nacional da Nota Fiscal de Serviço Eletrônica — gov.br/nfse](https://www.gov.br/nfse/pt-br)

---

## 1. Obrigatoriedade Nacional do Padrão ADN / NFS-e na Reforma Tributária (Art. 62 da LC nº 214/2025)

A **Lei Complementar nº 214, de 16 de janeiro de 2025**, tornou obrigatória para **todos os 5.570 Municípios e o Distrito Federal**, a partir de **1º de janeiro de 2026**, a integração ao **Ambiente de Dados Nacional (ADN)** da Nota Fiscal de Serviços Eletrônica de Padrão Nacional, sob pena de suspensão voluntária de transferências e impossibilidade de operacionalização da alíquota municipal e estadual do Imposto sobre Bens e Serviços (IBS) e da Contribuição sobre Bens e Serviços (CBS).

Os Municípios podem optar por uma de duas arquiteturas tecnológicas homologadas:
1. **Adoção Direta da Sefin Nacional (Emissor Público Nacional):** Os contribuintes estabelecidos no Município emitem a Declaração de Prestação de Serviços (DPS) diretamente nos servidores da plataforma `gov.br/nfse` (via Portal Web, aplicativo móvel ou WebService REST/JSON/XML), que gera a NFS-e Nacional e a disponibiliza simultaneamente à Receita Federal, ao CGIBS e ao Município;
2. **Manutenção de Emissor Próprio Municipal Compartilhado com o ADN:** O Município mantém seu sistema autorizador local (como Nota Milhão em São Paulo, Nota Carioca no Rio de Janeiro, BHISS em Belo Horizonte ou ISS Curitiba), mas obriga-se a adotar o **leiaute padronizado dos grupos de IBS e CBS** e a transmitir de forma **síncrona ou quase em tempo real** o arquivo XML autorizado para o Ambiente de Dados Nacional (ADN).

---

## 2. Estrutura dos Novos Grupos XML de Tributação `IBSCBS` na DPS e na NFS-e Nacional

O leiaute técnico da Declaração de Prestação de Serviços (DPS) e da NFS-e Nacional incorpora o grupo estruturado `<IBSCBS>` dentro do bloco de valores e tributos (`<valores><trib>`), coexistindo com o grupo `<tribMun>` (ISSQN) e `<tribFed>` (PIS/Cofins e Retenções na Fonte de IRRF/CSLL/INSS) durante todo o período de transição de **2026 a 2032**:

| Grupo / Tag XML no Padrão ADN | Nome Técnico do Campo | Tipo / Tamanho | Descrição e Regra de Validação na LC nº 214/2025 |
| :--- | :--- | :--- | :--- |
| `<cTribNac>` | Código de Tributação Nacional | Numérico (6 dígitos) | Código nacional padronizado derivado da Lista da LC 116/2003 (formato `II.SS.DD` — Item, Subitem e Desdobramento Nacional) |
| `<cNBS>` | Código da Nomenclatura Brasileira de Serviços (NBS) | Numérico (9 dígitos) | Classificação padronizada do serviço ou intangível na NBS 2.0, obrigatória para determinação de regimes diferenciados e exportação |
| `<cIndOp>` | Código Indicador da Operação de Consumo | Numérico (6 dígitos) | Identifica a regra de local da operação (art. 11 da LC 214/2025): execução presencial/física, bem imóvel, prestação remota/on-line ao domicílio do destinatário |
| `<CST>` | Código de Situação Tributária do IBS e da CBS | Numérico (3 dígitos) | Código unificado que define o regime de incidência da operação (tributação integral, alíquota reduzida, isenção, imunidade, diferimento, suspensão ou regime específico) |
| `<cClassTrib>` | Código de Classificação Tributária do IBS e da CBS | Numérico (6 dígitos) | Vincula exatamente o item da NFS-e ao dispositivo legal e anexo da **LC nº 214/2025** (ex.: redução de 60% para saúde/educação, redução de 30% para profissões regulamentadas) |
| `<vBC>` | Base de Cálculo do IBS e da CBS | Decimal (15,2) | Valor da operação (preço do serviço sem o ISS, o ICMS, o IBS e a CBS — **cálculo "por fora"**, nos termos do art. 12 da LC nº 214/2025) |
| `<pCBS>` / `<vCBS>` | Alíquota e Valor da CBS (União) | Decimal (4,4 / 15,2) | Alíquota de referência ou reduzida da CBS federal (0,9% em 2026; alíquota plena a partir de 2027) e respectivo valor apurado |
| `<pIBSEst>` / `<vIBSEst>` | Alíquota e Valor da Parcela Estadual do IBS | Decimal (4,4 / 15,2) | Alíquota estadual de destino do IBS (0,05% em 2026 e 2027; escalonamento gradual de 2029 a 2032) e respectivo valor |
| `<pIBSMun>` / `<vIBSMun>` | Alíquota e Valor da Parcela Municipal do IBS | Decimal (4,4 / 15,2) | Alíquota municipal de destino do IBS (0,05% em 2026 e 2027; transição gradual de substituição do ISS de 2029 a 2032) e respectivo valor |
| `<gCredPres>` | Grupo de Crédito Presumido | Grupo Complexo | Utilizado em aquisições de serviços de transportadores autônomos, produtores integrados ou cooperativas com direito a crédito presumido de IBS/CBS |
| `<gCompraGov>` | Grupo de Compras Governamentais | Grupo Complexo | Identifica operações contratadas pela Administração Pública Direta, Autarquias e Fundações (art. 149-B e redutor de alíquota com destinação integral ao ente comprador) |

---

## 3. Tabela de Códigos de Situação Tributária (`CST-IBS/CBS`) e Classificação (`cClassTrib`) Aplicáveis a Serviços

Em alinhamento entre a NFS-e Nacional e os Documentos Fiscais Eletrônicos de mercadorias (NF-e Modelo 55 / NFC-e Modelo 65), adotam-se os seguintes Códigos de Situação Tributária (`CST`) e enquadramentos de `cClassTrib` para o setor de serviços:

| CST IBS/CBS | Descrição da Situação Tributária | Principais Exemplos no Setor de Serviços (LC nº 214/2025) | Percentual de Redutor de Alíquota |
| :--- | :--- | :--- | :--- |
| **`000`** | Tributação Integral pelo Regime Geral | Serviços empresariais gerais (consultoria empresarial não regulamentada em conselho, TI corporativa/SaaS B2B, publicidade, vigilância, limpeza, locação de bens móveis) | **0%** (Alíquota padrão de referência, garantindo 100% de crédito financeiro ao tomador PJ no regime regular) |
| **`200`** | Tributação com Alíquota Reduzida em **30%** | **Profissões intelectuais de natureza científica, literária ou artística submetidas à fiscalização de conselho profissional** (advogados, contadores, engenheiros, arquitetos, economistas, administradores, médicos veterinários, jornalistas, psicólogos, corretores, representantes comerciais — art. 127 da LC 214/2025, cumpridos os requisitos societários) | **Redução de 30%** das alíquotas de IBS e CBS |
| **`200`** | Tributação com Alíquota Reduzida em **60%** | **Serviços de Educação** (Anexo II da LC 214/2025), **Serviços de Saúde Humana** (Anexo III da LC 214/2025), produções artísticas, culturais, jornalísticas e audiovisuais nacionais, comunicação institucional e desporto | **Redução de 60%** das alíquotas de IBS e CBS |
| **`200`** | Tributação com Alíquota Reduzida em **100% (Alíquota Zero)** | Serviços de transporte público coletivo de passageiros rodoviário e metroferroviário urbano, semiurbano e metropolitano (art. 157 da LC 214/2025), serviços prestados por Instituições Científicas, Tecnológicas e de Inovação (ICTs) sem fins lucrativos | **Redução de 100%** (Alíquota 0%) |
| **`400`** | Isenção | Serviços de transporte público coletivo nas hipóteses isentas e serviços específicos da Zona Franca de Manaus / Áreas de Livre Comércio | **Exoneração total** |
| **`410`** | Imunidade e Não Incidência | **Exportação de serviços para o exterior** (art. 80 da LC 214/2025 — com manutenção integral dos créditos de entrada), serviços de radiodifusão sonora e de sons e imagens de recepção livre e gratuita, entidades beneficentes de assistência social (art. 150, VI, "c") e templos | **Imune / Não Incidente** |
| **`620`** | Regime Específico — Serviços Financeiros, Planos de Saúde, Concursos de Prognósticos, Bens Imóveis e Hotelaria | Serviços bancários e financeiros (Arts. 181 a 233), planos de assistência à saúde (Arts. 234 a 243 — alíquota reduzida em 60% sobre receita líquida de prêmios menos sinistros), hotelaria, parques de diversão, bares, restaurantes e agências de viagens (alíquota reduzida em 40% sem crédito ao adquirente), operações com bens imóveis, construção civil, incorporação e locação imobiliária (Arts. 251 a 269 — redutor de **50%** nas alienações/construção e redutor de **70%** na locação/cessão onerosa de bens imóveis, além do redutor social) | Alíquotas e bases de cálculo específicas por setor |
| **`800`** | Simples Nacional (Apuração pelo PGDAS-D vs. Opção por Débito/Crédito de IBS/CBS) | Prestador optante pelo Simples Nacional que recolhe IBS e CBS dentro do DAS (transferindo crédito reduzido equivalente ao percentual pago no Simples) ou que optou por apurar IBS e CBS pelo regime regular "por fora" para transferir crédito integral ao tomador B2B (Art. 41 da LC 123/2006 c/c LC 214/2025) | Conforme opção semestral/anual do optante pelo Simples |

---

## 4. Regras de Local da Operação (`cIndOp`) e Fim da Guerra Fiscal Municipal

O leiaute nacional da NFS-e materializa o **princípio do destino** consagrado no art. 11 da Lei Complementar nº 214/2025 para definir automaticamente a qual Estado (`vIBSEst`) e a qual Município (`vIBSMun`) pertence o IBS destacado no documento fiscal:
1. **Serviços prestados fisicamente sobre a pessoa ou necessários à presença física do indivíduo (saúde presencial, estética, hotelaria, eventos, alimentação):** O código de município de incidência do IBS é o do **local da prestação física do serviço**;
2. **Serviços relacionados a bem imóvel (construção civil, engenharia, arquitetura, reforma, administração e corretagem de imóvel, vigilância e limpeza predial):** O IBS pertence ao **Município e Estado onde o imóvel está situado** (identificado pelo Cadastro Imobiliário Brasileiro — **CIB**, código nacional obrigatório na NFS-e para operações imobiliárias e de obras);
3. **Serviços de transporte de passageiros:** Local onde se inicia o serviço de transporte;
4. **Serviços de transporte de carga:** Local da entrega/destino da carga;
5. **Demais serviços e intangíveis prestados à distância (consultoria remota, advocacia, contabilidade, desenvolvimento de software, SaaS, nuvem, streaming, publicidade digital, call center):** O IBS pertence ao **Município e Estado do domicílio principal do adquirente ( nas operações onerosas) ou do destinatário**.

---

## 5. Integração da NFS-e Nacional com a Apuração Assistida e o *Split Payment* (Arts. 31 a 35 da LC nº 214/2025)

A chave de acesso de 50 posições da NFS-e Nacional (`id="NFSe..."`) passa a integrar o arranjo de liquidação financeira do **Split Payment** (recolhimento na liquidação financeira) gerido pela Receita Federal e pelo Comitê Gestor do IBS em conjunto com o Banco Central do Brasil:
- **Vinculação da Chave da NFS-e aos Meios de Pagamento Eletrônicos (PIX, Boleto Registrado, TED, Cartões de Crédito/Débito):** No grupo de informações de pagamento da NFS-e, a indicação da transação financeira permite que a instituição de pagamento segregue automaticamente, no ato da liquidação financeira da fatura de serviços, os valores de `<vCBS>` e `<vIBS>` (deduzidos os créditos já apropriados pelo prestador no sistema de Apuração Assistida da RFB/CGIBS);
- **Extinção Automática do Débito e Liberação Imediata do Crédito ao Tomador:** Uma vez liquidado o tributo via *Split Payment* ou recolhimento pelo prestador, o sistema de Apuração Assistida credita instantaneamente o valor de CBS e IBS na conta gráfica do tomador pessoa jurídica contribuinte do regime regular, eliminando glosas formais e o contencioso de retenções municipais de ISS (como o antigo CPOM).

---

## 6. Cronograma de Vigência e Convivência na NFS-e (2026 a 2033)

- **Ano-Calendário de 2026 (Ano-Teste — Art. 343 da LC 214/2025):** Preenchimento obrigatório dos campos de `<IBSCBS>` na NFS-e Nacional com alíquota-teste de **0,9% de CBS** e **0,1% de IBS** (sendo 0,05% estadual e 0,05% municipal), **dispensado o recolhimento financeiro** para os contribuintes que emitirem regularmente a NFS-e no padrão ADN (ou compensável com PIS/Cofins), mantendo-se o recolhimento integral do ISSQN (2% a 5%) e das retenções federais;
- **Anos de 2027 e 2028:** Extinção definitiva do PIS e da Cofins (e da retenção de PIS/Cofins nos 4,65% da CSRF, permanecendo apenas 1% de CSLL e 1,5% de IRRF), entrada em vigor da **CBS plena** e manutenção do IBS em **0,1%** (com ISSQN integral);
- **Anos de 2029 a 2032:** Redução progressiva das alíquotas do ISSQN na NFS-e (10% em 2029, 20% em 2030, 30% em 2031 e 40% em 2032) e aumento proporcional das alíquotas estaduais e municipais do IBS;
- **A partir de 1º de janeiro de 2033:** Extinção definitiva do ISSQN e vigência integral exclusiva do IBS e da CBS na NFS-e Nacional.
