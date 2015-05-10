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
 
def classify(t, train, classesTrain):
    otherArray = [t for _ in range(len(train))]
    ds = list(map(deuclidea, train, otherArray ))
    kcl = comptar([sorted([(ds[i], classesTrain[i])
                         for i in range(len(train))],
                        key=lambda x: x[0])[i][1] for i in range(k)])
    return max([(x , kcl[x]) for x in kcl.keys()],
              key=lambda x: x[1])[0]
              
def kNN(l, ratioToTest=3):
    train = list(map(lambda x: x[1],
                     filter(lambda v: v[0] % ratioToTest != 0, enumerate(l))))
    nc = len(train[0])
    classesTrain = list(map(lambda x: x.pop(0), train))
    
    test = list(map(lambda x: x[1],
                    filter(lambda v: v[0] % ratioToTest == 0, enumerate(l))))
    classesTest = list(map(lambda x: x.pop(0), test))
    
    # Classificacio
    predictions = list([classify(t, train, classesTrain) for t in test])
    accuracy = len(list(filter(lambda x: x[0] == x[1],
                                zip(*[predictions, classesTest])))) / len(test) * 100;
    return accuracy, predictions;   

# carrega de l'arxiu
#l = list(map(lambda l: (l.strip()).split(','),
#             open('../../materials/Tema4/4.3/iris.data.txt', 'r').readlines()))

#accuracy, predictions = kNN(l,3);

# Nombre de correctes
#print('Prec.:', accuracy, '%')


