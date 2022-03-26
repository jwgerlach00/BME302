import os
import pandas as pd
import plotly.express as px


dir_path = 'data/experiment2_trials'
for file in os.listdir(dir_path):
    print(file)
    df = pd.read_excel(f'{dir_path}/{file}')
    
    
    # Take rolling average
    window = 200
    df = df.rolling(window).mean()
    
    fig = px.line(df, x='time', y=['rms_biceps', 'rms_triceps']) #y=['biceps', 'triceps', 'rms_biceps', 'rms_triceps'])
    # fig.update_traces=dict(line=dict(width=10))
    fig.update_layout(title_text='Biceps and Triceps Coactivation RMS EMG', title_x=0.5, title_font=dict(size=40),
                      legend=dict(font=dict(size=30)))
    fig.update_xaxes(title_text='Time (s)', title_font=dict(size=30), tickfont=dict(size=20))
    fig.update_yaxes(title_text='RMS EMG (mV)', title_font=dict(size=30), tickfont=dict(size=20))
    fig.show()
    # fig.write_html('data/ex2_html_plots/{0}.html'.format(file.split('.')[0]))  # Trial 2 is the good one
