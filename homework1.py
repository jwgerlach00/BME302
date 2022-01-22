from math import sin, pi, exp
import matplotlib.pyplot as plt
import numpy as np

# def lv_pressure_before_filling(t, f):
#     return sin(2*pi*f*t)

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

# Plotting filling

#plateau: esv or edv

# Artificial heart init conditions
hr = 72  # bpm
period = 60/hr  # sec

# Y plataeu
edv = 120  # mL, diastole
esv = 65  # mL, systole

# Exponential k multiplier
k_diastole = 18  # sec^-1
k_systole = 9  # sec^-1

# Overall lengths of cardio cycle
diastole_len = (2/3)*period  # sec
systole_len = (1/3)*period  # sec

# Sub-sets of cardio cycle
cycle_start = 0
iso_fill_end = (1/3)*diastole_len + cycle_start  # sec
fill_end = (2/3)*diastole_len + iso_fill_end  # sec
iso_eject_end = (1/3)*systole_len + fill_end  # sec
eject_time = period  # sec

# Plotting filling
# time_iso_fill = np.linspace(0, iso_fill_len, 100)

# time_iso_eject = np.linspace(fill_len, iso_eject_len + fill_len, 100)
# time_eject = np.linspace(iso_eject_len, eject_len + iso_eject_len, 100)

diastole_time = np.linspace(cycle_start, diastole_len, 100)
systole_time = np.linspace(diastole_len, period, 100)

# lv_eject_plot = [lv_eject_base_eq(y_p=esv, y_0=edv, k=k_systole, t_0=t_0_diastole, t=t) for t in time_systole]

# Iso fill
fill_plot = [lv_fill_base_eq(y_p=edv, y_0=esv, k=k_diastole, t_0=iso_fill_end, t=t) for t in diastole_time]
eject_plot = [lv_eject_base_eq(y_p=edv, y_0=esv, k=k_systole, t_0=iso_eject_end, t=t) for t in systole_time]

# lv_fill_plot = [lv_fill_base_eq(y_p=edv, y_0=esv, k=k_diastole, t_0=t_0_diastole, t=t) for t in time_diastole]

plt.plot(diastole_time, fill_plot)
plt.plot(systole_time, eject_plot)
# plt.plot(time_systole, lv_eject_plot)
plt.show()

# t_0 @ start of diastole