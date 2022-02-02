import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from artificial_heart import ArtificialHeart


def run_loop(edv, sp, label, color, scatter=True):
    heart = ArtificialHeart()

    # Alter heart class properties
    heart.esv = 75.388
    heart.edv = edv; heart.sp = sp

    # Create time vector
    time = np.linspace(0, 1, 1000)
    
    # Find plot y values
    plot_vals_pressure = [heart.lv_pressure(t) for t in time]

    # Split time vector by eject and fill for pressure plotting
    time_eject = time[:round(heart.eject_end*1000)]
    time_fill = time[round(heart.eject_end*1000):]

    # Plot filling and ejecting seperately
    plot_vals_volume = [heart.lv_eject_base_eq(y_p=heart.esv, y_0=heart.edv, 
                                               t_0=heart.iso_eject_end, t=t) for t in time_eject] 
    + [heart.lv_fill_base_eq(y_p=heart.esv, y_0=heart.edv, t_0=heart.iso_fill_end, t=t) for t in time_fill]

    plt.plot(plot_vals_volume, plot_vals_pressure, zorder=1, color=color, lw=3, 
             label='Pressure-volume-loop {0}'.format(label))

    # Find pressure max for SP
    press_max = max(plot_vals_pressure)
    press_index = plot_vals_pressure.index(press_max)

    scatter_vals = pd.read_excel('pressure_volume.xlsx')
    
    # Plot scatter points if specified
    if scatter:
        plt.scatter(plot_vals_volume[press_index], press_max, zorder=2, label='SV, SP', s=60)
        [plt.scatter(v, p, zorder=2, label=label, s=60) for v, p, label in zip(scatter_vals.volume[:3], 
                                                                               scatter_vals.pressure[:3], 
                                                                               ['EDV, EDP', 'DV, DP', 'ESV, ESP'])]

    # Plot elastance
    corner_v, corner_p = scatter_vals.volume[3], max(plot_vals_pressure) - 5
    origin_v, origin_p = 0, 0
    plt.plot([origin_v, corner_v, 100], [origin_p, corner_p, corner_p/corner_v*100], 
             label='{0} {1}'.format('EDPVR', label), lw=3, zorder=3)

    # Format plots
    plt.xlabel('Volume (mL)', fontsize=16)
    plt.ylabel('Pressure (mm Hg)', fontsize=16)
    plt.legend()
    plt.title('Pressure Volume Loop', fontsize=24)

    
if __name__ == '__main__':
    heart = ArtificialHeart()
    
    # Plot normal pressure-volume-loop
    run_loop(heart.edv, heart.sp, label='', color='orange')
    plt.show()
    
    # Plot loops with different EDV and SP parameters
    run_loop(heart.edv - 0.15*heart.edv, heart.sp, scatter=False, label='-15% EDV', color='orange')
    run_loop(heart.edv, heart.sp + 0.20*heart.sp, scatter=False, label='+20% SP', color='red')
    run_loop(heart.edv - 0.15*heart.edv, heart.sp - 0.15*heart.sp, scatter=False, label='-15% EDV and SP', color='cyan')
    plt.show()
