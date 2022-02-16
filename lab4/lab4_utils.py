import pandas as pd
import sys

sys.path.append('..')
from raw_lab_data import VisualizeRaw


def plot_raw(exercise_num, cols_to_plot):
    """Generates plots for each trial of exercise 2 data.

    Returns:
        object: VisualizeRaw
    """
    df = pd.read_excel(f'data/exercise{exercise_num}.xlsx')
    raw = VisualizeRaw(df, 'time')
    raw.split_trials()
    [raw.plot_trials(f'raw_plots/exercise{exercise_num}', col) for col in cols_to_plot]
    return raw