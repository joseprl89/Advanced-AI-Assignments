def readRatings(filename="u.data"):
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