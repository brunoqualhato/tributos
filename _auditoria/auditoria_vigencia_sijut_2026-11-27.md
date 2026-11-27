# Auditoria de vigência e fonte dos documentos Sijut (27/11/2026)

Consulta ao Sijut em 27/11/2026, por `python3 scripts/reconciliar_vigencia_sijut_2026.py`. Cada documento cujo `fonte` aponta para o Sijut (`/externa/<idAto>`) foi comparado com o campo `vigente` e com as notas (`ancorasNoAto`) de `visao/original` do ato. Só a revogação integral que nomeia o revogador (`[Revogado(a) pelo(a) <ato>]`) altera o documento (`situacao: "Revogada"` e `revogada: true`); nenhuma outra linha é tocada.

## Resumo

- Arquivos do acervo com fonte no Sijut: 742; idAtos distintos: 741 pelo `fonte` atual e 736 depois de corrigir as fontes e tirar o documento sem fonte localizada (documentos que passam a compartilhar o idAto de outro arquivo).
- Vigentes no Sijut: 674; com `vigente` falso: 62.
- Revogações inequívocas (idAtos): 60; documentos alterados por revogação: 62.
- Ambíguas (só relatório): 2.
- Sentido inverso (documento Revogada e Sijut vigente): 0.
- `fonte` divergentes: 8 (7 corrigidas, 1 só relatada).

## Revogações inequívocas corrigidas

