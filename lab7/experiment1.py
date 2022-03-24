import pandas as pd
import plotly.express as px


df = pd.read_excel('data/experiment1.xlsx')

fig = px.line(df, y='data')
fig.show()