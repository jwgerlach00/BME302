import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('data/group_data.xlsx')

print(df)

fig = plt.figure()
fig.subplots_adjust(bottom=0.15)
plt.hist(df['nerve conduction velocity (m/s)'], zorder=2, color='purple')
plt.title('Nerve Conduction Velocity', fontsize=26)
plt.xlabel('Velocity (m/s)', fontsize=20)
plt.ylabel('Frequency', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.grid()
plt.savefig('data/nerve_conduction_velocity.png')

print(df['nerve conduction velocity (m/s)'].std())