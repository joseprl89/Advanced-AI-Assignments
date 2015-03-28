
# Returns a dictionary with structure {userId:favoriteWebId}
def readFavouriteData(filename):
    # Reads all the lines into a vector of vectors
    lines = [(l.strip()).split("\t")
        for l in (open(filename).readlines())]
    
    # Creates a dictionary with the id as the first item of the line.
    dictio = { int(l[0]) : int(l[1]) for l in lines}
   
    return dictio

def readWebData(filename):
    # Reads all the lines into a vector of vectors
    lines = [(l.strip()).split("\t")
        for l in (open(filename).readlines())]
    
    # Creates a dictionary with the id as the first item of the line.
    dictio = { int(l[0]) : {}  for l in lines}
   
    # Populate the dictionary with for each web, a dictionary for each user
    # containing the rest of values in an array
    for l in lines:
        webId = int(l[0])
        userId = int(l[1])
        values = [int(s) for s in l[2:]]
        dictio[webId][userId] = values
    
    return dictio

# Acts as readWebData but the first key is the web, and the second one is the user.
def readUserData(filename):
    # Reads all the lines into a vector of vectors
    lines = [(l.strip()).split("\t")
        for l in (open(filename).readlines())]
    
    # Creates a dictionary with the id as the first item of the line.
    dictio = { int(l[1]) : {}  for l in lines}
   
    # Populate the dictionary with for each web, a dictionary for each user
    # containing the rest of values in an array
    for l in lines:
        webId = int(l[0])
        userId = int(l[1])
        values = [int(s) for s in l[2:]]
        dictio[userId][webId] = values
    
    return dictio

