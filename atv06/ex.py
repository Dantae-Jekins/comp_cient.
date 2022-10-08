import pandas as pd;
from numpy import pi;
# 1. importar os dados de CSV do dataset de seeds:
# https://raw.githubusercontent.com/celsocrivelaro/simple-datasets/main/seeds.csv
# 2. colocar as linhas de cabeçalho: 
  # 1. Área A,
  # 2. Perímetro P,
  # 3. Extensão do núcleo,
  # 4. Largura,
  # 5. Coeficiente de Assimetria
  # 6. Extensão do sulgo do núcleo.
# 3. remover colunas extras no final
# 4. remover as linhas com valores nulos
# 5. Adicionar um campo Compactação cujo o cálculo é C = 4*pi*A/P^2
# 6. Exportar para CSV o valor final

nomes = [
        'Área',
        'Perímetro',
        'Extensão',
        'Largura',
        'Coeficiente',
        'Extensão Sulgo',
        ]

if __name__ == "__main__":

    seeds = pd.read_csv(
            'https://raw.githubusercontent.com/celsocrivelaro/simple-datasets/main/seeds.csv',
            header=None,
            names = nomes,
            index_col=False,
            usecols = nomes # Importa apenas 6 primeiras colunas, as quais serão nomeadas.
            );

    seeds['Compactação'] = (4*pi*seeds['Área']) / (seeds['Perímetro']**2)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df = pd.DataFrame(seeds)

    df = df.dropna() # dropar linhas contendo NaN

    df.to_csv('newSeeds.csv')
    print(df)