"""Lote: Notas Técnicas dos documentos fiscais eletrônicos (NF-e, CT-e e NFS-e) com IBS/CBS, 2026.
Especialistas: tributos_reforma_transicao (IBS, CBS e Imposto Seletivo) e documentos fiscais eletrônicos (leiautes).
Documentos:
- Grupo A (obrigatório): NT NF-e 2025.002 v1.53, 2026.006 v1.01 e 2026.010 v1.00; NT CT-e 2026.004 v1.01;
  NT NFS-e 009 v1.01 e 010 v1.00;
- Grupo B (tentativa; entra só se o PDF baixar, o texto tiver 5.000 caracteres ou mais e trouxer o número e a versão):
  NT NF-e 2026.005, 2026.007 e 2026.008; NT CT-e 2025.001 e 2026.005; NT NFS-e 008.
Os PDFs das Notas Técnicas de NF-e e de CT-e só são entregues com cookie de sessão do portal: `baixar_pdf_sessao`
abre a página de lista e, na mesma sessão, baixa o PDF. Os PDFs de NFS-e vêm do gov.br/nfse, sem cookie.
Cada PDF é convertido por `converter_nt` (`pdftotext -layout`, sem capa, sumário, cabeçalhos e rodapés repetidos),
com um título `##` para cada título numerado de primeiro nível do sumário e o texto da seção em bloco `text`,
que preserva as colunas dos leiautes.
Uso: python3 scripts/gerar_reforma_notas_tecnicas_dfe_2026.py
"""
from collections import Counter
from pathlib import Path
from typing import NamedTuple
import gzip
import html
import http.cookiejar
import math
import re
import sys
import time
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co
import pdf_regulamento as pdfr
from comum import LimiteTaxa, USER_AGENT, salvar_atomico

ORGAO_DFE = "Secretaria Especial da Receita Federal do Brasil / ENCAT - CONFAZ"
ORGAO_NFSE = "Secretaria-Executiva do Comitê Gestor da Nota Fiscal de Serviço Eletrônica de Padrão Nacional (SE/CGNFS-e)"
LISTA_NFE = "https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY="
LISTA_CTE = "https://www.cte.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=Y0nErnoZpsg="
NFE_ARQUIVO = "https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo="
CTE_ARQUIVO = "https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo="
NFSE_RTC = "https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc"
NFSE_VIA = "https://www.gov.br/nfse/pt-br/nfs-e-via/documentacao-tecnica/notas-tecnicas"
ATC = "reguladores/rfb/outros-atos/2026/"
ATC_1 = ("Ato Técnico Conjunto RFB/CGIBS nº 1/2026", ATC + "ato-152654-1-2026.md")
ATC_7 = ("Ato Técnico Conjunto Sufis/CGIBS nº 7/2026", ATC + "ato-153887-7-2026.md")
ATC_8 = ("Ato Técnico Conjunto Sufis/CGIBS nº 8/2026", ATC + "ato-153886-8-2026.md")
ATC_10 = ("Ato Técnico Conjunto Sufis/CGIBS nº 10/2026", ATC + "ato-154369-10-2026.md")
NT_2024_002 = "reforma-tributaria/split-payment/nota-tecnica-nfe-2024-002-ibs-cbs-is.md"
NT_NFSE_2025 = "reforma-tributaria/cbs-receita-federal/nota-tecnica-nfse-nacional-ibs-cbs.md"
PASTA = "reforma-tributaria/documentos-fiscais-eletronicos/"
MIN_CARACTERES_PDF_GRUPO_B = 5000
MIN_CARACTERES_CORPO = 500
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro",
         "novembro", "dezembro"]


class NT(NamedTuple):
    grupo: str            # "A" (obrigatória) ou "B" (tentativa)
    chave: str            # nome do PDF no cache `_fonte/pdf`
    arquivo: str          # nome do documento Markdown em `PASTA`
    titulo: str
    tipo: str
    numero: str
    versao: str
    data: str             # data de publicação da versão (AAAA-MM-DD)
    origem_data: str      # onde a data foi lida: "portal" (lista de Notas Técnicas) ou "capa"
    orgao: str
    tributos: list
    ementa: str
    fonte: str            # página de lista (NF-e e CT-e) ou o próprio PDF (NFS-e)
    url_lista: str | None  # página de lista que abre a sessão (None: sem cookie)
    url_pdf: str | None   # None: o link é lido no item da lista
    item_lista: str | None  # padrão do texto do item na lista, quando `url_pdf` é None
    portal: str
    atc: tuple            # (rótulo, caminho) do ato que fixa a versão
    capa: str             # trecho que a capa do PDF precisa trazer, além de número e versão
    notas: list


