# 🚀 Pilar 8: O Novo Sistema Tributário sobre o Consumo (IBS, CBS, Imposto Seletivo e Split Payment)

## 1. Visão Geral da Reforma Tributária (EC 132/2023)
A Emenda Constitucional nº 132, promulgada em 20 de dezembro de 2023, extingue 5 tributos cumulativos e fragmentados (PIS, COFINS, IPI, ICMS e ISS) e institui o modelo de **IVA Dual** (CBS + IBS), acompanhado do **Imposto Seletivo**.

## 2. A Estrutura do IVA Dual Brasileiro

| Tributo | Esfera de Competência | Gestão / Arrecadação | Base Legal Complementar | Substitui |
| :--- | :--- | :--- | :--- | :--- |
| **CBS (Contribuição sobre Bens e Serviços)** | Federal | Secretaria Especial da Receita Federal do Brasil (RFB) | [Lei Complementar nº 214/2025](../reforma-tributaria/lei-complementar-214-2025.md) | PIS/Pasep e Cofins |
| **IBS (Imposto sobre Bens e Serviços)** | Subnacional (Estados, DF e Municípios) | Comitê Gestor do IBS (CG-IBS) | [Lei Complementar nº 214/2025](../reforma-tributaria/lei-complementar-214-2025.md) e [LC nº 227/2026](../reforma-tributaria/lei-complementar-227-2026.md) | ICMS (estadual) e ISS (municipal) |
| **Imposto Seletivo (IS)** | Federal | Receita Federal do Brasil | [Lei Complementar nº 214/2025](../reforma-tributaria/lei-complementar-214-2025.md) | IPI (parcialmente, exceto Zona Franca) |

## 3. A Tecnologia do Split Payment Inteligente
O [Split Payment Inteligente](../reforma-tributaria/split-payment/split-payment-modelo-operacional.md) é o mecanismo tecnológico estruturante da Reforma Tributária brasileira:
- **Separação Automática no Ato do Pagamento:** Quando o comprador realiza um pagamento via Pix, cartão ou arranjo bancário, o valor do tributo devido é retido instantaneamente e depositado na conta única do IBS/CBS.
- **Liquidação Líquida ao Fornecedor:** O fornecedor recebe apenas o valor líquido da mercadoria ou serviço, eliminando o passivo tributário a pagar e impedindo a inadimplência ou sonegação na cadeia.

### Modalidades de Split Payment:
1. **Split Payment Padrão (Eletrônico Inteligente):** Integrado a arranjos de pagamento (Pix, cartões de crédito/débito e boleto bancário). A liquidação física dos recursos já separa a parcela do tributo e repassa diretamente para a conta única do IBS e da CBS.
2. **Split Payment Simplificado:** Para transações sem identificação imediata da nota fiscal no ato do pagamento, com retenção de alíquota presumida e compensação na apuração mensal.

## 4. O Comitê Gestor do IBS (Lei Complementar nº 227/2026)
A [Lei Complementar nº 227/2026](../reforma-tributaria/lei-complementar-227-2026.md) disciplina o órgão público independente com representação paritária entre Estados (27 membros) e Municípios (27 membros), responsável por:
- Arrecadar o IBS e distribuir as receitas aos entes federados conforme o princípio do destino.
- Uniformizar a interpretação da legislação e julgar o contencioso administrativo tributário do imposto de forma colegiada e harmônica em todo o país.

