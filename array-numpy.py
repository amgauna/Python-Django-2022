# pip install numpy

#Introdução
import numpy as np
matriz = np.array([1,2,3],[4,5,6])
matriz

# Tipo
type(matriz)
matriz.dtype.name

# Dimensões
matriz.shape
matriz.size
matriz2 =np.random.randint(0,30,6).reshape(2,3)

#Criando valores
np.arrange(0,30,3)
np.linspace(0,10,4)
np.random.randint(0,30,5)
                  
# Operações com Numpy

import numpy as np
matriz = np.array([[1,2,3],[4,5,6]])
matriz.max()
matriz.argmax()
matriz.mean()
matriz.std()

matriz3 = np.array([[2,4,6],[8,7,1]])
matriz3.shape
matriz + matriz3
matriz * matriz3
matriz3 ** 2

# Seleção e Alteração de Valores
matriz3[1][1]
matriz3[0][2]
matriz3[matriz3>4]
matriz3[1][matriz3[1]>4]

matriz3[1][0] = 16
matriz3

matriz3 = np.insert(matriz3,1,[0,0,1],axis=0)
matriz3
matriz3.shape

