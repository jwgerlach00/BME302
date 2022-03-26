import sys
import pandas as pd
from raw_lab_data import VisualizeRaw


# Read data
df = pd.read_excel('data/exercise1.xlsx')
print(df.columns)

raw = VisualizeRaw(df, 'time')
raw.split_trials()

trial_data = raw.trial_data

print(trial_data)

raw.plot_trials('data/exercise1_plots', 'rms_biceps')
raw.plot_trials('data/exercise1_plots', 'rms_triceps')

for i, df in enumerate(trial_data):
    df.to_excel(f'data/exercise1/trial{i}.xlsx', index=False)