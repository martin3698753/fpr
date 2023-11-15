import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks as fp

plt.rc('text', usetex=True)

def graph(name, i):
    df = pd.read_csv("data/" + str(f'{name:g}') + ".csv", index_col=0)
    df = df.sort_values(by=['Input_A [V]'])
    x = df['Input_A [V]'].values
    y = df['Input_B [V]'].values
    peaks = fp(y, height=0.5, threshold=None)
    height = peaks[1]['peak_heights']
    index = x[peaks[0]][0]
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
