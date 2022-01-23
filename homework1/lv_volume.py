import matplotlib.pyplot as plt
import numpy as np
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

plt.plot(iso_eject_time, iso_eject_y)
plt.plot(eject_time, eject_y)
plt.plot(iso_fill_time, iso_fill_y)
plt.plot(fill_time, fill_y)

plt.scatter(heart.cycle_start, heart.edv)
plt.scatter(heart.iso_eject_end, heart.edv)
plt.scatter(heart.eject_end, heart.esv)
plt.scatter(heart.iso_fill_end, heart.esv)
plt.show()
