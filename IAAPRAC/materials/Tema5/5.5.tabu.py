# -*- coding: utf-8 -*-
# Nota: els grafs es representen com llistes de llistes
from random import randint, random

# Donats dos nodes, torna 1 si estan connectats, 0 si no
def connectats(graf, node1, node2):
    if node1 < node2:
        node1, node2 = node2, node1
    if node1 == node2:
        return 0
    else:
        return graf[node1][node2]


# Funció objectiu, que compta els vèrtexes connectas que tenen el
# mateix color
def objectiu(graf, estat):
    suma = 0
    for i in range(len(estat)-1):
        for j in range(i+1,len(estat)):
            if estat[i] == estat[j]:
                suma += connectats(graf, i, j)
    return suma  

# Torna una llista amb els vèrtexes que tenen algun problema
# (estan connectats a un altre del mateix color)
def vertexesProblema(graf, estat):
    nVertexes = len(estat)
    vertexes  = []
    for i in range(nVertexes):
        trobat = False
        j = 0
        while j<nVertexes and not trobat:
            if (estat[i]==estat[j]) and connectats(graf, i, j):
                trobat = True
            j += 1
        if trobat:
            vertexes.append(i)
    return vertexes

# Genera la llista de veïns d'un estat i torna el millor d'ells,
# tenint en compte la informació tabú i actualitzant-la per anotar
# el canvi d'estat produït
def vei(graf, estat, k, tabu, iterTabu):
    nVertexes = len(estat)
    
    # Primer de tot s'obtenen tots els vèrtexes connectats a algun
    # altre vèrtex del mateix color
    vertexes = vertexesProblema(graf, estat)

	# Per cadascun d'aquests parells, es proposa una nova solució
	# que consisteix a canviar el color d'un dels vèrtexes 
	# (tot comprovant que no prengui un color tabú).
    candidats = []
    for v in vertexes:
        # Si queden colors disponibles per aquell vèrtex
        if len(tabu[v]) < k:
            nouColor = randint(1,k)
            while tabu[v].has_key(nouColor):
                nouColor = randint(1,k)
            nouEstat    = estat[:]
            nouEstat[v] = nouColor
            candidats.append(nouEstat)

    # Es torna el millor estat obtingut (funció objectiu menor).
    # Si no hi ha solucions possibles (els vèrtexes problemàtics tenen
    # tots els colors en tabú) es torna un canvi a l'atzar per tal de
    # desbloquejar la situació.
    if len(candidats) > 0:
        triat  = min(candidats, key=lambda e:objectiu(graf,e))
        posicio = candidats.index(triat)
        canviat = vertexes[posicio]
    else:
        triat  = estat[:]
        canviat = sample(vertexes, 1)[0]
        triat[canviat] = randint(1, k)

    # S'afegeix el canvi a la llista tabú
    tabu[canviat][estat[canviat]] = iterTabu
    return triat

# Actualitza la informació tabú, descomptant una iteració de totes 
# les entrades i eliminant les que arribin a 0
def actualitzaTabu(tabu):
    for tabuVertex in tabu:
        for color in tabuVertex.keys():
            tabuVertex[color] -= 1
            if tabuVertex[color] <= 0:
                del tabuVertex[color]


# Donats un graf, una assignació inicial i un nombre de colors, busca
# una assignació òptima fent servir cerca tabú.
# També cal indicar el nombre màxim d'iteracions, així com el nombre
# d'iteracions que es manté un color en tabú.
def cercaTabu(graf, asignacio, k, iteracions, iterTabu):

    estat     = asignacio[:]
    millor    = estat[:]
    nVertexes = len(estat)

	# L'estructura "tabú" emmagatzema, per cada vèrtex (posicions a la
	# llista), els colors que té prohibits (claus de cada diccionari)
	# i durant quantes iteracions ho estaran (valors de cada
	# diccionari)
    tabu = [{} for n in range(nVertexes)]
    i = 0
    while i < iteracions and objectiu(graf, estat) > 0:

        # Selecciona el millor vei de l'estat actual
        estat = vei(graf, estat, k, tabu, iterTabu)

        if objectiu(graf,estat)<objectiu(graf,millor):
            millor = estat[:]
        print i,objectiu(graf,estat), objectiu(graf,millor)

        # Actualitza els estats tabú (descompta una iteració)
        actualitzaTabu(tabu)

        # Avança a la següent iteració
        i += 1

    return millor

# Genera un graf en forma de matriu de connectivitat, amb un nombre de
# vèrtexes i una probabilitat de contacte entre dos vèrtexes. Torna la
# meitat inferior de la matriu com llista de llistes.
# Es pot fer servir per generar grafs alternatius a l'exemple donat.
def generaGraf(nVertexes, probContacte):
    resultat = []
    for i in range(nVertexes):
		# 1 si el número aleatori és menor o igual que la
		# probabilidat de contacte, 0 si no
        f = lambda : random()<=probContacte and 1 or 0
        resultat.append([f() for j in range(i)])

    return resultat


# Programa principal

# Exemple manual: graf que representa Sudamèrica
sudamerica = [[],
             [1],
             [0,1],
             [0,0,1],
             [0,0,0,1],
             [1,0,0,0,0],
             [1,1,1,1,1,0],
             [1,0,0,0,0,1,1],
             [0,0,0,0,0,0,1,1],
             [0,0,0,0,0,0,0,1,1],
             [0,0,0,0,0,0,1,0,1,0],
             [0,0,0,0,0,0,1,0,1,1,1],
             [0,0,0,0,0,0,1,0,0,0,0,1]]

# Generació d'un graf aleatori.
# Paràmetres del problema: nombre de països i probabilitat que dos
# països qualssevol siguin fronterers.
# Lògicament, com més països hi hagi, més contaces tindrà un país donat
nPaisos      = 13
probContacte = 0.05
mapa         = generaGraf(nPaisos,probContacte)

# Execució de l'algorisme: nombre màxim d'iteracions i nombre d'iteracions
# que roman un color com a tabú per un país donat
iteracions = 200
iterTabu    = 15

# Nombre de colors
k=4

# Es crea un estat inicial aleatòriament
estat = [randint(1,k) for i in range(nPaisos)]

# S'executa la cerca tabú amb k colors amb l'exemple de Sudamèrica. 
# Es pot executar amb el mapa generat canviant els paràmetres.
solucio = cercaTabu(sudamerica, estat, k, iteracions, iterTabu)
print('Solució:' + str(solucio))
print('Colisions=' + str(objectiu(sudamerica, solucio)))

