# importing libraries
import pandas as pd
import glob
import os
  
# merging the files
joined_files = os.path.join('C:/Users/JohnMark/Desktop/baby_names/namesbystate', '*.TXT')
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)

df = pd.read_csv(joined_list[0])
df.columns = ['state','sex','year','name','births']
df['rank'] = df.groupby(['sex','year'])['births'].rank(method='min', ascending=False)

i=1
print("running loop")
while i < len(joined_list):
    df2 = pd.read_csv(joined_list[i])
    df2.columns = ['state','sex','year','name','births']
    df2['rank'] = df2.groupby(['sex','year'])['births'].rank(method='min', ascending=False)
    df = pd.concat([df, df2])
    i+=1

df['rank'] = df['rank'].astype(int)
df.to_csv('C:/Users/JohnMark/Desktop/baby_names/output/namesbystate_append.csv', index=False)
print("done")
