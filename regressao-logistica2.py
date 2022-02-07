# Predizendo Valores através da Regressão Logística

# Separando Conjunto de Dados
# Vamos começar separando os nossos dados em X (rótulos) e y (valores a serem preditos)

X = df.drop("DiseaseCat",axis=1)
X

y=df["DiseaseCat"]
y

# Através dos dados separados acima, podemos criar mais dois subgrupos, que serão o X_train, y_train 
# (para a máquina aprender com os dados) e o X_test, y_test (a máquina não conhece) para verificarmos 
# a eficiência do nosso modelo.

X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=100)

# Escalonamento dos Dados
# Para evitar dimensões de dados muito distantes uma das outras, devemos trazer os valores para uma
# escala mais próxima, evitando assim ruídos na análise:

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_train = pd.DataFrame(X_train, columns=["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"])
X_test = sc.transform(X_test)
X_test = pd.DataFrame(X_test, columns=["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"])
X_train

# Definindo melhores hiperparâmetros
# A escolha dos melhores hiperparâmetros ajuda bastante o algorítimo a trazer melhores resultados:

params=[
    {
    "penalty": ["l1","l2"],
    "C":[0.1,0.3,0.5,0.7,0.9,1,10,100]
    }
]
ins = LogisticRegression(C=0.9)
#grid_search = GridSearchCV(ins,params,cv=10)
#grid_search.fit(X_train,y_train)
#grid_search.best_params_

# Predizendo Valores
# Agora vamos predizer os valores de acordo com o aprendizado de máquina:

ins.fit(X_train,y_train)
pred = ins.predict(X_test)
pred[:10]

# Avaliando o Desempenho
# Uma importante ação na análise de dados é avaliar o desempenho do algorítimo:

ins.score(X_test,y_test)
print(classification_report(y_test,pred))
print(confusion_matrix(y_test,pred))

