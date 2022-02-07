# Aprofundando o estudo em Regressão Linear

# Escalonamento das Características
# Padronizamos nossas características pra ajustar o desvio padrão e evitar muitas distorções de variações de dados:

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_train = pd.DataFrame(X_train, columns=["cylinders","displacement","horsepower","weight"])
X_test = sc.transform(X_test)
X_test = pd.DataFrame(X_test,columns=["cylinders","displacement","horsepower","weight"])

# Definindo o melhor hiperparâmetro
# Os hiperparâmetros são as configurações que você envia para o algorítimo para que ele retorne o resultado. 
# Nem sempre os melhores hiperparâmetros são os padrões, para isso precisamos testar quais são as melhores características para o nosso algorítimo.

params = [
    {
        'fit_intercept':[True,False],
        'normalize':[True,False],
        'copy_X':[True,False],
        'n_jobs':[1,10,20,30,40],
        'positive':[True,False],
    }
]
ins = LinearRegression(normalize=True)
grid_search = GridSearchCV(ins,params,cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train,y_train)
grid_search.best_params_

# Ajustando e predizendo valores
# Agora que já dividimos os nossos dados e já temos os melhores hiperparâmetros podemos acionar nosso algorítimo
# para que ele aprenda com os dados e tente adivinhar os valores do conjunto de teste:

ins.fit(X_train,y_train)
pred = ins.predict(X_test)
pred[:10]

y_test[:10]

# Testes de Desempenho do Algorítmo
# Uma importante etapa do Machine Learning é verificar o desempenho das predições do algorítimo que estamos trabalhando, 
# verificando qual a sua taxa de erro, para assim avaliarmos se aquele modelo vai atender a nossa necessidade:

ins.score(X_test,y_test)

print("RMSE",np.sqrt(mean_squared_error(y_test,pred)))

cross = cross_val_score(ins,X_test,y_test,cv=10)
final = sum(cross) / len(cross)
final

# Testando se o modelo generaliza bem
# Pra fechar a análise do nosso modelo, vamos pegar alguns carros que não estavam no conjunto de dados e jogar no
# modelo pra ver se ele consegue retornar os galoes por milha (km/l) de forma correta:

X_real = pd.DataFrame([
    ["4","303","94",df["weight"].mean(),df["acceleration"].mean(),"1990",1]
],columns=X.columns.to_list())
X_real=sc.fit_transform(X_real)
pred = ins.predict(X_real)
pred

# Ao fim chegamos a conclusão que o modelo exibe resultados com precisão entre 73% e 80% e tem uma taxa de erro 
# médio de 3 galões por milha (km/l).
