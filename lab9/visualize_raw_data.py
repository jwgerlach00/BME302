import pandas as pd
from raw_lab_data import VisualizeRaw


# Read data
df = pd.read_excel('exercise3.xlsx')
print(df.columns)

raw = VisualizeRaw(df, 'time')
raw.split_trials()

trial_data = raw.trial_data

print(trial_data)

raw.plot_trials('exercise3/plots', 'flow')

for i, df in enumerate(trial_data):
    df.to_excel(f'exercise3/data/flow_trial{i}.xlsx', index=False)
