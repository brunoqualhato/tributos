#!/usr/bin/env python3
"""Reconcilia a vigência e a `fonte` dos documentos Sijut-derivados do acervo com o Sijut/RFB.
Varre os `.md` cujo `fonte` casa `/externa/<idAto>`, baixa `visao/original` de cada idAto (cache em `_fonte/api`) e lê
`vigente` e `ancorasNoAto[].texto`.
Classes:
  INEQUÍVOCA: `vigente` falso e alguma âncora do ato casa `[Revogado(a) pelo(a) <ato>]` (revogação integral que nomeia o
              revogador). Correção: `situacao: "Revogada"` e `revogada: true`, nada mais.
  AMBÍGUA:    `vigente` falso sem essa âncora (suspensão, 'sem efeito', sem nota). Só relatório, nenhum arquivo é editado.
  INVERSA:    frontmatter Revogada e Sijut vigente. Só relatório.
Também confere `FONTES_CORRETAS` (documentos cujo `fonte` aponta para o idAto de outro ato): o idAto novo só entra se o
número e o ano do documento aparecem na `epigrafeCompleta` desse idAto. A vigência desses documentos é avaliada pelo
idAto novo. A alteração é restrita às linhas `situacao:`, `revogada:` e `fonte:` do frontmatter.
Uso (a partir da raiz do repositório):
    python3 scripts/reconciliar_vigencia_sijut_2026.py             # só mostra o que seria feito
    python3 scripts/reconciliar_vigencia_sijut_2026.py --aplicar   # edita os documentos e grava o relatório em _auditoria/
Rodar de novo não altera nada: documentos já marcados como Revogada ou com o idAto novo são pulados.
"""
from pathlib import Path
import argparse
import collections
import re
import sys
import unicodedata
sys.path.insert(0, str(Path(__file__).resolve().parent))
import coleta_oficial as co  # noqa: E402
RAIZ = co.RAIZ
RELATORIO = f"_auditoria/auditoria_vigencia_sijut_{co.DATA_CONSULTA}.md"
GOVERNANCA = {"README.md", "PROGRESSO.md", "PLANO.md", "WORKLOG.md", "COBERTURA.md", "AGENT.md", "ACERVO.md", "Home.md"}
RE_FONTE = re.compile(r"/externa/(\d+)")
RE_REVOGADO = re.compile(r"^\[Revogad[oa]\(a\) pelo\(a\) (.*?)\]?$")
URL_SIJUT = "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/"
# caminho -> (idAto atual da fonte, idAto correto)
FONTES_CORRETAS = {
    'federal/leis-ordinarias/cprb/in-rfb-2053-2021-cprb.md': (122063, 122005),
    'federal/leis-ordinarias/irrf-servicos/in-srf-459-2004-csrf-retencao-servicos.md': (14683, 15365),
    'federal/leis-ordinarias/offshores/in-rfb-2180-2024-offshores-trusts.md': (136675, 136603),
    'federal/portarias/mf/portaria-mf-612-2023-remessa-conforme.md': (132277, 131703),
    'reguladores/mte-caixa/fgts-esocial/portaria-conjunta-rfb-mps-mte-44-2023-esocial.md': (132906, 132735),
    'reguladores/rfb/instrucoes-normativas/financeiro/ato-in-1585-2015.md': (67812, 67494),
    'reguladores/rfb/instrucoes-normativas/financeiro/in-rfb-1888-2019-criptoativos.md': (100733, 100592),
}
# Fonte que não aponta para o ato do documento e cujo ato correto não está no Sijut: só relatório, nenhuma edição.
FONTE_NAO_LOCALIZADA = {
    'reguladores/rfb/rat-fap-terceiros/portaria-conjunta-rfb-inss-1-2021-ntep.md': 112340,
}
ABREVIACOES = [("Instrução Normativa", "IN"), ("Ato Declaratório Executivo", "ADE"), ("Ato Declaratório Interpretativo", "ADI"),
               ("Portaria Conjunta", "PC"), ("Resolução", "Res.")]


