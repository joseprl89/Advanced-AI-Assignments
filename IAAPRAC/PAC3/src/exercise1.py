from PAC3.src.NaiveBayes import naiveBayes;
from PAC3.src.DecisionTree import decisionTree;
from PAC3.src.KNN import kNN;

def readData():
    # Load file
    l = list(map(lambda l: (l.strip()).split(','),
            open('../data/Wholesale customers.csv', 'r').readlines()))
    
    for row in l:
        row[1] = row[0] + '' + row[1]
    
    l = [row[1:] for row in l ]
    
    l = l[1:]
    return l;
    
    
print("RatioToTest, Naive bayes accuracy, Decision tree accuracy, kNNTreeAccuracy")
for ratioToTest in range(2,20):
    ######## Naive bayes 

    naiveBayesAccuracy, naiveBayesPredictions = naiveBayes(readData(), ratioTests=ratioToTest)
    
    # Print accuracy and predictions
    # print('naiveBayesAccuracy. :', naiveBayesAccuracy , '%')
    # print('naiveBayesPredictions:', naiveBayesPredictions)
    
    ######## Decision tree
    
    decisionTreeAccuracy,decisionTreePredictions = decisionTree(readData(),ratioToTest=ratioToTest)
    
    # Print accuracy and predictions
    #print('decisionTreeAccuracy:', decisionTreeAccuracy, '%')
    #print('decisionTreePredictions:', decisionTreePredictions)
    
    ######## kNN
    
    kNNAccuracy,kNNPredictions = kNN(readData(),ratioToTest=ratioToTest);
    
    # Print accuracy and predictions
    #print('kNNTreeAccuracy:', kNNAccuracy, '%')
    #print('kNNPredictions:', kNNPredictions)
    
    ######## Support vector machine Kernel 1
    
    
    ######## Support vector machine Kernel 2
    
    print(ratioToTest,",",naiveBayesAccuracy,",",decisionTreeAccuracy,",", kNNAccuracy)
