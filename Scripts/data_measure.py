from statistics import pvariance
from statistics import stdev
from statistics import linear_regression
import pandas as pd

import numpy as np

df = pd.read_csv("../Data/Data.csv")
v = df["No. Sockets"]
w = df["Cores"]
x = df["CPU Mark"]
y = df["Thread Mark"]
z = df["Power Performance"]
u = df["TDP (W)"]

print("NO.SOCKETS")
print(pvariance(v))
print(stdev(v))
v_count = []
for i in range(len(v)):
    v_count.append(i)
slope, intercept = linear_regression(v,v_count)
print(round(slope * 10 + intercept))
print("\n")

print("CORES")
print(pvariance(w))
print(stdev(w))
w_count = []
for i in range(len(w)):
    w_count.append(i)
slope, intercept = linear_regression(w,w_count)
print(round(slope * 256 + intercept))
print("\n")

print("CPU MARK")
print(pvariance(x))
print(stdev(x))
x_count = []
for i in range(len(x)):
    x_count.append(i)
slope, intercept = linear_regression(x,x_count)
print(round(slope * 200000 + intercept))
print("\n")

print("THREAD MARK")
print(pvariance(y))
print(stdev(y))
y_count = []
for i in range(len(y)):
    y_count.append(i)
slope, intercept = linear_regression(y,y_count)
print(round(slope * 4000 + intercept))
print("\n")

print("TDP")
print(pvariance(u))
print(stdev(u))
u_count = []
for i in range(len(u)):
    u_count.append(i)
slope, intercept = linear_regression(u,u_count)
print(round(slope * 500 + intercept))
print("\n")

print("POWER PERFORMANCE")
print(pvariance(z))
print(stdev(z))
z_count = []
for i in range(len(z)):
    z_count.append(i)
slope, intercept = linear_regression(z,z_count)
print(round(slope * 2000 + intercept))
print("\n")

q1 = np.percentile(v, 25)
q3 = np.percentile(v, 75)
iqr = q3 - q1
quartile_deviation = (q3 - q1) / 2
print("NO SOCKETS Interquartile Range (IQR):", iqr)
print("NO SOCKETS Quartile Deviation:", quartile_deviation)
print("\n")

q1 = np.percentile(w, 25)
q3 = np.percentile(w, 75)
iqr = q3 - q1
quartile_deviation = (q3 - q1) / 2
print("CORES Interquartile Range (IQR):", iqr)
print("CORES Quartile Deviation:", quartile_deviation)
print("\n")

q1 = np.percentile(x, 25)
q3 = np.percentile(x, 75)
iqr = q3 - q1
quartile_deviation = (q3 - q1) / 2
print("CPU MARK Interquartile Range (IQR):", iqr)
print("CPU MARK Quartile Deviation:", quartile_deviation)
print("\n")

q1 = np.percentile(y, 25)
q3 = np.percentile(y, 75)
iqr = q3 - q1
quartile_deviation = (q3 - q1) / 2
print("THREAD MARK Interquartile Range (IQR):", iqr)
print("THREAD MARK Quartile Deviation:", quartile_deviation)
print("\n")

q1 = np.percentile(u, 25)
q3 = np.percentile(u, 75)
iqr = q3 - q1
quartile_deviation = (q3 - q1) / 2
print("TDP Interquartile Range (IQR):", iqr)
print("TDP Quartile Deviation:", quartile_deviation)
print("\n")

q1 = np.percentile(z, 25)
q3 = np.percentile(z, 75)
iqr = q3 - q1
quartile_deviation = (q3 - q1) / 2
print("POWER PERFORMANCE Interquartile Range (IQR):", iqr)
print("POWER PERFORMANCE Quartile Deviation:", quartile_deviation)
print("\n")