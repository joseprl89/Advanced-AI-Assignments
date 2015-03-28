#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import sample
from itertools import repeat
from PAC1.src.euclideanDistance import euclideanSimilarity

# Given a dictionary like {webId : {userId : value}} it computes k-means
# clustering, with k groups, executing maxit iterations at most, using
# the specified similarity function.
# It returns two things (as a tuple):
# -{webId:cluster number} with the cluster assignemnts (which cluster
#  does each element belong to
# -[{userId:[values]}] a list with the k centroids (means of the values
#  for each cluster.
# Recall that input dictionary can be sparse, and that will be reflected
# on the centroids list.
def kmeans_dictio(dictionary, k, maxit, similarity = euclideanSimilarity):

    # First k random points are taken as initial centroids.
    # Each centroid is {userId : [values]}
    centroids = [dictionary[x] for x in sample(dictionary.keys(), k)]

    # Assign each webId to a cluster number
    previous    = {}
    assignment = {}

    # On each iteration it assigns points to the centroids and computes
    # new centroids
    for iteration in range(maxit):
        print('Iteration {}'.format(iteration + 1))
        
        # Assign points to the closest centroids
        for webId in dictionary:
            simils = list(map(similarity,repeat(dictionary[webId],k), centroids))
            assignment[webId] = simils.index(max(simils))
            print("Assigning web {} to centroid {}".format(webId,assignment[webId]))

        # If there are no changes in the assignment then finish
        if previous == assignment:
            print("Centroids not updated. Leaving.")
            break
        previous.update(assignment)

        # Recompute centroids: annotate each key values at each centroid
        values    = {x : {} for x in range(k)}
        counters = {x : {} for x in range(k)}
        for webId in dictionary:
            print("Computing centroid for web {}".format(webId))
            group = assignment[webId]
            for userId in dictionary[webId]:
                if not userId in values[group]:
                    # Create an array of 0's with the given length
                    values    [group][userId] = [0 for _ in range(len(dictionary[webId][userId]))]
                    counters [group][userId] = 0

                # Add vectors
                values[group][userId] = [x + y for x, y in zip(values[group][userId], dictionary[webId][userId])]
                counters[group][userId] = counters[group][userId] + 1

        print("Computing new centroids")
        # Compute means (new centroids)
        centroids = []
        for group in values:
            centr = {}
            for userId in values[group]:
                # Average using the counters and the sums performed before.
                centr[userId] = list(map(lambda x : x / counters[group][userId], values[group][userId]))
            centroids.append(centr)

        if None in centroids: break

    print("Done.")
    return (assignment, centroids)
