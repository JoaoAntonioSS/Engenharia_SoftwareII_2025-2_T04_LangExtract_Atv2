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
    print("   Responsável: Miguel (Dupla 1 - Releases Strategy)")
    print("=" * 70 + "\n")

    device = 0 if torch.cuda.is_available() else -1
    execution_mode = "GPU (CUDA)" if device == 0 else "CPU (Standard)"

    print(f"   > Modo de Execução do Script: {execution_mode}")
    print("-" * 70 + "\n")

    release_history = """
    History:
    - v1.1.1 (Latest): Bug fixes.
    - v1.1.0 (Nov 14): Feature release. Gap: ~2.5 months.
    - v1.0.9 (Aug 31): Improvements. Gap: ~2 weeks.
    - v1.0.8 (Aug 15): Features.
    Observations: Semantic Versioning used.
    """

    print(f"[DADOS] Histórico carregado para análise:\n{release_history}")
    print("-" * 70)

    results = []

    # --- MODELO 1: Flan-T5 ---
    print(f"[1/3] Inicializando Google Flan-T5-Large...")
    try:
        print("      > Tipo: Instruction Tuned (Text-to-Text)")
        pipe = pipeline("text2text-generation", model="google/flan-t5-large", device=device)

        print("      > Enviando prompt de instrução...")
        prompt = f"Analyze: {release_history}. Is it Rapid Release, Release Train or LTS?"
        out = pipe(prompt, max_new_tokens=20)[0]['generated_text']

        print(f"      > [SUCESSO] Resposta gerada: {out}")
        results.append(["Flan-T5", out, "Instruction-based"])
    except Exception as e:
        print(f"      > [ERRO] Falha na execução: {e}")
        results.append(["Flan-T5", "Erro", str(e)])

    print("-" * 40)

    # --- MODELO 2: BART (Com Contexto Melhorado) ---
    print(f"[2/3] Inicializando Facebook BART-Large-MNLI...")
    try:
        print("      > Tipo: Zero-Shot Classification")
        pipe = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=device)

        print("      > Classificando com template de contexto (Hypothesis Template)...")
        out = pipe(
            release_history,
            ["Rapid Release", "Release Train", "LTS"],
            hypothesis_template="The software release strategy is {}."
        )

        top_label = out['labels'][0]
        score = out['scores'][0]
        print(f"      > [SUCESSO] Classificação: {top_label} (Confiança: {score:.2f})")
        results.append(["BART-MNLI", top_label, f"Score: {score:.2f}"])
    except Exception as e:
        print(f"      > [ERRO] Falha na execução: {e}")
        results.append(["BART-MNLI", "Erro", str(e)])

    print("-" * 40)

    # --- MODELO 3: DistilBERT ---
    print(f"[3/3] Inicializando DistilBERT-MNLI (Modelo Leve)...")
    try:
        print("      > Tipo: Knowledge Distillation (Efficiency Baseline)")
        classifier_light = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli",
                                    device=device)

        print("      > Executando inferência rápida...")
        candidate_labels = ["Rapid Release", "Release Train", "LTS (Long Term Support)"]
        res_distil = classifier_light(release_history, candidate_labels)

        best_label_distil = res_distil['labels'][0]
        score_distil = res_distil['scores'][0]
        print(f"      > [SUCESSO] Classificação: {best_label_distil} (Confiança: {score_distil:.2f})")
        results.append(["DistilBERT", best_label_distil, f"Confiança: {score_distil:.2f}"])
    except Exception as e:
        print(f"      > [ERRO] Falha na execução: {e}")
        results.append(["DistilBERT", "Erro", str(e)])

    print("=" * 70)

    df = pd.DataFrame(results, columns=["Modelo", "Estratégia", "Justificativa"])

    print("\n[RELATÓRIO FINAL DA ANÁLISE]")
    print(df.to_string(index=False))
    print("\n" + "-" * 70)

    caminho_arquivo = f"{OUTPUT_DIR}/resultado_ia_releases.csv"
    df.to_csv(caminho_arquivo, index=False)
    print(f"[IO] Arquivo CSV exportado com sucesso para: {caminho_arquivo}")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    analisar_estrategia()