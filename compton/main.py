import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter as sf
from scipy.signal import find_peaks as fp

#Start Time, Sat Nov 22 09:14:03 GMT+0100 2014
#Energy calibration,  Offset: 0, Slope: 0.43199265003204346, Quadratic: 0
#Live Time (s), 564.497145
#Real Time (s), 600
#Elapsed Computational, 0
#Spectrum
#Channel, Energy (keV), Counts

angs = ['0', '10', '20', '30', '40', '50', '60', '70']
energy = np.zeros(8)

fig, ax = plt.subplots(4, 2)
fig.tight_layout()
def fun1(angle, vec, h, index):
    df = pd.read_csv("data/" + angle + "stA.csv", comment='#')
    x = df[" Energy (keV)"]
    y = df[" Counts"]
    y = sf(y, 101, 2)
    peaks = fp(y, height=h, distance=120)
    yp = peaks[1]['peak_heights']
    xp = x[peaks[0]].values

    if (angle == '30' or angle == '40' or angle == '50' or angle == '60'):
        yp = yp[1]
        xp = xp[1]
    energy[index] = xp.item()
    ax[vec].scatter(xp, yp)
    ax[vec].plot(x, y)
    ax[vec].set_title("hello", fontsize=8)

fun1(angs[0], (0,0), 10000, 0)
fun1(angs[1], (0,1), 5000, 1)
fun1(angs[2], (1,0), 1000, 2)
fun1(angs[3], (1,1), 300, 3)
fun1(angs[4], (2,0), 250, 4)
fun1(angs[5], (2,1), 200, 5)
fun1(angs[6], (3,0), 180, 6)
fun1(angs[7], (3,1), 180, 7)
print(energy)
plt.savefig("figs/fig1.pdf")
plt.show()

