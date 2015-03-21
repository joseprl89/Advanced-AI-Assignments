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

# construir una lista con los ficheros con extensión '.jpg'
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

NPIX = n*m    # Numero de píxeles de cada imagen:
NIM = len(imlist) # Numero de imágenes a analizar:

# Crear una matriz de tamaño NIM x NPIX:
A = numpy.array([numpy.array(Image.open(imlist[i])).flatten()
                     for i in range(NIM)],'f')

###############################
# ANALISIS PCA
###############################

# Centrado de los datos restando la media:
im_media = A.mean(axis=0)
for i in range(NIM):
      A[i] -= im_media

M = dot(A,A.T) # matriz AA' (NIM x NIM)
lam,vec = linalg.eigh(M) # obtener los NIM vectores y valores propios de M = AA'
aux = dot(A.T,vec).T # aplicar w = A'v para obtener los vectores propios de A'A 
V = aux[::-1] # ordenar vectores propios 
S = sqrt(lam)[::-1] # ordenar valores propios de A 

# Recomponer la imagen media:
im_media = im_media.reshape(m,n)

# Representar los autovalores PCA
pylab.plot(S[0:10],'o-')

# Obtener los dos primeros modos PCA y representarlos:
modo1 = V[0].reshape(m,n) 
modo2 = V[1].reshape(m,n)

# Representar graficamente:
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

