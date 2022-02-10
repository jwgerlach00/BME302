from math import pi, ceil
import numpy as np
import matplotlib.pyplot as plt


def mmhg_to_pa(x):
    """Converts mmHg to Pascals.

    Args:
        x (float): mmHg.

    Returns:
        float: Pascals.
    """
    return 133.322*x

def shear_stress(Q, mu, r):
    """Computes shear stress at the wall of a blood vessel.

    Args:
        Q (float): Flow rate.
        mu (float): Viscosity.
        r (float): Vessel radius.

    Returns:
        float: Shear stress.
    """
    return (4*Q*mu)/(pi*abs(r**3))

def velocity_profile(dP, mu, L, R, r):
    """Computes velocity through a blood vessel.

    Args:
        dP (float): Pressure gradient.
        mu (float): Viscosity.
        L (float): Vessel length.
        R (float): Max vessel radius.
        r (float): Current vessel radius.

    Returns:
        float: Velocity.
    """
    return (dP/(4*mu*L))*(R**2)*(1 - (r/R)**2)

def hagan_poiseuille(r, dP, mu, L):
    """Uses the Hagen-Poiseuille equation to find flow rate.

    Args:
        r (float): Current vessel radius.
        dP (float): Pressure gradient.
        mu (float): Viscosity.
        L (float): Vessel length.

    Returns:
        float: Flow rate.
    """
    return (pi*r**4*dP)/(8*mu*L)


def run_1a():
    radii = np.linspace(-vessel_rad, vessel_rad, 1000)  # cm
    
    # Generate velocities
    velocities = [velocity_profile(pressure_drop, viscosity, vessel_len, vessel_rad, r) for r in radii]  # cm/s
    
    # Generate shear stress
    Qs = [hagan_poiseuille(r, pressure_drop, viscosity, vessel_len) for r in radii]
    print(hagan_poiseuille(-1, pressure_drop, viscosity, vessel_len))
    stresses = [shear_stress(q, viscosity, r) for q, r in zip(Qs, radii)]  # Pa

    # Plot
    plt.figure()
    plt.plot(velocities, 1e4*radii, lw=3, color='b')
    plt.title('Radius wrt Velocity', fontsize=22)
    plt.xlabel('Velocity (cm/s)', fontsize=16)
    plt.ylabel('Radius (µm)', fontsize=16)
    plt.grid()
    plt.savefig('velocity_vs_radii.png')
    
    plt.figure()
    plt.plot(stresses, 1e4*radii, lw=3, color='b')
    plt.title('Radius wrt Stress', fontsize=22)
    plt.xlabel('Shear Stress (Pa)', fontsize=16)
    plt.ylabel('Radius (µm)', fontsize=16)
    plt.grid()
    plt.savefig('shear_stress_vs_radii.png')

def run_1b():
    Q = hagan_poiseuille(vessel_rad, pressure_drop, viscosity, vessel_len)
    
    num_fibers = np.linspace(6500, 7500, 1000)
    Qs = 60*Q*num_fibers  # mL/min
    
    # Find point closest to desired flow
    Q_diffs = [(q - desired_flow)**2 for q in Qs]
    min_index = Q_diffs.index(min(Q_diffs))
    
    # Plot
    plt.figure()
    plt.plot(num_fibers, Qs, color='b', lw=3)
    plt.scatter(num_fibers[min_index], Qs[min_index], color='r', label='Bioreactor fiber #', zorder=3, lw=3)
    plt.text(num_fibers[min_index] + 50, Qs[min_index], 
             '({0}, {1})'.format(ceil(num_fibers[min_index]), ceil(Qs[min_index])), color='r')
    plt.title('Total Flow Rate wrt Fiber Count', fontsize=22)
    plt.xlabel('Fiber Number', fontsize=16)
    plt.ylabel('Total Flow Rate (mL/min)', fontsize=16)
    plt.grid()
    plt.legend(fontsize=14)
    plt.savefig('1b_plot.png')


if __name__ == '__main__':
    # Vessel params
    vessel_diam = 500e-4  # um --> cm
    vessel_rad = vessel_diam/2  # cm
    vessel_len = 35  # cm
    pressure_drop = mmhg_to_pa(25)  # Pascals
    viscosity = 0.85e-3  # Poise (Pa*s)
    density = 1  # g/cm^3
    desired_flow = 7225  # mL/min
    
    run_1a()
    run_1b()
