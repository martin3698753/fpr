import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

yellow_grad = ['#D24E01', '#DC6601', '#FE8401', '#EC9006', '#EE9f27']

##Data
##Sodium
sod_f = np.array([313])
#sod_sec_l = np.array([292.4167, 292])
#sod_sec_r = np.array([333.716, 333.616])
#sod_tri_l = np.array([268.166, 268.25, 268.55])
#sod_tri_r = np.array([358.7, 358.833, 358.833])
sod_l = np.array([292.4167, 292, 268.166, 268.25, 268.55])
sod_r = np.array([333.716, 333.616, 358.7, 358.833, 358.833])
theta = np.zeros(5)
for i in range(5):
    theta[i] = (sod_r[i] - sod_l[i])/2

sod = np.concatenate((sod_l, sod_f, sod_r), axis=0)
sod = np.sort(sod)
plt.figure(figsize=(16, 4), dpi=120)
for i in range(sod.size):
    plt.axvline(sod[i], c=random.choice(yellow_grad), lw=0.5)
plt.savefig("pics/sod.pdf")
plt.cla()

d = np.zeros(5)
for i in range(2):
    d[i] = (1*589.592*10**(-9)) / np.sin(np.deg2rad(theta[i]))
for i in range(2,5):
    d[i] = (2*589.592*10**(-9)) / np.sin(np.deg2rad(theta[i]))

dk = np.mean(d)

difraction = np.array([1, 1, 2, 2, 2])
sod_df = pd.DataFrame(
    {
        "doleva":sod_l,
        "doprava":sod_r,
        "difrakce":difraction,
        "difrakcni uhel":theta,
        "mrizka e6":np.multiply(d, 10**6),
    }
)
sod_df = sod_df.round(3)
sod_df.to_csv("tabs/sod.csv", index=False)
#print(sod_df)
#print("d mean: ", dk, "| d std: ", np.std(d, ddof=1))
##Hydrogen
hyd_f = np.array([313])
hyd_l = np.array([295.666, 290, 277.166])
hyd_r = np.array([327.666, 330, 336])
theta_h = np.zeros(3)
lam = np.zeros(3)
for i in range(2):
    theta_h[i] = (hyd_r[i] - hyd_l[i])/2
    lam[i] = (dk * np.sin( np.deg2rad(theta_h[i]) ))/(1)
for i in range(2,3):
    theta_h[i] = (hyd_r[i] - hyd_l[i])/2
    lam[i] = (dk * np.sin( np.deg2rad(theta_h[i]) ))/(2)
rh = np.zeros(3)

col_df = pd.DataFrame(
    {
        "n2":np.arange(3,8),
        "lambda":np.array([656, 486, 434, 410, 397]),
        "colors":np.array(["red", "teal", "blue", "indigo", "violet"])
    }
)
col_df.to_csv("tabs/colors.csv", index=False)

rh[0] = (1/(lam[0])) * ( (1/(2**2)) - (1/(4**2)) )**(-1)
rh[1] = (1/(lam[1])) * ( (1/(2**2)) - (1/(3**2)) )**(-1)
rh[2] = (1/(lam[2])) * ( (1/(2**2)) - (1/(6**2)) )**(-1)

colors = np.array(["modrozelená", "červená", "indigo"])
dif = np.array([1, 1, 2])
hyd_df = pd.DataFrame(
    {
        "doleva":hyd_l,
        "doprava":hyd_r,
        "theta":theta_h,
        "difrakce":dif,
        "lambda[nm]":np.multiply(lam, 10**9),
        "color":colors,
        "rh e6":np.multiply(rh, 10**(-6)),
    }
)
hyd_df = hyd_df.round(3)
mp = 1.672721777*10**(-27)
me = 9.10938215*10**(-31)
c = 299792458
e0 = 8.8541878176*10**(-12)
e = 1.602176634*10**(-19)
rh_inf = np.mean(rh) * ((mp + me)/mp)
#print(rh_inf)
#print( ((me * e**4) / (8*e0**2 * rh_inf * c))**(1/3) )
print(hyd_df)
print("rh_inf ", rh_inf)
