import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, argrelextrema

plt.rcParams['text.usetex'] = True

neon_min = np.array([26.4, 44, 64.1])
hg_min = np.array([28.6, 33.4, 38.3, 43.1, 47.9, 52.7, 57.5, 62.3, 68.1, 72.7, 77.7])

def mes(name):
    mess = pd.read_csv(name + ".csv", index_col=0)
    mess['Input_A [V]'] = mess['Input_A [V]']*10
    #mess = mess.drop(columns='N')
    mess = mess.sort_values("Input_A [V]")
    plt.title("Frank-Hertzova křivka pro " + name)
    plt.xlabel(r'Urychlovací napětí $U_{A} [V]$')
    plt.ylabel(r'Anodový proud přepočtený na napětí $U_{B} [V]$')
    plt.scatter(mess['Input_A [V]'], mess['Input_B [V]'])
    plt.plot(mess['Input_A [V]'], mess['Input_B [V]'])

    mess['min'] = mess.iloc[argrelextrema(mess['Input_B [V]'].values, np.less_equal,
                                          order=2)[0]]['Input_B [V]']
    plt.scatter(mess['Input_A [V]'], mess['min'], c='r')
    plt.grid(axis='x', linestyle='--')

    if(name == "neon"):
        plt.xticks(np.append(np.arange(0, 80, 10), neon_min))
        tab = neon_min
    if(name == "hg"):
        plt.xticks(np.append(np.array([0, 10, 20]), hg_min))
        tab = hg_min
    #print(mess.to_markdown())
    #plt.show()
    tab_min = np.zeros(tab.shape[0])
    for i in range(tab.shape[0]-1):
        tab_min[i+1] = tab[i+1] - tab[i]

    df_min = pd.DataFrame(
        {
            "Ua":tab,
            "delta Ua":tab_min
        }
    )
    print(df_min)

mes("neon")
