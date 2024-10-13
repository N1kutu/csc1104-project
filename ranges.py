import pandas as pd
import matplotlib

# Use TkAgg for matplotlib if necessary
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("Data.csv")

# Define the bins and labels for the CPU performance categories
bins = [0, 1000, 5000, 20000, 50000, 100000, float('inf')]
labels = [
    "Very Low Performance", 
    "Low Performance", 
    "Mid Performance", 
    "High Performance", 
    "Very High Performance", 
    "Top Tier"
]

# Create a new column "CPU Mark Class" based on the ranges in the "CPU Mark" column
df["CPU Mark Class"] = pd.cut(df["CPU Mark"], bins=bins, labels=labels, right=True)

# Save the updated DataFrame to a new CSV file
df.to_csv("Data_ranges.csv", index=False)

# Optional: Display the first few rows to verify
print(df.head())