| # | Documento | idAto | Revogado por (nota oficial do Sijut) | Revogador no acervo |
|---|---|---|---|---|
| 1 | `reguladores/mte-caixa/fgts-esocial/portaria-conjunta-rfb-mps-mte-44-2023-esocial.md` | 132735 | Portaria Conjunta RFB / MPS / MTE nº 13, de 25 de junho de 2024 | sim |
| 2 | `reguladores/rfb/instrucoes-normativas/2011/ato-36692-1208-2011.md` | 36692 | Instrução Normativa RFB nº 2111, de 20 de outubro de 2022 | não |
| 3 | `reguladores/rfb/instrucoes-normativas/2011/ato-36794-1211-2011.md` | 36794 | Instrução Normativa RFB nº 1289, de 4 de setembro de 2012 | não |
| 4 | `reguladores/rfb/instrucoes-normativas/2011/ato-37094-1223-2011.md` | 37094 | Instrução Normativa RFB nº 1928, de 24 de março de 2020 | não |
| 5 | `reguladores/rfb/instrucoes-normativas/2011/ato-37095-1224-2011.md` | 37095 | Instrução Normativa RFB nº 1300, de 20 de novembro de 2012 | não |
| 6 | `reguladores/rfb/instrucoes-normativas/2011/ato-37097-1226-2011.md` | 37097 | Instrução Normativa RFB nº 2287, de 28 de outubro de 2025 | não |
| 7 | `reguladores/rfb/instrucoes-normativas/2011/ato-37127-1229-2011.md` | 37127 | Instrução Normativa RFB nº 1508, de 4 de novembro de 2014 | não |
| 8 | `reguladores/rfb/instrucoes-normativas/2012/ato-39257-1312-2012.md` | 39257 | Instrução Normativa RFB nº 2161, de 28 de setembro de 2023 | não |
| 9 | `reguladores/rfb/instrucoes-normativas/2013/ato-48807-1425-2013.md` | 48807 | Instrução Normativa RFB nº 1717, de 17 de julho de 2017 | não |
| 10 | `reguladores/rfb/instrucoes-normativas/2014/ato-59786-1539-2014.md` | 59786 | Instrução Normativa RFB nº 1883, de 11 de abril de 2019 | não |
| 11 | `reguladores/rfb/instrucoes-normativas/2015/ato-69971-1597-2015.md` | 69971 | Instrução Normativa RFB nº 2053, de 6 de dezembro de 2021 | sim |
| 12 | `reguladores/rfb/instrucoes-normativas/2015/ato-70249-1599-2015.md` | 70249 | Instrução Normativa RFB nº 2005, de 29 de janeiro de 2021 | sim |
| 13 | `reguladores/rfb/instrucoes-normativas/2016/ato-79344-1678-2016.md` | 79344 | Instrução Normativa RFB nº 1986, de 29 de outubro de 2020 | não |
| 14 | `reguladores/rfb/instrucoes-normativas/2016/ato-79445-1682-2016.md` | 79445 | Instrução Normativa RFB nº 2060, de 13 de dezembro de 2021 | não |
| 15 | `reguladores/rfb/instrucoes-normativas/2019/ato-100592-1888-2019.md` | 100592 | Instrução Normativa RFB nº 2291, de 14 de novembro de 2025 | sim |
| 16 | `reguladores/rfb/instrucoes-normativas/2021/ato-115131-2005-2021.md` | 115131 | Instrução Normativa RFB nº 2237, de 4 de dezembro de 2024 | sim |
| 17 | `reguladores/rfb/instrucoes-normativas/2022/ato-124859-2092-2022.md` | 124859 | Instrução Normativa RFB nº 2121, de 15 de dezembro de 2022 | sim |
| 18 | `reguladores/rfb/instrucoes-normativas/2022/ato-125060-2094-2022.md` | 125060 | Instrução Normativa RFB nº 2237, de 4 de dezembro de 2024 | sim |
| 19 | `reguladores/rfb/instrucoes-normativas/2022/ato-126432-2107-2022.md` | 126432 | Instrução Normativa RFB nº 2110, de 17 de outubro de 2022 | sim |
| 20 | `reguladores/rfb/instrucoes-normativas/2022/ato-126434-2109-2022.md` | 126434 | Instrução Normativa RFB nº 2121, de 15 de dezembro de 2022 | sim |
| 21 | `reguladores/rfb/instrucoes-normativas/financeiro/in-rfb-1888-2019-criptoativos.md` | 100592 | Instrução Normativa RFB nº 2291, de 14 de novembro de 2025 | sim |
| 22 | `reguladores/rfb/outros-atos/2001/ato-5605-7-2001.md` | 5605 | Instrução Normativa SRF nº 247, de 21 de novembro de 2002 | não |
| 23 | `reguladores/rfb/outros-atos/2002/ato-5707-26-2002.md` | 5707 | Instrução Normativa SRF nº 296, de 6 de fevereiro de 2003 | não |
| 24 | `reguladores/rfb/outros-atos/2007/ato-5685-20-2007.md` | 5685 | Ato Declaratório Interpretativo RFB nº 26, de 25 de abril de 2008 | não |
| 25 | `reguladores/rfb/outros-atos/2010/ato-28821-587-2010.md` | 28821 | Portaria MF nº 203, de 14 de maio de 2012 | não |
| 26 | `reguladores/rfb/outros-atos/2010/ato-30584-2466-2010.md` | 30584 | Portaria RFB nº 1215, de 23 de julho de 2020 | não |
| 27 | `reguladores/rfb/outros-atos/2010/ato-5454-97-2010.md` | 5454 | Ato Declaratório Executivo Codac nº 99, de 29 de dezembro de 2011 | não |
| 28 | `reguladores/rfb/outros-atos/2012/ato-39122-107-2012.md` | 39122 | Ato Declaratório Executivo Codac nº 9, de 20 de fevereiro de 2013 | não |
| 29 | `reguladores/rfb/outros-atos/2012/ato-39228-105-2012.md` | 39228 | Resolução CGSN nº 140, de 22 de maio de 2018 | sim |
| 30 | `reguladores/rfb/outros-atos/2013/ato-48632-19-2013.md` | 48632 | Ato Declaratório Executivo SRRF02 nº 4, de 12 de março de 2020 | não |
| 31 | `reguladores/rfb/outros-atos/2015/ato-70597-123-2015.md` | 70597 | Portaria Coana nº 72, de 29 de outubro de 2020 | não |
| 32 | `reguladores/rfb/outros-atos/2015/ato-70620-1754-2015.md` | 70620 | Portaria RFB nº 1713, de 22 de dezembro de 2016 | não |
| 33 | `reguladores/rfb/outros-atos/2015/ato-70662-217-2015.md` | 70662 | Portaria DRF/CTA nº 148, de 7 de outubro de 2016 | não |
| 34 | `reguladores/rfb/outros-atos/2016/ato-79132-130-2016.md` | 79132 | Resolução CGSN nº 156, de 29 de setembro de 2020 | não |
| 35 | `reguladores/rfb/outros-atos/2017/ato-89021-6447-2017.md` | 89021 | Portaria RFB nº 460, de 17 de setembro de 2024 | não |
| 36 | `reguladores/rfb/outros-atos/2020/ato-114629-4-2020.md` | 114629 | Ato Declaratório Executivo SRRF03 nº 1, de 22 de fevereiro de 2021 | não |
| 37 | `reguladores/rfb/outros-atos/2021/ato-122412-102-2021.md` | 122412 | Portaria Conjunta RFB / PGFN nº 64, de 2 de agosto de 2022 | sim |
| 38 | `reguladores/rfb/outros-atos/2021/ato-122425-20-2021.md` | 122425 | Portaria ALF/ITJ nº 56, de 23 de fevereiro de 2024 | não |
| 39 | `reguladores/rfb/outros-atos/2022/ato-122738-1-2022.md` | 122738 | Portaria IRF/SLS nº 1, de 18 de abril de 2023 | não |
| 40 | `reguladores/rfb/outros-atos/2022/ato-124717-81-2022.md` | 124717 | Portaria Coana nº 159, de 5 de agosto de 2024 | não |
| 41 | `reguladores/rfb/outros-atos/2022/ato-125375-64-2022.md` | 125375 | Portaria Conjunta RFB / PGFN nº 103, de 21 de dezembro de 2022 | sim |
| 42 | `reguladores/rfb/outros-atos/2022/ato-126900-242-2022.md` | 126900 | Portaria RFB nº 309, de 31 de março de 2023 | sim |
| 43 | `reguladores/rfb/outros-atos/2022/ato-127603-12-2022.md` | 127603 | Ato Declaratório Executivo DRF/BSB nº 19, de 28 de dezembro de 2022 | sim |
| 44 | `reguladores/rfb/outros-atos/2022/ato-127606-15-2022.md` | 127606 | Ato Declaratório Executivo DRF/BSB nº 20, de 28 de dezembro de 2022 | sim |
| 45 | `reguladores/rfb/outros-atos/2022/ato-127607-16-2022.md` | 127607 | Ato Declaratório Executivo DRF/BSB nº 21, de 28 de dezembro de 2022 | sim |
| 46 | `reguladores/rfb/outros-atos/2022/ato-127608-17-2022.md` | 127608 | Ato Declaratório Executivo DRF/BSB nº 22, de 28 de dezembro de 2022 | sim |
| 47 | `reguladores/rfb/outros-atos/2022/ato-127749-214-2022.md` | 127749 | Ato Declaratório Executivo DRF/SOR nº 905, de 7 de agosto de 2025 | não |
| 48 | `reguladores/rfb/outros-atos/2022/ato-127750-215-2022.md` | 127750 | Ato Declaratório Executivo DRF/SOR nº 905, de 7 de agosto de 2025 | não |
| 49 | `reguladores/rfb/outros-atos/2022/ato-127962-150-2022.md` | 127962 | Ato Declaratório Executivo Decex/RJO nº 56, de 22 de março de 2024 | não |
| 50 | `reguladores/rfb/outros-atos/2022/ato-127965-66-2022.md` | 127965 | Portaria ALF/VCP nº 74, de 13 de fevereiro de 2023 | não |
| 51 | `reguladores/rfb/outros-atos/2022/ato-127977-103-2022.md` | 127977 | Portaria Conjunta RFB / PGFN nº 391, de 27 de dezembro de 2023 | sim |
| 52 | `reguladores/rfb/outros-atos/2022/ato-128016-277-2022.md` | 128016 | Portaria RFB nº 607, de 6 de novembro de 2025 | não |
| 53 | `reguladores/rfb/outros-atos/2022/ato-132784-33-2022.md` | 132784 | Portaria Conjunta RFB / MPS / MTE nº 44, de 11 de agosto de 2023 | sim |
| 54 | `reguladores/rfb/outros-atos/2023/ato-130676-319-2023.md` | 130676 | Portaria RFB nº 744, de 28 de outubro de 2026 | não |
| 55 | `reguladores/rfb/outros-atos/2023/ato-132670-133-2023.md` | 132670 | Portaria Coana nº 164, de 12 de setembro de 2024 | não |
| 56 | `reguladores/rfb/outros-atos/2023/ato-132735-44-2023.md` | 132735 | Portaria Conjunta RFB / MPS / MTE nº 13, de 25 de junho de 2024 | sim |
| 57 | `reguladores/rfb/outros-atos/2023/ato-133034-346-2023.md` | 133034 | Portaria RFB nº 520, de 5 de março de 2025 | não |
| 58 | `reguladores/rfb/outros-atos/2023/ato-134080-368-2023.md` | 134080 | Portaria RFB nº 501, de 20 de dezembro de 2024 | não |
| 59 | `reguladores/rfb/outros-atos/2023/ato-135324-14-2023.md` | 135324 | Ato Declaratório Executivo Coana nº 51, de 1º de agosto de 2025 | não |
| 60 | `reguladores/rfb/outros-atos/2023/ato-135349-847-2023.md` | 135349 | Ato Declaratório Executivo DRF/SOR nº 221, de 6 de março de 2025 | não |
| 61 | `reguladores/rfb/outros-atos/2023/ato-135371-15-2023.md` | 135371 | Ato Declaratório Executivo Coana nº 57, de 8 de agosto de 2025 | não |
| 62 | `reguladores/rfb/outros-atos/2024/ato-141278-477-2024.md` | 141278 | Portaria RFB nº 744, de 28 de outubro de 2026 | não |