def sem_acentos(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def milhar(num: str) -> str:
    n = num.replace(".", "")
    return f"{int(n):,}".replace(",", ".") if n.isdigit() else num


def nome_curto(rotulo: str, ano: str | None = None) -> str:
    """'Instrução Normativa RFB nº 2111, de 20 de outubro de 2022' -> 'IN RFB 2.111/2022' (sem acentos)."""
    m = re.match(r"^(.*?)\s+nº\s*([\d\.]+)(?:\s*\([^)]*\))?,?\s*(?:de .*?(\d{4}))?", rotulo)
    if not m:
        return sem_acentos(rotulo)[:60]
    tipo = re.sub(r"\s*/\s*", "/", m.group(1))
    for longo, curto in ABREVIACOES:
        tipo = tipo.replace(longo, curto)
    ano = m.group(3) or ano or ""
    return sem_acentos(f"{tipo} {milhar(m.group(2))}" + (f"/{ano}" if ano else ""))


def separar_frontmatter(texto: str) -> tuple[int, int] | None:
    """Intervalo [início, fim) do frontmatter (linha '---' inicial até a '---' final), sem traduzir quebras de linha."""
    if not texto.startswith("---"):
        return None
    m = re.search(r"\n---[ \t]*\r?\n", texto[3:])
    return (0, 3 + m.end()) if m else None


def campo(fm: str, nome: str) -> str | None:
    m = re.search(rf'^{nome}: "?([^"\r\n]*)"?\s*$', fm, re.M)
    return m.group(1) if m else None


def varrer() -> list[dict]:
    docs = []
    for p in sorted(RAIZ.rglob("*.md")):
        rel = p.relative_to(RAIZ)
        if p.name in GOVERNANCA or any(x.startswith((".", "_")) or x == "wiki" for x in rel.parts):
            continue
        texto = p.read_bytes().decode("utf-8")
        fim = separar_frontmatter(texto)
        if not fim:
            continue
        fm = texto[:fim[1]]
        fonte = campo(fm, "fonte") or ""
        m = RE_FONTE.search(fonte)
        caminho = rel.as_posix()
        if not m and caminho not in FONTE_NAO_LOCALIZADA:
            continue
        docs.append({"caminho": caminho, "titulo": campo(fm, "titulo") or "", "ano": campo(fm, "ano") or "",
                     "situacao": campo(fm, "situacao"), "revogada": campo(fm, "revogada"),
                     "id_fonte": int(m.group(1)) if m else None})
    return docs


def numero_titulo(titulo: str) -> str | None:
    m = re.search(r"nº\s*([\d\.]+)", titulo)
    return m.group(1).replace(".", "").lstrip("0") if m else None


def confere_epigrafe(doc: dict, epigrafe: str) -> bool:
    numero = numero_titulo(doc["titulo"])
    texto = epigrafe.replace(".", "")
    return bool(numero) and bool(re.search(rf"\bnº\s*0*{numero}\b", texto)) and doc["ano"] in texto


def consultar(ids: set[int]) -> dict[int, dict]:
    sijut = {}
    for i, id_ato in enumerate(sorted(ids), 1):
        d = co.api().baixar_corpo_ato_rfb(id_ato)
        revogadores = []
        for a in d.get("ancorasNoAto") or []:
            m = RE_REVOGADO.match((a.get("texto") or "").strip())
            if m:
                revogadores.append({"texto": m.group(1).strip(), "id": a.get("idAto")})
        sijut[id_ato] = {"vigente": bool(d.get("vigente")), "epigrafe": d.get("epigrafeCompleta") or "",
                         "revogadores": revogadores,
                         "notas": [(a.get("texto") or "").strip() for a in d.get("ancorasNoAto") or []]}
        if i % 100 == 0:
            print(f"  ... {i}/{len(ids)} idAtos consultados", file=sys.stderr)
    return sijut


def analisar() -> dict:
    docs = varrer()
    por_caminho = {d["caminho"]: d for d in docs}
    problemas = []
    fontes = []
    for caminho, (atual, novo) in FONTES_CORRETAS.items():
        d = por_caminho.get(caminho)
        if d is None:
            problemas.append(f"documento da lista FONTES_CORRETAS não encontrado: {caminho}")
            continue
        d["fonte_nova"] = None
        if d["id_fonte"] == novo:
            d["fonte_ja_corrigida"] = True
        elif d["id_fonte"] != atual:
            problemas.append(f"{caminho}: fonte tem idAto {d['id_fonte']}, esperado {atual} ou {novo}")
            continue
        d["fonte_nova"] = novo
        fontes.append(d)
    for caminho, id_fonte in FONTE_NAO_LOCALIZADA.items():
        d = por_caminho.get(caminho)
        if d is None or d["id_fonte"] != id_fonte:
            problemas.append(f"documento NTEP não encontrado ou com outra fonte: {caminho}")
    for d in docs:
        d["id_efetivo"] = d["fonte_nova"] if d.get("fonte_nova") else d["id_fonte"]
        if d["caminho"] in FONTE_NAO_LOCALIZADA:
            d["id_efetivo"] = None  # a fonte descreve outro ato: não serve para avaliar a vigência do documento
    ids = {d["id_efetivo"] for d in docs if d["id_efetivo"]} | {d["id_fonte"] for d in docs if d["id_fonte"]}
    sijut = consultar(ids)
    for d in fontes:
        d["epigrafe_nova"] = sijut[d["fonte_nova"]]["epigrafe"]
        d["epigrafe_antiga"] = sijut[d["id_fonte"]]["epigrafe"] if d["id_fonte"] in sijut else ""
        d["epigrafe_ok"] = confere_epigrafe(d, d["epigrafe_nova"])
        if not d["epigrafe_ok"]:
            problemas.append(f"{d['caminho']}: epígrafe do idAto {d['fonte_nova']} não casa com o título "
                             f"({d['epigrafe_nova']!r}); fonte não será trocada")
    ids_acervo = {d["id_fonte"] for d in docs} | {d["id_efetivo"] for d in docs}
    grupos = collections.defaultdict(list)
    for d in docs:
        if d["id_efetivo"]:
            grupos[d["id_efetivo"]].append(d)
    inequivocas, ambiguas, inversas, vigentes = [], [], [], 0
    for id_ato, lista in sorted(grupos.items()):
        s = sijut[id_ato]
        marcado = any(x["situacao"] == "Revogada" or x["revogada"] == "true" for x in lista)
        if s["vigente"]:
            vigentes += 1
            if marcado:
                inversas.append(id_ato)
        elif s["revogadores"]:
            inequivocas.append(id_ato)
        else:
            ambiguas.append(id_ato)
    return {"docs": docs, "ids_brutos": len({d["id_fonte"] for d in docs if d["id_fonte"]}), "grupos": grupos, "sijut": sijut, "fontes": fontes, "problemas": problemas, "vigentes": vigentes,
            "inequivocas": inequivocas, "ambiguas": ambiguas, "inversas": inversas, "ids_acervo": ids_acervo}


def correcoes(r: dict) -> list[dict]:
    """Uma entrada por documento a editar: o que muda e a mensagem de commit sugerida."""
    lista = []
    ineq = set(r["inequivocas"])
    for d in r["docs"]:
        troca_fonte = bool(d.get("fonte_nova")) and d.get("epigrafe_ok") and d["id_fonte"] != d["fonte_nova"]
        revoga = d["id_efetivo"] in ineq and not (d.get("fonte_nova") and not d.get("epigrafe_ok"))
        if revoga and d["situacao"] == "Revogada" and d["revogada"] == "true":
            revoga = False  # já corrigido numa execução anterior
        elif revoga and (d["situacao"] != "Em vigor" or d["revogada"] != "false"):
            r["problemas"].append(f"{d['caminho']}: situacao/revogada atuais ({d['situacao']!r}/{d['revogada']!r}) "
                                  "não são 'Em vigor'/false; não editado")
            revoga = False
        if not (troca_fonte or revoga):
            continue
        curto = nome_curto(d["titulo"], d["ano"])
        rev = r["sijut"][d["id_efetivo"]]["revogadores"]
        por = "; ".join(nome_curto(x["texto"]) for x in rev)
        if revoga and troca_fonte:
            msg = f"fix(vigencia): corrige a fonte e marca a {curto} como revogada ({por})"
        elif revoga:
            msg = f"fix(vigencia): marca a {curto} como revogada ({por})"
        else:
            msg = f"fix(fonte): corrige o idAto da fonte da {curto} ({d['fonte_nova']})"
        lista.append({"doc": d, "revoga": revoga, "troca_fonte": troca_fonte, "msg": msg})
    return lista


def editar(texto: str, c: dict) -> str:
    fim = separar_frontmatter(texto)[1]
    fm, corpo = texto[:fim], texto[fim:]
    if c["revoga"]:
        fm, n1 = re.subn(r'^situacao: "Em vigor"(?=\r?$)', 'situacao: "Revogada"', fm, count=1, flags=re.M)
        fm, n2 = re.subn(r'^revogada: false(?=\r?$)', 'revogada: true', fm, count=1, flags=re.M)
        if n1 != 1 or n2 != 1:
            raise RuntimeError(f"{c['doc']['caminho']}: linhas situacao/revogada não encontradas")
    if c["troca_fonte"]:
        d = c["doc"]
        fm, n = re.subn(rf'^(fonte: "[^"\r\n]*/externa/){d["id_fonte"]}(")', rf"\g<1>{d['fonte_nova']}\g<2>", fm, count=1, flags=re.M)
        if n != 1:
            raise RuntimeError(f"{d['caminho']}: linha fonte não encontrada")
    return fm + corpo


def md(s: str) -> str:
    return s.replace("|", "\\|")


def relatorio(r: dict, cs: list[dict]) -> str:
    docs, sijut, grupos = r["docs"], r["sijut"], r["grupos"]
    ids_acervo = r["ids_acervo"]
    n_falsos = len(r["inequivocas"]) + len(r["ambiguas"])
    L = [f"# Auditoria de vigência e fonte dos documentos Sijut ({co.DATA_CONSULTA_BR})", "",
         f"Consulta ao Sijut em {co.DATA_CONSULTA_BR}, por `python3 scripts/reconciliar_vigencia_sijut_2026.py`. "
         "Cada documento cujo `fonte` aponta para o Sijut (`/externa/<idAto>`) foi comparado com o campo `vigente` e com as "
         "notas (`ancorasNoAto`) de `visao/original` do ato. Só a revogação integral que nomeia o revogador "
         "(`[Revogado(a) pelo(a) <ato>]`) altera o documento (`situacao: \"Revogada\"` e `revogada: true`); nenhuma outra "
         "linha é tocada.", "",
         "## Resumo", "",
         f"- Arquivos do acervo com fonte no Sijut: {len([d for d in docs if d['id_fonte']])}; idAtos distintos: {r['ids_brutos']} pelo `fonte` atual e {len(grupos)} depois de corrigir as fontes e tirar o documento sem fonte localizada (documentos que passam a compartilhar o idAto de outro arquivo).",
         f"- Vigentes no Sijut: {r['vigentes']}; com `vigente` falso: {n_falsos}.",
         f"- Revogações inequívocas (idAtos): {len(r['inequivocas'])}; documentos alterados por revogação: "
         f"{sum(1 for c in cs if c['revoga'])}.",
         f"- Ambíguas (só relatório): {len(r['ambiguas'])}.",
         f"- Sentido inverso (documento Revogada e Sijut vigente): {len(r['inversas'])}.",
         f"- `fonte` divergentes: {len(r['fontes']) + len(FONTE_NAO_LOCALIZADA)} ({sum(1 for c in cs if c['troca_fonte'])} "
         f"corrigidas, {len(FONTE_NAO_LOCALIZADA)} só relatada).", ""]
    L += ["## Revogações inequívocas corrigidas", "",
          "| # | Documento | idAto | Revogado por (nota oficial do Sijut) | Revogador no acervo |", "|---|---|---|---|---|"]
    k = 0
    for c in cs:
        if not c["revoga"]:
            continue
        k += 1
        d = c["doc"]
        rev = sijut[d["id_efetivo"]]["revogadores"]
        texto = "; ".join(x["texto"] for x in rev)
        noacervo = "; ".join("sim" if x["id"] in ids_acervo else "não" for x in rev)
        L.append(f"| {k} | `{d['caminho']}` | {d['id_efetivo']} | {md(texto)} | {noacervo} |")
    fora = [c for c in cs if c["revoga"] and not any(x["id"] in ids_acervo for x in sijut[c["doc"]["id_efetivo"]]["revogadores"])]
    L += ["", "## Revogados por ato fora do acervo", "",
          f"{len(fora)} dos documentos revogados têm o ato revogador fora do acervo. O documento revogado continua no acervo "
          "como registro histórico, agora com `situacao: \"Revogada\"`.", ""]
    for c in fora:
        d = c["doc"]
        L.append(f"- `{d['caminho']}`: {md('; '.join(x['texto'] for x in sijut[d['id_efetivo']]['revogadores']))}")
    L += ["", "## Ambíguas (sem edição)", "",
          "`vigente` falso sem nota de revogação integral. Suspensão e 'sem efeito' não equivalem a revogação e não têm texto "
          "canônico em `situacao`; o documento fica como está.", "",
          "| Documento | idAto | Evidência no Sijut |", "|---|---|---|"]
    for id_ato in r["ambiguas"]:
        for d in grupos[id_ato]:
            notas = "; ".join(sijut[id_ato]["notas"]) or "sem nota"
            L.append(f"| `{d['caminho']}` | {id_ato} | {md(notas)} |")
    L += ["", "## `fonte` que apontava para outro ato", "",
          "O idAto antigo descreve outro ato. A troca só é feita quando número e ano do título do documento aparecem na "
          "`epigrafeCompleta` do idAto novo.", "",
          "| Documento | idAto antigo | Epígrafe do idAto antigo | idAto novo | Epígrafe do idAto novo | Resultado |", "|---|---|---|---|---|---|"]
    corrigidos = {c["doc"]["caminho"]: c for c in cs}
    for d in r["fontes"]:
        c = corrigidos.get(d["caminho"])
        res = "fonte trocada" if c and c["troca_fonte"] else ("já estava correta" if d.get("fonte_ja_corrigida") else "epígrafe não casa; não alterado")
        if c and c["revoga"]:
            res += f"; marcada Revogada (ato revogado por {md('; '.join(x['texto'] for x in sijut[d['id_efetivo']]['revogadores']))})"
        L.append(f"| `{d['caminho']}` | {d['id_fonte']} | {md(d['epigrafe_antiga'])} | {d['fonte_nova']} | {md(d['epigrafe_nova'])} | {res} |")
    for caminho, id_fonte in FONTE_NAO_LOCALIZADA.items():
        d = next((x for x in docs if x["caminho"] == caminho), None)
        ep = sijut[id_fonte]["epigrafe"] if id_fonte in sijut else "(não consultado)"
        if id_fonte in sijut and sijut[id_fonte]["revogadores"]:
            ep += " (vigente falso; revogado por " + "; ".join(x["texto"] for x in sijut[id_fonte]["revogadores"]) + ")"
        L.append(f"| `{caminho}` | {id_fonte} | {md(ep)} | não localizado | o ato do documento (Portaria Conjunta RFB/INSS nº 1/2021, NTEP) "
                 "não foi encontrado no Sijut por tipo, número, ano nem por 'Nexo Técnico Epidemiológico' | só relatório; "
                 "verificar a origem do texto antes de manter o documento |")
    L += ["", "## Sentido inverso", ""]
    L += [f"- idAto {i}: documento marcado Revogada e ato vigente no Sijut." for i in r["inversas"]] or ["Nenhum caso."]
    if r["problemas"]:
        L += ["", "## Ocorrências do script", ""] + [f"- {p}" for p in r["problemas"]]
    L.append("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--aplicar", action="store_true", help="edita os documentos e grava o relatório")
    args = ap.parse_args()
    r = analisar()
    cs = correcoes(r)
    sijut, grupos = r["sijut"], r["grupos"]
    print(f"arquivos com fonte no Sijut: {len([d for d in r['docs'] if d['id_fonte']])}; idAtos: {len(grupos)}; "
          f"vigentes: {r['vigentes']}; vigente falso: {len(r['inequivocas']) + len(r['ambiguas'])}")
    print(f"INEQUÍVOCAS (idAtos): {len(r['inequivocas'])}; arquivos a marcar Revogada: {sum(1 for c in cs if c['revoga'])}")
    print(f"AMBÍGUAS: {len(r['ambiguas'])}")
    for i in r["ambiguas"]:
        print(f"  {i}: {[d['caminho'] for d in grupos[i]]} {sijut[i]['notas']}")
    print(f"INVERSAS: {len(r['inversas'])} {r['inversas']}")
    print(f"FONTES divergentes: {len(r['fontes'])} + {len(FONTE_NAO_LOCALIZADA)} só relatório; a trocar: {sum(1 for c in cs if c['troca_fonte'])}")
    for d in r["fontes"]:
        print(f"  {d['caminho']}: {d['id_fonte']} -> {d['fonte_nova']} epígrafe {'OK' if d['epigrafe_ok'] else 'NÃO CASA'}: {d['epigrafe_nova']}")
    for p in r["problemas"]:
        print(f"OCORRÊNCIA: {p}")
    for c in cs:
        print(f"COMMIT\t{c['doc']['caminho']}\t{c['msg']}")
    if not args.aplicar:
        print("(sem --aplicar: nada foi gravado)")
        return 0
    for c in cs:
        p = RAIZ / c["doc"]["caminho"]
        texto = p.read_bytes().decode("utf-8")
        p.write_bytes(editar(texto, c).encode("utf-8"))
    co.gravar(RAIZ / RELATORIO, relatorio(r, cs))
    print(f"{len(cs)} documentos editados; relatório em {RELATORIO}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
