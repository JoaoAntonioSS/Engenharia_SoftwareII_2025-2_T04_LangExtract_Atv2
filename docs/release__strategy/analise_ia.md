# Análise de Estratégia de Releases (IA)
**Responsável:** Miguel Lucas (Dupla 1 - Strategy Releases)
**Data:** 19/12/2025

## 1. Metodologia e Ambiente
Para identificar a estratégia de releases do **LangExtract**, utilizamos uma abordagem comparativa com três modelos de arquiteturas distintas para evitar viés algorítmico.

### 1.1 Configuração de Hardware 
Os testes foram executados localmente para validar a viabilidade de execução em hardware gamer/consumer:
* **GPU:** NVIDIA GeForce RTX 5060 (Aceleração CUDA Ativa)
* **CPU:** Intel Core i5-10400F
* **RAM:** 32 GB
* **Ambiente:** PyCharm 2025.2 / Python 3.12

### 1.2 Justificativa dos Modelos Selecionados 
1.  **facebook/bart-large-mnli (Zero-Shot):** Selecionado como o "especialista". É um modelo robusto para classificação sem treinamento prévio, ideal para categorizar estratégias de engenharia.
2.  **google/flan-t5-large (Instruction):** Selecionado pela capacidade de raciocínio. Diferente dos classificadores, ele gera texto baseado em instruções lógicas, permitindo ver se o modelo "entende" o histórico.
3.  **distilbert-base-uncased (Distilled):** Selecionado para análise de eficiência. É uma versão leve (compactada) do BERT, usada aqui para verificar se modelos menores conseguem manter a precisão dos gigantes.

## 2. Resultados Obtidos
A tabela abaixo apresenta a classificação inferida baseada no histórico v1.0.8 a v1.1.1, utilizando a técnica de *Hypothesis Template* para melhorar o contexto:

| Modelo | Estratégia Identificada | Confiança/Obs |
| :--- | :--- | :--- |
| **Flan-T5** | LTS (Long Term Support) | Instruction-based |
| **BART-MNLI** | **Rapid Release** | Score: 0.51 |
| **DistilBERT** | Release Train | Confiança: 0.56  |

## 3. Discussão Crítica: Comparação de Eficácia
Observou-se uma divergência completa entre os três modelos, o que enriqueceu a análise:

* **DistilBERT (O Modelo Leve):** Classificou erroneamente como **Release Train** com confiança moderada (0.56). O modelo alucinou um calendário fixo onde existem datas irregulares, provando que modelos destilados perdem a capacidade de interpretar nuances temporais.
* **Flan-T5 (O Modelo Gerativo):** Insistiu na classificação **LTS**, confundindo o intervalo de 2.5 meses entre versões com um suporte de longo prazo.
* **BART-MNLI (O Vencedor):** Foi o **modelo mais efetivo**. Com a adição de contexto semântico (*hypothesis template*), sua confiança na estratégia correta (**Rapid Release**) subiu para **0.51**. Ele identificou corretamente que o projeto libera *features* assim que prontas (Feature-based), alinhando-se perfeitamente com a análise manual da equipe.
## 3. Discussão Crítica: Comparação de Eficácia 
Observou-se uma divergência completa entre os três modelos, o que enriqueceu a análise:

* **DistilBERT (O Modelo Leve):** Classificou como **Release Train**. Esta inferência provou-se incorreta (alucinação), pois o projeto não possui datas fixas de calendário. Isso demonstra que modelos "destilados" perdem nuances importantes de contexto.
* **Flan-T5 (O Modelo Gerativo):** Classificou como **LTS**. O modelo interpretou equivocadamente o gap de 2.5 meses como um suporte de longo prazo, falhando em notar a ausência de patches retroativos.
* **BART-MNLI (O Vencedor):** Foi o **modelo mais efetivo**. Ele alinhou-se com a análise manual (Ground Truth) da equipe, identificando corretamente a estratégia de **Rapid Release**. Sua arquitetura de inferência textual mostrou-se superior para captar que o projeto libera *features* assim que prontas, seguindo *Semantic Versioning*.

## 4. Conclusão Final
A triangulação entre IA e Análise Manual confirmou que o **LangExtract** utiliza uma estratégia de **Feature-based Rapid Release**. O experimento evidenciou que modelos maiores de classificação Zero-Shot (BART) são mais confiáveis para tarefas de Engenharia de Software do que modelos destilados ou puramente gerativos.