NTS = [
    NT("A", "nt-nfe-2025-002-v1-53.pdf", "nota-tecnica-nfe-2025-002-v1-53-leiaute-ibs-cbs-is.md",
       "Nota Técnica NF-e/NFC-e nº 2025.002-RTC, versão 1.53 (Reforma Tributária do Consumo: leiaute de IBS, CBS e IS)",
       "Nota Técnica", "2025.002", "1.53", "2026-10-30", "portal", ORGAO_DFE, ["IBS", "CBS", "Imposto Seletivo"],
       "Nota técnica de adequação dos leiautes da NF-e (modelo 55) e da NFC-e (modelo 65) para inclusão dos campos e das "
       "regras de validação referentes à Reforma Tributária do Consumo - RTC (IBS, CBS e Imposto Seletivo).",
       LISTA_NFE, LISTA_NFE, NFE_ARQUIVO + "BMcHSMEoepU=", None, "Portal Nacional da NF-e", ATC_10, "Nota Técnica",
       [f"Sucede a versão 1.52, aprovada pelo {ATC_8[0]} (`{ATC_8[1]}`). A seção 1 do PDF informa que esta NT substitui, no "
        f"âmbito da NF-e e da NFC-e, a NT 2024.002 v1.10 (`{NT_2024_002}`). No PDF, os Anexos I e II só trazem a "
        "indicação \"Tabela a ser publicada\" e os Anexos III e IV remetem à tabela publicada na aba \"Documentos\", opção "
        "\"Diversos\", do Portal Nacional da NF-e; as tabelas não constam do texto."]),
    NT("A", "nt-nfe-2026-006-v1-01.pdf", "nota-tecnica-nfe-2026-006-v1-01-vinculacao-pagamento-split-payment.md",
       "Nota Técnica NF-e/NFC-e nº 2026.006, versão 1.01 (Vinculação com a Transação de Pagamento do DF-e, Split Payment)",
       "Nota Técnica", "2026.006", "1.01", "2026-10-30", "portal", ORGAO_DFE, ["IBS", "CBS", "Split Payment"],
       "Divulga a especificação técnica para a vinculação entre a NF-e ou a NFC-e e a transação financeira sujeita ao split "
       "payment, com o grupo de informações da vinculação e o evento de vinculação da transação de pagamento.",
       LISTA_NFE, LISTA_NFE, NFE_ARQUIVO + "7xf05PpO4Z0=", None, "Portal Nacional da NF-e", ATC_10, "Nota Técnica",
       [f"Os campos têm caráter preparatório: o split payment está previsto para 2027 e não há exigência de preenchimento "
        f"em produção em 2026 (item 'Histórico de Alterações / Cronograma' do PDF). Complementa a NT 2025.002 "
        f"(`{PASTA}nota-tecnica-nfe-2025-002-v1-53-leiaute-ibs-cbs-is.md`)."]),
    NT("A", "nt-nfe-2026-010-v1-00.pdf", "nota-tecnica-nfe-2026-010-v1-00-danfe-reforma-tributaria.md",
       "Nota Técnica NF-e/NFC-e nº 2026.010, versão 1.00 (DANFE para a Reforma Tributária do Consumo)",
       "Nota Técnica", "2026.010", "1.00", "2026-10-01", "portal", ORGAO_DFE, ["IBS", "CBS", "Imposto Seletivo"],
       "Divulga o modelo do DANFE (Documento Auxiliar da NF-e) para a Reforma Tributária do Consumo, com as alterações do "
       "leiaute para a apresentação de IBS, CBS e Imposto Seletivo.",
       LISTA_NFE, LISTA_NFE, NFE_ARQUIVO + "ugn4MYF5PLg=", None, "Portal Nacional da NF-e", ATC_8, "Nota Técnica",
       [f"Complementa a NT 2025.002 (`{PASTA}nota-tecnica-nfe-2025-002-v1-53-leiaute-ibs-cbs-is.md`). "
        "Os dois arquivos de modelo do DANFE que acompanham a NT (vertical e horizontal) não fazem parte do PDF e não foram "
        "incorporados; as páginas finais do PDF trazem um exemplo de DANFE, preservado em bloco de texto, que perde a "
        "formatação visual."]),
    NT("A", "nt-cte-2026-004-v1-01.pdf", "nota-tecnica-cte-2026-004-v1-01-reforma-tributaria.md",
       "Nota Técnica CT-e nº 2026.004, versão 1.01 (CT-e, CT-e OS e GTV-e na Reforma Tributária do Consumo: valor líquido, "
       "multa e juros, formas de emissão e crédito presumido)",
       "Nota Técnica", "2026.004", "1.01", "2026-10-30", "portal", ORGAO_DFE, ["IBS", "CBS"],
       "Nota técnica de adequação dos leiautes do CT-e, do CT-e OS e da GTV-e à Reforma Tributária do Consumo: valor "
       "líquido da prestação, grupo de multa e juros, formas de emissão, CT-e Simplificado e evento de apropriação do "
       "crédito presumido.",
       LISTA_CTE, LISTA_CTE, CTE_ARQUIVO + "urai6j7wfLM=", None, "Portal Nacional do CT-e", ATC_10, "Conhecimento de Transporte",
       ["Os atos técnicos conjuntos indicam uma NT 2026.004 também para BP-e, NFCom, NF3e, NFAg e NFGas; elas são "
        "documentos próprios dos respectivos portais e não integram o acervo. A versão 1.00 deste CT-e foi aprovada pelo "
        f"{ATC_8[0]} (`{ATC_8[1]}`)."]),
    NT("A", "nt-nfse-009-v1-01.pdf", "nota-tecnica-nfse-009-v1-01-leiaute-reforma-tributaria.md",
       "Nota Técnica SE/CGNFS-e nº 009, versão 1.01 (Leiaute da NFS-e na Reforma Tributária do Consumo)",
       "Nota Técnica SE/CGNFS-e", "009", "1.01", "2026-09-11", "capa", ORGAO_NFSE, ["IBS", "CBS", "ISSQN"],
       "Atualiza o leiaute da Nota Fiscal de Serviço Eletrônica (NFS-e) de padrão nacional para a Reforma Tributária do "
       "Consumo: notas de ajuste de IBS/CBS, grupos do IBS e da CBS, Simples Nacional, bens imóveis, comércio exterior, "
       "eventos e condomínios.",
       f"{NFSE_RTC}/nota-tecnica-009-se-cgnfs-e-v-1-01.pdf", None, f"{NFSE_RTC}/nota-tecnica-009-se-cgnfs-e-v-1-01.pdf",
       None, "Portal da NFS-e (gov.br/nfse)", ATC_7, "Comitê Gestor da Nota Fiscal de Serviço Eletrônica",
       ["Os Anexos VI (Leiautes e Regras de Negócio da NFS-e, versão 1.04) e VII (Tabela de Indicadores da Operação, "
        "versão 1.02) são planilhas .xlsx publicadas no portal da NFS-e "
        "(https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica) e foram apenas referenciados, sem conversão. "
        f"Complementa ou ajusta as Notas Técnicas anteriores da NFS-e, entre elas a nota técnica nacional com IBS e CBS "
        f"(`{NT_NFSE_2025}`). A atualização do portal de "
        "25/11/2026 ainda não tem nota técnica numerada e não consta deste documento."]),
    NT("A", "nt-nfse-via-010-v1-00.pdf", "nota-tecnica-nfse-via-010-v1-00-leiaute.md",
       "Nota Técnica SE/CGNFS-e nº 010, versão 1.00 (Leiaute da NFS-e Via e evento de Manifestação do Adquirente)",
       "Nota Técnica SE/CGNFS-e", "010", "1.00", "2026-09-11", "capa", ORGAO_NFSE, ["IBS", "CBS"],
       "Atualiza o leiaute da Nota Fiscal de Serviço Eletrônica de Exploração de Via (NFS-e Via) de padrão nacional e "
       "cria o evento de Manifestação do Adquirente.",
       f"{NFSE_VIA}/nt-010-se-cgnfse-leiaute-nfse-via-v-1.00.pdf", None,
       f"{NFSE_VIA}/nt-010-se-cgnfse-leiaute-nfse-via-v-1.00.pdf", None, "Portal da NFS-e (gov.br/nfse)", ATC_7,
       "Comitê Gestor da Nota Fiscal de Serviço Eletrônica",
       ["O Manual para Emissão da NFS-e Via (versão 1.02) e o Anexo IV (Leiautes RN ADN, planilha) são publicados à parte "
        "no portal da NFS-e e foram apenas referenciados."]),
    # Grupo B
    NT("B", "nt-nfe-2026-008-v1-01.pdf", "nota-tecnica-nfe-2026-008-v1-01-valor-liquido-produto.md",
       "Nota Técnica NF-e/NFC-e nº 2026.008, versão 1.01 (Valor Líquido do Produto)",
       "Nota Técnica", "2026.008", "1.01", "2026-10-30", "portal", ORGAO_DFE, ["IBS", "CBS"],
       "Divulga a criação de campos para o valor líquido do produto e para o ICMS previsto no pagamento antecipado na "
       "NF-e e na NFC-e, com as regras de validação correspondentes.",
       LISTA_NFE, LISTA_NFE, None, r"2026\.008 v1\.01 -", "Portal Nacional da NF-e", ATC_10, "Nota Técnica", []),
    NT("B", "nt-nfe-2026-005-v1-00.pdf", "nota-tecnica-nfe-2026-005-v1-00-simples-nacional.md",
       "Nota Técnica NF-e/NFC-e nº 2026.005, versão 1.00 (Simples Nacional na Reforma Tributária do Consumo)",
       "Nota Técnica", "2026.005", "1.00", "2026-10-30", "portal", ORGAO_DFE, ["IBS", "CBS", "Simples Nacional"],
       "Atualizações para o Simples Nacional na NF-e e na NFC-e: informações de IBS e CBS dos optantes e regras de "
       "validação correspondentes.",
       LISTA_NFE, LISTA_NFE, NFE_ARQUIVO + "HInG7WD5Sj8=", None, "Portal Nacional da NF-e", ATC_10, "Nota Técnica", []),
    NT("B", "nt-nfe-2026-007-v1-11.pdf", "nota-tecnica-nfe-2026-007-v1-11-contribuinte-exclusivo-ibs-cbs.md",
       "Nota Técnica NF-e/NFC-e nº 2026.007, versão 1.11 (Emissão por Contribuinte Exclusivo do IBS/CBS)",
       "Nota Técnica", "2026.007", "1.11", "2026-10-30", "portal", ORGAO_DFE, ["IBS", "CBS"],
       "Regras de validação e atualização de regras existentes da NF-e e da NFC-e para a verificação dos cadastros na Lista "
       "Centralizada de Contribuintes da RFB (LCC-RFB) e no Cadastro Centralizado de Contribuintes (CCC), na emissão por "
       "contribuinte exclusivo do IBS/CBS.",
       LISTA_NFE, LISTA_NFE, None, r"2026\.007 v1\.11 -", "Portal Nacional da NF-e", ATC_10, "Nota Técnica", []),
    NT("B", "nt-cte-2025-001-v1-14b.pdf", "nota-tecnica-cte-2025-001-v1-14b-leiaute-base-reforma-tributaria.md",
       "Nota Técnica CT-e nº 2025.001-RTC, versão 1.14b (Leiaute base da Reforma Tributária do Consumo no CT-e)",
       "Nota Técnica", "2025.001", "1.14b", "2026-04-30", "portal", ORGAO_DFE, ["IBS", "CBS"],
       "Nota técnica de adequação dos leiautes do CT-e, do CT-e OS e da GTV-e à Reforma Tributária do Consumo (IBS e "
       "CBS), com as regras de validação.",
       LISTA_CTE, LISTA_CTE, None, r"CT-e 2025\.001 v\.1\.14b", "Portal Nacional do CT-e",
       None, "Conhecimento de Transporte",
       ["É a última versão da série 2025.001 do CT-e na lista do portal. Alterações posteriores do leiaute constam da NT "
        f"2026.004 do CT-e (`{PASTA}nota-tecnica-cte-2026-004-v1-01-reforma-tributaria.md`)."]),
    NT("B", "nt-cte-2026-005-v1-00.pdf", "nota-tecnica-cte-2026-005-v1-00-simples-nacional.md",
       "Nota Técnica CT-e nº 2026.005, versão 1.00 (Simples Nacional na Reforma Tributária do Consumo)",
       "Nota Técnica", "2026.005", "1.00", "2026-10-30", "portal", ORGAO_DFE, ["IBS", "CBS", "Simples Nacional"],
       "Atualizações para o Simples Nacional no CT-e: tipo de regime de apuração do IBS e da CBS, grupos de valores dos "
       "optantes, regras de validação e eventos de tributação do Simples Nacional.",
       LISTA_CTE, LISTA_CTE, CTE_ARQUIVO + "AtaVevRXCIQ=", None, "Portal Nacional do CT-e", ATC_10,
       "Conhecimento de Transporte",
       ["Na lista do portal existe uma NT 2026.005 v1.00 com o mesmo título para o BP-e; este documento é a do CT-e."]),
    NT("B", "nt-nfse-008-v1-02.pdf", "nota-tecnica-nfse-008-v1-02-danfse.md",
       "Nota Técnica SE/CGNFS-e nº 008, versão 1.02 (Especificações técnicas do DANFSe)",
       "Nota Técnica SE/CGNFS-e", "008", "1.02", "2026-07-14", "capa", ORGAO_NFSE, ["IBS", "CBS", "ISSQN"],
       "Especifica o DANFSe (Documento Auxiliar da Nota Fiscal de Serviço Eletrônica) da NFS-e de padrão nacional, com "
       "os campos e o formulário, incluindo as informações de IBS e CBS.",
       f"{NFSE_RTC}/nt-008-se-cgnfse-danfse-20260714-v1-02.pdf", None,
       f"{NFSE_RTC}/nt-008-se-cgnfse-danfse-20260714-v1-02.pdf", None, "Portal da NFS-e (gov.br/nfse)", ATC_1,
       "Comitê Gestor da Nota Fiscal de Serviço Eletrônica", []),
]

