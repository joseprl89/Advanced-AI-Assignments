from functools import reduce
from random import randrange
from itertools import repeat

# parametros

k = 3
maxit = 10

# declaracion de funciones

def deuclidea(x, y):
   return sum(map(lambda a, b: (float(a) - float(b)) ** 2,
                  x, y)) ** 0.5

def contar(l):
   p = {}
   for x in l:
      p.setdefault(x, 0)
      p[x] += 1
   return p
 
def classify(t):
   ds = [deuclidea(centroides[i][1], t)
         for i in range(len(centroides))]
   return min([(ds[i], centroides[i][0])
               for i in range(len(centroides))],
              key=lambda x: x[0])[1]

def nextCentr(l):
   if (l == []):
      return None
   else:
      if len(l)==1:
         return l[0][2]
      else:
         tot2 = list(zip(*[x[2] for x in l]))
         num = len(tot2[0])
         return list(map(lambda l: reduce(lambda a, b:
                                       float(a) + float(b), l)
                      / num, list(tot2)))         
   
def kmeans(clase, k, maxit):
   filt = list(filter(lambda x: x[0] == x[1],
                    [(clasesTrain[i], clase, train[i])
                     for i in range(len(train))]))
   conj = [filt[i][2] for i in range(len(filt))]
   centr = [conj[randrange(len(conj))] for i in range(k)]
   anteriores = None
   for it in range(maxit):
      cercanos = [min(zip(*[list(map(deuclidea,
                                     repeat(ej, k),
                                     centr)), range(k)]))[1]
                  for ej in conj]
      centr2 = [nextCentr(list(filter(
         lambda x: x[0] == x[1],
         zip(*[list(repeat(c, len(conj))),
               cercanos, conj]))))
                for c in range(k)]
      if None in centr2: break
      if cercanos == anteriores: break
      anteriores = cercanos

   return [(clase, x) for x in filter(lambda x: x!=None, centr2)]

# carga del archivo
l = list(map(lambda l: (l.strip()).split(','),
             open('iris.data.txt', 'r').readlines()))

# construccion del training: 2 de cada 3 
train = list(map(lambda x: x[1],
                 filter(lambda v: v[0] % 3 != 0, enumerate(l))))
nc = len(train[0])
clasesTrain = list(map(lambda x: x.pop(nc - 1), train))

# construccion del test: 1 de cada 3
test = list(map(lambda x: x[1],
                filter(lambda v: v[0] % 3 == 0, enumerate(l))))
clasesTest = list(map(lambda x: x.pop(nc - 1), test))

# Entrenamiento
clases = contar(clasesTrain)
centroides = reduce(lambda x, y: x + y,
                    [kmeans(c, k, maxit) for c in clases.keys()])

# Clasificacion
predicciones = list(map(classify, test))   

# Numero de correctos
print('Prec.:',
      len(list(filter(lambda x: x[0] == x[1],
                      zip(*[predicciones, clasesTest]))))
      / len(test) * 100, '%')
