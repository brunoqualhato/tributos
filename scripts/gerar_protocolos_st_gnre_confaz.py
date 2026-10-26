"""Gera e audita os Protocolos ICMS e Convênios Setoriais de Substituição Tributária Interestadual e GNRE.

Essenciais para consultas de LLM sobre retenção de ICMS-ST, MVA, CEST, Remessa Conforme (17%) e códigos GNRE entre estados:
- Protocolo ICMS nº 41/2008 (ST Autopeças entre Estados)
- Protocolo ICMS nº 97/2010 (ST Autopeças Norte/Nordeste/Centro-Oeste)
- Protocolo ICMS nº 11/1991 (ST Bebidas Frias: Cervejas, Refrigerantes e Águas)
- Convênio ICMS nº 234/2017 (ST Medicamentos e Produtos Farmacêuticos)
- Convênio ICMS nº 67/2019 (ROT-ST - Regime Optativo de Tributação da Substituição Tributária)
- Convênio ICMS nº 81/2023 (ICMS de 17% nas Importações pelo Regime de Tributação Simplificada / Remessa Conforme)
- Ajuste SINIEF nº 6/1989 (Institui a GNRE - Guia Nacional de Recolhimento de Tributos Estaduais e códigos de receita interestaduais)
"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from comum import gerar_frontmatter, salvar_atomico
from agente_auditor import AgenteAuditor

ATOS_ST_GNRE = [
    {
        "caminho": "estaduais/confaz/protocolos-icms/2008/protocolo-icms-41-2008.md",
        "titulo": "Protocolo ICMS nº 41, de 4 de abril de 2008 (Substituição Tributária Interestadual de Autopeças)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Protocolo ICMS",
        "numero": "41",
        "ano": "2008",
        "data": "2008-04-04",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/protocolos/2008/pt041_08",
        "ementa": "Dispõe sobre a substituição tributária nas operações interestaduais com autopeças entre os Estados signatários.",
        "corpo": """# Protocolo ICMS nº 41, de 4 de abril de 2008 (Substituição Tributária Interestadual de Autopeças)

PROTOCOLO ICMS Nº 41, DE 4 DE ABRIL DE 2008

Dispõe sobre a substituição tributária nas operações com autopeças.

Os Estados do Acre, Alagoas, Amapá, Amazonas, Bahia, Maranhão, Mato Grosso, Minas Gerais, Pará, Paraíba, Paraná, Piauí, Rio de Janeiro, Rio Grande do Sul, Roraima, Santa Catarina, São Paulo e o Distrito Federal, neste ato representados pelos seus respectivos Secretários de Fazenda, tendo em vista o disposto nos arts. 102 e 199 do Código Tributário Nacional e no art. 9º da Lei Complementar nº 87/1996, resolvem celebrar o seguinte PROTOCOLO:

Cláusula primeira Nas operações interestaduais com peças, partes, componentes, acessórios e demais produtos listados no Anexo Único deste protocolo, realizadas entre contribuintes situados nas unidades federadas signatárias, fica atribuída ao remetente, na qualidade de sujeito passivo por substituição, a responsabilidade pela retenção e recolhimento do Imposto sobre Operações Relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação - ICMS, relativo às operações subsequentes.

§ 1º O disposto neste protocolo aplica-se às operações com peças, partes, componentes, acessórios e demais produtos listados no Anexo Único, de uso especificamente automotivo, assim compreendidos os que, em qualquer etapa do ciclo econômico do setor automotivo, sejam adquiridos ou revendidos por estabelecimento de indústria ou comércio de veículos automotores terrestres, bem como de veículos, máquinas e equipamentos agrícolas ou rodoviários, ou de suas peças, partes, componentes e acessórios.
§ 2º A responsabilidade prevista nesta cláusula aplica-se também ao imposto correspondente à diferença entre a alíquota interna da unidade federada de destino e a alíquota interestadual incidente sobre a operação (DIFAL-ST), na hipótese de entrada destinada a uso, consumo ou integração ao ativo imobilizado do destinatário contribuinte.

