"""Módulo de utilitários comuns para a esteira de dados tributários e contábeis.

Inclui cliente de rede com controle de taxa (rate limiting), headers oficiais,
gestão de cache compactado (gzip) e formatação de YAML frontmatter canônico.
"""
from pathlib import Path
import datetime as dt
import gzip
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = "TributosBot/1.0 (+https://github.com/tributos-br/tributos; pesquisa academica e civica)"

class LimiteTaxa:
    """Controlador de vazão de requisições por segundo."""
    def __init__(self, rps: float = 2.0):
        self.intervalo = 1.0 / max(0.1, rps)
        self.ultima = 0.0

    def esperar(self):
        agora = time.time()
        espera = self.intervalo - (agora - self.ultima)
        if espera > 0:
            time.sleep(espera)
        self.ultima = time.time()


class Rede:
    """Cliente HTTP com retentativas, rate limit e cabeçalhos padrão."""
    def __init__(self, rps: float = 2.0, timeout: int = 40):
        self.limite = LimiteTaxa(rps)
        self.timeout = timeout
        self.headers = {
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/json,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding": "gzip, deflate",
        }

    def get(self, url: str, headers: dict = None, max_tentativas: int = 3):
        self.limite.esperar()
        hdrs = {**self.headers, **(headers or {})}
        req = urllib.request.Request(url, headers=hdrs)
        
        for tentativa in range(1, max_tentativas + 1):
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    status = resp.status
                    bruto = resp.read()
                    if resp.headers.get("Content-Encoding") == "gzip":
                        bruto = gzip.decompress(bruto)
                    return status, bruto, dict(resp.headers)
            except urllib.error.HTTPError as e:
                if e.code in (404, 410):
                    return e.code, b"", {}
                if e.code in (429, 500, 502, 503, 504) and tentativa < max_tentativas:
                    time.sleep(2 ** tentativa)
                    continue
                raise
            except Exception as e:
                if tentativa < max_tentativas:
                    time.sleep(2 ** tentativa)
                    continue
                raise
        raise RuntimeError(f"Falha após {max_tentativas} tentativas: {url}")

    def post_json(self, url: str, payload: dict, headers: dict = None, max_tentativas: int = 3):
        self.limite.esperar()
        corpo = json.dumps(payload).encode("utf-8")
        hdrs = {
            **self.headers,
            "Content-Type": "application/json",
            **(headers or {})
        }
        req = urllib.request.Request(url, data=corpo, headers=hdrs, method="POST")
        for tentativa in range(1, max_tentativas + 1):
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    status = resp.status
                    bruto = resp.read()
                    if resp.headers.get("Content-Encoding") == "gzip":
                        bruto = gzip.decompress(bruto)
                    return status, bruto, dict(resp.headers)
            except urllib.error.HTTPError as e:
                if e.code in (429, 500, 502, 503, 504) and tentativa < max_tentativas:
                    time.sleep(2 ** tentativa)
                    continue
                raise
            except Exception as e:
                if tentativa < max_tentativas:
                    time.sleep(2 ** tentativa)
                    continue
                raise
        raise RuntimeError(f"Falha no POST após {max_tentativas} tentativas: {url}")


def salvar_atomico(caminho: Path, dados: bytes):
    """Grava um arquivo atomicamente usando arquivo temporário adjacente."""
    caminho.parent.mkdir(parents=True, exist_ok=True)
    temp = caminho.with_suffix(caminho.suffix + f".tmp.{time.time_ns()}")
    temp.write_bytes(dados)
    temp.replace(caminho)


def yaml_str(valor: str) -> str:
    """Escapa uma string para inclusão segura no cabeçalho YAML."""
    if valor is None:
        return '""'
    limpa = valor.replace("\r", "").replace("\n", " ").strip()
    limpa = limpa.replace('"', '\\"')
    return f'"{limpa}"'


def gerar_frontmatter(meta: dict) -> str:
    """Gera o bloco frontmatter YAML canônico."""
    linhas = ["---"]
    ordem = [
        "titulo", "esfera", "orgao", "tipo", "numero", "data", "ano",
        "tributos_afetados", "situacao", "revogada", "fonte", "ementa"
    ]
    for chave in ordem:
        if chave in meta:
            val = meta[chave]
            if isinstance(val, bool):
                linhas.append(f"{chave}: {'true' if val else 'false'}")
            elif isinstance(val, (int, float)):
                linhas.append(f"{chave}: {val}")
            elif isinstance(val, list):
                itens = ", ".join(f'"{item}"' for item in val)
                linhas.append(f"{chave}: [{itens}]")
            elif val is None:
                linhas.append(f"{chave}: null")
            else:
                linhas.append(f"{chave}: {yaml_str(str(val))}")
    linhas.append("---")
    return "\n".join(linhas) + "\n\n"
