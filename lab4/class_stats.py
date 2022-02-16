import pandas as pd
from scipy.stats import ttest_rel
import numpy as np


# Read and clear data
df = pd.read_excel('data/class_data.xlsx')

# Drop all rows with at least 1 NaN value
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.columns)

# T-test statistics
p_val_sys_pulse = ttest_rel(df.sys_bp_auscultation, df.sys_bp_pulse).pvalue
p_val_sys_mic = ttest_rel(df.sys_bp_auscultation, df.sys_bp_mic).pvalue

p_val_dia_pulse = ttest_rel(df.dia_bp_auscultation, df.dia_bp_pulse).pvalue
p_val_dia_mic = ttest_rel(df.dia_bp_auscultation, df.dia_bp_mic).pvalue

# Calculate means
mean_sys_auscultation, mean_sys_pulse, mean_sys_mic = df.sys_bp_auscultation.mean(), df.sys_bp_pulse.mean(), \
    df.sys_bp_mic.mean()
mean_dia_auscultation, mean_dia_pulse, mean_dia_mic = df.dia_bp_auscultation.mean(), df.dia_bp_pulse.mean(), \
    df.dia_bp_mic.mean()
    
# Calculate stds
std_sys_auscultation, std_sys_pulse, std_sys_mic = df.sys_bp_auscultation.std(), df.sys_bp_pulse.std(), \
    df.sys_bp_mic.std()
std_dia_auscultation, std_dia_pulse, std_dia_mic = df.dia_bp_auscultation.std(), df.dia_bp_pulse.std(), \
    df.dia_bp_mic.std()

stats_df = pd.DataFrame({
    'measure': ['p_val', 'mean', 'std'],
    'systolic_auscultation': [np.nan, mean_sys_auscultation, std_sys_auscultation],
    'systolic_pulse': [p_val_sys_pulse, mean_sys_pulse, std_sys_pulse], 
    'systolic_mic': [p_val_sys_mic, mean_sys_mic, std_sys_mic],
    'diastolic_auscultation': [np.nan, mean_dia_auscultation, std_dia_auscultation], 
    'diastolic_pulse': [p_val_dia_pulse, mean_dia_pulse, std_dia_pulse], 
    'diastolic_mic': [p_val_dia_mic, mean_dia_mic, std_dia_mic],
})

stats_df.to_excel('out_data/class_stats.xlsx', index=False)