"""Agente Especialista em APIs Oficiais de Dados Abertos.

Responsável por consultar APIs públicas estruturadas:
- API da Receita Federal (Sijut): INs, Portarias, Soluções de Consulta COSIT/DISIT
- API do Senado / Câmara (normas.leg.br e dadosabertos.camara.leg.br)
"""
from pathlib import Path
import json
import hashlib
import gzip
import sys
import urllib.parse

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from comum import Rede, salvar_atomico

API_RFB_PESQUISA = "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
API_RFB_CORPO = "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/"

# IDs reais de tipos normativos da Receita Federal no Sijut:
# 42: Instrução Normativa, 79: IN Conjunta, 57: Portaria, 81: Portaria Conjunta, 10: Ato Declaratório Interpretativo, 11: ADN, 59: Parecer Normativo, 9: ADE, 72: Solução de Consulta, 73: Solução de Divergência, 75: SCI
TIPOS_RFB = {
    "IN": 42,
    "IN_CONJUNTA": 79,
    "PORTARIA": 57,
    "PORTARIA_CONJUNTA": 81,
    "ADI": 10,
    "ADN": 11,
    "PARECER_NORMATIVO": 59,
    "ADE": 9,
    "COSIT": 72,
    "SC": 72,
    "SD": 73,
    "SCI": 75,
    "AD": 7
}

class AgenteAPI:
    def __init__(self, rps: float = 1.5):
        self.rede = Rede(rps=rps)
        self.cache_dir = RAIZ / "_fonte" / "api"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def consultar_atos_rfb(self, termo: str = "", tipo_sigla: str = None, ano: int = None, numero: str = None, data_inicio: str = None, data_fim: str = None, pagina: int = 1, tamanho: int = 10) -> dict:
        """Consulta o Sijut/RFB via API JSON oficial."""
        payload = {
            "tipoPesquisa": "formulario",
            "termo": termo,
            "tipoData": "dataPublicacao",
            "apenasAtosVigentes": False,
            "apenasAtosInternos": False,
            "publicado": True,
            "internet": True,
            "ordenacaoColuna": "publicacao",
            "ordenacaoDirecao": "desc",
            "paginacaoPaginaAtual": pagina,
            "paginacaoQuantidadePorPagina": tamanho
        }
        if tipo_sigla and tipo_sigla.upper() in TIPOS_RFB:
            payload["tiposAtosSelecionados"] = str(TIPOS_RFB[tipo_sigla.upper()])
        if numero:
            payload["numeroAto"] = str(numero)
        if ano:
            payload["anoAto"] = str(ano)
            payload["dataInicio"] = f"01/01/{ano}"
            payload["dataFim"] = f"31/12/{ano}"
        elif data_inicio or data_fim:
            if data_inicio:
                payload["dataInicio"] = data_inicio
            if data_fim:
                payload["dataFim"] = data_fim
            
        cache_key = hashlib.sha256((API_RFB_PESQUISA + json.dumps(payload, sort_keys=True)).encode()).hexdigest()
        cache_file = self.cache_dir / "rfb" / f"pesquisa_{tipo_sigla or 'geral'}_{ano or 'todos'}_n{numero or 'todos'}_p{pagina}_{cache_key[:8]}.json.gz"
        
        if cache_file.exists():
            return json.loads(gzip.decompress(cache_file.read_bytes()).decode("utf-8"))
            
        print(f"[Agente API] Consultando Sijut/RFB (termo='{termo}', tipo={tipo_sigla}, ano={ano}, pág={pagina})...")
        status, dados, _ = self.rede.post_json(API_RFB_PESQUISA, payload)
        if status != 200:
            raise RuntimeError(f"Erro na API RFB: HTTP {status}")
            
        salvar_atomico(cache_file, gzip.compress(dados))
        return json.loads(dados.decode("utf-8"))

    def baixar_corpo_ato_rfb(self, id_ato: int) -> dict:
        """Baixa o conteúdo integral da visão original de um ato da RFB."""
        url = f"{API_RFB_CORPO}{id_ato}/visao/original"
        cache_file = self.cache_dir / "rfb" / "atos" / f"ato_{id_ato}.json.gz"
        
        if cache_file.exists():
            return json.loads(gzip.decompress(cache_file.read_bytes()).decode("utf-8"))
            
        status, dados, _ = self.rede.get(url)
        if status != 200:
            raise RuntimeError(f"Erro ao obter ato {id_ato}: HTTP {status}")
            
        salvar_atomico(cache_file, gzip.compress(dados))
        return json.loads(dados.decode("utf-8"))

    def baixar_norma_lexml(self, urn: str) -> dict:
        """Obtém metadados e texto oficial de norma federal via normas.leg.br (LexML)."""
        url_meta = f"https://normas.leg.br/api/public/normas?urn={urllib.parse.quote(urn, safe=':;@!~$-.')}&tipo_documento=maior-detalhe"
        cache_key = hashlib.sha256(urn.encode()).hexdigest()
        cache_file = self.cache_dir / "lexml" / f"{cache_key}.json.gz"
        
        if cache_file.exists():
            dados = json.loads(gzip.decompress(cache_file.read_bytes()).decode("utf-8"))
        else:
            status, bruto, _ = self.rede.get(url_meta)
            if status != 200 or not bruto:
                raise RuntimeError(f"Erro ao consultar URN {urn}: HTTP {status}")
            dados = json.loads(bruto.decode("utf-8"))
            salvar_atomico(cache_file, gzip.compress(bruto))

        # Seleciona o melhor binário HTML
        encodings = dados.get("encoding", [])
        if isinstance(encodings, dict):
            encodings = [encodings]

        texto_html = ""
        for enc in encodings:
            content_url = enc.get("contentUrl", "")
            if content_url and "html" in (enc.get("encodingFormat") or "text/html"):
                public_url = content_url.replace("/api/binario/", "/api/public/binario/")
                st, html_bytes, _ = self.rede.get(public_url)
                if st == 200 and html_bytes:
                    texto_html = html_bytes.decode("utf-8", errors="replace")
                    break

        return {
            "urn": urn,
            "metadados": dados,
            "html": texto_html
        }

if __name__ == "__main__":
    agente = AgenteAPI()
    resultado = agente.consultar_atos_rfb(tipo_sigla="IN", ano=2024, pagina=1, tamanho=3)
    total = resultado.get("total", 0) if isinstance(resultado, dict) else len(resultado)
    print(f"[Agente API] Sucesso! Encontrados registros na API da Receita Federal. Total informado: {total}")
