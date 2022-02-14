import pandas as pd
import plotly.express as px


class VisualizeRaw:
    def __init__(self, df, time_col) -> None:
        self.df = df
        self.time = time_col
        self.trial_data = []
        
    def start_indices(self):
        # Find all indices where time resets to 0s (start of trial)
        print(self.df.where(self.df[self.time] == 0).dropna().index.tolist())
        return self.df.where(self.df[self.time] == 0).dropna().index.tolist()
    
    def split_trials(self):
        # Break data into trials
        start_indices = self.start_indices()
        
        for i, start_inx in enumerate(start_indices):
            try:
                end_inx = start_indices[i + 1] if i != len(start_indices) - 1 else len(self.df)
                self.trial_data.append(self.df.iloc[start_inx:end_inx])
            except Exception as e:
                print(start_inx, e)
                pass
        
        # Ensure that all the data is accounted for
        assert len(start_indices) == len(self.trial_data)
    
    def plot_trials(self, dir_path, column):
        # Plot each trial to visualize
        for i, trial in enumerate(self.trial_data):
            fig = px.line(x=trial[self.time], y=trial[column])
            fig.write_html('{0}/{1}_trial{2}.html'.format(dir_path, column, i))
            
    def plot_columns(self, dir_path, ex_num):
        columns = list(self.df.columns)
        columns.pop(columns.index(self.time))
        figs = [px.line(x=self.df[self.time], y=self.df[col]) for col in columns]
        [x.write_html('{0}/{1}{2}.html'.format(dir_path, col, ex_num)) for x, col in zip(figs, columns)]
            
    def pull_trial_df(self, trial_num, filename, ext='xlsx'):
        if ext == 'xlsx':
            return self.trial_data[trial_num].to_excel(f'{filename}.xlsx', index=False)
        elif ext == 'csv':
            return self.trial_data[trial_num].to_csv(f'{filename}.csv', index=False)
        else:
            raise f'{ext} is not a recognized file extension.'