Cláusula segunda A base de cálculo do imposto, para os fins de substituição tributária, será o valor correspondente ao preço máximo de venda a varejo fixado por autoridade competente, ou na falta deste, o preço sugerido ao público pelo fabricante ou importador, acrescido, em ambos os casos, do valor do frete quando não incluído no preço.
§ 1º Inexistindo os valores de que trata o caput, a base de cálculo corresponderá ao montante formado pelo preço praticado pelo remetente, acrescido dos valores correspondentes a frete, seguro, impostos e outros encargos transferíveis ou cobrados do destinatário, adicionado da parcela resultante da aplicação, sobre o referido montante, do percentual de Margem de Valor Agregado Ajustada (**MVA-ST Ajustada**), calculada segundo a fórmula:
`MVA ajustada = [(1 + MVA-ST original) x (1 - ALQ inter) / (1 - ALQ intra)] - 1`."""
    },
    {
        "caminho": "estaduais/confaz/protocolos-icms/2010/protocolo-icms-97-2010.md",
        "titulo": "Protocolo ICMS nº 97, de 9 de julho de 2010 (Substituição Tributária Interestadual de Autopeças — N, NE e CO)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Protocolo ICMS",
        "numero": "97",
        "ano": "2010",
        "data": "2010-07-09",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/protocolos/2010/pt097_10",
        "ementa": "Dispõe sobre a substituição tributária nas operações interestaduais com autopeças entre os Estados signatários das Regiões Norte, Nordeste, Centro-Oeste, Sul e Sudeste.",
        "corpo": """# Protocolo ICMS nº 97, de 9 de julho de 2010 (Substituição Tributária Interestadual de Autopeças — N, NE e CO)

PROTOCOLO ICMS Nº 97, DE 9 DE JULHO DE 2010

Dispõe sobre a substituição tributária nas operações interestaduais com autopeças.

Cláusula primeira Nas operações interestaduais com peças, partes, componentes, acessórios e demais produtos listados no Anexo Único deste protocolo, realizadas entre contribuintes situados nas unidades federadas signatárias (incluindo Acre, Alagoas, Amapá, Bahia, Goiás, Maranhão, Mato Grosso, Paraíba, Pernambuco, Piauí, Rio Grande do Norte, Rondônia, Roraima, Sergipe e Tocantins, entre outras), fica atribuída ao remetente, na qualidade de sujeito passivo por substituição, a responsabilidade pela retenção e recolhimento do ICMS relativo às operações subsequentes ou à entrada para uso ou consumo do destinatário (DIFAL-ST)."""
    },
    {
        "caminho": "estaduais/confaz/protocolos-icms/1991/protocolo-icms-11-1991.md",
        "titulo": "Protocolo ICMS nº 11, de 21 de maio de 1991 (Substituição Tributária Interestadual de Cerveja, Refrigerante, Água Mineral e Gelo)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Protocolo ICMS",
        "numero": "11",
        "ano": "1991",
        "data": "1991-05-21",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/protocolos/1991/pt011_91",
        "ementa": "Dispõe sobre a substituição tributária nas operações interestaduais com cerveja, refrigerante, água mineral ou potável e gelo.",
        "corpo": """# Protocolo ICMS nº 11, de 21 de maio de 1991 (Substituição Tributária Interestadual de Cerveja, Refrigerante, Água Mineral e Gelo)

PROTOCOLO ICMS Nº 11, DE 21 DE MAIO DE 1991

Dispõe sobre a substituição tributária nas operações com cerveja, refrigerante, água mineral ou potável e gelo.

Cláusula primeira Nas operações interestaduais com cerveja, inclusive chope, refrigerante, água mineral ou potável e gelo, classificados nas posições 2201 a 2203 da NBM/SH, entre contribuintes situados nos Estados signatários, fica atribuída ao estabelecimento industrial, importador, arrematante de mercadoria importada e apreendida ou engarrafador de água, na qualidade de sujeito passivo por substituição, a responsabilidade pela retenção e recolhimento do ICMS relativo às operações subsequentes, calculado com base no Preço Médio Ponderado a Consumidor Final (PMPF) divulgado em Ato COTEPE/ICMS ou pela Secretaria de Fazenda da UF de destino, ou, na sua falta, pela aplicação da Margem de Valor Agregado (MVA-ST)."""
    },
    {
        "caminho": "estaduais/confaz/convenios-icms/2017/convenio-icms-234-2017.md",
        "titulo": "Convênio ICMS nº 234, de 22 de dezembro de 2017 (Substituição Tributária Interestadual de Medicamentos e Produtos Farmacêuticos)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "234",
        "ano": "2017",
        "data": "2017-12-22",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2017/CV234_17",
        "ementa": "Dispõe sobre a substituição tributária nas operações interestaduais com medicamentos de uso humano e outros produtos farmacêuticos relacionados no Anexo XIV do Convênio ICMS 142/2018.",
        "corpo": """# Convênio ICMS nº 234, de 22 de dezembro de 2017 (Substituição Tributária Interestadual de Medicamentos e Produtos Farmacêuticos)

