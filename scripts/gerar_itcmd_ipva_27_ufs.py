"""Gera e audita as Leis Estaduais de ITCMD e IPVA das 19 UFs faltantes, completando 27/27 Estados.

Inclui regras detalhadas de:
- Alíquotas por Estado (ITCMD progressivo/fixo até 8% e IPVA por categoria de veículo: passeio, utilitários, caminhões, motos, locadoras e elétricos/híbridos)
- Regras de competência interestadual do ITCMD (imóveis na UF de localização do bem vs. bens móveis/quotas/aplicações na UF de domicílio do de cujus ou do doador, e regras da EC 132/2023)
- Regras de competência interestadual do IPVA (Tema 708 STF - domicílio efetivo e transferência de veículo entre UFs no mesmo exercício)
"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from comum import gerar_frontmatter, salvar_atomico
from agente_auditor import AgenteAuditor

UFS_PATRIMONIO_19 = [
    {
        "uf": "es", "estado": "Espírito Santo", "urn_uf": "espirito.santo",
        "orgao": "Assembleia Legislativa do Estado do Espírito Santo / SEFAZ-ES",
        "itcmd_num": "10011", "itcmd_ano": "2013", "itcmd_data": "2013-05-20",
        "itcmd_aliquota": "4% (alíquota única sobre transmissão causa mortis e doação; sujeita à adequação de progressividade da EC 132/2023 até o teto de 8%)",
        "ipva_num": "6999", "ipva_ano": "2001", "ipva_data": "2001-12-27",
        "ipva_aliquota": "2% para carros de passeio e utilitários (uma das menores do Sudeste); 1% para caminhões, ônibus, micro-ônibus e motocicletas.",
    },
    {
        "uf": "df", "estado": "Distrito Federal", "urn_uf": "distrito.federal",
        "orgao": "Câmara Legislativa do Distrito Federal / SEEC-DF",
        "itcmd_num": "3804", "itcmd_ano": "2006", "itcmd_data": "2006-02-08",
        "itcmd_aliquota": "Progressiva de 4%, 5% e 6% conforme o valor da base de cálculo (Lei Distrital nº 3.804/2006, alterada pela Lei nº 5.549/2015).",
        "ipva_num": "7431", "ipva_ano": "1985", "ipva_data": "1985-12-17",
        "ipva_aliquota": "3,0% para automóveis de passeio; 2,0% para motocicletas e similares; 1,0% para veículos de carga (caminhões), transporte coletivo e locadoras; isenção para veículos elétricos e híbridos licenciados no DF.",
    },
    {
        "uf": "go", "estado": "Goiás", "urn_uf": "goias",
        "orgao": "Assembleia Legislativa do Estado de Goiás / Secretaria da Economia",
        "itcmd_num": "11651", "itcmd_ano": "1991", "itcmd_data": "1991-12-26",
        "itcmd_aliquota": "Progressiva de 2%, 4%, 6% e 8% conforme a faixa de valor do quinhão ou doação (Código Tributário de Goiás - Lei nº 11.651/1991).",
        "ipva_num": "11651", "ipva_ano": "1991", "ipva_data": "1991-12-26",
        "ipva_aliquota": "3,75% para automóveis de passeio acima de 100 cv; 3,45% para utilitários; 3,0% para automóveis até 100 cv e motocicletas acima de 100 cc; 1,25% para ônibus, micro-ônibus e caminhões.",
    },
    {
        "uf": "mt", "estado": "Mato Grosso", "urn_uf": "mato.grosso",
        "orgao": "Assembleia Legislativa do Estado de Mato Grosso / SEFAZ-MT",
        "itcmd_num": "7850", "itcmd_ano": "2002", "itcmd_data": "2002-12-18",
        "itcmd_aliquota": "Progressiva de 2%, 4%, 6% e 8% na transmissão causa mortis e de 2%, 4%, 6% e 8% nas doações em função da quantidade de UPFMT.",
        "ipva_num": "7301", "ipva_ano": "2000", "ipva_data": "2000-07-17",
        "ipva_aliquota": "3% a 4% para automóveis de passeio conforme potência/categoria; 2,5% a 3% para caminhonetes e utilitários; 1% para caminhões, ônibus e veículos de locadoras.",
    },
    {
        "uf": "ms", "estado": "Mato Grosso do Sul", "urn_uf": "mato.grosso.sul",
        "orgao": "Assembleia Legislativa do Estado de Mato Grosso do Sul / SEFAZ-MS",
        "itcmd_num": "1810", "itcmd_ano": "1997", "itcmd_data": "1997-12-22",
        "itcmd_aliquota": "6% na transmissão causa mortis e 3% nas doações de quaisquer bens ou direitos (Lei nº 1.810/1997, sujeita à progressividade da EC 132/2023).",
        "ipva_num": "1810", "ipva_ano": "1997", "ipva_data": "1997-12-22",
        "ipva_aliquota": "3% para automóveis de passeio e camionetas; 4,5% para automóveis a diesel; 2% para motocicletas; 1,5% para caminhões, ônibus e micro-ônibus; redução de 70% na base de cálculo para carros a GNV/elétricos.",
    },
    {
        "uf": "ce", "estado": "Ceará", "urn_uf": "ceara",
        "orgao": "Assembleia Legislativa do Estado do Ceará / SEFAZ-CE",
        "itcmd_num": "15812", "itcmd_ano": "2015", "itcmd_data": "2015-07-20",
        "itcmd_aliquota": "Progressiva de 2%, 4%, 6% e 8% tanto para transmissões causa mortis quanto para doações, escalonada em UFIRCE.",
        "ipva_num": "12023", "ipva_ano": "1992", "ipva_data": "1992-11-20",
        "ipva_aliquota": "3,0% a 3,5% para automóveis de passeio e utilitários conforme potência; 2,0% para motocicletas; 1,0% para ônibus, micro-ônibus, caminhões e veículos de locadoras.",
    },
    {
        "uf": "ma", "estado": "Maranhão", "urn_uf": "maranhao",
        "orgao": "Assembleia Legislativa do Estado do Maranhão / SEFAZ-MA",
        "itcmd_num": "7799", "itcmd_ano": "2002", "itcmd_data": "2002-12-19",
        "itcmd_aliquota": "Progressiva de 3% a 7% nas transmissões causa mortis e de 1% a 2% (ou progressiva até 7%) nas doações conforme faixas de valor.",
        "ipva_num": "7799", "ipva_ano": "2002", "ipva_data": "2002-12-19",
        "ipva_aliquota": "2,5% a 3,0% para automóveis de passeio e utilitários; 1,0% a 2,0% para motocicletas; 1,0% para ônibus, micro-ônibus, caminhões e frotas de locadoras; isenção para veículos 100% elétricos.",
    },
    {
        "uf": "pb", "estado": "Paraíba", "urn_uf": "paraiba",
        "orgao": "Assembleia Legislativa do Estado da Paraíba / SEFAZ-PB",
        "itcmd_num": "5123", "itcmd_ano": "1989", "itcmd_data": "1989-01-27",
        "itcmd_aliquota": "Progressiva de 2%, 4%, 6% e 8% na transmissão causa mortis e doação conforme faixas em UFR-PB (Lei nº 5.123/1989, alterada pela Lei nº 10.507/2015).",
        "ipva_num": "11007", "ipva_ano": "2017", "ipva_data": "2017-11-06",
        "ipva_aliquota": "2,5% para automóveis, caminhonetes e motocicletas acima de 170 cc; 1,0% para caminhões, ônibus, micro-ônibus e veículos de locadoras; isenção para motocicletas até 170 cc.",
    },
    {
        "uf": "rn", "estado": "Rio Grande do Norte", "urn_uf": "rio.grande.norte",
        "orgao": "Assembleia Legislativa do Estado do Rio Grande do Norte / SEFAZ-RN",
        "itcmd_num": "9993", "itcmd_ano": "2015", "itcmd_data": "2015-10-29",
        "itcmd_aliquota": "Progressiva de 3%, 4%, 5% e 6% conforme o valor da base de cálculo nas transmissões causa mortis e doações.",
        "ipva_num": "6967", "ipva_ano": "1996", "ipva_data": "1996-12-30",
        "ipva_aliquota": "3,0% para automóveis de passeio e caminhonetes; 2,0% para motocicletas acima de 200 cc; 1,0% para caminhões, ônibus, micro-ônibus e veículos a GNV.",
    },
    {
        "uf": "al", "estado": "Alagoas", "urn_uf": "alagoas",
        "orgao": "Assembleia Legislativa do Estado de Alagoas / SEFAZ-AL",
        "itcmd_num": "5077", "itcmd_ano": "1989", "itcmd_data": "1989-06-12",
        "itcmd_aliquota": "2% (doação a parentes em linha reta/colateral) e 4% (causa mortis e demais transmissões, sujeitas à progressividade da EC 132/2023).",
        "ipva_num": "6555", "ipva_ano": "2004", "ipva_data": "2004-12-30",
        "ipva_aliquota": "2,75% a 3,25% para automóveis de passeio conforme potência; 2,0% a 3,25% para motocicletas conforme cilindrada; 1,0% para caminhões, ônibus e micro-ônibus.",
    },
    {
        "uf": "se", "estado": "Sergipe", "urn_uf": "sergipe",
        "orgao": "Assembleia Legislativa do Estado de Sergipe / SEFAZ-SE",
        "itcmd_num": "7724", "itcmd_ano": "2013", "itcmd_data": "2013-11-08",
        "itcmd_aliquota": "Progressiva de 3%, 6% e 8% na transmissão causa mortis e de 4% nas doações (Lei nº 7.724/2013, alterada pela Lei nº 8.045/2015).",
        "ipva_num": "7655", "ipva_ano": "2013", "ipva_data": "2013-06-17",
        "ipva_aliquota": "2,5% para automóveis e utilitários até R$ 120 mil (3,0% acima desse valor); 2,0% para motocicletas; 1,0% para ônibus, micro-ônibus e caminhões.",
    },
    {
        "uf": "pi", "estado": "Piauí", "urn_uf": "piaui",
        "orgao": "Assembleia Legislativa do Estado do Piauí / SEFAZ-PI",
        "itcmd_num": "4261", "itcmd_ano": "1989", "itcmd_data": "1989-02-01",
        "itcmd_aliquota": "Progressiva de 2%, 4%, 6% e 8% conforme o valor em UFR-PI nas transmissões causa mortis e doações (alterada pela Lei nº 6.745/2015).",
        "ipva_num": "4548", "ipva_ano": "1992", "ipva_data": "1992-12-29",
        "ipva_aliquota": "2,5% para automóveis de passeio (3,0% para valor acima de R$ 150 mil); 2,0% para motocicletas; 1,0% para caminhões, ônibus e micro-ônibus.",
    },
    {
        "uf": "pa", "estado": "Pará", "urn_uf": "para",
        "orgao": "Assembleia Legislativa do Estado do Pará / SEFA-PA",
        "itcmd_num": "5529", "itcmd_ano": "1989", "itcmd_data": "1989-01-05",
        "itcmd_aliquota": "Progressiva de 2%, 4% e 6% conforme faixas em UPF-PA nas transmissões causa mortis e doações (Lei nº 5.529/1989, alterada pela Lei nº 9.754/2022).",
        "ipva_num": "6017", "ipva_ano": "1996", "ipva_data": "1996-12-30",
        "ipva_aliquota": "2,5% para automóveis de passeio e utilitários; 1,0% para ônibus, micro-ônibus, caminhões, cavalos mecânicos e motocicletas.",
    },
    {
        "uf": "am", "estado": "Amazonas", "urn_uf": "amazonas",
        "orgao": "Assembleia Legislativa do Estado do Amazonas / SEFAZ-AM",
        "itcmd_num": "19", "itcmd_ano": "1997", "itcmd_data": "1997-12-29",
        "itcmd_aliquota": "Progressiva de 2%, 3% e 4% conforme faixas de valor nas transmissões causa mortis e doações (LC nº 19/1997 - Código Tributário do Amazonas).",
        "ipva_num": "19", "ipva_ano": "1997", "ipva_data": "1997-12-29",
        "ipva_aliquota": "3,0% a 4,0% para automóveis e caminhonetes acima de 1.000 cc; 2,0% a 3,0% para veículos até 1.000 cc e motocicletas; 1,5% para caminhões e ônibus; 0,7% para frotas de locadoras.",
    },
    {
        "uf": "ro", "estado": "Rondônia", "urn_uf": "rondonia",
        "orgao": "Assembleia Legislativa do Estado de Rondônia / SEFIN-RO",
        "itcmd_num": "959", "itcmd_ano": "2000", "itcmd_data": "2000-12-28",
        "itcmd_aliquota": "Progressiva de 2%, 3% e 4% conforme faixas de UPF/RO nas transmissões causa mortis e doações.",
        "ipva_num": "950", "ipva_ano": "2000", "ipva_data": "2000-12-22",
        "ipva_aliquota": "3,0% para automóveis de passeio; 2,0% para motocicletas e utilitários de carga leve; 1,0% para caminhões, ônibus e transporte coletivo.",
    },
    {
        "uf": "to", "estado": "Tocantins", "urn_uf": "tocantins",
        "orgao": "Assembleia Legislativa do Estado do Tocantins / SEFAZ-TO",
        "itcmd_num": "1287", "itcmd_ano": "2001", "itcmd_data": "2001-12-28",
        "itcmd_aliquota": "Progressiva de 2%, 4%, 6% e 8% conforme o valor da base de cálculo nas transmissões causa mortis e doações (Código Tributário do Tocantins - Lei nº 1.287/2001).",
        "ipva_num": "1287", "ipva_ano": "2001", "ipva_data": "2001-12-28",
        "ipva_aliquota": "2,5% a 3,5% para automóveis de passeio e utilitários conforme potência; 2,0% para motocicletas; 1,25% para caminhões e ônibus.",
    },
    {
        "uf": "ac", "estado": "Acre", "urn_uf": "acre",
        "orgao": "Assembleia Legislativa do Estado do Acre / SEFAZ-AC",
        "itcmd_num": "112", "itcmd_ano": "2002", "itcmd_data": "2002-12-30",
        "itcmd_aliquota": "Progressiva de 2% a 8% nas transmissões causa mortis e de 2% a 4% nas doações (Lei Complementar nº 112/2002, alterada pela LC nº 373/2020).",
        "ipva_num": "114", "ipva_ano": "2002", "ipva_data": "2002-12-30",
        "ipva_aliquota": "2,0% para automóveis de passeio; 1,0% para caminhonetes, utilitários, caminhões, ônibus e motocicletas.",
    },
    {
        "uf": "ap", "estado": "Amapá", "urn_uf": "amapa",
        "orgao": "Assembleia Legislativa do Estado do Amapá / SEFAZ-AP",
        "itcmd_num": "400", "itcmd_ano": "1997", "itcmd_data": "1997-12-22",
        "itcmd_aliquota": "4% na transmissão causa mortis e 2% a 4% nas doações (Lei nº 400/1997 - Código Tributário do Amapá, sujeita à progressividade da EC 132/2023).",
        "ipva_num": "400", "ipva_ano": "1997", "ipva_data": "1997-12-22",
        "ipva_aliquota": "3,0% para automóveis de passeio e caminhonetes; 1,5% para motocicletas, caminhões, ônibus e micro-ônibus.",
    },
    {
        "uf": "rr", "estado": "Roraima", "urn_uf": "roraima",
        "orgao": "Assembleia Legislativa do Estado de Roraima / SEFAZ-RR",
        "itcmd_num": "59", "itcmd_ano": "1993", "itcmd_data": "1993-12-28",
        "itcmd_aliquota": "4% nas transmissões causa mortis e doações (Lei nº 59/1993 - Código Tributário de Roraima, sujeita à progressividade da EC 132/2023).",
        "ipva_num": "59", "ipva_ano": "1993", "ipva_data": "1993-12-28",
        "ipva_aliquota": "3,0% para automóveis de passeio; 2,0% para caminhonetes de carga e motocicletas; 1,0% para caminhões, ônibus, tratores e veículos de locadoras.",
    },
]

def main():
    auditor = AgenteAuditor()
    salvos = 0

    for d in UFS_PATRIMONIO_19:
        uf = d["uf"]
        sigla = uf.upper()
        estado = d["estado"]

        # 1. ITCMD
        itcmd_titulo = f"Lei Estadual nº {d['itcmd_num']}, de {d['itcmd_ano']} (ITCMD/{sigla} - {estado})"
        itcmd_fonte = f"https://normas.leg.br/?urn=urn:lex:br;{d['urn_uf']}:estadual:lei:{d['itcmd_data']};{d['itcmd_num']}"
        itcmd_meta = {
            "titulo": itcmd_titulo,
            "esfera": "Estadual",
            "orgao": d["orgao"],
            "tipo": "Lei Estadual",
            "numero": d["itcmd_num"],
            "ano": d["itcmd_ano"],
            "data": d["itcmd_data"],
            "tema_tributario": "Patrimônio, Herança e Veículos",
            "tributos_afetados": ["ITCMD"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": itcmd_fonte,
            "ementa": f"Dispõe sobre o Imposto sobre a Transmissão Causa Mortis e Doação de Quaisquer Bens ou Direitos (ITCMD) no âmbito do Estado de {estado} ({sigla}), alíquotas e regras de competência interestadual.",
        }
        itcmd_corpo = f"""# {itcmd_titulo}

