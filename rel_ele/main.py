import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from scipy.signal import savgol_filter as sf
from scipy.signal import find_peaks as fp

c = 299792458
me = 510.998950
e = 1.602176634*10**(-19)

def proloz(x, y, c, label):
    x = np.sort(x)
    y = np.sort(y)
    a = np.polyfit(x, y, 1)
    plt.plot(x, a[0]*x+a[1], c=c, label=label)

def edge_theory(emax):
    me = 510.998
    up = 2*emax**2
    down = 2*emax + me
    return (up/down)

names = ['Cs137', 'Co60', 'Na22', 'Y88']
def fun2(name):
    edges = np.empty(1)
    edges_err = np.empty(1)
    pk = np.empty(1)

    match name:
        case 'Co60':
            fig, ax = plt.subplots(3, 1)
            #ax[0].set_xlim([800, 1300])
            #ax[0].xaxis.set_major_locator(ticker.MultipleLocator(100))
            #ax[0].xaxis.set_minor_locator(ticker.MultipleLocator(10))
            ax[1].set_xlim([940, 1020])
            ax[1].set_ylim([10, 30])
            ax[1].xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[1].xaxis.set_minor_locator(ticker.MultipleLocator(2))
            ax[1].yaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[1].yaxis.set_minor_locator(ticker.MultipleLocator(5))
            l = 950
            r = 990
            ax[1].axvline(l)
            ax[1].axvline(r)
            hrana = np.mean([l, r])
            edges[0] = hrana
            edges_err[0] = np.std([l, r])

            ax[2].set_xlim([1100, 1160])
            ax[2].set_ylim([0, 20])
            ax[2].xaxis.set_major_locator(ticker.MultipleLocator(15))
            ax[2].xaxis.set_minor_locator(ticker.MultipleLocator(5))
            ax[2].yaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[2].yaxis.set_minor_locator(ticker.MultipleLocator(5))
            l = 1115
            r = 1135
            ax[2].axvline(l)
            ax[2].axvline(r)
            hrana = np.mean([l, r])
            edges = np.append(edges, hrana)
            edges_err = np.append(edges_err, np.std([l, r]))
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
            r = 500
            plt.axvline(l)
            plt.axvline(r)
            hrana = np.mean([l, r])
            edges[0] = hrana
            edges_err[0] = np.std([l, r])

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
            ax[1].set_ylim([0, 50])
            ax[1].set_xlim([250, 450])
            ax[1].xaxis.set_major_locator(ticker.MultipleLocator(100))
            ax[1].xaxis.set_minor_locator(ticker.MultipleLocator(10))
            l = 330
            r = 360
            ax[1].axvline(l)
            ax[1].axvline(r)
            hrana = np.mean([l, r])
            edges[0] = hrana
            edges_err[0] = np.std([l, r])

            ax[2].set_ylim([2, 8])
            ax[2].set_xlim([1050, 1080])
            ax[2].xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[2].xaxis.set_minor_locator(ticker.MultipleLocator(1))
            l = 1055
            r = 1070
            ax[2].axvline(l)
            ax[2].axvline(r)
            hrana = np.mean([l, r])
            edges = np.append(edges, hrana)
            edges_err = np.append(edges_err, np.std([l, r]))
        case 'Y88':
            fig, ax = plt.subplots(3, 1)
            ax[0].set_ylim([0, 7000])
            ax[0].set_xlim([400, 1600])
            #ax[0].xaxis.set_major_locator(ticker.MultipleLocator(100))
            #ax[0].xaxis.set_minor_locator(ticker.MultipleLocator(10))
            ax[1].set_ylim([200, 350])
            ax[1].set_xlim([680, 740])
            ax[1].xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[1].xaxis.set_minor_locator(ticker.MultipleLocator(5))
            l = 690
            r = 720
            ax[1].axvline(l)
            ax[1].axvline(r)
            hrana = np.mean([l, r])
            edges[0] = hrana
            edges_err[0] = np.std([l, r])

            ax[2].set_ylim([90, 125])
            ax[2].set_xlim([1230, 1250])
            ax[2].xaxis.set_major_locator(ticker.MultipleLocator(10))
            ax[2].xaxis.set_minor_locator(ticker.MultipleLocator(1))
            l = 1243
            r = 1247
            plt.axvline(l)
            plt.axvline(r)
            hrana = np.mean([l, r])
            edges = np.append(edges, hrana)
            edges_err = np.append(edges_err, np.std([l, r]))


    fig.tight_layout()
    df = pd.read_csv("data/" + name + ".csv")
    y = df[" Counts"].values
    x = df[" Energy (keV)"].values
    y = sf(y, 50, 2)
    #fig.supxlabel("Energie [keV]")
    #fig.supylabel("počet detekovaných kvant")
    fig.text(0.5, 0.015, 'Energie [keV]', ha='center', va='center', fontproperties={'weight': 'normal', 'style': 'italic'})
    fig.text(0.01, 0.5, 'Počet detekovaných kvant', ha='center', va='center', rotation='vertical')

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
    plt.clf()
    #plt.show()
    return(edges, edges_err)

#edg = np.empty(0, dtype=int)
#edg_er = np.empty(0, dtype=int)
#for n in names:
    #print(fun2(n))

nms = ['Cs137', 'Co60', '-', 'Na22', '-', 'Y88', ' -']
peak_data = np.array([661.666, 1173.3245, 1332.5978, 551.03069, 1274.69751831, 897.96597451, 1460.7852461])
edg = np.array([485, 970, 1125, 345, 1062.5, 705, 1245])
edg_t = np.array
edg_er = np.array([15, 20, 10, 15, 7.5, 15, 2])
p = (2*peak_data - edg)
##p = np.sqrt(edg*2*me)
Tk = p**2/(2*me)
Tr = np.sqrt(p**2 + me**2) - me
df1 = pd.DataFrame(
    {
        "name":nms,
        "peaks":peak_data,
        "edges":edg,
        "edges_error":edg_er,
        "momentum":p,
    }
)
df1 = df1.round(3)
#df1.to_csv("figs/df1.csv", index=False)
print(df1)
p = np.sort(p)
edg = np.sort(edg)
edg_er = np.sort(edg_er)
plt.errorbar(p, edg, edg_er, fmt='o', linewidth=2, capsize=6, label="naměřená data")
#proloz(p, edg, 'blue', 'lxxx')
proloz(p, Tk, 'green', 'klasická')
proloz(p, Tr, 'red', 'relativistická')
plt.xlabel(r"$p [\frac{KeV}{c^2}]$")
plt.ylabel(r"$T [KeV]$")
plt.legend()
#plt.savefig("figs/fig1.pdf")
#plt.show()
