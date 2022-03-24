import os
import pandas as pd


dir_path = 'data/experiment4_trials'
for file in os.listdir(dir_path):
    df = pd.read_excel(f'{dir_path}/{file}')
    print(file, df['comments'].dropna())