# Linhas de cabeçalho que não chegam a 60% das páginas de uma NT (o PDF muda o cabeçalho no meio do texto)
CABECALHOS_EXTRAS = {
    "nt-nfe-2026-010-v1-00.pdf": {"Projeto", "Nota Fiscal Eletrônica", "NT 2026.010 – DANFE Reforma Tributária"},
    "nt-cte-2026-005-v1-00.pdf": {"Conhecimento de Transporte Eletrônico – Simples Nacional"},
}


# ---------------------------------------------------------------------------------------------------------------
# Download com sessão
# ---------------------------------------------------------------------------------------------------------------
_limite = LimiteTaxa(1.0)


def _get(opener, url: str, referer: str = None, tentativas: int = 3) -> bytes:
    cabecalhos = {"User-Agent": USER_AGENT, "Accept": "text/html,application/pdf,*/*;q=0.8",
                  "Accept-Language": "pt-BR,pt;q=0.9", "Accept-Encoding": "gzip"}
    if referer:
        cabecalhos["Referer"] = referer
    for tentativa in range(1, tentativas + 1):
        _limite.esperar()
        try:
            with opener.open(urllib.request.Request(url, headers=cabecalhos), timeout=120) as resp:
                bruto = resp.read()
                return gzip.decompress(bruto) if resp.headers.get("Content-Encoding") == "gzip" else bruto
        except Exception:
            if tentativa == tentativas:
                raise
            time.sleep(2 ** tentativa)


