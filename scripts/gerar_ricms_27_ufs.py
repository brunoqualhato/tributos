"""Gera e audita os Regulamentos do ICMS (RICMS) e Leis Orgânicas do ICMS das 27 Unidades Federativas.

Construído especificamente para alimentar LLMs com as regras completas internas e interestaduais de cada Estado:
- Alíquota modal interna vigentes (2024-2026) e Fundo de Combate à Pobreza (FCP/FECOP/FECOEP/FEM)
- Alíquotas interestaduais de saída e entrada (4%, 7% e 12%)
- Metodologia de cálculo do DIFAL Contribuinte (Uso/Consumo e Ativo Imobilizado: Base Dupla "por dentro" vs. Base Única) e DIFAL Não Contribuinte (EC 87/2015 e LC 190/2022)
- Antecipação Tributária na entrada interestadual (com e sem encerramento de fase, regras para Simples Nacional) e Substituição Tributária (ICMS-ST)
- Transferências interestaduais entre estabelecimentos do mesmo titular (LC 204/2023 e Convênio ICMS 109/2024)
- Benefícios fiscais e regimes especiais de cada UF (TTD SC, COMPETE-ES, PROGOIÁS, PRODEPE, DESENVOLVE, FDI, ZFM/ALC, etc.)
"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from comum import gerar_frontmatter, salvar_atomico
from agente_auditor import AgenteAuditor

UFS_RICMS = [
    # =========================================================================
    # REGIÃO SUDESTE (SP, RJ, MG, ES)
    # =========================================================================
    {
        "uf": "sp",
        "estado": "São Paulo",
        "regiao": "Sudeste",
        "decreto_num": "45490",
        "decreto_ano": "2000",
        "decreto_data": "2000-11-30",
        "titulo": "Decreto nº 45.490, de 30 de novembro de 2000 (Regulamento do ICMS - RICMS/SP)",
        "lei_base": "Lei Estadual nº 6.374, de 1º de março de 1989",
        "orgao": "Governo do Estado de São Paulo / Secretaria da Fazenda e Planejamento (SEFAZ/SP)",
        "urn_uf": "sao.paulo",
        "aliquota_modal": "18%",
        "fcp": "Até 2% (FECOEP/SP - Lei nº 16.006/2015, aplicável a bebidas alcoólicas, fumo/cigarros, cosméticos/perfumaria específicos)",
        "aliquotas_internas_especificas": "7% (insumos agropecuários, cesta básica selecionada, indústria de processamento eletrônico de dados); 12% (serviços de transporte, refeições, máquinas industriais/agrícolas relaciondas, carnes, óleo diesel/etanol hidratado conforme regras específicas, medicamentos genéricos); 18% (alíquota modal geral e energia elétrica residencial até 200 kWh); 25% (supérfluos, bebidas alcoólicas, fumo, perfumes/cosméticos).",
        "aliquota_inter_saida_n_ne_co_es": "7% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% (para MG, RJ, PR, SC, RS)",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012 e Convênio ICMS 38/2013 - FCI)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 117 e Art. 49 do RICMS/SP e Lei nº 17.470/2021): exclui-se o ICMS interestadual da base de operação e divide-se por `(1 - Alíquota Interna SP)` para apurar a base de cálculo no destino, deduzindo o imposto interestadual de 4% ou 12%.",
        "antecipacao_st": "Art. 426-A do RICMS/SP (Antecipação Tributária com encerramento de tributação na entrada interestadual de mercadoria sujeita ao regime de ST em SP quando procedente de UF sem acordo/protocolo vigente); Art. 115, XV-A (Diferencial de alíquotas por antecipação na entrada interestadual para contribuinte optante pelo Simples Nacional paulista quando a alíquota interestadual for inferior à interna de SP, ex.: 4% para 18% ou 12% para 18%).",
        "beneficios_destaque": "Anexo I (Isenções), Anexo II (Reduções de Base de Cálculo), Anexo III (Créditos Outorgados), Regime Especial de Tributação para Comércio Eletrônico (Decreto nº 67.383/2022), diferimento em insumos agropecuários e sucroenergéticos, e Sistema e-CredAc (Portaria SRE 65/2023) para apropriação e transferência de crédito acumulado de ICMS.",
    },
    {
        "uf": "rj",
        "estado": "Rio de Janeiro",
        "regiao": "Sudeste",
        "decreto_num": "27427",
        "decreto_ano": "2000",
        "decreto_data": "2000-11-17",
        "titulo": "Decreto nº 27.427, de 17 de novembro de 2000 (Regulamento do ICMS - RICMS/RJ)",
        "lei_base": "Lei Estadual nº 2.657, de 26 de dezembro de 1996",
        "orgao": "Governo do Estado do Rio de Janeiro / Secretaria de Estado de Fazenda (SEFAZ/RJ)",
        "urn_uf": "rio.janeiro",
        "aliquota_modal": "20% + 2% de FECP = 22% de carga efetiva modal (Lei nº 10.253/2023, vigente a partir de 20/03/2024)",
        "fcp": "2% em regra geral sobre todas as operações internas e de importação sujeitas ao ICMS (Fundo Estadual de Combate à Pobreza e às Desigualdades Sociais - FECP, Lei nº 4.056/2002), exceto cesta básica, medicamentos essenciais e atividades expressamente dispensadas; podendo chegar a até 4% em supérfluos específicos.",
        "aliquotas_internas_especificas": "7% (cesta básica essencial - Lei nº 9.391/2021); 12% (transporte aéreo e operações específicas); 18% + 2% FECP (energia elétrica até faixa limite e telecomunicações - LC 194/2022); 20% + 2% FECP = 22% (alíquota geral modal); 25% a 32% + FECP (bebidas alcoólicas, cigarros/fumo, armas, embarcações de esporte/recreio).",
        "aliquota_inter_saida_n_ne_co_es": "7% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% (para SP, MG, PR, SC, RS)",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012 e Convênio ICMS 38/2013)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 3º, VI e Art. 4º, VI da Lei nº 2.657/1996, com redação da Lei nº 7.071/2015): aplica-se a alíquota interna do RJ (20% + 2% FECP = 22%) sobre a base recomposta por dentro, deduzindo o ICMS interestadual destacado (4% ou 12%).",
        "antecipacao_st": "Livro II do RICMS/RJ (Substituição Tributária nas operações internas e interestaduais); exigência de recolhimento antecipado do ICMS-ST + FECP-ST na barreira fiscal/entrada do território fluminense quando o remetente de outra UF não possuir inscrição de substituto no RJ.",
        "beneficios_destaque": "RIO+ (Regimes diferenciados de importação pelos portos e aeroportos fluminenses), Lei nº 6.979/2015 (tratamento tributário especial para indústrias em municípios do interior fluminense - alíquota efetiva de 2%/3%), Lei nº 9.025/2020 (comércio atacadista / centros de distribuição com crédito presumido nas saídas interestaduais). Nota sobre o FEEF/FOT (Fundo Orçamentário Temporário - Lei nº 8.645/2019): depósito de 10% do benefício fiscal fruído.",
    },
    {
        "uf": "mg",
        "estado": "Minas Gerais",
        "regiao": "Sudeste",
        "decreto_num": "48589",
        "decreto_ano": "2023",
        "decreto_data": "2023-03-22",
        "titulo": "Decreto nº 48.589, de 22 de março de 2023 (Regulamento do ICMS - RICMS/MG)",
        "lei_base": "Lei Estadual nº 6.763, de 26 de dezembro de 1975",
        "orgao": "Governo do Estado de Minas Gerais / Secretaria de Estado de Fazenda (SEF/MG)",
        "urn_uf": "minas.gerais",
        "aliquota_modal": "18%",
        "fcp": "2% (Fundo de Erradicação da Miséria - FEM/MG, art. 12-A da Lei nº 6.763/1975 e Decreto nº 46.927/2015), incidente sobre cervejas, chopes, refrigerantes, bebidas alcoólicas, cigarros, armas, celulares, perfumes, cosméticos e iates.",
        "aliquotas_internas_especificas": "7% (produtos da cesta básica com redução de base no Anexo II); 12% (ferro-gusa, produtos siderúrgicos e metalúrgicos selecionados em operações internas entre contribuintes, móveis, calçados, tratores/máquinas agrícolas, transporte aéreo); 18% (alíquota geral modal, energia elétrica e comunicações pós-LC 194/2022); 25% + 2% FEM (supérfluos, bebidas alcoólicas, fumo, perfumes).",
        "aliquota_inter_saida_n_ne_co_es": "7% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% (para SP, RJ, PR, SC, RS)",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 12, § 1º e Art. 13, § 1º-C da Lei nº 6.763/1975 e Art. 31 do RICMS/MG 2023): exclui-se o ICMS interestadual do valor da operação, divide-se por `(1 - Alíquota Interna MG)` e aplica-se a alíquota interna sobre a nova base, subtraindo o ICMS interestadual.",
        "antecipacao_st": "Anexo VII do Novo RICMS/MG (Decreto nº 48.589/2023): Substituição Tributária interna e interestadual. Antecipação do Diferencial de Alíquota (Recolhimento de Equalização - Art. 12, § 14 da Lei nº 6.763/1975) exigida nas aquisições interestaduais de mercadorias para comercialização ou industrialização por empresas do Simples Nacional mineiras quando a alíquota interestadual (4% ou 12%) for inferior à alíquota interna mineira.",
        "beneficios_destaque": "TTS (Tratamento Tributário Setorial) / Corredor de Importação de MG (diferimento na importação e crédito presumido nas saídas interestaduais e internas), TTS E-Commerce (crédito presumido para vendas não presenciais interestaduais), TTS Atacadista/Distribuidor.",
    },
    {
        "uf": "es",
        "estado": "Espírito Santo",
        "regiao": "Sudeste",
        "decreto_num": "1090",
        "decreto_ano": "2002",
        "decreto_data": "2002-10-25",
        "titulo": "Decreto nº 1.090-R, de 25 de outubro de 2002 (Regulamento do ICMS - RICMS/ES)",
        "lei_base": "Lei Estadual nº 7.000, de 27 de dezembro de 2001",
        "orgao": "Governo do Estado do Espírito Santo / Secretaria de Estado da Fazenda (SEFAZ/ES)",
        "urn_uf": "espirito.santo",
        "aliquota_modal": "17%",
        "fcp": "2% (Fundo Estadual de Combate à Pobreza e às Desigualdades Sociais - FUNCOP/ES, Lei Complementar nº 336/2005), incidente sobre bebidas alcoólicas, fumo, perfumes/cosméticos e embarcações de esporte.",
        "aliquotas_internas_especificas": "7% (cesta básica reduzida); 12% (transporte interstadual/intermunicipal de cargas e passageiros, máquinas e equipamentos industriais, rochas ornamentais/mármore e granito, café); 17% (alíquota geral modal, energia elétrica e telecomunicações - LC 194/2022); 25% + 2% FUNCOP (supérfluos, bebidas alcoólicas, fumo).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Atenção à Regra Constitucional do ES: embora pertença geograficamente à Região Sudeste, nos termos da Resolução SF nº 22/1989, as saídas interestaduais promovidas por contribuintes do Espírito Santo para QUALQUER unidade da Federação aplicam a alíquota de 12%, ou 4% para importados; já as remessas dos demais estados do Sul e Sudeste — SP, RJ, MG, PR, SC, RS — destinadas ao ES aplicam a alíquota de 7%!)",
        "aliquota_inter_saida_s_se": "12% nas saídas do ES para Sul/Sudeste; 7% nas entradas no ES oriundas de SP, RJ, MG, PR, SC e RS (exceto 4% importados).",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Única (Art. 63, XI e XII do RICMS/ES e Lei nº 7.000/2001): o Espírito Santo destaca-se historicamente por adotar cálculo sobre a base da operação, aplicando o percentual equivalente à diferença entre a alíquota interna (17%) e a interestadual (7%, 12% ou 4%), observadas as regras da LC 190/2022.",
        "antecipacao_st": "Anexo V do RICMS/ES (Regime de Substituição Tributária). Exigência de antecipação parcial ou ST nas entradas interestaduais sem protocolo quando listado em portaria SEFAZ/ES.",
        "beneficios_destaque": "COMPETE-ES (Programa de Desenvolvimento e Proteção à Economia do Estado do Espírito Santo - Lei nº 10.568/2016: COMPETE Atacadista com carga efetiva de 1,1% nas saídas interestaduais e COMPETE E-Commerce para vendas não presenciais com carga efetiva de 1,1%), INVEST-ES (diferimento no ativo e crédito presumido industrial) e FUNDAP (operações de comércio exterior pelos portos capixabas).",
    },

    # =========================================================================
    # REGIÃO SUL (PR, SC, RS)
    # =========================================================================
    {
        "uf": "pr",
        "estado": "Paraná",
        "regiao": "Sul",
        "decreto_num": "7871",
        "decreto_ano": "2017",
        "decreto_data": "2017-09-29",
        "titulo": "Decreto nº 7.871, de 29 de setembro de 2017 (Regulamento do ICMS - RICMS/PR)",
        "lei_base": "Lei Estadual nº 11.580, de 14 de novembro de 1996",
        "orgao": "Governo do Estado do Paraná / Secretaria de Estado da Fazenda (SEFA/PR)",
        "urn_uf": "parana",
        "aliquota_modal": "19,5% (elevada de 19% para 19,5% pela Lei nº 21.850/2023, vigente desde 18/03/2024)",
        "fcp": "2% (Fundo Estadual de Combate à Pobreza do Paraná - FECOP/PR, Lei nº 18.573/2015), incidente sobre bebidas alcoólicas, águas minerais gasosas, fumo, perfumes/cosméticos, artefatos de joalheria.",
        "aliquotas_internas_especificas": "0% / Isenção (cesta básica paranaense para consumidor final); 7% (insumos agropecuários selecionados); 12% (refeições, veículos automotores novos sob regime de ST, máquinas e aparelhos industriais, produtos da indústria de informática, tijolos/telhas, produtos alimentícios da cesta básica na cadeia intermediária); 18% (energia elétrica e comunicações); 19,5% (alíquota geral modal); 27% + 2% FECOP = 29% (bebidas alcoólicas, fumo, armas).",
        "aliquota_inter_saida_n_ne_co_es": "7% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% (para RS, SC, SP, RJ, MG)",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 14, § 8º da Lei nº 11.580/1996, incluído pela Lei nº 18.879/2016): exclui-se o ICMS interestadual do valor da operação, recompõe-se a base dividindo por `(1 - Alíquota Interna PR de 19,5%)`, aplica-se 19,5% e deduz-se o imposto interestadual.",
        "antecipacao_st": "Anexo IX do RICMS/PR (Substituição Tributária). Diferencial de Alíquotas por Antecipação (Equalização de 12% ou 4% para a alíquota interna) nas entradas interestaduais destinadas à comercialização ou industrialização por empresas paranaenses optantes pelo Simples Nacional (Art. 17, XIV do RICMS/PR).",
        "beneficios_destaque": "Diferimento parcial de 38,46% nas operações internas entre contribuintes paranaenses (resultando em carga tributária efetiva de 12% em vez de 19,5% no atacado/indústria interna - Art. 28 do Anexo VIII do RICMS/PR), Programa Paraná Competitivo (Decreto nº 6.434/2017 - diferimento na importação pelos portos de Paranaguá e Antonina e crédito presumido nas saídas).",
    },
    {
        "uf": "sc",
        "estado": "Santa Catarina",
        "regiao": "Sul",
        "decreto_num": "2870",
        "decreto_ano": "2001",
        "decreto_data": "2001-08-27",
        "titulo": "Decreto nº 2.870, de 27 de agosto de 2001 (Regulamento do ICMS - RICMS/SC)",
        "lei_base": "Lei Estadual nº 10.297, de 26 de dezembro de 1996",
        "orgao": "Governo do Estado de Santa Catarina / Secretaria de Estado da Fazenda (SEF/SC)",
        "urn_uf": "santa.catarina",
        "aliquota_modal": "17%",
        "fcp": "Santa Catarina NÃO instituiu adicional de alíquota de Fundo de Combate à Pobreza (FCP = 0% em SC).",
        "aliquotas_internas_especificas": "7% (produtos da cesta básica catarinense); 12% (Kits e mercadorias destinadas a contribuintes nas operações internas entre indústrias/atacadistas conforme art. 19, III, 'n' da Lei nº 10.297/1996 - regra geral B2B interno de 12% em SC; veículos automotores; óleo diesel; transporte; energia elétrica rural); 17% (alíquota geral modal, vendas a consumidor final não contribuinte, energia elétrica até 500 kWh e telecomunicações - LC 194/2022); 25% (supérfluos, bebidas alcoólicas, cigarros, perfumes/cosméticos).",
        "aliquota_inter_saida_n_ne_co_es": "7% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% (para PR, RS, SP, RJ, MG)",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 9º, § 6º da Lei nº 10.297/1996, alterado pela Lei nº 18.315/2021): cálculo com exclusão do ICMS interestadual e recomposição pela alíquota interna aplicável em SC (17% ou 12% conforme o produto).",
        "antecipacao_st": "Anexo 3 do RICMS/SC (Substituição Tributária - SC reduziu substancialmente a lista de segmentos no ICMS-ST nos últimos anos, excluindo bebidas quentes, autopeças, materiais de construção, ferramentas, lâmpadas e produtos farmacêuticos da ST interna).",
        "beneficios_destaque": "TTD 409 / TTD 410 / TTD 411 (Tratamento Tributário Diferenciado na Importação por portos e aeroportos catarinenses — Itajaí, Navegantes, São Francisco do Sul, Imbituba, Itapoá — com diferimento no desembaraço aduaneiro e crédito presumido nas saídas interestaduais a 4%, resultando em carga efetiva de 1,0% a 2,6% mais 0,4% de fundos estaduais FUMDES/Fundo Social), TTD 478 (E-Commerce catarinense com crédito presumido).",
    },
    {
        "uf": "rs",
        "estado": "Rio Grande do Sul",
        "regiao": "Sul",
        "decreto_num": "37699",
        "decreto_ano": "1997",
        "decreto_data": "1997-08-26",
        "titulo": "Decreto nº 37.699, de 26 de agosto de 1997 (Regulamento do ICMS - RICMS/RS)",
        "lei_base": "Lei Estadual nº 8.820, de 27 de janeiro de 1989",
        "orgao": "Governo do Estado do Rio Grande do Sul / Secretaria da Fazenda (SEFAZ/RS)",
        "urn_uf": "rio.grande.sul",
        "aliquota_modal": "17%",
        "fcp": "2% (Fundo de Proteção e Amparo Social do Estado do Rio Grande do Sul - AMPARA/RS, Lei nº 14.742/2015), incidente sobre bebidas alcoólicas, cerveja sem álcool, cigarros/fumo, perfumaria e cosméticos.",
        "aliquotas_internas_especificas": "7% (cesta básica gaúcha); 12% (máquinas e equipamentos industriais, implementos agrícolas, diferimento parcial B2B interno que reduz a carga de 17% para 12% nas saídas internas entre contribuintes gaúchos); 17% (alíquota geral modal, energia elétrica e comunicações); 25% + 2% AMPARA = 27% (bebidas alcoólicas, fumo, armas, perfumaria).",
        "aliquota_inter_saida_n_ne_co_es": "7% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% (para PR, SC, SP, RJ, MG)",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Livro I, Art. 16, I, 'f' e 'g' do RICMS/RS): recomposição da base de cálculo pela alíquota interna gaúcha (17%) após exclusão do ICMS interestadual.",
        "antecipacao_st": "Livro III do RICMS/RS (Substituição Tributária) e Regime Optativo de Tributação da Substituição Tributária (ROT-ST). Diferencial de Alíquotas de Fronteira (Livro I, Art. 46, § 4º do RICMS/RS) exigido na entrada de mercadorias oriundas de outra UF destinadas a comercialização ou industrialização no RS (inclusive Simples Nacional, respeitada a faixa de isenção estadual para ME/EPP até R$ 360 mil).",
        "beneficios_destaque": "FUNDOPEM/RS e INTEGRAR/RS (incentivo financeiro-fiscal à implantação e expansão industrial no RS), Diferimento Parcial de ICMS nas operações internas entre contribuintes (carga efetiva de 12%), e Fator de Ajuste de Fruição (FAF) vinculado à aquisição de insumos internos.",
    },

    # =========================================================================
    # REGIÃO CENTRO-OESTE (DF, GO, MT, MS)
    # =========================================================================
    {
        "uf": "df",
        "estado": "Distrito Federal",
        "regiao": "Centro-Oeste",
        "decreto_num": "18955",
        "decreto_ano": "1997",
        "decreto_data": "1997-12-22",
        "titulo": "Decreto nº 18.955, de 22 de dezembro de 1997 (Regulamento do ICMS - RICMS/DF)",
        "lei_base": "Lei Distrital nº 1.254, de 8 de novembro de 1996",
        "orgao": "Governo do Distrito Federal / Secretaria de Estado de Economia (SEEC/DF)",
        "urn_uf": "distrito.federal",
        "aliquota_modal": "20% (elevada de 18% para 20% pela Lei Distrital nº 7.326/2023, vigente desde 22/01/2024)",
        "fcp": "2% (Fundo de Combate e Erradicação da Pobreza do DF - Lei nº 4.220/2008), incidente sobre bebidas alcoólicas, fumo, perfumes/cosméticos, embarcações de esporte.",
        "aliquotas_internas_especificas": "7% (produtos de informática selecionados, cesta básica essencial); 12% (móveis, calçados, vestuário, medicamentos, refeições, carnes e produtos agropecuários); 20% (alíquota geral modal); 25% a 35% + 2% FCP (bebidas alcoólicas, fumo/cigarros, armas).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas do DF para Sul/Sudeste; 7% nas entradas no DF oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 48, II do RICMS/DF e Lei nº 1.254/1996, alterada pela Lei nº 7.109/2022): cálculo por dentro com recomposição pela alíquota interna do DF (20%).",
        "antecipacao_st": "Caderno I do Anexo IV do RICMS/DF (Substituição Tributária) e Antecipação Tributária de ICMS (Art. 320-D do RICMS/DF) nas aquisições interestaduais de mercadorias elencadas.",
        "beneficios_destaque": "Regime Especial de Atacadista do DF (Lei nº 5.005/2012 e Decreto nº 39.753/2019 - apuração por crédito outorgado nas saídas internas e interestaduais) e Emprega-DF / PRÓ-DF II.",
    },
    {
        "uf": "go",
        "estado": "Goiás",
        "regiao": "Centro-Oeste",
        "decreto_num": "4852",
        "decreto_ano": "1997",
        "decreto_data": "1997-12-29",
        "titulo": "Decreto nº 4.852, de 29 de dezembro de 1997 (Regulamento do Código Tributário do Estado de Goiás - RCTE/GO)",
        "lei_base": "Lei Estadual nº 11.651, de 26 de dezembro de 1991 (Código Tributário do Estado de Goiás - CTE/GO)",
        "orgao": "Governo do Estado de Goiás / Secretaria de Estado da Economia (ECONOMIA/GO)",
        "urn_uf": "goias",
        "aliquota_modal": "19% (elevada de 17% para 19% pela Lei nº 22.460/2023, vigente desde 01/04/2024)",
        "fcp": "Até 2% (Fundo de Proteção Social do Estado de Goiás - PROTEGE GOIÁS, Lei nº 14.469/2003), além de contribuição de até 15% ao PROTEGE GOIÁS sobre o valor dos benefícios fiscais fruídos.",
        "aliquotas_internas_especificas": "7% (cesta básica com redução de base de cálculo no Anexo IX do RCTE); 12% (transporte aéreo, insumos selecionados); 17% (energia elétrica e telecomunicações - respeitado o limite da LC 194/2022); 19% (alíquota geral modal); 25% + 2% PROTEGE (bebidas alcoólicas, fumo, perfumes).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas de GO para Sul/Sudeste; 7% nas entradas em GO oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 65, III do RCTE/GO e Art. 20, § 1º-A da Lei nº 11.651/1991): cálculo por dentro com exclusão do ICMS da operação interestadual e inclusão do ICMS interno de 19% na própria base.",
        "antecipacao_st": "Anexo VIII do RCTE/GO (Substituição Tributária). Antecipação de ICMS na entrada interestadual para empresas do Simples Nacional (Decreto nº 9.104/2017 - revogado parcialmente para confeccionistas/calçados, mantido conforme hipóteses específicas).",
        "beneficios_destaque": "PROGOIÁS (Lei nº 20.787/2020 - crédito outorgado de até 67% do saldo devedor de ICMS para indústrias), PRODUZIR / FOMENTAR, Crédito Outorgado para Atacadista/Distribuidor (Anexo IX, art. 11, III do RCTE/GO - crédito outorgado de 3% nas saídas interestaduais tributadas a 12%), e Fundo Estadual de Infraestrutura (FUNDEINFRA - Lei nº 21.670/2022, contribuição sobre commodities agropecuárias e minerais).",
    },
    {
        "uf": "mt",
        "estado": "Mato Grosso",
        "regiao": "Centro-Oeste",
        "decreto_num": "2214",
        "decreto_ano": "2014",
        "decreto_data": "2014-03-27",
        "titulo": "Decreto nº 2.214, de 27 de março de 2014 (Regulamento do ICMS - RICMS/MT)",
        "lei_base": "Lei Estadual nº 7.098, de 30 de dezembro de 1998",
        "orgao": "Governo do Estado de Mato Grosso / Secretaria de Estado de Fazenda (SEFAZ/MT)",
        "urn_uf": "mato.grosso",
        "aliquota_modal": "17%",
        "fcp": "2% (Fundo Estadual de Combate e Erradicação da Pobreza - FECEP/MT, Lei Complementar nº 144/2003), incidente sobre bebidas alcoólicas, fumo, armas, cosméticos/perfumaria e embarcações.",
        "aliquotas_internas_especificas": "7% (cesta básica mato-grossense com redução de base); 12% (transporte, insumos selecionados); 17% (alíquota geral modal, energia elétrica e comunicações); 25% a 35% + 2% FECEP (bebidas alcoólicas, cigarros, armas).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas de MT para Sul/Sudeste; 7% nas entradas em MT oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 72, IX e § 8º do RICMS/MT e Lei nº 7.098/1998, alterada pela Lei nº 11.693/2022): apuração do DIFAL Contribuinte com base dupla por dentro (17%).",
        "antecipacao_st": "Anexo X do RICMS/MT (Substituição Tributária, com transição para o Regime de Estimativa Simplificado / ST reformulada pela LC 631/2019). Exigência de ICMS Garantido / Antecipação em operações interestaduais específicas.",
        "beneficios_destaque": "PRODEIC (Programa de Desenvolvimento Industrial e Comercial de Mato Grosso - LC nº 631/2019), PROAT (Programa de Desenvolvimento do Setor Atacadista), e FETHAB (Fundo Estadual de Transporte e Habitação - Lei nº 7.263/2000, exigido como condição para fruição do diferimento nas operações internas e de exportação de soja, milho, algodão, gado e madeira).",
    },
    {
        "uf": "ms",
        "estado": "Mato Grosso do Sul",
        "regiao": "Centro-Oeste",
        "decreto_num": "9203",
        "decreto_ano": "1998",
        "decreto_data": "1998-09-18",
        "titulo": "Decreto nº 9.203, de 18 de setembro de 1998 (Regulamento do ICMS - RICMS/MS)",
        "lei_base": "Lei Estadual nº 1.810, de 22 de dezembro de 1997 (Código Tributário do Estado de Mato Grosso do Sul)",
        "orgao": "Governo do Estado de Mato Grosso do Sul / Secretaria de Estado de Fazenda (SEFAZ/MS)",
        "urn_uf": "mato.grosso.sul",
        "aliquota_modal": "17%",
        "fcp": "2% (Fundo de Apoio à Comunidade - FAC / FCP-MS, Lei nº 3.337/2006), incidente sobre bebidas alcoólicas, fumo, perfumes e cosméticos.",
        "aliquotas_internas_especificas": "7% (cesta básica sul-mato-grossense com redução de base); 12% (transporte, refeições); 17% (alíquota geral modal, gás natural, energia elétrica e telecomunicações - LC 194/2022); 25% + 2% FCP (bebidas alcoólicas, fumo, cosméticos).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas de MS para Sul/Sudeste; 7% nas entradas em MS oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 21, IV e § 3º da Lei nº 1.810/1997, com redação da Lei nº 5.805/2021): cálculo por dentro com recomposição pela alíquota interna de 17%.",
        "antecipacao_st": "Anexo III do RICMS/MS (Substituição Tributária) e ICMS Equalização Simples Nacional / ICMS Garantido na entrada de mercadorias oriundas de outros estados destinadas à comercialização.",
        "beneficios_destaque": "MS Forte-Indústria (Lei Complementar nº 93/2001 - crédito outorgado/presumido sobre o saldo devedor industrial), Regime Especial para Comércio Atacadista e E-Commerce (Decreto nº 13.275/2011), e FUNDERSUL (Fundo de Desenvolvimento do Sistema Rodoviário do Estado de MS - Lei nº 1.963/1999, condição para diferimento do ICMS em produtos agropecuários).",
    },

    # =========================================================================
    # REGIÃO NORDESTE (BA, PE, CE, MA, PB, RN, AL, SE, PI)
    # =========================================================================
    {
        "uf": "ba",
        "estado": "Bahia",
        "regiao": "Nordeste",
        "decreto_num": "13780",
        "decreto_ano": "2012",
        "decreto_data": "2012-03-16",
        "titulo": "Decreto nº 13.780, de 16 de março de 2012 (Regulamento do ICMS - RICMS/BA)",
        "lei_base": "Lei Estadual nº 7.014, de 4 de dezembro de 1996",
        "orgao": "Governo do Estado da Bahia / Secretaria da Fazenda (SEFAZ/BA)",
        "urn_uf": "bahia",
        "aliquota_modal": "20,5% (elevada de 19% para 20,5% pela Lei nº 14.629/2023, vigente desde 07/02/2024)",
        "fcp": "2% (Fundo Estadual de Combate e Erradicação da Pobreza - FUNCEP/BA, Lei nº 7.988/2001), incidente sobre bebidas alcoólicas, fumo/cigarros, perfumes/cosméticos, embarcações de esporte.",
        "aliquotas_internas_especificas": "7% (alimentos da cesta básica baiana - farinha de mandioca, feijão, arroz, milho, hortifrutigranjeiros); 12% (operações internas com leite, aves, gado, calçados, móveis, artefatos plásticos produzidos na BA); 18% / 20,5% (energia elétrica e telecomunicações até a modal); 20,5% (alíquota geral modal); 27% + 2% FUNCEP = 29% (bebidas alcoólicas, cigarros, ultraleves/iates).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas da BA para Sul/Sudeste; 7% nas entradas na BA oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 17, XI e § 6º da Lei nº 7.014/1996, com redação da Lei nº 14.415/2021): cálculo por dentro com exclusão do ICMS interestadual e inclusão da alíquota interna baiana (20,5%).",
        "antecipacao_st": "Anexo 1 do RICMS/BA (Substituição Tributária) e **Antecipação Parcial do ICMS** (Art. 12-A da Lei nº 7.014/1996 e Art. 321 do RICMS/BA): exigida em TODAS as entradas interestaduais de mercadorias destinadas à comercialização (inclusive de optantes pelo Simples Nacional), correspondente à diferença entre a alíquota interna (ou 12% para Simples com desconto) e a interestadual (4%, 7% ou 12%), sem encerramento da fase de tributação (gera crédito para contribuintes normais).",
        "beneficios_destaque": "DESENVOLVE (Programa de Desenvolvimento Industrial e de Integração Econômica do Estado da Bahia - Lei nº 7.980/2001: dilação de prazo de até 90% do saldo devedor com desconto de até 90% na quitação antecipada), Decreto nº 7.799/2000 (Regime Especial de Atacadista na Bahia com redução de base de cálculo nas saídas internas para que a carga seja de 10%/12% e dispensa parcial de antecipação), e Polo de Informática de Ilhéus (Decreto nº 4.316/1995).",
    },
    {
        "uf": "pe",
        "estado": "Pernambuco",
        "regiao": "Nordeste",
        "decreto_num": "44650",
        "decreto_ano": "2017",
        "decreto_data": "2017-06-30",
        "titulo": "Decreto nº 44.650, de 30 de junho de 2017 (Regulamento do ICMS - RICMS/PE)",
        "lei_base": "Lei Estadual nº 15.730, de 17 de março de 2016",
        "orgao": "Governo do Estado de Pernambuco / Secretaria da Fazenda (SEFAZ/PE)",
        "urn_uf": "pernambuco",
        "aliquota_modal": "20,5% (elevada de 18% para 20,5% pela Lei nº 18.305/2023, vigente desde 01/01/2024)",
        "fcp": "2% (Fundo Estadual de Combate e Erradicação da Pobreza - FECEP/PE, Lei nº 12.523/2003), incidente sobre bebidas alcoólicas, fumo, perfumes/cosméticos, embarcações de recreio.",
        "aliquotas_internas_especificas": "7% (cesta básica pernambucana, gipsita/gesso do Polo Gesseiro do Araripe); 12% (transporte aéreo, veículos novos, refeições, produtos de informática); 20,5% (alíquota geral modal); 25% a 27% + 2% FECEP (bebidas alcoólicas, fumo, armas).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas de PE para Sul/Sudeste; 7% nas entradas em PE oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 12, X e § 1º da Lei nº 15.730/2016, alterada pela Lei nº 17.118/2020): recomposição por dentro pela alíquota interna de 20,5%.",
        "antecipacao_st": "Sistemática de Fronteiras / Antecipação Tributária de Pernambuco (Art. 329 e Anexo 12 do RICMS/PE): cobrança de antecipação parcial ou com liberação nas entradas interestaduais de mercadorias para comercialização ou industrialização (Extrato de Notas Fiscais / Fronteiras PE).",
        "beneficios_destaque": "PRODEPE (Programa de Desenvolvimento do Estado de Pernambuco - Lei nº 11.675/1999: crédito presumido de até 75% a 95% para indústrias, centrais de distribuição e importadores pelo Porto de Suape), PROIND (crédito presumido industrial), PROAT (Atacadistas de alimentos/bebidas/higiene), e Sistemática de Tecidos, Artigos de Armarinho e Confecções (Polo de Confecções do Agreste - Lei nº 12.431/2003).",
    },
    {
        "uf": "ce",
        "estado": "Ceará",
        "regiao": "Nordeste",
        "decreto_num": "33327",
        "decreto_ano": "2019",
        "decreto_data": "2019-10-30",
        "titulo": "Decreto nº 33.327, de 30 de outubro de 2019 (Regulamento do ICMS - RICMS/CE)",
        "lei_base": "Lei Estadual nº 18.665, de 28 de dezembro de 2023 (nova Lei Orgânica do ICMS/CE, sucedendo a Lei nº 12.670/1996)",
        "orgao": "Governo do Estado do Ceará / Secretaria da Fazenda (SEFAZ/CE)",
        "urn_uf": "ceara",
        "aliquota_modal": "20% (elevada de 18% para 20% pela Lei nº 18.305/2023 e mantida na Lei nº 18.665/2023, vigente desde 01/01/2024)",
        "fcp": "2% (Fundo Estadual de Combate à Pobreza - FECOP/CE, Lei Complementar nº 37/2003), incidente sobre bebidas alcoólicas, fumo, perfumes/cosméticos, aviões/iates de recreio.",
        "aliquotas_internas_especificas": "7% (cesta básica com redução de base de cálculo); 12% (serviços de transporte, produtos de informática, móveis, calçados, indústria têxtil local); 18% (energia elétrica e comunicações conforme faixas); 20% (alíquota geral modal); 28% + 2% FECOP = 30% (bebidas alcoólicas, cigarros, armas).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas do CE para Sul/Sudeste; 7% nas entradas no CE oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 29 da Lei nº 18.665/2023): cálculo por dentro com recomposição pela alíquota interna do Ceará (20%).",
        "antecipacao_st": "Regime de **Substituição Tributária por Carga Líquida por CNAE** do Ceará (Lei nº 14.237/2008 e Decretos regulamentadores) e **ICMS Antecipado** na entrada interestadual (Art. 767 do RICMS/CE) cobrado no posto fiscal/SITRAM nas aquisições de outros estados.",
        "beneficios_destaque": "FDI (Fundo de Desenvolvimento Industrial do Ceará - Lei nº 10.367/1979: PROVIN para indústrias e PCDM para centros de distribuição no Porto do Pecém/Mucuripe) e ZPE do Ceará (Zona de Processamento de Exportação de Pecém).",
    },
    {
        "uf": "ma",
        "estado": "Maranhão",
        "regiao": "Nordeste",
        "decreto_num": "19714",
        "decreto_ano": "2003",
        "decreto_data": "2003-07-10",
        "titulo": "Decreto nº 19.714, de 10 de julho de 2003 (Regulamento do ICMS - RICMS/MA)",
        "lei_base": "Lei Estadual nº 7.799, de 19 de dezembro de 2002 (Código Tributário do Estado do Maranhão)",
        "orgao": "Governo do Estado do Maranhão / Secretaria de Estado da Fazenda (SEFAZ/MA)",
        "urn_uf": "maranhao",
        "aliquota_modal": "22% (elevada de 20% para 22% pela Lei nº 12.120/2023, vigente desde 21/02/2024)",
        "fcp": "2% (Fundo Maranhense de Combate à Pobreza - FUMACOP, Lei nº 8.205/2004), incidente sobre bebidas alcoólicas, fumo/cigarros, cosméticos/perfumaria e embarcações.",
        "aliquotas_internas_especificas": "8% / 12% (cesta básica maranhense); 12% (transporte, insumos agrícolas, produtos cerâmicos); 22% (alíquota geral modal); 25% a 28,5% + 2% FUMACOP (bebidas alcoólicas, cigarros, armas).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas do MA para Sul/Sudeste; 7% nas entradas no MA oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 20 da Lei nº 7.799/2002, alterado pela Lei nº 11.662/2022): recomposição por dentro pela alíquota interna de 22%.",
        "antecipacao_st": "Antecipação Parcial do ICMS nas entradas interestaduais para comercialização (diferença entre alíquota interna e interestadual) e Substituição Tributária no Anexo 4.0 do RICMS/MA.",
        "beneficios_destaque": "MAIS EMPRESAS (Programa de Apoio ao Desenvolvimento Industrial do Maranhão - Lei nº 9.121/2010: crédito presumido de até 95% sobre o saldo devedor industrial) e Regime Especial de Atacadista do Maranhão (Lei nº 9.379/2011 - carga tributária líquida reduzida).",
    },
    {
        "uf": "pb",
        "estado": "Paraíba",
        "regiao": "Nordeste",
        "decreto_num": "18930",
        "decreto_ano": "1997",
        "decreto_data": "1997-06-19",
        "titulo": "Decreto nº 18.930, de 19 de junho de 1997 (Regulamento do ICMS - RICMS/PB)",
        "lei_base": "Lei Estadual nº 6.379, de 2 de dezembro de 1996",
        "orgao": "Governo do Estado da Paraíba / Secretaria de Estado da Fazenda (SEFAZ/PB)",
        "urn_uf": "paraiba",
        "aliquota_modal": "20% (elevada de 18% para 20% pela Lei nº 12.788/2023, vigente desde 01/01/2024)",
        "fcp": "2% (Fundo de Combate e Erradicação da Pobreza no Estado da Paraíba - FUNCEP/PB, Lei nº 7.611/2004), incidente sobre bebidas alcoólicas, fumo, perfumes e embarcações.",
        "aliquotas_internas_especificas": "7% / 12% (cesta básica paraibana); 18% (energia elétrica e telecomunicações até a faixa legal); 20% (alíquota geral modal); 25% a 27% + 2% FUNCEP (bebidas alcoólicas, fumo/cigarros).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas da PB para Sul/Sudeste; 7% nas entradas na PB oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 14 da Lei nº 6.379/1996, alterada pela Lei nº 12.190/2022): recomposição por dentro pela alíquota interna de 20%.",
        "antecipacao_st": "Cobrança de ICMS Garantido / Antecipado nas entradas interestaduais de mercadorias destinadas a comercialização (Art. 106, II, 'c' e 'g' do RICMS/PB) e Anexo 05 (Substituição Tributária).",
        "beneficios_destaque": "FAIN (Fundo de Apoio ao Desenvolvimento Industrial da Paraíba - crédito presumido industrial de até 74,25%) e Regime Especial de Tributação para Atacadistas e Distribuidores.",
    },
    {
        "uf": "rn",
        "estado": "Rio Grande do Norte",
        "regiao": "Nordeste",
        "decreto_num": "31825",
        "decreto_ano": "2022",
        "decreto_data": "2022-08-18",
        "titulo": "Decreto nº 31.825, de 18 de agosto de 2022 (Novo Regulamento do ICMS - RICMS/RN)",
        "lei_base": "Lei Estadual nº 6.968, de 30 de dezembro de 1996",
        "orgao": "Governo do Estado do Rio Grande do Norte / Secretaria de Estado da Fazenda (SEFAZ/RN)",
        "urn_uf": "rio.grande.norte",
        "aliquota_modal": "18% (retornou a 18% em 01/01/2024 após vigência temporária de 20% em 2023)",
        "fcp": "2% (Fundo Estadual de Combate à Pobreza - FECOP/RN, Lei Complementar nº 261/2003), incidente sobre bebidas alcoólicas, fumo, perfumes/cosméticos e embarcações.",
        "aliquotas_internas_especificas": "7% / 12% (cesta básica potiguar, sal marinho, carcinicultura); 18% (alíquota geral modal, energia elétrica e comunicações); 25% a 27% + 2% FECOP (bebidas alcoólicas, fumo, cosméticos).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas do RN para Sul/Sudeste; 7% nas entradas no RN oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 20 da Lei nº 6.968/1996, alterada pela Lei nº 11.044/2021): cálculo por dentro com recomposição pela alíquota interna de 18%.",
        "antecipacao_st": "Antecipação Tributária na entrada interestadual de mercadorias para comercialização (Art. 556 do Novo RICMS/RN - Decreto nº 31.825/2022) e Anexo 19 (Substituição Tributária).",
        "beneficios_destaque": "PROEDI (Programa de Estímulo ao Desenvolvimento Industrial do RN - Decreto nº 29.030/2019: crédito presumido de 75% a 95% sobre o saldo devedor de ICMS) e Regime Especial de Atacadista do RN.",
    },
    {
        "uf": "al",
        "estado": "Alagoas",
        "regiao": "Nordeste",
        "decreto_num": "35245",
        "decreto_ano": "1991",
        "decreto_data": "1991-12-26",
        "titulo": "Decreto nº 35.245, de 26 de dezembro de 1991 (Regulamento do ICMS - RICMS/AL)",
        "lei_base": "Lei Estadual nº 5.900, de 27 de dezembro de 1996",
        "orgao": "Governo do Estado de Alagoas / Secretaria de Estado da Fazenda (SEFAZ/AL)",
        "urn_uf": "alagoas",
        "aliquota_modal": "19% + 1% de FECOEP = 20% de carga efetiva modal (Lei nº 8.779/2022)",
        "fcp": "1% em regra geral sobre todas as operações internas e de importação sujeitas à alíquota modal, e 2% sobre supérfluos, bebidas alcoólicas, fumo e cosméticos (Fundo Estadual de Combate e Erradicação da Pobreza - FECOEP/AL, Lei nº 6.558/2004).",
        "aliquotas_internas_especificas": "7% (cesta básica alagoana); 12% (transporte, insumos agrícolas, produtos cerâmicos); 19% + 1% FECOEP = 20% (alíquota geral modal); 27% + 2% FECOEP = 29% (bebidas alcoólicas, fumo, perfumes).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas de AL para Sul/Sudeste; 7% nas entradas em AL oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 21 da Lei nº 5.900/1996, alterada pela Lei nº 8.567/2021): recomposição por dentro pela alíquota interna de Alagoas (19% + 1% FECOEP).",
        "antecipacao_st": "Antecipação do ICMS na entrada interestadual (Art. 591-A do RICMS/AL - diferença entre alíquota interna e interestadual) e Anexo II (Substituição Tributária).",
        "beneficios_destaque": "PRODESIN (Programa de Desenvolvimento Integrado do Estado de Alagoas - Lei nº 5.671/1995: incentivo fiscal industrial, central de distribuição e sistemática de importação por conta e ordem com quitação via precatórios/créditos judiciais nos termos da legislação estadual e convalidação CONFAZ) e Regime Especial de Atacadista (Decreto nº 20.747/2012).",
    },
    {
        "uf": "se",
        "estado": "Sergipe",
        "regiao": "Nordeste",
        "decreto_num": "21400",
        "decreto_ano": "2002",
        "decreto_data": "2002-12-10",
        "titulo": "Decreto nº 21.400, de 10 de dezembro de 2002 (Regulamento do ICMS - RICMS/SE)",
        "lei_base": "Lei Estadual nº 3.796, de 26 de dezembro de 1996",
        "orgao": "Governo do Estado de Sergipe / Secretaria de Estado da Fazenda (SEFAZ/SE)",
        "urn_uf": "sergipe",
        "aliquota_modal": "19% + 1% de FECOEP = 20% de carga efetiva modal (Lei nº 9.391/2023, vigente desde 2024)",
        "fcp": "1% sobre as operações internas em geral e 2% sobre supérfluos, bebidas alcoólicas, fumo e cosméticos (Fundo Estadual de Combate e Erradicação da Pobreza - FECOEP/SE, Lei nº 4.731/2002).",
        "aliquotas_internas_especificas": "7% / 12% (cesta básica sergipana); 19% + 1% FECOEP = 20% (alíquota geral modal); 25% a 27% + 2% FECOEP (bebidas alcoólicas, fumo, cosméticos).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas de SE para Sul/Sudeste; 7% nas entradas em SE oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 13 da Lei nº 3.796/1996, alterada pela Lei nº 8.952/2021): cálculo por dentro com recomposição pela alíquota interna sergipana.",
        "antecipacao_st": "Antecipação Tributária com e sem encerramento de fase nas entradas interestaduais (Art. 783 do RICMS/SE) e Anexo IX (Substituição Tributária).",
        "beneficios_destaque": "PSDI (Programa Sergipano de Desenvolvimento Industrial - Lei nº 3.140/1991: recolhimento reduzido a até 6,2%/8% do ICMS devido para empreendimentos industriais).",
    },
    {
        "uf": "pi",
        "estado": "Piauí",
        "regiao": "Nordeste",
        "decreto_num": "21866",
        "decreto_ano": "2023",
        "decreto_data": "2023-03-06",
        "titulo": "Decreto nº 21.866, de 6 de março de 2023 (Novo Regulamento do ICMS - RICMS/PI)",
        "lei_base": "Lei Estadual nº 4.257, de 6 de janeiro de 1989",
        "orgao": "Governo do Estado do Piauí / Secretaria de Estado da Fazenda (SEFAZ/PI)",
        "urn_uf": "piaui",
        "aliquota_modal": "21% (elevada de 18% para 21% pela Lei Complementar nº 269/2022, vigente desde 2023/2024)",
        "fcp": "2% (Fundo Estadual de Combate à Pobreza - FECOP/PI, Lei nº 5.622/2006), incidente sobre bebidas alcoólicas, refrigerantes, fumo, cosméticos e embarcações.",
        "aliquotas_internas_especificas": "7% / 12% (cesta básica piauiense); 18% (energia elétrica residencial até limite e comunicações); 21% (alíquota geral modal); 25% a 29% + 2% FECOP (bebidas alcoólicas, fumo).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas do PI para Sul/Sudeste; 7% nas entradas no PI oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 24 da Lei nº 4.257/1989): recomposição por dentro pela alíquota interna de 21%.",
        "antecipacao_st": "Antecipação Parcial do ICMS nas entradas interestaduais de mercadorias destinadas à comercialização (inclusive Simples Nacional) e Substituição Tributária no Anexo X do Novo RICMS/PI.",
        "beneficios_destaque": "Lei nº 6.146/2011 (Incentivos Fiscais para Empreendimentos Industriais no Piauí - dispensa de 60% a 100% do ICMS apurado) e Regime Especial Atacadista do Piauí.",
    },

    # =========================================================================
    # REGIÃO NORTE (PA, AM, RO, TO, AC, AP, RR)
    # =========================================================================
    {
        "uf": "pa",
        "estado": "Pará",
        "regiao": "Norte",
        "decreto_num": "4676",
        "decreto_ano": "2001",
        "decreto_data": "2001-06-18",
        "titulo": "Decreto nº 4.676, de 18 de junho de 2001 (Regulamento do ICMS - RICMS/PA)",
        "lei_base": "Lei Estadual nº 5.530, de 13 de janeiro de 1989",
        "orgao": "Governo do Estado do Pará / Secretaria de Estado da Fazenda (SEFA/PA)",
        "urn_uf": "para",
        "aliquota_modal": "19% (elevada de 17% para 19% pela Lei nº 9.755/2022, vigente desde 2023/2024)",
        "fcp": "Pará não cobra adicional geral de FCP sobre o ICMS (0%).",
        "aliquotas_internas_especificas": "7% / 12% (cesta básica paraense, farinha de mandioca, açaí nas hipóteses regulamentadas); 17% (energia elétrica e telecomunicações - LC 194/2022); 19% (alíquota geral modal); 25% a 30% (bebidas alcoólicas, fumo/cigarros, supérfluos).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas do PA para Sul/Sudeste; 7% nas entradas no PA oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 12 da Lei nº 5.530/1989, alterada pela Lei nº 8.870/2019 e Lei nº 9.541/2022): cálculo por dentro com recomposição pela alíquota interna do Pará (19%).",
        "antecipacao_st": "Apêndice I do RICMS/PA (Antecipação Especial do ICMS na entrada no território paraense de mercadorias procedentes de outra UF) e Anexo XIII (Substituição Tributária).",
        "beneficios_destaque": "Política de Incentivos ao Desenvolvimento Socioeconômico do Estado do Pará (Lei nº 6.489/2002 - crédito presumido industrial, agroindustrial e mineral) e Regime Tributário Diferenciado para Atacadistas no Pará.",
    },
    {
        "uf": "am",
        "estado": "Amazonas",
        "regiao": "Norte",
        "decreto_num": "20686",
        "decreto_ano": "1999",
        "decreto_data": "1999-12-28",
        "titulo": "Decreto nº 20.686, de 28 de dezembro de 1999 (Regulamento do ICMS - RICMS/AM)",
        "lei_base": "Lei Complementar Estadual nº 19, de 29 de dezembro de 1997 (Código Tributário do Estado do Amazonas)",
        "orgao": "Governo do Estado do Amazonas / Secretaria de Estado da Fazenda (SEFAZ/AM)",
        "urn_uf": "amazonas",
        "aliquota_modal": "20% (elevada de 18% para 20% pela Lei Complementar nº 242/2022, vigente desde 2023/2024)",
        "fcp": "Até 2% (Fundo de Promoção Social e Erradicação da Pobreza - FPS/AM, Lei nº 3.584/2010), incidente sobre bebidas alcoólicas, fumo, armas e embarcações.",
        "aliquotas_internas_especificas": "7% (cesta básica amazonense e produtos industrializados na Zona Franca de Manaus em operações internas específicas); 12% (transporte aéreo, refeições); 18% (energia elétrica e comunicações); 20% (alíquota geral modal); 25% + FPS (bebidas alcoólicas, fumo, supérfluos).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas do AM para Sul/Sudeste; 7% nas entradas no AM oriundas de SP, RJ, MG, PR, SC e RS (com **isenção na origem e crédito presumido de 7% ou 12% no destino** quando destinado à **Zona Franca de Manaus** — Manaus, Rio Preto da Eva e Presidente Figueiredo — ou à **ALC Tabatinga**, nos termos do Decreto-Lei nº 288/1967 e Convênios ICM 65/1988, ICMS 52/1992 e ICMS 134/2019!).",
        "aliquota_inter_importados": "4% nas saídas de bens importados sem industrialização; 12% nas saídas interestaduais de bens industrializados na Zona Franca de Manaus conforme Processo Produtivo Básico (PPB - art. 1º, § 4º, II da Resolução SF nº 13/2012, que excetua da alíquota de 4% os bens produzidos em conformidade com o PPB na ZFM!).",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 13 da LC nº 19/1997, alterada pela LC nº 219/2021): cálculo por dentro com recomposição pela alíquota interna de 20%.",
        "antecipacao_st": "Cobrança de **Antecipação do ICMS e Substituição Tributária** no desembaraço eletrônico de documentos fiscais de entrada (DT-e SEFAZ/AM - Art. 107 do RICMS/AM), e crédito fiscal presumido de igual valor ao imposto desonerado nas entradas incentivadas da ZFM (art. 49 do Decreto-Lei nº 288/1967).",
        "beneficios_destaque": "Polo Industrial de Manaus (PIM / Zona Franca de Manaus - Lei Estadual nº 2.826/2003: crédito estímulo de ICMS de 55% a 100% para indústrias incentivadas com projeto aprovado na SUFRAMA/CODAM, diferimento na importação de insumos do exterior e isenção/crédito presumido nas compras nacionais pelo Convênio ICM 65/1988), e Corredor de Importação do Amazonas (Lei nº 3.830/2012).",
    },
    {
        "uf": "ro",
        "estado": "Rondônia",
        "regiao": "Norte",
        "decreto_num": "22721",
        "decreto_ano": "2018",
        "decreto_data": "2018-04-05",
        "titulo": "Decreto nº 22.721, de 5 de abril de 2018 (Regulamento do ICMS - RICMS/RO)",
        "lei_base": "Lei Estadual nº 688, de 27 de dezembro de 1996",
        "orgao": "Governo do Estado de Rondônia / Secretaria de Estado de Finanças (SEFIN/RO)",
        "urn_uf": "rondonia",
        "aliquota_modal": "19,5% (elevada de 17,5% para 19,5% pela Lei nº 5.629/2023, vigente desde 12/01/2024)",
        "fcp": "2% (Fundo Estadual de Combate e Erradicação da Pobreza de Rondônia - FECOEP/RO, Lei Complementar nº 842/2015), incidente sobre bebidas alcoólicas, cigarros/fumo, perfumes e armas.",
        "aliquotas_internas_especificas": "12% (cesta básica rondoniense, carnes, gado em pé, transporte); 17,5% (energia elétrica e telecomunicações); 19,5% (alíquota geral modal); 25% a 35% + 2% FECOEP (bebidas alcoólicas, fumo/cigarros, armas).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas de RO para Sul/Sudeste; 7% nas entradas em RO oriundas de SP, RJ, MG, PR, SC e RS (com isenção/abatimento do Convênio ICMS 52/1992 nas remessas de produtos industrializados nacionais destinados à **Área de Livre Comércio de Guajará-Mirim - ALC Guajará-Mirim**).",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 18 da Lei nº 688/1996, alterada pela Lei nº 5.298/2022): cálculo por dentro com recomposição pela alíquota interna de 19,5%.",
        "antecipacao_st": "Anexo VI do RICMS/RO (Substituição Tributária) e **Anexo VII (Antecipação do Imposto sem Encerramento de Fase de Tributação)** exigida na entrada de mercadorias oriundas de outra UF no Posto Fiscal de Fronteira (Portal Fisconforme SEFIN/RO).",
        "beneficios_destaque": "CONDER (Conselho de Desenvolvimento do Estado de Rondônia - Lei Complementar nº 61/1992: incentivo tributário de até 85% do ICMS para indústrias e agroindústrias), Crédito Presumido nas Saídas Interestaduais de Mercadorias Importadas (Lei nº 1.473/2005), e ALC de Guajará-Mirim.",
    },
    {
        "uf": "to",
        "estado": "Tocantins",
        "regiao": "Norte",
        "decreto_num": "2912",
        "decreto_ano": "2006",
        "decreto_data": "2006-12-29",
        "titulo": "Decreto nº 2.912, de 29 de dezembro de 2006 (Regulamento do ICMS - RICMS/TO)",
        "lei_base": "Lei Estadual nº 1.287, de 28 de dezembro de 2001 (Código Tributário do Estado do Tocantins)",
        "orgao": "Governo do Estado do Tocantins / Secretaria da Fazenda (SEFAZ/TO)",
        "urn_uf": "tocantins",
        "aliquota_modal": "20% (elevada de 18% para 20% pela Medida Provisória nº 33/2022 convertida na Lei nº 4.141/2023)",
        "fcp": "2% (Fundo Estadual de Combate e Erradicação da Pobreza - FECOEP/TO, Lei nº 3.015/2015), incidente sobre bebidas alcoólicas, fumo, perfumes/cosméticos e embarcações.",
        "aliquotas_internas_especificas": "12% (cesta básica tocantinense com redução de base, transporte); 18% (energia elétrica e telecomunicações); 20% (alíquota geral modal); 25% + 2% FECOEP = 27% (bebidas alcoólicas, fumo, supérfluos).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas de TO para Sul/Sudeste; 7% nas entradas em TO oriundas de SP, RJ, MG, PR, SC e RS.",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 22 da Lei nº 1.287/2001, alterada pela Lei nº 3.890/2022): cálculo por dentro com recomposição pela alíquota interna de 20%.",
        "antecipacao_st": "Anexo XXI do RICMS/TO (Substituição Tributária) e Complementação de Alíquota / Antecipação nas entradas interestaduais para comercialização por empresas do Simples Nacional.",
        "beneficios_destaque": "PROINDÚSTRIA (Lei nº 1.385/2003), PROSPERAR, e Lei nº 1.201/2000 (Comércio Atacadista e E-Commerce / Vendas Não Presenciais no Tocantins com carga tributária efetiva de 1% a 2% nas saídas interestaduais).",
    },
    {
        "uf": "ac",
        "estado": "Acre",
        "regiao": "Norte",
        "decreto_num": "008",
        "decreto_ano": "1998",
        "decreto_data": "1998-01-26",
        "titulo": "Decreto nº 008, de 26 de janeiro de 1998 (Regulamento do ICMS - RICMS/AC)",
        "lei_base": "Lei Complementar Estadual nº 55, de 9 de julho de 1997",
        "orgao": "Governo do Estado do Acre / Secretaria de Estado da Fazenda (SEFAZ/AC)",
        "urn_uf": "acre",
        "aliquota_modal": "19% (elevada de 17% para 19% pela Lei Complementar nº 423/2022, vigente desde 01/04/2023)",
        "fcp": "Acre não aplica adicional separado na alíquota modal (incorporado nos percentuais específicos).",
        "aliquotas_internas_especificas": "7% / 12% (cesta básica acreana); 17% (energia elétrica e telecomunicações - LC 194/2022); 19% (alíquota geral modal); 25% a 33% (bebidas alcoólicas, fumo/cigarros, supérfluos).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas do AC para Sul/Sudeste; 7% nas entradas no AC oriundas de SP, RJ, MG, PR, SC e RS (com isenção/abatimento do Convênio ICMS 52/1992 nas remessas de produtos industrializados nacionais destinados às **Áreas de Livre Comércio de Brasiléia, Epitaciolândia e Cruzeiro do Sul**).",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Art. 6º da LC nº 55/1997, alterada pela LC nº 396/2022): cálculo por dentro com recomposição pela alíquota interna de 19%.",
        "antecipacao_st": "Cobrança de **Antecipação Tributária** (com e sem encerramento de tributação - Art. 96 do RICMS/AC) no ingresso de mercadorias procedentes de outras UFs no Estado do Acre.",
        "beneficios_destaque": "COPIAI (Comissão da Política de Incentivos às Atividades Industriais do Estado do Acre - Lei nº 1.358/2000: financiamento/incentivo de até 85% a 95% do ICMS industrial) e ALCs de Brasiléia/Epitaciolândia e Cruzeiro do Sul.",
    },
    {
        "uf": "ap",
        "estado": "Amapá",
        "regiao": "Norte",
        "decreto_num": "2269",
        "decreto_ano": "1998",
        "decreto_data": "1998-07-24",
        "titulo": "Decreto nº 2.269, de 24 de julho de 1998 (Regulamento do ICMS - RICMS/AP)",
        "lei_base": "Lei Estadual nº 400, de 22 de dezembro de 1997 (Código Tributário do Estado do Amapá)",
        "orgao": "Governo do Estado do Amapá / Secretaria de Estado da Fazenda (SEFAZ/AP)",
        "urn_uf": "amapa",
        "aliquota_modal": "18%",
        "fcp": "Amapá não cobra adicional separado na alíquota modal.",
        "aliquotas_internas_especificas": "7% / 12% (cesta básica amapaense); 18% (alíquota geral modal, energia elétrica e comunicações); 25% a 29% (bebidas alcoólicas, fumo/cigarros, joias, armas).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas do AP para Sul/Sudeste; 7% nas entradas no AP oriundas de SP, RJ, MG, PR, SC e RS (com isenção/abatimento do Convênio ICMS 52/1992 nas remessas de produtos industrializados nacionais destinados à **Área de Livre Comércio de Macapá e Santana - ALCMS**).",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Lei nº 400/1997, alterada pela Lei nº 2.662/2022): cálculo por dentro com recomposição pela alíquota interna de 18%.",
        "antecipacao_st": "Antecipação do ICMS na entrada interestadual para comercialização e Anexo III do RICMS/AP (Substituição Tributária).",
        "beneficios_destaque": "Área de Livre Comércio de Macapá e Santana (ALCMS - Lei Federal nº 8.387/1991, art. 11 e Convênio ICMS 52/1992: isenção de ICMS e IPI nas remessas nacionais e suspensão/isenção na importação para consumo interno na ALCMS) e Selo Verde Amapá.",
    },
    {
        "uf": "rr",
        "estado": "Roraima",
        "regiao": "Norte",
        "decreto_num": "4335",
        "decreto_ano": "2001",
        "decreto_data": "2001-08-03",
        "titulo": "Decreto nº 4.335-E, de 3 de agosto de 2001 (Regulamento do ICMS - RICMS/RR)",
        "lei_base": "Lei Estadual nº 59, de 28 de dezembro de 1993 (Código Tributário do Estado de Roraima)",
        "orgao": "Governo do Estado de Roraima / Secretaria de Estado da Fazenda (SEFAZ/RR)",
        "urn_uf": "roraima",
        "aliquota_modal": "20% (elevada de 17% para 20% pela Lei nº 1.767/2022, vigente desde 2023/2024)",
        "fcp": "Roraima não cobra adicional separado na alíquota modal.",
        "aliquotas_internas_especificas": "7% / 12% (cesta básica roraimense); 17% (energia elétrica e telecomunicações - LC 194/2022); 20% (alíquota geral modal); 25% a 28% (bebidas alcoólicas, fumo/cigarros, armas).",
        "aliquota_inter_saida_n_ne_co_es": "12% (Resolução SF nº 22/1989)",
        "aliquota_inter_saida_s_se": "12% nas saídas de RR para Sul/Sudeste; 7% nas entradas em RR oriundas de SP, RJ, MG, PR, SC e RS (com isenção/abatimento do Convênio ICMS 52/1992 nas remessas de produtos industrializados nacionais destinados às **Áreas de Livre Comércio de Boa Vista e Bonfim - ALC Boa Vista/Bonfim**).",
        "aliquota_inter_importados": "4% (Resolução SF nº 13/2012)",
        "metodologia_difal_contribuinte": "Base Dupla / Cálculo 'por dentro' (Lei nº 59/1993, alterada pela Lei nº 1.640/2022): cálculo por dentro com recomposição pela alíquota interna de 20%.",
        "antecipacao_st": "Cobrança de **Diferencial de Alíquota de Fronteira / Antecipação** (Art. 75 do RICMS/RR) no ingresso de mercadorias no Posto Fiscal do Jundiá (divisa AM/RR) e Substituição Tributária.",
        "beneficios_destaque": "Áreas de Livre Comércio de Boa Vista e Bonfim (Lei Federal nº 8.256/1991 e Convênio ICMS 52/1992 - isenção de ICMS e IPI nas aquisições nacionais de industrializados com internamento SUFRAMA e crédito presumido na entrada) e Lei nº 215/1998 (Incentivos Agroindustriais e Florestais).",
    },
]

def montar_corpo_ricms(d: dict) -> str:
    slug_uf = d["uf"].upper()
    return f"""# {d['titulo']}

