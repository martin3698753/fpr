import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from scipy.signal import savgol_filter as sf
from scipy.signal import find_peaks as fp

plt.rc('text', usetex=True)
c = 299792458
me = 510.998950
e = 1.602176634*10**(-19)

def plot_line(x, y, c, label):
    x = np.sort(x)
    y = np.sort(y)
    plt.scatter(x, y, c=c)
    a = np.polyfit(x, y, 2)
    plt.plot(x, a[0]*x**2+a[1]*x+a[2], c=c, label=label)

df1 = pd.read_csv("figs/df1.csv", index_col=False)
p = df1.momentum
T = df1.Tk
Tr = df1.Tr
plot_line(p, T, 'blue', 'klasická')
plot_line(p, Tr, 'red', 'relativistická')
plt.xlabel(r"$p [\frac{KeV}{c^2}]$")
plt.ylabel(r"$T [KeV]$")
plt.legend()
plt.savefig("figs/fig1.pdf")
plt.show()
