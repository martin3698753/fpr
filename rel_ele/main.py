import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from scipy.signal import savgol_filter as sf
from scipy.signal import find_peaks as fp

names = ['Cs137', 'Co60', 'Na22', 'Y88', 'Eu152']
fig, ax = plt.subplots(2, 2)
fig.tight_layout()
def fun1(name, vec):
    match name:
        case 'Co60':
            ax[vec].set_xlim([1100, 1200])
            #ax[vec].set_ylim([0, 30])
            ax[vec].xaxis.set_major_locator(ticker.MultipleLocator(20))
            ax[vec].xaxis.set_minor_locator(ticker.MultipleLocator(2))
            ax[vec].yaxis.set_major_locator(ticker.MultipleLocator(100))
            ax[vec].yaxis.set_minor_locator(ticker.MultipleLocator(10))
            hrana = np.mean([1110, 1120])
        case 'Cs137':
            ax[vec].set_xlim([640, 680])
            ax[vec].xaxis.set_major_locator(ticker.MultipleLocator(5))
            ax[vec].xaxis.set_minor_locator(ticker.MultipleLocator(1))
            hrana = np.mean([642, 645])
        case 'Eu152':
            ax[vec].set_xlim([0, 600])

    df = pd.read_csv("data/" + name + ".csv")
    y = df[" Counts"].values
    x = df[" Energy (keV)"].values
    y = sf(y, 50, 2)
    peaks = fp(y, height=100)
    yp = peaks[1]['peak_heights']
    xp = x[peaks[0]]

    ax[vec].plot(x, y)
    #ax[vec].scatter(x, y)
    #ax[vec].scatter(xp, yp)
    #plt.axvline(1166.25)
    #plt.axvline(1178.02)
fun1(names[0], (0, 0))
fun1(names[1], (0, 1))
fun1(names[2], (1, 0))
fun1(names[3], (1, 1))
plt.show()
