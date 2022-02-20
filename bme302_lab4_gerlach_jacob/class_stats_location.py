import pandas as pd
from scipy.stats import ttest_rel
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Read and clear data
    df = pd.read_excel('data/class_data.xlsx')

    # Drop all rows with at least 1 NaN value
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)

    # T-test statistics
    p_val_forearm = ttest_rel(df.sys_bp_upper_arm, df.sys_bp_forearm).pvalue
    p_val_leg_sit = ttest_rel(df.sys_bp_upper_arm, df.sys_bp_leg_sit).pvalue
    p_val_leg_stand = ttest_rel(df.sys_bp_upper_arm, df.sys_bp_leg_stand).pvalue

    # Calculate means
    mean_upper_arm, mean_forearm, mean_leg_sit, mean_leg_stand = df.sys_bp_upper_arm.mean(), df.sys_bp_forearm.mean(), \
        df.sys_bp_leg_sit.mean(), df.sys_bp_leg_stand.mean()

    # Calculate stds
    std_upper_arm, std_forearm, std_leg_sit, std_leg_stand = df.sys_bp_upper_arm.std(), df.sys_bp_forearm.std(), \
        df.sys_bp_leg_sit.std(), df.sys_bp_leg_stand.std()

    stats_df = pd.DataFrame({
        'measure': ['p_val', 'mean', 'std'],
        'upper_arm': [np.nan, mean_upper_arm, std_upper_arm],
        'forearm': [p_val_forearm, mean_forearm, std_forearm],
        'leg_sitting': [p_val_leg_sit, mean_leg_sit, std_leg_sit],
        'leg_standing': [p_val_leg_stand, mean_leg_stand, std_leg_stand]
    })
    print(stats_df)

    # Export stats
    stats_df.to_excel('out_data/class_stats_location.xlsx', index=False)
    means = stats_df.iloc[1, 1:]
    yerr = stats_df.iloc[2, 1:]
    
    xticks = list(stats_df.keys()[1:])

    plt.bar(list(range(len(means))), means, yerr=yerr, error_kw=dict(lw=3, capsize=5, capthick=2), color='r', zorder=2)
    plt.title('Blood Pressure as a Function of Location', size=24)
    plt.xticks(list(range(4)), xticks, rotation=45, ha='right', fontsize=16)
    plt.yticks(list(range(0, 180, 40)), fontsize=16)
    xlabel = plt.xlabel('Measurement location', fontsize=18)
    plt.ylabel('Average BP (mmHg)', fontsize=18)
    plt.grid()
    
    plt.savefig('out_data/class_location_bar.png', bbox_extra_artists=(xlabel,), bbox_inches='tight')
