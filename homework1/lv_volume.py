import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from artificial_heart import ArtificialHeart
    

heart = ArtificialHeart()

# --------------------------------- Plotting --------------------------------- #
# Time arrays
iso_eject_time = np.linspace(heart.cycle_start, heart.iso_eject_end, 100)
eject_time = np.linspace(heart.iso_eject_end, heart.eject_end, 100)
iso_fill_time = np.linspace(heart.eject_end, heart.iso_fill_end, 100)
fill_time = np.linspace(heart.iso_fill_end, heart.period, 100)

# Y values for ISO fill and eject
iso_eject_y = len(iso_eject_time)*[heart.edv]
iso_fill_y = len(iso_fill_time)*[heart.esv]

# Y values for fill and eject
eject_y = [heart.lv_eject_base_eq(y_p=heart.esv, y_0=heart.edv, t_0=heart.iso_eject_end, t=t) 
           for t in eject_time]
fill_y = [heart.lv_fill_base_eq(y_p=heart.esv, y_0=heart.edv, t_0=heart.iso_fill_end, t=t) 
          for t in fill_time]

plt.plot(iso_eject_time, iso_eject_y, zorder=1, lw=3, color='red', label='Isovolumetric contraction')
plt.plot(eject_time, eject_y, lw=3, zorder=1, color='orange', label='Ventricular systole (ejection)')
plt.plot(iso_fill_time, iso_fill_y, lw=3, zorder=1, color='blueviolet', label='Isovolumetric relaxation')
plt.plot(fill_time, fill_y, lw=3, zorder=1, color='indigo', label='Ventricular diastole (filling)')

plt.scatter(heart.cycle_start, heart.edv, s=60, zorder=2, color='black', label='End diastolic volume')
plt.scatter(heart.iso_eject_end, heart.edv, s=60, zorder=2, color='darkblue', 
            label='Diastolic volume\n(aortic valve opens)')
plt.scatter(heart.eject_end, heart.esv, s=60, zorder=2, color='darkgreen', label='End systolic volume')
plt.scatter(heart.iso_fill_end, heart.esv, s=60, zorder=2, color='b', label='Systolic volume\n(mitral valve opens)')

plt.xlabel('Time (seconds)'); plt.ylabel('Volume (mL)')
plt.legend(loc='lower right')

plt.show()

pd.DataFrame([list(iso_eject_time) + list(eject_time) + list(iso_fill_time) + list(fill_time), 
              iso_eject_y + eject_y + iso_fill_y + fill_y]).transpose().to_excel('volume.xlsx', header=['time', 'plot'], 
                                                                              index=False)
