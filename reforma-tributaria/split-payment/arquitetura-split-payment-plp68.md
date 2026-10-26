---
titulo: "Arquitetura Operacional do Split Payment no PLP 68/2024"
esfera: "Federal"
orgao: "Congresso Nacional / Ministério da Fazenda"
tipo: "Norma Técnica e Projeto de Lei"
numero: "68"
data: "2024-04-24"
ano: "2024"
tema_tributario: "Reforma Tributária e Transição"
tributos_afetados: ["IBS", "CBS", "Split Payment Inteligente"]
situacao: "Em tramitação"
revogada: false
fonte: "https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2429846"
ementa: "Detalhamento da sistemática de recolhimento na liquidação financeira (Split Payment) prevista nos arts. 49 a 53 do PLP nº 68/2024."
---

# Arquitetura Operacional do Split Payment no PLP 68/2024

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
