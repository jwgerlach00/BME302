from matplotlib.cbook import index_of
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from artificial_heart import ArtificialHeart


heart = ArtificialHeart()

# --------------------------------- Plotting --------------------------------- #
# Time arrays
before_filling_time = np.linspace(heart.cycle_start, heart.iso_fill_end, 100)
after_filling_time = [heart.iso_fill_end, heart.period]

# Y values for plots
before_filling_plot = [heart.lv_pressure(t=t) for t in before_filling_time]
after_filling_plot = [heart.lv_pressure(t=t) for t in after_filling_time]

# Plot lines before and after filling
plt.plot(before_filling_time, before_filling_plot, zorder=1, lw=3, color='red', label='Before LV filling')
plt.plot(after_filling_time, after_filling_plot, zorder=1, lw=3, color='orange', label='During and after LV filling')

# Find sp from max of pressure graph
sp = max(before_filling_plot)
sp_time = before_filling_time[before_filling_plot.index(sp)]

# Plot points
plt.scatter(heart.cycle_start, heart.lv_pressure(heart.cycle_start), zorder=2, s=60, color='black',
            label='End diastolic volume')
plt.scatter(heart.iso_eject_end, heart.lv_pressure(heart.iso_eject_end), zorder=2, s=60, color='darkblue',
            label='Diastolic pressure')
plt.scatter(sp_time, sp, zorder=2, s=60, color='purple', label='Systolic pressure')
plt.scatter(0.28, 114.616, s=60, zorder=2, color='blue', label='End systolic pressure')

plt.legend()
plt.xlabel('Time (s)', fontsize=16)
plt.ylabel('Pressure (mm Hg)', fontsize=16)
plt.title('LV Pressure wrt Time', fontsize=24)

plt.show()

# Output data for use in pressure-volume-loop
pd.DataFrame([list(before_filling_time) + after_filling_time, 
              before_filling_plot + after_filling_plot]).transpose().to_excel('pressure.xlsx', header=['time', 'plot'], 
                                                                              index=False)
