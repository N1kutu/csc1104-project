import pandas as pd
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import scipy.stats as stats
import pylab as py

df3 = pd.read_csv("../Data/Data.csv")
df = pd.read_csv("../Data/Test.csv")
df2 = pd.read_csv("../Data/Predictor.csv")

a = df3["No. Sockets"]
b = df3["Cores"]
c = df3["Thread Mark"]
d = df3["TDP (W)"]
e = df3["Power Performance"]
x = df["Actual CPU Mark"]
y = df2["Predicted CPU Mark"]
z = df3["CPU Mark"]

xlim = x.min(), x.max()
ylim = y.min(), y.max()


'''
# Boxplots comparing actual vs predicted values
plt.boxplot([x, y], tick_labels=["Acutal CPU Mark", "Predicted CPU Mark"])

plt.title("Actual CPU Mark vs Predicted CPU Mark")
plt.ylabel("CPU Mark")

# Plots comparing actual vs predicted values
ax[0].plot(x)
ax[0].set_title("Actual CPU Mark")
ax[1].plot(y)
ax[1].set_title("Predicted CPU Mark")

# Scatter plots comparing actual vs predicted values
for color in ['tab:blue']:
    n = 849
    x = x
    scale = 100.0 * np.random.rand(n)
    ax[0].scatter(x, y, c=color, s=scale, label="Actual CPU Values",
               alpha=0.5, edgecolors='none')

for color in ['tab:red']:
    n = 849
    y = y
    scale = 100.0 * np.random.rand(n)
    ax[1].scatter(x, y, c=color, s=scale, label="Predicted CPU Values",
               alpha=0.5, edgecolors='none')

ax[0].legend()
ax[0].grid(True)
ax[1].legend()
ax[1].grid(True)

# Bar charts comparing actual versus predicted values
X_axis = np.arange(len(x)) 

plt.bar(X_axis - 0.2, x, 0.4, label = "Actual")
plt.bar(X_axis + 0.2, y, 0.4, label = "Predicted")
  
plt.ylabel("CPU Mark") 
plt.title("Actual CPU Mark vs Predicted CPU Mark") 
plt.legend() 



# Probability plot https://www.statology.org/q-q-plot-python/
stats.probplot(z, dist="norm", plot=py, )
py.show() 

z = sorted(z)
fig, ax = plt.subplots()

z_list = []
for i in range(len(z)):
    z_list.append(i)

for color in ['tab:blue']:
    n = len(z)
    x = z
    scale = 100.0 * np.random.rand(n)
    ax.scatter(x, z_list, c=color, s=scale, label="CPU Mark",
               alpha=0.5, edgecolors='none')

ax.legend()
ax.grid(True)

a = sorted(a)
fig, ax = plt.subplots()

a_list = []
for i in range(len(a)):
    a_list.append(i)

for color in ['tab:red']:
    n = len(a)
    x = a
    scale = 10.0 * np.random.rand(n)
    ax.scatter(x, a_list, c=color, s=scale, label="No. Sockets",
               alpha=0.5, edgecolors='none')

ax.legend()

b = sorted(b)
fig, ax = plt.subplots()

b_list = []
for i in range(len(b)):
    b_list.append(i)

for color in ['tab:green']:
    n = len(b)
    x = b
    scale = 10.0 * np.random.rand(n)
    ax.scatter(x, b_list, c=color, s=scale, label="Cores",
               alpha=0.5, edgecolors='none')

ax.legend()

c = sorted(c)
fig, ax = plt.subplots()

c_list = []
for i in range(len(c)):
    c_list.append(i)

for color in ['tab:orange']:
    n = len(c)
    x = c
    scale = 10.0 * np.random.rand(n)
    ax.scatter(x, c_list, c=color, s=scale, label="Thread Mark",
               alpha=0.5, edgecolors='none')

ax.legend()

d = sorted(d)
fig, ax = plt.subplots()

d_list = []
for i in range(len(d)):
    d_list.append(i)

for color in ['tab:purple']:
    n = len(d)
    x = d
    scale = 10.0 * np.random.rand(n)
    ax.scatter(x, d_list, c=color, s=scale, label="TDP (W)",
               alpha=0.5, edgecolors='none')

ax.legend()

'''

e = sorted(e)
fig, ax = plt.subplots()

e_list = []
for i in range(len(e)):
    e_list.append(i)

for color in ['tab:pink']:
    n = len(e)
    x = e
    scale = 10.0 * np.random.rand(n)
    ax.scatter(x, e_list, c=color, s=scale, label="Power Performance",
               alpha=0.5, edgecolors='none')

ax.legend()

plt.show()