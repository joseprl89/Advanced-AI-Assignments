import os

parametros = '-t 1 -d 1'
train = 'Iris-setosa.train.txt'
test  = 'Iris-setosa.test.txt'
model = 'Iris-setosa.model.txt'
preds = 'Iris-setosa.predicciones.txt'
outs  = 'Iris-setosa.output.txt'

os.system('./svm_learn ' + parametros + ' ' + train + ' ' + model)

os.system('./svm_classify ' + test + ' ' + model + ' ' + preds + ' > ' + outs)

l = list(map(lambda l: l.strip(),
             open(outs, 'r').readlines()))
print(l[0])
print(l[2])
print(l[3])
