import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter as sf

#Start Time, Sat Nov 22 09:14:03 GMT+0100 2014
#Energy calibration,  Offset: 0, Slope: 0.43199265003204346, Quadratic: 0
#Live Time (s), 564.497145
#Real Time (s), 600
#Elapsed Computational, 0
#Spectrum
#Channel, Energy (keV), Counts

angs = ['0', '10', '20', '30', '40', '50', '60', '70']

fig, ax = plt.subplots(4, 2)
fig.tight_layout()
def fun1(angle, vec):
    df = pd.read_csv("data/" + angle + "stA.csv", comment='#')
    x = df[" Energy (keV)"]
    y = df[" Counts"]
    y = sf(y, 101, 2)

    ax[vec].plot(x, y)
    ax[vec].set_title("hello", fontsize=8)

fun1(angs[0], (0,0))
fun1(angs[1], (0,1))
fun1(angs[2], (1,0))
fun1(angs[3], (1,1))
fun1(angs[4], (2,0))
fun1(angs[5], (2,1))
fun1(angs[6], (3,0))
fun1(angs[7], (3,1))
plt.savefig("figs/fig1.pdf")
plt.show()

