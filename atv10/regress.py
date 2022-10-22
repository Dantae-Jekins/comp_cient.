from math import floor
from random import seed
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score

name = ['carat','price','depth']
seeds = pd.read_csv(
        'https://raw.githubusercontent.com/tidyverse/ggplot2/main/data-raw/diamonds.csv',
        header=0,
        usecols=name,
        index_col=False
    )

seedsRand = seeds.sample(
        frac=1
    )

# separando 20% para teste e 80% para treinamento
training = seeds[:floor(len(seedsRand)*0.80)]
test = seeds[floor(len(seedsRand)*0.80):]


reg = linear_model.LinearRegression()

# Monta o modelo de regressão linear com base variáveis passaada
reg.fit(training[["carat","depth"]],training['price'])

# Estimativa dos valores e preço com base na reta.
predicted = reg.predict(training[["carat","depth"]])
print(
    reg.coef_,
    reg.score(training[["carat","depth"]],training['price']),
    r2_score(predicted, test["price"])
)