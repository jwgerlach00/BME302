import pandas as pd
import plotly.express as px
import sys
sys.path.append('..')
from raw_lab_data import VisualizeRaw


df3 = pd.read_excel('data/exercise3.xlsx')

raw = VisualizeRaw(df3, 'time')
# columns = ['pressure', 'cardiomicrophone', 'pulse']
raw.split_trials()
raw.pull_trial_df(2, 'exercise3_trial2')
# raw.plot_columns('raw_plots', '3')