# Relatório Técnico de Auditoria Tributária Estadual: Piauí (PI)

**Data de Elaboração:** Outubro de 2026  
**Competência Analítica:** Direito Tributário Estadual e Relações Federativas  
**Unidade Federativa Auditada:** Estado do Piauí (PI)  
**Arquivo de Referência:** `_auditoria/estados/auditoria_pi.md`  

---

## 1. Auditoria do Acervo Normativo Estadual

### 1.1 Normas Presentes no Repositório (`estaduais/pi/`)
A auditoria efetuada na base documental do repositório identificou os seguintes arquivos na pasta `estaduais/pi/`:
* `ricms/decreto-21866-2023.md`: Novo Regulamento do ICMS do Estado do Piauí (Decreto Estadual nº 21.866, de 6 de março de 2023, que revogou o histórico Decreto nº 13.500/2008). Contém as regras de incidência, fato gerador, não incidência, alíquotas (alíquota modal fixada em 21% com esteio na Lei Complementar nº 269/2022), regras de DIFAL, antecipação tributária e parametrização das transferências entre filiais.
* `leis/itcmd/lei-4261-1989.md`: Lei Estadual nº 4.261, de 1º de fevereiro de 1989, que disciplina o Imposto sobre a Transmissão Causa Mortis e Doação de Quaisquer Bens ou Direitos (ITCD/ITCMD) no Piauí, fixando tabelas progressivas de alíquotas e hipóteses de isenção.
* `leis/ipva/lei-4548-1992.md`: Lei Estadual nº 4.548, de 29 de dezembro de 1992, regulamentando o Imposto sobre a Propriedade de Veículos Automotores (IPVA), fato gerador, base de cálculo e repartição de receitas.

### 1.2 Normas Fundamentais Faltantes no Repositório
Para assegurar a completude e segurança técnica das análises tributárias do Piauí, aponta-se a necessidade de inclusão dos seguintes diplomas:

1. **Lei Básica Geral do ICMS (Lei Estadual nº 4.257, de 6 de janeiro de 1989):**
   * *Status:* Ausente em pasta autônoma `estaduais/pi/leis/icms/`.
   * *Relevância:* É a matriz legislativa ordinária do ICMS piauiense. Define legalmente as hipóteses de incidência, base de cálculo, regimes de arbitramento, responsabilidade de transportadores e intermediadores, multas moratórias e punitivas. Deve estar devidamente consolidada com a **Lei Complementar Estadual nº 269, de 8 de dezembro de 2022** (que elevou a alíquota interna básica modal de 18% para 21%) e com a **Lei Estadual nº 7.731, de 21 de janeiro de 2022** (adequação do DIFAL às balizas da LC 190/2021).
2. **Fundo Estadual de Combate à Pobreza (FECOP/PI):**
   * *Status:* Ausente.
   * *Relevância:* Instituído pela **Lei Estadual nº 5.622, de 28 de dezembro de 2006** (fundamentada no art. 82 do ADCT da CF/88) e regulamentado pelo **Decreto Estadual nº 12.502/2007** e alterações posteriores. Adiciona até 2% (dois pontos percentuais) na alíquota do ICMS sobre mercadorias supérfluas (bebidas alcoólicas, cigarros, combustíveis automotivos da classe gasolina, joias, armas e munições).
3. **Lei do Processo Administrativo Tributário (PAT/PI):**
   * *Status:* Ausente em `estaduais/pi/leis/pat/`.
   * *Relevância:* Disciplinado originariamente pela **Lei Estadual nº 4.254, de 27 de dezembro de 1988**, combinada com as regras de contencioso fiscal e julgamento em instâncias ordinárias perante o **Conselho de Contribuintes do Estado do Piauí (CONSEF/PI)**, definindo prazos de defesa, nulidades de autos de infração e pedidos de reconsideração.
