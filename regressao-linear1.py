# Modelo de Regressão Linear no Python
# Para trabalhar com regressão linear vamos trabalhar com um Data Frame de Veículos, para baixá-lo basta clicar aqui.

# Importando Módulos e DataFrame
# Vamos começar importando os módulos necessários

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
%matplotlib inline

df = pd.read_csv("autocar.csv")
df.head()

# Análise exploratória
# Vamos entender melhor os nossos dados através dos comandos abaixo:

df.info()

df.describe()
sns.pairplot(df)

plt.figure(figsize=(12,8))
sns.heatmap(df.corr(),annot=True)

sns.jointplot(x='weight',y='mpg',data=df,kind='reg')

sns.barplot(y='displacement',x='cylinders',data=df)

sns.barplot(x=df['year'].value_counts().index,y=df['year'].value_counts().values,data=df)

sns.lineplot(y='mpg',x='horsepower',data=df)

# Dividindo os dados em X e Y
# Lembra da última aula onde dividamos os dados nas labels (x) e o valor que queremos predizer (y).
# Vamos retirar a coluna name desse dataframe também, pois ela não tem relevância para análise dos dados.

X = df.drop(['mpg','name'],axis=1)
X

y = df['mpg']
y

# Dividindo em dados de treino e dados de teste
# Primeiro dividimos em características (X) e valor a ser previsto (y), agora vamos dividir em dados
# de treino (máquina vai aprender) e dados de teste (máquina vai tentar acertar).

X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2,random_)

