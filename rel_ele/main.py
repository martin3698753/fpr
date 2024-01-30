import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter as sf
from scipy.signal import find_peaks as fp

names = ['Co60', 'Cs137', 'Eu152', 'Na22', 'Y88']
fig, ax = plt.subplots(2, 2)
fig.tight_layout()
def fun1(name, vec):
    match name:
        case 'Co60':
            ax[vec].set_xlim([1000, 1500])
        case 'Cs137':
            ax[vec].set_xlim([0, 800])
        case 'Eu152':
            ax[vec].set_xlim([0, 600])

    df = pd.read_csv("data/" + name + ".csv")
    y = df[" Counts"].values
    x = df[" Energy (keV)"].values
    #y = sf(y, 50, 2)
    peaks = fp(y, height=100)
    yp = peaks[1]['peak_heights']
    xp = x[peaks[0]]

    ax[vec].plot(x, y)
    #ax[vec].scatter(xp, yp)
    #plt.axvline(1166.25)
    #plt.axvline(1178.02)
fun1(names[0], (0, 0))
fun1(names[1], (0, 1))
fun1(names[2], (1, 0))
fun1(names[3], (1, 1))
plt.show()
