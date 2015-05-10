# declaracio de funcions

def bondat(classes, conjunt):
    p = {}
    for i in range(len(classes)):
        p.setdefault(conjunt[i], {})
        p[conjunt[i]].setdefault(classes[i], 0)
        p[conjunt[i]][classes[i]] += 1

    return sum([max([(val, p[atr][val])
                    for val in p[atr].keys()])[1]
               for atr in p.keys()])

def classeMF(classes):
    p = {}
    for x in classes:
        p.setdefault(x, 0)
        p[x] += 1
    return max([(p[cl], cl) for cl in p.keys()])[1]

def iteracio2(c):
    c.pop(1)
    return (c[0][0], iteracio(list(c[2]), list(zip(*c[1]))))

def iteracio(cl, cj):
    l = sorted(set(cl))
    if len(l)==1:
        return ("classe", l[0])
    else:
        (b, col) = max([(bondat(cl, cj[i]), i)
                      for i in range(len(cj))])
        l = cj.pop(col)
        lu = sorted(set(l))
        cj = list(zip(*cj))
        if len(cj) == 0:
            l = [list(filter(lambda x: x[0] == x[1], y))
                 for y in [[(val, l[i], cl[i])
                             for i in range(len(l))]
                             for val in lu]]
            return ("atr", col, [(lp[0][0],
                               ("classe", classeMF(list(list(zip(*lp))[2]))))
                              for lp in l])
        elif b == len(cl):
            l = [list(filter(lambda x: x[0] == x[1], y))
                   for y in [[(val, l[i], cl[i])
                                 for i in range(len(l))]
                                 for val in lu]]
            return ("atr", col, [(lp[0][0], ("classe",
                                    classeMF(list(list(zip(*lp))[2])))) for lp in l])
        else:   
            l = [list(filter(lambda x: x[0] == x[1], y))
                   for y in [[(val, l[i], list(cj[i]), cl[i])
                                 for i in range(len(l))]
                                 for val in lu]]
            return ('atr', col, [iteracio2(list(zip(*x)))
                                      for x in l])

def testEx(ex, arbre):
    if isinstance(arbre, tuple):
        if arbre[0] == "classe":
            return arbre[1]
        elif arbre[0] == "atr":
            valor = ex.pop(arbre[1])
            arbre = list(filter(lambda x: x[0][0] == x[1],
                        [(l, valor) for l in arbre[2]]))
            if len(arbre)==0:
                return None
            else:
                return testEx(ex, arbre[0][0][1])
        else:
            return None

    return None

def decisionTree(l, ratioToTest=3):    
    # construccio del training: 2 de cada 3 
    train = list(map(lambda x: x[1],
                     filter(lambda v: v[0] % ratioToTest != 0, enumerate(l))))
    
    classesTrain = list(map(lambda x: x.pop(0), train))
    
    # construccio del test: 1 de cada 3
    test = list(map(lambda x: x[1],
                    filter(lambda v: v[0] % ratioToTest == 0, enumerate(l))))
    classesTest = list(map(lambda x: x.pop(0), test))
    
    # Construccio de l'arbre
    arbre = iteracio(classesTrain, list(zip(*train)))
    # print(arbre)
    
    # Classificacio
    predictions = [testEx(ex, arbre) for ex in test]
    accuracy = len(list(filter(lambda x: x[0] == x[1],
                                    zip(*[predictions, classesTest])))) / len(test) * 100;
    
    return accuracy,predictions

# carrega de l'arxiu
#l = list(map(lambda l: (l.strip()).split(','),
#            open('../../materials/Tema4/4.4.1/mushroom.data.txt', 'r').readlines()))

#accuracy,predictions = decisionTree(l)

# Nombre de correctes
#print('Prec.:', accuracy, '%')
