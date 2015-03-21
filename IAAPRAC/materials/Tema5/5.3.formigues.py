# -*- coding: utf-8 -*-
import random, sys, math

# Nota: en comptes de matrius es fan servir llistes de llistes

# Genera una matriu de distàncies de nCiutats x nCiutats
def matriuDistancies(nCiut, distanciaMaxima):
    matriu = [[0 for i in range(nCiut)] for j in range(nCiut)]

    for i in range(nCiut):
        for j in range(i):
            matriu[i][j] = distanciaMaxima*random.random()       
            matriu[j][i] = matriu[i][j]

    return matriu

# Tria el pas d'una formiga, tenint en compte les distàncies i les
# feromones i descartant les ciutats ja visitades
def triaCiutat(dists, ferom, visitades):
	# Es calcula la taula de pesos de cada ciutat
    llistaPesos = []
    disponibles = []
    actual      = visitades[-1]

    # Influència de cada valor (alfa: feromones; beta: distàncies)
    alfa = 1.0
    beta = 0.5

    # El paràmetro beta (pes de les distàncies) és 0.5, alfa=1.0
    for i in range(len(dists)):
        if i not in visitades:
            fer  = math.pow((1.0 + ferom[actual][i]), alfa)
            pes  = math.pow(1.0/dists[actual][i], beta) * fer
            disponibles.append(i)
            llistaPesos.append(pes)

	# Es tria aleatòriament cadascuna de les ciutats disponibles,
	# tenint en compte el seu pes relatiu
    valor     = random.random() * sum(llistaPesos)
    acumulat  = 0.0
    i         = -1
    while valor > acumulat:
        i         += 1
        acumulat  += llistaPesos[i]

    return disponibles[i]    

# Genera una "formiga", que triarà un camí tenint en compte les 
# distàncies i els rastres de feromones. Torna una tupla amb el camí
# i la seva longitud.
def triaCami(distancies, feromones):
	# La ciutat inicial sempre és la 0
    cami     = [0]
    longCami = 0

	# Tria cada pas segons la distància i les feromones
    while len(cami) < len(distancies):
        ciutat      = triaCiutat(distancies, feromones, cami)
        longCami += distancies[cami[-1]][ciutat]
        cami.append(ciutat)

	# Per terminar s'ha de tornar a la ciutat d'origen (0)
    longCami += distancies[cami[-1]][0]
    cami.append(0)
    
    return (cami, longCami)

# Actualitza la matriu de feromones seguint el cami rebut
def rastreFeromones(feromones, cami, dosi):
    for i in range(len(cami) - 1):
        feromones[cami[i]][cami[i+1]] += dosi

# Evapora totes les feromones multiplicant-les per una constant
# = 0.9 (és a dir, el coeficient d'evaporació és 0.1)
def evaporaFeromones(feromones):
    for llista in feromones:
        for i in range(len(llista)):
            llista[i] *= 0.9

# Resol el problema del viatjant de comerç mitjançant l'algorisme de
# la colònia de formigues. Rep una matriu de distàncies i torna una
# tupla amb el millor camí que ha obtingut (llista d'índexos) i la
# seva longitud.
def formigues(distancies, iteracions, distMitjana):
    # Primer es crea una matriu de feromones buida
    n = len(distancies)
    feromones = [[0 for i in range(n)] for j in range(n)]

    # El millor camí i la seva longitud (inicialment "infinita")
    millorCami     = []
    longMillorCami = sys.maxint

	# A cada iteració es genera una formiga, que tria un camí, i si és
	# millor que el millor que teníem, deixa el seu rastre de
	# feromones (més gran quan més curt sigui el camí)
    for iter in range(iteracions):
        (cami,longCami) = triaCami(distancies, feromones)

        if longCami <= longMillorCami:
            millorCami     = cami
            longMillorCami = longCami
        
        rastreFeromones(feromones, cami, distMitjana/longCami)

		# En qualsevol cas, les feromones es van evaporant
        evaporaFeromones(feromones)

	# Es torna el millor camí que s'hagi trobat
    return (millorCami, longMillorCami)


# Generació d'una matriu de prova
numCiutats      = 10
distanciaMaxima = 10
ciutats         = matriuDistancies(numCiutats, distanciaMaxima)

# Obtenció del millor camí
iteracions  = 1000
distMitjana = numCiutats*distanciaMaxima/2
(cami, longCami) = formigues(ciutats, iteracions, distMitjana)
print("Camí: ", cami)
print("Longitud del camí: ", longCami)





