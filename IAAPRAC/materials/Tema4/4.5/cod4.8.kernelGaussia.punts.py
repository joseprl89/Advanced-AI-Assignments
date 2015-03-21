from functools import reduce
from math import exp

# declaracio de kernel

def kernel(a, b, gamma=1):
   return exp(-gamma * sum(map(lambda x, y: (float(x) - float(y)) ** 2, a, b)))

# declaracio de funcions

def h(x, tp, tn, cp, cn, b):
   y = (sum([kernel(x, xi) for xi in tp]) / cp -
        sum([kernel(x, xi) for xi in tn]) / cn - b)
   if y > 0:
      return '+1'
   else:
      return '-1'

train = list(map(lambda l: (l.strip()).split(','),
             open('punts.txt', 'r').readlines()))

# Entrenament
tp = list(zip(*filter(lambda x: x[len(train[0])-1] == '+1', train)))
tp.pop(len(tp)-1)
tp = list(zip(*tp))
cp = len(tp)
tn = list(zip(*filter(lambda x: x[len(train[0])-1] == '-1', train)))
tn.pop(len(tn)-1)
tn = list(zip(*tn))
cn = len(tn)

b = (sum([sum([kernel(xi, xj) for xi in tp])
          for xj in tp]) / (cp ** 2) -
     sum([sum([kernel(xi, xj) for xi in tn])
          for xj in tn]) / (cn ** 2)) / 2

test = [['3','6']]
classesTest = ['-1']
prediccions = [h(x, tp, tn, cp, cn, b) for x in test] 

# Nombre de correctes
print('Prec.:', len(list(filter(lambda x: x[0] == x[1],
                                zip(*[prediccions, classesTest]))))
                / len(test) * 100, '%')
