from math import exp, sin, pi


class ArtificialHeart:
    def __init__(self) -> None:
        # Artificial heart init conditions
        heart_rate = 72  # bpm
        self.period = 60/heart_rate  # sec
        
        # Pressure
        self.sp = 120  # mmHg
        self.min_lv_pressure = 10  # mmHg

        # Y plataeu
        self.esv = 65  # mL, systole
        self.edv = 120  # mL, diastole

        # Exponential k multiplier
        self.k_systole = 9  # sec^-1
        self.k_diastole = 18  # sec^-1

        # Overall lengths of cardio cycle
        systole_len = (1/3)*self.period  # sec
        diastole_len = (2/3)*self.period  # sec

        # Sub-sets of cardio cycle
        self.cycle_start = 0  # sec
        self.iso_eject_end = (1/3)*systole_len + self.cycle_start  # sec
        self.eject_end = (2/3)*systole_len + self.iso_eject_end  # sec
        self.iso_fill_end = (1/3)*diastole_len + self.eject_end  # sec
        
        sin_period = 2*(self.period - (2/3)*diastole_len)  # sec
        self.sin_freq = 1/sin_period  # sec^-1

    def lv_fill_base_eq(self, y_p, y_0, t_0, t):
        if t < t_0:
            return y_0
        else:
            return y_p + (y_0 - y_p)*(1 - exp(-self.k_diastole*(t - t_0)))
        
    def lv_eject_base_eq(self, y_p, y_0, t_0, t):
        if t < t_0:
            return y_0
        else:
            return y_p + (y_0 - y_p)*exp(-self.k_systole*(t - t_0))
        
    def lv_pressure(self, t):
        if t < self.iso_fill_end:
            return (self.sp - self.min_lv_pressure)*sin(2*pi*self.sin_freq*t) + self.min_lv_pressure
        else:
            return self.min_lv_pressure
