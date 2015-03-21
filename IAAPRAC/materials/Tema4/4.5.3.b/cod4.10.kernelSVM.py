from functools import reduce
from math import exp
from time import clock

# declaracio de kernel

def kernelSVM(a, b):
   la = [(int(k),int(v)) for k, v in (l.split(':') for l in a)]
   lb = [(int(k),int(v)) for k, v in (l.split(':') for l in b)]
   s = 0
   i = 0
   j = 0
   while (i < len(la)) and (j < len(lb)):
      if la[i][0] == lb[j][0]:
         s += la[i][1] * lb[j][1]
         i += 1
         j += 1
      elif la[i][0] < lb[j][0]:
         i += 1
      else:
         j +=1
   return s

def kernelSVMRBF(a, b, gamma=1):
   return exp(-gamma * (kernelSVM(a, a) - 2 *
                        kernelSVM(a, b) + kernelSVM(b, b)))

kernel = kernelSVMRBF

# declaracio de funcions

def h(x, tp, tn, cp, cn, b):
   y = (sum([kernel(x, xi) for xi in tp]) / cp -
        sum([kernel(x, xi) for xi in tn]) / cn - b)
   if y > 0:
      return '+1'
   else:
      return '-1'

# carrega de l'arxiu
data = list(map(lambda l: (l.strip()).split(' '),
                 filter(lambda x: x[0] != '#',
                        open('vectors.dat', 'r').readlines())))

# construccio del train: 2 de cada 3
train = list(map(lambda x: x[1],
                filter(lambda v: v[0] % 3 != 0, enumerate(data))))

# construccio del test: 1 de cada 3
test = list(map(lambda x: x[1],
                filter(lambda v: v[0] % 3 == 0, enumerate(data))))
classesTest = list(map(lambda x: x.pop(0), test))

del(data)

# Entrenament
tp = list(filter(lambda x: x[0] == '+1', train))
l=list(map(lambda x: x.pop(0), tp))
del(l)
cp = len(tp)

tn = list(filter(lambda x: x[0] == '-1', train))
l=list(map(lambda x: x.pop(0), tn))
del(l)
cn = len(tn)

del(train)

inici = clock()
b = (sum([sum([kernel(xi, xj) for xi in tp])
          for xj in tp]) / float(cp ** 2) -
     sum([sum([kernel(xi, xj) for xi in tn])
          for xj in tn]) / float(cn ** 2)) / 2.0
print("b", b, clock() - inici, "s")

inici = clock()
prediccions = [h(x, tp, tn, cp, cn, b) for x in test] 
print("h", clock() - inici, "s")

# Nombre de correctes
print('Prec.:', len(list(filter(lambda x: x[0] == x[1],
                                zip(*[prediccions, classesTest]))))
                / len(test) * 100, '%')

