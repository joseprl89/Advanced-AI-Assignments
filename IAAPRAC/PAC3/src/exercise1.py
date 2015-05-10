from PAC3.src.NaiveBayes import naiveBayes;
from PAC3.src.DecisionTree import decisionTree;

# Load file
l = list(map(lambda l: (l.strip()).split(','),
            open('../data/Wholesale customers.csv', 'r').readlines()))

for row in l:
    row[1] = 'Channel:' + row[0] + ' ' + 'Region: ' + row[1]

l = [row[1:] for row in l ]

ratioToTest=10

######## Naive bayes 

naiveBayesAccuracy, naiveBayesPredictions = naiveBayes(l, ratioTests=ratioToTest)

# Print accuracy and predictions
print('naiveBayesAccuracy. :', naiveBayesAccuracy , '%')

######## Decision tree

decisionTreeAccuracy,decisionTreePredictions = decisionTree(l,ratioToTest=ratioToTest)

# Print accuracy and predictions
print('decisionTreeAccuracy:', decisionTreeAccuracy, '%')
print('decisionTreeAccuracy:', decisionTreePredictions)

######## kNN



######## Support vector machine Kernel 1


######## Support vector machine Kernel 2


