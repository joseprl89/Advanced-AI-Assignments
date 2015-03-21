import numpy as np
import pylab
from scikits.learn.lda import LDA

# Datos gaussianos:
mu1, sigma1 = 10, 5.5
X1 = mu1 + sigma1*np.random.randn(100,2)
mu2, sigma2 = -10, 5.5
X2 = mu2 + sigma2*np.random.randn(100,2)

# Representar gráficamente los datos de entrenamiento: 
fig1 = pylab.figure()
pylab.scatter(X1[:,0],X1[:,1],marker ='^',c='r')
pylab.scatter(X2[:,0],X2[:,1],marker ='o',c='b',hold='on')
pylab.legend(('Grupo 1', 'Grupo 2'))

# Concatenar los dos conjuntos de puntos:
XT = np.concatenate((X1,X2))

# Etiquetar los datos como tipo 1 o tipo 2:
label1 = np.ones(X1.shape[0])
label2 = 2*np.ones(X2.shape[0])
labelT = np.concatenate((label1,label2))

# Fase de entrenamiento: 
clf = LDA()
clf.fit(XT, labelT)
LDA(priors=None)

#Fase de predicción:
print clf.predict([[20, 0]]) #predicción para el dato [20,0]
print clf.predict([[5, -20]])#predicción para el dato [5,-20]

# Representación de la predicción de los datos [20,0] y [5,-20]:
pylab.scatter(20,0,s=100,marker ='x',c='k')
pylab.annotate('LDA grupo 1',xy=(20,-2),xycoords='data',
               xytext=(-50,-50),
               textcoords='offset points',
               arrowprops=dict(arrowstyle="->")) 
pylab.scatter(-15,-5,s=100,marker ='x',c='k')
pylab.annotate('LDA grupo 2',xy=(-15,-5),xycoords='data',
               xytext=(-50,50),
               textcoords='offset points',
               arrowprops=dict(arrowstyle="->")) 

# Predicción de datos en una retícula:
fig2 = pylab.figure()
for i in range(-20,21,1):
    for k in range(-20,21,1):
        p = clf.predict([[i, k]])
        print i,k,p
        if p == 1:
             pylab.scatter(i,k,s=20,marker='o',c='r',hold='on')
        else:
             pylab.scatter(i,k,s=20,marker = 'o',c='b',hold='on')

pylab.axis([-20,20,-20,20])
pylab.text(5,5,'GRUPO 1',fontsize=25,fontweight='bold',color='k')
pylab.text(-10,-10,'GRUPO 2',fontsize=25,fontweight='bold',color='k')

pylab.show()
        




