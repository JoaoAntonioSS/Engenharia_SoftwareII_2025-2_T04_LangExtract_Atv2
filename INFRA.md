# 📄 INFRA.md — Infraestrutura Utilizada no Projeto

Este documento descreve detalhadamente toda a infraestrutura utilizada pela equipe para executar as análises das Frentes do projeto. 

---

## 💻 Ambiente da Frente 1 – Estratégia de Releases

Os testes foram executados localmente. O script detectou o hardware disponível, mas optou-se pela execução em modo CPU para validar a reprodutibilidade em ambientes sem drivers CUDA específicos:

As especificações do hardware utilizado são:

### 🔹 Processamento
- **CPU:** Intel(R) Core(TM) i5-10400F CPU @ 2.90GHz
- **GPU (Disponível):** NVIDIA GeForce RTX 5060 (Execução realizada em modo de compatibilidade CPU)

### 🔹 Memória e Armazenamento
- **Memória RAM:** 32 GB

### 🔹 Sistema Operacional
- **Windows 11**

### 🔹 Versão do Python
- **Python 3.12**

### 🔹 IDE
- **PyCharm 2025.2**


## 💻 Ambiente da Frente 2 – Modelo de Branching e Fluxo de Trabalho

Os testes foram executados no ambiente Google Colab, priorizando reprodutibilidade e facilidade de execução em ambientes acadêmicos:

As especificações do hardware utilizado são:

### 🔹 Ambiente
- `Google Colab`

### 🔹 Processamento
- **CPU:** CPU virtual padrão do Google Colab
- **GPU:** Não utilizada (execução em CPU)

### 🔹 Memória e Armazenamento
- **RAM Total:** Alocação padrão do Google Colab

### 🔹 Versão do Python
- **Python 3**

### 🔹 Framework
- `Hugging Face Transformers`


## 🖥️ Ambiente da Frente 3 – Governança do Projeto
