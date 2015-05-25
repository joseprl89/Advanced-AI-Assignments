from numpy.random.mtrand import normal
from numpy import concatenate, reshape
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pylab

# a). Generate the data
observacions = 1000

X1 = normal(0.5, 0.2, observacions)
X2 = normal(4.5, 0.6, observacions)
X3 = [3 * x1 + 1 for x1 in X1 ]
X4 = [2 * X1[i] + X2[i] for i in range(observacions)]

# Build the observations,4 sized matrix from the data. That means that row[i] will contain X1[i], X2[i], X3[i] and X4[i].
A = concatenate((X1,X2,X3,X4), axis=0)
A = reshape(A,(4,observacions))
A = A.transpose()
print("Data matrix: ", A)

# b) Scatter plot all data combinations.
dataSeries = [X1,X2,X3,X4]
for i in range(len(dataSeries)):
    for j in range(i+1, len(dataSeries)):
        # compare data set Xi to Xj.
        plt.scatter(dataSeries[i], dataSeries[j])
        fig = pylab.gcf()
        fig.canvas.set_window_title('Scatter plot X' + str(i+1) + " to X" + str(j+1))
        plt.show()

# c) Apply PCA 
pca = PCA(n_components=4)
pca.fit(A)
print("PCA related datasets:", pca.explained_variance_ratio_)

# d) Apply PCA to 4 independent datasets 
Y1 = normal(1, 0.1, observacions)
Y2 = normal(1, 0.1, observacions)
Y3 = normal(1, 0.1, observacions)
Y4 = normal(1, 0.1, observacions)

# Build the observations,4 sized matrix from the data. That means that row[i] will contain X1[i], X2[i], X3[i] and X4[i].
B = concatenate((Y1,Y2,Y3,Y4), axis=0)
B = reshape(B,(4,observacions))
B = B.transpose()

pca2 = PCA(n_components=4)
pca2.fit(B)
print("PCA unrelated datasets:", pca2.explained_variance_ratio_)


