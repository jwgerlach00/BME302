import os
import pandas as pd
import plotly.express as px
from clean_data import moving_average


dir_path = 'data/experiment2_trials'
for file in os.listdir(dir_path):
    print(file)
    df = pd.read_excel(f'{dir_path}/{file}')
    
    # Take rolling average
    window = 200
    df = df.rolling(window).mean()
    
    fig = px.line(df, x='time', y=['rms_biceps', 'rms_triceps']) #y=['biceps', 'triceps', 'rms_biceps', 'rms_triceps'])
    fig.write_html('data/ex2_html_plots/{0}.html'.format(file.split('.')[0]))  # Trial 2 is the good one
