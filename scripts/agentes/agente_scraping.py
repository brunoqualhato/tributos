"""Agente Especialista em Web Scraping.

Responsável pela captura em portais oficiais sem API REST:
- Planalto (CF/88, CTN, Leis Complementares, Decretos)
- CONFAZ (Convênios e Ajustes SINIEF)
- CFC e CPC (Normas Brasileiras de Contabilidade e Pronunciamentos)
"""
from pathlib import Path
import hashlib
import gzip
import sys

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from comum import Rede, salvar_atomico

class AgenteScraping:
    def __init__(self, rps: float = 2.0):
        self.rede = Rede(rps=rps)
        self.cache_dir = RAIZ / "_fonte" / "scraping"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def raspar_pagina(self, url: str, rotulo: str = "geral") -> str:
        """Baixa página com cache e controle de vazão."""
        chave = hashlib.sha256(url.encode()).hexdigest()
        cache_file = self.cache_dir / rotulo / f"{chave}.html.gz"
        
        if cache_file.exists():
            return gzip.decompress(cache_file.read_bytes()).decode("utf-8", errors="replace")
            
        print(f"[Agente Scraping] Raspando URL ({rotulo}): {url}")
        status, dados, _ = self.rede.get(url)
        if status != 200:
            raise RuntimeError(f"Erro ao raspar {url}: HTTP {status}")
            
        salvar_atomico(cache_file, gzip.compress(dados))
        return dados.decode("utf-8", errors="replace")

    def raspar_ctn_planalto(self) -> str:
        """Exemplo: Coleta o Código Tributário Nacional (Lei 5.172/1966) do Planalto."""
        url = "https://www.planalto.gov.br/ccivil_03/leis/l5172compilado.htm"
        return self.raspar_pagina(url, rotulo="planalto")

if __name__ == "__main__":
    agente = AgenteScraping()
    html = agente.raspar_ctn_planalto()
    print(f"[Agente Scraping] CTN capturado com sucesso! Tamanho bruto: {len(html)} bytes.")
