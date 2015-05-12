from math import exp
from svmutil import svm_predict, svm_train
from builtins import range

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


def svm(l, kernel, ratioToTest=3):
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
    
    # Get only unique classes
    seen = set()
    seen_add = seen.add
    classesTrain = list(map(lambda x: x.pop(0), train))
    classesTest = list(map(lambda x: x.pop(0), test))
    
    # Merge array and get only the uniques
    classes = classesTrain + classesTest
    uniqueClasses = [ x for x in classes if not (x in seen or seen_add(x))]
    
    # start with accuracy 1
    resultsPerClass = {}
    for c in uniqueClasses:
        trainData = []
        testData = []
        
        # Copy the array and set the class to +1 if it equals the class we try to detect.
        for i, row in enumerate(train):
            if l[i][0] == c:
                c2 = 1
            else:
                c2 = -1
            
            copyRow = row[:]
            copyRow[0] = c2
            trainData.append(copyRow)

        y=list(map(lambda x: int(x.pop(0)), trainData))
    
        x = [dict([(i+1,kernel(trainData[i], trainData[j]))
               for i in range(len(trainData))])
             for j in range(len(trainData))]
    
        list(map(lambda l, i: l.update({0:i+1}), x, range(len(x))))
    
        model = svm_train(y, x, '-s 0 -t 4 -q')
        
        # svm_save_model('model.km.txt', model)
        
        # Copy the test array and set the class to +1 if it equals the class we try to detect.
        for i, row in enumerate(test):
            if l[i][0] == c:
                c2 = 1
            else:
                c2 = -1
                
            testData.append([ value for value in row ])
            testData[i][0] = c2

        yt=list(map(lambda x: int(x.pop(0)), testData))
        
        xt = [dict([(i+1,kernel(testData[j], trainData[i]))
                   for i in range(len(trainData))])
             for j in range(len(testData))]
        list(map(lambda l, i: l.update({0:-1}), xt, range(len(xt))))
        
        p_label, p_acc, p_val = svm_predict(yt, xt, model, '-q') # Quiet mode to avoid polluting the output
        
        # Store the results per the given class
        resultsPerClass[c] = p_val
    
    print(uniqueClasses)
    
    print (resultsPerClass)
    
    # Remove the array with a single element.
    for key in resultsPerClass:
        resultsPerClass[key] = [x[0] for x in resultsPerClass[key]]

    print (resultsPerClass)
    
    predictions = [None] * len(testData)
    for clazz, resultsArray in resultsPerClass.items():
        for i,value in enumerate(resultsArray):
            if value > 0:
                if predictions[i] == None:
                    predictions[i] = clazz
                    continue

                if value > resultsPerClass[predictions[i]][i]:
                    predictions[i] = clazz;
    
    classesTest = list(map(lambda x: x.pop(0), test))
    accuracy = len(list(filter(lambda x: x[0] == x[1],
                               zip(*[predictions, classesTest])))) / len(test) * 100;

    return accuracy, predictions

# Load file
l = list(map(lambda l: (l.strip()).split(','),
        open('../data/Wholesale customers.csv', 'r').readlines()))

for row in l:
    row[1] = row[0] + '' + row[1]

l = [row[1:] for row in l ]

l = l[1:]

print("SVM: ", svm(l, kernelRBF, ratioToTest=4))