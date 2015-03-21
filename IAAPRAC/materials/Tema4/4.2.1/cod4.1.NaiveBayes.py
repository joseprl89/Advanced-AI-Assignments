from functools import reduce

# declaracio de funcions
def comptar(l):
   p = {}
   for x in l:
      p.setdefault(x, 0)
      p[x] += 1
   return p
   
def comptar2(l, k):
   p = {}
   for i in range(len(l)):
      p.setdefault(k[i], {})
      p[k[i]].setdefault(l[i], 0)
      p[k[i]][l[i]] += 1
   return p

def Pxik(atr, N, k):
   if atr in N[k]:
      return N[k][atr] / Nk[k]
   else:
      return Nk[k] / n ** 2

def classify(t):
   l = [(k , Nk[k] / n *
        reduce(lambda x, y: x * y,
               map(Pxik, t, Nxik,
                   [k for a in range(len(t))])))
        for k in Nk.keys()]
   return max(l, key=lambda x: x[1])[0]

# carrega de l'arxiu
l = list(map(lambda l: (l.strip()).split(','),
             open('mushroom.data.txt', 'r').readlines()))

# construccio del training: 2 de cada 3 
train = list(map(lambda x: x[1],
                 filter(lambda v: v[0] % 3 != 0, enumerate(l))))
n = len(train)

# construccio del test: 1 de cada 3
test = list(map(lambda x: x[1],
                filter(lambda v: v[0] % 3 == 0, enumerate(l))))

# transposta del training
m = list(zip(*train))

# Numerador de P(k)
Nk = comptar(m[0])

# Numerador de P(xi|k)
Nxik = [comptar2(m[1], m[0]) for i in range(1, len(m))]

# Classificacio
classes = list(map(lambda x: x.pop(0), test))
prediccions = list(map(classify, test))   

# Nombre de correctes
print('Prec.:', len(list(filter(lambda x: x[0] == x[1],
                                zip(*[prediccions, classes]))))
                / len(test) * 100, '%')