4. **Legislação de Fomento e Benefícios Fiscais Convalidados:**
   * **PRODEPI (Programa de Desenvolvimento Econômico do Estado do Piauí - Lei Estadual nº 4.859/1996 e Decreto nº 9.698/1997):** Principal diploma de incentivos fiscais do estado, outorgando crédito presumido de ICMS de até 90% a 95% do saldo devedor para indústrias de transformação, agronegócio e energia renovável. Convalidado pelo Convênio ICMS 190/2017 nos termos da LC 160/2017.
   * **Regime Especial de Tributação para Atacadistas (Decreto nº 21.866/2023 / Decreto anterior nº 17.587/2017):** Carga tributária reduzida e crédito outorgado na distribuição atacadista.
   * **Incentivos ao Complexo de Energias Renováveis (Decretos Estaduais de Fomento Eólico e Solar):** Tratamento tributário favorecido com isenção ou diferimento na importação e aquisição interna de aerogeradores, painéis fotovoltaicos e inversores de frequência.

---

## 2. Relacionamento Tributário Interestadual

### 2.1 Alíquotas Interestaduais Aplicáveis
Em virtude da localização do Piauí na Região Nordeste e da aplicação cogente das Resoluções do Senado Federal nº 22/1989 e nº 13/2012:
* **Saídas Interestaduais promovidas por contribuintes piauienses:** Alíquota uniforme de **12%**, independentemente do estado de destino.
* **Entradas Interestaduais destinadas a contribuintes do Piauí:**
  * Alíquota de **7%**, nas remessas originadas dos Estados das Regiões Sul e Sudeste (exceto Espírito Santo).
  * Alíquota de **12%**, nas remessas originadas dos Estados das Regiões Norte, Nordeste, Centro-Oeste e do Estado do Espírito Santo.
* **Bens e Mercadorias Importadas do Exterior (ou com Conteúdo de Importação > 40%):** Alíquota de **4%** (Resolução SF nº 13/2012 e Convênio ICMS nº 38/2013), com exceção das mercadorias sem similar nacional constantes da Lista CAMEX e produtos sob incentivo da Lei de Informática.

### 2.2 Diferencial de Alíquotas (DIFAL)
O ordenamento do Piauí disciplina o DIFAL em duas frentes:

#### A) DIFAL Contribuinte (Uso, Consumo ou Ativo Permanente)
Regulado pela Lei Estadual nº 4.257/1989 e arts. 62 e seguintes do Novo RICMS/PI (Decreto nº 21.866/2023):
* **Metodologia de Base Dupla ("Cálculo por Dentro"):** O Piauí exige a recomposição da base de cálculo com a alíquota interna piauiense (21%):
$$\text{Base Dupla} = \frac{\text{Valor da Operação na Origem} - \text{ICMS Origem}}{1 - \text{Alíquota Interna PI}}$$
$$\text{DIFAL Devido} = (\text{Base Dupla} \times \text{Alíquota Interna PI}) - (\text{Valor Operação Origem} \times \text{Alíquota Interestadual})$$
* **Demonstrativo Financeiro (Entrada de Transformador Elétrico de MG para Usina Solar em Bom Jesus/PI):**
  * Valor de Nota de Origem (MG): R$ 1.000.000,00 com alíquota interestadual de 7% (ICMS Origem = R$ 70.000,00).
  * Valor líquido sem ICMS na Origem: R$ 930.000,00.
  * Alíquota interna do Piauí: 21%.
  * Base Recomposta: $\frac{930.000}{1 - 0,21} = \frac{930.000}{0,79} \approx \text{R\$} 1.177.215,19$.
  * ICMS Total Interno PI: $1.177.215,19 \times 21\% \approx \text{R\$} 247.215,19$.
  * DIFAL a recolher à SEFAZ/PI: $247.215,19 - 70.000,00 = \text{R\$} 177.215,19$.
  *(A carga real efetiva do diferencial alcança 17,72% do valor da nota fiscal de origem, sobrecarregando em quase 4 pontos percentuais a diferença nominal de 14%).*

#### B) DIFAL Não Contribuinte (EC 87/2015, LC 190/2021 e Lei Estadual nº 7.731/2022)
* Incide nas vendas destinadas a pessoas físicas ou jurídicas não inscritas como contribuintes habituais do imposto no Piauí (e-commerce e televendas).
* Utiliza base única calculada com base na operação final, devendo o remetente de outra UF apurar o tributo pela diferença entre a alíquota interna piauiense (21% ou 23% para supérfluos com FECOP) e a interestadual aplicável.
* Recolhimento operacionalizado via GNRE para cada nota fiscal ou mensalmente caso o estabelecimento remetente detenha inscrição estadual especial como substituto tributário na SEFAZ/PI.

