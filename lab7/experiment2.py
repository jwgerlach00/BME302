import os
import pandas as pd
import plotly.express as px


# Read in data for each trial and plot
dir_path = 'data/experiment2_trials'
for file in os.listdir(dir_path):
    # Read file
    print(file)
    df = pd.read_excel(f'{dir_path}/{file}')
    
    # Take rolling average to smooth data
    window = 200
    df = df.rolling(window).mean()
    
    # Plot each trial
    fig = px.line(df, x='time', y=['rms_biceps', 'rms_triceps']) #y=['biceps', 'triceps', 'rms_biceps', 'rms_triceps'])
    fig.update_traces(line=dict(width=5))
    fig.update_layout(title_text='Biceps and Triceps Coactivation RMS EMG', title_x=0.5, title_font=dict(size=40),
                      legend=dict(font=dict(size=35)))
    fig.update_xaxes(title_text='Time (s)', title_font=dict(size=40), tickfont=dict(size=30))
    fig.update_yaxes(title_text='RMS EMG (mV-s)', title_font=dict(size=40), tickfont=dict(size=30))
    
    # Show and save plot
    fig.show()
    fig.write_html('data/ex2_html_plots/{0}.html'.format(file.split('.')[0]))  # Trial 2 is the good one
