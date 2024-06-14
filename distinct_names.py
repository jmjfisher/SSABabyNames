# importing libraries
import pandas as pd
import glob
import os
  
# merging the files
joined_files = os.path.join('C:/Users/JohnMark/Desktop/baby_names/names', '*.TXT')
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)

df = pd.read_csv(joined_list[0])
df.columns = ['name','sex','births']
df['rank'] = df.groupby('sex')['births'].rank(method='min', ascending=False)
df['year'] = joined_list[0][-8:-4]

i=1
print("starting loop")
while i < len(joined_list):
    df2 = pd.read_csv(joined_list[i])
    df2.columns = ['name','sex','births']
    df2['rank'] = df2.groupby('sex')['births'].rank(method='min', ascending=False)
    df2['year'] = joined_list[i][-8:-4]
    df = pd.concat([df, df2])
    i+=1

df['rank'] = df['rank'].astype(int)
df['year'] = df['year'].astype(int)
df.to_csv('C:/Users/JohnMark/Desktop/baby_names/output/names_append.csv', index=False)
print("done")
