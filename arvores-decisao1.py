# hoje iniciaremos um novo algorítimo de machine learning dentro do Python, o modelo conhecido como Árvores de Decisão.

# Entendendo as Árvores de Decisão
# Na aula de hoje trabalharemos com um dataset nativo de classificação de flores da espécie íris.

# Importando Módulos
# Como sempre, vamos iniciar importando os módulos necessários:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from IPython.display import Image
%matplotlib inline

# Importando Dataset
# Como mencionado anteriormente, vamos trabalhar com um dataset de classificação de espécies de íris
# de acordo com o cumprimento de sépalas e pétalas dessas flores:

df = pd.read_csv("Iris.csv")
df.head()

# Preparando os dados
# Já foi falado em aulas anteriores que o algorítimo consegue trabalhar melhor com valores numéricos que com strings.
# Para tanto, no nosso Dataframe vamos substituir o valor nominal das espécies por valores inteiros. Veja como fazer:

idCat,cat = pd.factorize(df["Species"])
idCat

cat

df['SpeciesCat']=idCat

del df['Id']
del df["Species"]

# Análise Exploratória
# Vamos entender os dados através da análise exploratória:

df.info()

df.describe()

sns.countplot(df["SpeciesCat"])

sns.pairplot(df,hue="SpeciesCat")

sns.swarmplot(x="SpeciesCat",y="PetalWidthCm",data=df)

# Dividindo Dados de Treino e Teste
# Continuando nossa análise inicial dos dados, vamos dividir o conjunto de dados para a máquina treinar 
# o aprendizado e vamos reservar alguns dados para que ela teste o seu próprio aprendizado. 
# Lembrando que os dados de teste a máquina não conhece, então funciona como uma prova pra ela:

X = df.drop("SpeciesCat",axis=1)
y = df["SpeciesCat"]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=100)

X_train.shape


y_train.shape
