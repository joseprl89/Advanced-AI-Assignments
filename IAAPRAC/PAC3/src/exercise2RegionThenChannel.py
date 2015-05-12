from PAC3.src.NaiveBayes import naiveBayes;
from PAC3.src.KNN import kNN;
from PAC3.src.SVM import kernelTypeLinear;
from PAC3.src.SVM import kernelTypeRBF;
from PAC3.src.SVM import kernelRBF;
from PAC3.src.SVM import kernelSetRBF;
from PAC3.src.SVM import kernelSet;
from PAC3.src.SVM import svm;
from copy import deepcopy
from PAC3.src.DecisionTree import decisionTree

def calculateTwoIdsSVM(l, ratioToTest=3, kernel=kernelSet, kernelType=kernelTypeLinear):
    # Get a matrix removing the first column.
    minusOneId = deepcopy(l);
    for row in minusOneId:
        row.pop(0)
    
    accuracySecondId,_ = svm(minusOneId, ratioToTest, kernel=kernel, kernelType=kernelType)
    accuracyFirstId,_ = svm(l, ratioToTest, kernel=kernel, kernelType=kernelType)
    
    # We only care when both decisions are correct, that means we need to multiply the accuracies
    return accuracyFirstId * accuracySecondId / 100


def calculateTwoIds(l, ratioToTest=3, method=naiveBayes):
    # Get a matrix removing the first column.
    minusOneId = deepcopy(l);
    for row in minusOneId:
        row.pop(0)
    
    accuracySecondId,_ = method(minusOneId, ratioToTest)
    accuracyFirstId,_ = method(l, ratioToTest)
    
    # We only care when both decisions are correct, that means we need to multiply the accuracies
    return accuracyFirstId * accuracySecondId /100

def readData():
    # Load file
    l = list(map(lambda l: (l.strip()).split(','),
            open('../data/Wholesale customers.csv', 'r').readlines()))
    
    l = l[1:]
            
    return l;
    
ratioToTest=3

print("RatioToTest, Naive bayes accuracy, Decision tree accuracy, kNNTreeAccuracy, SVM Lineal, SVM RBF, SVM RBF SET")

######## Naive bayes 
naiveBayesAccuracy = calculateTwoIds(readData(), ratioToTest=ratioToTest, method=naiveBayes)

######## Decision tree
decisionTreeAccuracy = calculateTwoIds(readData(),ratioToTest=ratioToTest, method=decisionTree)

######## kNN
kNNAccuracy = calculateTwoIds(readData(), ratioToTest=ratioToTest, method=kNN);

######## Support vector machine Kernel linear 
svm1Accuracy = calculateTwoIdsSVM(readData(), ratioToTest=ratioToTest, kernel=kernelSet, kernelType=kernelTypeLinear)

######## Support vector machine Kernel RBF
svm2Accuracy = calculateTwoIdsSVM(readData(), ratioToTest=ratioToTest, kernel=kernelRBF, kernelType=kernelTypeRBF)

######## Support vector machine Kernel RBF SET
svm3Accuracy = calculateTwoIdsSVM(readData(), ratioToTest=ratioToTest, kernel=kernelSetRBF, kernelType=kernelTypeRBF)

# Print results using CSV format
print(ratioToTest,",",naiveBayesAccuracy,",",decisionTreeAccuracy,",", kNNAccuracy,",", svm1Accuracy, ",",svm2Accuracy, ",",svm3Accuracy)

