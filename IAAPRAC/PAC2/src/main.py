import matplotlib.pyplot as plot
import pylab
from PAC2.src.readdata import readWholeSaleCustomersData
from PAC2.src import distanceCalculation
from PAC2.src.scaledown import scaledown
from numpy import set_printoptions, dot, linalg, argsort, zeros, allclose, array
from _dummy_thread import exit
from mpl_toolkits.mplot3d import Axes3D

set_printoptions(precision = 3)

def exercise1():
    # Read data
    d = readWholeSaleCustomersData()
    
    # display the grap:
    fig1 = plot.figure()
    sp = fig1.gca(projection = '3d')
    sp.scatter(d[:,0],d[:,1],d[:,2])
    fig1.canvas.set_window_title('Initial matrix graph')
    plot.show()
    
    # ANALISIS PCA:
    # Step 1: Calculate covariance matrix (N x N):
    d1 = d - d.mean(0)
    matcov = dot(d1.transpose(),d1)
    
    # Step 2: Obtain Eigenvalue and eigenvectors of covariance matrix
    valp1,vecp1 = linalg.eig(matcov)
    
    # Step 3: Decide which vectors are relevant and plot in 2d the eigenvalues decreasing:
    ind_creciente = argsort(valp1) # orden creciente 
    ind_decre = ind_creciente[::-1] # orden decreciente 
    val_decre = valp1[ind_decre] # valores propios en orden decreciente
    vec_decre = vecp1[:,ind_decre] # ordenar tambien vectores propios
    pylab.plot(val_decre,'o-')
    pylab.gcf().canvas.set_window_title('Eigenvalues')
    pylab.show()
    
    print("Eigenvalues")
    print(valp1)
    print("EigenVectors")
    print(vecp1)
    
    # Project all data to the new base defined by the eigenvectors
    d_PCA = zeros((d.shape[0],d.shape[1]))
    for i in range(d.shape[0]):
        for j in range(d.shape[1]):
            d_PCA[i,j] = dot(d1[i,:],vecp1[:,j])
    
    # Recover initial data by inverting the projection
    orig_means = d.mean(0)
    d_recon = zeros((d.shape[0],d.shape[1]))
    for i in range(d.shape[0]):
        d_recon[i] = orig_means
        for j in range(d.shape[1]):
            d_recon[i] += d_PCA[i,j]*vecp1[:,j]
    
    # Verify that the original data is obtained
    if allclose(d,d_recon):
        print("Reconstruction successful")
    else:
        print("Failed to reconstruct the initial data")
        exit(10)
    
    
    # Project data to the new base using only a subset of the eigenvectors data
    for idx in range(d.shape[1]):
        eigenvectorIndexUsed = idx + 1
       
        # Project data
        d_PCA2 = zeros((d.shape[0],eigenvectorIndexUsed))
        for i in range(d.shape[0]):
            for j in range(eigenvectorIndexUsed):
                d_PCA2[i,j] = dot(d1[i,:],vec_decre[:,j])
        
        # Rebuild on partial data
        d_recon2 = zeros((d.shape[0],d.shape[1]))
        for i in range(d.shape[0]):
            d_recon2[i] = orig_means
            for j in range(eigenvectorIndexUsed):
                d_recon2[i] += d_PCA2[i,j]*vec_decre[:,j] 

        
        # Compare rebuilt data to initial one with relative tolerance of 0.05
        if allclose(d,d_recon2,rtol=0.05):
            print("Managed to obtain a 95% accuracy by using " + str(eigenvectorIndexUsed) + " eigenvector values")
        else:
            print("Didn´t obtain a 95% accuracy by using " + str(eigenvectorIndexUsed) + " eigenvector values")
    
        # Graphic representation of the reconstruction
        fig2 = plot.figure()
        sp2 = fig2.gca(projection = '3d')
        sp2.scatter(d_recon2[:,0],d_recon2[:,1],d_recon2[:,2],c='r',marker='x')
        pylab.gcf().canvas.set_window_title('Reconstruction with ' + str(eigenvectorIndexUsed) + ' eigenvector values')
        plot.show()
        