def _link_na_lista(pagina: bytes, padrao: str, url_lista: str) -> str:
    """URL do PDF do item da lista cujo texto casa com `padrao`. Espaço no `href` vale '+' (base64)."""
    texto = pagina.decode("utf-8", errors="replace")
    achados = []
    for m in re.finditer(r'<a[^>]*href="([^"]*exibirArquivo[^"]*)"[^>]*>(.*?)</a>', texto, re.S):
        rotulo = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
        if re.search(padrao, rotulo):
            href = html.unescape(m.group(1)).strip().replace(" ", "+")
            achados.append(url_lista.rsplit("/", 1)[0] + "/" + href)
    if len(set(achados)) != 1:
        raise ValueError(f"Item da lista {url_lista} não localizado de forma única para o padrão {padrao!r}: {achados}")
    return achados[0]


def baixar_pdf_sessao(url_lista: str, url_pdf: str | None, nome: str, item_lista: str = None) -> Path:
    """Baixa o PDF de um portal que exige cookie de sessão (NF-e e CT-e).
    Abre a página de lista (GET), guarda os cookies e, na mesma sessão, baixa o PDF com a lista como Referer.
    Sem `url_pdf`, o link é o do item da lista cujo texto casa com `item_lista`. Valida a assinatura `%PDF`
    e guarda o arquivo em `_fonte/pdf/` (cache ignorado pelo git)."""
    destino = co.CACHE_PDF / nome
    if destino.exists() and destino.stat().st_size > 0:
        return destino
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    pagina = _get(opener, url_lista)
    alvo = url_pdf or _link_na_lista(pagina, item_lista, url_lista)
    bruto = _get(opener, alvo, referer=url_lista)
    if not bruto.startswith(b"%PDF"):
        raise RuntimeError(f"O portal não devolveu um PDF para {alvo}")
    salvar_atomico(destino, bruto)
    return destino


