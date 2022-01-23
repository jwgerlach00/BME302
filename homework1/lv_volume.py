from math import exp
import matplotlib.pyplot as plt
import numpy as np


def lv_fill_base_eq(y_p, y_0, k, t_0, t):
    if t < t_0:
        return y_0
    else:
        return y_p + (y_0 - y_p)*(1 - exp(-k*(t - t_0)))
    
def lv_eject_base_eq(y_p, y_0, k, t_0, t):
    if t < t_0:
        return y_0
    else:
        return y_p + (y_0 - y_p)*exp(-k*(t - t_0))
    

# ------------------------------- Declarations ------------------------------- #
# Artificial heart init conditions
hr = 72  # bpm
period = 60/hr  # sec

# Y plataeu
esv = 65  # mL, systole
edv = 120  # mL, diastole

# Exponential k multiplier
k_systole = 9  # sec^-1
k_diastole = 18  # sec^-1

# Overall lengths of cardio cycle
systole_len = (1/3)*period  # sec
diastole_len = (2/3)*period  # sec

# Sub-sets of cardio cycle
cycle_start = 0  # sec
iso_eject_end = (1/3)*systole_len + cycle_start  # sec
eject_end = (2/3)*systole_len + iso_eject_end  # sec
iso_fill_end = (1/3)*diastole_len + eject_end  # sec

# --------------------------------- Plotting --------------------------------- #
# Plot time arrays
iso_eject_time = np.linspace(cycle_start, iso_eject_end, 100)
eject_time = np.linspace(iso_eject_end, eject_end, 100)
iso_fill_time = np.linspace(eject_end, iso_fill_end, 100)
fill_time = np.linspace(iso_fill_end, period, 100)

# Y values for ISO fill and eject
iso_fill_y = len(iso_fill_time)*[esv]
iso_eject_y = len(iso_eject_time)*[edv]

# Y values for fill and eject
fill_y = [lv_fill_base_eq(y_p=esv, y_0=edv, k=k_diastole, t_0=iso_fill_end, t=t) for t in fill_time]
eject_y = [lv_eject_base_eq(y_p=esv, y_0=edv, k=k_systole, t_0=iso_eject_end, t=t) for t in eject_time]

plt.plot(iso_eject_time, iso_eject_y)
plt.plot(eject_time, eject_y)
plt.plot(iso_fill_time, iso_fill_y)
plt.plot(fill_time, fill_y)
plt.show()
