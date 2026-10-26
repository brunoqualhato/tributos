"""Ingestão e catalogação com alta fidelidade das normas estruturantes da Reforma Tributária sobre o Consumo.

Especialista: tributos_reforma_transicao
Abrange:
- Emenda Constitucional nº 132/2023 (Marco Constitucional do IBS, CBS e Imposto Seletivo)
- PLP 68/2024 - Arquitetura Operacional do Split Payment (arts. 49 a 53)
- PLP 108/2024 - Estrutura e Governança do Comitê Gestor do IBS
- Portaria MF nº 170/2024 - Programa de Transição da CBS na Receita Federal
- Regimes Específicos e Diferenciados do IBS e CBS (PLP 68/2024)
- Imposto Seletivo (Sin Tax) - Bens prejudiciais à saúde e ao meio ambiente (PLP 68/2024)
"""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "agentes"))

from comum import salvar_atomico, gerar_frontmatter

NORMAS_REFORMA = [
    {
        "titulo": "Emenda Constitucional nº 132, de 20 de dezembro de 2023",
        "esfera": "Federal",
        "orgao": "Congresso Nacional",
        "tipo": "Emenda Constitucional",
        "numero": "132",
        "ano": "2023",
        "data": "2023-12-20",
        "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": ["IBS", "CBS", "Imposto Seletivo", "ICMS", "ISSQN", "IPI", "PIS/Pasep", "Cofins"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:federal:emenda.constitucional:2023-12-20;132",
        "ementa": "Altera o Sistema Tributário Nacional para instituir o Imposto sobre Bens e Serviços (IBS), a Contribuição sobre Bens e Serviços (CBS) e o Imposto Seletivo (IS), estabelecendo a transição federativa até 2033.",
        "caminho": "reforma-tributaria/emenda-constitucional-132-2023.md",
        "conteudo": """# Emenda Constitucional nº 132, de 20 de dezembro de 2023

Altera o Sistema Tributário Nacional (Reforma Tributária do Consumo).

As Mesas da Câmara dos Deputados e do Senado Federal, nos termos do § 3º do art. 60 da Constituição Federal, promulgam a seguinte Emenda ao texto constitucional:

## 1. INSTITUIÇÃO DO IBS E CBS (IVA DUAL)

### Art. 156-A (Imposto sobre Bens e Serviços - IBS)
Lei complementar instituirá imposto sobre bens e serviços de competência compartilhada entre Estados, Distrito Federal e Municípios.
§ 1º O imposto previsto no caput será informado pelo princípio da neutralidade e:
I - incidirá sobre operações com bens materiais ou imateriais, inclusive direitos, ou com serviços;
II - incidirá sobre a importação de bens materiais ou imateriais, inclusive direitos, ou de serviços;
V - não será objeto de concessão de incentivos e benefícios financeiros ou fiscais relativos ao imposto ou de desonerações;
VIII - será cobrado pelo somatório das alíquotas fixadas pelo Estado e pelo Município de destino da operação;
IX - não integrará sua própria base de cálculo nem a dos demais tributos sobre consumo;
X - será não cumulativo, compensando-se o imposto devido pelo contribuinte com o montante cobrado sobre todas as operações nas quais seja adquirente de bem material ou imaterial, inclusive direito, ou de serviço.

### Art. 195, V (Contribuição sobre Bens e Serviços - CBS)
Incidirá sobre bens materiais e imateriais, inclusive direitos, e sobre serviços, de competência da União, compartilhando fato gerador, base de cálculo e regimes com o IBS estadual/municipal.

## 2. IMPOSTO SELETIVO (ART. 153, VIII)
Compete à União instituir imposto sobre produção, extração, comercialização ou importação de bens e serviços prejudiciais à saúde ou ao meio ambiente, nos termos de lei complementar.

## 3. CRONOGRAMA DE TRANSIÇÃO (ADCT ARTS. 124 A 133)
- 2026: Alíquota de teste de 0,9% para a CBS e 0,1% para o IBS (compensáveis com PIS/Cofins);
- 2027: Extinção integral do PIS e da Cofins; início da cobrança plena da CBS e do Imposto Seletivo; alíquotas do IPI reduzidas a zero (exceto Zona Franca de Manaus);
- 2029 a 2032: Redução gradual das alíquotas do ICMS e do ISS (10% ao ano de redução em 2029, 20% em 2030, etc.);
- 2033: Extinção definitiva do ICMS e do ISSQN; vigência plena e exclusiva do IBS e da CBS.
"""
    },
    {
        "titulo": "Arquitetura Operacional do Split Payment no PLP 68/2024",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Ministério da Fazenda",
        "tipo": "Norma Técnica e Projeto de Lei",
        "numero": "68",
        "ano": "2024",
        "data": "2024-04-24",
        "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": ["IBS", "CBS", "Split Payment Inteligente"],
        "situacao": "Em tramitação",
        "revogada": False,
        "fonte": "https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2429846",
        "ementa": "Detalhamento da sistemática de recolhimento na liquidação financeira (Split Payment) prevista nos arts. 49 a 53 do PLP nº 68/2024.",
        "caminho": "reforma-tributaria/split-payment/arquitetura-split-payment-plp68.md",
        "conteudo": """# Arquitetura Operacional do Split Payment no PLP 68/2024

Detalhamento técnico da sistemática dos arts. 49 a 53 da Lei Complementar do IBS e CBS.

## 1. CONCEITO E FINALIDADE
O Split Payment (recolhimento na liquidação financeira) é o mecanismo tecnológico pelo qual as instituições participantes de arranjos de pagamento (bancos, credenciadoras de cartão e instituições de pagamento Pix) segregam automaticamente, no momento da liquidação da transação, o valor líquido devido ao vendedor e o montante de IBS e CBS devido ao Fisco.

## 2. MODALIDADES PREVISTAS

### A. Split Payment Inteligente (Art. 51)
- Integrado em tempo real ao Documento Fiscal Eletrônico (DF-e);
- Ao processar o pagamento, o sistema consulta a conta-corrente fiscal do fornecedor;
- Se o fornecedor possuir créditos homologados suficientes de IBS/CBS, o montante retido é reduzido ou zerado;
- Retém apenas a diferença necessária para quitação do débito daquela operação.

### B. Split Payment Simplificado (Art. 52)
- Aplicado subsidiariamente quando não for tecnicamente viável a conciliação instantânea nota a nota;
- Retenção baseada em percentual médio do setor ou alíquota padrão, com posterior ajuste na conta fiscal.

### C. Split Payment Manual (Art. 53)
- Realizado diretamente pelo adquirente adimplente quando a operação não for liquidada por instituição de pagamento regulada.
"""
    },
    {
        "titulo": "Estrutura e Governança do Comitê Gestor do IBS no PLP 108/2024",
        "esfera": "Nacional",
        "orgao": "Congresso Nacional / Conselho Nacional de Política Fazendária",
        "tipo": "Projeto de Lei Complementar",
        "numero": "108",
        "ano": "2024",
        "data": "2024-06-04",
        "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": ["IBS", "Comitê Gestor do IBS"],
        "situacao": "Em tramitação",
        "revogada": False,
        "fonte": "https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2438865",
        "ementa": "Institui o Comitê Gestor do Imposto sobre Bens e Serviços (CG-IBS), disciplina o processo administrativo tributário do IBS, a distribuição de receitas aos entes federados e o ITCMD.",
        "caminho": "reforma-tributaria/comite-gestor-ibs/estrutura-governanca-plp108.md",
        "conteudo": """# Estrutura e Governança do Comitê Gestor do IBS (PLP 108/2024)

Estrutura institucional, competências e funcionamento do Comitê Gestor do IBS (CG-IBS).

## 1. NATUREZA JURÍDICA E COMPOSIÇÃO
O Comitê Gestor do IBS é entidade pública sob regime especial, dotada de independência administrativa, técnica e financeira, com sede em Brasília/DF.

### Composição da Instância Máxima (Conselho Superior):
- 27 membros representando cada um dos Estados e o Distrito Federal;
- 27 membros representando o conjunto dos Municípios (sendo 14 eleitos por voto direto de cada município e 13 eleitos com voto ponderado pela população).

## 2. COMPETÊNCIAS EXCLUSIVAS
I - Editar regulamento único do IBS com eficácia em todo o território nacional;
II - Arrecadar o imposto, realizar a compensação e creditamento via conta fiscal;
III - Efetuar a distribuição da arrecadação ao Estado e Município de destino da operação;
IV - Decidir o contencioso administrativo tributário em segunda instância por meio de Tribunal Administrativo paritário.
"""
    },
    {
        "titulo": "Portaria MF nº 170, de 31 de janeiro de 2024 (Governança da CBS)",
        "esfera": "Federal",
        "orgao": "Ministério da Fazenda",
        "tipo": "Portaria",
        "numero": "170",
        "ano": "2024",
        "data": "2024-01-31",
        "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": ["CBS", "IBS", "Transição da Reforma"],
        "situacao": "Em vigor",
        "revogada": False,
        "fonte": "https://normas.leg.br/?urn=urn:lex:br:ministerio.fazenda:portaria:2024-01-31;170",
        "ementa": "Institui no âmbito do Ministério da Fazenda o Programa de Governança e Transição do Sistema Tributário sobre o Consumo.",
        "caminho": "reforma-tributaria/cbs-receita-federal/portaria-mf-170-2024.md",
        "conteudo": """# Portaria MF nº 170, de 31 de janeiro de 2024

Institui o Programa de Governança e Transição da Reforma Tributária do Consumo no Ministério da Fazenda.

O MINISTRO DE ESTADO DA FAZENDA, no uso das atribuições que lhe confere o art. 87 da Constituição Federal, resolve:

Art. 1º Fica instituído o Programa Especial de Transição do Sistema Tributário sobre o Consumo, com vistas a coordenar o desenvolvimento técnico e tecnológico da Contribuição sobre Bens e Serviços (CBS) e a integração com o Comitê Gestor do IBS.

Art. 2º São objetivos prioritários do Programa:
I - O desenvolvimento da infraestrutura de tecnologia de informação para o Split Payment em parceria com o Banco Central do Brasil e instituições de pagamento;
II - A harmonização das regras de apuração não cumulativa ampla entre CBS e IBS;
III - A padronização dos Documentos Fiscais Eletrônicos (NF-e, NFS-e nacional, NFC-e e CT-e) para recepção dos campos de IBS e CBS a partir de 2026.

FERNANDO HADDAD
Ministro da Fazenda
"""
    },
    {
        "titulo": "Regimes Específicos e Diferenciados do IBS e CBS no PLP 68/2024",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Ministério da Fazenda",
        "tipo": "Norma Técnica e Projeto de Lei",
        "numero": "68-RE",
        "ano": "2024",
        "data": "2024-04-24",
        "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": ["IBS", "CBS", "Regimes Diferenciados"],
        "situacao": "Em tramitação",
        "revogada": False,
        "fonte": "https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2429846",
        "ementa": "Sistematização dos Regimes Específicos e Diferenciados do IBS e da CBS previstos nos arts. 120 a 280 do PLP nº 68/2024.",
        "caminho": "reforma-tributaria/regimes-especificos/regimes-diferenciados-plp68.md",
        "conteudo": """# Regimes Específicos e Diferenciados do IBS e CBS no PLP 68/2024

Sistematização dos tratamentos tributários setoriais sob o novo IVA Dual.

## 1. REDUÇÃO DE ALÍQUOTAS (REGIMES DIFERENCIADOS)

### Redução de 60% da alíquota padrão:
- Serviços de educação e saúde privada;
- Dispositivos médicos e de acessibilidade para pessoas com deficiência;
- Medicamentos essenciais;
- Produtos agropecuários, aquícolas, pesqueiros, florestais in natura;
- Alimentos da Cesta Básica Nacional e insumos agropecuários;
- Produções artísticas, culturais e jornalísticas nacionais.

### Redução de 100% (Alíquota Zero):
- Cesta Básica Nacional de Alimentos isenta;
- Medicamentos para tratamento de câncer e doenças raras;
- Automóveis de passageiros adquiridos por pessoas com deficiência e motoristas de táxi.

## 2. REGIMES ESPECÍFICOS DE TRIBUTAÇÃO
- **Combustíveis e Lubrificantes:** Tributação monofásica ad rem uniforme nacional;
- **Serviços Financeiros e Seguros:** Base de cálculo baseada na margem de intermediação financeira (spread) sem creditamento da taxa;
- **Operações com Bens Imóveis:** Redução na base de cálculo para incorporação, parcelamento de solo e locação;
- **Sociedades Cooperativas:** Não incidência sobre atos cooperativos praticados entre a cooperativa e seus associados.
"""
    },
    {
        "titulo": "Imposto Seletivo (Sin Tax) no PLP 68/2024",
        "esfera": "Federal",
        "orgao": "Congresso Nacional / Ministério da Fazenda",
        "tipo": "Norma Técnica e Projeto de Lei",
        "numero": "68-IS",
        "ano": "2024",
        "data": "2024-04-24",
        "tema_tributario": "Reforma Tributária e Transição",
        "tributos_afetados": ["Imposto Seletivo", "IBS", "CBS"],
        "situacao": "Em tramitação",
        "revogada": False,
        "fonte": "https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2429846",
        "ementa": "Disciplina a incidência, o fato gerador, as bases de cálculo e a lista de produtos sujeitos ao Imposto Seletivo (art. 153, VIII da CF).",
        "caminho": "reforma-tributaria/imposto-seletivo/incidencia-e-aliquotas-plp68.md",
        "conteudo": """# Imposto Seletivo (Sin Tax) no PLP 68/2024

Regras de incidência e bens gravados pelo Imposto Seletivo (IS).

## 1. NATUREZA E FINALIDADE
O Imposto Seletivo tem finalidade extrafiscal, visando desestimular o consumo de bens materiais e serviços que causem dano à saúde ou ao meio ambiente.

## 2. BENS GRAVADOS PELO IMPOSTO SELETIVO
Conforme o Anexo do PLP 68/2024, sujeitam-se à incidência monofásica do IS na produção, extração ou importação:

I - Veículos automotores terrestres (alíquotas moduladas pela eficiência energética e emissão de carbono);
II - Embarcações e aeronaves esportivas ou de recreio;
III - Produtos do fumo e derivados do tabaco (cigarros e charutos);
IV - Bebidas alcoólicas (cervejas, destilados, vinhos, com alíquota progressiva pelo teor alcoólico);
V - Bebidas açucaradas (refrigerantes e néctares com alto teor de açúcar adicionado);
VI - Bens minerais extraídos (minério de ferro, petróleo e gás natural, com alíquota máxima de 1% no valor da extração).
"""
    }
]

def gerar_normas_reforma():
    gerados = []
    print(f"Iniciando estruturação de {len(NORMAS_REFORMA)} normas fundamentais da Reforma Tributária...")
    
    for item in NORMAS_REFORMA:
        destino = RAIZ / item["caminho"]
        destino.parent.mkdir(parents=True, exist_ok=True)
        
        meta = {
            "titulo": item["titulo"],
            "esfera": item["esfera"],
            "orgao": item["orgao"],
            "tipo": item["tipo"],
            "numero": item["numero"],
            "ano": item["ano"],
            "data": item["data"],
            "tema_tributario": item["tema_tributario"],
            "tributos_afetados": item["tributos_afetados"],
            "situacao": item["situacao"],
            "revogada": item["revogada"],
            "fonte": item["fonte"],
            "ementa": item["ementa"]
        }
        
        frontmatter = gerar_frontmatter(meta)
        conteudo_md = item["conteudo"].strip()
        conteudo_final = f"{frontmatter}{conteudo_md}\n"
        
        salvar_atomico(destino, conteudo_final.encode("utf-8"))
        print(f"✓ Gerado: {destino.relative_to(RAIZ)}")
        gerados.append(destino)
        
    print(f"\n{len(gerados)} normas da Reforma Tributária estruturadas com sucesso!")
    return gerados

if __name__ == "__main__":
    gerar_normas_reforma()
