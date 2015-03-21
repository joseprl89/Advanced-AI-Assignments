from functools import reduce
from math import exp
from time import clock

# declaracio de kernel

def kernelRBF(a, b, gamma=1):
   return exp(-gamma * sum(map(
      lambda x, y: (float(x) - float(y)) ** 2, a, b)))

def kernelSet(a, b):
   da = dict((k,v) for k, v in (l.split(':') for l in a))
   db = dict((k,v) for k, v in (l.split(':') for l in b))
   return 2 ** sum(min(float(da[key]),float(db[key]))
                   for key in da.keys() if key in db)

def kernelSetRBF(a, b, gamma=1):
   return exp(-gamma * (kernelSet(a, a) - 2 *
                        kernelSet(a, b) + kernelSet(b, b)))

def kernelSVM(a, b):
   da = dict((k,v) for k, v in (l.split(':') for l in a))
   db = dict((k,v) for k, v in (l.split(':') for l in b))
   return 2 ** sum(float(da[key]) * float(db[key])
                   for key in da.keys() if key in db)

kernel = kernelSVM

# declaracio de funcions

def h(x, tp, tn, cp, cn, b):
   y = (sum([kernel(x, xi) for xi in tp]) / cp -
        sum([kernel(x, xi) for xi in tn]) / cn - b)
   if y > 0:
      return '+1'
   else:
      return '-1'

# carrega de l'arxiu
train = list(map(lambda l: (l.strip()).split(' '),
                 filter(lambda x: x[0] != '#',
                        open('train.dat', 'r').readlines())))

# Entrenament
tp = list(filter(lambda x: x[0] == '1', train))
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
          for xj in tp]) / (cp ** 2) -
     sum([sum([kernel(xi, xj) for xi in tn])
          for xj in tn]) / (cn ** 2)) / 2
print("b", b, clock() - inici, "s")

test = list(map(lambda l: (l.strip()).split(' '),
                filter(lambda x: x[0] != '#',
                       open('test.dat', 'r').readlines())))
classesTest=list(map(lambda x: x.pop(0), test))

inici = clock()
prediccions = [h(x, tp, tn, cp, cn, b) for x in test] 
print("h", clock() - inici, "s")

# Nombre de correctes
print('Prec.:', len(list(filter(lambda x: x[0] == x[1],
                                zip(*[prediccions, classesTest]))))
                / len(test) * 100, '%')