## Revogados por ato fora do acervo

41 dos documentos revogados têm o ato revogador fora do acervo. O documento revogado continua no acervo como registro histórico, agora com `situacao: "Revogada"`.

- `reguladores/rfb/instrucoes-normativas/2011/ato-36692-1208-2011.md`: Instrução Normativa RFB nº 2111, de 20 de outubro de 2022
- `reguladores/rfb/instrucoes-normativas/2011/ato-36794-1211-2011.md`: Instrução Normativa RFB nº 1289, de 4 de setembro de 2012
- `reguladores/rfb/instrucoes-normativas/2011/ato-37094-1223-2011.md`: Instrução Normativa RFB nº 1928, de 24 de março de 2020
- `reguladores/rfb/instrucoes-normativas/2011/ato-37095-1224-2011.md`: Instrução Normativa RFB nº 1300, de 20 de novembro de 2012
- `reguladores/rfb/instrucoes-normativas/2011/ato-37097-1226-2011.md`: Instrução Normativa RFB nº 2287, de 28 de outubro de 2025
- `reguladores/rfb/instrucoes-normativas/2011/ato-37127-1229-2011.md`: Instrução Normativa RFB nº 1508, de 4 de novembro de 2014
- `reguladores/rfb/instrucoes-normativas/2012/ato-39257-1312-2012.md`: Instrução Normativa RFB nº 2161, de 28 de setembro de 2023
- `reguladores/rfb/instrucoes-normativas/2013/ato-48807-1425-2013.md`: Instrução Normativa RFB nº 1717, de 17 de julho de 2017
- `reguladores/rfb/instrucoes-normativas/2014/ato-59786-1539-2014.md`: Instrução Normativa RFB nº 1883, de 11 de abril de 2019
- `reguladores/rfb/instrucoes-normativas/2016/ato-79344-1678-2016.md`: Instrução Normativa RFB nº 1986, de 29 de outubro de 2020
- `reguladores/rfb/instrucoes-normativas/2016/ato-79445-1682-2016.md`: Instrução Normativa RFB nº 2060, de 13 de dezembro de 2021
- `reguladores/rfb/outros-atos/2001/ato-5605-7-2001.md`: Instrução Normativa SRF nº 247, de 21 de novembro de 2002
- `reguladores/rfb/outros-atos/2002/ato-5707-26-2002.md`: Instrução Normativa SRF nº 296, de 6 de fevereiro de 2003
- `reguladores/rfb/outros-atos/2007/ato-5685-20-2007.md`: Ato Declaratório Interpretativo RFB nº 26, de 25 de abril de 2008
- `reguladores/rfb/outros-atos/2010/ato-28821-587-2010.md`: Portaria MF nº 203, de 14 de maio de 2012
- `reguladores/rfb/outros-atos/2010/ato-30584-2466-2010.md`: Portaria RFB nº 1215, de 23 de julho de 2020
- `reguladores/rfb/outros-atos/2010/ato-5454-97-2010.md`: Ato Declaratório Executivo Codac nº 99, de 29 de dezembro de 2011
- `reguladores/rfb/outros-atos/2012/ato-39122-107-2012.md`: Ato Declaratório Executivo Codac nº 9, de 20 de fevereiro de 2013
- `reguladores/rfb/outros-atos/2013/ato-48632-19-2013.md`: Ato Declaratório Executivo SRRF02 nº 4, de 12 de março de 2020
- `reguladores/rfb/outros-atos/2015/ato-70597-123-2015.md`: Portaria Coana nº 72, de 29 de outubro de 2020
- `reguladores/rfb/outros-atos/2015/ato-70620-1754-2015.md`: Portaria RFB nº 1713, de 22 de dezembro de 2016
- `reguladores/rfb/outros-atos/2015/ato-70662-217-2015.md`: Portaria DRF/CTA nº 148, de 7 de outubro de 2016
- `reguladores/rfb/outros-atos/2016/ato-79132-130-2016.md`: Resolução CGSN nº 156, de 29 de setembro de 2020
- `reguladores/rfb/outros-atos/2017/ato-89021-6447-2017.md`: Portaria RFB nº 460, de 17 de setembro de 2024
- `reguladores/rfb/outros-atos/2020/ato-114629-4-2020.md`: Ato Declaratório Executivo SRRF03 nº 1, de 22 de fevereiro de 2021
- `reguladores/rfb/outros-atos/2021/ato-122425-20-2021.md`: Portaria ALF/ITJ nº 56, de 23 de fevereiro de 2024
- `reguladores/rfb/outros-atos/2022/ato-122738-1-2022.md`: Portaria IRF/SLS nº 1, de 18 de abril de 2023
- `reguladores/rfb/outros-atos/2022/ato-124717-81-2022.md`: Portaria Coana nº 159, de 5 de agosto de 2024
- `reguladores/rfb/outros-atos/2022/ato-127749-214-2022.md`: Ato Declaratório Executivo DRF/SOR nº 905, de 7 de agosto de 2025
- `reguladores/rfb/outros-atos/2022/ato-127750-215-2022.md`: Ato Declaratório Executivo DRF/SOR nº 905, de 7 de agosto de 2025
- `reguladores/rfb/outros-atos/2022/ato-127962-150-2022.md`: Ato Declaratório Executivo Decex/RJO nº 56, de 22 de março de 2024
- `reguladores/rfb/outros-atos/2022/ato-127965-66-2022.md`: Portaria ALF/VCP nº 74, de 13 de fevereiro de 2023
- `reguladores/rfb/outros-atos/2022/ato-128016-277-2022.md`: Portaria RFB nº 607, de 6 de novembro de 2025
- `reguladores/rfb/outros-atos/2023/ato-130676-319-2023.md`: Portaria RFB nº 744, de 28 de outubro de 2026
- `reguladores/rfb/outros-atos/2023/ato-132670-133-2023.md`: Portaria Coana nº 164, de 12 de setembro de 2024
- `reguladores/rfb/outros-atos/2023/ato-133034-346-2023.md`: Portaria RFB nº 520, de 5 de março de 2025
- `reguladores/rfb/outros-atos/2023/ato-134080-368-2023.md`: Portaria RFB nº 501, de 20 de dezembro de 2024
- `reguladores/rfb/outros-atos/2023/ato-135324-14-2023.md`: Ato Declaratório Executivo Coana nº 51, de 1º de agosto de 2025
- `reguladores/rfb/outros-atos/2023/ato-135349-847-2023.md`: Ato Declaratório Executivo DRF/SOR nº 221, de 6 de março de 2025
- `reguladores/rfb/outros-atos/2023/ato-135371-15-2023.md`: Ato Declaratório Executivo Coana nº 57, de 8 de agosto de 2025
- `reguladores/rfb/outros-atos/2024/ato-141278-477-2024.md`: Portaria RFB nº 744, de 28 de outubro de 2026