def obter_pdf(nt: NT) -> Path:
    if nt.url_lista and nt.url_lista != nt.url_pdf:
        return baixar_pdf_sessao(nt.url_lista, nt.url_pdf, nt.chave, nt.item_lista)
    return co.baixar_pdf(nt.url_pdf, nt.chave)


# ---------------------------------------------------------------------------------------------------------------
# Conversão do PDF
# ---------------------------------------------------------------------------------------------------------------
RX_RODAPE_PAGINA = re.compile(r"^\s*P[aá]gina\s+\d+\s*(/|de)\s*\d+\s*$", re.I)
RX_NUMERO_SOLTO = re.compile(r"^\s*\d{1,3}\s*$")
RX_PONTILHADO = re.compile(r"^(?P<txt>.*?)\s*\.{4,}\s*(?P<pg>\d+)?\s*$")
RX_SUBNIVEL = re.compile(r"^(\d+(\.\d+)+\.?\s|[a-z]\.\s|Grupo\s)")
ZONA_ALTO, ZONA_BAIXO = 6, 4


def _compacto(texto: str) -> str:
    return re.sub(r"\s+", "", texto).lower()


def _normal(texto: str) -> str:
    return re.sub(r"[^\w]", "", texto.lower())


def _paginas(pdf: Path) -> list[list[str]]:
    paginas = pdfr.pdftotext(pdf, layout=True).split("\f")
    while paginas and not paginas[-1].strip():
        paginas.pop()
    return [[l.rstrip() for l in p.replace("\t", " ").split("\n")] for p in paginas]


