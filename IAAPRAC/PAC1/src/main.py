import json
from PAC1.src.ReadWebData import readRatings
from PAC1.src.kmeans_dictio import kmeans_dictio

# Read the ratings
ratings = readRatings("../data/webs.data")


# Dump the JSON
print(readRatings("../data/webs.data"))

# Get the kmeans dictionary
assignment, centroids = kmeans_dictio(ratings, 6, 10)

# Dump the Assignments JSON
print("Assignments: " + json.dumps(assignment))
print("Centroids: " + json.dumps(centroids))