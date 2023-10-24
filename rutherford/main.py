#Resource
#http://hyperphysics.phy-astr.gsu.edu/hbase/rutsca.html

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import Button, Slider

#Voltage is 5V
#at 30 deg it was 0,3 V
#at 0 deg it was 0.8 V
#
plt.rcParams['text.usetex'] = True

def graph(angl):
    angl = angl * (np.pi/180)
    a = 0.00056
    b = 0.055
    dw = np.sin((angl-b)/(2))**4
    return (a/dw)

t = np.concatenate((np.repeat(100, 7), np.repeat(200, 2), np.repeat(600, 2), np.repeat(900, 2)))
ang = np.array([0, 5, -5, 10, -10, 15, -15, 20, -20, 25, -25, 30, -30])
angl = np.linspace(-30, 30, 10000)
n = np.array([1258, 1339, 806, 975, 311, 437, 109, 203, 78, 186, 39, 104, 300])
N = np.divide(n, t)

df = pd.DataFrame(
    {
        "angle":ang,
        "num_of_a":n,
        "time":t,
        "N":N
    }
)
df = df.round(3)
df.to_csv("data/data1.csv", index=False)
#print(df)
plt.scatter(ang, N, label="data")
plt.plot(angl, graph(angl), c='green', label=r"$f(\theta)$")
plt.ylim(0, 50)
plt.xlabel("úhel rozptylu " + r"$\theta$", fontsize=12)
plt.ylabel("četnost částic " + r"$N(\theta)$", fontsize=12)
plt.annotate(r"$A = 56 \cdot 10^{-6}$", xy=(-30, 40))
plt.annotate(r"$B = 55 \cdot 10^{-3}$", xy=(-30, 38))
plt.legend()
plt.savefig("data/graph1.pdf")
#plt.show()
