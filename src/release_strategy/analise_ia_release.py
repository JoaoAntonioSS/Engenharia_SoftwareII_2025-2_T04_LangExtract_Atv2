import pandas as pd
from transformers import pipeline
import torch
import os
import warnings

warnings.filterwarnings("ignore")

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(CURRENT_DIR, "../../data/processed")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def analisar_estrategia():
    print("\n" + "=" * 70)
    print("   ATIVIDADE 2 - ANÁLISE DE ESTRATÉGIA DE RELEASES (IA)")
    print("   Responsável: Miguel (Dupla 1)")
    print("=" * 70 + "\n")

    device = 0 if torch.cuda.is_available() else -1
    execution_mode = "GPU (CUDA)" if device == 0 else "CPU (Standard)"
    print(f"[SISTEMA] Modo de Execução Detectado: {execution_mode}")
    print("-" * 70 + "\n")

    release_history = """
    History:
    - v1.1.1 (Latest): Bug fixes.
    - v1.1.0 (Nov 14): Feature release. Gap: ~2.5 months from prev.
    - v1.0.9 (Aug 31): Improvements. Gap: ~2 weeks from prev.
    - v1.0.8 (Aug 15): Features.
    - v1.0.6 (Aug 13): Major Refactor. Gap: Irregular.
    - v1.0.5 (Aug 7): Bug Fixes.
    - v1.0.4 (Aug 5): Integration (Ollama). Feature driven.

    Observations: 
    1. Semantic Versioning used. 
    2. Releases happen when features are ready (Feature-based), not by calendar.
    """

    print(f"[DADOS] Histórico carregado (Amostra):\n{release_history}")
    print("-" * 70)

    results = []


    labels = ["Feature-based Release", "Release Train", "LTS"]

    # --- MODELO 1: Flan-T5 ---
    print(f"[1/3] Inicializando Flan-T5 (Instruction)...")
    try:
        pipe = pipeline("text2text-generation", model="google/flan-t5-large", device=device)
        prompt = f"Analyze: {release_history}. Choose one strategy: Feature-based Release, Release Train or LTS."
        out = pipe(prompt, max_new_tokens=20)[0]['generated_text']
        results.append(["Flan-T5", out, "Instruction-based"])
        print(f"      > [SUCESSO] Resposta: {out}")
    except Exception as e:
        results.append(["Flan-T5", "Erro", str(e)])

    print("-" * 40)

    # --- MODELO 2: BART (Zero-Shot) ---
    print(f"[2/3] Inicializando BART-Large (Zero-Shot)...")
    try:
        pipe = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=device)
        out = pipe(release_history, labels)

        top_label = out['labels'][0]
        score = out['scores'][0]
        results.append(["BART-MNLI", top_label, f"Score: {score:.2f}"])
        print(f"      > [SUCESSO] Classificação: {top_label} ({score:.2f})")
    except Exception as e:
        results.append(["BART-MNLI", "Erro", str(e)])

    print("-" * 40)

    # --- MODELO 3: DistilBERT ---
    print(f"[3/3] Inicializando DistilBERT (Efficiency)...")
    try:
        classifier_light = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli",
                                    device=device)
        res_distil = classifier_light(release_history, labels)

        best_label = res_distil['labels'][0]
        score = res_distil['scores'][0]
        results.append(["DistilBERT", best_label, f"Confiança: {score:.2f}"])
        print(f"      > [SUCESSO] Classificação: {best_label} ({score:.2f})")
    except Exception as e:
        results.append(["DistilBERT", "Erro", str(e)])

    print("=" * 70)

    df = pd.DataFrame(results, columns=["Modelo", "Estratégia", "Justificativa"])
    print("\n[RELATÓRIO FINAL - ALINHADO COM DUPLA]")
    print(df.to_string(index=False))
    print("\n" + "-" * 70)

    caminho_arquivo = f"{OUTPUT_DIR}/resultado_ia_releases.csv"
    df.to_csv(caminho_arquivo, index=False)
    print(f"[IO] Arquivo CSV exportado.")


if __name__ == "__main__":
    analisar_estrategia()