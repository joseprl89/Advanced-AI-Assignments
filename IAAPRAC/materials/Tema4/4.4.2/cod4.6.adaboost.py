from itertools import repeat
from math import log
from math import exp

# parametres
T = 50

# declaracio de funcions

def hti(atvl, val, igual):
   if (igual and (val == atvl)) or (not igual and (val != atvl)):
      pred = +1
   else:
      pred = -1
   return pred

def error(Dt, cl, atvl, val, igual):
   s = 0
   for i in range(len(cl)):
      if hti(atvl[i], val, igual) != int(cl[i]):
         s += Dt[i]
   return s

def WeakLearner(Dt, tr):
   ll = []
   for atr in range(len(tr)-1):
      for val in sorted(set(tr[atr+1])):
         et = error(Dt, tr[0], tr[atr+1], val, True)
         ll.append([et, atr+1, val, True])
         et = error(Dt, tr[0], tr[atr+1], val, False)
         ll.append([et, atr+1, val, False])
   return min(ll)

def testEx(ex, model):
   return sum([regla[0] * hti(ex[regla[2]], regla[3], regla[4])
               for regla in model])

# carrega de l'arxiu
l = list(map(lambda l: (l.strip()).split(','),
             open('mushroom.adaboost.txt', 'r').readlines()))

# construccio del training: 2 de cada 3 
train = list(map(lambda x: x[1],
                 filter(lambda v: v[0] % 3 != 0, enumerate(l))))

# construccio del test: 1 de cada 3
test = list(map(lambda x: x[1],
                filter(lambda v: v[0] % 3 == 0, enumerate(l))))

# Entrenament
tt = list(zip(*train))
m = len(train)
Dt = list(repeat(1/m, m))
model = []
for i in range(T):
   [et, atr, val, igual] = WeakLearner(Dt, tt)
   if et > 0.5:
      print("Error: et out of range!")
      break
   if et == 0:
      print("Ja esta tot ben classificat!")
      break
   alfat = 1 / 2 * log((1 - et) / et)
   Dt2 = [Dt[j] * exp(-alfat * hti(tt[atr][j], val, igual) *
                      float(train[j][0]))
          for j in range(m)]
   s = sum(Dt2)
   Dt = [Dt2[j]/s for j in range(m)]
   model.append((alfat, et, atr, val, igual))
print(len(model), "reglas apreses!")
  
# Classificacio
prediccions = [testEx(ex, model) for ex in test]

# Nombre de correctes
print('Prec.:', len(list(filter(
   lambda x: x[0] * float(x[1][0]) > 0,
   zip(*[prediccions, test]))))
      / len(test) * 100, '%')
