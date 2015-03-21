from scipy import stats
from numpy import *

# datos:
mu1, sigma1 = 200, 30
x = mu1 + sigma1*random.randn(3).T
mu2, sigma2 = 10, 5
y = mu2 + sigma2*random.randn(3).T

# matriz de covarianza:
covmat = cov(x,y,bias=1)

# matriz de correlación:
corrmat = corrcoef(x,y)

>>> print covmat
[[ 902.94004704  -86.47788485]
 [ -86.47788485   26.52406588]]

>>> print var(x), var(y)
902.940047043 26.5240658823

>>> print corrmat
[[ 1.         -0.55879891]
 [-0.55879891  1.        ]]

# relación entre ambas:
>>> cov(x/std(x),y/std(y),bias=1)
array([[ 1.        , -0.55879891],
       [-0.55879891,  1.        ]])




