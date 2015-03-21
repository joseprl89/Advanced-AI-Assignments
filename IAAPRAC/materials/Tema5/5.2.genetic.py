# -*- coding: utf-8 -*-
from random import random, randint, sample
from collections import namedtuple

# Calcula el capital invertit per un individu
def capitalInvertit(individu):
    return sum(map(lambda x,y: x*y.preu,individu,inversions))

# Calcula el rendiment obtingut per un individu
def rendiment(individu):
    return sum(map(lambda x,y: x*y.preu*y.rendim,
                               individu, inversions))

# Si un individu gasta més capital del disponible, s'eliminen
# aleatòriament inversions fins que s'ajusta al capital
def ajustaCapital(individu):
    ajustat = individu[:]
    while capitalInvertit(ajustat)>capital:
        pos = randint(0,len(ajustat)-1)
        if ajustat[pos] > 0:
            ajustat[pos] -= 1

    return ajustat
    
# Crea un individu a l'atzar, en aquest cas una selecció d'inversions
# que no excedeixin el capital disponible
def creaIndividu(inversions, capital):
    individu = [0]*len(inversions)

    while capitalInvertit(individu) < capital:
        eleccio = randint(0,len(inversions)-1)
        individu[eleccio] += 1

    return ajustaCapital(individu)

# Crea un nou individu creuant altres dos (les posicions dels quals
# s'indiquen al segon paràmetre)
def creua(poblacio, posicions):
    L = len(poblacio[0])

	# Pren els gens del primer progenitor i després pren a l'atzar
	# un segment d'entre 1 i L gens del segon progenitor
    fill   = poblacio[posicions[0]][:]
    inici  = randint(0,L-1)
    final  = randint(inici+1,L)
    fill[inici:final] = poblacio[posicions[1]][inici:final]

    return ajustaCapital(fill)

# Aplica mutacions a un individu segons una taxa donada; garantitza
# que compleix les restriccions de capital i inversions
def muta(individu, taxaMutacio):
    mutat = []
    for i in range(len(individu)):
        if random() > taxaMutacio:
            mutat.append(individu[i])
        else:
            mutat.append(randint(0,inversions[i].quantitat))

    return ajustaCapital(mutat)

# Fa evolucionar el sistema durant un nombre de generacions
def evoluciona(poblacio, generacions):

    # Ordena la població inicial per rendiment produït
    poblacio.sort(key=lambda x:rendiment(x))    

    # Alguns valors útils
    N           = len(poblacio)
    taxaMutacio = 0.01
    
    # Genera una llista del tipus [0,1,1,2,2,2,3,3,3,3,...] per 
    # representar les probabilitats de reproduir-se de cada
    # individu (el primer 1 possibilitat, el segon 2, etc.)
    reproduccio = [x for x in range(N) for y in range(x+1)]

    for i in range(generacions):
		# Es generen N-1 nous individus creuant els existents
        fills = [creua(poblacio,sample(reproduccio,2)) for x in range(N-1)]

        # S'apliquen mutacions amb una certa probabilitat
        fills = [muta(x, taxaMutacio) for x in fills]

		# S'afegeix el millor individu de la població anterior
		# (elitisme)
        fills.append(poblacio[-1])
        poblacio = fills

        # S'ordenen els individus per rendiment
        poblacio.sort(key=lambda x:rendiment(x))
            

    # Torna el millor individu trobat
    return poblacio[-1]


# Declara una tupla amb noms per representar cada inversió
Inversio = namedtuple('Inversio', 'preu quantitat rendim')

numInver  = 100
maxPreu   = 1000
maxCant   = 10
maxRend   = 0.2


# Genera una llista de tuples Inversio
inversions=[Inversio(random()*maxPreu, randint(1,maxCant),
                     random()*maxRend) for i in range(numInver)]
print (inversions)

capital      = 50000
individus    = 20
generacions  = 1000

poblacio = [creaIndividu(inversions,capital)
                                     for i in range(individus)]

# Nota: per simplificar el programa s'accedeix a inversions i capital
# de forma global (només es llegeixen, no es modifiquen)

millor = evoluciona(poblacio, generacions)
print(millor, capitalInvertit(millor), rendiment(millor))