## Ambíguas (sem edição)

`vigente` falso sem nota de revogação integral. Suspensão e 'sem efeito' não equivalem a revogação e não têm texto canônico em `situacao`; o documento fica como está.

| Documento | idAto | Evidência no Sijut |
|---|---|---|
| `reguladores/rfb/outros-atos/2022/ato-125275-1-2022.md` | 125275 | [Execução suspensa pelo(a) Ato Declaratório Executivo RFB nº 1, de 15 de janeiro de 2024] |
| `reguladores/rfb/outros-atos/2023/ato-135359-843-2023.md` | 135359 | [Sem efeito pelo(a) Ato Declaratório Executivo DRF/SOR nº 248, de 13 de março de 2025] |

## `fonte` que apontava para outro ato

O idAto antigo descreve outro ato. A troca só é feita quando número e ano do título do documento aparecem na `epigrafeCompleta` do idAto novo.

| Documento | idAto antigo | Epígrafe do idAto antigo | idAto novo | Epígrafe do idAto novo | Resultado |
|---|---|---|---|---|---|
| `federal/leis-ordinarias/cprb/in-rfb-2053-2021-cprb.md` | 122063 | Ato Declaratório Executivo DRF/REC nº 250, de 8 de dezembro de 2021 | 122005 | Instrução Normativa RFB nº 2053, de 6 de dezembro de 2021 | fonte trocada |
| `federal/leis-ordinarias/irrf-servicos/in-srf-459-2004-csrf-retencao-servicos.md` | 14683 | Instrução Normativa DPRF nº 107, de 26 de novembro de 1991 | 15365 | Instrução Normativa SRF nº 459, de 18 de outubro de 2004 | fonte trocada |
| `federal/leis-ordinarias/offshores/in-rfb-2180-2024-offshores-trusts.md` | 136675 | Solução de Consulta Cosit nº 27, de 14 de março de 2024 | 136603 | Instrução Normativa RFB nº 2180, de 11 de março de 2024 | fonte trocada |
| `federal/portarias/mf/portaria-mf-612-2023-remessa-conforme.md` | 132277 | Ato Declaratório Executivo DRF/MCR nº 267, de 24 de julho de 2023 | 131703 | Portaria MF nº 612, de 29 de junho de 2023 | fonte trocada |
| `reguladores/mte-caixa/fgts-esocial/portaria-conjunta-rfb-mps-mte-44-2023-esocial.md` | 132906 | Solução de Consulta Disit/SRRF03 nº 3014, de 21 de agosto de 2023 | 132735 | Portaria Conjunta RFB / MPS / MTE nº 44, de 11 de agosto de 2023 | fonte trocada; marcada Revogada (ato revogado por Portaria Conjunta RFB / MPS / MTE nº 13, de 25 de junho de 2024) |
| `reguladores/rfb/instrucoes-normativas/financeiro/ato-in-1585-2015.md` | 67812 | Ato Declaratório Executivo DRF/SJR nº 38, de 11 de setembro de 2015 | 67494 | Instrução Normativa RFB nº 1585, de 31 de agosto de 2015 | fonte trocada |
| `reguladores/rfb/instrucoes-normativas/financeiro/in-rfb-1888-2019-criptoativos.md` | 100733 | Ato Declaratório Executivo DRF/ANA nº 28, de 13 de maio de 2019 | 100592 | Instrução Normativa RFB nº 1888, de 3 de maio de 2019 | fonte trocada; marcada Revogada (ato revogado por Instrução Normativa RFB nº 2291, de 14 de novembro de 2025) |
| `reguladores/rfb/rat-fap-terceiros/portaria-conjunta-rfb-inss-1-2021-ntep.md` | 112340 | Instrução Normativa SRF nº 14, de 2 de dezembro de 1969 (vigente falso; revogado por Instrução Normativa SRF nº 79, de 1º de agosto de 2000) | não localizado | o ato do documento (Portaria Conjunta RFB/INSS nº 1/2021, NTEP) não foi encontrado no Sijut por tipo, número, ano nem por 'Nexo Técnico Epidemiológico' | só relatório; verificar a origem do texto antes de manter o documento |

## Sentido inverso

Nenhum caso.
