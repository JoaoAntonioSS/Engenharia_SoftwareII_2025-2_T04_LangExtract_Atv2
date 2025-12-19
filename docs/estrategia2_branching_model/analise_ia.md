# Análise de Fluxo de Trabalho e Branching Model (IA)
**Responsável:** João Antônio Sousa da Silva (Dupla 2 - Branching Model / Workflow)  
**Data:** 19/12/2025

## 1. Metodologia e Ambiente
Para identificar o modelo de **branching** e o **fluxo de trabalho** adotado no projeto **LangExtract**, utilizamos uma abordagem comparativa com modelos de LLM hospedados no Hugging Face, aplicados diretamente sobre o conteúdo do arquivo **CONTRIBUTING.md** do repositório.

### 1.1 Configuração de Hardware
Os testes foram executados no ambiente Google Colab, priorizando reprodutibilidade e facilidade de execução em ambientes acadêmicos:
* **Ambiente:** Google Colab
* **Processador:** CPU virtual padrão
* **Memória RAM:** Alocação padrão do Colab
* **GPU:** Não utilizada (execução em CPU)
* **Linguagem:** Python 3
* **Framework:** Hugging Face Transformers

### 1.2 Justificativa dos Modelos Selecionados
1. **roberta-large-mnli (Zero-Shot):** Selecionado pela alta robustez em tarefas de *Natural Language Inference*, sendo eficaz na identificação de padrões de workflow sem necessidade de treinamento adicional.
2. **microsoft/deberta-v3 (Zero-Shot):** Escolhido por representar uma arquitetura moderna e otimizada para compreensão contextual profunda. Sua tentativa de uso faz parte da análise experimental.
3. **t5-v1_1-base (Instruction):** Utilizado para análise baseada em instruções (*Text-to-Text*), permitindo respostas abertas sobre o fluxo de trabalho descrito.

### 1.3 Definição das Classes (Labels)
Para a classificação Zero-Shot, foram definidas as seguintes categorias de branching models:
1. **GitHub Flow:** Modelo simplificado com branches curtos e integração contínua.
2. **GitFlow:** Modelo estruturado com múltiplas branches permanentes.
3. **Trunk-Based Development:** Desenvolvimento concentrado na branch principal com integrações frequentes.
4. **Centralized Workflow:** Fluxo tradicional com contribuições diretas na branch principal.

*Justificativa:* Essas classes representam os principais paradigmas de controle de versões, evitando sobreposição semântica e facilitando a inferência correta dos modelos.

## 2. Resultados Obtidos
A tabela abaixo apresenta os resultados consolidados da análise automática sobre o **CONTRIBUTING.md**:

| Modelo | Workflow Identificado | Confiança/Obs |
| :--- | :--- | :--- |
| **RoBERTa MNLI** | **GitHub Flow** | Confiança: 0.32 |
| **DeBERTa v3 MNLI** | Erro de carregamento | Modelo indisponível no ambiente |
| **T5 v1.1 Base** | Resposta inconclusiva | Instruction-based reasoning |

## 3. Discussão Crítica: Convergência e Limitações
Os resultados indicam uma predominância do **GitHub Flow**, especialmente evidenciada pelo modelo RoBERTa.

* **Desempenho do RoBERTa:** Mesmo com confiança moderada, o modelo conseguiu associar corretamente práticas como branches curtos, pull requests e integração contínua ao GitHub Flow.
* **Limitação do DeBERTa:** A indisponibilidade do modelo destaca limitações práticas de compatibilidade e acesso em ambientes compartilhados.
* **Fragilidade do T5:** O modelo baseado em instruções apresentou respostas genéricas, demonstrando menor eficácia para tarefas de classificação objetiva de workflow.

## 4. Conclusão Final
Com base na análise automatizada, conclui-se que o projeto **LangExtract** adota um fluxo de trabalho alinhado ao **GitHub Flow**.

A convergência entre o resultado do modelo Zero-Shot e a análise manual reforça que o projeto prioriza simplicidade, integração contínua e colaboração via pull requests, características centrais desse modelo de branching.