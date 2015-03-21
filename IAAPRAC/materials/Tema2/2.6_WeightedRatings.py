# Produces a sorted list of weighted ratings from a dictionary of
# user ratings and a user id.
# You can choose the function of similarity between users.
def weightedRating(dictio, user, similarity = pearsonCoeff):
    # In the first place a dictionary is generated with the similarities
    # of our user with all other users.
    # This dictionary could be stored to avoid recomputing it.
    simils = {x: similarity(dictio[user], dictio[x])
              for x in dictio if x != user}

    # Auxiliary dictionaries {movieId: [rating*users similarity]}
    # and {movieId: [users similarity]} (numerator and denominator
    # of the weighted rating)
    numerator   = {}
    denominator = {}

    # The ratings dictionary is traversed, while filling the auxiliary
    # dictionaries with the values found.
    for userId in simils:
        for movieId in dictio[userId]:
            if not numerator.has_key(movieId):
                numerator  [movieId] = []
                denominator[movieId] = []
            s = simils[userId]
            numerator  [movieId].append(dictio[userId][movieId]*s)
            denominator[movieId].append(s)

    # Compute and sort weighted ratings    
    result = []
    for movieId in numerator:
        s1 = sum(numerator  [movieId])
        s2 = sum(denominator[movieId])
        if s2 == 0:
            mean = 0.0
        else:
            mean = s1/s2
        result.append((movieId,mean))

    result.sort(key = lambda x: x[1], reverse=True)
    return result