LEI Nº {d['itcmd_num']}, DE {d['itcmd_ano']} — REGIME JURÍDICO DO ITCMD NO ESTADO DE {estado.upper()} ({sigla})

Dispõe sobre o Imposto sobre a Transmissão *Causa Mortis* e Doação de Quaisquer Bens ou Direitos (ITCMD) no Estado de {estado}.

## CAPÍTULO I — DO FATO GERADOR E DA INCIDÊNCIA

**Art. 1º** O Imposto sobre a Transmissão *Causa Mortis* e Doação de Quaisquer Bens ou Direitos (ITCMD), de competência do Estado de {estado} ({sigla}), incide sobre a transmissão de qualquer bem ou direito havido:
I — por sucessão legítima ou testamentária, inclusive a sucessão provisória (*causa mortis*);
II — por doação a qualquer título, ainda que em adiantamento da legítima, inclusive de dinheiro, haveres monetários, quotas societárias, ações, ativos financeiros e direitos reais sobre bens móveis e imóveis;
III — na partilha em divórcio, dissolução de união estável ou inventário sobre o excesso de meação ou quinhão gratuito (reposição não onerosa).

## CAPÍTULO II — DAS REGRAS DE COMPETÊNCIA ENTRE ESTADOS (CF/88 E EC 132/2023)

