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
                  
