import os
import pandas as pd


"""
    Reads in each file in directory and extract comments for visualization purposes
"""


out_df = pd.DataFrame(columns=['file', 'comment', 'index'])

dir_path = 'data/experiment4_trials'
for file in os.listdir(dir_path):
    df = pd.read_excel(f'{dir_path}/{file}')
    out_df.loc[len(out_df)] = [file, list(df['comments'].dropna())[0], list(df['comments'].dropna().index)[0]]
    out_df.sort_values(by='index', inplace=True)
    out_df.to_excel('lab7_comments.xlsx', index=False)
    
print(out_df)
