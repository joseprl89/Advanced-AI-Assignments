import json
from PAC1.src.ReadWebData import readRatings
from PAC1.src.kmeans_dictio import kmeans_dictio
from sklearn import metrics

# Read the ratings
ratings = readRatings("../data/webs.data")


# Dump the JSON
print(readRatings("../data/webs.data"))

# Get the kmeans dictionary
assignment, centroids = kmeans_dictio(ratings, 4, 100)

# [1..5], [6..11], [12..16] i [17..20]
labels_true = [
               0,0,0,0,0,
               1,1,1,1,1,1,
               2,2,2,2,2,
               3,3,3,3
               ];
labels_obtained = []

for i in range(1,21):
    labels_obtained.append(assignment[i])

# Dump the Assignments JSON
# print("Expected: " + json.dumps(labels_true))
# print("Obtained: " + json.dumps(labels_obtained))

ard = metrics.adjusted_rand_score(labels_true, labels_obtained)

print("Adjusted rand score = {}".format(ard))