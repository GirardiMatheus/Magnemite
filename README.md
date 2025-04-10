<div align="center">
  <h1>
    <img src="./assets/Magnemite.svg" width="100" height="100" alt="Magnemite Logo" style="vertical-align: middle; margin-right: 10px;">
    Magnemite
  </h1>

  <p>Este projeto realiza uma análise interativa do consumo de energia elétrica no Brasil, utilizando dados oficiais de concessionárias. Com gráficos interativos, filtros por estado, região e destaques dos maiores consumidores.</p>
</div>

## Funcionalidades

- **Gráficos interativos com Plotly**: Visualize dados por estado, região ou maiores consumidores.
- **Filtros dinâmicos**: Dropdowns para navegação mais intuitiva.
- **Tratamento de dados**: Limpeza, normalização e agregação para facilitar a visualização.
- **Notebook interativo**: Projeto conduzido via Jupyter Notebook para exploração contínua.
- **Script de download de dados**: Automatiza a coleta dos dados brutos em `scripts/data_download.py`.

## Pré-requisitos

- Python 3.9 ou superior
- Jupyter Notebook (pode usar VSCode com extensão Jupyter)
- Instalar os pacotes do `requirements.txt`

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/magnemite.git
   cd magnemite

2. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt

## Executando o Projeto

1. (Opcional) Faça o download automatizado dos dados brutos com o script:

    ```bash
   python scripts/data_download.py

2. Inicie o Jupyter Notebook:

    ```bash
    jupyter notebook

3. Abra o notebook initial_analysis.ipynb e execute as células.

    Os gráficos interativos estarão disponíveis diretamente no notebook.

## Abra o notebook initial_analysis.ipynb e execute as células.
- Todos os Estados: Evolução mensal do consumo por estado (UF).
- Por Região: Gráficos separados por Norte, Nordeste, Sudeste, Sul e Centro-Oeste.
- Maiores Consumidores: Top estados com maior consumo acumulado no período.

## Dataset

Os dados utilizados estão em formato .xlsx, contendo registros por mês, estado, tipo de consumidor e volume de consumo.

**Nota:** Certifique-se de que o arquivo esteja em data/Dados brutos.xlsx ou utilize o script de download automático.

## Estrutura do Projeto
  ```bash
    magnemite/
    ├── assets/                  # Logos, imagens e ícones
    ├── data/                    # Arquivos de entrada, como Excel
    ├── scripts/
    │   └── data_download.py     # Script para baixar os dados automaticamente
    ├── initial_analysis.ipynb   # Notebook principal de análise e visualização
    ├── requirements.txt         # Dependências do projeto
    └── README.md  