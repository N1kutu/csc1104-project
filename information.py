import pandas as pd
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt

df = pd.read_csv('Updated_Test.csv')

print(df.describe())
print(df['Cores'].hist())

'''
x = df["Cores"]
y = df["CPU Name"]
plt.scatter(x, y, label= "stars", color= "m",  
            marker= "*", s=30) 
'''

plt.show()