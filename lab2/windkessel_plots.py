import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def moving_average(arr, window):
    """Smooths out each column of an array using a moving average

    Args:
        a (np.Array): Input array to be smoothed
        window (int): Number of sequential points to average

    Returns:
        np.Array: Smoothed array
    """
    length = round(len(arr)/window)
    out = []
    for i in range(length):
        arr_i = arr[window*i:window*(i + 1)]
        arr_i = arr_i.mean(axis=0)
        out.append(arr_i)
    return np.array(out)


if __name__ == '__main__':
    # Read in trial data
    one_element_df = pd.read_excel('windkessel_plot_data/1_element.xlsx').dropna()  # Data for one-element Windkessel
    two_element_df = pd.read_excel('windkessel_plot_data/2_element.xlsx').dropna()  # Data for two-element Windkessel

    # Crop the data (eyeballed)
    one_element_df = one_element_df.iloc[round(0.35*len(one_element_df)):round(0.9*len(one_element_df))]
    two_element_df = two_element_df.iloc[round(0.05*len(two_element_df)):round(0.9*len(two_element_df))]

    # Take a moving average of the data
    one_element_avg = moving_average(one_element_df.to_numpy(), 50)
    two_element_avg = moving_average(two_element_df.to_numpy(), 100)

    # Plot Windkessel data
    plt.plot(one_element_avg[:, 0], one_element_avg[:, 1], lw=3, color='b')
    plt.title('One-Element Windkessel', fontsize=24)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Voltage (mV)', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.savefig('1_element_plot.png')
    
    plt.figure()
    plt.plot(two_element_avg[:, 0], two_element_avg[:, 1], lw=3, color='r')
    plt.title('Two-Element Windkessel', fontsize=24)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Voltage (mV)', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.savefig('2_element_plot.png')
