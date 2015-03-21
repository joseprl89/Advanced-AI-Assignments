# -*- coding: utf-8 -*-
import random, sys, math, operator

# Calcula el temps mitjà d'esèra d'un conjunt de servidors
# i una distribució de clients
def tempsMitjaEspera(servidors, clients):
    temps = [t*(1+c) for (t,c) in zip(servidors, clients)]
    suma   = sum(map(operator.mul, temps,clients))
    return  suma / float(sum(clients))


# Genera un veí de l'estat actual: simplement mou un client
# d'un servidor a un altre a l'atzar
def generaVei(estat):
    nou = estat[:]
    fet = False
    while not fet:
        triats     = random.sample(range(len(estat)), 2)
        origen     = triats[0]
        destinacio = triats[1]

        # El nombre de clients en un servidor ha de ser >=0
        if nou[origen] > 0:
            nou[origen]  -= 1
            nou[destinacio] += 1
            fet           = True

    return nou

# Tenint en compte l'energia de cada estat, la iteració actual
# i el factor de tolerància, decideix si un nou estat s'accepta 
# o no
def accepta(energia, novaEnergia, iteracions, factor):
    if novaEnergia < energia:
        return True
    else:
        valor = math.exp((energia-novaEnergia)/
                         (iteracions*factor))
        return random.random() < valor

# Aplica l'algorisme de recocció simulada a un conjunt de servidors
# i una distribució de clients. La tolerància indica l'empitjorament
# acceptable a l'iniciar l'algorisme (aproximat).
def recoccioSimulada(servidors, clients, tolerancia, iteracions):

	# La tolerància permet ajustar la temperatura per controlar si
	# s'accepta o no un nou estat "pitjor" (amb temps de resposta més
	# gran)
    factor = tolerancia / float(iteracions)

    # Es calcula el temps mitjà d'espera de l'estat inicial
    estat = clients[:]
    temps = tempsMitjaEspera(servidors, estat)

	# S'emmagatzema el millor estat obtingut; serà aquell que es tornarà
    millor      = estat[:]
    millorTemps = temps
    for i in range(iteracions):
        nou       = generaVei(estat)
        nouTemps = tempsMitjaEspera(servidors, nou)

        if accepta(temps, nouTemps, i+1, factor):
            estat = nou
            temps = nouTemps

            if nouTemps < millorTemps:
                millor      = estat[:]
                millorTemps = temps

    return millor


# Paràmetres generals del problema
# La tolerància indica aproximadament el màxim empitjorament que
# s'accepta inicialment
numServidors = 50
numClients   = 400
maxTResposta = 10
tolerancia   = 1.0
iteracions   = 2000

# Generació d'un conjunt de servidors
servidors = [random.randint(1,maxTResposta)
                            for i in range(numServidors)]
print(servidors)

# Inicialment els clients es distribueixen per igual entre tots els
# servidors; si en sobra cap, s'assigna a l'atzar
clients = [numClients/numServidors
                            for i in range(numServidors)]

resta = numClients - sum(clients)
if resta>0:
    for serv in random.sample(range(numServidors), resta):
        clients[serv] += 1

print(clients, tempsMitjaEspera(servidors, clients))

# Es crida a recocció simulada per que obtingui una bona
# distribució dels clients als servidors
clients = recoccioSimulada(servidors, clients, tolerancia,
                                                   iteracions)

print(clients, tempsMitjaEspera(servidors, clients))
