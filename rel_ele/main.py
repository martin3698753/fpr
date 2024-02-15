import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from scipy.signal import savgol_filter as sf
from scipy.signal import find_peaks as fp

def edge_theory(emax):
    me = 510.998
    up = 2*emax**2
    down = 2*emax + me
    return (up/down)

names = ['Cs137', 'Co60', 'Na22', 'Y88', 'Y88b', 'Eu152']
def fun2(name):
    fig, ax = plt.subplots(2, 1)
    fig.tight_layout()
    df = pd.read_csv("data/" + name + ".csv")
    y = df[" Counts"].values
    x = df[" Energy (keV)"].values
    y = sf(y, 50, 2)

    match name:
        case 'Co60':
            fig, ax = plt.subplots(3, 1)
            #ax[0].set_xlim([800, 1300])
            #ax[0].xaxis.set_major_locator(ticker.MultipleLocator(100))
            #ax[0].xaxis.set_minor_locator(ticker.MultipleLocator(10))
            ax[1].set_xlim([900, 1000])
            ax[1].set_ylim([0, 30])
            ax[1].xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[1].xaxis.set_minor_locator(ticker.MultipleLocator(2))
            ax[1].yaxis.set_major_locator(ticker.MultipleLocator(100))
            ax[1].yaxis.set_minor_locator(ticker.MultipleLocator(10))
            l = 958
            r = 962
            ax[1].axvline(l)
            ax[1].axvline(r)
            hrana = np.mean([l, r])

            ax[2].set_xlim([1100, 1200])
            ax[2].set_ylim([0, 30])
            ax[2].xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[2].xaxis.set_minor_locator(ticker.MultipleLocator(2))
            ax[2].yaxis.set_major_locator(ticker.MultipleLocator(100))
            ax[2].yaxis.set_minor_locator(ticker.MultipleLocator(10))
            l = 1114
            r = 1122
            ax[2].axvline(l)
            ax[2].axvline(r)
            hranb = np.mean([l, r])
        case 'Cs137':
            fig, ax = plt.subplots(2, 1)
            ax[0].set_xlim([200, 680])
            ax[0].xaxis.set_major_locator(ticker.MultipleLocator(100))
            ax[0].xaxis.set_minor_locator(ticker.MultipleLocator(10))
            ax[1].set_ylim([0, 60])
            ax[1].set_xlim([400, 700])
            ax[1].xaxis.set_major_locator(ticker.MultipleLocator(100))
            ax[1].xaxis.set_minor_locator(ticker.MultipleLocator(10))
            l = 470
            r = 490
            plt.axvline(l)
            plt.axvline(r)
            hrana = np.mean([l, r])
        case 'Na22':
            fig, ax = plt.subplots(3, 1)
            #ax[0].set_xlim([200, 600])
            #ax[0].xaxis.set_major_locator(ticker.MultipleLocator(100))
            #ax[0].xaxis.set_minor_locator(ticker.MultipleLocator(10))
            ax[1].set_ylim([0, 100])
            ax[1].set_xlim([200, 400])
            ax[1].xaxis.set_major_locator(ticker.MultipleLocator(100))
            ax[1].xaxis.set_minor_locator(ticker.MultipleLocator(10))
            l = 330
            r = 360
            ax[1].axvline(l)
            ax[1].axvline(r)
            hrana = np.mean([l, r])

            ax[2].set_ylim([0, 10])
            ax[2].set_xlim([1040, 1090])
            ax[2].xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[2].xaxis.set_minor_locator(ticker.MultipleLocator(1))
            l = 1061
            r = 1063
            ax[2].axvline(l)
            ax[2].axvline(r)
            hranb = np.mean([l, r])
        case 'Y88':
            fig, ax = plt.subplots(3, 1)
            ax[0].set_ylim([0, 7000])
            ax[0].set_xlim([500, 1600])
            ax[0].xaxis.set_major_locator(ticker.MultipleLocator(100))
            ax[0].xaxis.set_minor_locator(ticker.MultipleLocator(10))
            ax[1].set_ylim([100, 500])
            ax[1].set_xlim([650, 750])
            ax[1].xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[1].xaxis.set_minor_locator(ticker.MultipleLocator(1))
            ax[2].set_ylim([0, 500])
            ax[2].set_xlim([1200, 1300])
            ax[2].xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[2].xaxis.set_minor_locator(ticker.MultipleLocator(1))
            l = 685
            r = 710
            plt.axvline(l)
            plt.axvline(r)
            hrana = np.mean([l, r])


    fig.tight_layout()
    df = pd.read_csv("data/" + name + ".csv")
    y = df[" Counts"].values
    x = df[" Energy (keV)"].values
    y = sf(y, 50, 2)

    if (name == "Y88"):
        peaks = fp(y, height=2000)
    else:
        peaks = fp(y, height=100)
    yp = peaks[1]['peak_heights']
    xp = x[peaks[0]]
    for i in range(3):
        ax[i].scatter(xp, yp)
        ax[i].plot(x, y)
        ax[i].grid(axis='x', which='both')

    plt.savefig("figs/" + name + ".pdf")
    plt.show()
#fig, ax = plt.subplots(2, 2)
#fig.tight_layout()
#def fun1(name, vec):
#    match name:
#        case 'Co60':
#            #ax[vec].set_xlim([1100, 1200])
#            #ax[vec].set_ylim([0, 30])
#            ax[vec].xaxis.set_major_locator(ticker.MultipleLocator(20))
#            ax[vec].xaxis.set_minor_locator(ticker.MultipleLocator(2))
#            ax[vec].yaxis.set_major_locator(ticker.MultipleLocator(100))
#            ax[vec].yaxis.set_minor_locator(ticker.MultipleLocator(10))
#            hrana = np.mean([1110, 1120])
#        case 'Cs137':
#            #ax[vec].set_xlim([640, 680])
#            ax[vec].xaxis.set_major_locator(ticker.MultipleLocator(5))
#            ax[vec].xaxis.set_minor_locator(ticker.MultipleLocator(1))
#            hrana = np.mean([642, 645])
#        case 'Eu152':
#            #ax[vec].set_xlim([0, 600])
#            ax[vec].xaxis.set_major_locator(ticker.MultipleLocator(5))
#            ax[vec].xaxis.set_minor_locator(ticker.MultipleLocator(1))
#
#    df = pd.read_csv("data/" + name + ".csv")
#    y = df[" Counts"].values
#    x = df[" Energy (keV)"].values
#    #y = sf(y, 50, 2)
#    peaks = fp(y, height=100)
#    yp = peaks[1]['peak_heights']
#    xp = x[peaks[0]]
#
#    ax[vec].plot(x, y)
#    #ax[vec].scatter(x, y)
#    #ax[vec].scatter(xp, yp)
#    #plt.axvline(1166.25)
#    #plt.axvline(1178.02)
#fun1(names[0], (0, 0))
#fun1(names[1], (0, 1))
#fun1(names[2], (1, 0))
#fun1(names[3], (1, 1))
#plt.show()
fun2(names[3])