### 2.3 Transferências entre Estabelecimentos do Mesmo Titular (ADC 49/STF, LC 204/2023, Convênios 178/2023 e 109/2024)
* **Regramento no Novo RICMS/PI (Decreto nº 21.866/2023):** As remessas entre matriz e filiais não constituem fato gerador do ICMS (CFOP `6.151`/`6.152` na saída e `2.151`/`2.152` na entrada).
* **Transferência de Créditos (Convênio ICMS 178/2023):** É obrigatória a transferência escritural do crédito do remetente para a filial recebedora, limitada à aplicação das alíquotas interestaduais (12% ou 4%) sobre o custo de produção ou de aquisição recente.
* **Opção Anual pela Equiparação Tributária (Convênio ICMS 109/2024):** Contribuintes sediados no Piauí podem lavrar termo no RUDFTO eletrônico optando por equiparar as transferências a operações tributadas ordinárias, gerando débito destacado de 12% ou 4% na NF-e de saída e assegurando a compensação na filial de destino.

### 2.4 Substituição Tributária (ICMS-ST) e Protocolos CONFAZ
* O Piauí regulamenta o ICMS-ST em conformidade com o **Convênio ICMS 142/2018**.
* **Segmentos sob ICMS-ST no PI:** Combustíveis e lubrificantes, bebidas (cervejas, refrigerantes, águas minerais e destilados), cimento, autopeças, pneumáticos, materiais de construção e acabamento, medicamentos e produtos farmacêuticos, lâmpadas e materiais elétricos.
* **Cálculo da MVA Ajustada:**
$$\text{MVA Ajustada} = \left[ \frac{(1 + \text{MVA-ST Original}) \times (1 - \text{ALQ Inter})}{(1 - \text{ALQ Intra})} \right] - 1$$
Com ALQ Intra de 21% e ALQ Inter de 7% (mercadorias do Sul/Sudeste), o fator multiplicador é:
$$\text{Fator de Ajuste} = \frac{1 - 0,07}{1 - 0,21} = \frac{0,93}{0,79} \approx 1,1772$$
Uma majoração compulsória de 17,72% sobre a margem de agregação original do produto.

---

## 3. Mecanismos de Dedução, Tomada de Crédito e Restrições

### 3.1 Regime de Não-Cumulatividade e Manutenção de Crédito
* Estruturado com base no art. 155, § 2º, I da CF/88 e nos arts. 25 a 35 da Lei Estadual nº 4.257/1989 e Novo RICMS/PI.
* **Desoneração Plena das Exportações:** Os créditos de ICMS cobrados nas aquisições de insumos, matérias-primas e embalagens destinadas a produtos exportados (grãos do MATOPIBA, cera de carnaúba, mel) são integralmente mantidos e acumulados na escrita fiscal, vedado qualquer estorno pelo Fisco estadual (art. 21, § 2º da LC 87/1996).
* **Estorno de Crédito:** Aplicável nas saídas isentas ou não tributadas ocorridas sem previsão legal de manutenção, bem como nos casos comprovados de extravio, perda física ou deterioração de estoques.

### 3.2 Ativo Permanente e Controle via CIAP (1/48 avos)
* Em observância estrita à Lei Complementar nº 102/2000 e aos arts. 75 e seguintes do Decreto Estadual nº 21.866/2023, a tomada de crédito sobre ativos imobilizados ocorre à fração de **1/48 por mês**.
* **Fórmula de Apropriação:**
$$\text{Relação Mensal} = \frac{\text{Saídas e Prestações Tributadas} + \text{Saídas para o Exterior}}{\text{Total Geral das Saídas e Prestações}}$$
$$\text{Crédito Escriturado} = \left( \frac{\text{ICMS Total de Entrada}}{48} \right) \times \text{Relação Mensal}$$
* Registrado no **Bloco G da EFD-ICMS/IPI**. Em caso de alienação ou baixa do bem antes de decorridos 48 meses da entrada em operação, o saldo remanescente das frações não apropriadas é cancelado sem direito a qualquer indenização tributária.