def remover_cabecalhos_rodapes(paginas: list[list[str]], extras: set = frozenset()) -> list[list[str]]:
    """Tira de cada página os cabeçalhos e rodapés repetidos: linhas iguais, nas zonas de topo e de pé, em 60% ou mais
    das páginas de conteúdo (a capa fica fora da contagem), mais 'Página N / M' e o número de página solto no pé."""
    limiar = math.ceil(0.6 * len(paginas))
    contagem = Counter()
    for p in paginas:
        cheias = [l.strip() for l in p if l.strip()]
        contagem.update(set(cheias[:ZONA_ALTO] + cheias[-ZONA_BAIXO:]))
    repetidas = {s for s, c in contagem.items() if c >= limiar} | set(extras)
    saida = []
    for p in paginas:
        indices = [i for i, l in enumerate(p) if l.strip()]
        zona = set(indices[:ZONA_ALTO] + indices[-ZONA_BAIXO:])
        remover = {i for i in zona if p[i].strip() in repetidas or RX_RODAPE_PAGINA.match(p[i])}
        if indices and RX_NUMERO_SOLTO.match(p[indices[-1]]):
            remover.add(indices[-1])
        saida.append([l for i, l in enumerate(p) if i not in remover])
    return saida


def separar_sumario(linhas: list[str]):
    """(antes, entradas, depois): `entradas` = [(recuo, texto, página)] do sumário; ele começa na linha 'Sumário' e termina
    na última entrada com linha pontilhada ('Título ..... 7') ou número de página solto, incluindo títulos quebrados."""
    idx = next((i for i, l in enumerate(linhas) if l.strip().lower() in ("sumário", "sumario")), None)
    if idx is None:
        return linhas, [], []
    entradas, pendente, fim, i = [], [], idx + 1, idx + 1
    while i < len(linhas):
        s = linhas[i].strip()
        if not s:
            i += 1
            continue
        m = RX_PONTILHADO.match(linhas[i])
        if m and not m.group("txt").strip() and not pendente:
            i += 1  # linha só de pontos, sem título
            continue
        if m:
            partes = pendente + [linhas[i]]
            texto = " ".join(re.sub(r"\.{4,}.*$", "", p).strip() for p in partes)
            entradas.append((len(partes[0]) - len(partes[0].lstrip()), re.sub(r"\s+", " ", texto), m.group("pg")))
            pendente, fim = [], i + 1
        elif RX_NUMERO_SOLTO.match(s) and pendente:
            texto = " ".join(p.strip() for p in pendente)
            entradas.append((len(pendente[0]) - len(pendente[0].lstrip()), re.sub(r"\s+", " ", texto), s))
            pendente, fim = [], i + 1
        else:
            # continuação de título quebrado: algum dos 3 próximos trechos não vazios fecha a entrada
            proximos = [l for l in linhas[i + 1:i + 8] if l.strip()][:3]
            if not any(RX_PONTILHADO.match(l) or RX_NUMERO_SOLTO.match(l) for l in proximos):
                break
            pendente.append(linhas[i])
        i += 1
    return linhas[:idx], entradas, linhas[fim:]


def titulos_primeiro_nivel(entradas: list) -> list[str]:
    """Títulos de primeiro nível do sumário (no menor recuo, sem subníveis como '2.1', 'a.' ou 'Grupo X'). Os numerados
    precisam formar a sequência 1, 2, 3...; senão alguma entrada do sumário foi perdida."""
    if not entradas:
        return []
    recuo = min(e[0] for e in entradas)
    titulos = [e[1] for e in entradas if e[0] <= recuo + 1 and not RX_SUBNIVEL.match(e[1])]
    numeros = [int(m.group(1)) for m in (re.match(r"(\d+)\.?\s", t) for t in titulos) if m]
    if numeros != list(range(1, len(numeros) + 1)):
        raise RuntimeError(f"Títulos numerados do sumário fora de sequência: {numeros}")
    return titulos


