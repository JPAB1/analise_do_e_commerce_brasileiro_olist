# Projeto: Análise do E-Commerce Brasileiro (Olist)


Este projeto realiza uma análise exploratória dos dados de vendas da Olist, utilizando **Python**, **Pandas**, **Matplotlib** e **Seaborn**.  
O objetivo é compreender padrões de compra, distribuição geográfica, tendências temporais e identificar outliers nos preços e fretes.

---

## 📂 Estrutura do Projeto
\\\
├── data
│   ├── raw/                # Bases originais da Olist
│   └── processed/          # Bases tratadas e consolidadas
├── docs/                   # Gráficos e relatórios gerados
├── notebooks/              # Scripts e análises exploratórias
├── src/                    # Funções de limpeza e preparação
└── README.md               # Documentação do projeto
\\\
# Instale as dependências:

# bash
pip install -r requirements.txt
Certifique-se de que os arquivos da Olist estejam na pasta data/raw/.

# 🚀 Uso

Executar a limpeza e preparação dos dados
# bash

python src/limpeza.py
Isso gera o arquivo consolidado em:

# Código

data/processed/vendas_consolidadas_brasil.csv
Rodar as análises exploratórias
Abra o notebook em notebooks/analise.ipynb e execute célula por célula.
Os gráficos serão salvos automaticamente na pasta docs/.

# 📈 Principais Análises

- Distribuição por Estado: Identificação dos estados com maior volume de pedidos.

- Tendência Temporal: Evolução mensal das compras.

- Comparativo de Preço e Frete: Média e mediana por estado.

- Outliers de Frete: Identificação de valores discrepantes.

- Tempo de Entrega: Cálculo de dias entre compra e entrega.

# 🛠️ Tecnologias Utilizadas
- Python

- Pandas

- Matplotlib

- Seaborn