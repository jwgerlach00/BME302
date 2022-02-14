import sys
import pandas as pd
sys.path.append('..')
from raw_lab_data import VisualizeRaw


# Read data
df = pd.read_excel('labchart_data.xlsx')

raw = VisualizeRaw(df, 'time')
raw.split_trials()
raw.plot_trials('trial_figs_test', 'channel_1')

raw.pull_trial_df(3, '1_element')
raw.pull_trial_df(9, '2_element')
