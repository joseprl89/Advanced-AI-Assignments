from numpy import *
from numpy.linalg import eig


# Calcula la distancia euclídea entre dos vectores/tuplas
def distEuclidea(v1, v2):
    return sqrt(sum(pow(x-y,2) for x,y in zip(v1,v2)))


# Cálculo de la matriz de distancias de una lista de puntos
def matrizDist(puntos):
    # Crea una matriz de pxp, siendo p el número de puntos
    dist = zeros((len(puntos), len(puntos)))

    # Calcula las distancias entre puntos
    for i in range(len(puntos)):
        for j in range(i):
            d = distEuclidea(puntos[i], puntos[j])
            dist[i,j] = d
            dist[j,i] = d
    return dist


# Cálculo de la laplaciana sin normalizar
def laplaciana(W):
     I   = identity(len(W),float)
     D   = diag([sum(Wi) for Wi in W])
     L = D - W
     return L


# Generación del modelo espectral
def modeloEspectral(puntos):
    # Cálculo de los valores y vectores propios
    W = matrizDist(puntos)
    L = laplaciana(W)
    valp, vecp = eig(L)

    # Ordenación por valor propio (menor a mayor) de los valores
    # propios y de los vectores propios (por columnas)
    orden = sorted(range(len(valp)), key = valp.__getitem__)
    valp.sort()
    vecp2 = zeros((len(vecp), len(vecp)))
    for col in range(len(orden)):
        vecp2[:,col] = vecp[:,orden[col]]

    return valp, vecp2

# Lee un fichero con los datos de los jugadores, formato
# "horasJuego horasChat clase" (la clase se ignora), y
# devuelve una lista
def leeJugadores(nomFich="Jugadores.txt"):
    lineas = [(l.strip()).split("\t")
        for l in (open(nomFich).readlines())]

    lista = []
    for i in range(len(lineas)):
        lista.append((float(lineas[i][0]), float(lineas[i][1])))
    return lista


# Conjunto de puntos de ejemplo en forma de lista
puntos = [(0.5,4.5), (1,4), (0.5,2), (1,1.5),
          (2.5,2), (3.5,3.5), (4.5,2.5), (4,1)]
