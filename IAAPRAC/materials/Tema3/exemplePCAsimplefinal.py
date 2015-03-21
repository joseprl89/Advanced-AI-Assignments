# -*- coding: utf-8 -*-
from numpy import *
import pylab
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
set_printoptions(precision = 3)

# Datos: distribución normal multivariada en 3d 
mean = [1,5,10]
cov = [[-1,1,2],[-2,3,1],[4,0,3]]
d = random.multivariate_normal(mean,cov,1000)

# representación gráfica de los datos:
fig1 = plot.figure()
sp = fig1.gca(projection = '3d')
sp.scatter(d[:,0],d[:,1],d[:,2])
plot.show()

# ANALISIS PCA:
# Paso 1: Calcular la matriz de covarianza de los datos (N x N):
d1 = d - d.mean(0)
matcov = dot(d1.transpose(),d1)

# Paso 2: Obtener los valores y vectores propios de la matrix de covarianza:
valp1,vecp1 = linalg.eig(matcov)

# Paso 3: Decidir qué vectores son los relevantes representando
# los valores propios en orden decreciente (scree plot):
ind_creciente = argsort(valp1) # orden creciente 
ind_decre = ind_creciente[::-1] # orden decreciente 
val_decre = valp1[ind_decre] # valores propios en orden decreciente
vec_decre = vecp1[:,ind_decre] # ordenar tambien vectores propios
pylab.plot(val_decre,'o-')
pylab.show()


# Proyectar datos a la nueva base definida por los 
# todos los vectores propios (espacio PCA 3D)
d_PCA = zeros((d.shape[0],d.shape[1]))
for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        d_PCA[i,j] = dot(d1[i,:],vecp1[:,j])

# recuperar datos originales invirtiendo la proyección (reconstrucción):
orig_means = d.mean(0)
d_recon = zeros((d.shape[0],d.shape[1]))
for i in range(d.shape[0]):
    d_recon[i] = orig_means
    for j in range(d.shape[1]):
         d_recon[i] += d_PCA[i,j]*vecp1[:,j]

# comprobar que se recuperan los datos originales:
allclose(d,d_recon)


# Proyectar datos a la nueva base definida por los dos
# vectores propios con mayor valor propio (espacio PCA 2D)
d_PCA2 = zeros((d.shape[0],2))
for i in range(d.shape[0]):
    for j in range(2):
        d_PCA2[i,j] = dot(d1[i,:],vec_decre[:,j])

# reconstruir datos invirtiendo la proyección PCA 2D:
d_recon2 = zeros((d.shape[0],d.shape[1]))
for i in range(d.shape[0]):
    d_recon2[i] = orig_means
    for j in range(2):
         d_recon2[i] += d_PCA2[i,j]*vec_decre[:,j] 

# En general dará falso por el error introducido al descartar
# una componente
allclose(d,d_recon2)

# representación gráfica de los datos:
fig2 = plot.figure()
sp2 = fig2.gca(projection = '3d')
sp2.scatter(d_recon2[:,0],d_recon2[:,1],d_recon2[:,2],c='r',marker='x')
plot.show()
