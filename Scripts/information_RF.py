import pandas as pd
import matplotlib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("../Data/Data.csv")

correlation_matrix = df.corr(numeric_only=True)
correlation_matrix["CPU Mark"]

meanCpu = df.loc[
    (df["No. Sockets"] == 1) & (df["Cores"] == 10) & (df["CPU Mark"] == 13457)
]

X = df.drop(["CPU Mark", "Category", "CPU Name"], axis=1).values
y = df["CPU Mark"].values
cpu_names = df["CPU Name"]

new_data_point = np.array(
    [
        1.160895,
        7.550530,
        1740.388457,
        76.98498,
        173.882688
    ]
)

X_train, X_test, y_train, y_test, cpu_names_train, cpu_names_test = train_test_split(
    X, y, cpu_names, test_size=0.2, random_state=12345
)

rf_model = RandomForestRegressor(n_estimators=100, random_state=12345)
rf_model.fit(X_train, y_train)

train_preds = rf_model.predict(X_train)
test_preds = rf_model.predict(X_test)

train_rmse = root_mean_squared_error(y_train, train_preds)
test_rmse = root_mean_squared_error(y_test, test_preds)

print(f"Train RMSE: {train_rmse}")
print(f"Test RMSE: {test_rmse}")

param_grid = {
    "n_estimators": [50, 100],  # Fewer options
    "max_depth": [10, None],   # Simplify depth range
    "min_samples_split": [2, 5],  # Focus on common split values
    "min_samples_leaf": [1, 2],   # Use fewer leaf sizes
}

gridsearch = GridSearchCV(RandomForestRegressor(random_state=12345), param_grid, cv=3)
gridsearch.fit(X_train, y_train)

best_rf_model = gridsearch.best_estimator_

best_test_preds = best_rf_model.predict(X_test)
best_test_rmse = root_mean_squared_error(y_test, best_test_preds)

print(f"Best Test RMSE: {best_test_rmse}")
print(f"Best Parameters: {gridsearch.best_params_}")

tmp = []
tmp2 = []
for i in range(len(best_test_preds)):
    y_test1 = y_test[i] * 0.075
    y_testmax = y_test[i] + y_test1
    y_testmin = y_test[i] - y_test1
    if y_testmin < best_test_preds[i] and best_test_preds[i] <= y_testmax:
        tmp.append(1)
    else:
        tmp.append(0)
        tmp2.append(best_test_preds[i])

predictions_with_names = pd.DataFrame(
    {
        "CPU Name": cpu_names_test.values,
        "Predicted CPU Mark": best_test_preds,
        "Actual CPU Mark": y_test,
        "Accuracy (%)": (tmp.count(1) / len(tmp)) * 100,
    }
)

predictions_with_names.to_csv("../Data/Predictor_RF.csv", index=False)

cmap = sns.cubehelix_palette(as_cmap=True)
f, ax = plt.subplots()
points = ax.scatter(X_test[:, 3], X_test[:, 4], c=y_test, s=50, cmap=cmap)
plt.colorbar(points)
plt.title("Test Data Predictions Visualization")
#plt.show()
