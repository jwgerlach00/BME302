import os
import pandas as pd
import plotly.express as px


dir_path = 'data/experiment2_trials'
for file in os.listdir(dir_path):
    print(file)
    df = pd.read_excel(f'{dir_path}/{file}')
    fig = px.line(df, x='time', y=['biceps', 'triceps', 'rms_biceps', 'rms_triceps'])
    fig.show()  # Trial 0 is the good one
