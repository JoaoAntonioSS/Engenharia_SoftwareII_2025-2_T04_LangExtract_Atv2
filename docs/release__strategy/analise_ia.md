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

## 2. Resultados Obtidos
A tabela abaixo apresenta a classificação inferida baseada no histórico v1.0.8 a v1.1.1, utilizando a técnica de *Hypothesis Template* para contexto:

| Modelo | Estratégia Identificada | Confiança/Obs |
| :--- | :--- | :--- |
| **Flan-T5** | LTS (Long Term Support) | Instruction-based |
| **BART-MNLI** | **Rapid Release** | Score: 0.51 (Acerto) |
| **DistilBERT** | Release Train | Confiança: 0.56 (Alucinação) |

## 3. Discussão Crítica: Comparação de Eficácia
Observou-se uma divergência completa entre os três modelos, o que enriqueceu a análise:

* **DistilBERT (O Modelo Leve):** Classificou erroneamente como **Release Train** com a maior confiança do teste (0.56). O modelo alucinou um calendário fixo em um histórico irregular, provando que modelos destilados perdem a capacidade de interpretar nuances temporais complexas.
* **Flan-T5 (O Modelo Gerativo):** Insistiu na classificação **LTS**, confundindo o intervalo de 2.5 meses entre versões com um suporte de longo prazo.
* **BART-MNLI (O Vencedor):** Foi o **modelo mais efetivo**. Com a adição de contexto semântico (*hypothesis template*), ele identificou corretamente a estratégia de **Rapid Release** (Score: 0.51). Ele compreendeu que o projeto libera *features* assim que prontas (Feature-based), alinhando-se perfeitamente com a análise manual da equipe.

## 4. Conclusão Final
A triangulação entre IA e Análise Manual confirmou que o **LangExtract** utiliza uma estratégia de **Feature-based Rapid Release**. O experimento evidenciou que o modelo BART (Zero-Shot) é mais confiável para tarefas de governança de software do que modelos destilados ou puramente gerativos.