### 3.3 Restrições de Crédito para Energia Elétrica e Telecomunicações
* **Energia Elétrica (LC 87/1996, art. 33, II):**
  * O crédito de ICMS somente pode ser apropriado por estabelecimentos industriais sobre o consumo efetivo no processo produtivo de transformação (obrigatória a apresentação de laudo técnico de eficiência e demanda energética homologado por engenheiro habilitado).
  * Admite-se também o crédito proporcional para empresas exportadoras diretas.
* **Comunicações (LC 87/1996, art. 33, IV):**
  * Restrito estritamente a empresas que prestem serviços de telecomunicações para terceiros ou que efetuem operações e prestações voltadas à exportação exterior.

### 3.4 Impacto do Adicional do FECOP (2%)
* A parcela adicional de 2% do FECOP cobrada sobre bens e serviços supérfluos não dá direito a crédito compensável para o contribuinte que a suporta em operações subsequentes.
* Trata-se de recolhimento segregado, carimbado para políticas de assistência social, devendo ser recolhido por meio de DAR (Documento de Arrecadação de Receitas) com código específico de receita.

---

## 4. Setor Agrícola e Rural (Cerrado Piauiense no MATOPIBA e Bacias Tradicionais)

### 4.1 Caracterização Regional e Econômica
O Piauí experimenta duas realidades agropecuárias dinâmicas e complementares:
1. **O Polo de Grãos do Cerrado Piauiense (MATOPIBA):** Concentrado na porção Sudoeste do Estado, nos municípios de **Uruçuí, Bom Jesus, Currais, Baixa Grande do Ribeiro, Santa Filomena, Ribeiro Gonçalves e Gilbués**.
   * Região com topografia plana ideal para mecanização pesada, solo profundo e regularidade de chuvas.
   * Produção maciça de soja em grão, milho safrinha, algodão em pluma e sorgo granífero, figurando entre as fronteiras agrícolas de maior expansão de produtividade por hectare do Brasil.
2. **Polo Apícola do Semiárido (Região de Picos e Simplício Mendes):**
   * Maior bacia de apicultura e maior polo exportador de mel do Brasil, destacando-se pelo mel silvestre orgânico certificado internacionalmente (sem resíduos de pesticidas), exportado majoritariamente para a União Europeia e Estados Unidos.
3. **Cera e Pó da Carnaúba (Vale do Rio Parnaíba e Norte Piauiense):**
   * Atividade extrativa e agroindustrial milenar com refino da cera de carnaúba (aplicada na indústria automobilística, alimentícia, cosmética e farmacêutica global), gerando divisas de exportação.

### 4.2 Insumos Agropecuários (Convênio ICMS 100/1997 e Convênio ICMS 26/2021)
* O Piauí aplica as regras do Convênio ICMS nº 100/1997 e prorrogações:
  * **Isenção e Redução da Base de Cálculo:** Nas saídas internas de sementes fiscalizadas, fertilizantes químicos e biológicos, mudas de plantas, corretivos agrícolas e defensivos fitossanitários.
  * **Tributação Interestadual Escalonada:** Cumprimento da tabela progressiva do Convênio 26/2021, que fixou a tributação gradual de adubos e fertilizantes nas saídas interestaduais com alíquota consolidada de até 4% em 2025.

### 4.3 Diferimento do ICMS nas Saídas de Grãos e Produtos Rurais
* O Decreto Estadual nº 21.866/2023 assegura o **diferimento do lançamento do ICMS** para as saídas internas de soja, milho e algodão promovidas por produtores rurais com destino a:
  1. Estabelecimentos esmagadores e agroindústrias instaladas em território piauiense (ex.: complexo esmagador de Uruçuí);
  2. Cooperativas de produtores rurais constituídas no estado;
  3. Armazéns gerais e empresas comerciais exportadoras (tradings) com fim exclusivo de embarque para o exterior.
* O imposto diferido considera-se recolhido nas operações de exportação (por imunidade) ou transfere-se para o adquirente industrial quando da saída subsequente do óleo refinado ou farelo de soja.

