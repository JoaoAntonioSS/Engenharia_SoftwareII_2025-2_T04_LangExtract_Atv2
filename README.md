# 🧠 Engenharia de Software II – 2025.2 – T04  
### Projeto: **LangExtract – Gerência de Configuração**

Este é o repositório oficial da **Atividade 2** da disciplina **Engenharia de Software II (Turma T04)**.  
O objetivo é aplicar técnicas de **Processamento de Linguagem Natural (PLN)** para identificar **Padrões de Gerência de Configuração** em um projeto de código aberto.

O trabalho é dividido em três **frentes de análise**:

1. 🗒️ **Frente 1 – Estratégia de Releases**  
2. 🧩 **Frente 2 – Modelo de Branching e Fluxo de Trabalho**  
3. 🗂️ **Frente 3 – Governança do Projeto**  

---

## 🎯 Projeto Alvo da Análise

- **Repositório:** [`google/langextract`](https://github.com/google/langextract)  
- **Descrição:** Biblioteca Python desenvolvida pelo Google que utiliza **Modelos de Linguagem (LLMs)** para extrair informações estruturadas (como dados médicos) a partir de textos não estruturados.

## ⚙️ Como Reproduzir a Análise

Este repositório contém todo o código necessário para replicar as análises realizadas nas três frentes.

### 1. Configuração do Ambiente

> Recomendamos o uso de um ambiente virtual (`venv`) para isolar as dependências.

```bash
# 1. Clone o repositório
git clone https://github.com/[SEU_USUARIO]/Engenharia_SoftwareII_2025-2_T04_langextract.git
cd Engenharia_SoftwareII_2025-2_T04_langextract

# 2. Crie e ative o ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: .\venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt
```

### 2. Executando as Análises

Os scripts de cada frente estão localizados na pasta `/scripts`.

```bash
# Frente 1 – Estratégia de Releases
scripts/estrategia1_releases.py

# Frente 2 – Modelo de Branching e Fluxo de Trabalho
scripts/estrategia2_branching_model.py

# Frente 3 – Governança do Projeto
scripts/estrategia3_governance_analysis.py

```
---

## 🧩 Estrutura de Pastas

```bash
.
├── docs/              # Análises com modelos de IA e manuais
│   ├── estrategia1_releases
│      ├── analise_ia.md
│      ├── analise_manual.ipynb
│   ├── estrategia2_branching_model
│      ├── analise_ia.md
│      ├── analise_manual.ipynb
│   ├── estrategia3_governance_analysis
│      ├── analise_ia.md
│      ├── analise_manual.ipynb
├── output/              # Resultados das análises com modelos de IA
│   ├── resultado_ia_branching_model.csv
│   ├── resultado_ia_governance_analysis.csv
│   ├── resultado_ia_releases.csv
├── scripts/              # Scripts de execução de cada frente
│   ├── estrategia1_releases.py
│   ├── estrategia2_branching_model.py
│   └── estrategia3_governance_analysis.py
└── .gitignore
└── README.md             # Documento principal com instruções de execução do projeto e análise geral dos resultados das 3 frentes
└── requirements.txt      # Arquivo com as dependências necessárias à execução dos scripts
```
## 🗒️ Análise da Frente 1: Estratégia de Releases

**Responsáveis:** Miguel Lucas Santana Freire (análise com modelo de IA) e Débora Diana Gonçalves dos Santos (análise manual)

### 🎯 Objetivo
Analisar a estratégia de releases do projeto com uma abordagem comparativa, para identificar padrões de gerência de configuração. Na análise manual, foi feita a inspeção manual do histórico de versões, tags e estrutura de branches.

---

### 🧠 Modelos Utilizados
**Modelo:** `zero-shot-classification`  
**Base:** `facebook/bart-large-mnli`

**Modelo:** `text2text-generation`  
**Base:** `google/flan-t5-large`

**Modelo:** `text-classification`  
**Base:** `distilbert-base-uncased`

### 💡 Por que estes modelos?
**facebook/bart-large-mnli (Zero-Shot):** Selecionado como o "especialista". É um modelo robusto para classificação sem treinamento prévio.

**google/flan-t5-large (Instruction):** Selecionado pela capacidade de raciocínio lógico baseada em instruções (Text-to-Text).

**distilbert-base-uncased (Distilled):** Selecionado para análise de eficiência. É uma versão leve do BERT, usada para verificar a precisão de modelos compactos.  

### ⚙️ Metodologia
Definição das Classes (Labels) - Para a classificação Zero-Shot, definimos três categorias distintas que representam os principais paradigmas de Engenharia de Release:  
**1. Feature-based Release:** Define projetos ágeis onde a publicação de versões é gatilhada pela conclusão de funcionalidades, sem calendário fixo.  
**2. Release Train:** Define projetos com janelas de lançamento rígidas baseadas em calendário (ex: toda terça-feira), independente do escopo.  
**3. LTS (Long Term Support):** Define projetos que mantêm suporte e patches de segurança para versões legadas por longos períodos.  
Justificativa - A escolha destas três classes garante que o modelo avalie os pilares de Velocidade, Previsibilidade e Estabilidade, evitando sobreposição semântica que poderia reduzir a acurácia da inferência.  
O script executado foi:

```bash
scripts/estrategia1_releases.py
```

# Análise Manual vs. Análise de IA do Projeto LangExtract

**Responsáveis:** Allex Lemos de Souza Pinheiro e Thiago Menezes Vasconcelos

## 1. Estratégia de Releases

Na análise manual, ficou claro que o projeto **LangExtract** segue uma **estratégia de releases baseada em funcionalidades (Feature-based Release)**, com o uso do **Semantic Versioning (SemVer)**. As versões são incrementadas conforme novas funcionalidades são implementadas e corrigidas, sem depender de um ciclo fixo de lançamento (não há **Release Train**) ou versões de longo prazo (sem **LTS**). As releases são feitas de maneira contínua, sem datas específicas para o lançamento.

Na análise de IA, todos os modelos utilizados nas três frentes (documentação, código e estrutura) confirmaram que a **estratégia é baseada em funcionalidades**. O modelo **BART-MNLI** apresentou um alto grau de confiança ao classificar a estratégia de **Feature-based Release**. No entanto, houve uma falha na IA ao não identificar a ausência de **Release Train**, um ponto claramente observado na análise manual. A IA também acertou ao identificar que o projeto não possui versões **LTS**.

**Conclusão**: A análise manual e a IA concordaram em grande parte, especialmente em relação à estratégia **Feature-based Release**. A maior diferença foi na identificação da ausência de **Release Train**, onde a IA não foi capaz de captar essa particularidade.

---

## 2. Branching Model e Fluxo de Trabalho

De acordo com a análise manual, o projeto segue o **GitHub Flow**, um modelo simplificado de branching. Nesse modelo, a **branch principal (main)** é a única linha de base permanente. Todas as alterações são feitas por meio de **pull requests (PRs)** para a **main**, sem o uso de uma branch **develop** ou outras branches de longa duração. Isso caracteriza o fluxo de trabalho do projeto como ágil e direto.

A análise de IA também confirmou que o modelo de branching adotado é o **GitHub Flow**. O modelo **RoBERTa MNLI** conseguiu identificar o uso de branches curtos e a integração contínua via **pull requests**. No entanto, houve um problema com o modelo **DeBERTa v3**, que não pôde ser carregado, o que limitou a análise. Já o modelo **T5** foi menos eficiente e forneceu respostas inconclusivas, não conseguindo classificar o fluxo de trabalho de maneira objetiva.

**Conclusão**: A análise manual e a IA concordaram quanto ao uso do **GitHub Flow** no projeto. A principal diferença foi o desempenho inconsistente da IA, com o modelo **DeBERTa v3** não funcionando corretamente e o **T5** apresentando respostas genéricas. A análise manual, por outro lado, foi mais clara e detalhada ao descrever o fluxo de trabalho.

---

## 3. Governança do Projeto

A análise manual indicou que o projeto **LangExtract** tem uma governança bem estruturada, com práticas consistentes de controle de versões e integração contínua. As releases são baseadas em versões consolidadas e estáveis da branch **main**, com uma clara organização do repositório e mensagens de commit bem definidas. A documentação também é bem organizada, o que ajuda a manter a governança do projeto de forma transparente e eficiente.

Na análise de IA, os modelos identificaram que a governança é **estruturada**, com uma média de aderência aos padrões de mensagens de commit e versionamento entre 86% e 91%, dependendo do modelo. O modelo **all-MiniLM-L** foi eficaz ao identificar commits bem estruturados, enquanto o **all-mpnet-base** teve um desempenho ainda melhor ao identificar nuances em refatorações complexas. O modelo **paraphrase-L3** também validou a clareza das mensagens de commit.

**Conclusão**: A análise manual e a IA concordaram que o projeto possui uma governança bem estruturada, com boas práticas de versionamento e controle de commits. No entanto, a análise manual foi mais detalhada, explicando a organização do repositório e a ausência de commits fora do padrão. A IA, por sua vez, foi eficaz em identificar padrões de commit e versionamento, com uma taxa de aderência bastante alta.

---

## Considerações Finais

**Convergências**: Tanto a análise manual quanto as de IA concordaram nos pontos principais, como a **estratégia de releases baseada em funcionalidades**, o **GitHub Flow** no branching model e a **governança estruturada**. Em geral, os resultados foram bastante consistentes, com a IA oferecendo uma confirmação rápida das estratégias e práticas observadas manualmente.

**Desafios e Limitações**: Apesar das muitas convergências, a IA apresentou algumas limitações. O modelo **DeBERTa v3**, por exemplo, não foi carregado corretamente, o que impediu uma análise completa do fluxo de trabalho. Além disso, o modelo **T5** não foi eficaz na classificação do fluxo de trabalho, resultando em respostas inconclusivas. Outro ponto importante foi a falha da IA em identificar a **ausência de Release Train**, algo que foi bem claro na análise manual.

**Valor da Análise Manual vs. IA**: A análise manual ofereceu uma visão mais detalhada e rica, explorando nuances como a **ausência de branches de longa duração** e o comportamento específico de **releases contínuas**. A IA, por outro lado, foi eficiente em identificar padrões gerais e fornecer uma resposta mais rápida, mas teve dificuldades com a identificação de detalhes mais complexos ou técnicos, como a falta de **Release Train**.

Em resumo, ambos os métodos de análise se complementam bem. A análise manual foi mais robusta em termos de detalhes e explicações, enquanto a IA mostrou ser uma ferramenta útil para confirmar padrões gerais de forma rápida e eficiente.
