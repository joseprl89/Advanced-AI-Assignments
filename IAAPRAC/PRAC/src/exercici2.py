from numpy.random.mtrand import np
import matplotlib.pyplot as plt
import pylab
from numpy import concatenate, split
from sklearn.naive_bayes import GaussianNB
from sklearn.lda import LDA

observacions = 2000
def classifierComparison(X1, X2, observacions):
    x1,y1 = X1.T
    x2,y2 = X2.T
    
    # b) Represent in a scatter plot
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    ax1.scatter(x1,y1, c='b', marker="s", label='X1')
    ax1.scatter(x2,y2, c='r', marker="o", label='X2')
    plt.legend(loc='upper left');
    fig = pylab.gcf()
    fig.canvas.set_window_title('X1 vs X2')
    plt.show()
    
    # c) create train and test data.
    # First split into two the arrays
    [train1, test1] = split(X1, 2)
    [train2, test2] = split(X2, 2)
    
    expected = concatenate(( np.zeros(observacions/2) , np.ones(observacions/2) ))
    
    # Merge them back into test and train data
    train = concatenate((train1, train2))
    test = concatenate((test1,test2))
    
    # Classify using Naive Bayes
    gaussianClassifier = GaussianNB()
    gaussianClassifier.fit(train, expected)
    naiveBayesScore = gaussianClassifier.score(test, expected)
    
    print("Naive Bayes score: ", naiveBayesScore)
    
    # Classify using LDA
    ldaClassifier = LDA()
    ldaClassifier.fit(train, expected)
    ldaScore = ldaClassifier.score(test, expected)
    
    print("LDA score: ", ldaScore)

# a). Generate the data
X1 = np.random.multivariate_normal([5,-4],[[2,-1],[-1,2]],observacions)
X2 = np.random.multivariate_normal([1,-3],[[1,1.5],[1.5,3]],observacions)

classifierComparison(X1,X2, observacions)

# d) Change X1 to be at 2 -4 instead of 5 -4.
X1D = np.random.multivariate_normal([2,-4],[[2,-1],[-1,2]],observacions)
classifierComparison(X1D,X2, observacions)
