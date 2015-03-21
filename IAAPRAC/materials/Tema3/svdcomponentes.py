>>> from numpy import *

>>> A = array([[1, 2],[3, 4]]) 

>>> U,S,Vh = linalg.svd(A)

>>> S[0]*U[:,0].reshape(-1,1)*V[:,0] + \
S[1]*U[:,1].reshape(-1,1)*V[:,1]

array([[ 1.,  2.],
       [ 3.,  4.]])
