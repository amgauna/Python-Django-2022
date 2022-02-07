# Python - Pandas e Seaborn - Introdução

# Seaborn e Pandas
# O site da documentação do Seaborn é o seguinte. Para baixar a biblioteca podemos rodar o seguinte comando:

pip install seaborn

# Importando Módulos
# Como sempre o primeiro passo é importar os módulos necessários:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# DataFrame e Análise Exploratória
# Vamos instanciar o DataFrame e verificar como estão dispostos os nossos dados:

df = pd.read_csv("flights.csv",sep=",")
df.head()

df.info()
df.describe()

# Plotagem de Gráficos
# Nos exemplos da aula utilizaremos os datasets do seaborn presentes neste site.
# Vamos iniciar a criação de gráficos com Seaborn:

sns.displot(df['passengers'],bins=50)

# Gráfico Displot
# Podemos também combinar métodos do Matplotlib com o Seaborn como no exemplo abaixo.

plt.figure(figsize=(12,8))
sns.barplot(x='year',y='passengers',data=df)

# Gráfico Barplot

sns.jointplot(x='year',y='passengers',data=df)

# Gráfico Jointplot
# O gráfico de Pairplot é um dos mais utilizados na análise exploratória.

sns.pairplot(df,hue='month')

# Gráfico Pairplot
# O gráfico de calor nos mostra as correlações entre as séries do nosso DataFrame, 
# sendo que quanto mais próximo de 1 maior a correlação.

sns.heatmap(df.corr(),annot=True)//