DECRETO Nº {d['decreto_num']}, DE {d['decreto_ano']} — REGULAMENTO DO ICMS DO ESTADO DE {d['estado'].upper()} (RICMS/{slug_uf})

Regulamenta o Imposto sobre Operações Relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação (ICMS) no Estado de {d['estado']}, instituído pela {d['lei_base']}.

O GOVERNADOR DO ESTADO DE {d['estado'].upper()}, no uso de suas atribuições constitucionais e tendo em vista o disposto na {d['lei_base']} e na Lei Complementar Federal nº 87, de 13 de setembro de 1996 (Lei Kandir), DECRETA:

## TÍTULO I — DA INCIDÊNCIA, DO FATO GERADOR E DA NÃO INCIDÊNCIA

**Art. 1º** O Imposto sobre Operações Relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação (ICMS), de competência do Estado de {d['estado']} ({slug_uf}), rege-se pelas normas da {d['lei_base']} e pelas disposições deste Regulamento (RICMS/{slug_uf}).

**Art. 2º** O imposto incide sobre:
I — operações relativas à circulação de mercadorias, inclusive o fornecimento de alimentação e bebidas em bares, restaurantes e estabelecimentos similares;
II — prestações de serviços de transporte interestadual e intermunicipal, por qualquer via, de pessoas, bens, mercadorias ou valores;
III — prestações onerosas de serviços de comunicação, por qualquer meio;
IV — entrada de mercadoria ou bem importados do exterior, por pessoa física ou jurídica, ainda que não seja contribuinte habitual do imposto, qualquer que seja a sua finalidade;
V — entrada, no território do Estado de {d['estado']}, de mercadoria ou bem oriundos de outra unidade da Federação, destinados a uso, consumo ou ativo permanente de contribuinte do imposto;
VI — operações e prestações iniciadas em outra unidade da Federação que destinem bens e serviços a consumidor final, contribuinte ou não do imposto, localizado no Estado de {d['estado']}.

