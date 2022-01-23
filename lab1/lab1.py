import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('windkessel_plot_data.xlsx')

plt.plot(df.tt3, df.yt3)
plt.plot(df.tt3, df.yt3_small)
plt.plot(df.tt3, df.yt3_big)
plt.show()