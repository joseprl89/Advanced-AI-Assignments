#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import sample
from itertools import repeat
from PAC1.src.euclideanDistance import euclideanSimilarity

# Given a dictionary like {key1 : {key2 : value}} it computes k-means
# clustering, with k groups, executing maxit iterations at most, using
# the specified similarity function.
# It returns two things (as a tuple):
# -{key1:cluster number} with the cluster assignemnts (which cluster
#  does each element belong to
# -[{key2:[values]}] a list with the k centroids (means of the values
#  for each cluster.
# Recall that input dictionary can be sparse, and that will be reflected
# on the centroids list.
def kmeans_dictio(dictionary, k, maxit, similarity = euclideanSimilarity):
    
    # First k random points are taken as initial centroids.
    # Each centroid is {key2 : [value]}
    centroids = [dictionary[x] for x in sample(dictionary.keys(), k)]
    
    # Assign each key1 to a cluster number 
    previous    = {}
    assignment = {}
    
    # On each iteration it assigns points to the centroids and computes
    # new centroids
    for _ in range(maxit):

        # Assign points to the closest centroids
        for key1 in dictionary:
            simils = list(map(similarity,repeat(dictionary[key1],k), centroids))
            assignment[key1] = simils.index(max(simils))

        # If there are no changes in the assignment then finish
        if previous == assignment:
            break
        previous.update(assignment)
            
        # Recompute centroids: annotate each key values at each centroid
        values    = {x : {} for x in range(k)}
        counters = {x : {} for x in range(k)}
        for key1 in dictionary:
            group = assignment[key1]
            for key2 in dictionary[key1]:
                if not key2 in values[group]:
                    values    [group][key2] = 0
                    counters [group][key2] = 0
                
                # TODO Modify the update of values to sum arrays rather 
                # than single values.
                values  [group][key2] += dictionary[key1][key2]
                counters[group][key2] += 1
        
        # Compute means (new centroids)
        centroids = []
        for group in values:
            centr = {}
            for key2 in values[group]:
                centr[key2] = values[group][key2] / counters[group][key2]
            centroids.append(centr)
        
        if None in centroids: break

    return (assignment, centroids)
