import numpy as np
import pylab as py
import scipy as sc
import mdp
from mdp import fastica

# Fuentes originales
t = np.linspace(0,10,1000)
Sa = np.sin(2*sc.pi*t)
Sb = np.sin(13*sc.pi*t)

S1 = Sa.reshape(1,-1)
S0 = Sb.reshape(1,-1)
S = np.concatenate((S0,S1))

# Datos mezclados
A = [[1, 4], [-3, 2]] # Matriz de mezcla

X = np.dot(A, S) # Observaciones 

# Descomposicion ICA:

y_ICA = mdp.fastica(X.T, dtype='float32')

# representacion de resultados:
fig1 = py.figure()
py.subplot(211)
py.plot(S.T[:,0])
py.subplot(212)
py.plot(S.T[:,1])
fig1.suptitle('Fuentes originales')

fig2 = py.figure()
py.subplot(211)
py.plot(X.T[:,0])
py.subplot(212)
py.plot(X.T[:,1])
fig2.suptitle('Fuentes mezcladas')

fig3 = py.figure()
py.subplot(211)
py.plot(y_ICA[:,0])
py.subplot(212)
py.plot(y_ICA[:,1])
fig3.suptitle('Componentes independientes (ICA)')

py.show()

