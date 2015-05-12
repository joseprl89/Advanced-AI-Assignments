from math import exp
from svmutil import svm_predict, svm_train
from builtins import range

kernelTypeLinear = 0
kernelTypePolynomial = 1
kernelTypeRBF = 2
kernelTypeSigmoid = 3
kernelTypePrecomputed = 4

# Kernel Radial Base Function
def kernelRBF(a, b, gamma=1):
    a = [v.split(':')[0] for v in a]
    b = [v.split(':')[0] for v in b]
    
    return exp(-gamma * sum(map(
      lambda x, y: (float(x) - float(y)) ** 2, a, b)))

def kernelSet(a, b):
    da = dict((k,v) for k, v in (l.split(':') for l in a))
    db = dict((k,v) for k, v in (l.split(':') for l in b))
    
    summ = 0
    for key in da.keys():
        if key in db:
            summ = summ + min(float(da[key]),float(db[key])) 
    return 2 ** summ;

def kernelSetRBF(a, b, gamma=1):
    return exp(-gamma * (kernelSet(a, a) - 2 *
                        kernelSet(a, b) + kernelSet(b, b)))

def kernelSVM(a, b):
    da = dict((k,v) for k, v in (l.split(':') for l in a))
    db = dict((k,v) for k, v in (l.split(':') for l in b))
    return 2 ** sum(float(da[key]) * float(db[key])
                   for key in da.keys() if key in db)


def svm(l, kernel, ratioToTest=3, kernelType=4):
    # Normalize data. All the data must be in the 0..1 range.
    maxRow = [float(v) for v in l[0]]
    for i in range(1, len(l)):
        for j in range(len(maxRow)):
            if (float(maxRow[j]) < float(l[i][j])):
                maxRow[j] =  float(l[i][j])
    
    for i in range(len(l)):
        for j in range(1,len(maxRow)):
            l[i][j] = float(l[i][j]) / maxRow[j]  
    
    # Convert the format to the correct one
    for i, row in enumerate(l):
        c = l[i][0];
        l[i] = [ str(j) + ':' + str(value) for j,value in enumerate(row) ]
        l[i][0] = c
    
    # construccio del training: radioToTest - 1 de cada ratioToTest 
    train = list(map(lambda x: x[1],
                     filter(lambda v: v[0] % ratioToTest != 0, enumerate(l))))
    
    # construccio del test: 1 de cada ratioToTest
    test = list(map(lambda x: x[1],
                    filter(lambda v: v[0] % ratioToTest == 0, enumerate(l))))


    y=list(map(lambda x: int(x.pop(0)), train))

    x = [dict([(i+1,kernel(train[i], train[j]))
           for i in range(len(train))])
         for j in range(len(train))]

    list(map(lambda l, i: l.update({0:i+1}), x, range(len(x))))

    model = svm_train(y, x, '-s 0 -t ' + str(kernelType) + ' -q')
    
    yt=list(map(lambda x: int(x.pop(0)), test))
    
    xt = [dict([(i+1,kernel(test[j], train[i]))
               for i in range(len(train))])
         for j in range(len(test))]
    list(map(lambda l, i: l.update({0:-1}), xt, range(len(xt))))
    
    p_label, p_acc, p_val = svm_predict(yt, xt, model, '-q') # Quiet mode to avoid polluting the output
    
    # Store the results per the given class
    return p_acc[0], p_label