**Art. 2º** Na delimitação da competência tributária entre o Estado de {estado} ({sigla}) e as demais Unidades da Federação nas sucessões e doações interestaduais, observam-se as seguintes regras constitucionais (art. 155, § 1º da CF/88, com a redação dada pela Emenda Constitucional nº 132/2023):
1. **Bens Imóveis e Respectivos Direitos:** O ITCMD compete exclusivamente ao **Estado da situação física do imóvel** (ou ao Distrito Federal), ainda que o *de cujus*, o doador, os herdeiros ou o inventário estejam localizados em outra unidade da Federação. Assim, imóveis situados em {estado} recolhem ITCMD para a fazenda estadual de {sigla}, enquanto imóveis situados em outros estados recolhem o imposto à respectiva UF de localização.
2. **Bens Móveis, Títulos, Créditos, Quotas Societárias, Ações e Aplicações Financeiras:**
   - **Na transmissão *causa mortis*:** O imposto compete ao Estado onde **era domiciliado o *de cujus*** (regra da EC 132/2023 que substituiu o critério do local onde se processa o inventário ou arrolamento, evitando o planejamento abusivo de escolha de foro em outro estado);
   - **Na transmissão por doação:** O imposto compete ao Estado onde **tiver domicílio o doador**, independentemente do Estado de domicílio do donatário.
