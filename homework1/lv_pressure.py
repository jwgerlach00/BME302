import numpy as np
import matplotlib.pyplot as plt
from artificial_heart import ArtificialHeart


heart = ArtificialHeart()

# --------------------------------- Plotting --------------------------------- #
# Time arrays
before_filling_time = np.linspace(heart.cycle_start, heart.iso_fill_end, 100)
after_filling_time = [heart.iso_fill_end, heart.period]

# Y values for plots
before_filling_plot = [heart.lv_pressure(t=t) for t in before_filling_time]
after_filling_plot = [heart.lv_pressure(t=t) for t in after_filling_time]

plt.plot(before_filling_time, before_filling_plot)
plt.plot(after_filling_time, after_filling_plot)

plt.scatter(heart.cycle_start, heart.lv_pressure(heart.cycle_start))
plt.scatter(heart.iso_eject_end, heart.lv_pressure(heart.iso_eject_end))
plt.scatter(heart.eject_end, heart.lv_pressure(heart.eject_end))
plt.scatter(heart.iso_fill_end, heart.lv_pressure(t=heart.iso_fill_end))
plt.show()
