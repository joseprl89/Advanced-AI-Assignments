from math import sqrt

def pearsonCoefficientWithArrays(array1,array2):
    # The arrays will have the same data, so no need to check for commmons
    
    # Compute the means of each array
    mean1 = sum(array1)/len(array1)
    mean2 = sum(array2)/len(array2)

    # Compute numerator and denominator
    num  = sum([(array1[i]-mean1)*(array2[i]-mean2) for i in range(len(array1))])
    den1 = sqrt(sum([pow(array1[i]-mean1, 2) for i in range(len(array1))]))
    den2 = sqrt(sum([pow(array2[i]-mean2, 2) for i in range(len(array1))]))
    den  = den1*den2

    # Compute the coefficient if possible or return zero
    if den==0:
        return 0

    return num/den

# calculates the euclidean similarity between two arrays.
def euclideanSimilarityArrays(array1, array2):
    squaredSum = 0
    
    for i in range(len(array1)):
        squaredSum += pow(array1[i]-array2[i], 2)        
    
    return 1/(1+sqrt(squaredSum))

# webData is a dictionary of { ids : [interactions] }
# The result is the average of all the [interactions] arrays
def webInteractionAverage(interactionsDictionary):
    interactions = []
    count = 0
    for index in interactionsDictionary:
        if len (interactions) == 0:
            interactions = interactionsDictionary[index]
            count = 1
        else:
            interactions = [x + y for x, y in zip(interactions, interactionsDictionary[index])]
            count = count + 1
    
    if count == 0:
        return 0
    
    return list(map(lambda x: x/len(interactions), interactions))
        
    

# UserData is a dictionary of { webId : [interactions] }
# The result is a tuple with the webId and the interactions done with them.
# The method perform is a naive average of the interacions, as we don't have 
# any info on what should be the ponderation of the data.
def mostActiveWebsite(userData):
    maximumAverageInteractions = 0
    mostActiveWeb = -1
    for webId in userData:
        interactions = userData[webId]
        average = sum(interactions) / len(interactions)
        if average > maximumAverageInteractions:
            mostActiveWeb = webId
            maximumAverageInteractions = average
    
    return mostActiveWeb, userData[mostActiveWeb]
