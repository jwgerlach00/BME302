from doctest import testmod
import os
import pandas as pd
import plotly.express as px


dir_path = 'data/experiment4_trials'
for file in os.listdir(dir_path):
    print(file)
    df = pd.read_excel(f'{dir_path}/{file}')
    fig = px.line(df, x='time', y='emg')
    fig.write_html('data/ex4_html_plots/{0}.html'.format(file.split('.')[0]))
