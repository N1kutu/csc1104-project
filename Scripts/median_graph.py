import pandas as pd
#import matplotlib

#matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('Data_trimmed10%.csv')

# Plot histogram of 'CPU Mark'
plt.figure(figsize=(10, 6))
ax = df['CPU Mark'].plot(kind='hist', bins=30, alpha=0.7, color='blue', edgecolor='black', grid=False)

# Calculate the median of 'CPU Mark'
median_value = df['CPU Mark'].median()
mean_value = df['CPU Mark'].mean()

# Add a vertical line for the median
plt.axvline(median_value, color='red', linestyle='dashed', linewidth=2, label='Median')
plt.axvline(mean_value, color='orange', linestyle='solid', linewidth=1, label='Mean')

# Customize the plot
plt.title('Histogram of CPU Mark with Median Line')
plt.xlabel('CPU Mark')
plt.ylabel('Frequency')
plt.legend()
#plt.grid(axis='y', alpha=0.75)

# Save the plot to a file
plt.savefig('cpu_mark_histogram10%.png', dpi=300)

# Optionally, close the plot
#plt.show()
plt.close()

