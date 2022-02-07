# Na aula de hoje aprenderemos um novo algorítimo de Machine Learning, conhecido 
# como KNN ou K vizinhos mais próximos.

# KNN no Machine Learning
# O hiperparâmetro k tem forte importância no KNN e representa a quantidade de 
# vizinhos que você quer comparar a sua classe.
# Veja um exemplo de KNN
#  Repare que dependendo do k escolhido a classificação pode ser bem diferente.

# Importando módulos
# Vamos importar os módulos necessários para rodar a nossa análise:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
%matplotlib inline

# Importando DataFrame
# Neste exemplo vamos classificar um câncer como benigno ou maligno de acordo com as características
# da pele, sangue e outras características. Para baixar o dataset clique aqui.

df = pd.read_csv("cancer.csv")
df.head()

# Preparando os dados
# Vamos excluir colunas desnecessárias, transformar dados string em dados binários e limpar dados 
# vazios para preparar nossos dados para o aprendizado de máquina:

del df["id"]

del df["Unnamed: 32"]

df['diagnosis'].unique()

idCat, cat = pd.factorize(df['diagnosis'])
idCat
#M = 0 B = 1
df['diagnosisCat']=idCat

# Análise exploratória
# Vamos analisar os nossos dados e a integração entre eles:

df.info()

df.describe()

sns.countplot(x='diagnosisCat',data=df)

df['diagnosisCat'].value_counts()

# Aprofundando em KNN no Python
# Divisão em Dados de Treino e Teste
# Vamos dividir o nosso conjunto de dados em treino e teste:

X = df.drop('diagnosisCat',axis=1)
y = df['diagnosisCat']
y.head()

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=100)

X_train.shape
X_test.shape

# Escalonamento de Dados
# Como possuímos features com números muito distantes, precisamos escalonar, normalizar, esses velores
# antes de iniciar o algorítimo para que nosso modelo não priorize determinada série em deterimento a outra.

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_train = pd.DataFrame(X_train, columns=X.columns)
X_test = sc.transform(X_test)
X_test = pd.DataFrame(X_test, columns=X.columns)
X_test

# Escolhendo melhores hiperparâmetros
# Com a escolha dos melhores hiperparâmetros conseguimos extrair dados mais precisos do nosso conjunto de dados.

params = [
    {
    'n_neighbors':[1,3,6,9,12,15],
    'weights':['uniform','distance']
    }
]
ins = KNeighborsClassifier(n_neighbors=6, weights='distance')
#grid_search = GridSearchCV(ins,params,cv=5)
#grid_search.fit(X_train,y_train)
#grid_search.best_params_

# Ajustando e Fazendo Previsões
# Vamos fazer previsões dos valores de treino e verificar se no teste os valores batem:

ins.fit(X_train,y_train)
pred = ins.predict(X_test)
pred[:5]

y_test[:5]

# Testando o desempenho
# Vamos verificar se este modelo de algorítimo é adequado para o nosso conjunto de dados:

ins.score(X_test,y_test)

cross = cross_val_score(ins,X_test,y_test,cv=10,scoring="accuracy")
final = sum(cross) / len(cross)
final

