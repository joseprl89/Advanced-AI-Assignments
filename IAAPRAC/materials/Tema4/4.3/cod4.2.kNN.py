# parametres

k = 3

# declaracio de funcions

def deuclidea(x, y):
   return sum(map(lambda a, b: (float(a) - float(b)) ** 2,
                  x, y)) ** (1 / 2)

def comptar(l):
   p = {}
   for x in l:
      p.setdefault(x, 0)
      p[x] += 1
   return p
 
def classify(t):
   ds = list(map(deuclidea, train, [t for x in range(len(train))]))
   kcl = comptar([sorted([(ds[i], classesTrain[i])
                         for i in range(len(train))],
                        key=lambda x: x[0])[i][1]
                 for i in range(k)])
   return max([(x , kcl[x]) for x in kcl.keys()],
              key=lambda x: x[1])[0]

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

# Classificacio
prediccions = list(map(classify, test))   

# Nombre de correctes
print('Prec.:', len(list(filter(lambda x: x[0] == x[1],
                                zip(*[prediccions, classesTest]))))
                / len(test) * 100, '%')
