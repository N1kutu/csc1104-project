import pandas as pd
import matplotlib

# Use TkAgg for matplotlib if necessary
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("Data_trimmed10%.csv")

# Display summary statistics of the DataFrame
print(df.describe())

# Calculate and print the mean of all numerical columns
mean_values = df.mean(numeric_only=True)
print("\nMean values of the numerical columns:")
print(mean_values)

# Plot data (currently commented out for demonstration purposes)
"""
x = df["Cores"]
y = df["CPU Name"]
plt.scatter(x, y, label="CPU Data", color="m", marker="*", s=30)

# Display the plot
plt.show()
"""
