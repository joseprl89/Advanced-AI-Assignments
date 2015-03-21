# -*- coding: utf-8 -*-
from random import random

# Funció que es vol minimitzar
def funcio(x, y):
    sum1 = x**2 * (4-2.1*x**2 + x**4/3.0)
    sum2 = x*y
    sum3 = y**2 * (-4+4*y**2)
    return sum1 + sum2 + sum3


# Torna un número aleatori dintre del rang amb distribució uniforme
# (proporcionada per random)
def aleatori(inf, sup):
    return random()*(sup-inf) + inf

# Classe que representa una partícula individual i que facilita les
# operacions necessàries
class Particula:
	# Alguns atributs de classe (comuns a totes les partícules)
	# Paràmetres per actualitzar la velocitat
    inercia     = 1.4
    cognitiva   = 2.0
    social      = 2.0
    # Límits de l'espai de solucions
    infx = -2.0
    supx =  2.0
    infy = -1.0
    supy =  1.0
    # Factor d'ajust de la velocitat inicial
    ajustV = 100.0
        
    # Crea una partícula dins dels límits indicats
    def __init__(self):
        self.x  = aleatori(Particula.infx, Particula.supx)
        self.y  = aleatori(Particula.infy, Particula.supy)
        self.vx = aleatori(Particula.infx/Particula.ajustV,
                           Particula.supx/Particula.ajustV)
        self.vy = aleatori(Particula.infy/Particula.ajustV,
                           Particula.supy/Particula.ajustV)
        self.xLoc     = self.x
        self.yLoc     = self.y
        self.valorLoc = funcio(self.x, self.y)

    # Actualitza la velocitat de la partícula
    def actualitzaVelocitat(self, xGlob, yGlob):
        cogX    = Particula.cognitiva*random()*(self.xLoc-self.x)
        socX    = Particula.social*random()*(xGlob-self.x)
        self.vx = Particula.inercia*self.vx + cogX + socX
        cogY    = Particula.cognitiva*random()*(self.yLoc-self.y)
        socY    = Particula.social*random()*(yGlob-self.x)
        self.vy = Particula.inercia*self.vy + cogY + socY

    # Actualitza la posició de la partícula
    def actualitzaPosicio(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy

		# S'ha de mantenir dins de l'espai de solucions
        self.x = max(self.x, Particula.infx)
        self.x = min(self.x, Particula.supx)
        self.y = max(self.y, Particula.infy)
        self.y = min(self.y, Particula.supy)

        # Si és inferior a la millor, l'adopta com la millor
        valor = funcio(self.x, self.y)
        if valor < self.valorLoc:
            self.xLoc     = self.x
            self.yLoc     = self.y
            self.valorLoc = valor

# Mou un eixam de partícules durant les iteracions indicades.
# Torna les coordenades i el valor del mínim obtingut.    
def eixamParticules(particules, iteracions, reduccioInercia):

    # Registra la millor posició global i el seu valor
    millorParticula = min(particules, key=lambda p:p.valorLoc)
    xGlob     = millorParticula.xLoc
    yGlob     = millorParticula.yLoc
    valorGlob = millorParticula.valorLoc

    # Bucle principal de simulació
    for iter in range(iteracions):
        # Actualitza la velocitat i posició de cada partícula
        for p in particules:
            p.actualitzaVelocitat(xGlob, yGlob)
            p.actualitzaPosicio()

		# Fins que no s'han mogut totes les partícules no s'actualitza
		# el mínim global, per simular que totes es mouen a l'hora
        millorParticula = min(particules, key=lambda p:p.valorLoc)
        if millorParticula.valorLoc < valorGlob:
            xGlob     = millorParticula.xLoc
            yGlob     = millorParticula.yLoc
            valorGlob = millorParticula.valorLoc

        # Finalment es redueix la inèrcia de les partícules
        Particula.inercia*=reduccioInercia

    return (xGlob, yGlob, valorGlob)


# Paràmetres del problema
nParticules = 10
iteracions = 100
redInercia  = 0.9

# Genera un conjunt inicial de partícules
particules=[Particula() for i in range(nParticules)]

# Executa l'algorisme de l'eixam de partícules
print(eixamParticules(particules, iteracions, redInercia))