### 4.4 NFP-e (Modelo 55) e Regime Simplificado do Produtor Rural
* **Nota Fiscal Eletrônica de Produtor Rural:** A emissão da NFP-e (modelo 55) é obrigatória para todas as saídas de mercadorias promovidas por produtores rurais do Piauí, com a definitiva desativação dos blocos de notas fiscais avulsas em papel.
* **Regime Especial do Produtor Pessoa Física:** Isenção de obrigações acessórias complexas (dispensa da apresentação de Sped EFD-ICMS/IPI e livros contábeis completos) para produtores rurais não personificados como pessoa jurídica, mantendo-se a escrituração simplificada das notas fiscais no portal da SEFAZ/PI.

---

## 5. Setor Industrial, Energias Renováveis e Mineração

### 5.1 O Hub de Energias Renováveis (Eólica e Solar Fotovoltaica)
* O Piauí desponta como protagonista absoluto da transição energética do Brasil e da América Latina:
  * **Complexos Eólicos:** Concentrados na **Chapada do Araripe e no Vale do Canindé (Simões, Marcolândia, Caldeirão Grande do Piauí e Curral Novo)** e no Litoral (Ilha Grande e Parnaíba), aproveitando os ventos constantes de alta densidade;
  * **Complexos Solares Fotovoltaicos:** Sedia o **Parque Solar de São Gonçalo do Gurguéia** (um dos maiores parques solares da América Latina, operado pela Enel Green Power) e os complexos solares de **Ribeira do Piauí, Caldeirão Grande e São João do Piauí**, com capacidade instalada de múltiplos gigawatts.
* **Tratamento Tributário das Energias Renováveis:**
  * **Diferimento e Isenção na Entrada de Equipamentos:** Concessão de diferimento do ICMS nas importações e aquisições interestaduais (DIFAL) de aerogeradores, pás eólicas, torres de aço, inversores de corrente contínua/alternada e módulos fotovoltaicos de silício cristalino;
  * **Autoprodução e Transmissão de Energia:** Isenção e regras especiais de compensação na conexão à Rede Básica do Sistema Interligado Nacional (SIN) e na geração distribuída (Convênio ICMS nº 16/2015 e Convênio ICMS 109/2014).

### 5.2 O Complexo Agroindustrial de Grãos em Uruçuí
* A cidade de **Uruçuí** consolidou-se como a "capital do agronegócio piauiense", abrigando mega-complexos industriais de processamento e esmagamento de grãos da **Bunge** e tradings internacionais.
* As indústrias realizam a extração de óleo degomado de soja e produção de farelo proteico para nutrição animal, integrando incentivos do PRODEPI (crédito outorgado) com regimes de drawback aduaneiro para os grãos que são escoados pela malha ferroviária e rodoviária rumo ao Porto do Itaqui (MA).

### 5.3 O Polo Mineral e Joalheiro de Pedro II (Opala Nobre)
* O município de **Pedro II**, no Norte piauiense, abriga uma das únicas reservas comerciais de **Opala nobre** do planeta (ao lado da Austrália).
* A atividade engloba a extração mineral artesanal e industrial, lapidação e joalheria de prata e ouro. A tributação goza de tratamento diferenciado nas saídas internas para o artesanato mineral e na circulação voltada ao turismo cultural.

### 5.4 O Programa de Desenvolvimento Econômico do Piauí (PRODEPI)
* Instituído pela **Lei Estadual nº 4.859/1996** e regulamentado pelo **Decreto Estadual nº 9.698/1997**:
  * É o principal instrumento financeiro-fiscal do estado, convalidado pelo Convênio ICMS nº 190/2017 nos termos da LC 160/2017.
  * Otorga às indústrias instaladas ou em expansão no estado um **crédito presumido de até 90% a 95% do ICMS apurado** sobre as operações próprias industriais.
  * Concede dilação de prazo de recolhimento e diferimento do imposto incidente sobre a importação de máquinas, aparelhos e equipamentos que integrem o ativo imobilizado fabril.

---

## 6. Setor de Produto Acabado: Atacado, Varejo e Distribuição

