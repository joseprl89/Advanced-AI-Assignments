from functools import reduce

# As we are using global variables, prepend with two underlines 
# to avoid potential issues with variables with the same name
__Nk = [];
__n = 0;
__Nxik = [];

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
        return N[k][atr] / __Nk[k]
    else:
        return __Nk[k] / __n ** 2

def classify(t):
    l = [(k , __Nk[k] / __n *
        reduce(lambda x, y: x * y,
               map(Pxik, t, __Nxik,
                   [k for _ in range(len(t))])))
        for k in __Nk.keys()]
    return max(l, key=lambda x: x[1])[0]

def naiveBayes(l, ratioTests=3):
    global __n,__Nk,__Nxik;    
    
    # construccio del training: 2 de cada 3 
    train = list(map(lambda x: x[1],
                     filter(lambda v: v[0] % ratioTests != 0, enumerate(l))))
    __n = len(train)
    
    # construccio del test: 1 de cada 3
    test = list(map(lambda x: x[1],
                    filter(lambda v: v[0] % ratioTests == 0, enumerate(l))))
    
    # transposta del training
    m = list(zip(*train))
    
    # Numerador de P(k)
    __Nk = comptar(m[0])
    
    # Numerador de P(xi|k)
    __Nxik = [ comptar2 (m[ i ] , m[ 0 ] ) for i in range (1 , len (m) ) ]
    
    # Classificacio
    classes = list(map(lambda x: x.pop(0), test))
    predictions = list(map(classify, test))   
    
    accuracy =  len(list(filter(lambda x: x[0] == x[1],
                                zip(*[predictions, classes])))) / len(test) * 100;
                                
    return accuracy, predictions;

# Load file
# l = list(map(lambda l: (l.strip()).split(','),
#             open('../../materials/Tema4/4.2.1/mushroom.data.txt', 'r').readlines()))

# accuracy, predictions = naiveBayes(l)

# Print accuracy and predictions
# print('Prec.:', accuracy , '%')
# print('Predictions.:', predictions)
