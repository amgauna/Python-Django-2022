# Python e Pandas - União, Filtros e Apply

# Pandas e Python - Filtros
# Vamos criar primeiramente dois DataFrames fictícios.

df1 = pd.DataFrame({'A':[1,2,3],'B':[4,5,6]},index=[19,20,21])
df2 = pd.DataFrame({'C':['a','b','c'],'D':['d','e','f']},index=[20,21,22])

# União de DataFrames
# Agora que já temos dois conjunto de dados, podemos trabalhar os métodos de união:

pd.concat([df1,df2], axis=1)
df1.join(df2,how='outer').fillna(df1['A'].mean())

# Filtros de Dados
# Vamos verificar agora como filtrar dados em DataFrames usando Python.

df1['C']=[8,10,12]
df1.loc[22]=[13,16,19]
df1[df1['A']>2]
df1[(df1['A']>2) & (df1['C']>15)]
df1[df1['B'] == 6]

# O operador E é representado pelo e comercial (&) e o operador OU é representado pelo pipe (|).

# Método Apply
# O método apply nos ajuda a percorrer um DataFrame executando operações dentro dos dados.

df1.apply(lambda x:x*3)

def maioresCincoA(x):
    if x > 5:
        return True
    else:
        return False

    
#df1['Maiores']=df1['A'].apply(maioresCincoA)
    
df1['A']=df1['A'].apply(maioresCincoA)
    
    

