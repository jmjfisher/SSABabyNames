# importing libraries
import pandas as pd
import os
  
file = os.path.join('C:/Users/JohnMark/Desktop/baby_names/output', 'names_append.csv')

df = pd.read_csv(file, header=0)
df = df.drop(columns=['births','rank','year'])
df = df.drop_duplicates()

df.to_csv('C:/Users/JohnMark/Desktop/baby_names/output/distinct_names.csv', index=False)