def exercise2():
    # Read data
    d = readWholeSaleCustomersData()
    
    # display the grap:
    fig1 = plot.figure()
    sp = fig1.gca(projection = '3d')
    sp.scatter(d[:,0],d[:,1],d[:,2])
    fig1.canvas.set_window_title('Initial matrix graph')
    plot.show()
    
    # ANALISIS PCA:
    # Step 1: Calculate covariance matrix (N x N):
    d1 = d - d.mean(0)
    matcov = dot(d1.transpose(),d1)
    
    # Step 2: Obtain Eigenvalue and eigenvectors of covariance matrix
    valp1,vecp1 = linalg.eig(matcov)
    
    # Step 3: Decide which vectors are relevant and plot in 2d the eigenvalues decreasing:
    ind_creciente = argsort(valp1) # orden creciente 
    ind_decre = ind_creciente[::-1] # orden decreciente 
    val_decre = valp1[ind_decre] # valores propios en orden decreciente
    vec_decre = vecp1[:,ind_decre] # ordenar tambien vectores propios
    pylab.plot(val_decre,'o-')
    pylab.gcf().canvas.set_window_title('Eigenvalues')
    pylab.show()
    
    print("Eigenvalues")
    print(valp1)
    print("EigenVectors")
    print(vecp1)
    
    # Project all data to the new base defined by the eigenvectors
    d_PCA = zeros((d.shape[0],d.shape[1]))
    for i in range(d.shape[0]):
        for j in range(d.shape[1]):
            d_PCA[i,j] = dot(d1[i,:],vecp1[:,j])
    
    # Recover initial data by inverting the projection
    orig_means = d.mean(0)
    d_recon = zeros((d.shape[0],d.shape[1]))
    for i in range(d.shape[0]):
        d_recon[i] = orig_means
        for j in range(d.shape[1]):
            d_recon[i] += d_PCA[i,j]*vecp1[:,j]
    
    # Verify that the original data is obtained
    if allclose(d,d_recon):
        print("Reconstruction successful")
    else:
        print("Failed to reconstruct the initial data")
        exit(10)
    
    dictionaryByRegion = {
                          "1.0":[],
                          "2.0":[],
                          "3.0":[]
                          }
    dictionaryByChannel = {
                           "1.0":[],
                           "2.0":[]
                           }
    
    # Project data
    d_PCA2 = zeros((d.shape[0],4))
    for i in range(d.shape[0]):
        for j in range(0,2):
            d_PCA2[i,j] = dot(d1[i,:],vec_decre[:,j])
        
    # Rebuild on partial data
    d_recon2 = zeros((d.shape[0],d.shape[1]))
    for i in range(d.shape[0]):
        d_recon2[i] = orig_means
        for j in range(0,2):
            d_recon2[i] += d_PCA2[i,j]*vec_decre[:,j]
        # populate the channel and region dictionary
        dictionaryByChannel[str(d[i][0])].append(d_recon2[i])
        dictionaryByRegion[str(d[i][1])].append(d_recon2[i])

    
    # Graphic representation of the reconstruction by channel
    channel1Array = array(dictionaryByChannel["1.0"])    
    channel2Array = array(dictionaryByChannel["2.0"])    

    plot.scatter(channel1Array[:,0],channel1Array[:,1],c="r", marker="x")
    plot.scatter(channel2Array[:,0],channel2Array[:,1],c="b", marker="x")
    pylab.gcf().canvas.set_window_title('2D scatter plot by channel')
    plot.show()

    # Graphic representation of the reconstruction by region
    region1Array = array(dictionaryByRegion["1.0"])    
    region2Array = array(dictionaryByRegion["2.0"])    
    region3Array = array(dictionaryByRegion["3.0"])    

    plot.scatter(region1Array[:,0],region1Array[:,1],c="r", marker="x")
    plot.scatter(region2Array[:,0],region2Array[:,1],c="b", marker="x")
    plot.scatter(region3Array[:,0],region3Array[:,1],c="g", marker="x")
    pylab.gcf().canvas.set_window_title('2D scatter plot by region')
    plot.show()