### 6.1 Regime Especial do Comércio Atacadista (Decreto nº 21.866/2023)
* Para consolidar o Piauí (especialmente as cidades de Teresina, Floriano e Picos) como polo de abastecimento atacadista regional e barrar a dependência comercial de centros como Fortaleza (CE) e Recife (PE), o Decreto nº 21.866/2023 previu a sistemática especial para o comércio atacadista.
* **Mecanismos do Regime Atacadista Piauiense:**
  * Recolhimento do ICMS na entrada interestadual com carga tributária reduzida e encerramento de fase para determinadas mercadorias;
  * Outorga de crédito presumido de ICMS nas saídas que garante às empresas atacadistas credenciadas uma **carga tributária líquida efetiva entre 1% e 3%**;
  * Estorno proporcional dos créditos ordinários de entrada para compatibilização da carga favorecida.

### 6.2 Pautas Fiscais e MVA Setorial
* A SEFAZ/PI utiliza pautas fiscais de valores mínimos de referência e Preço Médio Ponderado a Consumidor Final (PMPF) para produtos de alta rotatividade:
  * Combustíveis automotivos e gás de cozinha;
  * Bebidas alcoólicas, refrigerantes e águas envasadas;
  * Farinha de trigo e cimento Portland.
* Para as demais mercadorias submetidas ao ICMS-ST, aplica-se a margem de agregação calculada pela MVA Ajustada com base na alíquota interna de 21% (+ FECOP).

### 6.3 E-commerce, Fiscalização de Trânsito e Intermediação Digital
* **Fiscalização em Postos Fiscais de Fronteira:** O Piauí mantém forte estrutura de controle e fiscalização nas divisas com Maranhão, Ceará, Pernambuco e Bahia, conferindo as notas fiscais eletrônicas de carga via leitor de Manifesto Eletrônico de Documentos Fiscais (MDF-e).
* **DIMP e Responsabilidade Solidária:** A SEFAZ/PI utiliza amplamente os dados do Convênio ICMS 169/2022 (DIMP) para fiscalizar as operações de comércio eletrônico desacompanhadas de documentação idônea.
* As plataformas digitais e marketplaces que operam no território piauiense possuem responsabilidade solidária formalmente atribuída pela Lei nº 4.257/1989 em casos de omissão de emissão ou envio de mercadorias sem recolhimento prévio do DIFAL não contribuinte.

---

## 7. Transição para o IBS / CBS da Reforma Tributária (EC 132/2023 e LC 214/2025)

### 7.1 Impacto Fiscal e Redistributivo para o Piauí (Princípio do Destino)
* O Estado do Piauí é, de forma inconteste, um **importador líquido de mercadorias, insumos e bens finais de consumo**. Com base econômica secundária concentrada no agronegócio primário e em energias renováveis (ambos fortemente desonerados nas saídas de exportação ou no mercado atacadista), o Estado consome a quase totalidade de bens manufaturados produzidos no Sul e Sudeste.
* Sob a sistemática do ICMS tradicional, a receita tributária correspondente à alíquota de 7% fica retida nos estados produtores (origem).
* **Ganho Projetado com a Emenda Constitucional nº 132/2023:** A fixação definitiva do **princípio do destino puro (art. 156-A da CF/88)** transformará o perfil da arrecadação piauiense. O IBS cobrado sobre todos os bens e serviços consumidos pela população de Teresina, Parnaíba, Picos e de todo o interior será recolhido integralmente aos cofres do Estado do Piauí e seus 224 municípios. O Piauí figura, em todos os estudos fazendários nacionais, como um dos maiores beneficiários líquidos em termos de ampliação percentual de arrecadação per capita ao longo da transição federativa.

### 7.2 Extinção do ICMS e Perda dos Incentivos Locais (PRODEPI)
* De acordo com as disposições constitucionais, as alíquotas do ICMS serão reduzidas proporcionalmente entre 2029 e 2032 (90%, 80%, 70% e 60% da alíquota vigente), ocorrendo a extinção completa em 2033.
* O PRODEPI e os regimes especiais para o setor atacadista e energias renováveis serão extintos por ausência de objeto em 31 de dezembro de 2032. O Piauí não poderá mais utilizar a ferramenta do crédito presumido para atrair indústrias, devendo competir com infraestrutura, disponibilidade de energia limpa e qualificação técnica.

