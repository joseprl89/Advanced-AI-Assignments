from scipy import stats
import numpy as np

# datos gaussianos:
mu, sigma = 10, 5.5
y = mu + sigma*np.random.randn(10000)

# Estimación de momentos:
# momento de primer orden: media
media = y.mean()

# momento segundo orden: varianza
var = y.var()

# momento tercer orden: asimetría (skweness)
skew = stats.skew(y)

# momento cuarto orden: Curtosis
kurt = stats.kurtosis(y)

>>> print media, var, skew, kurt
10.0575611617 30.9623694469 0.0126290768091 0.025294666173
