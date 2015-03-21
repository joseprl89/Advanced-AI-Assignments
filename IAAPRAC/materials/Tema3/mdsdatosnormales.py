from numpy import *
from scaledown import *
import pylab as py

# Matriz de datos (N variables x M observaciones):
N = 4
M = 30

# Generar datos a partir de 3 clusters diferentes:

X1 = 10 + 2*random.randn(M/3,N) # cluster 1 (dispersi�n media)
X2 = -10 + 5*random.randn(M/3,N) # cluster 2 (dispersi�n alta)
X3 = 1*random.randn(M/3,N) # cluster 3 (dispersi�n baja)

A = concatenate((X1,X2,X3))

# Escoger m�trica de espacio original (Eucl�dea o Pearson):
metrica = pearson
# metrica = euclidean

# T�cnica MDS: Devuelve la posici�n de los datos
# originales en un espacio 2D:
mds = scaledown(A,metrica)

# Representaci�n de los datos en el espacio 2D MDS:
fig1 = py.figure()
for i in range(0,M/3,1):
    py.scatter(mds[i][0],mds[i][1],marker='o',c='r')
for i in range(M/3,2*M/3,1):
    py.scatter(mds[i][0],mds[i][1],marker='v',c='g')
for i in range(2*M/3,M,1):
    py.scatter(mds[i][0],mds[i][1],marker='x',c='b')
fig1.suptitle('Metrica Pearson')
py.show()
