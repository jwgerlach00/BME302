import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('')


if __name__ == '__main__':
    # Hard-coded timestamps
    start_inx = 46281
    end_inx = 103746
    systole_inx = 73987
    diastole_inx = 97987
    
    # Import and clean data
    df = pd.read_excel('exercise3_trial2.xlsx')
    cropped_df = df.iloc[start_inx:end_inx]
    cropped_df.time = cropped_df.time - cropped_df.time.iloc[0]
    
    # Clamp upper cardiomic amplitude
    new_cardiomic = []
    for i in cropped_df.cardiomicrophone:
        if abs(i) >= 3:
            i = 3
        new_cardiomic.append(i)
    cropped_df.cardiomicrophone = new_cardiomic
    
    # Create plotting ranges
    systole_coords_x, systole_coords_y = df.time.iloc[systole_inx], df.pressure.iloc[systole_inx]
    diastole_coords_x, diastole_coords_y = df.time.iloc[diastole_inx], df.pressure.iloc[diastole_inx]
    systole_range_x = 2*[systole_coords_x]
    diastole_range_x = 2*[diastole_coords_x]
    pressure_range = [min(cropped_df.pressure), max(cropped_df.pressure)]
    pulse_range = [min(cropped_df.pulse), max(cropped_df.pulse)]
    cardiomic_range = [min(cropped_df.cardiomicrophone), max(cropped_df.cardiomicrophone)]
    
    # Plot pressure
    plt.plot(cropped_df.time, cropped_df.pressure, color='k')
    plt.plot(systole_range_x, pressure_range, lw=3, color='b')
    plt.scatter(systole_coords_x, systole_coords_y, color='b', lw=3, zorder=3)
    plt.text(systole_coords_x + 1, systole_coords_y, f'({round(systole_coords_x)}, {round(systole_coords_y)})', 
             color='b')
    plt.plot(diastole_range_x, pressure_range, lw=3, color='r')
    plt.scatter(diastole_coords_x, diastole_coords_y, color='r', lw=3, zorder=3)
    plt.text(diastole_coords_x + 1, diastole_coords_y + 5, f'({round(diastole_coords_x)}, {round(diastole_coords_y)})', 
             color='r')
    plt.title('Pressure as a Function of Time', fontsize=24)
    plt.xlabel('Time (seconds)', fontsize=18)
    plt.ylabel('Pressure (mmHg)', fontsize=18)
    plt.legend(['Signal', 'Systole', 'Diastole'], fontsize=14)
    plt.grid()
    plt.savefig('out_data/finger_pulse_pressure.png')
    
    # Plot pulse
    plt.figure()
    plt.plot(cropped_df.time, cropped_df.pulse, color='k')
    plt.plot(systole_range_x, pulse_range, lw=3, color='b')
    plt.plot(diastole_range_x, pulse_range, lw=3, color='r')
    plt.title('Finger Pulse as a Function of Time', fontsize=24)
    plt.xlabel('Time (seconds)', fontsize=18)
    plt.ylabel('Pulse (volts)', fontsize=18)
    plt.legend(['Signal', 'Systole', 'Diastole'], fontsize=14)
    plt.grid()
    plt.savefig('out_data/finger_pulse.png')
    
    plt.figure()
    plt.plot(cropped_df.time, cropped_df.cardiomicrophone, color='k')
    plt.plot(systole_range_x, cardiomic_range, lw=3, color='b')
    plt.plot(diastole_range_x, cardiomic_range, lw=3, color='r')
    plt.title('Cardiomic as a Function of Time', fontsize=24)
    plt.xlabel('Time (seconds)', fontsize=18)
    plt.ylabel('Amplitude (milli-volts)', fontsize=18)
    plt.legend(['Signal', 'Systole', 'Diastole'], fontsize=14)
    plt.grid()
    plt.savefig('out_data/finger_cardiomic.png')