**Art. 3º** O imposto não incide sobre:
I — operações e prestações que destinem ao exterior mercadorias, inclusive produtos primários e produtos industrializados semi-elaborados, ou serviços (assegurada a manutenção e o aproveitamento do montante do imposto cobrado nas operações e prestações anteriores);
II — operações interestaduais relativas a energia elétrica e petróleo, inclusive lubrificantes e combustíveis líquidos e gasosos dele derivados, quando destinados à industrialização ou à comercialização;
III — operações com ouro, quando definido em lei como ativo financeiro ou instrumento cambial;
IV — operações com livros, jornais, periódicos e o papel destinado a sua impressão;
V — saída física de mercadoria de um estabelecimento para outro de **mesma titularidade** (transferência interna ou interestadual entre matriz e filial), nos termos do § 4º do art. 12 da Lei Complementar nº 87/1996 (incluído pela Lei Complementar nº 204/2023) e do Convênio ICMS nº 109/2024.

---

## TÍTULO II — DAS ALÍQUOTAS INTERNAS E INTERESTADUAIS EM {d['estado'].upper()} ({slug_uf})

### 1. Quadro Geral de Alíquotas ({slug_uf})

| Modalidade da Operação / Prestação | Alíquota Aplicável em {slug_uf} | Fundamento Legal |
| :--- | :--- | :--- |
| **Alíquota Interna Modal (Regra Geral)** | **{d['aliquota_modal']}** | {d['lei_base']} e RICMS/{slug_uf} |
| **Fundo de Combate à Pobreza (FCP)** | {d['fcp']} | Art. 82, § 1º do ADCT e Legislação Estadual |
| **Saída Interestadual para N, NE, CO e ES** | **{d['aliquota_inter_saida_n_ne_co_es']}** | Resolução do Senado Federal nº 22/1989 |
| **Saída / Entrada Interestadual com Sul e Sudeste** | **{d['aliquota_inter_saida_s_se']}** | Resolução do Senado Federal nº 22/1989 |
| **Saída Interestadual de Bens Importados (Conteúdo de Importação > 40%)** | **{d['aliquota_inter_importados']}** | Resolução do Senado Federal nº 13/2012 e Convênio ICMS 38/2013 |
| **Transporte Aéreo Interestadual (Passageiros, Carga e Mala Postal)** | **4%** | Resolução do Senado Federal nº 95/1996 |

