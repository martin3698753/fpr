import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter as sf
from scipy.signal import find_peaks as fp

names = ['Co60', 'Cs137', 'Eu152', 'Na22', 'Y88']

def fun1(name):
    match name:
        case "Co60":
            plt.xlim(1000, 1500)


    df = pd.read_csv("data/" + name + ".csv")
    y = df[" Counts"].values
    x = df[" Energy (keV)"].values
    w = sf(y, 50, 2)
    peaks = fp(w, height=100)
    yp = peaks[1]['peak_heights']
    xp = x[peaks[0]]
    plt.plot(x, w)
    #plt.scatter(xp, yp)
    #plt.axvline(1166.25)
    #plt.axvline(1178.02)
    plt.show()
for n in names:
    fun1(n)
