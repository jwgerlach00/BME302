import numpy as np


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