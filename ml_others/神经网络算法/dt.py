from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd
from sklearn import cross_validation

X = np.array([[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [1, 1], [2, 2], [3, 3]])
y = np.array([1, 1, 1, 1, 1, 2, 2, 2])
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)

clf.fit(X, y)
print(clf.predict([[20, 21]]))
