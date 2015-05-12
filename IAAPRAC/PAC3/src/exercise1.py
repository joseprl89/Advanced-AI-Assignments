from PAC3.src.NaiveBayes import naiveBayes;
from PAC3.src.DecisionTree import decisionTree;
from PAC3.src.KNN import kNN;
from PAC3.src.SVM import kernelTypeLinear;
from PAC3.src.SVM import kernelTypeRBF;
from PAC3.src.SVM import kernelRBF;
from PAC3.src.SVM import kernelSetRBF;
from PAC3.src.SVM import kernelSet;
from PAC3.src.SVM import svm;

def readData():
    # Load file
    l = list(map(lambda l: (l.strip()).split(','),
            open('../data/Wholesale customers.csv', 'r').readlines()))
    
    for row in l:
        row[1] = row[0] + '' + row[1]
    
    l = [row[1:] for row in l ]
    
    l = l[1:]
    return l;
    
    
print("RatioToTest, Naive bayes accuracy, Decision tree accuracy, kNNTreeAccuracy, SVM Lineal, SVM RBF, SVM RBF SET")
for ratioToTest in range(2,20):
    ######## Naive bayes 
    naiveBayesAccuracy, naiveBayesPredictions = naiveBayes(readData(), ratioTests=ratioToTest)
    
    ######## Decision tree
    decisionTreeAccuracy,decisionTreePredictions = decisionTree(readData(),ratioToTest=ratioToTest)
    
    ######## kNN
    kNNAccuracy,kNNPredictions = kNN(readData(),ratioToTest=ratioToTest);
    
    ######## Support vector machine Kernel linear 
    svm1Accuracy, svm1Predictions = svm(readData(), ratioToTest=ratioToTest, kernel=kernelSet, kernelType=kernelTypeLinear)
    
    ######## Support vector machine Kernel RBF
    svm2Accuracy, svm2Predictions = svm(readData(), ratioToTest=ratioToTest, kernel=kernelRBF, kernelType=kernelTypeRBF)
    
    ######## Support vector machine Kernel RBF SET
    svm3Accuracy, svm3Predictions = svm(readData(), ratioToTest=ratioToTest, kernel=kernelSetRBF, kernelType=kernelTypeRBF)
    
    # Print results using CSV format
    print(ratioToTest,",",naiveBayesAccuracy,",",decisionTreeAccuracy,",", kNNAccuracy,",", svm1Accuracy, ",",svm2Accuracy, ",",svm3Accuracy)