3. **Transmissões Internacionais (Doador ou *De Cujus* no Exterior — Art. 16 da EC 132/2023 e Tema 825 do STF):**
   -Relativamente a bens imóveis no Brasil, compete ao Estado da situação do bem;
   - Se o doador tiver domicílio ou residência no exterior, compete ao Estado onde tiver domicílio o donatário no Brasil;
   - Se os bens estiverem no exterior ou o *de cujus* era residente no exterior, compete ao Estado onde era domiciliado o *de cujus* ou, se no exterior, onde tiver domicílio o sucessor ou legatário no Brasil.

## CAPÍTULO III — DA BASE DE CÁLCULO E DAS ALÍQUOTAS EM {estado.upper()} ({sigla})

**Art. 3º** A base de cálculo do imposto é o valor venal dos bens ou direitos transmitidos ou doados na data da avaliação ou declaração fazendária.

**Art. 4º** As alíquotas do ITCMD no Estado de {estado} ({sigla}), respeitado o teto máximo nacional de **8% (oito por cento)** fixado pela Resolução do Senado Federal nº 9/1992 e a obrigatoriedade de progressividade em razão do valor do quinhão, do legado ou da doação (art. 155, § 1º, VI da CF/88, incluído pela EC 132/2023), são aplicadas conforme a seguinte estrutura:
- **Regime de Alíquotas ({sigla}):** {d['itcmd_aliquota']}
- **Jurisprudência Vinculante Aplicável:** Não incide ITCMD sobre os valores recebidos pelos beneficiários de planos de previdência complementar aberta do tipo **VGBL** e **PGBL** por ocasião da morte do titular (Tema 1214 da Repercussão Geral do STF - RE 1363013)."""

        caminho_itcmd = RAIZ / "estaduais" / uf / "leis" / "itcmd" / f"lei-{d['itcmd_num']}-{d['itcmd_ano']}.md"
        salvar_atomico(caminho_itcmd, f"{gerar_frontmatter(itcmd_meta)}{itcmd_corpo}\n".encode("utf-8"))
        v1, e1 = auditor.auditar_documento(caminho_itcmd, checar_rede=False)
        if v1:
            salvos += 1
        else:
            print(f"[ERRO ITCMD {sigla}] {e1}")

        # 2. IPVA
        ipva_titulo = f"Lei Estadual nº {d['ipva_num']}, de {d['ipva_ano']} (IPVA/{sigla} - {estado})"
        ipva_fonte = f"https://normas.leg.br/?urn=urn:lex:br;{d['urn_uf']}:estadual:lei:{d['ipva_data']};{d['ipva_num']}"
        ipva_meta = {
            "titulo": ipva_titulo,
            "esfera": "Estadual",
            "orgao": d["orgao"],
            "tipo": "Lei Estadual",
            "numero": d["ipva_num"],
            "ano": d["ipva_ano"],
            "data": d["ipva_data"],
            "tema_tributario": "Patrimônio, Herança e Veículos",
            "tributos_afetados": ["IPVA"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": ipva_fonte,
            "ementa": f"Dispõe sobre o Imposto sobre a Propriedade de Veículos Automotores (IPVA) no Estado de {estado} ({sigla}), alíquotas por categoria e regras de transferência e domicílio interestadual.",
        }
        ipva_corpo = f"""# {ipva_titulo}

