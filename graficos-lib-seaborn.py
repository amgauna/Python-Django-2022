# Python e Pandas - lib Seaborn, porém agora com um Data Frame mais complexo.

# Aprendendo Seaborn - Python
# Na aula de hoje vamos trabalhar com o Dataset car_crashes.csv 
# que pode ser baixado no Github = https://github.com/mwaskom/seaborn-data

# Importando Data Frame
# Vamos importar o Data Frame de acidentes veiculares baixado no site do Github e já vamos fazer nossa análise exploratória:

df = pd.read_csv("car_crashes.csv",sep=",")
df.head()

df.info()
sns.pairplot(df)

# Pairplot Python
# Podemos também utilizar outros gráficos para entender melhor nossos dados:

sns.heatmap(df.corr(),annot=True)

# Heatmap Python

sns.jointplot(x='alcohol',y='speeding',data=df,kind='reg')
sns.jointplot(x='alcohol',y='no_previous',data=df,kind='reg')

