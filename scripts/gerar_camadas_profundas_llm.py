"""Gera e audita as 4 Camadas Profundas para Inferência de LLMs sobre Regras Nacionais, Estaduais e entre Estados:

1. Anexos II a XXVII do Convênio ICMS 142/2018 (Segmentos CEST 01 a 28 x NCM) e Mapa de Protocolos de ICMS-ST por UF
2. Legislação de Benefícios Fiscais e Regimes Especiais Estaduais Convalidados (TTD SC, COMPETE-ES, TTS MG, PROGOIÁS, PRODEPE PE, Atacadista/DESENVOLVE BA, Carga Líquida/FDI CE, ZFM/PIM AM e Atacadista/E-Commerce TO)
3. Resolução CGSN nº 140/2018 Consolidada (Regulamento Completo do Simples Nacional: Anexos I a V, Fator 'r', Sublimite Estadual de R$ 3,6 milhões, Permissão de Crédito CSOSN 101 e Regras Interestaduais)
4. Guia Prático da EFD-ICMS/IPI (SPED Fiscal: Registros C100, C197, E110, E200 ST por UF, E300 DIFAL/FCP por UF, Bloco G CIAP e Bloco K) e Nota Técnica NF-e 2024.002 (Leiautes XML de IBS, CBS e Imposto Seletivo)
"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from comum import gerar_frontmatter, salvar_atomico
from agente_auditor import AgenteAuditor

CAMADAS_LLM = [
    # =========================================================================
    # CAMADA 1: TABELAS DE SEGMENTOS CEST X NCM E MAPA DE PROTOCOLOS ICMS-ST POR UF
    # =========================================================================
    {
        "caminho": "estaduais/confaz/convenios-icms/2018/convenio-icms-142-2018-anexos-cest-ncm.md",
        "titulo": "Anexos II a XXVII do Convênio ICMS nº 142/2018 (Tabela Nacional de Segmentos CEST 01 a 28 x NCM para Substituição Tributária)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Anexo de Convênio ICMS",
        "numero": "142-ANEXOS",
        "ano": "2018",
        "data": "2018-12-14",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2018/CV142_18",
        "ementa": "Consolida os Anexos II a XXVII do Convênio ICMS nº 142/2018, detalhando os 26 segmentos ativos do Código Especificador da Substituição Tributária (CEST), faixas de NCM/SH e a regra de dupla condição cumulativa (NCM + descrição + segmento) para incidência do ICMS-ST.",
        "corpo": """# Anexos II a XXVII do Convênio ICMS nº 142/2018 (Tabela Nacional de Segmentos CEST 01 a 28 x NCM para Substituição Tributária)

ANEXOS II A XXVII DO CONVÊNIO ICMS Nº 142, DE 14 DE DEZEMBRO DE 2018

## 1. Regra Fundamental de Enquadramento no ICMS-ST (Cláusula Sétima e Decisão Normativa)

Para que uma mercadoria esteja sujeita ao regime de **Substituição Tributária (ICMS-ST)** ou **Antecipação com Encerramento de Tributação** em operação interna ou interestadual, devem ser atendidas **cumulativamente 3 (três) condições**:
1. **Condição 1 — Previsão no Convênio ICMS nº 142/2018 (Autorizativo Nacional):** O produto deve constar em um dos Anexos II a XXVII do Convênio ICMS nº 142/2018, identificado simultaneamente pelo seu **código NCM/SH**, pela **descrição exata da mercadoria** e pelo **segmento econômico correspondente (2 primeiros dígitos do CEST)**;
2. **Condição 2 — Previsão na Legislação Interna do Estado de Destino:** Como o Convênio ICMS nº 142/2018 é **autorizativo**, o Estado de destino deve ter incluído expressamente aquele CEST/NCM em seu próprio Regulamento do ICMS (RICMS) ou portaria de ST;
3. **Condição 3 — Existência de Convênio ou Protocolo ICMS entre a UF de Origem e a UF de Destino (nas operações interestaduais):**
   - **Se houver Protocolo/Convênio vigente entre os dois Estados:** O **remetente** (na UF de origem) é o substituto tributário responsável por reter o ICMS-ST na NF-e (CFOP `6.401`, `6.403` ou `6.404`) e recolhê-lo em favor da UF de destino (GNRE código `10009-9` por operação ou `10004-8` por apuração mensal);
   - **Se NÃO houver Protocolo/Convênio entre a UF de origem e a UF de destino, mas a mercadoria tiver ST interna na UF de destino:** O remetente emite a NF-e sem retenção de ST (CFOP `6.101` ou `6.102`), e a responsabilidade recai sobre o **adquirente destinatário** pela **Antecipação Tributária com encerramento de fase** na entrada do território do Estado de destino (ex.: art. 426-A do RICMS/SP).

---

## 2. Estrutura do Código CEST (`SS.III.DD`)

O **Código Especificador da Substituição Tributária (CEST)** é composto por **7 (sete) dígitos numéricos** (`SS.III.DD`):
- **`SS` (1º e 2º dígitos):** Identificam o **Segmento** do bem ou mercadoria (`01` a `28`);
- **`III` (3º ao 5º dígitos):** Identificam o **Item** de um mesmo segmento;
- **`DD` (6º e 7º dígitos):** Especificam o **Desdobramento** de um item.

---

## 3. Tabela Completa dos Anexos e Segmentos do Convênio ICMS nº 142/2018

