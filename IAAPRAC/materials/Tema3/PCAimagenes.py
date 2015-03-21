import os
from PIL import Image
import numpy
import pylab
from pca_im import *

import matplotlib.pyplot as plt

###############################
# COSNTRUIR MATRIZ DE DATOS
###############################

# Obtener directorio actual en el que están las imágenes
path= os.getcwd()  
dirList=os.listdir(path)

# construir una lista con los ficheros
# con extension '.jpg' en el directorio
imlist = []
i = 0
for fname in dirList:
    filename, filext = os.path.splitext(fname)
    if filext == '.jpg':
        imlist.append(fname) 
        i = i +1
          
# Abrir la primera imagen y obtener su tamaño en píxeles
im = numpy.array(Image.open(imlist[0])) 
m,n = im.shape[0:2]
# Numero de pixels de cada imagen:
NPIX = n*m

# Numero de imágenes a analizar:
NIM = len(imlist)

# Crear una matriz de tamaño NIM x NPIX con las NIM imágenes
# desplegadas en forma de vectores fila de longitud NPIX:
A = numpy.array([numpy.array(Image.open(imlist[i])).flatten()
                     for i in range(NIM)],'f')

###############################
# ANÁLISIS PCA
###############################

# Centrado de los datos restando la media:
im_media = A.mean(axis=0)
for i in range(NIM):
      A[i] -= im_media

# Para calcular PCA hay que diagonalizar la matriz A'A de tamaÒo NPIX x NPIX.
# Debido a que NPIX >> NIM, en su lugar diagonalizamos la matriz AA' de tamaÒo
# mucho menor (NIM x NIM) puesto que ambas matrices comparten los valores propios no nulos.
# Diagonalizacion de AA': AA'v = lambda*v (1)
# Diagonalizacion de A'A: A'A w = lambda*w (2)
# Relacion entre ambas: multiplicando (1) por A' por la izquierda, tenemos
# A'AA'v = A'lambda*v (3).
# Indentificando (3) con (2) tenemos que w = A'v. 


M = dot(A,A.T) # matriz AA' de dimensionalidad reducida (NIM x NIM)
lam,vec = linalg.eigh(M) # obtener los NIM vectores y valores propios de M = AA'
aux = dot(A.T,vec).T # obtener los vectores propios de A'A con valores
                     # propios no nulos vienen dados por w = A'v  
# los últimos vectores propios son los relevanetes (están ordenados de menor a mayor autovalor)
V = aux[::-1] 
S = sqrt(lam)[::-1] 

# Recomponer la imagen media:
im_media = im_media.reshape(m,n)

## Representar los autovalores PCA
pylab.plot(S[0:10],'o-')

# Obtener los dos primeros modos PCA y representarlos:
modo1 = V[0].reshape(m,n) 
modo2 = V[1].reshape(m,n)

# Representar gráficamente:
fig1 = pylab.figure()
fig1.suptitle('Imagen promedio')
pylab.gray()
pylab.imshow(im_media)
##
fig2 = pylab.figure()
fig2.suptitle('Primer modo PCA')
pylab.gray()
pylab.imshow(modo1)
##
fig3 = pylab.figure()
fig3.suptitle('Segundo modo PCA')
pylab.gray()
pylab.imshow(modo2)
pylab.show()

