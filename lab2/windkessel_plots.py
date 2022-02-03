import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate


def moving_average(arr, window):
    """Smooths out each column of an array using a moving average.

    Args:
        a (np.Array): Input array to be smoothed.
        window (int): Number of sequential points to average.

    Returns:
        np.Array: Smoothed array.
    """
    length = round(len(arr)/window)
    out = []
    for i in range(length):
        arr_i = arr[window*i:window*(i + 1)]
        arr_i = arr_i.mean(axis=0)
        out.append(arr_i)
    return np.array(out)


def discrete_bounded_integral(y_up, y_lo, x):
    """Computes desired integral using pre-established datapoints and bounds.

    Args:
        y_up (iterable): Y values of the upper bound function.
        y_lo (iterable): Same length as y_up. Y values of the lower bound function.
        x (iterable): Same length as y_up and y_lo. X values.

    Returns:
        float: Integral value.
    """
    upper = integrate.simps(y_up, x)
    lower = integrate.simps(y_lo, x)
    return upper - lower


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

    # Plot Windkessel data without integrals
    # plt.plot(one_element_avg[:, 0], one_element_avg[:, 1], lw=3, color='b')
    # plt.title('One-Element Windkessel', fontsize=24)
    # plt.xlabel('Time (s)', fontsize=16)
    # plt.ylabel('Voltage (mV)', fontsize=16)
    # plt.xticks(fontsize=12)
    # plt.yticks(fontsize=12)
    # plt.grid(True)
    # plt.savefig('1_element_plot.png')
    
    # plt.figure()
    # plt.plot(two_element_avg[:, 0], two_element_avg[:, 1], lw=3, color='r')
    # plt.title('Two-Element Windkessel', fontsize=24)
    # plt.xlabel('Time (s)', fontsize=16)
    # plt.ylabel('Voltage (mV)', fontsize=16)
    # plt.xticks(fontsize=12)
    # plt.yticks(fontsize=12)
    # plt.grid(True)
    # plt.savefig('2_element_plot.png')
    
    # Calculate integrals - experiment
    min_one_el = one_element_avg[0, 1]*np.ones(len(one_element_avg))
    min_two_el = min(two_element_avg[:, 1])*np.ones(len(two_element_avg))
    one_element_integral = discrete_bounded_integral(one_element_avg[:, 1], min_one_el, one_element_avg[:, 0])
    two_element_integral = discrete_bounded_integral(two_element_avg[:, 1], min_two_el, two_element_avg[:, 0])
    
    # Calculate integrals - simulation
    sim_df = pd.read_csv('1-2-element_simulations.csv')
    sim_min = np.zeros(len(sim_df.t1))
    one_sim_integral = discrete_bounded_integral(sim_df.y1, sim_min, sim_df.t1)
    two_sim_integral = discrete_bounded_integral(sim_df.y2, sim_min, sim_df.t2)
    
    # Export integral dataframe
    integrals_df = pd.DataFrame(columns=['one_experiment', 'two_experiment', 'one_sim', 'two_sim'])
    integrals_df.one_experiment = [one_element_integral]
    integrals_df.two_experiment = [two_element_integral]
    integrals_df.one_sim = [one_sim_integral]
    integrals_df.two_sim = [two_sim_integral]
    integrals_df.to_excel('integrals.xlsx')
    
    # Plot integral fills - experiment
    plt.figure()  # 1-element
    plt.plot(one_element_avg[:, 0], one_element_avg[:, 1], lw=3, color='b', label='Smoothed data')
    plt.fill_between(one_element_avg[:, 0], min_one_el, one_element_avg[:, 1], color='orange', label='Integral')
    plt.title('One-Element Windkessel Experiment', fontsize=24)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Voltage (mV)', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.savefig('1_element_exp.png')
    
    plt.figure()  # 2-element
    plt.plot(two_element_avg[:, 0], two_element_avg[:, 1], lw=3, color='r', label='Smoothed data')
    plt.fill_between(two_element_avg[:, 0], min_two_el, two_element_avg[:, 1], label='Integral')
    plt.title('Two-Element Windkessel Experiment', fontsize=24)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Voltage (mV)', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.savefig('2_element_exp.png')
    
    # Plot integral fills - simulation
    plt.figure()  # 1-element
    plt.plot(sim_df.t1, sim_df.y1, lw=3, color='b', label='Simulation data')
    plt.fill_between(sim_df.t1, sim_min, sim_df.y1, color='orange', label='Integral')
    plt.title('One-Element Windkessel Simulation', fontsize=24)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Pressure (mmHg)', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.savefig('1_element_sim.png')
    
    plt.figure()  # 2-element
    plt.plot(sim_df.t2, sim_df.y2, lw=3, color='r', label='Simulation data')
    plt.fill_between(sim_df.t2, sim_min, sim_df.y2, label='Integral')
    plt.title('Two-Element Windkessel Simulation', fontsize=24)
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Pressure (mmHg)', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.savefig('2_element_sim.png')

    # Print peak differences (y-range)
    print(max(sim_df.y1), max(sim_df.y2))
    print(max(one_element_avg[:, 1]) - one_element_avg[0, 1], max(two_element_avg[:, 1]) - two_element_avg[0, 1])
