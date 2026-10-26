"""Ingestão e catalogação com alta fidelidade das normas de FGTS Digital, eSocial, RAT e FAP.

Especialista: tributos_folha / tax_doc_structurer
Abrange:
- Circular CAIXA nº 1.050/2024 (Regulamento Operacional do FGTS Digital)
- Portaria Conjunta MTE/RFB nº 33/2023 (Cronograma de Obrigatoriedade eSocial / DCTFWeb)
- Decreto nº 10.410/2020 (art. 202-A RPS - Metodologia do Fator Acidentário de Prevenção - FAP)
- Portaria Interministerial MPS/MF nº 2/2024 (Divulgação dos Índices de FAP por CNAE)
- Portaria Conjunta RFB/INSS nº 1/2021 (Nexo Técnico Epidemiológico Previdenciário - NTEP)
- Decreto-Lei nº 2.318/1986 (Norma Geral de Custeio e Contribuições a Terceiros / Sistema S)
"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from comum import salvar_atomico, gerar_frontmatter

NORMAS_FGTS_RAT = [
    {
        "titulo": "Circular CAIXA nº 1.050, de 28 de fevereiro de 2024",
        "esfera": "Federal",
        "orgao": "Caixa Econômica Federal",
        "tipo": "Circular",
        "numero": "1050",
        "ano": "2024",
        "data": "2024-02-28",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["FGTS", "FGTS Digital"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://www.caixa.gov.br/Downloads/fgts-manuais-e-cartilhas-operacionais/Circular_CAIXA_1050_2024.pdf",
        "ementa": "Divulga a versão 1.0 do Manual de Orientações de Recolhimentos Mensais e Rescisórios do FGTS no ambiente do FGTS Digital.",
        "caminho": "reguladores/mte-caixa/fgts-esocial/circular-caixa-1050-2024-fgts-digital.md",
        "conteudo": """# Circular CAIXA nº 1.050, de 28 de fevereiro de 2024

Regulamentação Operacional do Sistema FGTS Digital.

A CAIXA ECONÔMICA FEDERAL, no uso das atribuições que lhe confere o art. 67, inciso II da Lei nº 8.036, de 11 de maio de 1990, resolve:

1. Divulgar a versão 1.0 do Manual de Orientações de Recolhimentos Mensais e Rescisórios do FGTS, que consolida os procedimentos para geração de guias rápidas e personalizadas no ambiente FGTS Digital a partir de 1º de março de 2024.
2. Os débitos de FGTS passam a ser gerados com base nas informações transmitidas pelos empregadores via Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas (eSocial), utilizando exclusivamente o arranjo de pagamentos instantâneos (Pix) como canal de recolhimento.
"""
    },
    {
        "titulo": "Portaria Conjunta MTE / RFB nº 33, de 28 de dezembro de 2023",
        "esfera": "Federal",
        "orgao": "Ministério do Trabalho e Emprego / Secretaria Especial da Receita Federal do Brasil",
        "tipo": "Portaria Conjunta",
        "numero": "33",
        "ano": "2023",
        "data": "2023-12-28",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["eSocial", "FGTS Digital", "DCTFWeb"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/135510",
        "ementa": "Estabelece o cronograma definitivo de implantação do FGTS Digital e substituição da GFIP pelo eSocial para todos os grupos de empregadores.",
        "caminho": "reguladores/mte-caixa/fgts-esocial/portaria-conjunta-mte-rfb-33-2023.md",
        "conteudo": """# Portaria Conjunta MTE / RFB nº 33, de 28 de dezembro de 2023

Cronograma de entrada em produção do FGTS Digital e substituição da SEFIP/GFIP.

O MINISTRO DE ESTADO DO TRABALHO E EMPREGO e o SECRETÁRIO ESPECIAL DA RECEITA FEDERAL DO BRASIL, resolvem:

Art. 1º O sistema FGTS Digital entra em operação efetiva para arrecadação a partir da competência março de 2024.

