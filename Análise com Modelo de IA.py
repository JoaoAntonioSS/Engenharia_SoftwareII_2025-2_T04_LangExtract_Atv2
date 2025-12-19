# 1. Instalação e Imports
!pip install sentence-transformers requests matplotlib

import requests
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer, util

# 2. Configurações
REPO_OWNER = "google"
REPO_NAME = "langextract"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
QTD_COMMITS = 100 

# 3. Função para pegar commits
def get_commits(owner, repo, limit=100):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page={limit}"
    response = requests.get(url)
    commits_list = []
    if response.status_code == 200:
        data = response.json()
        for item in data:
            msg = item['commit']['message'].split('\n')[0]
            commits_list.append(msg)
    return commits_list

# 4. Execução
print(f"Baixando os últimos {QTD_COMMITS} commits...")
commits_reais = get_commits(REPO_OWNER, REPO_NAME, limit=QTD_COMMITS)
print(f"Total: {len(commits_reais)} commits.")

print(f"Carregando IA ({MODEL_NAME})...")
model = SentenceTransformer(MODEL_NAME)


padrao_bom = [
    "feat: add functionality", "fix: resolve bug", "docs: update readme", # Conventional
    "Add new feature support", "Update dependency versions", "Remove unused code", # Imperative Mood
    "Refactor internal logic", "Merge pull request"
]

padrao_ruim = [
    "fixed", "stuff", "wip", "changes", "temp", "bug", "oops", "worked on it", "aaa", "test"
]

embeddings_bom = model.encode(padrao_bom)
embeddings_ruim = model.encode(padrao_ruim)

print("\n--- REANALISANDO COM CRITÉRIOS AJUSTADOS (GOOGLE STYLE) ---")

good_count = 0
bad_count = 0
exemplos_bons = []
exemplos_ruins = []

# Lista de verbos fortes para ajudar a IA na decisão
verbos_fortes = ["Add", "Fix", "Update", "Remove", "Refactor", "Bump", "Create", "Merge", "feat", "fix", "docs", "chore"]

for commit in commits_reais:
    emb_commit = model.encode(commit)
    
    sim_bom = util.cos_sim(emb_commit, embeddings_bom).max().item()
    
    # Lógica Híbrida: Semântica (IA) + Sintaxe (Verbos)
    primeira_palavra = commit.split(' ')[0].replace(':', '')
    
    is_good = False
    
    # Se começar com verbo forte OU tiver alta similaridade com boas práticas
    if primeira_palavra in verbos_fortes or sim_bom > 0.30:
        is_good = True
    
    # Se for muito curto (< 5 letras) é ruim (ex: "fix")
    if len(commit) < 5:
        is_good = False

    if is_good:
        good_count += 1
        if len(exemplos_bons) < 3: exemplos_bons.append(commit)
    else:
        bad_count += 1
        if len(exemplos_ruins) < 3: exemplos_ruins.append(commit)

# 5. Resultados
total = good_count + bad_count
maturity = (good_count / total) * 100

print("\n" + "="*50)
print(f"RELATÓRIO DE GOVERNANÇA AJUSTADO")
print("="*50)
print(f"Commits Estruturados (Conventional + Imperative): {good_count}")
print(f"Commits Genéricos / Sem Padrão Claro: {bad_count}")
print(f"Nível de Maturidade Real: {maturity:.1f}%")

print("\nExemplos BONS (Reconhecidos):")
for ex in exemplos_bons: print(f"   - {ex}")

print("\nExemplos INSUFICIENTES:")
for ex in exemplos_ruins: print(f"   - {ex}")

# Gráfico
plt.figure(figsize=(7, 7))
labels = [f'Estruturado ({maturity:.1f}%)', f'Ad-hoc ({100-maturity:.1f}%)']
colors = ['#2E7D32', '#FF7043'] 
plt.pie([good_count, bad_count], labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, shadow=True)
plt.title(f'Análise de Governança (Padrão Google)\nProjeto: {REPO_NAME}')
plt.show()

if maturity > 70:
    print("\nCONCLUSÃO: Governança ALTA (Padrão Profissional Detectado).")
else:
    print("\nCONCLUSÃO: Governança Média.")
