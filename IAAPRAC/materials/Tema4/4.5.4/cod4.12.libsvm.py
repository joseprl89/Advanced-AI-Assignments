from libsvm.svmutil import *

y, x = svm_read_problem('Iris-setosa.train.txt')
m = svm_train(y, x, '-c 4 -t 1 -d 2')
yt, xt = svm_read_problem('Iris-setosa.test.txt')
p_label, p_acc, p_val = svm_predict(yt, xt, m)

