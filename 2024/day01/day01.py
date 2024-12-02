import pandas as pd

# Read input data frame
input_df = pd.read_csv("input.txt", sep = '\\s+', header = None, names = ['loc1', 'loc2'])

# Sort all columns using apply sort_values
input_df = input_df.apply(lambda x: x.sort_values().values)

# Calculate difference
input_df['diff'] = abs(input_df['loc1'] - input_df['loc2'])
print(input_df)

# Calculate total distance
print(sum(input_df['diff']))