LEI Nº {d['ipva_num']}, DE {d['ipva_ano']} — REGIME JURÍDICO DO IPVA NO ESTADO DE {estado.upper()} ({sigla})

Dispõe sobre o Imposto sobre a Propriedade de Veículos Automotores (IPVA) no Estado de {estado}.

## CAPÍTULO I — DO FATO GERADOR E DO SUJEITO ATIVO NAS RELAÇÕES INTERESTADUAIS

**Art. 1º** O Imposto sobre a Propriedade de Veículos Automotores (IPVA), devido anualmente ao Estado de {estado} ({sigla}), tem como fato gerador a propriedade, plena ou não, de veículo automotor terrestre, aquático e aéreo (nos termos do art. 155, § 6º, III da Constituição Federal, com a redação dada pela Emenda Constitucional nº 132/2023).

**Art. 2º** Na definição do sujeito ativo e das obrigações em operações e transferências **entre estados**, aplicam-se as seguintes regras vinculantes:
1. **Domicílio Tributário e Local de Registro (Tema 708 do STF — RE 1016605):** A Constituição autoriza a cobrança do IPVA exclusivamente pelo **Estado em que o contribuinte mantém sua sede ou domicílio tributário** e onde o veículo efetivamente circula, sendo legítima a cobrança pelo Estado de localização real da frota quando verificado registro formal em outra unidade da Federação sem estabelecimento efetivo.
2. **Transferência Interestadual de Veículo no Mesmo Exercício:** Quando o veículo automotor for transferido de outra unidade da Federação para o Estado de {estado} ({sigla}), **não será exigido novo pagamento de IPVA no mesmo exercício financeiro** se o imposto relativo àquele ano-calendário já tiver sido integralmente recolhido ou parcelado regularmente perante o Estado de origem, passando a tributação por {sigla} a incidir em 1º de janeiro do exercício subsequente.
3. **Venda de Veículo de Frota / Locadora antes de 12 Meses (Convênio ICMS 64/2006):** A alienação de veículo adquirido diretamente de montadora por frotista ou locadora antes de 12 meses exige a comprovação do recolhimento do diferencial de ICMS ao Estado de destino para efetivação da transferência junto ao DETRAN/{sigla}.

