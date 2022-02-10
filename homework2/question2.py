import numpy as np
import matplotlib.pyplot as plt


def dyne_to_mmhg(dyne):
    """Converts dyne units to mmHg for pressure.

    Args:
        dyne (float): Dynes.

    Returns:
        float: mmHg
    """
    return 0.00075*dyne

def find_pressure_drop(tau, L_r_ratio):
    """Solves for pressure drop.

    Args:
        tau (float): Stress.
        L_r_ratio (float): Ratio between length and radius.

    Returns:
        float: Pressure difference.
    """
    return tau*2*L_r_ratio
    
def cassons(T_y, s, shear_rate):
    """Stress equation for Casson's fluid.

    Args:
        T_y (float): Yield stress.
        s (float): Sqrt of viscosity.
        shear_rate (float): Shear rate.

    Returns:
        float: Stress.
    """
    return (T_y**(1/2) + s*shear_rate**(1/2))**2

def newtonian(s, shear_rate):
    """Stress equation for Newtonian fluid.

    Args:
        s (float): Sqrt of viscosity.
        shear_rate (float): Shear rate.

    Returns:
        float: Stress.
    """
    return (s**2)*shear_rate


def run_2a():
    print(dyne_to_mmhg(find_pressure_drop(yield_stress, L_ovr_R)))
    
def run_2b_2c():
    shear_rates = np.linspace(0.001, 10000, 1000000)  # sec^-1
    casson_stresses = [cassons(yield_stress, s, shear_rate) for shear_rate in shear_rates]  # dynes/cm^2
    newton_stresses = [newtonian(s, shear_rate) for shear_rate in shear_rates]  # dynes/cm^2
    
    # Plot
    plt.figure()
    plt.plot(shear_rates, casson_stresses, shear_rates, newton_stresses, lw=2)
    plt.title('Shear Stress wrt Shear Rate', fontsize=22)
    plt.legend(['Casson\'s fluid', 'Newtonian fluid'], fontsize=14)
    plt.xlabel('Shear Rate (sec^-1)', fontsize=16)
    plt.ylabel('Shear Stress (dynes/cm^2)', fontsize=16)
    plt.grid()
    plt.savefig('2b_normal.png')
    
    # Plot on log axes
    plt.figure()
    plt.plot(shear_rates, casson_stresses, shear_rates, newton_stresses, lw=2)
    plt.plot([0.001, 10000], 2*[cassons(yield_stress, s, 10)], 2*[10], 
             [min(newton_stresses), max(newton_stresses)], color='k')
    plt.title('Shear Stress wrt Shear Rate', fontsize=22)
    plt.legend(['Casson\'s fluid', 'Newtonian fluid', 'Agreement approx.'], fontsize=14)
    plt.xlabel('Shear Rate (sec^-1)', fontsize=16)
    plt.ylabel('Shear Stress (dynes/cm^2)', fontsize=16)
    plt.yscale('log')
    plt.xscale('log')
    plt.grid()
    plt.savefig('2b_log.png')


if __name__ == '__main__':
    yield_stress = 0.028  # dynes/cm^2, at 37C
    L_ovr_R = 200
    s = 0.280  # (dynes*sec/cm^2)^(1/2)
    run_2a()
    run_2b_2c()