def exercise3():
    # Read data
    d = readWholeSaleCustomersData()
    
    # display the grap:
    fig1 = plot.figure()
    sp = fig1.gca(projection = '3d')
    sp.scatter(d[:,0],d[:,1],d[:,2])
    fig1.canvas.set_window_title('Initial matrix graph')
    plot.show()
    
    # ANALISIS PCA:
    # Step 1: Calculate covariance matrix (N x N):
    d1 = d - d.mean(0)
    matcov = dot(d1.transpose(),d1)
    
    # Step 2: Obtain Eigenvalue and eigenvectors of covariance matrix
    valp1,vecp1 = linalg.eig(matcov)
    
    # Step 3: Decide which vectors are relevant and plot in 2d the eigenvalues decreasing:
    ind_creciente = argsort(valp1) # orden creciente 
    ind_decre = ind_creciente[::-1] # orden decreciente 
    val_decre = valp1[ind_decre] # valores propios en orden decreciente
    vec_decre = vecp1[:,ind_decre] # ordenar tambien vectores propios
    pylab.plot(val_decre,'o-')
    pylab.gcf().canvas.set_window_title('Eigenvalues')
    pylab.show()
    
    print("Eigenvalues")
    print(valp1)
    print("EigenVectors")
    print(vecp1)
    
    # Project all data to the new base defined by the eigenvectors
    d_PCA = zeros((d.shape[0],d.shape[1]))
    for i in range(d.shape[0]):
        for j in range(d.shape[1]):
            d_PCA[i,j] = dot(d1[i,:],vecp1[:,j])
    
    # Recover initial data by inverting the projection
    orig_means = d.mean(0)
    d_recon = zeros((d.shape[0],d.shape[1]))
    for i in range(d.shape[0]):
        d_recon[i] = orig_means
        for j in range(d.shape[1]):
            d_recon[i] += d_PCA[i,j]*vecp1[:,j]
    
    # Verify that the original data is obtained
    if allclose(d,d_recon):
        print("Reconstruction successful")
    else:
        print("Failed to reconstruct the initial data")
        exit(10)
    
    dictionaryByRegion = {
                          "1.0":[],
                          "2.0":[],
                          "3.0":[]
                          }
    dictionaryByChannel = {
                           "1.0":[],
                           "2.0":[]
                           }
    
    firstComponent = 1
    
    # Project data
    d_PCA2 = zeros((d.shape[0],d.shape[1]))
    for i in range(d.shape[0]):
        for j in range(firstComponent,firstComponent + 2):
            d_PCA2[i,j] = dot(d1[i,:],vec_decre[:,j])
        
    # Rebuild on partial data
    d_recon2 = zeros((d.shape[0],d.shape[1]))
    for i in range(d.shape[0]):
        d_recon2[i] = orig_means
        for j in range(firstComponent,firstComponent + 2):
            d_recon2[i] += d_PCA2[i,j]*vec_decre[:,j]
        # populate the channel and region dictionary
        dictionaryByChannel[str(d[i][0])].append(d_recon2[i])
        dictionaryByRegion[str(d[i][1])].append(d_recon2[i])

    
    # Graphic representation of the reconstruction by channel
    channel1Array = array(dictionaryByChannel["1.0"])    
    channel2Array = array(dictionaryByChannel["2.0"])    

    plot.scatter(channel1Array[:,0],channel1Array[:,1],c="r", marker="x")
    plot.scatter(channel2Array[:,0],channel2Array[:,1],c="b", marker="x")
    pylab.gcf().canvas.set_window_title('2D scatter plot by channel')
    plot.show()

    # Graphic representation of the reconstruction by region
    region1Array = array(dictionaryByRegion["1.0"])    
    region2Array = array(dictionaryByRegion["2.0"])    
    region3Array = array(dictionaryByRegion["3.0"])    

    plot.scatter(region1Array[:,0],region1Array[:,1],c="r", marker="x")
    plot.scatter(region2Array[:,0],region2Array[:,1],c="b", marker="x")
    plot.scatter(region3Array[:,0],region3Array[:,1],c="g", marker="x")
    pylab.gcf().canvas.set_window_title('2D scatter plot by region')
    plot.show()

def exercise4():
    # Read data
    d = readWholeSaleCustomersData()
        
    # Scale down using MDS the dimensions
    #mds = array(scaledown(d,distanceCalculation.euclideanDistance))
    mds = array(scaledown(d,distanceCalculation.pearson))
    
    # Representaci�n de los datos en el espacio 2D MDS:
    fig1 = pylab.figure()
    pylab.scatter(mds[:,0],mds[:,1],marker='o',c='r')
    fig1.suptitle('MDS - Metrica Pearson')
    pylab.show()

exercise4()

















