"""Conversor de HTML jurídico para CommonMark estrito.

Preserva artigos, parágrafos, incisos, alíneas, tabelas e notas de alteração/revogação.
"""
from html.parser import HTMLParser
import re
import unicodedata

class LegalHTMLToMD(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texto = []
        self.ignorar = False
        self.tags_ignorar = {"script", "style", "head", "meta", "link", "noscript"}
        self.pilha_formatacao = []
        self.em_tabela = False
        self.linhas_tabela = []
        self.linha_atual = []
        self.celula_atual = []

    def handle_starttag(self, tag, attrs):
        t = tag.lower()
        if t in self.tags_ignorar:
            self.ignorar = True
            return
        if t == "table":
            self.em_tabela = True
            self.linhas_tabela = []
        elif t == "tr" and self.em_tabela:
            self.linha_atual = []
        elif t in ("td", "th") and self.em_tabela:
            self.celula_atual = []
        elif t in ("b", "strong"):
            self.texto.append("**")
        elif t in ("i", "em"):
            self.texto.append("*")
        elif t in ("s", "strike", "del"):
            self.texto.append("~~")
        elif t in ("p", "div", "br", "h1", "h2", "h3", "h4", "h5", "h6", "li"):
            self.texto.append("\n\n")

    def handle_endtag(self, tag):
        t = tag.lower()
        if t in self.tags_ignorar:
            self.ignorar = False
            return
        if t in ("b", "strong"):
            self.texto.append("**")
        elif t in ("i", "em"):
            self.texto.append("*")
        elif t in ("s", "strike", "del"):
            self.texto.append("~~")
        elif t in ("td", "th") and self.em_tabela:
            celula = "".join(self.celula_atual).strip().replace("\n", " ").replace("|", "\\|")
            self.linha_atual.append(celula)
            self.celula_atual = []
        elif t == "tr" and self.em_tabela:
            if self.linha_atual:
                self.linhas_tabela.append(self.linha_atual)
            self.linha_atual = []
        elif t == "table" and self.em_tabela:
            self.em_tabela = False
            if self.linhas_tabela:
                max_cols = max(len(r) for r in self.linhas_tabela)
                linhas_md = []
                for idx, row in enumerate(self.linhas_tabela):
                    padded = row + [""] * (max_cols - len(row))
                    linhas_md.append("| " + " | ".join(padded) + " |")
                    if idx == 0:
                        linhas_md.append("| " + " | ".join(["---"] * max_cols) + " |")
                self.texto.append("\n\n" + "\n".join(linhas_md) + "\n\n")
            self.linhas_tabela = []

    def handle_data(self, data):
        if self.ignorar:
            return
        if self.em_tabela and self.celula_atual is not None:
            self.celula_atual.append(data)
        else:
            self.texto.append(data)


def converter_html_para_md(html: str) -> str:
    """Converte string HTML de norma jurídica para Markdown limpo."""
    parser = LegalHTMLToMD()
    parser.feed(html)
    bruto = "".join(parser.texto)
    
    # Normalização de espaços e quebras
    bruto = re.sub(r"[ \t]+", " ", bruto)
    bruto = re.sub(r"\n\s*\n\s*\n+", "\n\n", bruto)
    # Remove marcas duplicadas acidentais (ex: **** ou ~~~~ )
    bruto = re.sub(r"\*{4,}", "", bruto)
    bruto = re.sub(r"~{4,}", "", bruto)
    
    return bruto.strip()