| Anexo do Convênio 142/18 | Prefixo CEST (`SS`) | Segmento Econômico | Principais Capítulos / Posições da NCM/SH Abrangidas | Principais Convênios / Protocolos Setoriais de Referência |
| :---: | :---: | :--- | :--- | :--- |
| **Anexo II** | **`01.xxx.xx`** | **Autopeças** | Caps. 39, 40 (pneus/câmaras/correias), 68, 70 (vidros automotivos), 73, 83, 84 (motores/bombas/filtros), 85 (baterias/ignição/faróis), 87 (partes e peças do `8708`), 90 | Protocolos ICMS `41/2008` e `97/2010` |
| **Anexo III** | **`02.xxx.xx`** | **Bebidas Alcoólicas, exceto Cerveja e Chope** | Posições `2204` (vinhos), `2205` (vermutes), `2206` (sidras/hidromel), `2207` e `2208` (destilados: uísque, vodca, cachaça, gim, licores) | Protocolos ICMS `14/2006`, `96/2009` e `103/2012` |
| **Anexo IV** | **`03.xxx.xx`** | **Cervejas, Chopes, Refrigerantes, Águas e Outras Bebidas (Bebidas Frias)** | Posições `2201` (águas minerais e gelo), `2202` (refrigerantes, energéticos, isotônicos, chás prontos) e `2203` (cervejas de malte e chopes) | Protocolos ICMS `11/1991` e `10/1992` |
| **Anexo V** | **`04.xxx.xx`** | **Cigarros e Outros Produtos Derivados do Fumo** | Posições `2401`, `2402` (charutos, cigarrilhas e cigarros contendo tabaco) e `2403` (tabaco para fumar, fumo picado) | Convênio ICMS `111/2017` |
| **Anexo VI** | **`05.xxx.xx`** | **Cimentos** | Posições `2523` (cimento Portland branco, comum, aluminoso, de escórias, pozolânico) | Protocolo ICMS `11/1985` |
| **Anexo VII** | **`06.xxx.xx`** | **Combustíveis e Lubrificantes** | Posições `2207` (etanol hidratado EHC e anidro EAC), `2710` (gasolinas, óleo diesel, querosene de aviação, óleos combustíveis, óleos lubrificantes), `2711` (GLP e gás natural), `3826` (biodiesel B100) | LC `192/2022`, Convênios ICMS `110/2007`, `199/2022` e `15/2023` |
| **Anexo VIII** | **`07.xxx.xx`** | **Energia Elétrica** | Posição `2716.00.00` (energia elétrica destinada à comercialização, industrialização ou consumo em ambiente livre ACL/ACR) | Convênios ICMS `83/2000` e `77/2011` |
| **Anexo IX** | **`08.xxx.xx`** | **Ferramentas** | Capítulo `82` (ferramentas manuais, serras, limas, alicates, chaves de porcas, ferramentas intercambiáveis, facas industriais) e `9017` (instrumentos de medida) | Protocolos ICMS `193/2009` e `27/2010` |
| **Anexo X** | **`09.xxx.xx`** | **Lâmpadas, Reatores e "Starter"** | Posições `8539` (lâmpadas e tubos de incandescência, descarga ou LED), `8504.10.00` (reatores) e `8536.50` (*starters*) | Protocolo ICMS `17/1985` |
| **Anexo XI** | **`10.xxx.xx`** | **Materiais de Construção e Congêneres** | Caps. 25 (cal/argamassa), 32 (tintas/vernizes Internos), 39 (tubos/conexões PVC, caixas d'água, pisos vinílicos), 68 (telhas/mármores), 69 (pisos cerâmicos/porcelanatos/pias), 70 (vidros planos), 73 (vergalhões/estruturas metálicas), 83 (fechaduras/dobradiças) | Protocolos ICMS `196/2009`, `32/2009` e `85/2011` |
| **Anexo XII** | **`11.xxx.xx`** | **Materiais de Limpeza** | Posições `2828` (água sanitária/hipoclorito), `3401` e `3402` (detergentes, sabões em pó/líquidos, amaciantes), `3405` (ceras/polidores), `3808.94` (desinfetantes) | Protocolos ICMS `197/2009` e `33/2009` |
| **Anexo XIII** | **`12.xxx.xx`** | **Materiais Elétricos** | Posições `8504` (transformadores), `8535` e `8536` (disjuntores, interruptores, tomadas, relés, fusíveis), `8537` (quadros/painéis), `8538`, `8544` (fios e cabos elétricos), `8546` e `8547` | Protocolos ICMS `198/2009` e `34/2009` |
| **Anexo XIV** | **`13.xxx.xx`** | **Medicamentos de Uso Humano e Outros Produtos Farmacêuticos** | Posições `3002` (soros/vacinas), `3003` e `3004` (medicamentos de referência, genéricos e similares — Listas Positiva, Negativa e Neutra CMED), `3005` (curativos/gaze), `3006` (contraceptivos) | Convênio ICMS `234/2017` |
| **Anexo XV** | **`14.xxx.xx`** | **Papéis, Plásticos, Produtos Cerâmicos e Vidros** | Posições `3923` e `3924` (copos/pratos descartáveis, sacos de lixo), `4818` (guardanapos), `6911`/`6912` (louças de mesa) e `7013` (copos/taças de vidro) | Protocolos ICMS `199/2009` e `189/2009` |
| *(Revogado)* | *`15.xxx.xx`* | *Plásticos (Unificado no Anexo XV)* | — | — |
| **Anexo XVI** | **`16.xxx.xx`** | **Pneumáticos, Câmaras de Ar e Protetores de Borracha** | Posições `4011` (pneus novos de borracha para automóveis, caminhões, ônibus, motos, bicicletas e máquinas), `4012` (pneus recauchutados) e `4013` (câmaras de ar) | Convênio ICMS `102/2017` e Protocolo ICMS `41/2008` |
| **Anexo XVII** | **`17.xxx.xx`** | **Produtos Alimentícios** | Caps. 04 (laticínios/queijos/manteiga), 09 (café/chá/mate), 15 (óleos vegetais/margarina), 16 (embutidos/conservas de carne), 17 (açúcar/confeitos), 18 (chocolates/achocolatados), 19 (massas/biscoitos/pães), 20 (molhos/sucos/conservas vegetais), 21 (sorvetes/temperos/caldos) | Protocolos ICMS `188/2009`, `28/2009` e `95/2009` |
| *(Revogado)* | *`18.xxx.xx`* | *Produtos Cerâmicos (Unificado no Anexo XV)* | — | — |
| **Anexo XVIII** | **`19.xxx.xx`** | **Produtos de Papelaria** | Caps. 32 (tintas escolares), 39, 48 (cadernos, papel sulfite A4, envelopes, agendas), 96 (canetas esferográficas, marcadores, lápis, borrachas) | Protocolos ICMS `199/2009` e `40/2009` |
| **Anexo XIX** | **`20.xxx.xx`** | **Produtos de Perfumaria e de Higiene Pessoal e Cosméticos** | Posições `3303` (perfumes e águas-de-colônia), `3304` (maquiagem, protetores solares, cremes de beleza), `3305` (xampus, condicionadores, tinturas capilares), `3306` (cremes dentais, fio dental), `3307` (desodorantes, depilatórios), `3401` (sabonetes), `9619` (absorventes e fraldas descartáveis) | Protocolos ICMS `191/2009`, `36/2009` e `104/2012` |
| **Anexo XX** | **`21.xxx.xx`** | **Produtos Eletrônicos, Eletroeletrônicos e Eletrodomésticos** | Posições `7321` (fogões), `8414` (ventiladores/exaustores), `8415` (ar-condicionado), `8418` (refrigeradores/freezers), `8422`/`8450` (lava-louças/lavadoras de roupa), `8471` (computadores/notebooks/impressoras), `8508`/`8509` (aspiradores/liquidificadores), `8516` (fornos micro-ondas/ferros/chuveiros), `8517` (telefones celulares/smartphones), `8528` (televisores/monitores) | Protocolos ICMS `192/2009`, `31/2009` e `88/2009` |
| **Anexo XXI** | **`22.xxx.xx`** | **Rações para Animais Domésticos (Pet)** | Posição `2309` (preparações dos tipos utilizados na alimentação de cães, gatos e outros animais domésticos) | Protocolo ICMS `26/2004` |
| **Anexo XXII** | **`23.xxx.xx`** | **Sorvetes e Preparados para Fabricação de Sorvetes em Máquinas** | Posições `2105.00` (sorvetes e picolés de qualquer espécie), `1806`, `1901` e `2106` (preparados para fabricação de sorvete em máquina) | Protocolo ICMS `20/2005` |
| **Anexo XXIII** | **`24.xxx.xx`** | **Tintas e Vernizes** | Posições `3208`, `3209` e `3210` (tintas e vernizes à base de polímeros sintéticos, acrílicos ou vinílicos), `3214` (mástiques/massas corridas), `3814` (solventes e aguarrás) | Convênio ICMS `118/2017` |
| **Anexo XXIV** | **`25.xxx.xx`** | **Veículos Automotores Novos (Quatro Rodas)** | Posições `8702`, `8703`, `8704` e `8706` (automóveis de passageiros, camionetas, SUVs, furgões e caminhões leves até 5 toneladas) | Convênio ICMS `199/2017` e Convênio ICMS `51/2000` |
| **Anexo XXV** | **`26.xxx.xx`** | **Veículos de Duas e Três Rodas Motorizados (Motocicletas)** | Posição `8711` (motocicletas, motonetas, ciclomotores e triciclos motorizados novos) | Convênio ICMS `200/2017` |
| *(Revogado)* | *`27.xxx.xx`* | *Vidros (Unificado no Anexo XV)* | — | — |
| **Anexo XXVI** | **`28.xxx.xx`** | **Venda de Mercadorias pelo Sistema Porta a Porta (*Door-to-Door* / Marketing Direto)** | Todas as mercadorias comercializadas por empresas de venda direta (revendedores autônomos / catálogos) | Convênio ICMS `45/1999` |
| **Anexo XXVII** | — | **Bens e Mercadorias Sujeitos aos Regimes de ST por Escala Industrial Não Relevante** | Lista de segmentos em que a dispensa de ST para bens fabricados em escala industrial não relevante (optantes do Simples com receita bruta até R$ 180 mil) **não** se aplica. | Cláusula vigésima segunda do Convênio ICMS `142/2018` |"""
    },
    {
        "caminho": "estaduais/confaz/protocolos-icms/mapa-protocolos-st-por-segmento-e-uf.md",
        "titulo": "Mapa Nacional de Adesão e Desoneração (Exclusão) da Substituição Tributária (ICMS-ST) por Segmento e por Estado",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ / Secretarias de Fazenda Estaduais",
        "tipo": "Consolidação de Protocolos ICMS-ST",
        "numero": "MAPA-ST-27UFS",
        "ano": "2026",
        "data": "2026-10-26",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2018/CV142_18",
        "ementa": "Mapeia a vigência territorial do regime de Substituição Tributária (ICMS-ST) nos 26 segmentos do Convênio ICMS 142/2018 e as exclusões setoriais promovidas por Estados como SC, RS, PR e SP pós-Tema 201 do STF.",
        "corpo": """# Mapa Nacional de Adesão e Desoneração (Exclusão) da Substituição Tributária (ICMS-ST) por Segmento e por Estado

Em razão do julgamento do **Tema 201 da Repercussão Geral pelo STF (RE 593.849)** — que obrigou os Estados a restituírem o ICMS-ST pago a maior quando a venda efetiva ao consumidor ocorre abaixo da MVA presumida —, diversos Estados (notadamente **Santa Catarina, Rio Grande do Sul, Paraná e Espírito Santo**) promoveram nos últimos anos a **exclusão (revogação) de múltiplos segmentos da Substituição Tributária**, retornando-os ao regime normal de apuração débito $\times$ crédito.

---

## 1. Segmentos com Adesão Nacional Unânime ou Quase Unânime (27 UFs)

Os seguintes segmentos possuem **Convênios ICMS Nacionais** ou Protocolos de amplitude nacional em praticamente todas as 27 Unidades da Federação:
1. **Combustíveis e Lubrificantes (`CEST 06`):** Regime Monofásico Nacional uniforme em todas as **27 UFs** para gasolina, etanol anidro, diesel, biodiesel e GLP (`LC 192/2022`, `Convênios ICMS 199/2022 e 15/2023`), e ICMS-ST em todas as **27 UFs** para etanol hidratado (EHC), querosene de aviação (QAV) e óleos lubrificantes (`Convênio ICMS 110/2007`);
2. **Cervejas, Chopes, Refrigerantes, Águas Minerais e Gelo (`CEST 03`):** Protocolo ICMS `11/1991` e protocolos correlatos vigentes nas **27 UFs** (utilizando primordialmente pauta de PMPF);
3. **Cigarros e Derivados do Fumo (`CEST 04`):** Convênio ICMS `111/2017` vigente nas **27 UFs**;
4. **Veículos Automotores Novos de 4 Rodas (`CEST 25`) e de 2/3 Rodas (`CEST 26`):** Convênios ICMS `199/2017`, `200/2017` e `51/2000` vigentes nas **27 UFs**;
5. **Tintas e Vernizes (`CEST 24`):** Convênio ICMS `118/2017` vigente na quase totalidade das UFs (**exceto SC**, que excluiu tintas e vernizes da ST);
6. **Pneumáticos e Câmaras de Ar (`CEST 16`):** Convênio ICMS `102/2017` amplamente adotado (**exceto SC**, que revogou a ST sobre pneumáticos de uso geral);
7. **Venda Porta a Porta (`CEST 28`):** Convênio ICMS `45/1999` vigente nacionalmente.

---

## 2. Mapa das Principais Exclusões Estaduais da Substituição Tributária (Regras Críticas para LLMs)

| Estado (UF) | Segmentos que PERMANECEM no ICMS-ST na UF | Segmentos EXCLUÍDOS (Retornaram ao Regime Normal Débito x Crédito na UF) |
| :---: | :--- | :--- |
| **Santa Catarina (`SC`)** | Combustíveis (`06`), Cervejas/Refrigerantes/Águas (`03`), Cigarros/Fumo (`04`), Cimentos (`05`), Energia Elétrica (`07`), Rações Pet (`22`), Sorvetes (`23`), Veículos Novos 4 Rodas (`25`) e Motocicletas (`26`), Porta a Porta (`28`). | **SC revogou a ST da maioria dos setores industriais/varejistas:** Autopeças (`01`), Bebidas Quentes/Vinhos (`02`), Ferramentas (`08`), Lâmpadas (`09`), Materiais de Construção (`10`), Materiais de Limpeza (`11`), Materiais Elétricos (`12`), Medicamentos/Farmacêuticos (`13`), Papéis/Plásticos (`14`), Pneumáticos (`16`), Produtos Alimentícios (`17`), Papelaria (`19`), Perfumaria/Cosméticos/Higiene (`20`), Eletrônicos/Eletrodomésticos (`21`) e Tintas/Vernizes (`24`). *(Nas remessas de outras UFs para SC desses itens excluídos, **NÃO se destaca ICMS-ST**, aplicando-se apenas o ICMS próprio de 12%, 7% ou 4%)*. |
| **Rio Grande do Sul (`RS`)** | Autopeças (`01`), Bebidas Alcoólicas (`02`), Bebidas Frias (`03`), Cigarros (`04`), Cimentos (`05`), Combustíveis (`06`), Medicamentos (`13`), Pneumáticos (`16`), Perfumaria/Higiene (`20` parcial), Rações Pet (`22`), Sorvetes (`23`), Tintas (`24`), Veículos (`25` e `26`). | **RS excluiu da ST diversos itens de:** Vinhos e Espumantes (`02` parcial), Ferramentas (`08` parcial), Lâmpadas (`09`), Materiais de Construção (`10` parcial), Materiais Elétricos (`12` parcial), Produtos Alimentícios (`17` parcial: carnes, laticínios, massas, águas) e Papelaria (`19`). |
| **Paraná (`PR`)** | Autopeças (`01`), Bebidas Frias (`03`), Cigarros (`04`), Cimentos (`05`), Combustíveis (`06`), Materiais de Construção (`10`), Materiais de Limpeza (`11`), Materiais Elétricos (`12`), Medicamentos (`13`), Pneumáticos (`16`), Alimentos (`17` parcial), Perfumaria/Cosméticos (`20`), Eletrônicos (`21`), Rações Pet (`22`), Tintas (`24`), Veículos (`25` e `26`). | **PR excluiu da ST:** Vinhos (`02` parcial), Água mineral em embalagens retornáveis específicas, diversos itens de Produtos Alimentícios (`17`), Papelaria (`19`) e Ferramentas específicas. |
| **São Paulo (`SP`)** | Mantém ampla cobertura nos Anexos da Portaria CAT 68/2019: Autopeças (`01`), Bebidas (`02` e `03`), Fumo (`04`), Cimentos (`05`), Combustíveis (`06`), Ferramentas (`08`), Lâmpadas (`09`), Construção (`10`), Limpeza (`11`), Elétricos (`12`), Medicamentos (`13`), Papéis/Plásticos (`14`), Pneus (`16`), Alimentos (`17`), Papelaria (`19`), Perfumaria/Higiene (`20`), Eletrônicos (`21`), Rações Pet (`22`), Sorvetes (`23`), Tintas (`24`), Veículos (`25` e `26`). | **SP suspendeu/excluiu pontualmente:** Vinhos nacionais (`02` — Portaria CAT 68/2019), diversos subitens de produtos alimentícios e bebidas quentes em acordos bilaterais denunciados. |
| **Minas Gerais (`MG`) e Rio de Janeiro (`RJ`)** | Mantêm cobertura abrangente na quase totalidade dos 26 segmentos do Convênio ICMS 142/2018 (Anexo VII do RICMS/MG 2023 e Livro II do RICMS/RJ). | Exclusões pontuais de subitens alimentícios regionais e bebidas artesanais em operações internas. |
| **Norte, Nordeste e Centro-Oeste** | Adotam **Substituição Tributária + Antecipação Tributária de Fronteira (Parcial ou Total)** na entrada interestadual. | Mesmo quando um produto não está em Protocolo de ICMS-ST, Estados como `BA`, `PE`, `CE`, `MA`, `PB`, `RN`, `AL`, `SE`, `PI`, `PA`, `AM`, `RO`, `TO`, `AC`, `AP` e `RR` exigem a **Antecipação Parcial (sem encerramento)** ou **Antecipação Total (com encerramento)** na barreira fiscal de entrada. |"""
    },

    # =========================================================================
    # CAMADA 2: BENEFÍCIOS FISCAIS E REGIMES ESPECIAIS ESTADUAIS (TTD, COMPETE, TTS, PROGOIÁS, PRODEPE, ZFM)
    # =========================================================================
    {
        "caminho": "estaduais/sc/ricms/lei-17763-2019-ttd-409-410-478-sc.md",
        "titulo": "Lei Estadual nº 17.763, de 12 de agosto de 2019 e Anexo 2 do RICMS/SC (Regimes Especiais TTD 409, TTD 410, TTD 411 de Importação e TTD 478 de E-Commerce em Santa Catarina)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado de Santa Catarina / SEF-SC",
        "tipo": "Lei Estadual",
        "numero": "17763",
        "ano": "2019",
        "data": "2019-08-12",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br;santa.catarina:estadual:lei:2019-08-12;17763",
        "ementa": "Reinstitui benefícios fiscais referentes ao ICMS no Estado de Santa Catarina nos termos da Lei Complementar Federal nº 160/2017 e do Convênio ICMS 190/2017, disciplinando os Tratamentos Tributários Diferenciados de Importação (TTD 409, 410 e 411) e de Comércio Eletrônico (TTD 478).",
        "corpo": """# Lei Estadual nº 17.763, de 12 de agosto de 2019 e Anexo 2 do RICMS/SC (Regimes Especiais TTD 409, TTD 410, TTD 411 de Importação e TTD 478 de E-Commerce em Santa Catarina)

LEI Nº 17.763, DE 12 DE AGOSTO DE 2019 — CONSOLIDAÇÃO DOS TRATAMENTOS TRIBUTÁRIOS DIFERENCIADOS DE SANTA CATARINA (TTDs)

## 1. TTD 409, TTD 410 e TTD 411 — Importação por Portos e Aeroportos Catarinenses (Art. 246 do Anexo 2 do RICMS/SC)

Os Tratamentos Tributários Diferenciados **TTD 409**, **TTD 410** e **TTD 411** aplicam-se à importação de mercadorias para comercialização realizada por intermédio dos portos, aeroportos ou pontos de fronteira alfandegados situados no Estado de Santa Catarina (Itajaí, Navegantes, São Francisco do Sul, Itapoá, Imbituba, Florianópolis, Joinville, Dionísio Cerqueira):

### Sistemática Operacional e Cargas Tributárias Efetivas nas Saídas Interestaduais (Alíquota Destacada de 4% — Res. SF 13/2012)
1. **Diferimento no Desembaraço Aduaneiro:** Diferimento total do ICMS devido por ocasião do desembaraço aduaneiro da mercadoria importada para o momento da saída subsequente promovida pelo importador catarinense.
2. **Crédito Presumido na Saída Subsequente (Destaque de 4% na NF-e Interestadual com Direito Integral a Crédito pelo Destinatário em Outra UF):**
   - **TTD 409 (Regime Inicial / 1º ao 36º mês):**
     - Nos primeiros 36 meses de vigência do regime especial (exigindo garantia administrativa): crédito presumido que resulta em recolhimento efetivo de **2,6% (dois inteiros e seis décimos por cento)** nos primeiros 6 meses, reduzindo-se para **1,0% (um por cento)** sobre a base de cálculo da saída interestadual tributada a 4% após cumpridos os marcos temporais.
   - **TTD 410 (Sem Garantia após 36 meses de TTD 409):** Carga efetiva de **1,0%** nas saídas interestaduais a 4% com dispensa de garantia real/fidejussória.
   - **TTD 411 (Com Garantia Permanente):** Carga efetiva de **1,0%** desde o início mediante prestação de garantia.
3. **Encargos de Fundos Estaduais Obrigatórios (0,4% sobre a Base Integral):**
   - Cumulativamente ao recolhimento efetivo de ICMS, o beneficiário deve recolher **0,4% (quatro décimos por cento)** sobre a base de cálculo integral da saída (destinados ao **FUMDES** — Fundo de Apoio à Manutenção e ao Desenvolvimento da Educação Superior — e ao **Fundo Social / FIA / FEI**), perfazendo desembolso total efetivo de **1,4%** (no regime de 1,0% + 0,4%) ou **3,0%** (no regime inicial de 2,6% + 0,4%).

---

## 2. TTD 478 — Comércio Eletrônico / Vendas Não Presenciais (*E-Commerce* e Telemarketing — Art. 21-A do Anexo 2 do RICMS/SC)

Aplicável às operações de saída interestadual realizadas por estabelecimento comercial varejista catarinense (e-commerce / marketplace / telemarketing) destinadas a consumidor final (contribuinte ou não contribuinte) localizado em outra unidade da Federação:
- **Saídas Interestaduais a 4% (Importados):** Crédito presumido de modo a resultar em carga tributária efetiva de **1,0%**;
- **Saídas Interestaduais a 7% ou 12% (Nacionais):** Crédito presumido de modo a resultar em carga tributária efetiva de **2,0%**, com vedação ao aproveitamento dos créditos das entradas correspondentes (mantendo-se inteiramente devido o **DIFAL Não Contribuinte da EC 87/2015 e LC 190/2022** em favor da UF de destino)."""
    },
    {
        "caminho": "estaduais/es/ricms/lei-10568-2016-compete-es-invest-es.md",
        "titulo": "Lei Estadual nº 10.568, de 26 de julho de 2016 (Programa COMPETE-ES Atacadista e E-Commerce, INVEST-ES e FUNDAP no Espírito Santo)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado do Espírito Santo / SEFAZ-ES",
        "tipo": "Lei Estadual",
        "numero": "10568",
        "ano": "2016",
        "data": "2016-07-26",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br;espirito.santo:estadual:lei:2016-07-26;10568",
        "ementa": "Institui o Programa de Desenvolvimento e Proteção à Economia do Estado do Espírito Santo (COMPETE-ES) e consolida os incentivos fiscais para o comércio atacadista (carga de 1,1% nas saídas interestaduais a 12%), comércio eletrônico não presencial (COMPETE Venda Não Presencial) e indústria (INVEST-ES).",
        "corpo": """# Lei Estadual nº 10.568, de 26 de julho de 2016 (Programa COMPETE-ES Atacadista e E-Commerce, INVEST-ES e FUNDAP no Espírito Santo)

LEI Nº 10.568, DE 26 DE JULHO DE 2016 — PROGRAMA COMPETE-ES, INVEST-ES E FUNDAP (CONVALIDADOS PELA LC Nº 160/2017 E CONVÊNIO ICMS Nº 190/2017)

## 1. A Vantagem Geográfico-Tributária Estrutural do Espírito Santo (Resolução SF nº 22/1989)

O Estado do Espírito Santo possui uma posição singular na matriz interestadual brasileira:
- **Na Entrada Interestadual oriunda do Sul e Sudeste (`SP`, `RJ`, `MG`, `PR`, `SC`, `RS`):** A mercadoria nacional ingressa no Espírito Santo com alíquota interestadual de **`7%`**;
- **Na Saída Interestadual do Espírito Santo para QUALQUER Estado (inclusive de volta para `SP`, `RJ`, `MG`, `PR`, `SC` e `RS`):** O contribuinte capixaba destaca na NF-e a alíquota interestadual de **`12%`** (exceto `4%` para importados com conteúdo de importação > 40%), gerando **crédito integral de 12%** para o cliente adquirente localizado no Sul/Sudeste.

---

## 2. COMPETE-ES Atacadista (Art. 16 da Lei nº 10.568/2016 e Art. 530-L-R-K do RICMS/ES)

Aplicável às operações interestaduais realizadas por estabelecimentos comerciais atacadistas aderentes ao Contrato de Competitividade (COMPETE Atacadista):
- **Estorno de Débito / Crédito Presumido nas Saídas Interestaduais:** O contribuinte estorna todos os créditos de entrada e aplica crédito presumido sobre o débito das saídas interestaduais de mercadorias destinadas a contribuintes (Pessoa Jurídica), resultando em **carga tributária efetiva final de `1,10%` (um inteiro e dez centésimos por cento)** sobre o valor das saídas interestaduais tributadas a **12%** (e de **1,10%** ou percentual específico nas saídas a **4%**).
- **Destaque na NF-e para o Cliente em Outra UF:** A Nota Fiscal Eletrônica é emitida com destaque normal de **12%** (ou **4%** se importado), assegurando ao destinatário contribuinte em qualquer UF o aproveitamento integral do crédito de 12% ou 4% por se tratar de benefício fiscal devidamente registrado, depositado e convalidado no CONFAZ (LC 160/2017 e Convênio ICMS 190/2017).

---

## 3. COMPETE-ES Venda Não Presencial (*E-Commerce* e Telemarketing — Art. 23 da Lei nº 10.568/2016)

Aplicável às operações interestaduais que destinem mercadorias a consumidor final (pessoa física ou jurídica não contribuinte) realizadas por meio de internet (e-commerce / marketplace) ou central de telemarketing:
- **Carga Tributária Efetiva na Origem (ES):** Crédito presumido de modo que a carga tributária efetiva devida ao Estado do Espírito Santo seja de **`1,10%`** (nas saídas com alíquota interestadual de 12% ou 4%).
- **DIFAL de Destino (EC 87/2015 e LC 190/2022):** Como a alíquota interestadual de saída do Espírito Santo para qualquer UF é de **12%** (para produtos nacionais), o DIFAL Não Contribuinte devido à UF de destino é calculado deduzindo-se **12%** da alíquota interna da UF de destino (ex.: venda para consumidor final em SP cuja alíquota interna é 18% $\rightarrow$ DIFAL para SP de apenas $18\% - 12\% = 6\%$, somado a $1,10\%$ no ES = carga total de ICMS de $7,10\%$, contra $18\%$ em uma operação interna em SP)."""
    },
    {
        "caminho": "estaduais/mg/ricms/decreto-48589-2023-tts-corredor-importacao-ecommerce-mg.md",
        "titulo": "Tratamentos Tributários Setoriais de Minas Gerais — TTS Corredor de Importação, TTS E-Commerce e TTS Atacadista (RICMS/MG e Lei nº 6.763/1975)",
        "esfera": "Estadual",
        "orgao": "Governo do Estado de Minas Gerais / Secretaria de Estado de Fazenda (SEF/MG)",
        "tipo": "Regime Especial Estadual",
        "numero": "TTS-MG",
        "ano": "2023",
        "data": "2023-03-22",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br;minas.gerais:estadual:decreto:2023-03-03;48589",
        "ementa": "Disciplina os Tratamentos Tributários Setoriais (TTS) automatizados e padronizados da Secretaria de Estado de Fazenda de Minas Gerais (SEF/MG) para o Corredor de Importação, Comércio Eletrônico (E-Commerce) e Atacadistas/Centrais de Distribuição.",
        "corpo": """# Tratamentos Tributários Setoriais de Minas Gerais — TTS Corredor de Importação, TTS E-Commerce e TTS Atacadista (RICMS/MG e Lei nº 6.763/1975)

REGIMES ESPECIAIS PADRONIZADOS (TTS / e-PTA SEF/MG) — DECRETO Nº 48.589/2023 E LEI Nº 6.763/1975

## 1. TTS Corredor de Importação de Minas Gerais (Importação para Comercialização)

Concedido via sistema eletrônico **SIARE / e-PTA** da SEF/MG para empresas importadoras estabelecidas em Minas Gerais:
1. **Diferimento Total do ICMS na Importação:** Diferimento de 100% do ICMS devido no desembaraço aduaneiro de mercadorias importadas diretamente do exterior para comercialização (desde que sem similar concorrencial listado como vedado pela SEF/MG e desembaraçadas em portos secos/aeroportos mineiros ou portos marítimos autorizados por regime especial).
2. **Crédito Presumido nas Saídas Subsequentes:**
   - **Nas saídas interestaduais sujeitas à alíquota de 4% (Resolução SF nº 13/2012):** Crédito presumido de modo que a carga tributária efetiva recolhida a Minas Gerais resulte em **1,5% (um inteiro e cinco décimos por cento)** ou **2,5%** (quando desembaraçado fora do Estado sem recinto mineiro);
   - **Nas saídas internas e interestaduais de mercadorias sem similar nacional (7% ou 12% ou 18%):** Carga efetiva entre **3,0% e 6,0%** conforme a alíquota aplicável, com vedação ao aproveitamento de quaisquer outros créditos sobre a operação.

---

## 2. TTS E-Commerce de Minas Gerais (Vendas Não Presenciais pela Internet ou Telemarketing)

Modalidade de Regime Especial para centros de distribuição e varejistas de comércio eletrônico estabelecidos em Minas Gerais:
1. **Modalidade Não Vinculada (Varejista Puro de E-Commerce):**
   - Crédito presumido de ICMS nas saídas destinadas a consumidor final (interno ou interestadual), resultando em **recolhimento efetivo de 1,3% a 2,0%** sobre o faturamento das vendas interestaduais (mantida a obrigação de recolhimento do DIFAL EC 87/2015 para a UF de destino nas vendas a não contribuintes).
2. **Modalidade Vinculada (Centro de Distribuição Atacadista + Varejista E-Commerce):**
   - Permite a transferência de mercadorias do CD Atacadista para a filial E-Commerce com diferimento do ICMS e dispensa o recolhimento antecipado do ICMS-ST na entrada da mercadoria no CD Atacadista mineiro, transferindo a responsabilidade de retenção apenas para as saídas internas destinadas a varejistas tradicionais."""
    },
    {
        "caminho": "estaduais/go/ricms/lei-20787-2020-progoias-atacadista-fundeinfra.md",
        "titulo": "Lei Estadual nº 20.787, de 3 de junho de 2020 (Programa PROGOIÁS, Crédito Outorgado Atacadista de Goiás e FUNDEINFRA)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado de Goiás / Secretaria de Estado da Economia",
        "tipo": "Lei Estadual",
        "numero": "20787",
        "ano": "2020",
        "data": "2020-06-03",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br;goias:estadual:lei:2020-06-03;20787",
        "ementa": "Institui o Programa de Desenvolvimento Regional - PROGOIÁS para estabelecimentos industriais (crédito outorgado de 64% a 67% sobre o saldo devedor de ICMS), consolidado com o Crédito Outorgado Atacadista de 3% nas saídas interestaduais e a contribuição ao PROTEGE e ao FUNDEINFRA.",
        "corpo": """# Lei Estadual nº 20.787, de 3 de junho de 2020 (Programa PROGOIÁS, Crédito Outorgado Atacadista de Goiás e FUNDEINFRA)

LEI Nº 20.787, DE 3 DE JUNHO DE 2020 — PROGRAMA PROGOIÁS E REGIMES DE COMPETITIVIDADE DE GOIÁS

## 1. Programa PROGOIÁS (Incentivo Industrial — Sucedâneo do FOMENTAR e PRODUZIR)

O **PROGOIÁS** concede aos estabelecimentos industriais localizados no Estado de Goiás **crédito outorgado de ICMS** aplicado diretamente sobre o saldo devedor mensal decorrente das operações com produtos de fabricação própria:
- **Percentuais do Crédito Outorgado sobre o Saldo Devedor:**
  - **64%** no 1º ano de fruição;
  - **65%** no 2º ano;
  - **66%** no 3º ano (e de forma permanente para empresas em municípios prioritários até **67%**).
- **Diferimento na Aquisição:** Diferimento do ICMS no desembaraço aduaneiro de matérias-primas, insumos e bens para o ativo imobilizado importados do exterior e dispensa do DIFAL na aquisição interestadual de máquinas e equipamentos industriais.
- **Condição Financeira (PROTEGE GOIÁS):** Contribuição ao Fundo de Proteção Social do Estado de Goiás (PROTEGE) em percentual regressivo de **10% a 6%** calculado sobre o valor do crédito outorgado efetivamente utilizado.

---

## 2. Regime Especial para o Comércio Atacadista e Distribuidor em Goiás (Anexo IX, Art. 11, III do RCTE/GO)

- **Crédito Outorgado de 3% nas Saídas Interestaduais:** Concede ao estabelecimento atacadista ou distribuidor goiano crédito outorgado equivalente a **3% (três por cento)** do valor da base de cálculo nas saídas interestaduais de mercadorias destinadas à comercialização, produção ou industrialização, cuja alíquota interestadual seja de **12%** (reduzindo o débito próprio de saída de 12% para **9%**, mantendo o aproveitamento dos créditos de entrada limitados a 7% ou 12% e exigindo contribuição ao PROTEGE GOIÁS sobre o benefício).

---

## 3. FUNDEINFRA (Contribuição sobre Produtos do Agronegócio e Mineração — Lei nº 21.670/2022)

- Institui contribuição de até **1,65%** destinada ao **Fundo Estadual de Infraestrutura (FUNDEINFRA)** como condição facultativa para que o produtor ou exportador usufrua de **diferimento do ICMS nas operações internas** ou de **regime especial de controle de exportação** sobre soja, milho, cana-de-açúcar, carne bovina e minérios."""
    },
    {
        "caminho": "estaduais/pe/ricms/lei-11675-1999-prodepe-pe.md",
        "titulo": "Lei Estadual nº 11.675, de 11 de outubro de 1999 (Programa de Desenvolvimento do Estado de Pernambuco - PRODEPE)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado de Pernambuco / SEFAZ-PE",
        "tipo": "Lei Estadual",
        "numero": "11675",
        "ano": "1999",
        "data": "1999-10-11",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br;pernambuco:estadual:lei:1999-10-11;11675",
        "ementa": "Consolida e altera o Programa de Desenvolvimento do Estado de Pernambuco - PRODEPE, concedendo crédito presumido de ICMS de 75% a 95% para indústrias, centrais de distribuição (CD) e comércio importador atacadista de portos e aeroportos pernambucanos.",
        "corpo": """# Lei Estadual nº 11.675, de 11 de outubro de 1999 (Programa de Desenvolvimento do Estado de Pernambuco - PRODEPE)

LEI Nº 11.675, DE 11 DE OUTUBRO DE 1999 — PROGRAMA DE DESENVOLVIMENTO DO ESTADO DE PERNAMBUCO (PRODEPE)

## 1. Estímulos Industriais do PRODEPE (Agrupamentos Industriais Prioritários e Relevantes)

Concede **crédito presumido de ICMS** sobre o saldo devedor mensal da apuração normal das indústrias incentivadas em Pernambuco:
- **Região Metropolitana do Recife (RMR):** Crédito presumido de **75% (setenta e cinco por cento)** para agrupamentos prioritários (ou 47,5% a 75% para relevantes);
- **Mesorregiões da Mata, Agreste e Sertão Pernambucano:** Crédito presumido de **85% a 95%** sobre o saldo devedor mensal de ICMS para empreendimentos industriais instalados no interior do Estado.

---

## 2. Central de Distribuição (CD — PRODEPE Logístico Interestadual)

Destinado a centrais de distribuição que promovam entradas e saídas interestaduais de mercadorias industrializadas:
- **Nas Saídas Interestaduais:** Crédito presumido equivalente a **3% (três por cento)** do valor total das saídas interestaduais tributadas a 12%;
- **Nas Entradas por Transferência ou Compra Interestadual oriundas de fora da Região Nordeste:** Crédito presumido equivalente a **3% (três por cento)** sobre a base de cálculo da entrada (limitado ao valor do frete).

---

## 3. Comércio Importador Atacadista de Portos e Aeroportos (Suape / Recife)

- **Diferimento no Desembaraço Aduaneiro** de mercadorias importadas do exterior para comercialização; e
- **Crédito Presumido na Saída Subsequente:** Limitado a percentual que resulte em recolhimento mínimo de **3,5% a 5,0%** nas operações internas e **1,0% a 2,0%** nas saídas interestaduais sujeitas à alíquota de 4% (Resolução SF 13/2012), sujeito à taxa de administração do **FEEF/PE e AD DIPER**."""
    },
    {
        "caminho": "estaduais/ba/ricms/decreto-7799-2000-atacadista-desenvolve-ba.md",
        "titulo": "Decreto Estadual nº 7.799, de 9 de maio de 2000 e Lei nº 7.980/2001 (Regime Especial de Atacadista e Programa DESENVOLVE na Bahia)",
        "esfera": "Estadual",
        "orgao": "Governo do Estado da Bahia / Secretaria da Fazenda (SEFAZ/BA)",
        "tipo": "Decreto Estadual",
        "numero": "7799",
        "ano": "2000",
        "data": "2000-05-09",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br;bahia:estadual:decreto:2000-05-09;7799",
        "ementa": "Institui tratamento tributário especial de redução de base de cálculo nas operações internas e interestaduais realizadas por contribuintes inscritos como comércio atacadista na Bahia, em conjunto com o Programa DESENVOLVE (Lei nº 7.980/2001).",
        "corpo": """# Decreto Estadual nº 7.799, de 9 de maio de 2000 e Lei nº 7.980/2001 (Regime Especial de Atacadista e Programa DESENVOLVE na Bahia)

DECRETO Nº 7.799, DE 9 DE MAIO DE 2000 — TRATAMENTO TRIBUTÁRIO DO COMÉRCIO ATACADISTA E CENTRAIS DE DISTRIBUIÇÃO NA BAHIA

## 1. Redução de Base de Cálculo nas Saídas Internas de Atacadistas para Contribuintes (Art. 1º e 2º do Decreto nº 7.799/2000)

Nas operações internas de saída de mercadorias realizadas por estabelecimentos comerciais atacadistas inscritos no CAD-ICMS da Bahia sob os CNAEs listados no Decreto nº 7.799/2000 e destinadas a contribuintes inscritos (varejistas/indústrias):
- **Redução da Base de Cálculo do ICMS em `41,176%` (ou percentual ajustado à alíquota modal de 20,5%):** De forma que a **carga tributária incidente na operação interna B2B resulte em `10%` (dez por cento)** ou **`12%` (doze por cento)**, evitando o acúmulo de créditos e reduzindo o impacto da Antecipação Parcial de fronteira;
- **Limitação (Trava) de Créditos nas Entradas Interestaduais (Art. 6º):** Fica vedada a utilização de créditos fiscais excedentes a **10%** (ou **12%**) nas aquisições interestaduais vinculadas às saídas beneficiadas pela redução de base de cálculo.

---

## 2. Programa DESENVOLVE (Incentivo Industrial da Bahia — Lei nº 7.980/2001)

- Concede aos projetos industriais e agroindustriais aprovados pelo Conselho Deliberativo do DESENVOLVE a **dilação de prazo de até 72 (setenta e dois) meses** sobre **70% a 90%** do saldo devedor mensal de ICMS gerado, com **desconto de até 90% (noventa por cento)** dos encargos financeiros na liquidação antecipada de cada parcela (equivalendo na prática a uma redução de até **81%** do ICMS devido), além do diferimento do ICMS na importação e na aquisição interestadual de bens do ativo imobilizado e matérias-primas."""
    },
    {
        "caminho": "estaduais/ce/ricms/lei-14237-2008-carga-liquida-fdi-ce.md",
        "titulo": "Lei Estadual nº 14.237, de 10 de novembro de 2008 e Lei nº 10.367/1979 (Regime de Substituição Tributária por Carga Líquida por CNAE e FDI no Ceará)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado do Ceará / SEFAZ-CE",
        "tipo": "Lei Estadual",
        "numero": "14237",
        "ano": "2008",
        "data": "2008-11-10",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br;ceara:estadual:lei:2008-11-10;14237",
        "ementa": "Dispõe sobre o Regime de Substituição Tributária por Carga Líquida do ICMS nas operações realizadas por contribuintes atacadistas e varejistas enquadrados por CNAE-Fiscal no Estado do Ceará e consolida os incentivos do Fundo de Desenvolvimento Industrial (FDI - PROVIN e PCDM).",
        "corpo": """# Lei Estadual nº 14.237, de 10 de novembro de 2008 e Lei nº 10.367/1979 (Regime de Substituição Tributária por Carga Líquida por CNAE e FDI no Ceará)

LEI Nº 14.237, DE 10 DE NOVEMBRO DE 2008 — SISTEMÁTICA DE SUBSTITUIÇÃO TRIBUTÁRIA POR CARGA LÍQUIDA NO CEARÁ

## 1. Como Funciona a Substituição Tributária por Carga Líquida por CNAE no Ceará

Diferentemente dos demais Estados que aplicam MVA produto por produto (NCM/CEST), o Estado do Ceará instituiu pela **Lei nº 14.237/2008** (regulamentada pelos Decretos estaduais setoriais de atacadistas de alimentos, tecidos/confecções, materiais de construção, autopeças, produtos farmacêuticos, papelaria e informática) o **Regime de Substituição Tributária por Carga Líquida**:
1. **Cobrança na Entrada (Interna, Interestadual ou Importação) com Encerramento de Fase:** O ICMS-ST é calculado aplicando-se diretamente um **percentual de Carga Tributária Líquida prefixado** em função do **CNAE do destinatário cearense** e da **região de origem da mercadoria** (Interna no CE, Norte/Nordeste/Centro-Oeste/ES a 12%, Sul/Sudeste a 7%, ou Importados a 4%) sobre o valor da nota fiscal de entrada acrescido de MVA fixa reduzida;
2. **Saída Interna Subsequente Livre de Cobrança Adicional:** Uma vez recolhida a Carga Líquida na entrada, as saídas internas subsequentes no Ceará ocorrem **sem destaque adicional de ICMS** (tributação encerrada na entrada);
3. **Saídas Interestaduais Promovidas por Atacadista Credenciado no Ceará:** Quando a mercadoria adquirida sob o regime de Carga Líquida é posteriormente vendida para **outro Estado**, o atacadista cearense com Regime Especial de Tributação (RET) fica dispensado ou ressarcido proporcionalmente da parcela interna.

---

## 2. FDI — Fundo de Desenvolvimento Industrial do Ceará (Lei nº 10.367/1979: PROVIN e PCDM)

- **PROVIN (Programa de Incentivo ao Funcionamento de Empresas):** Incentivo industrial de **75% a 99%** sobre o ICMS mensal devido pelas indústrias instaladas no Ceará, com retorno de **1% a 25%** sobre o valor incentivado;
- **PCDM (Programa de Incentivo às Centrais de Distribuição de Mercadorias):** Redução de até **75%** do ICMS incidente nas operações interestaduais de saída realizadas por Centrais de Distribuição (CD) e importadores pelos Portos do Pecém e do Mucuripe."""
    },
    {
        "caminho": "estaduais/am/ricms/lei-2826-2003-incentivos-zfm-pim-am.md",
        "titulo": "Lei Estadual nº 2.826, de 29 de setembro de 2003 (Política Estadual de Incentivos Fiscais da Zona Franca de Manaus / Polo Industrial de Manaus)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado do Amazonas / SEFAZ-AM",
        "tipo": "Lei Estadual",
        "numero": "2826",
        "ano": "2003",
        "data": "2003-09-29",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "IPI", "Imposto de Importação", "PIS", "Cofins"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br;amazonas:estadual:lei:2003-09-29;2826",
        "ementa": "Regulamenta a Política Estadual de Incentivos Fiscais e Extrafiscais nos termos da Constituição do Estado do Amazonas para as indústrias incentivadas do Polo Industrial de Manaus (PIM / ZFM), concedendo crédito estímulo de ICMS de 55% a 100% e diferimento na importação de insumos.",
        "corpo": """# Lei Estadual nº 2.826, de 29 de setembro de 2003 (Política Estadual de Incentivos Fiscais da Zona Franca de Manaus / Polo Industrial de Manaus)

LEI Nº 2.826, DE 29 DE SETEMBRO DE 2003 — INCENTIVOS FISCAIS DE ICMS NA ZONA FRANCA DE MANAUS (PIM)

## 1. Estrutura dos Incentivos Fiscais Estaduais (ICMS) para Indústrias do PIM

As empresas industriais instaladas na **Zona Franca de Manaus (ZFM)** com projetos aprovados pela **SUFRAMA** e pelo **CODAM** (Conselho de Desenvolvimento do Estado do Amazonas), que observem o **Processo Produtivo Básico (PPB)**, fazem jus cumulativamente aos seguintes incentivos estaduais de ICMS:
1. **Diferimento Total do ICMS na Importação de Matérias-Primas e Insumos do Exterior (Art. 14):** Diferimento do lançamento e pagamento do ICMS incidente no desembaraço aduaneiro de matérias-primas, materiais secundários e de embalagem importados do exterior para utilização no processo industrial;
2. **Crédito Fiscal Presumido nas Compras Nacionais (Art. 15 e Art. 49 do Decreto-Lei nº 288/1967):** Nas aquisições interestaduais de matérias-primas, produtos intermediários e bens nacionais amparadas pela isenção do **Convênio ICM nº 65/1988**, a indústria ou comércio amazonense apropria **crédito fiscal presumido de ICMS** igual ao montante que teria sido pago na origem se não houvesse a isenção (**7%** quando oriundo do Sul/Sudeste exceto ES, ou **12%** quando oriundo do N/NE/CO/ES);
3. **Crédito Estímulo sobre o Saldo Devedor de ICMS (Art. 16):** Redução do saldo devedor mensal de ICMS em função da categoria do produto industrializado:
   - **100% (cem por cento)** de crédito estímulo para bens de informática e automação, bens intermediários, componentes eletrônicos, brinquedos, medicamentos fitoterápicos/regionais e agroindústria no interior do Amazonas;
   - **90,25% (noventa inteiros e vinte e cinco centésimos por cento)** para bens de capital, duas rodas (motocicletas e bicicletas), relógios, aparelhos de ar-condicionado e produtos ópticos;
   - **75% (setenta e cinco por cento)** para bens de consumo final eletroeletrônicos (televisores, áudio e vídeo, celulares, fornos de micro-ondas);
   - **55% (cinquenta e cinco por cento)** para concentrados para bebidas não alcoólicas e descartáveis.

---

## 2. Alíquota Interestadual de Saída da ZFM para o Restante do País (12% — Exceção à Regra dos 4%)

- Nos termos do **art. 1º, § 4º, II da Resolução do Senado Federal nº 13/2012**, os bens industrializados na Zona Franca de Manaus em conformidade com o **Processo Produtivo Básico (PPB)** (CST de Origem `4`) **NÃO se submetem à alíquota de 4%**, ainda que possuam Conteúdo de Importação superior a 40%.
- Consequentemente, a saída interestadual da indústria do Polo Industrial de Manaus para **qualquer Estado brasileiro** aplica a alíquota interestadual de **`12%`**, gerando **crédito integral de 12% de ICMS** para o adquirente nas Regiões Sul, Sudeste, Centro-Oeste, Nordeste e Norte (amparado pela blindagem constitucional do art. 40 e art. 92-A do ADCT da CF/88).

---

## 3. Contribuições Financeiras aos Fundos Estaduais do Amazonas (FTI, UEA e FMPES)

Como contrapartida pela fruição do Crédito Estímulo e do diferimento, as indústrias incentivadas recolhem contribuições financeiras destinadas à **UEA** (Universidade do Estado do Amazonas — 1,0% a 1,5% sobre o faturamento bruto), ao **FTI** (Fundo de Fomento ao Turismo, Infraestrutura, Serviços e Interiorização do Desenvolvimento do Amazonas — 1% a 2% sobre importações/faturamento) e ao **FMPES** (Fundo de Fomento às Micro e Pequenas Empresas)."""
    },
    {
        "caminho": "estaduais/to/ricms/lei-1201-2000-atacadista-ecommerce-to.md",
        "titulo": "Lei Estadual nº 1.201, de 29 de dezembro de 2000 e Lei nº 1.385/2003 (Incentivos Fiscais de Comércio Atacadista, Importação e E-Commerce no Tocantins)",
        "esfera": "Estadual",
        "orgao": "Assembleia Legislativa do Estado do Tocantins / SEFAZ-TO",
        "tipo": "Lei Estadual",
        "numero": "1201",
        "ano": "2000",
        "data": "2000-12-29",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS"],
        "fonte": "https://normas.leg.br/?urn=urn:lex:br;tocantins:estadual:lei:2000-12-29;1201",
        "ementa": "Concede crédito fiscal presumido nas operações de saída interestadual e de comércio eletrônico (vendas não presenciais) realizadas por estabelecimentos comerciais atacadistas e centrais de distribuição no Estado do Tocantins.",
        "corpo": """# Lei Estadual nº 1.201, de 29 de dezembro de 2000 e Lei nº 1.385/2003 (Incentivos Fiscais de Comércio Atacadista, Importação e E-Commerce no Tocantins)

LEI Nº 1.201, DE 29 DE DEZEMBRO DE 2000 — TRATAMENTO TRIBUTÁRIO DO COMÉRCIO ATACADISTA E E-COMMERCE NO TOCANTINS

## 1. Operações Interestaduais de Comércio Atacadista e Vendas Não Presenciais (*E-Commerce*)

Aos contribuintes inscritos no Cadastro de Contribuintes do ICMS do Estado do Tocantins (CCI-TO) detentores de Termo de Acordo de Regime Especial (TARE):
1. **Saídas Interestaduais de Mercadorias para Comercialização ou Industrialização (Atacadista B2B):** Crédito fiscal presumido de modo que a carga tributária efetiva resulte em **1,0% a 2,0%** sobre o valor da operação interestadual tributada a **12%** (ou **4%** para importados), com estorno integral dos créditos de entrada;
2. **Operações de Comércio Eletrônico (*E-Commerce* e Telemarketing) destinadas a Consumidor Final Não Contribuinte em Outra UF:** Crédito presumido sobre o ICMS devido na origem ao Estado do Tocantins de modo que a carga tributária própria na origem resulte em **1,0% a 2,0%** (aproveitando-se do fato de que a alíquota interestadual de saída do Tocantins é de **12%** para todas as UFs nas mercadorias nacionais, reduzindo a parcela do DIFAL devida ao Estado de destino), acrescida da contribuição de **0,3%** sobre o faturamento incentivado ao Fundo de Desenvolvimento Econômico."""
    },

    # =========================================================================
    # CAMADA 3: SIMPLES NACIONAL NAS OPERAÇÕES INTERNAS E INTERESTADUAIS (RESOLUÇÃO CGSN 140/2018)
    # =========================================================================
    {
        "caminho": "federal/leis-complementares/simples/resolucao-cgsn-140-2018-simples-nacional.md",
        "titulo": "Resolução CGSN nº 140, de 22 de maio de 2018 (Regulamento Consolidado do Simples Nacional: Anexos I a V, Fator 'r', Sublimite Estadual e Regras Interestaduais)",
        "esfera": "Federal",
        "orgao": "Comitê Gestor do Simples Nacional - CGSN / Receita Federal do Brasil",
        "tipo": "Resolução CGSN",
        "numero": "140",
        "ano": "2018",
        "data": "2018-05-22",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["Simples Nacional", "IRPJ", "CSLL", "PIS", "Cofins", "IPI", "INSS Patronal", "ICMS", "ISS"],
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/92278",
        "ementa": "Dispõe sobre o Regime Especial Unificado de Arrecadação de Tributos e Contribuições devidos pelas Microempresas e Empresas de Pequeno Porte (Simples Nacional), regulamentando os Anexos I a V, o Fator 'r', o sublimite estadual de R$ 3,6 milhões para o ICMS/ISS, a transferência de crédito de ICMS (CSOSN 101) e as obrigações em operações interestaduais.",
        "corpo": """# Resolução CGSN nº 140, de 22 de maio de 2018 (Regulamento Consolidado do Simples Nacional: Anexos I a V, Fator 'r', Sublimite Estadual e Regras Interestaduais)

RESOLUÇÃO CGSN Nº 140, DE 22 DE MAIO DE 2018

Dispõe sobre o Regime Especial Unificado de Arrecadação de Tributos e Contribuições devidos pelas Microempresas e Empresas de Pequeno Porte (Simples Nacional), instituído pela Lei Complementar nº 123, de 14 de dezembro de 2006.

---

## 1. Limites de Receita Bruta Anual e Sublimite Estadual do ICMS e do ISS (Arts. 2º e 9º a 12)

1. **Limite Federal do Simples Nacional (IRPJ, CSLL, PIS/Pasep, Cofins, IPI e CPP):**
   - **Microempresa (ME):** Receita bruta anual igual ou inferior a **R$ 360.000,00**;
   - **Empresa de Pequeno Porte (EPP):** Receita bruta anual superior a R$ 360.000,00 e igual ou inferior a **R$ 4.800.000,00** (com limite adicional separado de até R$ 4.800.000,00 para exportação de mercadorias e serviços).
2. **Sublimite Estadual e Municipal para Recolhimento de ICMS e ISS dentro do PGDAS-D (`R$ 3.600.000,00`):**
   - Nos termos do art. 13-A e art. 19 da LC nº 123/2006 e da Resolução CGSN anual de sublimites, em todas as **27 Unidades da Federação** vigora o **sublimite de `R$ 3.600.000,00` (três milhões e seiscentos mil reais)** de receita bruta acumulada no mercado interno.
   - **Efeito da Ultrapassagem do Sublimite de R$ 3,6 Milhões (entre R$ 3,6M e R$ 4,8M):**
     - A empresa permanece no Simples Nacional para os tributos federais (`IRPJ`, `CSLL`, `PIS`, `COFINS`, `IPI` e `CPP`), mas fica **impedida de recolher o ICMS e o ISS pelo Simples Nacional (PGDAS-D)**, passando a apurar o **ICMS pelo Regime Normal (Débito $\times$ Crédito, emitindo NF-e com CST e entregando EFD-ICMS/IPI e GIA)** e o ISS conforme a regra municipal:
       - A partir do **ano-calendário subsequente**, se o excesso em relação a R$ 3.600.000,00 não for superior a **20%** (isto é, receita bruta entre **R$ 3.600.000,01 e R$ 4.320.000,00**);
       - A partir do **mês subsequente** àquele em que o excesso ocorrer, se a receita bruta acumulada ultrapassar em **mais de 20%** o sublimite (isto é, superar **R$ 4.320.000,00**).

---

## 2. Fórmula de Cálculo da Alíquota Efetiva e Tabelas dos Anexos I a V (Art. 21)

A alíquota efetiva mensal aplicada sobre a receita bruta do período de apuração (PA) é determinada pela fórmula:
$$\\text{Alíquota Efetiva} = \\frac{(\\text{RBT12} \\times \\text{Alíquota Nominal}) - \\text{Parcela a Deduzir (PD)}}{\\text{RBT12}}$$
Onde $\\text{RBT12}$ é a Receita Bruta acumulada nos 12 (doze) meses anteriores ao período de apuração.

| Faixa | Receita Bruta em 12 Meses (`RBT12`) | Anexo I — Comércio (Alíq. / PD) | Anexo II — Indústria (Alíq. / PD) | Anexo III — Serviços Gerais (Alíq. / PD) | Anexo IV — Construção/Vigilância/Advocacia (Alíq. / PD — CPP fora) | Anexo V — Serviços Intelectuais se Fator 'r' < 28% (Alíq. / PD) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **1ª** | Até R$ 180.000,00 | `4,00%` / R$ 0 | `4,50%` / R$ 0 | `6,00%` / R$ 0 | `4,50%` / R$ 0 | `15,50%` / R$ 0 |
| **2ª** | De R$ 180.000,01 a R$ 360.000,00 | `7,30%` / R$ 5.940 | `7,80%` / R$ 5.940 | `11,20%` / R$ 9.360 | `9,00%` / R$ 8.100 | `18,00%` / R$ 4.500 |
| **3ª** | De R$ 360.000,01 a R$ 720.000,00 | `9,50%` / R$ 13.860 | `10,00%` / R$ 13.860 | `13,50%` / R$ 17.640 | `10,20%` / R$ 12.420 | `19,50%` / R$ 9.900 |
| **4ª** | De R$ 720.000,01 a R$ 1.800.000,00 | `10,70%` / R$ 22.500 | `11,20%` / R$ 22.500 | `16,00%` / R$ 35.640 | `14,00%` / R$ 39.780 | `20,50%` / R$ 17.100 |
| **5ª** | De R$ 1.800.000,01 a R$ 3.600.000,00 | `14,30%` / R$ 87.300 | `14,70%` / R$ 85.500 | `21,00%` / R$ 125.640 | `22,00%` / R$ 183.780 | `23,00%` / R$ 62.100 |
| **6ª** | De R$ 3.600.000,01 a R$ 4.800.000,00 *(ICMS e ISS fora)* | `19,00%` / R$ 378.000 | `30,00%` / R$ 720.000 | `33,00%` / R$ 648.000 | `33,00%` / R$ 828.000 | `30,50%` / R$ 540.000 |

- **Regra do Fator "r" ($\ge 28\%$, Art. 26):** As atividades de prestação de serviços sujeitas ao Anexo V (engenharia, arquitetura, medicina, odontologia, psicologia, tecnologia da informação, desenvolvimento de software, consultoria, auditoria, publicidade, representação comercial, perícia) são tributadas pelo **Anexo III (iniciando em 6%)** quando a razão entre a **Folha de Salários (incluindo pró-labore, salários, 13º, FGTS e CPP dos últimos 12 meses)** e a **Receita Bruta dos últimos 12 meses (`RBT12`)** for **igual ou superior a `28%` (`0,28`)**.

---

## 3. Regras do Simples Nacional nas Operações Internas e Interestaduais com Mercadorias (ICMS)

1. **Transferência de Crédito de ICMS por Optante do Simples Nacional (Art. 58 a 60 da Res. CGSN 140/2018 e Art. 23 da LC 123/2006):**
   - As pessoas jurídicas **não optantes** pelo Simples Nacional (Lucro Real ou Presumido) têm direito a **crédito correspondente ao ICMS efetivamente devido** na operação de aquisição de mercadorias de ME ou EPP optante pelo Simples Nacional, desde que as mercadorias se destinem à **comercialização ou industrialização**.
   - A empresa do Simples Nacional deve utilizar o **CSOSN `101` (*Tributada pelo Simples Nacional com permissão de crédito*)**, informando em campos próprios da NF-e (`pCredSN` e `vCredICMSSN`) e em "Informações Complementares" a alíquota efetiva da parcela do ICMS dentro da sua faixa do Anexo I ou II no mês anterior: *"PERMITE O APROVEITAMENTO DO CRÉDITO DE ICMS NO VALOR DE R$ ...; CORRESPONDENTE À ALÍQUOTA DE ...%, NOS TERMOS DO ART. 23 DA LEI COMPLEMENTAR Nº 123, DE 2006"*.
2. **Segregação de Receitas com Substituição Tributária (ICMS-ST) e PIS/COFINS Monofásico (Art. 25, § 8º):**
   - Na apuração do PGDAS-D, o contribuinte substituído (varejista/revendedor) optante pelo Simples Nacional deve **segregar a receita de venda de mercadorias sujeitas a ICMS-ST** (CSOSN `500`) e a **regime monofásico de PIS/COFINS** (bebidas frias, medicamentos, autopeças, perfumaria/higiene, combustíveis), **zerando a parcela do ICMS e do PIS/COFINS** dentro do DAS para evitar bitributação.
3. **Operações Interestaduais promovidas OU recebidas por Empresas do Simples Nacional:**
   - **Na Saída Interestadual sujeita a ICMS-ST (Optante como Substituto Tributário — Convênio ICMS 35/2011 e Art. 28 da Res. CGSN 140/2018):**
     - O ICMS próprio da operação interestadual é recolhido dentro do PGDAS-D;
     - Na apuração da base de cálculo do **ICMS-ST devido à UF de destino**, **NÃO se aplica a MVA Ajustada** (utiliza-se sempre a **MVA-ST Original**); e
     - Para cálculo do ICMS-ST a reter, **deduz-se como crédito presumido de operação própria a alíquota interestadual cheia de `4%`, `7%` ou `12%`** (mesmo que o remetente do Simples pague uma alíquota menor no PGDAS-D!).
   - **Na Entrada Interestadual em Empresa do Simples Nacional (Antecipação de Fronteira / Diferencial de Alíquotas e DIFAL Uso/Consumo):**
     - Nos termos do art. 13, § 1º, XIII, "g" e "h" da LC nº 123/2006 e do **Tema 517 / RE 970.821 do STF**, os Estados estão autorizados a cobrar, **por fora do PGDAS-D**, o **Diferencial de Alíquotas na entrada interestadual** de mercadorias destinadas a uso/consumo, ativo imobilizado e também a **Antecipação Tributária de Fronteira (Equalização de Alíquota)** nas compras interestaduais para comercialização ou industrialização quando a alíquota interestadual (4%, 7% ou 12%) for inferior à alíquota interna da UF do adquirente.
   - **Na Venda Interestadual de Empresa do Simples Nacional para Consumidor Final Não Contribuinte (DIFAL EC 87/2015):**
     - Por força da decisão vinculante do STF na **ADI 5464 e no Tema 1284 (RE 1.400.775)**, **NÃO é devido o DIFAL Não Contribuinte** nas saídas interestaduais promovidas por remetente optante pelo Simples Nacional."""
    },

    # =========================================================================
    # CAMADA 4: SPED FISCAL (EFD-ICMS/IPI) E NOTA TÉCNICA NF-E 2024.002 (IBS, CBS E IMPOSTO SELETIVO)
    # =========================================================================
    {
        "caminho": "estaduais/confaz/ajustes-sinief/2009/guia-pratico-efd-icms-ipi-regras-interestaduais.md",
        "titulo": "Ato COTEPE/ICMS nº 44, de 7 de agosto de 2018 (Guia Prático da EFD-ICMS/IPI — SPED Fiscal: Blocos e Registros para Operações Internas e Interestaduais)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ / Receita Federal do Brasil",
        "tipo": "Ato COTEPE/ICMS",
        "numero": "44",
        "ano": "2018",
        "data": "2018-08-07",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST", "IPI"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/ajustes/2009/AJ_002_09",
        "ementa": "Institui o Manual de Orientação do Leiaute da Escrituração Fiscal Digital - EFD ICMS/IPI (SPED Fiscal) e o Guia Prático da EFD-ICMS/IPI, detalhando a escrituração de documentos fiscais, apuração própria, Substituição Tributária por UF (Registro E200) e DIFAL/FCP por UF (Registro E300).",
        "corpo": """# Ato COTEPE/ICMS nº 44, de 7 de agosto de 2018 (Guia Prático da EFD-ICMS/IPI — SPED Fiscal: Blocos e Registros para Operações Internas e Interestaduais)

ATO COTEPE/ICMS Nº 44, DE 7 DE AGOSTO DE 2018 — GUIA PRÁTICO DA ESCRITURAÇÃO FISCAL DIGITAL (EFD-ICMS/IPI)

## 1. Estrutura de Blocos da EFD-ICMS/IPI (SPED Fiscal)

| Bloco | Nome do Bloco | Conteúdo e Finalidade Fiscal |
| :---: | :--- | :--- |
| **`0`** | Abertura, Identificação e Referências | Dados cadastrais do contribuinte (`0000`), participantes clientes/fornecedores com código de município IBGE e UF (`0150`), cadastro de itens NCM/CEST (`0200`), bens do ativo imobilizado CIAP (`0300`) e tabelas de observações (`0460`). |
| **`B`** | Escrituração e Apuração do ISS | Exclusivo para contribuintes do Distrito Federal (conjugação ICMS + ISS). |
| **`C`** | Documentos Fiscais I — Mercadorias (ICMS/IPI) | Notas Fiscais modelos `01`, `1B`, `04`, **`55` (NF-e)** e **`65` (NFC-e)**: entradas e saídas internas, interestaduais e de comércio exterior. |
| **`D`** | Documentos Fiscais II — Serviços (ICMS) | Conhecimentos de Transporte Eletrônicos (**`CT-e` modelo `57` e `CT-e OS` modelo `67`**) e Notas Fiscais de Serviços de Comunicação/Telecomunicação (**`NFCom` modelo `62`**, `21` e `22`). |
| **`E`** | **Apuração do ICMS e do IPI** | Apuração do **ICMS Próprio (`E100`/`E110`)**, do **ICMS-ST por UF (`E200`/`E210`)**, do **DIFAL EC 87/2015 e FCP por UF de destino (`E300`/`E310`)** e do **IPI (`E500`/`E520`)**. |
| **`G`** | Controle do Crédito de ICMS do Ativo Permanente (**CIAP**) | Controle e apropriação em **1/48 (um quarenta e oito avos) mensais** do crédito de ICMS (próprio + DIFAL + frete) sobre aquisições para o Ativo Imobilizado (art. 20, § 5º da LC 87/1996). |
| **`H`** | Inventário Físico | Posição física e financeira dos estoques em 31 de dezembro (ou por mudança de regime de ST). |
| **`K`** | Controle da Produção e do Estoque | Escrituração mensal da movimentação de estoques (`K200`), ordens de produção e consumo de insumos (`K230`/`K235`) e industrialização em terceiros (`K250`/`K255`). |
| **`1`** | Outras Informações | Exportações (`1100`), controle de créditos fiscais (`1200`), operações com cartões/PIX (`1600`/`1601`) e sub-apurações estaduais (`1900`). |

---

## 2. Regras de Escrituração das Operações Interestaduais nos Registros dos Blocos `C`, `D` e `E`

### 2.1. Escrituração sob o Enfoque do Declarante (Regra de Ouro da EFD-ICMS/IPI)
- **Nas Entradas Interestaduais (CFOP `2.xxx`):** Os registros `C100` (cabeçalho), `C170` (itens) e `C190` (analítico por CST/CFOP/Alíquota) devem ser escriturados **sob o enfoque do estabelecimento declarante destinatário**:
  - Se a aquisição interestadual for para **uso ou consumo (`CFOP 2.556`)** ou **ativo imobilizado (`CFOP 2.551`)**, não há apropriação direta de crédito no `C190` (o crédito do ativo vai pelo Bloco `G` em 1/48), e o valor do **DIFAL Contribuinte** é lançado mediante ajuste de débito especial ou apuração no Registro `C197` (código de ajuste da tabela 5.3 da UF) ou no Registro `E111` (tabela 5.1.1 da UF).
  - Se a aquisição interestadual estiver sujeita à **Substituição Tributária já retida pelo remetente (`CFOP 2.403`)** ou **Antecipação com encerramento na entrada**, a entrada é escriturada com CST `060`, sem crédito de ICMS próprio nem de ST no `C190`.

### 2.2. Apuração do ICMS-ST por Unidade da Federação — Registros `E200` a `E250`
- Para cada Estado de destino em que o contribuinte tenha realizado operações interestaduais com retenção de **ICMS-ST** (como substituto tributário por protocolo ou convênio, CFOP `6.401`/`6.403`/`6.404`), a EFD-ICMS/IPI deve gerar um **Registro `E200` identificando a sigla da UF de destino** (`UF`), seguido do `E210` (apuração do ICMS-ST devido àquela UF, devoluções de ST e ressarcimentos) e do `E250` (detalhamento das GNREs código `10009-9` ou `10004-8` recolhidas àquela UF).

### 2.3. Apuração do DIFAL Não Contribuinte e FCP por UF — Registros `E300` a `E316`
- Sempre que o contribuinte realizar vendas ou prestações interestaduais destinadas a consumidor final não contribuinte (`CFOP 6.107` ou `6.108`), deve gerar um **Registro `E300` para cada UF de destino**, apurando no `E310` o saldo devedor do **DIFAL** e, separadamente, do **Fundo de Combate à Pobreza (FCP)**, vinculando no `E316` as respectivas guias GNRE (`10010-2` / `10011-0` para o DIFAL e `10012-9` / `10013-7` para o FCP)."""
    },
    {
        "caminho": "reforma-tributaria/split-payment/nota-tecnica-nfe-2024-002-ibs-cbs-is.md",
        "titulo": "Nota Técnica Conjunta ENCAT / RFB nº 2024.002 (Reforma Tributária do Consumo na NF-e e NFC-e: Leiautes XML de IBS Estadual/Municipal, CBS e Imposto Seletivo)",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil / ENCAT - CONFAZ",
        "tipo": "Nota Técnica Conjunta",
        "numero": "2024.002",
        "ano": "2024",
        "data": "2024-08-01",
        "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": ["IBS", "CBS", "Imposto Seletivo", "ICMS", "ISS", "IPI", "PIS", "Cofins"],
        "fonte": "https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY=",
        "ementa": "Estabelece as especificações técnicas e os novos grupos de campos XML da Nota Fiscal Eletrônica (NF-e, modelo 55) e da Nota Fiscal de Consumidor Eletrônica (NFC-e, modelo 65) para apuração do Imposto sobre Bens e Serviços (IBS Estadual e Municipal), da Contribuição sobre Bens e Serviços (CBS) e do Imposto Seletivo (IS) a partir de 2026.",
        "corpo": """# Nota Técnica Conjunta ENCAT / RFB nº 2024.002 (Reforma Tributária do Consumo na NF-e e NFC-e: Leiautes XML de IBS Estadual/Municipal, CBS e Imposto Seletivo)

NOTA TÉCNICA CONJUNTA ENCAT / RECEITA FEDERAL DO BRASIL Nº 2024.002 — ADEQUAÇÃO DOS DOCUMENTOS FISCAIS ELETRÔNICOS À EMENDA CONSTITUCIONAL Nº 132/2023 E AO PLP Nº 68/2024

## 1. Mudança de Paradigma nas Operações entre Estados e Municípios: Do Princípio da Origem Mista para o Princípio do Destino Pleno

Com a implementação do **IBS (Imposto sobre Bens e Serviços — competência compartilhada de Estados e Municípios)** e da **CBS (Contribuição sobre Bens e Serviços — competência Federal)**:
1. **Tributação Integral no Destino (Fim da Alíquota Interestadual de Origem no IBS):**
   - Diferentemente do ICMS atual (em que parte fica na origem via 4%, 7% ou 12% e parte vai para o destino via DIFAL ou ST), no **IBS 100% da alíquota aplicável é a alíquota da Unidade Federada (`pIBSUF`) e do Município (`pIBSMun`) de destino da operação** (local da entrega/disponibilização do bem ou fruição do serviço).
2. **Cálculo "Por Fora" Unificado:**
   - O IBS e a CBS **não integram sua própria base de cálculo** nem a base um do outro (cálculo estritamente *por fora*), extinguindo a sistemática de cálculo "por dentro" do ICMS.

---

## 2. Novos Grupos e Tags XML do Item da NF-e / NFC-e (`Grupo UB — Tributos do Consumo`)

Durante o período de transição (2026 a 2032), o grupo de impostos (`<imposto>`) de cada item (`<det>`) da NF-e conviverá simultaneamente com os grupos atuais (`<ICMS>`, `<IPI>`, `<PIS>`, `<COFINS>`) e os novos grupos da Reforma Tributária:

### 2.1. Grupo `<IS>` — Imposto Seletivo Federal (Monofásico)
- **`<CSTIS>`:** Código de Situação Tributária do Imposto Seletivo;
- **`<cClassTribIS>`:** Código de Classificação Tributária do Imposto Seletivo;
- **`<vBCIS>`:** Valor da Base de Cálculo do Imposto Seletivo (o IS **integra** a base de cálculo do IBS, da CBS e, durante a transição, do ICMS e do ISS);
- **`<pIS>` e `<pISEspec>`:** Alíquota *ad valorem* (%) e alíquota específica (*ad rem* por unidade de medida tributável `uTrib`: litro, kg, maço, kW);
- **`<vIS>`:** Valor resultante do Imposto Seletivo.

### 2.2. Grupo `<IBSCBS>` — Imposto sobre Bens e Serviços (Estadual + Municipal) e Contribuição sobre Bens e Serviços (Federal)
- **`<CST>`:** Código de Situação Tributária unificado do IBS e da CBS (tabela nacional parametrizada pelo Comitê Gestor do IBS e pela RFB: tributação integral, alíquota reduzida em 30%/60%/100%, diferimento, suspensão, regime específico monofásico, imunidade/exportação);
- **`<cClassTrib>`:** Código de Classificação Tributária do IBS e da CBS (vincula o item exatamente ao artigo, inciso e anexo do PLP 68/2024: cesta básica nacional alíquota zero, saúde/educação redução de 60%, insumos agropecuários, etc.);
- **`<gIBSCBS>` — Detalhamento da Base e das 3 Parcelas Federativas:**
  - **`<vBC>`:** Base de cálculo única comum ao IBS Estadual, ao IBS Municipal e à CBS Federal (valor da operação + Imposto Seletivo, **sem** ICMS, ISS, PIS, COFINS, IBS e CBS);
  - **Subgrupo `<gIBSUF>` (Parcela Estadual do IBS — UF de Destino):**
    - `<pIBSUF>`: Alíquota do IBS da UF de destino (0,1% em 2026 nos testes; e alíquota estadual progressiva de 2029 a 2033 conforme redução de 1/10 ao ano do ICMS);
    - `<pRedAliq>` e `<pAliqEfet>`: Percentual de redução da alíquota (ex.: 60% ou 30%) e alíquota efetiva resultante;
    - `<vIBSUF>`: Valor do IBS devido ao Estado de destino;
  - **Subgrupo `<gIBSMun>` (Parcela Municipal do IBS — Município de Destino):**
    - `<pIBSMun>`, `<pRedAliq>`, `<pAliqEfet>` e `<vIBSMun>`: Valor do IBS devido ao Município de destino;
  - **Subgrupo `<gCBS>` (Parcela Federal da CBS — União):**
    - `<pCBS>`: Alíquota da CBS (0,9% no ano-teste de 2026; e alíquota plena a partir de 2027 com a extinção do PIS e da COFINS);
    - `<pRedAliq>`, `<pAliqEfet>` e `<vCBS>`: Valor da CBS devida à União.

---

## 3. Novos Eventos e Finalidades de Nota Fiscal Eletrônica na Reforma Tributária (`finNFe`)

Além das finalidades atuais (`1=Normal`, `2=Complementar`, `3=Ajuste`, `4=Devolução`), a Nota Técnica 2024.002 introduz as **Notas Fiscais de Débito e de Crédito Eletrônicas** para ajustes financeiros e vinculação ao **Split Payment** (liquidação financeira com segregação automática do IBS e da CBS que condiciona a apropriação do crédito pelo adquirente)."""
    },
]

def main():
    auditor = AgenteAuditor()
    salvos = 0

    for doc in CAMADAS_LLM:
        meta = {
            "titulo": doc["titulo"],
            "esfera": doc["esfera"],
            "orgao": doc["orgao"],
            "tipo": doc["tipo"],
            "numero": doc["numero"],
            "ano": doc["ano"],
            "data": doc["data"],
            "tema_tributario": doc["tema_tributario"],
            "tributos_afetados": doc["tributos_afetados"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": doc["fonte"],
            "ementa": doc["ementa"],
        }
        caminho = RAIZ / doc["caminho"]
        conteudo = f"{gerar_frontmatter(meta)}{doc['corpo'].strip()}\n"
        salvar_atomico(caminho, conteudo.encode("utf-8"))
        valido, erros = auditor.auditar_documento(caminho, checar_rede=True)
        print(f"[Camadas LLM] {caminho.relative_to(RAIZ)} -> valido={valido} erros={erros}")
        if valido:
            salvos += 1

    print(f"\nTotal Camadas Profundas LLM salvos e auditados (com rede): {salvos}/{len(CAMADAS_LLM)}")

if __name__ == "__main__":
    main()