def localizar_titulos(linhas: list[str], titulos: list[str]) -> list[tuple[int, int]]:
    """(primeira linha, última linha) do título de cada seção no corpo, em ordem; título quebrado ocupa até 3 linhas."""
    posicoes, i = [], 0
    for titulo in titulos:
        alvo = _normal(titulo)
        achado = None
        for j in range(i, len(linhas)):
            acumulado = ""
            for k in range(j, min(j + 3, len(linhas))):
                if not linhas[k].strip():
                    break
                acumulado += _normal(linhas[k])
                if acumulado == alvo:
                    achado = (j, k)
                    break
                if not alvo.startswith(acumulado):
                    break
            if achado:
                break
        if not achado:
            raise ValueError(f"Título do sumário não localizado no corpo: {titulo!r}")
        posicoes.append(achado)
        i = achado[1] + 1
    return posicoes


def bloco_texto(linhas: list[str]) -> str:
    """Bloco ```text com o recuo comum removido, sem espaços no fim das linhas e sem mais de uma linha em branco seguida."""
    linhas = [re.sub(r"[\x00-\x08\x0b-\x1f\x7f]", "", l).replace("\u00a0", " ").replace("\uf0b7", "•").replace("\uf0fc", "✓").replace("\uf0a7", "•").rstrip() for l in linhas]
    while linhas and not linhas[0].strip():
        linhas.pop(0)
    while linhas and not linhas[-1].strip():
        linhas.pop()
    if not linhas:
        return ""
    recuo = min(len(l) - len(l.lstrip()) for l in linhas if l.strip())
    compactado, vazio = [], False
    for l in linhas:
        if not l.strip():
            if not vazio:
                compactado.append("")
            vazio = True
        else:
            compactado.append(l[recuo:])
            vazio = False
    cerca = "```"
    while any(l.lstrip().startswith(cerca) for l in compactado):
        cerca += "`"
    return f"{cerca}text\n" + "\n".join(compactado) + f"\n{cerca}"


def _secao_preliminar(linhas: list[str]) -> tuple[str, str] | None:
    """Texto que antecede o primeiro título numerado (ou o sumário): título = primeira linha, se curta; corpo = o resto."""
    cheias = [l for l in linhas if l.strip()]
    if not cheias:
        return None
    primeira = cheias[0].strip()
    if len(primeira) <= 80 and not primeira.endswith((".", ":", ";")):
        resto = linhas[linhas.index(cheias[0]) + 1:]
        return re.sub(r"\s+", " ", primeira), bloco_texto(resto)
    return "Texto inicial", bloco_texto(linhas)


class Conversao(NamedTuple):
    capa: str
    texto_total: int
    paginas: int
    corpo: str
    titulos: list
    preliminares: list


def converter_nt(pdf: Path, numero: str, versao: str, trecho_capa: str, extras: set = frozenset()) -> Conversao:
    """Converte uma NT (PDF com texto) em Markdown: `## título` por título numerado de primeiro nível do sumário e
    o texto da seção em bloco `text`. Sem sumário numerado, o texto vira um único bloco."""
    paginas = _paginas(pdf)
    texto_total = len(pdfr.pdftotext(pdf, layout=True))
    capa = "\n".join(l.strip() for l in paginas[0] if l.strip())
    for exigido in (numero, versao, trecho_capa):
        if _compacto(exigido) not in _compacto(capa):
            raise ValueError(f"A capa do PDF não traz {exigido!r}: {capa[:200]!r}")
    conteudo = remover_cabecalhos_rodapes(paginas[1:], extras)
    linhas = [l for p in conteudo for l in p]
    antes, entradas, depois = separar_sumario(linhas)
    titulos = titulos_primeiro_nivel(entradas)
    secoes, preliminares = [], []
    if titulos:
        posicoes = localizar_titulos(depois, titulos)
        for trecho in (antes, depois[:posicoes[0][0]]):
            prelim = _secao_preliminar(trecho)
            if prelim:
                preliminares.append(prelim)
                secoes.append(prelim)
        for n, (titulo, (ini, fim)) in enumerate(zip(titulos, posicoes)):
            proximo = posicoes[n + 1][0] if n + 1 < len(posicoes) else len(depois)
            secoes.append((titulo, bloco_texto(depois[fim + 1:proximo])))
        if len(secoes) - len(preliminares) != len(titulos):
            raise RuntimeError("O número de seções gerado difere do número de títulos do sumário")
    else:
        secoes.append(("Texto da Nota Técnica", bloco_texto(linhas)))
    corpo = "\n\n".join(f"## {t}\n\n{b}" if b else f"## {t}" for t, b in secoes)
    return Conversao(capa, texto_total, len(paginas), corpo, titulos, preliminares)