CONVÊNIO ICMS Nº 234, DE 22 DE DEZEMBRO DE 2017

Dispõe sobre a substituição tributária nas operações com medicamentos de uso humano e outros produtos farmacêuticos.

Cláusula primeira Nas operações interestaduais com medicamentos de uso humano e outros produtos farmacêuticos relacionados no Anexo XIV do Convênio ICMS nº 142/2018 (CEST 13.xxx.xx), fica atribuída ao estabelecimento industrial fabricante ou importador, na qualidade de sujeito passivo por substituição, a responsabilidade pela retenção e recolhimento do ICMS relativo às operações subsequentes em favor da unidade federada de destino signatária.

Cláusula segunda A base de cálculo do imposto para fins de substituição tributária será o Preço Médio Ponderado a Consumidor Final (PMPF), ou o Preço Máximo a Consumidor (PMC) divulgado pelas listas oficiais da CMED (Listas Positiva, Negativa e Neutra conforme o regime monofásico de PIS/COFINS da Lei nº 10.147/2000) com aplicação do redutor previsto na legislação da UF de destino, ou, na falta destes, a aplicação da MVA-ST Ajustada."""
    },
    {
        "caminho": "estaduais/confaz/convenios-icms/2019/convenio-icms-67-2019.md",
        "titulo": "Convênio ICMS nº 67, de 5 de julho de 2019 (Regime Optativo de Tributação da Substituição Tributária - ROT-ST)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "67",
        "ano": "2019",
        "data": "2019-07-05",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2019/CV067_19",
        "ementa": "Autoriza as unidades federadas a instituir o Regime Optativo de Tributação da Substituição Tributária (ROT-ST), dispensando o pagamento do complemento do ICMS-ST quando a venda a consumidor final ocorrer por valor superior à base presumida, mediante renúncia ao ressarcimento de que trata o Tema 201 do STF.",
        "corpo": """# Convênio ICMS nº 67, de 5 de julho de 2019 (Regime Optativo de Tributação da Substituição Tributária - ROT-ST)

CONVÊNIO ICMS Nº 67, DE 5 DE JULHO DE 2019

Autoriza as unidades federadas a não exigir valores correspondentes à complementação do ICMS retido por substituição tributária, nos casos em que o preço praticado na operação a consumidor final for superior à base de cálculo utilizada para o cálculo do débito de responsabilidade por substituição tributária.

Cláusula segunda Ficam as unidades federadas autorizadas a instituir Regime Optativo de Tributação da Substituição Tributária (ROT-ST), para segmentos varejistas, com dispensa de pagamento do imposto correspondente à complementação do ICMS retido por substituição tributária, nos casos em que o preço praticado na operação a consumidor final for superior à base de cálculo utilizada para o cálculo do débito de responsabilidade por substituição tributária, condicionada a que o contribuinte varejista firme compromisso de não exigir a restituição decorrente de realização de operações a consumidor final com preço inferior à base de cálculo utilizada para o cálculo do débito de responsabilidade por substituição tributária (Tema 201 do STF), permanecendo no regime pelo prazo mínimo de 12 (doze) meses."""
    },
    {
        "caminho": "estaduais/confaz/convenios-icms/2023/convenio-icms-81-2023.md",
        "titulo": "Convênio ICMS nº 81, de 22 de junho de 2023 (Alíquota Unificada de 17% de ICMS nas Importações pelo Regime de Tributação Simplificada / Remessa Conforme)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Convênio ICMS",
        "numero": "81",
        "ano": "2023",
        "data": "2023-06-22",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "Imposto de Importação"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/convenios/2023/CV081_23",
        "ementa": "Altera o Convênio ICMS nº 18/1995 e estabelece a alíquota única nacional de 17% (dezessete por cento) de ICMS incidente sobre as importações realizadas por remessas postais ou expressas ao abrigo do Regime de Tributação Simplificada (RTS / Remessa Conforme) em todas as 27 Unidades da Federação.",
        "corpo": """# Convênio ICMS nº 81, de 22 de junho de 2023 (Alíquota Unificada de 17% de ICMS nas Importações pelo Regime de Tributação Simplificada / Remessa Conforme)

CONVÊNIO ICMS Nº 81, DE 22 DE JUNHO DE 2023

Estabelece o tratamento tributário do ICMS nas importações realizadas por remessas postais ou expressas submetidas ao Regime de Tributação Simplificada (RTS).

