from functools import reduce

# declaracio de funcions

def deuclidea(x, y):
   return sum(map(lambda a, b: (float(a) - float(b)) ** 2,
                  x[1], y)) ** (1 / 2)

def comptar(l):
   p = {}
   for x in l:
      p.setdefault(x, 0)
      p[x] += 1
   return p
 
def classify(t):
   ds = list(map(deuclidea, centroides,
                 [t for x in range(len(centroides))]))
   return min([(ds[i], centroides[i][0])
               for i in range(len(centroides))],
              key=lambda x: x[0])[1]

def calcularCentroides(classe):
   filt = list(filter(lambda x: x[0] == x[1],
                    [(classesTrain[i], classe, train[i])
                     for i in range(len(train))]))
   transp = list(zip(*[filt[i][2] for i in range(len(filt))]))
   return (classe,
           list(map(lambda l: reduce(lambda a, b:
                                     float(a) + float(b),
                                     l) / classes[classe], transp)))

# carrega de l'arxiu
l = list(map(lambda l: (l.strip()).split(','),
             open('iris.data.txt', 'r').readlines()))

# construccio del training: 2 de cada 3 
train = list(map(lambda x: x[1],
                 filter(lambda v: v[0] % 3 != 0, enumerate(l))))
nc = len(train[0])
classesTrain = list(map(lambda x: x.pop(nc - 1), train))

# construccio del test: 1 de cada 3
test = list(map(lambda x: x[1],
                filter(lambda v: v[0] % 3 == 0, enumerate(l))))
classesTest = list(map(lambda x: x.pop(nc - 1), test))

# Entrenament
classes = comptar(classesTrain)
centroides = [calcularCentroides(c) for c in classes.keys()]

# Classificacio
prediccions = list(map(classify, test))   

# Nombre de correctes
print('Prec.:', len(list(filter(lambda x: x[0] == x[1],
                                zip(*[prediccions, classesTest]))))
                / len(test) * 100, '%')
