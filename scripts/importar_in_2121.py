"""Importa a Instrução Normativa RFB nº 2.121/2022 (Consolidação do PIS/Cofins)."""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from agente_api import AgenteAPI
from html2md import converter_html_para_md
from comum import gerar_frontmatter, salvar_atomico
from agente_auditor import AgenteAuditor

def main():
    api = AgenteAPI()
    auditor = AgenteAuditor()

    id_ato = 127905
    detalhes = api.baixar_corpo_ato_rfb(id_ato)
    segs = sorted(detalhes.get("outrosSegmentos", []), key=lambda x: x.get("ordemSegmentoAto", 0))
    partes = [s.get("textoIntegra", "") for s in segs if s.get("textoIntegra") and not s.get("omitir")]
    texto_html = "\n\n".join(partes)
    md = converter_html_para_md(texto_html)

    ementa = "Consolida as normas sobre a apuração, a cobrança, a fiscalização, a arrecadação e a administração da Contribuição para o PIS/Pasep, da Contribuição para o Financiamento da Seguridade Social (Cofins), da Contribuição para o PIS/Pasep-Importação e da Cofins-Importação."

    meta = {
        "titulo": "Instrução Normativa RFB nº 2121, de 15 de dezembro de 2022",
        "esfera": "Federal",
        "orgao": "Secretaria Especial da Receita Federal do Brasil",
        "tipo": "Instrução Normativa",
        "numero": "2121",
        "ano": "2022",
        "data": "2022-12-15",
        "tema_tributario": "Produtos e Mercadorias",
        "tributos_afetados": ["PIS/Pasep", "Cofins", "Imposto de Importação"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": f"https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{id_ato}",
        "ementa": ementa
    }

    conteudo = f"{gerar_frontmatter(meta)}# Instrução Normativa RFB nº 2121, de 15 de dezembro de 2022\n\n{md}\n"

    # Salva em reguladores/rfb/instrucoes-normativas/2022/
    p1 = RAIZ / "reguladores" / "rfb" / "instrucoes-normativas" / "2022" / f"ato-{id_ato}-2121-2022.md"
    salvar_atomico(p1, conteudo.encode("utf-8"))

    # Salva em reguladores/rfb/pis-cofins-monofasico/
    p2 = RAIZ / "reguladores" / "rfb" / "pis-cofins-monofasico" / f"ato-{id_ato}-2121-2022.md"
    salvar_atomico(p2, conteudo.encode("utf-8"))

    val1, err1 = auditor.auditar_documento(p1, checar_rede=True)
    val2, err2 = auditor.auditar_documento(p2, checar_rede=True)
    print(f"IN 2121/2022 salva: p1 valid={val1} err={err1}, p2 valid={val2} err={err2}")

if __name__ == "__main__":
    main()
