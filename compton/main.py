import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter as sf
from scipy.signal import find_peaks as fp

#Start Time, Sat Nov 22 09:14:03 GMT+0100 2014
#Energy calibration,  Offset: 0, Slope: 0.43199265003204346, Quadratic: 0
#Live Time (s), 564.497145
#Real Time (s), 600
#Elapsed Computational, 0
#Spectrum
#Channel, Energy (keV), Counts
plt.rc('text', usetex=True)

angs = np.array(['0', '10', '20', '30', '40', '50', '60', '70'])
energy = np.zeros(8)
energy_c = np.zeros(8)
c = 299792458
e = 1.6*10**(-19)

fig, ax = plt.subplots(4, 2)
fig.tight_layout()
def fun1(angle, vec, h, index):
    df = pd.read_csv("data/" + angle + "stA.csv", comment='#')
    x = df[" Energy (keV)"]
    y = df[" Counts"]
    y = sf(y, 101, 2)
    peaks = fp(y, height=h, distance=120)
    yp = peaks[1]['peak_heights']
    xp = x[peaks[0]].values
    yp_c = yp
    xp_c = xp

    if (angle == '20' or angle == '30' or angle == '40'):
        yp = yp[1]
        xp = xp[1]
        yp_c = yp_c[2]
        xp_c = xp_c[2]

    if (angle == '50'):
        yp = yp[2]
        xp = xp[2]
        yp_c = yp_c[4]
        xp_c = xp_c[4]
    if (angle == '60'):
        yp = yp[6]
        xp = xp[6]
        yp_c = yp_c[9]
        xp_c = xp_c[9]
    if (angle == '70'):
        yp = yp[5]
        xp = xp[5]
        yp_c = yp_c[8]
        xp_c = xp_c[8]
    energy[index] = xp.item()
    energy_c[index] = xp_c.item()
    ax[vec].scatter(xp, yp, c='blue')
    ax[vec].scatter(xp_c, yp_c, c='red')
    ax[vec].plot(x, y)
    ax[vec].set_title("úhel je " + angle + " stupňů", fontsize=8)

fun1(angs[0], (0,0), 10000, 0)
fun1(angs[1], (0,1), 5000, 1)
fun1(angs[2], (1,0), 500, 2)
fun1(angs[3], (1,1), 300, 3)
fun1(angs[4], (2,0), 250, 4)
fun1(angs[5], (2,1), 150, 5)
fun1(angs[6], (3,0), 50, 6)
fun1(angs[7], (3,1), 40, 7)
plt.savefig("figs/fig1.pdf")
#plt.show()
plt.clf()

angle = angs.astype(int)
angle = np.deg2rad(angle)
angle = 1 - np.cos(angle)

#Fit
a, b = np.polyfit(angle, 1/energy, 1)

fig, ax = plt.subplots()
ax.scatter(angle, 1/energy)
ax.plot(angle, angle*a+b, label=r"$u(x) = -ax + b$")
ax.set_xlabel(r'$1-cos(\theta)$', fontsize=15)
ax.set_ylabel(r'$\frac{1}{E_2}$', fontsize=15)
ax.legend(loc="upper left")
plt.savefig("figs/fig2.pdf")
#plt.show()
plt.clf()
m0 = 1/(a) #ev/c^2
m0 = m0*(1.782662695944*10**(-36))*1000
e1 = 1/b

df = pd.DataFrame(
    {
        "angle":angs,
        "E2":energy,
        "E1":energy_c,
        "1-cosv":angle,
    }
)
print(np.mean(energy_c))
print(np.std(energy_c))
df = df.round(3)
df.to_csv("figs/data1.csv", index=False)
