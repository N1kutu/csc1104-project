import pandas as pd
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

df = pd.read_csv("Data.csv")
# print(df.mean())

print(df.corr())
meanCpu = df.loc[
    (df["No. Sockets"] == 1) & (df["Cores"] == 8) & (df["CPU Mark"] == 8672)
]

# meanCpu.to_csv("MeanCPU.csv")

plt.show()