### 2. Alíquotas Internas Seletivas e Diferenciadas ({slug_uf})
- **Detalhamento Setorial:** {d['aliquotas_internas_especificas']}
- **Combustíveis (Regime Monofásico Nacional - LC 192/2022):** Alíquotas específicas (*ad rem*, por litro ou quilograma) uniformes em todo o território nacional para gasolina, etanol anidro (EAC), óleo diesel, biodiesel (B100) e GLP, fixadas pelos Convênios ICMS nº 199/2022 e nº 15/2023.

---

## TÍTULO III — DAS REGRAS INTERESTADUAIS: DIFAL, ANTECIPAÇÃO, ICMS-ST E TRANSFERÊNCIAS

### 1. Diferencial de Alíquotas (DIFAL) nas Entradas Interestaduais em {slug_uf}
1. **DIFAL Contribuinte (Aquisição Interestadual para Uso, Consumo ou Ativo Imobilizado):**
   - **Metodologia de Cálculo em {slug_uf}:** {d['metodologia_difal_contribuinte']}
   - **Responsável pelo Recolhimento:** O estabelecimento destinatário contribuinte localizado no Estado de {d['estado']}, exceto quando a mercadoria estiver sujeita a protocolo/convênio de substituição tributária com cláusula expressa de retenção do diferencial pelo remetente de outra UF (DIFAL-ST).