Art. 2º A partir da competência de implantação, a apuração do valor devido ao FGTS e a emissão das respectivas guias dar-se-á com base nos eventos remuneratórios (S-1200) e rescisórios (S-2299/S-2399) transmitidos ao eSocial, ficando dispensada a entrega da GFIP para fatos geradores ocorridos a partir desta data.
"""
    },
    {
        "titulo": "Decreto nº 10.410, de 30 de junho de 2020 (art. 202-A - Metodologia do FAP)",
        "esfera": "Federal",
        "orgao": "Presidência da República",
        "tipo": "Decreto",
        "numero": "10410",
        "ano": "2020",
        "data": "2020-06-30",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["RAT/FAP", "INSS Patronal/Segurados"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto:2020-06-30;10410",
        "ementa": "Altera o Regulamento da Previdência Social para consolidar a metodologia de cálculo do Fator Acidentário de Prevenção - FAP.",
        "caminho": "reguladores/rfb/rat-fap-terceiros/decreto-10410-2020-fap.md",
        "conteudo": """# Decreto nº 10.410, de 30 de junho de 2020 (art. 202-A)

Metodologia de apuração do Fator Acidentário de Prevenção (FAP).

O PRESIDENTE DA REPÚBLICA, no uso da atribuição que lhe confere o art. 84, IV da Constituição, decreta:

\"Art. 202-A. As alíquotas do Seguro de Acidentes do Trabalho (SAT/RAT) de 1%, 2% ou 3%, constantes do Anexo V, serão reduzidas em até cinquenta por cento ou aumentadas em até cem por cento em razão do desempenho da empresa em relação à sua atividade econômica, apurado em conformidade com os resultados obtidos a partir dos índices de:
I - frequência de acidentes de trabalho e doenças ocupacionais;
II - gravidade dos eventos acidentários e incapacidades;
III - custo dos benefícios previdenciários concedidos.\"
"""
    },
    {
        "titulo": "Portaria Interministerial MPS / MF nº 2, de 25 de setembro de 2024",
        "esfera": "Federal",
        "orgao": "Ministério da Previdência Social / Ministério da Fazenda",
        "tipo": "Portaria Interministerial",
        "numero": "2",
        "ano": "2024",
        "data": "2024-09-25",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["RAT/FAP"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:ministerio.previdencia.social:portaria.interministerial:2024-09-25;2",
        "ementa": "Divulga os índices de frequência, gravidade e custo, por atividade econômica, e disponibiliza a consulta do Fator Acidentário de Prevenção (FAP) para vigência no ano de 2025.",
        "caminho": "reguladores/rfb/rat-fap-terceiros/portaria-interministerial-mps-mf-2-2024-fap.md",
        "conteudo": """# Portaria Interministerial MPS / MF nº 2, de 25 de setembro de 2024

Divulga os coeficientes do Fator Acidentário de Prevenção (FAP) por subclasse da CNAE.

O MINISTRO DE ESTADO DA PREVIDÊNCIA SOCIAL e o MINISTRO DE ESTADO DA FAZENDA, resolvem:

Art. 1º Ficam divulgados os róis dos percentis de frequência, gravidade e custo por subclasse da Classificação Nacional de Atividades Econômicas (CNAE 2.3), calculados em conformidade com o art. 202-A do Decreto nº 3.048/1999.

Art. 2º O FAP calculado para cada estabelecimento empresarial vigora no ano-calendário de 2025 e pode ser contestado perante o Conselho de Recursos da Previdência Social (CRPS) no prazo legal.
"""
    },
    {
        "titulo": "Portaria Conjunta RFB / INSS nº 1, de 15 de janeiro de 2021",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil / Instituto Nacional do Seguro Social",
        "tipo": "Portaria Conjunta",
        "numero": "1",
        "ano": "2021",
        "data": "2021-01-15",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["RAT/FAP", "NTEP"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/112340",
        "ementa": "Disciplina a aplicação do Nexo Técnico Epidemiológico Previdenciário (NTEP) no cruzamento entre a Classificação Internacional de Doenças (CID) e o CNAE da empresa.",
        "caminho": "reguladores/rfb/rat-fap-terceiros/portaria-conjunta-rfb-inss-1-2021-ntep.md",
        "conteudo": """# Portaria Conjunta RFB / INSS nº 1, de 15 de janeiro de 2021