## 5. Regulamentos da CBS e do IBS (2026)
Os regulamentos infralegais da LC 214/2025 foram publicados em 30/04/2026 e já estão no acervo:
| Ato | Conteúdo | Arquivo |
| :--- | :--- | :--- |
| **Decreto nº 12.955/2026** | Regulamento da CBS (620 artigos, Livros I a III), com as normas comuns ao IBS e à CBS no Livro I | [decreto-12955-2026-regulamento-cbs.md](../reforma-tributaria/regulamentos/decreto-12955-2026-regulamento-cbs.md) |
| **Decreto nº 13.075/2026** | Altera os arts. 105, 115 e 619: pessoas físicas e produtores rurais passam a se inscrever no CNPJ e a emitir documentos fiscais a partir de 1º/01/2027 | [decreto-13075-2026-altera-regulamento-cbs.md](../reforma-tributaria/regulamentos/decreto-13075-2026-altera-regulamento-cbs.md) |
| **Resolução CGIBS nº 6/2026** | Regulamento do IBS (617 artigos e Anexos I a V) | [resolucao-cgibs-6-2026-regulamento-ibs.md](../reforma-tributaria/regulamentos/resolucao-cgibs-6-2026-regulamento-ibs.md) |
| **Resolução CGIBS nº 13/2026** | Altera o art. 617 do Regulamento do IBS, espelhando o Decreto 13.075/2026 | [resolucao-cgibs-13-2026-altera-regulamento-ibs.md](../reforma-tributaria/regulamentos/resolucao-cgibs-13-2026-altera-regulamento-ibs.md) |
| **Portaria Conjunta MF/CGIBS nº 7/2026** | Reconhece o Livro I dos dois regulamentos como disposições comuns ao IBS e à CBS | [ato-150871-7-2026.md](../reguladores/rfb/outros-atos/2026/ato-150871-7-2026.md) |
## 6. Atos Conjuntos RFB/CGIBS e atos da RFB/MF sobre a CBS (2025-2026)
Os atos infralegais que operacionalizam os regulamentos ficam no caminho canônico dos atos da Receita Federal (`reguladores/rfb/outros-atos/`):
| Ato | Conteúdo | Arquivo |
| :--- | :--- | :--- |
| **Ato Conjunto RFB/CGIBS nº 1/2025** | Obrigações acessórias do IBS e da CBS em 2026 e período sem penalidades | [ato-148477-1-2025.md](../reguladores/rfb/outros-atos/2025/ato-148477-1-2025.md) |
| **Ato Conjunto RFB/CGIBS nº 2/2026** | Publicação do Manual de Integração e do Swagger da Plataforma Pública do Split Payment | [ato-151582-2-2026.md](../reguladores/rfb/outros-atos/2026/ato-151582-2-2026.md) |
| **Ato Conjunto RFB/CGIBS nº 3/2026** | Publicação da documentação técnica da Declaração de Regimes Específicos (DeRE) | [ato-151927-3-2026.md](../reguladores/rfb/outros-atos/2026/ato-151927-3-2026.md) |
| **Ato Conjunto RFB/CGIBS nº 4/2026** | Datas de início da obrigatoriedade dos documentos fiscais eletrônicos (art. 112 dos regulamentos) | [ato-152616-4-2026.md](../reguladores/rfb/outros-atos/2026/ato-152616-4-2026.md) |
| **Ato Conjunto RFB/CGIBS nº 5/2026** | Programa Nacional de Conformidade Tributária em 2026 | [ato-152862-5-2026.md](../reguladores/rfb/outros-atos/2026/ato-152862-5-2026.md) |
| **Ato Conjunto RFB/CGIBS nº 6/2026** | Dispensa de inscrição no cadastro com identificação única (CNPJ) e de emissão de documentos fiscais | [ato-153216-6-2026.md](../reguladores/rfb/outros-atos/2026/ato-153216-6-2026.md) |
| **Ato Conjunto RFB/CGIBS nº 7/2026** | Altera o Ato Conjunto nº 4/2026 (novas datas dos documentos fiscais) | [ato-154548-7-2026.md](../reguladores/rfb/outros-atos/2026/ato-154548-7-2026.md) |
| **Ato Conjunto RFB/CGIBS nº 8/2026** | Dispensa temporária de CNPJ para produtor rural e transportador autônomo de carga pessoas físicas | [ato-154689-8-2026.md](../reguladores/rfb/outros-atos/2026/ato-154689-8-2026.md) |
| **Portaria MF nº 3.074/2026** | Alíquotas específicas da CBS sobre combustíveis (Anexo em tabela) | [ato-154060-3074-2026.md](../reguladores/rfb/outros-atos/2026/ato-154060-3074-2026.md) |
| **Portaria RFB nº 763/2026** | Piloto da Reforma Tributária do Consumo para a CBS (Piloto RTC-CBS) | [ato-154673-763-2026.md](../reguladores/rfb/outros-atos/2026/ato-154673-763-2026.md) |
## 7. Atos Técnicos Conjuntos RFB/CGIBS (2026)
Os Atos Técnicos Conjuntos aprovam a documentação técnica dos documentos fiscais eletrônicos, da DeRE, da Plataforma Pública do Split Payment e dos sistemas aduaneiros, com fundamento no Decreto nº 12.955/2026 e na Resolução CGIBS nº 6/2026. Ficam no caminho canônico `reguladores/rfb/outros-atos/`:
| Ato | Conteúdo | Arquivo |
| :--- | :--- | :--- |
| **Ato Técnico Conjunto nº 1/2026** | Aprova e ratifica as Notas Técnicas de NF-e, NFC-e, CT-e, BP-e, NF3e, NFCom, NFGas e NFAg com IBS e CBS | [ato-152654-1-2026.md](../reguladores/rfb/outros-atos/2026/ato-152654-1-2026.md) |
| **Ato Técnico Conjunto nº 2/2026** | Aprova Notas e Informes Técnicos da NF-e e NFC-e, a NT do BP-e TA e os MOC da NFAg, NFGas e NF-e ABI | [ato-153091-2-2026.md](../reguladores/rfb/outros-atos/2026/ato-153091-2-2026.md) |
| **Ato Técnico Conjunto nº 3/2026** | Documentação técnica da DeRE, versão 1.2.0 | [ato-153349-3-2026.md](../reguladores/rfb/outros-atos/2026/ato-153349-3-2026.md) |
| **Ato Técnico Conjunto nº 4/2026** | Split Payment: Manual de Habilitação de Participantes e Manual de Redes | [ato-153354-4-2026.md](../reguladores/rfb/outros-atos/2026/ato-153354-4-2026.md) |
| **Ato Técnico Conjunto nº 5/2026** | Split Payment: Manuais de Operações, Integração, Tempos, Redes e Segurança e documento openAPI | [ato-153687-5-2026.md](../reguladores/rfb/outros-atos/2026/ato-153687-5-2026.md) |
| **Ato Técnico Conjunto nº 6/2026** | Documentação técnica da DeRE, versão 1.3 | [ato-153885-6-2026.md](../reguladores/rfb/outros-atos/2026/ato-153885-6-2026.md) |
| **Ato Técnico Conjunto nº 7/2026** | NFS-e: Notas Técnicas SE/CGNFS-e nº 009 e nº 010 (NFS-e e NFS-e Via) | [ato-153887-7-2026.md](../reguladores/rfb/outros-atos/2026/ato-153887-7-2026.md) |
| **Ato Técnico Conjunto nº 8/2026** | Notas Técnicas de NF-e, NFC-e, CT-e, NFCom, BP-e, NF3e, NFAg e NFGas (incluindo o DANFE da Reforma Tributária) | [ato-153886-8-2026.md](../reguladores/rfb/outros-atos/2026/ato-153886-8-2026.md) |
| **Ato Técnico Conjunto nº 9/2026** | Trabalhos conjuntos da RFB e da Diretoria Executiva do CGIBS (Coordenações e GTI), com efeitos até 31/03/2027 | [ato-154246-9-2026.md](../reguladores/rfb/outros-atos/2026/ato-154246-9-2026.md) |
| **Ato Técnico Conjunto nº 10/2026** | Notas Técnicas de DF-e, incluindo as atualizações para o Simples Nacional, e documentação da NF-e ABI | [ato-154369-10-2026.md](../reguladores/rfb/outros-atos/2026/ato-154369-10-2026.md) |
| **Ato Técnico Conjunto nº 11/2026** | Declaração Única de Importação (Duimp): layout 77.0.0 | [ato-154555-11-2026.md](../reguladores/rfb/outros-atos/2026/ato-154555-11-2026.md) |
| **Ato Técnico Conjunto nº 12/2026** | Declaração de Importação de Remessa (DIR): layout 1.0 | [ato-154556-12-2026.md](../reguladores/rfb/outros-atos/2026/ato-154556-12-2026.md) |
## 8. Simples Nacional na Reforma Tributária (Resoluções CGSN 2026)
| Ato | Conteúdo | Arquivo |
| :--- | :--- | :--- |
| **Resolução CGSN nº 186/2026** | Prazos e condições da opção pelo Simples Nacional e, para os optantes, pelo regime regular do IBS e da CBS em 2027 | [ato-150653-186-2026.md](../reguladores/rfb/outros-atos/2026/ato-150653-186-2026.md) |
| **Resolução CGSN nº 190/2026** | Altera a Resolução CGSN 140/2018; o anexo único traz os valores fixos do MEI com ICMS, ISS, CBS e IBS | [ato-152832-190-2026.md](../reguladores/rfb/outros-atos/2026/ato-152832-190-2026.md) |
| **Resolução CGSN nº 192/2026** | Altera a Resolução CGSN 11/2007 sobre a arrecadação do regime unificado, com referências ao IBS | [ato-152805-192-2026.md](../reguladores/rfb/outros-atos/2026/ato-152805-192-2026.md) |
| **Resolução CGSN nº 194/2026** | Altera a Resolução CGSN 186/2026 | [ato-153801-194-2026.md](../reguladores/rfb/outros-atos/2026/ato-153801-194-2026.md) |
| **Resolução CGSN nº 196/2026** | Altera as Resoluções CGSN 140/2018 e 190/2026; traz os Anexos I a V com alíquotas e partilha do Simples Nacional | [ato-154694-196-2026.md](../reguladores/rfb/outros-atos/2026/ato-154694-196-2026.md) |
## 9. Governança do Comitê Gestor do IBS (Resoluções CGIBS)
| Ato | Conteúdo | Arquivo |
| :--- | :--- | :--- |
| **Resolução CGIBS nº 4/2026** | Regimento Interno Procedimental | [resolucao-cgibs-4-2026-regimento-interno-procedimental.md](../reforma-tributaria/cgibs/resolucao-cgibs-4-2026-regimento-interno-procedimental.md) |
| **Resoluções CGIBS nº 5 e nº 9/2026** | Alteram o Regimento Interno Procedimental | [5](../reforma-tributaria/cgibs/resolucao-cgibs-5-2026-altera-regimento-interno.md) e [9](../reforma-tributaria/cgibs/resolucao-cgibs-9-2026-altera-regimento-procedimental.md) |
| **Resolução CGIBS nº 14/2026** | Proposta do percentual do IBS destinado ao financiamento do CGIBS em 2027 e estimativa de arrecadação do IBS | [resolucao-cgibs-14-2026-percentual-ibs-financiamento-cgibs-2027.md](../reforma-tributaria/cgibs/resolucao-cgibs-14-2026-percentual-ibs-financiamento-cgibs-2027.md) |
| **Resolução CGIBS nº 20/2026** | Tipologia, competência e publicidade dos atos e instrumentos formais do CGIBS | [resolucao-cgibs-20-2026-tipologia-dos-atos.md](../reforma-tributaria/cgibs/resolucao-cgibs-20-2026-tipologia-dos-atos.md) |
## 10. Publicações Institucionais e Orientações Técnicas (2026)
- **Cálculo da Alíquota de Referência pelo TCU ([Relatório TCU 2026](../reforma-tributaria/publicacoes/2026/tcu-calculo-referencia-cbs-2027.md)):** Estudo técnico do Tribunal de Contas da União estimando a alíquota de referência federal da CBS para 2027 em **11,3%**.
- **Cronograma de Documentos Fiscais Eletrônicos da RFB ([Orientação RFB 2026](../reforma-tributaria/publicacoes/2026/rfb-cronograma-documentos-fiscais.md)):** Cronograma de adequação das NF-e, NFC-e e CT-e aos campos e regras do IBS, CBS e Split Payment.
- **Adequação Tarifária do Saneamento pela ANA ([Resolução ANA 2026](../reforma-tributaria/publicacoes/2026/ana-adequacao-tarifas-saneamento-cbs.md)):** Diretrizes da Agência Nacional de Águas e Saneamento Básico para o reequilíbrio econômico-financeiro dos contratos de concessão perante a entrada em vigor da CBS.
