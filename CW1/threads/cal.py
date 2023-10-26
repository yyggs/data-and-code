import pandas as pd

# Create an empty list to store all the dataframes
all_data = []

# Loop over each file to read its content
for i in range(11, 21):  # Assuming files are named as data_output_1.csv, data_output_2.csv, ... data_output_10.csv
    filepath = f"data_output_{i}.csv"
    df = pd.read_csv(filepath)
    all_data.append(df)

# Concatenate all the dataframes
combined_data = pd.concat(all_data)

# Calculate the mean for each NumThreads
average_data = combined_data.groupby('NumThreads').mean().reset_index()

# Save the results to a new CSV file
average_data.to_csv("average_output.csv", index=False)
