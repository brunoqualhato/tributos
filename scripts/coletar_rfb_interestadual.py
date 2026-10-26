"""Coleta atos e Soluções de Consulta da Receita Federal (Sijut API) voltados à interação
entre Tributos Federais e Operações Estaduais/Interestaduais (ICMS na base de PIS/COFINS,
ICMS-ST, DIFAL, Subvenções de ICMS - Lei 14.789/2023, Zona Franca de Manaus e Áreas de Livre Comércio).
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "scripts" / "agentes"))

from agentes.agente_api import AgenteAPI
from agentes.agente_estruturador import AgenteEstruturador
from agentes.agente_auditor import AgenteAuditor

TERMOS_INTERESTADUAIS = [
    ("icms base de calculo pis cofins", 2023),
    ("icms base de calculo pis cofins", 2024),
    ("subvencao para investimento icms", 2024),
    ("subvencao para investimento icms", 2025),
    ("zona franca de manaus pis cofins", 2023),
    ("zona franca de manaus pis cofins", 2024),
    ("substituicao tributaria icms pis cofins", 2023),
    ("substituicao tributaria icms pis cofins", 2024),
    ("area de livre comercio", 2023),
    ("difal icms", 2023),
]

def main():
    api = AgenteAPI(rps=3.0)
    estruturador = AgenteEstruturador()
    auditor = AgenteAuditor()
    novos = []

    def buscar(termo, ano):
        salvos_local = []
        try:
            res = api.consultar_atos_rfb(termo=termo, ano=ano, pagina=1, tamanho=5)
            atos = res.get("atos", []) if isinstance(res, dict) else res
            for ato in atos:
                id_ato = ato.get("idAto")
                if not id_ato:
                    continue
                # Verifica se já existe no repositório
                if list(RAIZ.glob(f"reguladores/rfb/**/ato-{id_ato}-*.md")):
                    continue
                detalhes = api.baixar_corpo_ato_rfb(id_ato)
                dados = {**ato, **detalhes}
                caminho = estruturador.estruturar_ato_rfb(dados)
                if caminho and Path(caminho).exists():
                    ok, _ = auditor.auditar_documento(Path(caminho), checar_rede=False)
                    if ok:
                        salvos_local.append(Path(caminho))
        except Exception as e:
            print(f"[Aviso API RFB] {termo} ({ano}): {e}")
        return salvos_local

    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = [ex.submit(buscar, t, a) for t, a in TERMOS_INTERESTADUAIS]
        for f in as_completed(futs):
            novos.extend(f.result())

    print(f"[Coleta RFB Interestadual] {len(novos)} novos atos estruturados com sucesso.")

if __name__ == "__main__":
    main()
