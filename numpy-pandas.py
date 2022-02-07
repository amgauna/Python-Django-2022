# Python e Pandas

# Para instalarmos a biblioteca vamos rodar o seguinte comando:
# !pip install pandas

# Importando Libs

import numpy as np
import pandas as pd

# Criando DataFrame

# Abaixo estão listadas algumas formas de criar DataFrames com Pandas:
#df = pd.DataFrame([['a','b','c'],[1,2,3]])
#df = pd.DataFrame({'a':[1,2,3],'b':[5,6,7]})
#df = pd.DataFrame(np.random.randn(3,2))

df = pd.DataFrame(np.random.randint(1,10,6).reshape(2,3),
                  columns=['Cruzeiro','Atletico','America'],
                 index=['Gols','Vitorias'])
df

# O DataFrame criado acima ficou assim:
# DataFrame com Pandas e Seleção de Dados

# Nesta seção iremos demonstrar as formas de selecionar valores e séries do DataFrame.

type(df['Atletico'])
df['Cruzeiro']['Vitorias']
df.Cruzeiro

# A diferença do método loc para o iloc é que o loc pega pelo número 
# ou valor do índice, já o iloc pega pela posição do índice.

df.loc['Vitorias']
df.loc[['Vitorias'],['Atletico','America']]

df.iloc[1]
df.iloc[0,1:3]
