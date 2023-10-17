import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, argrelextrema

plt.rcParams['text.usetex'] = True

e = 1.60217*10**(-19)
h = 6.62607*10**(-34)
c = 299792458

neon_min = np.array([26.4, 44, 64.1])
hg_min = np.array([28.6, 33.4, 38.3, 43.1, 47.9, 52.7, 57.5, 62.3, 68.1, 72.7, 77.7])

def par_er2(sigma):
    print("Excit error = ", e*sigma)
    return (e*sigma)

def par_er(E, sigma):
    in_sq_up = ((c*E) + (h*c))*par_er2(sigma)
    in_sq_dw = h*c
    return np.sqrt(((in_sq_up)/in_sq_dw)**2)

def err(ar):
    le = ar.shape[0]
    sig = 0
    for i in range(le):
        sig += (np.mean(ar) - ar[i])**2
    return (np.sqrt( sig / (le*(le-1)) ))

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
    #plt.savefig("data/" + name + ".pdf")
    tab_min = np.zeros(tab.shape[0])
    for i in range(tab.shape[0]-1):
        tab_min[i+1] = tab[i+1] - tab[i]

    df_min = pd.DataFrame(
        {
            "Ua":tab,
            "delta Ua":tab_min,
        }
    )
    df_min = df_min.round(3)
    df_min.to_csv("data/" + name + ".csv")

    tab_min = np.delete(tab_min, 0)
    vlnocet = e*np.mean(tab_min) / (h*c)
    print(name + "  --------------")
    print("U mean = ", np.mean(tab_min))
    print("U err = ", err(tab_min))
    print("Excit = ", e*np.mean(tab_min))
    print("vlnocet = ", vlnocet)
    print("vlnocet er = ", par_er(np.mean(tab_min)*e, err(tab_min)))
    #plt.show()

mes("hg")
mes("neon")
