# python - lib Matplotlib - Introdução 

# Gráficos e Data Science
# Vamos iniciar instalando o módulo do Matplotlib:/

!pip install matplotlib

# Importando pacotes
# Vamos importar os pacotes necessários pra se trabalhar bem com Matplotlib:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# Repare que na última linha anterior rodamos o comando inline para facilitar 
# a exibição dos gráficos sem a necessidade de usar o método show.

# Plotando o primeiro gráfico
# Vamos plotar um gráfico com valores aleatórios para vermos o uso da lib:

X = [5,10,15,20,25]
y = [15, 25, 45, 55, 60]
plt.plot(X,y)
plt.show()

# Primeira plotagem com a lib Matplotlib do Python
# Personalizando gráfico
# Com a lib podemos também personalizar nomes dos eixos, criar legendas e assim por diante:

X = [5,10,15,20,25]
y = [15, 25, 45, 55, 60]
fig,axs = plt.subplots(figsize=(12,4))
axs.set_xlabel('Eixo X')
axs.set_ylabel('Eixo Y')
axs.set_title('Título do Gráfico')
axs.plot(X,y,"ro--",label="Dados 1")
axs.plot(y,X,"g<--",label="Dados 2")
axs.legend()

