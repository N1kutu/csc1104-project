import pandas as pd
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

df = pd.read_csv("Data.csv")
df2 = pd.read_csv("Data_trimmed10%.csv")
# print(df.mean())

# print(df["Cores"].hist(alpha=0.9))
print(df2["Cores"].hist(alpha=0.9))
meanCpu = df.loc[
    (df["No. Sockets"] == 1) & (df["Cores"] == 8) & (df["CPU Mark"] == 8672)
]

# meanCpu.to_csv("MeanCPU.csv")

plt.show()
