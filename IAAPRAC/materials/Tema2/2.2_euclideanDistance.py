from math import sqrt

def euclideanDist(dic1, dic2):
    # Compute the sum of squares of the elements common
    # to both dictionaries
    sum2 = sum([pow(dic1[elem]-dic2[elem], 2)
                for elem in dic1 if elem in dic2])
    return sqrt(suma)

def euclideanSimilarity(dic1, dic2):
    return 1/(1+euclideanDist(dic1, dic2))
	
