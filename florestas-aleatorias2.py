# Hoje aprenderemos como dividir os dados em treino e teste e aplicar esses 
# conjuntos no modelo de generalização Florestas Randômicas.

# Florestas Randômicas
# Divisão dos Dados

# Vamos começar dividindo nossos dados em dados de treino e teste:

X = df.drop("Purchased",axis=1)
y = df["Purchased"]
X.head()

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=100)
X_train.shape
y_test.shape

# Não é necessário realizar o escalonamento de dados para ensembles. Escolhendo melhores hiperparâmetros.
# Vamos escolher as melhores configurações para o modelo de Florestas Aleatórias para o nosso conjunto de dados:

params = [
    {
        "max_depth":[4,8,12],
        "max_features":[1,2,3],
        "min_samples_leaf":[4,8,12],
        "min_samples_split":[4,8,12]
    }
]
ins = RandomForestClassifier(max_depth=4,max_features=1,min_samples_leaf=12,min_samples_split=8)
#grid_search = GridSearchCV(ins,params,cv=5)
#grid_search.fit(X_train,y_train)
#grid_search.best_params_

# Ajustando e Fazendo Predições
# Vamos ajustar o medelo de Florestas Randômicas ao conjunto de dados e vamos ver os resultados 
# que ele exibe em relação ao conjunto de testes.

ins.fit(X_train,y_train)
pred = ins.predict(X_test)
pred[:10]

y_test[:10]

# Verificando desempenho do modelo
# Vamos ver a taxa de acertos do nosso modelo:

ins.score(X_test,y_test)

cross = cross_val_score(ins,X_test,y_test,cv=10,scoring="accuracy")
final = sum(cross) / len(cross)
final

print(classification_report(y_test,pred))

print(confusion_matrix(y_test,pred))

# Testando Novos Dados
# Para finalizar, vamos testar novos dados:

newX = pd.DataFrame([
    [48,29000,0]
],columns=X.columns)
pred2 = ins.predict(newX)
pred2

