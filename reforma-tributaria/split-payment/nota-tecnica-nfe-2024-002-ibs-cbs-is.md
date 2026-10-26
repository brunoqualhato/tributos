---
titulo: "Nota Técnica Conjunta ENCAT / RFB nº 2024.002 (Reforma Tributária do Consumo na NF-e e NFC-e: Leiautes XML de IBS Estadual/Municipal, CBS e Imposto Seletivo)"
esfera: "Federal"
orgao: "Secretaria Especial da Receita Federal do Brasil / ENCAT - CONFAZ"
tipo: "Nota Técnica Conjunta"
numero: "2024.002"
data: "2024-08-01"
ano: "2024"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS", "Imposto Seletivo", "ICMS", "ISS", "IPI", "PIS", "Cofins"]
situacao: "Em vigor"
revogada: false
fonte: "https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY="
ementa: "Estabelece as especificações técnicas e os novos grupos de campos XML da Nota Fiscal Eletrônica (NF-e, modelo 55) e da Nota Fiscal de Consumidor Eletrônica (NFC-e, modelo 65) para apuração do Imposto sobre Bens e Serviços (IBS Estadual e Municipal), da Contribuição sobre Bens e Serviços (CBS) e do Imposto Seletivo (IS) a partir de 2026."
---

# Nota Técnica Conjunta ENCAT / RFB nº 2024.002 (Reforma Tributária do Consumo na NF-e e NFC-e: Leiautes XML de IBS Estadual/Municipal, CBS e Imposto Seletivo)

NOTA TÉCNICA CONJUNTA ENCAT / RECEITA FEDERAL DO BRASIL Nº 2024.002 — ADEQUAÇÃO DOS DOCUMENTOS FISCAIS ELETRÔNICOS À EMENDA CONSTITUCIONAL Nº 132/2023 E AO PLP Nº 68/2024

## 1. Mudança de Paradigma nas Operações entre Estados e Municípios: Do Princípio da Origem Mista para o Princípio do Destino Pleno

Com a implementação do **IBS (Imposto sobre Bens e Serviços — competência compartilhada de Estados e Municípios)** e da **CBS (Contribuição sobre Bens e Serviços — competência Federal)**:
1. **Tributação Integral no Destino (Fim da Alíquota Interestadual de Origem no IBS):**
   - Diferentemente do ICMS atual (em que parte fica na origem via 4%, 7% ou 12% e parte vai para o destino via DIFAL ou ST), no **IBS 100% da alíquota aplicável é a alíquota da Unidade Federada (`pIBSUF`) e do Município (`pIBSMun`) de destino da operação** (local da entrega/disponibilização do bem ou fruição do serviço).
2. **Cálculo "Por Fora" Unificado:**
   - O IBS e a CBS **não integram sua própria base de cálculo** nem a base um do outro (cálculo estritamente *por fora*), extinguindo a sistemática de cálculo "por dentro" do ICMS.

---

## 2. Novos Grupos e Tags XML do Item da NF-e / NFC-e (`Grupo UB — Tributos do Consumo`)

Durante o período de transição (2026 a 2032), o grupo de impostos (`<imposto>`) de cada item (`<det>`) da NF-e conviverá simultaneamente com os grupos atuais (`<ICMS>`, `<IPI>`, `<PIS>`, `<COFINS>`) e os novos grupos da Reforma Tributária:

### 2.1. Grupo `<IS>` — Imposto Seletivo Federal (Monofásico)
- **`<CSTIS>`:** Código de Situação Tributária do Imposto Seletivo;
- **`<cClassTribIS>`:** Código de Classificação Tributária do Imposto Seletivo;
- **`<vBCIS>`:** Valor da Base de Cálculo do Imposto Seletivo (o IS **integra** a base de cálculo do IBS, da CBS e, durante a transição, do ICMS e do ISS);
- **`<pIS>` e `<pISEspec>`:** Alíquota *ad valorem* (%) e alíquota específica (*ad rem* por unidade de medida tributável `uTrib`: litro, kg, maço, kW);
- **`<vIS>`:** Valor resultante do Imposto Seletivo.

### 2.2. Grupo `<IBSCBS>` — Imposto sobre Bens e Serviços (Estadual + Municipal) e Contribuição sobre Bens e Serviços (Federal)
- **`<CST>`:** Código de Situação Tributária unificado do IBS e da CBS (tabela nacional parametrizada pelo Comitê Gestor do IBS e pela RFB: tributação integral, alíquota reduzida em 30%/60%/100%, diferimento, suspensão, regime específico monofásico, imunidade/exportação);
- **`<cClassTrib>`:** Código de Classificação Tributária do IBS e da CBS (vincula o item exatamente ao artigo, inciso e anexo do PLP 68/2024: cesta básica nacional alíquota zero, saúde/educação redução de 60%, insumos agropecuários, etc.);
- **`<gIBSCBS>` — Detalhamento da Base e das 3 Parcelas Federativas:**
  - **`<vBC>`:** Base de cálculo única comum ao IBS Estadual, ao IBS Municipal e à CBS Federal (valor da operação + Imposto Seletivo, **sem** ICMS, ISS, PIS, COFINS, IBS e CBS);
  - **Subgrupo `<gIBSUF>` (Parcela Estadual do IBS — UF de Destino):**
    - `<pIBSUF>`: Alíquota do IBS da UF de destino (0,1% em 2026 nos testes; e alíquota estadual progressiva de 2029 a 2033 conforme redução de 1/10 ao ano do ICMS);
    - `<pRedAliq>` e `<pAliqEfet>`: Percentual de redução da alíquota (ex.: 60% ou 30%) e alíquota efetiva resultante;
    - `<vIBSUF>`: Valor do IBS devido ao Estado de destino;
  - **Subgrupo `<gIBSMun>` (Parcela Municipal do IBS — Município de Destino):**
    - `<pIBSMun>`, `<pRedAliq>`, `<pAliqEfet>` e `<vIBSMun>`: Valor do IBS devido ao Município de destino;
  - **Subgrupo `<gCBS>` (Parcela Federal da CBS — União):**
    - `<pCBS>`: Alíquota da CBS (0,9% no ano-teste de 2026; e alíquota plena a partir de 2027 com a extinção do PIS e da COFINS);
    - `<pRedAliq>`, `<pAliqEfet>` e `<vCBS>`: Valor da CBS devida à União.

---

## 3. Novos Eventos e Finalidades de Nota Fiscal Eletrônica na Reforma Tributária (`finNFe`)

Além das finalidades atuais (`1=Normal`, `2=Complementar`, `3=Ajuste`, `4=Devolução`), a Nota Técnica 2024.002 introduz as **Notas Fiscais de Débito e de Crédito Eletrônicas** para ajustes financeiros e vinculação ao **Split Payment** (liquidação financeira com segregação automática do IBS e da CBS que condiciona a apropriação do crédito pelo adquirente).
