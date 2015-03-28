from math import sqrt

# calculates the euclidean similarity between two arrays.
def euclideanSimilarityArrays(array1, array2):
    squaredSum = 0
    
    for i in range(len(array1)):
        squaredSum += pow(array1[i]-array2[i], 2)        
    
    return 1/(1+sqrt(squaredSum))

# webData is a dictionary of { userId : [interactions] }
# The result is the average of all the [interactions] arrays
def webInteractionAverage(webData):
    interactions = []
    count = 0
    for userId in webData:
        if len (interactions) == 0:
            interactions = webData[userId]
            count = 1
        else:
            interactions = [x + y for x, y in zip(interactions, webData[userId])]
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
