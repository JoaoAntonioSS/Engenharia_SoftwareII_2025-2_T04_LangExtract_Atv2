# =========================================================
# ATIVIDADE 2 - FRENTE 2
# Análise do Fluxo de Trabalho / Branching Model
# Projeto: LangExtract
# Responsável: João Antônio Sousa da Silva
# =========================================================

import os
import torch
import pandas as pd
from transformers import pipeline
import warnings

warnings.filterwarnings("ignore")

# =========================================================
# CONFIGURAÇÃO DE DIRETÓRIOS (Compatível com Google Colab)
# =========================================================
CURRENT_DIR = os.getcwd()
OUTPUT_DIR = os.path.join(CURRENT_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR, "resultado_fluxo_trabalho_frente2.txt"
)

# =========================================================
# TEXTO DE ENTRADA (CONTRIBUTING.md)
# =========================================================
CONTRIBUTING_TEXT = """
This project uses GitHub pull requests for all submissions.
All changes must be reviewed before merging.
Contributors should create branches from the main branch.
Continuous integration checks are required before merge.
Releases are generated from the main branch.
"""

LABELS = [
    "GitHub Flow",
    "GitFlow",
    "Trunk-Based Development",
    "Centralized Workflow"
]

# =========================================================
# EXECUÇÃO
# =========================================================
def main():
    print("=" * 70)
    print("   ATIVIDADE 2 - ANÁLISE DO FLUXO DE TRABALHO (IA)")
    print("   Frente 2: Branching Model / Workflow")
    print("   Responsável: João Antônio Sousa da Silva")
    print("=" * 70)

    device = 0 if torch.cuda.is_available() else -1
    execution_mode = "GPU (CUDA)" if device == 0 else "CPU (Standard)"
    print(f"\n[SISTEMA] Modo de Execução Detectado: {execution_mode}")
    print("-" * 70)

    results = []

    # =====================================================
    # MODELO 1 - RoBERTa MNLI
    # =====================================================
    print("[1/3] Inicializando RoBERTa MNLI...")
    try:
        roberta_pipe = pipeline(
            "zero-shot-classification",
            model="roberta-large-mnli",
            device=device
        )
        out = roberta_pipe(CONTRIBUTING_TEXT, LABELS)
        results.append([
            "RoBERTa MNLI",
            out["labels"][0],
            f"Confiança: {out['scores'][0]:.2f}"
        ])
        print(f"      > Classificação: {out['labels'][0]}")
    except Exception as e:
        results.append(["RoBERTa MNLI", "Erro", str(e)])

    print("-" * 40)

    # =====================================================
    # MODELO 2 - DeBERTa v3 MNLI
    # =====================================================
    print("[2/3] Inicializando DeBERTa v3 MNLI...")
    try:
        deberta_pipe = pipeline(
            "zero-shot-classification",
            model="microsoft/deberta-v3-large-mnli",
            device=device
        )
        out = deberta_pipe(CONTRIBUTING_TEXT, LABELS)
        results.append([
            "DeBERTa v3 MNLI",
            out["labels"][0],
            f"Confiança: {out['scores'][0]:.2f}"
        ])
        print(f"      > Classificação: {out['labels'][0]}")
    except Exception as e:
        results.append(["DeBERTa v3 MNLI", "Erro", str(e)])

    print("-" * 40)

    # =====================================================
    # MODELO 3 - T5 Base (Instruction, NÃO Flan)
    # =====================================================
    print("[3/3] Inicializando T5 v1.1 Base...")
    try:
        t5_pipe = pipeline(
            "text2text-generation",
            model="google/t5-v1_1-base",
            device=device
        )
        prompt = (
            "Analyze the workflow described below and identify "
            "the branching model used: GitHub Flow, GitFlow, "
            "Trunk-Based Development or Centralized Workflow.\n\n"
            f"{CONTRIBUTING_TEXT}"
        )
        out = t5_pipe(prompt, max_new_tokens=30)[0]["generated_text"]
        results.append([
            "T5 v1.1 Base",
            out,
            "Instruction-based reasoning"
        ])
        print(f"      > Resposta: {out}")
    except Exception as e:
        results.append(["T5 v1.1 Base", "Erro", str(e)])

    print("=" * 70)

    # =====================================================
    # RELATÓRIO FINAL
    # =====================================================
    df = pd.DataFrame(
        results,
        columns=["Modelo", "Workflow Identificado", "Justificativa"]
    )

    print("\n[RELATÓRIO FINAL]")
    print(df.to_string(index=False))
    print("-" * 70)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(df.to_string(index=False))

    print(f"[IO] Resultado salvo em: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()