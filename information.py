import pandas as pd
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

df = pd.read_csv("Data.csv")

print(df.describe())
# print(df.mean())
# print(df["Cores"].hist())
meanCpu = df.loc[
    (df["No. Sockets"] == 1) & (df["Cores"] == 8) & (df["CPU Mark"] == 8672)
]

meanCpu.to_csv("MeanCPU.csv")

"""
x = df["Cores"]
y = df["CPU Name"]
plt.scatter(x, y, label= "stars", color= "m",  
            marker= "*", s=30) 
"""

# plt.show()
