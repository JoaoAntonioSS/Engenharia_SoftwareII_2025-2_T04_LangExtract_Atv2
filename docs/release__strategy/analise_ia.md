# Análise de Estratégia de Releases (IA)
**Responsável:** Miguel (Dupla 1 - Strategy Releases)
**Data:** 19/12/2025

## 1. Metodologia e Ambiente
Para identificar a estratégia de releases do **LangExtract**, utilizamos uma abordagem comparativa com três modelos de LLM hospedados no Hugging Face.

### 1.1 Configuração de Hardware
Os testes foram executados localmente. O script detectou o hardware disponível, mas optou-se pela execução em modo CPU para validar a reprodutibilidade em ambientes sem drivers CUDA específicos:
* **Processador:** Intel(R) Core(TM) i5-10400F CPU @ 2.90GHz
* **Memória RAM:** 32 GB
* **GPU (Disponível):** NVIDIA GeForce RTX 5060 (Execução realizada em modo de compatibilidade CPU)
* **IDE:** PyCharm 2025.2 / Python 3.12

### 1.2 Justificativa dos Modelos Selecionados
1.  **facebook/bart-large-mnli (Zero-Shot):** Selecionado como o "especialista". É um modelo robusto para classificação sem treinamento prévio.
2.  **google/flan-t5-large (Instruction):** Selecionado pela capacidade de raciocínio lógico baseada em instruções (*Text-to-Text*).
3.  **distilbert-base-uncased (Distilled):** Selecionado para análise de eficiência. É uma versão leve do BERT, usada para verificar a precisão de modelos compactos.

### 1.3 Definição das Classes (Labels)
Para a classificação Zero-Shot, definimos três categorias distintas que representam os principais paradigmas de Engenharia de Release:
1.  **Feature-based Release:** Define projetos ágeis onde a publicação de versões é gatilhada pela conclusão de funcionalidades, sem calendário fixo.
2.  **Release Train:** Define projetos com janelas de lançamento rígidas baseadas em calendário (ex: toda terça-feira), independente do escopo.
3.  **LTS (Long Term Support):** Define projetos que mantêm suporte e patches de segurança para versões legadas por longos períodos.

*Justificativa:* A escolha destas três classes garante que o modelo avalie os pilares de **Velocidade**, **Previsibilidade** e **Estabilidade**, evitando sobreposição semântica que poderia reduzir a acurácia da inferência.

## 2. Resultados Obtidos
A tabela abaixo apresenta a classificação final após o enriquecimento dos dados de entrada:

| Modelo | Estratégia Identificada | Confiança/Obs |
| :--- | :--- | :--- |
| **Flan-T5** | **Feature-based Release** | Instruction-based |
| **BART-MNLI** | **Feature-based Release** | **Score: 0.90 (Alta Precisão)** |
| **DistilBERT** | Feature-based Release | Confiança: 0.35 (Incerteza) |

## 3. Discussão Crítica: Convergência e Dados
O uso de um histórico detalhado gerou um consenso entre os modelos, alinhando-se 100% com a análise manual.

* **O Salto do BART (Data-Centric AI):** O modelo BART atingiu **90% de confiança**. Isso demonstra que, ao fornecer evidências de que versões são lançadas por funcionalidade (ex: v1.0.4 para Ollama, v1.0.3 para OpenAI), o modelo consegue descartar matematicamente as hipóteses de *Release Train* ou *LTS*.
* **A Fragilidade do DistilBERT:** Embora tenha acertado a categoria, o modelo leve manteve uma confiança baixa (0.35). Isso valida a hipótese de que modelos destilados ("light") são menos sensíveis a nuances de contexto complexo, servindo apenas para triagem inicial.

## 4. Conclusão Final
A estratégia do **LangExtract** é, inequivocamente, **Feature-based Release**.
A triangulação entre a IA (BART com 0.90 de score) e a análise manual da equipe confirma que o projeto prioriza a entrega contínua de valor (features) sem amarras de calendário (Release Train) ou legado (LTS).