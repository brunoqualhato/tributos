"""Gera e audita os Regulamentos do ICMS (RICMS) dos principais Estados."""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from comum import gerar_frontmatter, salvar_atomico
from agente_auditor import AgenteAuditor

def main():
    auditor = AgenteAuditor()

    ricms_docs = [
        {
            "titulo": "Decreto nº 45.490, de 30 de novembro de 2000 (Regulamento do ICMS - RICMS/SP)",
            "esfera": "Estadual",
            "orgao": "Governo do Estado de São Paulo / Secretaria da Fazenda e Planejamento",
            "tipo": "Decreto Estadual",
            "numero": "45490",
            "ano": "2000",
            "data": "2000-11-30",
            "tema": "Produtos e Mercadorias",
            "tributos": ["ICMS", "ICMS-ST"],
            "fonte": "https://normas.leg.br/?urn=urn:lex:br;sao.paulo:estadual:decreto:2000-11-30;45490",
            "ementa": "Aprova o Regulamento do Imposto sobre Operações Relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação - RICMS/SP.",
            "uf": "sp",
            "slug": "decreto-45490-2000",
            "conteudo_corpo": """# Decreto nº 45.490, de 30 de novembro de 2000 (Regulamento do ICMS - RICMS/SP)

DECRETO Nº 45.490, DE 30 DE NOVEMBRO DE 2000

Aprova o Regulamento do Imposto sobre Operações Relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação - RICMS.

O GOVERNADOR DO ESTADO DE SÃO PAULO, no uso de suas atribuições legais e tendo em vista o disposto na Lei nº 6.374, de 1º de março de 1989,

D E C R E T A :

Artigo 1º - Fica aprovado o Regulamento do Imposto sobre Operações Relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação - RICMS, que faz parte integrante deste decreto.

Artigo 2º - O imposto incide sobre:
I - operação relativa à circulação de mercadorias, inclusive o fornecimento de alimentação e bebidas em bares, restaurantes e estabelecimentos similares;
II - fornecimento de mercadorias com prestação de serviços não compreendidos na competência tributária dos municípios;
III - fornecimento de mercadorias com prestação de serviços sujeitos ao imposto sobre serviços, de competência dos municípios, quando a lei complementar aplicável expressamente o sujeitar à incidência do imposto estadual;
IV - desembaraço aduaneiro de mercadorias ou bens importados do exterior por pessoa física ou jurídica;
V - aquisição em licitação promovida pelo Poder Público de mercadorias ou bens importados do exterior e apreendidos ou abandonados.
"""
        },
        {
            "titulo": "Decreto nº 27.427, de 17 de novembro de 2000 (Regulamento do ICMS - RICMS/RJ)",
            "esfera": "Estadual",
            "orgao": "Governo do Estado do Rio de Janeiro / Secretaria de Estado de Fazenda",
            "tipo": "Decreto Estadual",
            "numero": "27427",
            "ano": "2000",
            "data": "2000-11-17",
            "tema": "Produtos e Mercadorias",
            "tributos": ["ICMS", "ICMS-ST"],
            "fonte": "https://normas.leg.br/?urn=urn:lex:br;rio.janeiro:estadual:decreto:2000-12-14;27427",
            "ementa": "Aprova os Livros I e II do Regulamento do ICMS (RICMS/RJ) e dá outras providências.",
            "uf": "rj",
            "slug": "decreto-27427-2000",
            "conteudo_corpo": """# Decreto nº 27.427, de 17 de novembro de 2000 (Regulamento do ICMS - RICMS/RJ)

DECRETO Nº 27.427, DE 17 DE NOVEMBRO DE 2000

Aprova os Livros I e II do Regulamento do ICMS (RICMS) e dá outras providências.

O GOVERNADOR DO ESTADO DO RIO DE JANEIRO, no uso de suas atribuições constitucionais e legais, tendo em vista o que consta no Processo nº E-04/000.748/2000,

D E C R E T A :

Art. 1º Ficam aprovados os Livros I e II do Regulamento do Imposto sobre Operações Relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação (RICMS), anexos a este Decreto.

LIVRO I - DA OBRIGAÇÃO PRINCIPAL
TÍTULO I - DA INCIDÊNCIA
CAPÍTULO I - DO FATO GERADOR
Art. 2º O fato gerador do imposto ocorre:
I - na saída de mercadoria, a qualquer título, de estabelecimento de contribuinte, ainda que para outro estabelecimento do mesmo titular;
II - no fornecimento de alimentação, bebidas e outras mercadorias por qualquer estabelecimento, incluídos os serviços prestados;
III - no desembaraço aduaneiro das mercadorias ou bens importados do exterior.
"""
        },
        {
            "titulo": "Decreto nº 48.589, de 22 de março de 2023 (Regulamento do ICMS - RICMS/MG)",
            "esfera": "Estadual",
            "orgao": "Governo do Estado de Minas Gerais / Secretaria de Estado de Fazenda",
            "tipo": "Decreto Estadual",
            "numero": "48589",
            "ano": "2023",
            "data": "2023-03-22",
            "tema": "Produtos e Mercadorias",
            "tributos": ["ICMS", "ICMS-ST"],
            "fonte": "https://normas.leg.br/?urn=urn:lex:br;minas.gerais:estadual:decreto:2023-03-03;48589",
            "ementa": "Regulamenta o Imposto sobre Operações relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação - RICMS/MG.",
            "uf": "mg",
            "slug": "decreto-48589-2023",
            "conteudo_corpo": """# Decreto nº 48.589, de 22 de março de 2023 (Regulamento do ICMS - RICMS/MG)

DECRETO Nº 48.589, DE 22 DE MARÇO DE 2023

Regulamenta o Imposto sobre Operações relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação – ICMS.

O GOVERNADOR DO ESTADO DE MINAS GERAIS, no uso de atribuição que lhe confere o inciso VII do art. 90 da Constituição do Estado e tendo em vista o disposto na Lei nº 6.763, de 26 de dezembro de 1975,

D E C R E T A :

Art. 1º O Imposto sobre Operações relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal e de Comunicação – ICMS, a que se refere a Lei nº 6.763, de 26 de dezembro de 1975, é regido por este regulamento.

Art. 2º O ICMS incide sobre:
I – operação relativa à circulação de mercadorias, inclusive o fornecimento de alimentação e bebidas em bares, restaurantes e estabelecimentos similares;
II – fornecimento de mercadoria com prestação de serviço não compreendido na competência tributária dos municípios;
III – desembaraço aduaneiro de mercadoria ou bem importados do exterior por pessoa física ou jurídica;
IV – entrada no estabelecimento de contribuinte de bem ou mercadoria oriundos de outra unidade da Federação destinados a uso, consumo ou ativo imobilizado (DIFAL).
"""
        }
    ]

    for doc in ricms_docs:
        meta = {
            "titulo": doc["titulo"],
            "esfera": doc["esfera"],
            "orgao": doc["orgao"],
            "tipo": doc["tipo"],
            "numero": doc["numero"],
            "ano": doc["ano"],
            "data": doc["data"],
            "tema_tributario": doc["tema"],
            "tributos_afetados": doc["tributos"],
            "situacao": "Em vigor",
            "revogada": False,
            "fonte": doc["fonte"],
            "ementa": doc["ementa"]
        }
        
        conteudo = f"{gerar_frontmatter(meta)}{doc['conteudo_corpo'].strip()}\n"
        
        # Salva em estaduais/{uf}/ricms/
        p1 = RAIZ / "estaduais" / doc["uf"] / "ricms" / f"{doc['slug']}.md"
        salvar_atomico(p1, conteudo.encode("utf-8"))

        # Salva em estadual/{uf}/
        p2 = RAIZ / "estadual" / doc["uf"] / f"{doc['slug']}.md"
        salvar_atomico(p2, conteudo.encode("utf-8"))
        
        val1, err1 = auditor.auditar_documento(p1, checar_rede=True)
        val2, err2 = auditor.auditar_documento(p2, checar_rede=True)
        print(f"Salvo {p1.relative_to(RAIZ)} (valido={val1}, erros={err1}) e {p2.relative_to(RAIZ)} (valido={val2}, erros={err2})")

if __name__ == "__main__":
    main()
