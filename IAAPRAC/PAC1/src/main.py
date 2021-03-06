from sklearn import metrics

from PAC1.src.ReadWebData import readWebData
from PAC1.src.ReadWebData import readUserData
from PAC1.src.ReadWebData import readFavouriteData

from PAC1.src.kmeans_dictio import kmeans_dictio

from PAC1.src.userRecommendation import pearsonCoefficientWithArrays
from PAC1.src.userRecommendation import webInteractionAverage
from PAC1.src.userRecommendation import mostActiveWebsite

# Read the data
webData = readWebData("../data/webs.data")
userData = readUserData("../data/webs.data")
favouriteData = readFavouriteData("../data/favorits.data")

# Get the kmeans dictionary
assignment, centroids = kmeans_dictio(webData, 4, 100)

# ARI Calculation.

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

ard = metrics.adjusted_rand_score(labels_true, labels_obtained)

print("Adjusted rand score = {}".format(ard))

# User recommendations:
recommendationsPerUser = {}

for user in userData:
    websVisited = userData[user]
    # userInteractionAverage = webInteractionAverage(websVisited)
    _,mostInteractionsByUser = mostActiveWebsite(websVisited)
        
    # Take the other webs in the group that are not visited by the user.
    websNotVisitedByUser = [web for web in webData if not web in websVisited]
    
    if len(websNotVisitedByUser) == 0:
        print("No webs in group not visited by user. Should look in all the other groups.")
        continue
    
    recommendations = []
    
    # Calculate Euclidean similarity for each of the other webs
    # compared to the user's favorite web (could also use the average)
    for otherWebId in websNotVisitedByUser:
        similarity = pearsonCoefficientWithArrays(webInteractionAverage(webData[otherWebId]), mostInteractionsByUser)
        recommendations.append({'similarity':similarity,'webId':otherWebId})
        
    recommendations = sorted(recommendations, key=lambda k: k['similarity'], reverse=True) 
    recommendationsPerUser[user] = recommendations

# Finally, iterate the recommendations, check the average location of the found issue.
count      = 0
sumIndexes = 0
sumLengths = 0
for userId in recommendationsPerUser:
    recommendations = recommendationsPerUser[userId]
    expectedFavourite = favouriteData[userId]
    indexes = [i for i,x in enumerate(recommendations) if x['webId'] == expectedFavourite]
    if len(indexes) == 1:
        sumIndexes = sumIndexes + indexes[0]
        sumLengths = sumLengths + len(recommendations)
        count = count + 1

print("Average index of the favourite is {} and the avg length is {}"
      .format(sumIndexes/count, sumLengths/count))
