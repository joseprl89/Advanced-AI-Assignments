from math import sqrt

# Calcula la distancia eucl�dea entre dos vectores/tuplas
def distEuclidea(v1, v2):
    return sqrt(sum(pow(x-y,2) for x,y in zip(v1,v2)))


# Calcula el enlace completo (m�ximo) entre dos grupos
# (distancia m�xima entre dos puntos de cada grupo)
def enlaceCompleto(puntos, g1, g2, dist = distEuclidea):
    # Busca el m�ximo en las combinaciones de puntos
    maxima = 0.0
    for p1 in g1:
        for p2 in g2:
            d = dist(puntos[p1], puntos[p2])
            if d > maxima:
                maxima = d
    return maxima


# Calcula el enlace simple (m�nimo) entre dos grupos
# (distancia m�m�nima entre dos puntos de cada grupo)
def enlaceSimple(puntos, g1, g2, dist = distEuclidea):
    # Busca el m�nimo en las combinaciones de puntos
    minima = float("inf")
    for p1 in g1:
        for p2 in g2:
            d = dist(puntos[p1], puntos[p2])
            if d < minima:
                minima = d
    return minima

# Dado un conjunto de puntos y un agrupamiento, fusiona
# los dos grupos m�s cercanos con el criterio indicado.
# "grupos" debe contener al menos dos grupos, y vuelve
# modificado, con los grupos elegidos fusionados.
def fusionaGrupos(puntos, grupos, criterio=enlaceCompleto,
                  dist=distEuclidea):
    if len(grupos) < 1: return
    
    # Busca el par de grupos m�s adecuados (valor m�nimo
    # del criterio utilizado).
    minimo  = float("inf")
    nombres = grupos.keys()
    for i in range(len(nombres)-1):
        for j in range(i+1, len(nombres)):
            d = criterio(puntos, grupos[nombres[i]],
                         grupos[nombres[j]], dist)
            if d < minimo:
                minimo    = d
                candidato = (nombres[i], nombres[j])

    # El nombre del nuevo grupo ser� el m�s bajo de los dos
    nombreGrupo = min(candidato)
    grupoBorrar = max(candidato)
    
    # Fusiona los dos grupos: a�ade los elementos a uno de
    # ellos y elimina el otro del diccionario "grupos".
    grupos[nombreGrupo].extend(grupos[grupoBorrar])
    del(grupos[grupoBorrar])
    

# Agrupamiento jer�rquico aglomerativo: fusiona grupos
# hasta obtener un �nico grupo
def agrupamientoAglomerativo(puntos, criterio=enlaceCompleto,
                             dist=distEuclidea):
    # Generaci�n del agrupamiento inicial (cada punto un grupo)
    grupos = {x:[x] for x in puntos}
    print(grupos)

    # Fusi�n de grupos hasta conseguir un �nico grupo
    while len(grupos) > 1:
        fusionaGrupos(puntos, grupos, criterio, dist)
        print(grupos)

# Lee un fichero con los datos de los jugadores, formato
# "horasJuego horasChat clase" (la clase se ignora)
def leeJugadores(nomFich="Jugadores.txt"):
    lineas = [(l.strip()).split("\t")
        for l in (open(nomFich).readlines())]
    # Se asigna un id=0,1,2,... a cada jugador
    diccio = {}
    for i in range(len(lineas)):
        diccio[i] = (float(lineas[i][0]), float(lineas[i][1]))
    return diccio


# Diccionario de puntos de ejemplo con sus coordenadas
puntos = {'A':(0.5,4.5), 'B':(1,4), 'C':(0.5,2), 'D':(1,1.5),
          'E':(2.5,2), 'F':(3.5,3.5), 'G':(4.5,2.5), 'H':(4,1)}


