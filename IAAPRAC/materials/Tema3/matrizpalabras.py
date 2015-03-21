from textos import *
import numpy
import operator


# obtener un conjunto de diccionarios:
docs = textos('C:\\textos\\*.txt')

# calcular la matriz de recuento de palabras
# tamano N textos x K palabras

dicc_sort = []
# loop over dictionaries
for k in range(len(docs)):
# ordenar diccionario por numero de apariciones
    ds = sorted(docs[k].iteritems(),key=operator.itemgetter(1),reverse=True)
    dicc_sort.append(ds)
# Seleccionar un grupo de K palabras que
# apezcan en los diferentes diccionarios:
    print k
# listar las 10 palabras más utilizadas en cada texto:
    for kw in range(1,10):
        print ds[kw][0]



