# Manipulando DataFrames com Pandas
# Adicionando e removendo linhas e colunas

df['Flamengo']=[3,17]
df.loc['Empates']=[0,0,0,0]
df.drop('America', axis=1, inplace=True)
del df['Cruzeiro']
df.drop('Empates',axis=0,inplace=True)
Remover dados faltantes ou duplicados

df2 = pd.DataFrame({'a':[1,1,np.nan],'b':[1,6,7],'c':[2,4,np.nan]})
df2.dropna()
df2.drop_duplicates(subset=['a'])
df2.fillna('Thiago')
df2.fillna(value=df2['b'].mean())
