from PAC2.src.readdata import readWholeSaleCustomersData
from PAC2.src.pca import pca

def exercise1():
    data = readWholeSaleCustomersData()
    projectionMatrix,variance,mean_X = pca(data)
    
    # Dump the result
    print("Projection matrix")
    print (projectionMatrix)
    print("Variance")
    print (variance)
    print("Mean")
    print (mean_X)
    
exercise1()