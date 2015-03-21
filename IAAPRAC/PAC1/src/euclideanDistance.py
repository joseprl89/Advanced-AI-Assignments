from math import sqrt

def euclideanDist(dic1, dic2):
    squaredSum = 0
    # iterate the dictionaries and sum the distance of the arrays using 
    # euclidean distance as well
    for elem in dic1:
        if elem in dic2:
            for i,val in enumerate(dic1[elem]):
                squaredSum += pow(val-dic2[elem][i], 2)        
    
    return sqrt(squaredSum)

def euclideanSimilarity(dic1, dic2):
    return 1/(1+euclideanDist(dic1, dic2))
    