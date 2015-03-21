from libsvm.svmutil import *
from time import clock

def kernelVSM(a, b):
   la = [(int(k),float(v)) for k, v in (l.split(':') for l in a)]
   lb = [(int(k),float(v)) for k, v in (l.split(':') for l in b)]
   s = 0
   i = 0
   j = 0
   while (i < len(la)) and (j < len(lb)):
      if la[i][0] == lb[j][0]:
         s += la[i][1] * lb[j][1]
         i += 1
         j += 1
      elif la[i][0] < lb[j][0]:
         i += 1
      else:
         j +=1
   return s

train = list(map(lambda l: (l.strip()).split(' '),
                 filter(lambda x: x[0] != '#',
                        open('train.dat', 'r').readlines())))
y=list(map(lambda x: int(x.pop(0)), train))

inici = clock()
x = [dict([(i+1,kernelVSM(train[i], train[j]))
           for i in range(len(train))])
     for j in range(len(train))]
list(map(lambda l, i: l.update({0:i+1}), x, range(len(x))))
print("km", clock() - inici, "s", len(x),"x",len(x[0]))

inici = clock()
model = svm_train(y, x, '-s 0 -t 4')
print("learn", clock() - inici, "s")
svm_save_model('model.km.txt', model)

##model = svm_load_model('model.km.txt')

test = list(map(lambda l: (l.strip()).split(' '),
                 filter(lambda x: x[0] != '#',
                        open('test.dat', 'r').readlines())))
yt=list(map(lambda x: int(x.pop(0)), test))
inici = clock()
xt = [dict([(i+1,kernelSVM(test[j], train[i]))
           for i in range(len(train))])
     for j in range(len(test))]
list(map(lambda l, i: l.update({0:-1}), xt, range(len(xt))))
print("kmt", clock() - inici, "s", len(xt),"x",len(xt[0]))

inici = clock()
p_label, p_acc, p_val = svm_predict(yt, xt, model)
print("predict", clock() - inici, "s")

