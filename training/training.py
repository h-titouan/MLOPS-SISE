import numpy as np
from sklearn import datasets
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from joblib import dump

import os
os.chdir("/Users/titouanhoude/Documents/GitHub/MLOPS-SISE/training")
iris = pd.read_csv('iris.csv', sep = ",")
# Y = iris.drop()
print(iris.columns)
y = iris["variety"]
x = iris.drop('variety', axis = 1)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(x, y)

dump(model, './iris_ML_v1.joblib')
