# hoje continuamos a falar do algorítimo de árvores de decisão passando 
# agora pela escolha dos hiperparâmetros, ajuste e predição.

# Árvores de Decisão com Python
# Escolhendo Hiperparâmetros
# Vamos iniciar escolhendo os melhores hiperparâmetros para o algorítimo:

params = [
    {
    'criterion':['gini','entropy'],
    'max_depth':[None,2,4,8,10,30,50,100]
    }
]
ins = DecisionTreeClassifier(max_depth=4)
#grid_search = GridSearchCV(ins,params,cv=5,scoring='accuracy')
#grid_search.fit(X_train,y_train)
#grid_search.best_params_

# Fazendo Previsões
# Bora agora verificar as previsões feitas pelo nosso modelo:

ins.fit(X_train,y_train)
pred = ins.predict(X_test)
pred[:5]

y_test[:5]

# Medições de Desempenho
# Vamos verificar agora as medições de desempenho do algorítimo para o nosso conjunto de dados:

ins.score(X_test,y_test)

cross = cross_val_score(ins,X_test,y_test,cv=5,scoring="accuracy")
final = sum(cross) / len(cross)
final

print(classification_report(y_test,pred))

print(confusion_matrix(y_test,pred))

# Teste com Novos Dados
# Para verificar o funcionamento das árvores de decisão, vamos inserir um teste com dados que nosso algorítimo não conhece.

newX = pd.DataFrame([
    [4.1,2,3,2]
],columns=X.columns)
newX

pred = ins.predict(newX)
pred

