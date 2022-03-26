import os
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt



dir_path = 'data/exercise1'
files = os.listdir(dir_path)
files.sort()
dataframes = []
for file, lbs in zip(files, [2, 5, 8, 10]):
    print(file)
    df = pd.read_excel(f'{dir_path}/{file}')
    df['category'] = file.split('.')[0] = f'{lbs} lbs'
    dataframes.append(df)
    
total_plotly_data = pd.concat(dataframes)
print(total_plotly_data)


fig = px.line(total_plotly_data, x='time', y='rms_biceps', color='category') #y=['biceps', 'triceps', 'rms_biceps', 'rms_triceps'])
fig.update_traces(line=dict(width=10))
fig.update_layout(title_text='Biceps RMS EMG as a Function of Time and Load', title_x=0.5, title_font=dict(size=40),
                    legend=dict(title='Load', font=dict(size=35)))
fig.update_xaxes(title_text='Time (s)', title_font=dict(size=40), tickfont=dict(size=30))
fig.update_yaxes(title_text='RMS EMG (mV)', title_font=dict(size=40), tickfont=dict(size=30))
# fig.write_html('data/ex2_html_plots/{0}.html'.format(file.split('.')[0]))  # Trial 2 is the good one
fig.show()
# Plot
# fig = plt.figure()
# fig.subplots_adjust(bottom=0.15, left=0.15, right=0.85)
# plt.plot(
#     dataframes[0]['time'], dataframes[0]['rms_biceps'],
#     dataframes[1]['time'], dataframes[1]['rms_biceps'],
#     dataframes[2]['time'], dataframes[2]['rms_biceps'],
#     dataframes[3]['time'], dataframes[3]['rms_biceps'],
#     color='purple', zorder=2, lw=4, label='max EMG'
# )
# plt.title('Max EMG as a Function of Stimulus', fontsize=24)
# plt.xlabel('Stimulus (mA)', fontsize=20)
# plt.ylabel('EMG (mV)', fontsize=20)
# plt.xticks(fontsize=16)
# plt.yticks(fontsize=16)
# plt.legend(fontsize=18)
# plt.grid()
# plt.show()
# plt.savefig('data/max_emg_vs_stim.png')
