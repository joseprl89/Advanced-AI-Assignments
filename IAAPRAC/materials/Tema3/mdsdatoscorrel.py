from numpy import *
from scaledown import *
import pylab as py

# Matriz de datos (N variables x M observaciones):
N = 10
M = 30

# Generar datos a partir de 3 grupos con correlaciones diferentes:

Xinit1 = random.randn(1,N) # cluster 1 (correlación baja)
X1 = Xinit1
for i in range(1,M/3,1):
    X1 = concatenate((X1,100*Xinit1 + random.rand(1,N)))

Xinit2 = random.randn(1,N) # cluster 2 (correlación media)
X2 = Xinit2
for i in range(1,M/3,1):
    X2 = concatenate((X2,50*Xinit2 + random.rand(1,N)))
    
Xinit3 = random.randn(1,N) # cluster 3 (correlación alta)
X3 = Xinit3
for i in range(1,M/3,1):
    X3 = concatenate((X3,10*Xinit3 + random.rand(1,N)))
    
#Representación correlaciones de cada grupo:
fig1 = py.figure()
py.scatter(X1[0],X1[1],marker='o',hold='on')
py.scatter(X2[0],X2[1],marker='x',hold='on')
py.scatter(X3[0],X3[1],marker='v',hold='on')

A = concatenate((X1,X2,X3))

# Escoger métrica de espacio original (Euclídea o Pearson):
metrica = euclidean
# metrica = pearson

# Técnica MDS: Devuelve la posición de los datos
# originales en un espacio 2D:
mds = scaledown(A,metrica)

# Representación de los datos en el espacio 2D MDS:
fig1 = py.figure()
for i in range(0,M/3,1):
    py.scatter(mds[i][0],mds[i][1],marker='o',c='r')
for i in range(M/3,2*M/3,1):
    py.scatter(mds[i][0],mds[i][1],marker='x',c='g')
for i in range(2*M/3,M,1):
    py.scatter(mds[i][0],mds[i][1],marker='v',c='b')
fig1.suptitle('Metrica Euclidea')
py.show()

