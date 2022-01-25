import matplotlib.pyplot as plt
import numpy as np
from artificial_heart import ArtificialHeart


heart = ArtificialHeart()

time = np.linspace(0, 1, 100)
plot_vals_pressure = [heart.lv_pressure(t) for t in time]

# plt.plot(time, plot_vals)


time_eject = time[:round(heart.eject_end*100)]
time_fill = time[round(heart.eject_end*100):]

plot_vals_volume = [heart.lv_eject_base_eq(y_p=heart.esv, y_0=heart.edv, t_0=heart.iso_eject_end, t=t) for t in time_eject] + [heart.lv_fill_base_eq(y_p=heart.esv, y_0=heart.edv, t_0=heart.iso_fill_end, t=t) for t in time_fill]

# plt.plot(time, plot_vals_volume)
# plt.show()

plt.plot(plot_vals_volume, plot_vals_pressure)
plt.scatter(plot_vals_volume[0], plot_vals_pressure[0], label='EDP/EDV')

press_max = max(plot_vals_pressure)
press_index = plot_vals_pressure.index(press_max)

plt.scatter(plot_vals_volume[press_index], press_max)

plt.show()