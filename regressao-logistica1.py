# Entendendo o algoritimo de Regressão Logística
# A representação da regressão logística se dá através da sigmoide:

# Sigmóide Regressão Logística Python
# Importando módulos
# Como sempre, vamos começar importando os módulos necessários:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
%matplotlib inline

# Importando Dataset
# Neste exemplo vamos trabalhar com um dataset que traz a incidência de diabetes é uma tribo indígena. 
# Você pode baixá-lo clicando aqui.

df = pd.read_csv("diabetes2.csv")
df.head()

# Análise Exploratória e Tratamento de Dados
# Vamos dar uma espiadinha nas características do nosso conjunto de dados:

df.info()

df.describe()

df['Disease'].unique()

dfCat = pd.get_dummies(df["Disease"].values)
df['DiseaseCat'] = dfCat["Diabético"].values

del df["Disease"]

df.head()

# Plotagem de Gráficos
# Vamos plotar alguns gráficos também para fazer uma análise visual:

sns.pairplot(df)

plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True)

sns.barplot(x=df["DiseaseCat"].value_counts().index, y=df["DiseaseCat"].value_counts().values)

df["DiseaseCat"].value_counts()


