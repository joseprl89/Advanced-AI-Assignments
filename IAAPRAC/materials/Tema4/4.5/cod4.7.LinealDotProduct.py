from functools import reduce

# declaracio de funcions

def prodEscalar(a, b):
   return sum(a[i]*b[i] for i in range(len(a)))

def h(t, w, b):
   y = prodEscalar(w, t) - b
   if y > 0:
      return +1
   else:
      return -1

# carrega de l'arxiu
l = list(map(lambda l: (l.strip()).split(','),
             open('iris.data.txt', 'r').readlines()))

# construccio del training: 2 de cada 3 
train = list(map(lambda x: x[1],
                 filter(lambda v: v[0] % 3 != 0, enumerate(l))))

# construccio del test: 1 de cada 3
test = list(map(lambda x: x[1],
                filter(lambda v: v[0] % 3 == 0, enumerate(l))))
classesTest = list(map(lambda x: int(x.pop(len(x)-1)), test))

# Entrenament
tp = list(zip(*filter(lambda x: x[len(train[0])-1] == '+1', train)))
tp.pop(len(tp)-1)
tn = list(zip(*filter(lambda x: x[len(train[0])-1] == '-1', train)))
tn.pop(len(tn)-1)
p = list(map(lambda l: reduce(lambda x, y: float(x)+float(y), l) / len(l), tp))
n = list(map(lambda l: reduce(lambda x, y: float(x)+float(y), l) / len(l), tn))
w = list(map(lambda a, b: a - b, p, n))
b = (prodEscalar(p, p) - prodEscalar(n, n)) / 2
prediccions = [h(list(map(lambda x: float(x), t)), w, b) for t in test] 

# Nombre de correctes
print('Prec.:', len(list(filter(lambda x: x[0] == x[1],
                                zip(*[prediccions, classesTest]))))
                / len(test) * 100, '%')