2. **DIFAL Não Contribuinte (EC 87/2015, LC 190/2022 e Convênio ICMS 236/2021):**
   - Nas vendas e prestações interestaduais destinadas a consumidor final não contribuinte do ICMS localizado no Estado de {d['estado']} (CFOP `6.107` ou `6.108`), o remetente de outra UF deve destacar o ICMS de origem pela alíquota interestadual (4%, 7% ou 12%) e recolher ao Estado de {d['estado']} (via GNRE ou apuração mensal de inscrito substituto) a diferença entre a alíquota interna vigente em {slug_uf} (acrescida do FCP, quando cabível) e a alíquota interestadual, utilizando base única com o ICMS interno de {slug_uf} integrado.

### 2. Substituição Tributária (ICMS-ST) e Antecipação na Entrada Interestadual
- **Regra Estadual ({slug_uf}):** {d['antecipacao_st']}
- **Cálculo da MVA Ajustada nas Operações Interestaduais entre Contribuintes Normais (Convênio ICMS 142/2018):**
  $$\\text{{MVA Ajustada}} = \\left[ \\frac{{(1 + \\text{{MVA-ST Original}}) \\times (1 - \\text{{ALQ Inter}})}}{{(1 - \\text{{ALQ Intra}})}} \\right] - 1$$
