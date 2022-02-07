Métodos e Agrupamentos com Pandas
Vamos começar a trabalhar então com métodos e agrupamentos:

Importar módulos e criar o DataFrame

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "modelo":["Uno","Monza","Camaro","Gol","Palio"],
    "marca":["Fiat","Chevrolet","Chevrolet","VW","Fiat"],
    "valor":[10000,20000,200000,30000,15000],
    "unidades":[10,30,100,25,15]
})
df
Métodos Descritivos

Oferecem informações dos dados e da estrutura do conjunto de dados:

df.describe()
df.info()
df.count()
Agrupamento de Dados

Podemos agrupar dados semelhantes utilizando Pandas, por exemplo: os veículos de determinada Marca, ou os remédios de determinado laboratório e assim por diante.

grupo = df.groupby("marca")
grupo['marca'].count()

grupo['modelo'].value_counts()

grupo['valor'].mean()

grupo['unidades'].sum()
Valores �?nicos

Para retornar valores únicos do nosso DataFrame podemos usar os seguintes métodos:

df['marca'].unique()
df['marca'].nunique()
df['marca'].value_counts()