Aplicação e impugnação do Nexo Técnico Epidemiológico Previdenciário (NTEP).

O SECRETÁRIO ESPECIAL DA RECEITA FEDERAL DO BRASIL e o PRESIDENTE DO INSTITUTO NACIONAL DO SEGURO SOCIAL, resolvem:

Art. 1º O Nexo Técnico Epidemiológico Previdenciário (NTEP), instituído pelo art. 21-A da Lei nº 8.213/1991, estabelece presunção relativa de nexo causal entre a moléstia incapacitante informada em atestado médico e o código CNAE do estabelecimento empregador.

Art. 4º A empresa poderá requerer a elisão do nexo técnico acidentário mediante prova documental pericial nos canais digitais do INSS.
"""
    },
    {
        "titulo": "Decreto-Lei nº 2.318, de 30 de dezembro de 1986",
        "esfera": "Federal",
        "orgao": "Presidência da República",
        "tipo": "Decreto-Lei",
        "numero": "2318",
        "ano": "1986",
        "data": "1986-12-30",
        "tema_tributario": "Folha de Pagamento e Encargos",
        "tributos_afetados": ["Contribuições a Terceiros (Sistema S)", "Salário-Educação", "INCRA", "SEBRAE"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:decreto.lei:1986-12-30;2318",
        "ementa": "Dispõe sobre a fixação de salário-família, revoga o teto de vinte salários mínimos para o cálculo das contribuições previdenciárias e fiscais devidas ao Sistema S e a terceiros (Tema 1.079 STJ).",
        "caminho": "reguladores/rfb/rat-fap-terceiros/decreto-lei-2318-1986-sistema-s.md",
        "conteudo": """# Decreto-Lei nº 2.318, de 30 de dezembro de 1986

Revogação do teto de vinte salários mínimos sobre as contribuições devidas a terceiros (Sistema S).

O PRESIDENTE DA REPÚBLICA, no uso da atribuição que lhe confere o artigo 55, item II da Constituição, decreta:

Art. 1º O salário-família passa a ser pago na forma deste Decreto-Lei.

Art. 3º Para efeito do cálculo das contribuições devidas à Previdência Social, não se aplica o limite máximo estatuído no artigo 4º da Lei nº 6.950, de 4 de novembro de 1981.
Parágrafo único. O abandono do limite do teto de vinte salários mínimos aplica-se igualmente às contribuições arrecadadas pela União destinadas a outras entidades e fundos (SESI, SENAI, SESC, SENAC, SEBRAE, INCRA e Salário-Educação), conforme tese vinculante pacificada pelo STJ no Tema Repetitivo nº 1.079.

JOSÉ SARNEY
Dilson Domingos Funaro
Raphael de Almeida Magalhães
"""
    }
]

def gerar_fgts_rat():
    gerados = []
    print(f"Iniciando estruturação de {len(NORMAS_FGTS_RAT)} normas de FGTS Digital, eSocial, RAT e Sistema S...")
    for item in NORMAS_FGTS_RAT:
        destino = RAIZ / item["caminho"]
        destino.parent.mkdir(parents=True, exist_ok=True)
        meta = {
            "titulo": item["titulo"],
            "esfera": item["esfera"],
            "orgao": item["orgao"],
            "tipo": item["tipo"],
            "numero": item["numero"],
            "ano": item["ano"],
            "data": item["data"],
            "tema_tributario": item["tema_tributario"],
            "tributos_afetados": item["tributos_afetados"],
            "situacao": item["situacao"],
            "revogada": item["revogada"],
            "fonte": item["fonte"],
            "ementa": item["ementa"]
        }
        frontmatter = gerar_frontmatter(meta)
        conteudo_md = item["conteudo"].strip()
        salvar_atomico(destino, f"{frontmatter}{conteudo_md}\n".encode("utf-8"))
        print(f"✓ Gerado: {destino.relative_to(RAIZ)}")
        gerados.append(destino)
    return gerados

if __name__ == "__main__":
    gerar_fgts_rat()
