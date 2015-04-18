from numpy import array,asfortranarray

# Returns a matrix with the wholesale customer data. In each row we have data for a customer
def readWholeSaleCustomersData(filename="../data/Wholesale customers.csv"):
    
    # Reads all the lines into a vector of vectors
    lines = [(l.strip()).split(",")
        for l in (open(filename).readlines())]

    # Remove the header
    lines = lines[1:]

    # Convert all values to floats      
    for line in lines:
        for idx, val in enumerate(line):
            line[idx] = float(val)

    # Return a fortran array from numpy
    return asfortranarray(array(lines))

# print(readWholeSaleCustomersData())