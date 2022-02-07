# Lib Matplotlib - Gráficos de Data Frames

# Testes com Matplotlib
# Importando Módulos e DataFrame
# Vamos iniciar importando os módulos necessários e o DataFrame de testes:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# Para essa aula vamos usar o conjunto de dados da Netflix. Para baixá-lo basta clicar aqui.

df = pd.read_csv("netflix_titles.csv",sep=',')
df.head()
Eixos X e Y

# Vamos fazer uma pequena análise das séries release_year e type deste DataFrame e já separar eixos x e y.

x = df['release_year'].value_counts().index
y = df['release_year'].value_counts().values

# Criando gráficos
# Separados os eixos, podemos começar a criar gráficos. Veja alguns exemplos:

fig, axs = plt.subplots(figsize=(12,4))
axs.set_xlabel('Ano')
axs.set_ylabel('Quantidade')
axs.set_title('Quantidade de Filmes por ano')
axs.bar(x, y)

# Gráficos de barras com Matplotlib
# Podemos também criar outros tipos de gráficos como o gráfico de pizza:

x = df['type'].value_counts().index
y = df['type'].value_counts().values

fig1, ax1 = plt.subplots()
ax1.pie(y, labels=x, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
