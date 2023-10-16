import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, argrelextrema

plt.rcParams['text.usetex'] = True

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

    #plt.xticks(np.append(np.arange(0, 100, 10), mess['min']))
    plt.show()
    print(mess.to_markdown())

mes("neon")
