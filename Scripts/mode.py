import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("Data_ranges.csv")

# Drop the first column
df_filtered = df.iloc[:, 1:]

# Calculate the mode of the remaining columns
mode_values = df_filtered.mode()

# Print the column names and their corresponding mode values
print("\nMode values of the columns (excluding the first column):")
for column in mode_values.columns:
    # Get the first mode value for each column
    mode_value = mode_values[column][0]
    print(f"{column:<30}: {mode_value}")
