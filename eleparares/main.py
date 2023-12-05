import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks as fp
from scipy.optimize import curve_fit

plt.rc('text', usetex=True)
res = np.zeros(8)
freq = np.zeros(8)

def graph(name, i):
    df = pd.read_csv("data/" + str(f'{name:g}') + ".csv", index_col=0)
    df = df.sort_values(by=['Input_A [V]'])
    x = df['Input_A [V]'].values
    y = df['Input_B [V]'].values
    peaks = fp(y, height=0.5, threshold=None)
    height = peaks[1]['peak_heights']
    index = x[peaks[0]][0]

    res[i-1] = index
    freq[i-1] = name

    plt.scatter(index, height)
    plt.axhline(y=height, linestyle='--', lw=0.8, c='green')
    plt.axvline(x=index, linestyle='--', lw=0.8, c='green')
    plt.plot(x, y)
    plt.grid(linestyle='-.')
    if (i<7):
        plt.xticks(np.append(np.array([0, 0.2, 0.4, 0.8]), index))
    else:
        plt.xticks(np.append(np.array([0, 0.2, 0.4]), index))
    plt.yticks(np.append(np.array([-0.5, 0, 1.5, 2]), height))
    plt.title("Frekvence " + str(name) + " MHz")
    plt.axhline(y=0, c='black', linestyle='--', lw=1)
    plt.xlabel(r"Napětí budící magnetické pole $U_A [V]$")
    plt.ylabel(r"Napětí odezvy vzorku $U_B [V]$")
    plt.savefig("figs/" + str(i) + ".pdf")
    plt.cla()

files = os.listdir("data")
for i in range(len(files)):
    files[i] = float(files[i][:-4])
files = sorted(files)
for i in range(1,9):
    graph(files[i], i)

magf = np.array(np.multiply(3.648,res))
ub = 9.27401*10**(-24)
h = 6.62607*10**(-34)
g = np.array(np.divide( np.multiply(freq, h), np.multiply(magf, ub) ))

coeff = np.polyfit(freq, magf, deg=1)
fitc = np.poly1d(coeff)
xspace = np.linspace(min(freq), max(freq), 10000)

resd = pd.DataFrame(
    {
        "Freq":freq,
        "Res_voltage":res,
        "Mag field Br":magf,
        "g_faktor":np.multiply(g, 10**9)
    }
)
resd = resd.round(3)
resd.to_csv("figs/resd.csv")
print(resd)
print(np.mean(g))
print(np.std(g, ddof=1))
plt.xlabel("Rezonanční frekvence " + r"$f_r [Mhz]$")
plt.ylabel("Rezonanční magnetické pole " + r"$B_r [mT]$")
plt.scatter(freq, magf, label=r"$B_r(f_r)$")
coeff = np.round(coeff, 3)
plt.plot(xspace, fitc(xspace), "--", label=str(coeff[0]) + r"$f_r$" + r"$+$" + str(coeff[1]))
plt.legend()
plt.savefig("figs/resd.pdf")
plt.cla()
#plt.show()
