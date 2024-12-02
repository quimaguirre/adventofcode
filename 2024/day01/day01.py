import pandas as pd

# Read input data frame
input_df = pd.read_csv("input.txt", sep = '\\s+', header = None, names = ['loc1', 'loc2'])

### PART 1 ###

# Sort all columns using apply sort_values
input_df = input_df.apply(lambda x: x.sort_values().values)

# Calculate difference
input_df['diff'] = abs(input_df['loc1'] - input_df['loc2'])
print(input_df)

# Calculate total distance
print(sum(input_df['diff']))


### PART 2 ###

# Count values in loc 2
loc2_counts = input_df['loc2'].value_counts().rename_axis('loc2').reset_index(name='counts')

# Merge counts with loc1
similarity_df = pd.merge(input_df[["loc1"]], loc2_counts, how = "inner", left_on = 'loc1', right_on = 'loc2')[['loc1', 'counts']]

# Calculate similarity score
similarity_df['similarity'] = similarity_df['loc1'] * similarity_df['counts']

# Calculate total similarity
print(sum(similarity_df['similarity']))