- **Remetente Optante pelo Simples Nacional (Convênio ICMS 35/2011):** Quando o remetente em outra UF for optante pelo Simples Nacional, **não se aplica a MVA Ajustada**, utilizando-se a **MVA-ST Original** prevista na legislação de {slug_uf}.

### 3. Transferências Interestaduais entre Estabelecimentos do Mesmo Titular (LC 204/2023 e Convênio ICMS 109/2024)
- Nas remessas interestaduais de mercadorias entre estabelecimentos pertencentes ao mesmo titular (CFOP `6.151`/`6.152` na saída e `2.151`/`2.152` na entrada), não ocorre fato gerador de ICMS, sendo assegurada a transferência de crédito ao estabelecimento destinatário limitado aos percentuais das alíquotas interestaduais (4%, 7% ou 12%) sobre o custo de produção ou valor médio de entrada em estoque, ou, alternativamente, mediante opção anual registrada no RUDFTO, a equiparação a operação regularmente tributada (Cláusula sexta do Convênio ICMS 109/2024).

---

## TÍTULO IV — BENEFÍCIOS FISCAIS E REGIMES ESPECIAIS EM {d['estado'].upper()} ({slug_uf})

- **Principais Regimes e Incentivos Estaduais ({slug_uf}):** {d['beneficios_destaque']}
- **Convalidação Nacional:** Os benefícios fiscais e financeiro-fiscais concedidos pelo Estado de {d['estado']} devidamente publicados, registrados e depositados perante a Secretaria Executiva do CONFAZ nos termos da Lei Complementar nº 160/2017 e do Convênio ICMS nº 190/2017 garantem a integralidade do crédito fiscal de ICMS destacado na nota fiscal ao adquirente localizado em qualquer outra unidade da Federação."""

def main():
    auditor = AgenteAuditor()
    salvos = []

    for d in UFS_RICMS:
        fonte_urn = f"https://normas.leg.br/?urn=urn:lex:br;{d['urn_uf']}:estadual:decreto:{d['decreto_data']};{d['decreto_num']}"
        meta = {
            "titulo": d["titulo"],
            "esfera": "Estadual",
            "orgao": d["orgao"],
            "tipo": "Decreto Estadual",
            "numero": d["decreto_num"],
            "ano": d["decreto_ano"],
            "data": d["decreto_data"],
            "tema_tributario": "Produtos e Mercadorias",
            "tributos_afetados": ["ICMS", "ICMS-ST"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": fonte_urn,
            "ementa": f"Aprova o Regulamento do Imposto sobre Operações Relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação do Estado de {d['estado']} (RICMS/{d['uf'].upper()}), disciplinando alíquotas internas ({d['aliquota_modal']}), DIFAL, antecipação tributária, substituição tributária e operações interestaduais.",
        }

        corpo = montar_corpo_ricms(d)
        conteudo = f"{gerar_frontmatter(meta)}{corpo}\n"
        slug = f"decreto-{d['decreto_num']}-{d['decreto_ano']}.md"
        if d["uf"] == "es":
            slug = "decreto-1090-r-2002.md"
        elif d["uf"] == "rr":
            slug = "decreto-4335-e-2001.md"

        caminho = RAIZ / "estaduais" / d["uf"] / "ricms" / slug
        salvar_atomico(caminho, conteudo.encode("utf-8"))
        valido, erros = auditor.auditar_documento(caminho, checar_rede=False)
        if not valido:
            print(f"[ERRO SCHEMA] {caminho}: {erros}")
        else:
            salvos.append(caminho)

    print(f"[Wave 2] {len(salvos)}/{len(UFS_RICMS)} RICMS estaduais gerados e validados com sucesso!")

if __name__ == "__main__":
    main()
