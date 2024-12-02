import pandas as pd

input_df = pd.read_csv("input.txt", sep = "\t", header = None, names = ["loc1", "loc2"])
input_df.sort_values(by=['loc1', 'loc2'], ascending = True)
print(input_df)