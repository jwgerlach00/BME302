import numpy as np
import pandas as pd
from math import pi
import sympy as sym


def hagan_poiseuille(r, P1, P2, mu, L):
    """Uses the Hagen-Poiseuille equation to find flow rate.

    Args:
        r (float): Current vessel radius.
        dP (float): Pressure gradient.
        mu (float): Viscosity.
        L (float): Vessel length.

    Returns:
        float: Flow rate.
    """
    return (pi*r**4*(P1 - P2))/(8*mu*L)

def vascular_resistance_fudge_factor(x):
    return 1.25e-7*x

def calc_resistance(mu, L, r):
    return vascular_resistance_fudge_factor((8*mu*L)/(pi*r**4))

def sum_r_series(resistances):
    """Sums series resistances."""
    return np.sum(resistances)

def sum_r_parallel(resistances):
    """Sums parallel resistances."""
    reciprocals = [1/r for r in resistances]
    return 1/np.sum(reciprocals)


def run_3a():
    # Solve for individual resistances
    resistances = [calc_resistance(viscosity, l, r) for l, r in zip(lengths, radii)]  # mmHg*min/L
    
    # Solve for effective resistances
    R_23 = sum_r_parallel(resistances[1:3])  # mmHg*min/L
    R_1234 = sum_r_series([R_23, resistances[0], resistances[3]])  # mmHg*min/L
    R_overall = sum_r_parallel([R_1234, resistances[-1]])  # mmHg*min/L
    
    # Export results
    r_df = pd.DataFrame({'Resistor': ['R1', 'R2', 'R3', 'R4', 'R5'], 'Individual Resistance (mmHg*min/L)': resistances})
    eff_r_df = pd.DataFrame({'Resistor': ['R1_eff', 'R2_eff', 'R_eff'], 
                                   'Effective Resistance (mmHg*min/L)': [R_23, R_1234, R_overall]})
    r_df.to_excel('indiv_resistances.xlsx', index=False)
    eff_r_df.to_excel('eff_resistances.xlsx', index=False)
    
def run_3b():
    # Import resistances (given)
    r1, r2, r3, r4, r5 = list(pd.read_excel('indiv_resistances.xlsx')['Individual Resistance (mmHg*min/L)'])
    
    # Optimize system of equations to find p2 and p3
    p2, p3 = sym.symbols('p2 p3')
    
    eq1 = 5.238 + 0.524*p3 - p2
    eq2 = 11 - p3 - ((p2 - p3)/r2 + (p2 - p3)/r3)*r4 - ((p2 - p3)/r2 + (p2 - p3)/r3 - 0.65)*r5
    
    p2, p3 = sym.solve([eq1, eq2], [p2, p3]).values()
    
    # Plug and chug starting from p2 and p3
    Q1 = (p2 - p3)/r2 + (p2 - p3)/r3
    Q2 = Q1/2
    Q3 = Q1 - Q2
    Q4 = Q1
    Q5 = 0.65 - Q1
    p4 = p3 - Q1*r4
    
    # Export results
    out = pd.DataFrame({'Pressures1': ['P1', 'P2', 'P3', 'P4', np.nan], 'Pressures2': [p1, p2, p3, p4, np.nan], 
                        'Flow_Rates1': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'], 'FlowRates_2': [Q1, Q2, Q3, Q4, Q5]})
    print(out)
    out.to_excel('3b_output.xlsx', index=False)
    

if __name__ == '__main__':
    # Blood params
    viscosity= 0.0027  # N*s/m^2, at 37C
    density = 1060  # kg/m^3
    Q_in = 0.65  # L/min, equals Q_out
    p1 = 11  # mmHg
    
    radii = 1e-3*np.array([5, 4, 4, 2, 5])  # mm -> meters
    lengths = 1e-2*np.array([8, 6, 6, 8, 22])  # cm -> meters
    
    run_3a()
    run_3b()

