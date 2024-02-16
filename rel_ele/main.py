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

names = ['Cs137', 'Co60', 'Na22', 'Y88']
def fun2(name):
    edges = np.empty(1)
    pk = np.empty(1)

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
            edges[0] = hrana

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
            hrana = np.mean([l, r])
            edges = np.append(edges, hrana)
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
            edges[0] = hrana

        case 'Eu152':
            fig, ax = plt.subplots(2, 1)
            #ax[0].set_xlim([200, 680])
           # ax[0].xaxis.set_major_locator(ticker.MultipleLocator(100))
           # ax[0].xaxis.set_minor_locator(ticker.MultipleLocator(10))
           # ax[1].set_ylim([0, 60])
           # ax[1].set_xlim([400, 700])
           # ax[1].xaxis.set_major_locator(ticker.MultipleLocator(100))
           # ax[1].xaxis.set_minor_locator(ticker.MultipleLocator(10))
           # l = 470
           # r = 490
           # plt.axvline(l)
           # plt.axvline(r)
           # hrana = np.mean([l, r])
           # edges = np.append(edges, hrana)

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
            edges[0] = hrana

            ax[2].set_ylim([0, 10])
            ax[2].set_xlim([1040, 1090])
            ax[2].xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[2].xaxis.set_minor_locator(ticker.MultipleLocator(1))
            l = 1061
            r = 1063
            ax[2].axvline(l)
            ax[2].axvline(r)
            hrana = np.mean([l, r])
            edges = np.append(edges, hrana)
        case 'Y88':
            fig, ax = plt.subplots(3, 1)
            ax[0].set_ylim([0, 7000])
            #ax[0].set_xlim([500, 1600])
            ax[0].xaxis.set_major_locator(ticker.MultipleLocator(100))
            ax[0].xaxis.set_minor_locator(ticker.MultipleLocator(10))
            ax[1].set_ylim([100, 400])
            ax[1].set_xlim([650, 750])
            ax[1].xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[1].xaxis.set_minor_locator(ticker.MultipleLocator(1))
            l = 695
            r = 706
            ax[1].axvline(l)
            ax[1].axvline(r)
            hrana = np.mean([l, r])
            edges[0] = hrana

            ax[2].set_ylim([70, 160])
            ax[2].set_xlim([1230, 1250])
            ax[2].xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[2].xaxis.set_minor_locator(ticker.MultipleLocator(1))
            l = 1244
            r = 1247
            plt.axvline(l)
            plt.axvline(r)
            hrana = np.mean([l, r])
            edges = np.append(edges, hrana)


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
    for i in range(ax.shape[0]):
        ax[i].scatter(xp, yp)
        ax[i].plot(x, y)
        ax[i].grid(axis='x', which='both')

    plt.savefig("figs/" + name + ".pdf")
    #plt.clf()
    plt.show()
    return(edges)

edg = np.empty(0, dtype=int)
for n in names:
    edg = np.append(edg, fun2(n))

nms = ['Cs137', 'Co60', '', 'Na22', '', 'Y88', '']
peak_data = np.array([661.666, 1173.3245, 1332.5978, 551.03069, 1274.69751831, 897.96597451, 1460.7852461])
df1 = pd.DataFrame(
    {
        "name":nms,
        "peaks":peak_data,
        "edges":edg,
    }
)
print(df1)
