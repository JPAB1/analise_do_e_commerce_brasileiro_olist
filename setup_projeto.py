import os

# Define a estrutura de pastas do projeto
pastas = [
    "data/raw",         # Dados originais (baixados do Kaggle)
    "data/processed",   # Dados limpos e preparados
    "notebooks",        # Jupyter Notebooks para Análise Exploratória (EDA)
    "src",              # Scripts Python reutilizáveis (limpeza, utilitários)
    "docs",             # Relatórios, PDFs ou apresentações de entrega
]

# Cria as pastas
for pasta in pastas:
    os.makedirs(pasta, exist_ok=True)
    print(f"Pasta criada com sucesso: {pasta}")

# Cria arquivos vazios de boas práticas
arquivos = [
    "README.md",        # Documentação principal do projeto
    ".gitignore",       # Arquivos que o Git deve ignorar (venv, dados temporários)
    "requirements.txt"  # Dependências do projeto
]

for arquivo in arquivos:
    with open(arquivo, "w", encoding="utf-8") as f:
        if arquivo == ".gitignore":
            f.write("venv/\n__pycache__/\n.ipynb_checkpoints/\ndata/raw/*\ndata/processed/*\n*.zip\n")
        elif arquivo == "README.md":
            f.write("# Projeto: Análise do E-Commerce Brasileiro (Olist)\n\nRepositório para a atividade de análise de dados.")
    print(f"Arquivo básico criado: {arquivo}")
