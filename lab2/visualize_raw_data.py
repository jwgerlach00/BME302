import pandas as pd
import plotly.express as px


# Read data
df = pd.read_excel('labchart_data.xlsx')
time = df.time
channel_1 = df.channel_1

# Find all indices where time resets to 0s (start of trial)
start_indices = df.where(df.time == 0).dropna().index.tolist()

# Break data into trials
trial_data = []
for i, start in enumerate(start_indices):
    try:
        end = start_indices[i + 1]
        trial_data.append(df.iloc[start:end])
    except:
        pass

# Ensure that all the data is accounted for
assert len(start_indices) == len(trial_data) + 1

# Plot each trial to visualize
for i, trial in enumerate(trial_data):
    fig = px.line(x=trial.time, y=trial.channel_1)
    fig.write_html('trial_figures/trial{0}.html'.format(i))

# Write eyeballed selected trials
trial_data[3].to_excel('1_element.xlsx', index=False)
trial_data[9].to_excel('2_element.xlsx', index=False)
