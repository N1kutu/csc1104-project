import pandas as pd
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

df = pd.read_csv("Data.csv")
# print(df.nunique())

correlation_matrix = df.corr(numeric_only=True)
correlation_matrix["CPU Mark"]
meanCpu = df.loc[
    (df["No. Sockets"] == 1) & (df["Cores"] == 8) & (df["CPU Mark"] == 8672)
]

# meanCpu.to_csv("MeanCPU.csv")

X = df.drop("CPU Mark", axis=1)
X = X.drop("CPU Name", axis=1)
X = X.drop("Category", axis=1)
X = X.values
y = df["CPU Mark"]
y = y.values

import numpy as np
new_data_point = np.array([
    1.160895,
    7.550530,
    1740.388457,
    76.984982,
    173.882688,
])

distances = np.linalg.norm(X - new_data_point, axis=1)
k = 2
nearest_neighbor_ids = distances.argsort()[:k]

# Find the groun truth based on the three nearest neighbors
nearest_neighbor_mark = y[nearest_neighbor_ids]
prediction = nearest_neighbor_mark.mean()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=12345
)

from sklearn.neighbors import KNeighborsRegressor
knn_model = KNeighborsRegressor(n_neighbors = 2)
knn_model.fit(X_train, y_train)

from sklearn.metrics import root_mean_squared_error
train_preds = knn_model.predict(X_train)
rmse = root_mean_squared_error(y_train, train_preds)
test_preds = knn_model.predict(X_test)
mse = root_mean_squared_error(y_test, test_preds)

import seaborn as sns
cmap = sns.cubehelix_palette(as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(
    X_test[:, 3], X_test[:, 4], c=y_test, s=50, cmap=cmap
)
# f.colorbar(points)
# plt.show()

from sklearn.model_selection import GridSearchCV
parameters = {"n_neighbors": range(1, 50)}
gridsearch = GridSearchCV(KNeighborsRegressor(), parameters)
gridsearch.fit(X_train, y_train)

train_preds_grid = gridsearch.predict(X_train)
train_rmse = root_mean_squared_error(y_train, train_preds_grid)
# print(train_rmse)

test_preds_grid = gridsearch.predict(X_test)
test_rmse = root_mean_squared_error(y_test, test_preds_grid)
# print(test_rmse)

best_k = gridsearch.best_params_["n_neighbors"]
bagged_knn = KNeighborsRegressor(n_neighbors=best_k)
from sklearn.ensemble import BaggingRegressor
bagging_model = BaggingRegressor(bagged_knn, n_estimators=100)
bagging_model.fit(X_train, y_train)

test_preds_grid = bagging_model.predict(X_test)
test_rmse = root_mean_squared_error(y_test, test_preds_grid)
print(test_rmse)
print(test_preds_grid)