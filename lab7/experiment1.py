import os
import pandas as pd
import plotly.express as px


# List filenames
dir_path = 'data/exercise1'
files = os.listdir(dir_path)
files.sort()

# Create dataframes from files
dataframes = []
for file, lbs in zip(files, [2, 5, 8, 10]):
    print(file)
    df = pd.read_excel(f'{dir_path}/{file}')
    df['category'] = file.split('.')[0] = f'{lbs} lbs'
    dataframes.append(df)

# Concatenate dataframes
total_plotly_data = pd.concat(dataframes)

# Plot
fig = px.line(total_plotly_data, x='time', y='rms_biceps', color='category')
fig.update_traces(line=dict(width=10))
fig.update_layout(title_text='Biceps RMS EMG as a Function of Time and Load', title_x=0.5, title_font=dict(size=40),
                    legend=dict(title='Load', font=dict(size=35)))
fig.update_xaxes(title_text='Time (s)', title_font=dict(size=40), tickfont=dict(size=30))
fig.update_yaxes(title_text='RMS EMG (mV-s)', title_font=dict(size=40), tickfont=dict(size=30))

# Download plots
fig.write_html('data/ex2_html_plots/{0}.html'.format(file.split('.')[0]))  # Trial 2 is the good one
