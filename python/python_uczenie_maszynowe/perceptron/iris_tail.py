import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from python_uczenie_maszynowe.perceptron.Perceptron import Perceptron

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
print(df.tail)

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
# print(y)
X = df.iloc[0:100, [0, 2]].values
# print(X)
plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='Setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='Versicolor')
plt.xlabel('Długość działki [cm]')
plt.ylabel('Długość płatka [cm]')
plt.legend(loc='upper left')
plt.show()

ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.show()