### 7.3 Habilitação ao Fundo de Compensação de Benefícios Fiscais (FCBF)
* As indústrias do agronegócio em Uruçuí (Bunge) e os investidores dos parques solares e eólicos que possuem benefícios outorgados e convalidados sob o amparo da LC 160/2017 e do Convênio ICMS 190/2017 terão direito às verbas do FCBF (art. 159-A da CF/88 e LC 214/2025).
* O Comitê Gestor do IBS e a União Federal operacionalizarão a transferência de recursos financeiros compensatórios de forma decrescente no quadriênio 2029-2032, exigindo-se prova de regularidade cadastral e adimplemento das obrigações assumidas perante o Estado do Piauí.

### 7.4 Homologação de Saldos Credores de ICMS (Art. 134 do ADCT)
* O polo exportador de grãos do cerrado de Bom Jesus e Uruçuí, os exportadores de mel de Picos e as empresas de energia geram créditos acumulados substanciais de ICMS por força da imunidade constitucional da Lei Kandir.
* **Processamento dos Saldos Acumulados perante a LC 214/2025:**
  1. Os saldos credores de ICMS escriturados até 31 de dezembro de 2032 devem ser submetidos à **homologação formal e expressa perante a SEFAZ/PI**;
  2. Os créditos homologados serão convertidos em parcelas de abatimento contra o IBS devido à razão de **1/240 por mês ao longo de 20 anos**, corrigidos pela inflação medida pelo IPCA;
  3. Contribuintes que apresentarem excedentes de parcelas de 1/240 em relação aos seus débitos próprios de IBS poderão transferi-los a terceiros contribuintes devedores de IBS, sob regulação do Comitê Gestor.
* **Risco Iminente de Glosa:** O Estado do Piauí tradicionalmente adota postura fiscal rigorosa e restritiva no reconhecimento de créditos de exportação. Os contribuintes locais devem promover uma auditoria prévia profunda de sua escrituração fiscal eletrônica para afastar passivos e fundamentar robustamente todos os créditos que serão pleiteados na transição.

---

## 8. Conclusão e Matriz de Riscos

| Eixo Temático | Situação Atual no Piauí | Ponto Crítico / Risco Identificado | Ação Corretiva Recomendada |
| :--- | :--- | :--- | :--- |
| **Normas no Repositório** | Novo RICMS (Dec. 21.866/23), ITCD e IPVA presentes. Faltam Lei 4.257/89 completa, FECOP, PAT e PRODEPI. | Descompasso com a base legal primária das infrações e regimes de incentivo. | Inserir `leis/icms/lei-4257-1989.md`, `leis/fcp/lei-5622-2006.md` e `leis/pat/lei-4254-1988.md`. |
| **DIFAL e Substituição Tributária** | Alíquota básica de 21% (+ FECOP em supérfluos). DIFAL contribuinte com base dupla e MVA ajustada pesada. | Custo fiscal exorbitante na importação e aquisição interestadual de bens de capital para parques solares e eólicos. | Utilização de pleitos de diferimento específicos do PRODEPI e revisão de enquadramento NCM. |
| **Agronegócio (MATOPIBA) e Apicultura** | Cerrado com alta produtividade (Uruçuí/Bom Jesus) e polo apícola em Picos; diferimento amplo nas saídas internas. | Acúmulo maciço de créditos de ICMS sem liquidez imediata nas tradings e esmagadoras. | Organização dos dossiês de exportação para conversão futura no regime de 240 meses da LC 214/2025. |
| **Energias Renováveis e PRODEPI** | Polo eólico e solar de relevância continental; benefícios do PRODEPI convalidados até 2032. | Fim dos incentivos fiscais em 2032 e impacto na taxa interna de retorno (TIR) de novos projetos. | Habilitação rigorosa no FCBF e adequação dos contratos de longo prazo ao modelo do IBS/CBS. |
| **Reforma Tributária** | Piauí é estado fortemente beneficiado pelo princípio do destino. | Período de transição de 240 meses para liquidação de créditos acumulados e risco de cancelamento administrativo pela SEFAZ/PI. | Saneamento preventivo da escrituração do Sped Fiscal e governança tributária integrada. |
