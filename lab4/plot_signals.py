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
    
    mic_systole_inx = 71800
    mic_diastole_inx = 99855
    
    # Import and clean data
    df = pd.read_excel('exercise3_trial2.xlsx')
    cropped_df = df.iloc[start_inx:end_inx]
    cropped_df.time = cropped_df.time - cropped_df.time.iloc[0]
    
    # Clamp upper cardiomic amplitude
    # new_cardiomic = []
    # for i in cropped_df.cardiomicrophone:
    #     if abs(i) >= 3:
    #         i = 3
    #     new_cardiomic.append(i)
    # cropped_df.cardiomicrophone = new_cardiomic
    
    # Create plotting ranges
    systole_coords_x, systole_coords_y = df.time.iloc[systole_inx], df.pressure.iloc[systole_inx]
    diastole_coords_x, diastole_coords_y = df.time.iloc[diastole_inx], df.pressure.iloc[diastole_inx]
    systole_range_x = 2*[systole_coords_x]
    diastole_range_x = 2*[diastole_coords_x]
    pressure_range = [min(cropped_df.pressure), max(cropped_df.pressure)]
    pulse_range = [min(cropped_df.pulse), max(cropped_df.pulse)]
    cardiomic_range = [min(cropped_df.cardiomicrophone), max(cropped_df.cardiomicrophone)]
    
    mic_systole_coords_x, mic_systole_coords_y = df.time.iloc[mic_systole_inx], df.pressure.iloc[mic_systole_inx]
    mic_diastole_coords_x, mic_diastole_coords_y = df.time.iloc[mic_diastole_inx], df.pressure.iloc[mic_diastole_inx]
    mic_systole_range_x = 2*[mic_systole_coords_x]
    mic_diastole_range_x = 2*[mic_diastole_coords_x]
    
    # Plot pressure
    plt.plot(cropped_df.time, cropped_df.pressure, color='k')
    plt.plot(systole_range_x, pressure_range, lw=6, color='b', alpha=0.4)
    plt.scatter(systole_coords_x, systole_coords_y, color='b', lw=3, zorder=3)
    plt.text(systole_coords_x + 1, systole_coords_y, f'({round(systole_coords_x)}, {round(systole_coords_y)})', 
             color='b', fontsize=16)
    plt.plot(diastole_range_x, pressure_range, lw=6, color='r', alpha=0.4)
    plt.scatter(diastole_coords_x, diastole_coords_y, color='r', lw=3, zorder=3)
    plt.text(diastole_coords_x - 12, diastole_coords_y + 2, f'({round(diastole_coords_x)}, {round(diastole_coords_y)})', 
             color='r', fontsize=16)
    plt.plot(mic_systole_range_x, pressure_range, lw=6, color='purple', alpha=0.4)
    plt.scatter(mic_systole_coords_x, mic_systole_coords_y, color='purple', lw=3, zorder=3)
    plt.text(mic_systole_coords_x - 14, mic_systole_coords_y - 5, 
             f'({round(mic_systole_coords_x)}, {round(mic_systole_coords_y)})', color='purple', fontsize=16)
    plt.plot(mic_diastole_range_x, pressure_range, lw=6, color='darkred', alpha=0.4)
    plt.scatter(mic_diastole_coords_x, mic_diastole_coords_y, color='darkred', lw=3, zorder=3)
    plt.text(mic_diastole_coords_x - 6, mic_diastole_coords_y - 20, 
             f'({round(mic_diastole_coords_x)}, {round(mic_diastole_coords_y)})', color='darkred', fontsize=16)
    plt.title('Pressure as a Function of Time', fontsize=24)
    plt.xlabel('Time (seconds)', fontsize=18)#, labelpad=60)
    plt.ylabel('Pressure (mmHg)', fontsize=18)
    lgd = plt.legend(['Signal', 'Auscultation systole', 'Auscultation diastole', 'Cardiomic systole', 
                      'Cardiomic diastole'], fontsize=16, loc='lower center', bbox_to_anchor=(0.5, -0.5), ncol=2)
    plt.grid()
    plt.savefig('out_data/finger_pulse_pressure.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
    
    # Plot pulse
    plt.figure()
    plt.plot(cropped_df.time, cropped_df.pulse, color='k')
    plt.plot(systole_range_x, pulse_range, lw=6, color='b', alpha=0.4)
    plt.plot(diastole_range_x, pulse_range, lw=6, color='r', alpha=0.4)
    plt.title('Finger Pulse as a Function of Time', fontsize=24)
    plt.xlabel('Time (seconds)', fontsize=18)
    plt.ylabel('Pulse (volts)', fontsize=18)
    plt.legend(['Signal', 'Systole', 'Diastole'], fontsize=14)
    plt.grid()
    plt.savefig('out_data/finger_pulse.png')
    
    # Plot cardiomicrophone
    plt.figure()
    plt.plot(cropped_df.time, cropped_df.cardiomicrophone, color='k')
    plt.plot(mic_systole_range_x, cardiomic_range, lw=6, color='b', alpha=0.4)
    plt.plot(mic_diastole_range_x, cardiomic_range, lw=6, color='r', alpha=0.4)
    # plt.scatter(mic_systole_coords_x, mic_systole_coords_y)
    # plt.scatter(mic_diastole_coords_x, mic_diastole_coords_y)
    plt.title('Cardiomic as a Function of Time', fontsize=24)
    plt.xlabel('Time (seconds)', fontsize=18)
    plt.ylabel('Amplitude (milli-volts)', fontsize=18)
    plt.legend(['Signal', 'Systole', 'Diastole'], fontsize=14)
    plt.grid()
    plt.savefig('out_data/finger_cardiomic.png')
