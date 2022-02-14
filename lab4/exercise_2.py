import pandas as pd
import matplotlib.pyplot as plt
import sys

sys.path.append('..')
from raw_lab_data import VisualizeRaw


def plot_raw():
    """Generates plots for each trial of exercise 2 data.

    Returns:
        object: VisualizeRaw
    """
    df = pd.read_excel('data/exercise2.xlsx')
    raw = VisualizeRaw(df, 'time')
    raw.split_trials()
    raw.plot_trials('raw_plots', 'pulse')
    raw.plot_trials('raw_plots', 'pressure')
    raw.pull_trial_df(2, 'exercise2_trial2')
    return raw


if __name__ == '__main__':
    # Hard-coded timestamps
    start_inx = 46281
    end_inx = 103746
    systole_inx = 73987
    diastole_inx = 97987
    
    # Import and clean data
    df = pd.read_excel('exercise2_trial2.xlsx')
    cropped_df = df.iloc[start_inx:end_inx]
    cropped_df.time = cropped_df.time - cropped_df.time.iloc[0]
    
    # Create plotting ranges
    systole_x = 2*[df.time.iloc[systole_inx]]
    diastole_x = 2*[df.time.iloc[diastole_inx]]
    
    # Plot pressure
    pulse_y = [min(cropped_df.pressure), max(cropped_df.pressure)]
    plt.plot(cropped_df.time, cropped_df.pressure, color='k')
    plt.plot(systole_x, pulse_y, lw=3, color='b')
    plt.plot(diastole_x, pulse_y, lw=3, color='r')
    plt.title('Pressure as a Function of Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Pressure (mmHg)')
    plt.legend(['Signal', 'Systole', 'Diastole'])
    plt.grid()
    plt.show()
    
    # Plot pulse
    pulse_y = [min(cropped_df.pulse), max(cropped_df.pulse)]
    plt.plot(cropped_df.time, cropped_df.pulse, color='k')
    plt.plot(systole_x, pulse_y, lw=3, color='b')
    plt.plot(diastole_x, pulse_y, lw=3, color='r')
    plt.title('Finger Pulse as a Function of Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Pulse (volts)')
    plt.legend(['Signal', 'Systole', 'Diastole'])
    plt.grid()
    plt.show()
