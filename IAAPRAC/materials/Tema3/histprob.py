import numpy as np
import matplotlib.mlab as mlab
import pylab

# datos gaussianos media mu desviación estandard sigma:
mu, sigma = 200, 30
y_datos = mu + sigma*np.random.randn(10000)

# histograma recuento de valores en cada bin:
nbins = 50 #número de intérvalos

fig1 = pylab.figure()
n, bins, patches = pylab.hist(y_datos, nbins, normed=0, facecolor='green', alpha=0.75)
pylab.title(r'$\mathrm{Histograma\ datos\ gaussianos}\ \mu=200,\ \sigma=30$')
pylab.ylabel('Contaje')
pylab.xlabel('Intervalos (bin)')
pylab.show()

# histograma normalizado de los datos (densidad de probabilidad)
fig2 = pylab.figure()
p, bins, patches = pylab.hist(y_datos, nbins, normed=1, facecolor='blue', alpha=0.75)

# Ajuste de los datos con una funcion de densidad
# de probabilidad gaussiana:
y_pdf = mlab.normpdf(bins, mu, sigma)
l = pylab.plot(bins, y_pdf, 'r--', linewidth=1)
pylab.ylabel('Probabilidad')
pylab.xlabel('Intervalos (bin)')
pylab.title(r'$\mathrm{Densidad de probabilidad}\ \mu=200,\ \sigma=30$')
pylab.grid(True)
pylab.show()

# Comprobar que la integral de la función densidad de probabilidad
# es igual a 1:

Integral = sum(p*np.diff(bins))
print Integral