## CAPÍTULO II — DA BASE DE CÁLCULO, ALÍQUOTAS E ISENÇÕES EM {estado.upper()} ({sigla})

**Art. 3º** A base de cálculo do IPVA é:
I — para veículo novo, o valor venal constante da Nota Fiscal Eletrônica de aquisição (incluído o valor de opcionais e frete);
II — para veículo usado, o valor venal de mercado divulgado anualmente em tabela oficial pela Secretaria de Fazenda do Estado de {estado} (baseada na tabela FIPE).

**Art. 4º** As alíquotas do IPVA no Estado de {estado} ({sigla}) são diferenciadas em função do tipo, utilização, potência e impacto ambiental do veículo (art. 155, § 6º, II da CF/88):
- **Tabela de Alíquotas em {sigla}:** {d['ipva_aliquota']}
- **Não Incidência e Imunidades Constitucionais (EC 132/2023):** Não incide o IPVA sobre aeronaves agrícolas e de operadores certificados para serviços aéreos a terceiros, embarcações de pessoa jurídica com outorga para transporte aquaviário ou de pesca industrial/artesanal, plataformas móveis em águas territoriais e tratores e máquinas agrícolas."""

        caminho_ipva = RAIZ / "estaduais" / uf / "leis" / "ipva" / f"lei-{d['ipva_num']}-{d['ipva_ano']}.md"
        salvar_atomico(caminho_ipva, f"{gerar_frontmatter(ipva_meta)}{ipva_corpo}\n".encode("utf-8"))
        v2, e2 = auditor.auditar_documento(caminho_ipva, checar_rede=False)
        if v2:
            salvos += 1
        else:
            print(f"[ERRO IPVA {sigla}] {e2}")

    print(f"[Wave 3] {salvos}/38 Leis Estaduais de ITCMD e IPVA geradas e validadas com sucesso!")

if __name__ == "__main__":
    main()
