import pandas as pd
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt


df = pd.read_csv('Data.csv')

df_filtered = df[~df["TDP (W)"].astype(str).str.contains("NA", case=False, na=False)]

df_filtered['CPU Mark'] = [int(x.replace(",", "")) for x in df_filtered['CPU Mark']]

df_filtered['Power Performance'] = (df_filtered['CPU Mark'] / df_filtered['TDP (W)']).round(2)
df_filtered.to_csv('Test.csv', index=False)


print(df_filtered.describe())
print(df_filtered['Cores'].hist())

'''
x = df["Cores"]
y = df["CPU Name"]
plt.scatter(x, y, label= "stars", color= "m",  
            marker= "*", s=30) 
'''

plt.show()