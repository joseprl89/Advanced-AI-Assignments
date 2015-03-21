def readRatings(filename="u.data"):
    lines = [(l.strip()).split("\t")
        for l in (open(filename).readlines())]
    dictio = {int(l[0]) : {}  for l in lines}
   
    for l in lines:
        dictio[int(l[0])][int(l[1])] = int(l[2])   
    return dictio

