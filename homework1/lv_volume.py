import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from artificial_heart import ArtificialHeart
    

heart = ArtificialHeart()

# --------------------------------- Plotting --------------------------------- #
# Time arrays
iso_eject_time = np.linspace(heart.cycle_start, heart.iso_eject_end, 1000)
eject_time = np.linspace(heart.iso_eject_end, heart.eject_end, 1000)
iso_fill_time = np.linspace(heart.eject_end, heart.iso_fill_end, 1000)
fill_time = np.linspace(heart.iso_fill_end, heart.period, 1000)

# Y values for eject
eject_y = [heart.lv_eject_base_eq(y_p=heart.esv, y_0=heart.edv, t_0=heart.iso_eject_end, t=t) 
           for t in eject_time]
iso_eject_y = len(iso_eject_time)*[heart.edv]

# Re-declare heart esv so curve connects
heart.esv = min(eject_y)

# Y values for fill
fill_y = [heart.lv_fill_base_eq(y_p=heart.esv, y_0=heart.edv, t_0=heart.iso_fill_end, t=t) 
          for t in fill_time]
iso_fill_y = len(iso_fill_time)*[heart.esv]

sp_time = 0.229

# Generate plots
plt.plot(iso_eject_time, iso_eject_y, zorder=1, lw=3, color='red', label='Isovolumetric contraction')
plt.plot(eject_time, eject_y, lw=3, zorder=1, color='orange', label='Ventricular systole (ejection)')
plt.plot(iso_fill_time, iso_fill_y, lw=3, zorder=1, color='green', label='Isovolumetric relaxation')
plt.plot(fill_time, fill_y, lw=3, zorder=1, color='indigo', label='Ventricular diastole (filling)')

plt.scatter(heart.cycle_start, heart.edv, s=60, zorder=2, color='black', label='End diastolic volume')
plt.scatter(heart.iso_eject_end, heart.edv, s=60, zorder=2, color='darkblue', 
            label='Diastolic volume')
plt.scatter(sp_time, heart.lv_eject_base_eq(y_p=65, y_0=heart.edv, t_0=heart.iso_eject_end, t=sp_time), s=60, zorder=2, 
            color='darkgreen', label='Systolic volume')
plt.scatter(heart.iso_fill_end, heart.esv, s=60, zorder=2, color='b', label='End systolic volume')

print(heart.edv)
print(heart.edv)
print(heart.esv)
print(heart.esv)

plt.xlabel('Time (s)', fontsize=16); plt.ylabel('Volume (mL)', fontsize=16)
plt.title('LV Volume wrt Time', fontsize=24)
plt.legend(loc='lower right')

plt.show()

# Output data for pressure-volume-loop script
pd.DataFrame([list(iso_eject_time) + list(eject_time) + list(iso_fill_time) + list(fill_time), 
              iso_eject_y + eject_y + iso_fill_y + fill_y]).transpose().to_excel('volume.xlsx', header=['time', 'plot'], 
                                                                              index=False)
