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

plt.plot(before_filling_time, before_filling_plot, zorder=1, lw=3, color='red')
plt.plot(after_filling_time, after_filling_plot, zorder=1, lw=3, color='orange')

plt.scatter(heart.cycle_start, heart.lv_pressure(heart.cycle_start), zorder=2, s=60, color='black')
plt.scatter(heart.iso_eject_end, heart.lv_pressure(heart.iso_eject_end), zorder=2, s=60, color='darkblue')
plt.scatter(heart.eject_end, heart.lv_pressure(heart.eject_end), zorder=2, s=60, color='purple')
plt.scatter(heart.iso_fill_end, heart.lv_pressure(t=heart.iso_fill_end), s=60, zorder=2, color='blue')

plt.show()

pd.DataFrame([list(before_filling_time) + after_filling_time, 
              before_filling_plot + after_filling_plot]).transpose().to_excel('pressure.xlsx', header=['time', 'plot'], 
                                                                              index=False)
