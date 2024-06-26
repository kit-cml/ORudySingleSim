#tension comparison
from scipy.signal import find_peaks
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# coupled = pd.read_csv("../result/chlorpromazine/0.00/0conc.csv")
data1 = pd.read_csv("./500_bclfix/0.00/0conc.csv")
# data2 = pd.read_csv("./1000/0.00/0vmcheck.csv")
data2 = pd.read_csv("./1000_bclfix/0.00/0conc.csv")
data3 = pd.read_csv("./1500_bclfix/0.00/0conc.csv")
data4 = pd.read_csv("./2000_bclfix/0.00/0conc.csv")

# Create a figure and subplots with shared x- axis            
plt.figure()

time1 = data1['Time']-499500
# time1 = time1[time1 <= 301]
time2 = data2['Time']-999000
# time2 = time2[time2 <= 301]
time3 = data3['Time']-1498500

# Create scatter plots on each subplot
# plt.scatter(coupled['Time']-198000, coupled['cai'], label='Coupled', marker='o')
plt.scatter(data4['Time']-1998000, data4['cai'], color='red', label='2000 BCL')
plt.scatter(time3, data3['cai'].head(len(time3)), color='orange', label='1500 BCL')
plt.scatter(time2, data2['cai'].head(len(time2)), color='blue', label='1000 BCL')
plt.scatter(time1, data1['cai'].head(len(time1)), color='lightblue', label='500 BCL')

# plt.scatter(data4['Time']-1998000, data4['v'], color='red', label='2000 BCL')
# plt.scatter(data3['Time']-1498500, data3['v'], color='orange', label='1500 BCL')
# plt.scatter(data2['Time']-999000, data2['v'], color='blue', label='1000 BCL')
# plt.scatter(data1['Time']-499000, data1['v'], color='lightblue', label='500 BCL')


# Add labels and title (optional)
# plt.ylabel('Force (kilo pascal)')
plt.xlabel('Time (millisecond)')


# Add legend
plt.title("Calcium Concentration (in mMol) - Coupled")
plt.legend()  # Legend is placed on the top subplot

# Show the plot
# plt.tight_layout()
plt.savefig("Cai.png")

print("Coupled:")

peaks = find_peaks(data1['cai'])[0]
idx_max_peak = peaks[np.argmax(data1['cai'][peaks])]
max_peak = data1['cai'][idx_max_peak]
print("Peak for 500 BCL: ",max_peak)

peaks = find_peaks(data2['cai'])[0]
idx_max_peak = peaks[np.argmax(data2['cai'][peaks])]
max_peak = data2['cai'][idx_max_peak]
print("Peak for 1000 BCL: ",max_peak)

peaks = find_peaks(data3['cai'])[0]
idx_max_peak = peaks[np.argmax(data3['cai'][peaks])]
max_peak = data3['cai'][idx_max_peak]
print("Peak for 1500 BCL: ",max_peak)

peaks = find_peaks(data4['cai'])[0]
idx_max_peak = peaks[np.argmax(data4['cai'][peaks])]
max_peak = data4['cai'][idx_max_peak]
print("Peak for 2000 BCL: ",max_peak)
