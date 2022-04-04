from doctest import testmod
import os
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt


max_set1 = np.array([])
dir_path = 'data/experiment4_trials_set1'
files = os.listdir(dir_path)
files.sort()
for file in files:
    print(file)
    df = pd.read_excel(f'{dir_path}/{file}')
    max_set1 = np.append(max_set1, df['emg'].max())
    # fig = px.line(df, x='time', y='emg')
    # fig.write_html('data/ex4_html_plots/{0}.html'.format(file.split('.')[0]))
   
max_set2 = np.array([])
dir_path = 'data/experiment4_trials_set2'
files = os.listdir(dir_path)
files.sort()
for file in files:
    print(file)
    df = pd.read_excel(f'{dir_path}/{file}')
    max_set2 = np.append(max_set2, df['emg'].max())
    
max_avg = (max_set1 + max_set2)/2

currents = np.arange(6, 22, 2)

z = np.polyfit(currents, max_avg, 1)
p = np.poly1d(z)
eq = [round(x, 4) for x in z]

# Plot
fig = plt.figure()
fig.subplots_adjust(bottom=0.15, left=0.15, right=0.85)
plt.scatter(currents, max_avg, color='purple', zorder=2, lw=4, label='max EMG')
plt.plot(currents, p(currents), 'r--', label='1st order fit')
plt.text(8.5, 0.105, f'{eq[0]}x + {eq[1]}', fontsize=14, color='r')
plt.title('Max EMG as a Function of Stimulus', fontsize=24)
plt.xlabel('Stimulus (mA)', fontsize=20)
plt.ylabel('RMS EMG (mV-s)', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=18)
plt.grid()
plt.savefig('data/max_emg_vs_stim.png')