# ---------------------------------------------------------------------------------------------------------------
# Documento
# ---------------------------------------------------------------------------------------------------------------
def data_br(iso: str) -> str:
    return f"{iso[8:]}/{iso[5:7]}/{iso[:4]}"


def data_extenso(iso: str) -> str:
    return f"{int(iso[8:])} de {MESES[int(iso[5:7]) - 1]} de {iso[:4]}"


def titulo_com_data(nt: NT) -> str:
    """Epígrafe da NT com a data de publicação da versão antes do assunto entre parênteses."""
    return re.sub(r" \(", f", de {data_extenso(nt.data)} (", nt.titulo, count=1)


def caminho(nt: NT) -> str:
    return PASTA + nt.arquivo


def documento(nt: NT) -> tuple[str, Conversao]:
    pdf = obter_pdf(nt)
    conv = converter_nt(pdf, nt.numero, nt.versao, nt.capa, CABECALHOS_EXTRAS.get(nt.chave, frozenset()))
    if nt.grupo == "B" and conv.texto_total < MIN_CARACTERES_PDF_GRUPO_B:
        raise ValueError(f"Texto do PDF com {conv.texto_total} caracteres (mínimo {MIN_CARACTERES_PDF_GRUPO_B})")
    if len(conv.corpo) < MIN_CARACTERES_CORPO:
        raise ValueError(f"Corpo útil com {len(conv.corpo)} caracteres (mínimo {MIN_CARACTERES_CORPO})")
    meta = {
        "titulo": titulo_com_data(nt), "esfera": "Federal", "orgao": nt.orgao, "tipo": nt.tipo,
        "numero": nt.numero, "data": nt.data, "ano": nt.data[:4], "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": nt.tributos, "situacao": "Em vigor", "revogada": False, "fonte": nt.fonte, "ementa": nt.ementa,
    }
    origem = ("lista de Notas Técnicas do portal" if nt.origem_data == "portal" else "capa do PDF")
    fixada = (f"Versão aprovada ou ratificada pelo {nt.atc[0]} (`{nt.atc[1]}`)." if nt.atc else
              "Nenhum Ato Técnico Conjunto do acervo fixa esta versão.")
    secoes = len(conv.titulos)
    notas = [
        f"Texto extraído da camada de texto do PDF oficial da Nota Técnica {nt.numero}, versão {nt.versao}, divulgado "
        f"no {nt.portal} ({conv.paginas} páginas), consultado em {co.DATA_CONSULTA_BR}. A data do documento "
        f"({data_br(nt.data)}) é a de publicação da versão, lida na {origem}.",
        fixada,
        "Foram removidos a capa, o sumário, os cabeçalhos e rodapés repetidos e a numeração de página. "
        + (f"Os {secoes} títulos de primeiro nível do sumário viraram seções e o texto de cada uma, com os quadros "
           "e os leiautes, ficou em bloco de texto que mantém as colunas do PDF. " if secoes else
           "O texto, sem títulos numerados, ficou em um único bloco que mantém as colunas do PDF. ")
        + (("O texto que antecede esses títulos e não consta do sumário ficou em seção própria (" +
            "; ".join(t for t, _ in conv.preliminares) + "). ") if conv.preliminares else "")
        + "Figuras e imagens do PDF não foram convertidas. Em caso de dúvida, prevalece o PDF.",
    ]
    if nt.url_lista and nt.url_lista != nt.url_pdf:
        notas.append("O portal só entrega o PDF com cookie de sessão; o link da fonte é a página de lista de Notas Técnicas, "
                     "onde a versão consta como \"Publicada em " + data_br(nt.data) + "\".")
    notas += nt.notas
    extras = {"data_consulta": co.DATA_CONSULTA, "versao_texto": f"Versão {nt.versao} (PDF oficial, {data_br(nt.data)})"}
    return co.montar_documento(meta, conv.corpo, notas, extras), conv


if __name__ == "__main__":
    pendencias = []
    for nt in NTS:
        try:
            doc, conv = documento(nt)
        except (ValueError, RuntimeError, OSError) as erro:
            if nt.grupo == "A":
                raise
            pendencias.append((nt, erro))
            print(f"[NT DF-e 2026] PENDENTE {caminho(nt)}: {erro}")
            continue
        destino = co.gravar(caminho(nt), doc)
        print(f"[NT DF-e 2026] {destino.relative_to(co.RAIZ)} ({destino.stat().st_size} bytes, "
              f"{conv.paginas} páginas, {len(conv.titulos)} seções)")
    if pendencias:
        print(f"[NT DF-e 2026] {len(pendencias)} NT(s) do grupo B não entraram.")
