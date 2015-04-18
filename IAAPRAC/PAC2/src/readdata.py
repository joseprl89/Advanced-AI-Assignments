
# Returns a matrix with the wholesale customer data. In each row we have data for a customer
def readWholeSaleCustomersData(filename="../data/Wholesale customers.csv"):
    # Reads all the lines into a vector of vectors
    lines = [(l.strip()).split("\t")
        for l in (open(filename).readlines())]
    
    # Remove the Title from the csv file
    lines = lines[1:]
    
    return lines

# readWholeSaleCustomersData()