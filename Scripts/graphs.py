import pandas as pd
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("../Data/Bare_data.csv")

x = df["CPU Mark"]
y = df["Cores"]

xlim = x.min(), x.max()
ylim = y.min(), y.max()

df = pd.read_csv("../Data/Data.csv")
print(df.describe())


# Hex Bin Graph https://matplotlib.org/stable/gallery/statistics/hexbin_demo.html#sphx-glr-gallery-statistics-hexbin-demo-py

'''
fig, (ax0, ax1) = plt.subplots(ncols=2, sharey=True, figsize=(12, 8))

hb = ax0.hexbin(x, y, gridsize=50, cmap="inferno")
ax0.set_title("CPU Mark and CPU Core Distribution")
ax0.set_ylabel("CPU Cores")
ax0.set_xlabel("CPU Mark")

cb = fig.colorbar(hb, label = "Density")

hb = ax1.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
ax1.set(xlim=xlim, ylim=ylim)
ax1.set_title("With a log color scale")
cb = fig.colorbar(hb, ax=ax1, label='Density')
'''

# Fill between and Alpha https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_alpha.html#sphx-glr-gallery-lines-bars-and-markers-fill-between-alpha-py

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

CPUMarkMin = df["CPU Mark"].min()

ax1.plot(df["CPU Mark"], df["CPU Mark"], lw=2)
ax2.fill_between(df["CPU Mark"], CPUMarkMin, df["CPU Mark"], alpha=0.7)

for ax in ax1, ax2:
    ax.grid(True)
    ax.label_outer()

ax1.set_ylabel('CPU Mark')


plt.show()