from numpy import *
import nmf

# Matriz de datos aleatoria (100 textos x 10 palabras):
A = random.randint(0,100,(100,10))

#descomposición NMF utilizando 3 características:
W,F = nmf.factorize(A,pc=3,iter=500)

print(W)
print(F)

# Residuo de la aproximación:
R = A - dot(W,F)

# máximo error relativo de reconstruccion (%):
R_rel = 100*R/A
print(R_rel.max())