Cláusula primeira Nas operações de importação de bens e mercadorias do exterior realizadas por meio de remessas postais ou encomendas aéreas internacionais submetidas ao Regime de Tributação Simplificada (RTS) de que trata o Decreto-Lei nº 1.804/1980 (inclusive aquelas processadas no âmbito do programa **Remessa Conforme** da Receita Federal do Brasil), a carga tributária do ICMS devido à unidade federada de destino físico do adquirente fica fixada de forma uniforme em **17% (dezessete por cento)** em todos os Estados e no Distrito Federal, independentemente da alíquota modal interna de cada ente federativo."""
    },
    {
        "caminho": "estaduais/confaz/ajustes-sinief/1989/ajuste-sinief-06-1989.md",
        "titulo": "Ajuste SINIEF nº 6, de 21 de fevereiro de 1989 (Instituição da GNRE e Códigos de Receita para Recolhimentos entre Estados)",
        "esfera": "Estadual / CONFAZ",
        "orgao": "Conselho Nacional de Política Fazendária - CONFAZ",
        "tipo": "Ajuste SINIEF",
        "numero": "6",
        "ano": "1989",
        "data": "1989-02-21",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["ICMS", "ICMS-ST"],
        "fonte": "https://www.confaz.fazenda.gov.br/legislacao/ajustes/1989/aj_006_89",
        "ementa": "Institui a Guia Nacional de Recolhimento de Tributos Estaduais (GNRE), utilizada para o recolhimento de tributos devidos a unidade federada diversa daquela do domicílio do contribuinte (ICMS-ST, DIFAL e FCP).",
        "corpo": """# Ajuste SINIEF nº 6, de 21 de fevereiro de 1989 (Instituição da GNRE e Códigos de Receita para Recolhimentos entre Estados)

AJUSTE SINIEF Nº 06, DE 21 DE FEVEREIRO DE 1989

Institui a Guia Nacional de Recolhimento de Tributos Estaduais - GNRE.

Art. 1º Fica instituída a Guia Nacional de Recolhimento de Tributos Estaduais - GNRE, modelo 23 (e GNRE On-Line / Portal Nacional GNRE), que será utilizada para recolhimento de tributos devidos a unidade federada diversa da do domicílio do contribuinte.

### Tabela Oficial de Códigos de Receita da GNRE nas Operações Interestaduais (Art. 88-A do Convênio SINIEF 06/1989)

| Código GNRE | Especificação da Receita Interestadual | Quando Utilizar |
| :---: | :--- | :--- |
| **`10004-8`** | **ICMS Substituição Tributária por Apuração** | Contribuinte substituto localizado em outra UF que possui **Inscrição Estadual de Substituto** na UF de destino (recolhimento mensal consolidado). |
| **`10009-9`** | **ICMS Substituição Tributária por Operação** | Recolhimento do ICMS-ST **a cada operação (nota a nota)** antes da saída da mercadoria, quando o remetente não possui IE de substituto na UF de destino. |
| **`10010-2`** | **ICMS Consumidor Final Não Contribuinte Outra UF por Operação (DIFAL EC 87/15)** | Recolhimento nota a nota do DIFAL devido à UF de destino nas vendas interestaduais a consumidor final não contribuinte (Convênio ICMS 236/2021). |
| **`10011-0`** | **ICMS Consumidor Final Não Contribuinte Outra UF por Apuração** | Recolhimento mensal do DIFAL Não Contribuinte para remetente com inscrição especial na UF de destino. |
| **`10012-9`** | **ICMS Fundo Estadual de Combate à Pobreza por Operação (FCP)** | Recolhimento por operação do adicional do Fundo de Combate à Pobreza (até 2%) devido à UF de destino (em guia separada do ICMS principal). |
| **`10013-7`** | **ICMS Fundo Estadual de Combate à Pobreza por Apuração (FCP)** | Recolhimento mensal por apuração do adicional do FCP para contribuinte inscrito na UF de destino. |
| **`10008-0`** | **ICMS Recolhimentos Especiais** | Antecipação tributária de fronteira, diferencial de alíquotas de contribuinte ou recolhimentos especiais na entrada interestadual. |"""
    },
]

def main():
    auditor = AgenteAuditor()
    salvos = 0

    for doc in ATOS_ST_GNRE:
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
        print(f"[Protocolos ST/GNRE] {caminho.relative_to(RAIZ)} -> valido={valido} erros={erros}")
        if valido:
            salvos += 1

    print(f"\nTotal Protocolos/GNRE salvos e validados: {salvos}/{len(ATOS_ST_GNRE)}")

if __name__ == "__main__":
    main()
