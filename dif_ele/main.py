import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dc = 0.0575

x = np.linspace(0.01, 1, 1000)

def r(e):
    a = np.add(80**2, np.power(e, 2))
    b = np.multiply(np.subtract(80, e), np.sqrt(2))
    return np.multiply(np.divide(a, b), 0.001)

def mag(I):
    r = 0.062
    u0 = 1.256637*10**(-6)
    n = 320
    a = (4/5)**(3/2)
    b = np.multiply((u0 * n)/r, I)
    return (np.multiply(a, b))

def qm(I, e, U):
    a = np.multiply(2, U)
    b = np.power( np.multiply(mag(I), r(e)), 2 )
    return np.divide(a, b)

d1 = np.array([26, 25, 25, 26, 25, 23])
d2 = np.array([44, 42, 42, 40, 39, 38])

rings = pd.DataFrame(
    {
        "Napeti":np.arange(4, 5.1, 0.2),
        "d1":d1,
        "d2":d2,
    }
)
rings = rings.round(3)
rings.to_csv("data/rings.csv", index=False)

ohyb = np.arange(40, -1, -10)
proud = np.array([
    [0.47, 0.67, 0.87, 1.08, 1.24],
    [0.58, 0.82, 1.08, 1.33, 1.56],
    [0.69, 0.97, 1.24, 1.54, 1.79],
    [0.73, 1.03, 1.34, 1.66, 1.93]
])

proud = np.divide(proud, 2)

coils_cur = pd.DataFrame(
    {
        "ohyb":ohyb,
        "proud1":proud[0],
        "proud2":proud[1],
        "proud3":proud[2],
        "proud4":proud[3],

    }
)
coils_cur.to_csv("data/coils_cur.csv", index=False)


coils_charge = pd.DataFrame(
    {
        "qm1":qm(proud[0], ohyb, 2000)*10**(-11),
        "qm2":qm(proud[1], ohyb, 3000)*10**(-11),
        "qm3":qm(proud[2], ohyb, 4000)*10**(-11),
        "qm4":qm(proud[3], ohyb, 5000)*10**(-11),
    }
)
qm_all = np.concatenate((qm(proud[0], ohyb, 2000), qm(proud[1], ohyb, 3000), qm(proud[2], ohyb, 4000), qm(proud[3], ohyb, 5000)))
print(np.mean(qm_all) * 10**(-11))
print(np.std(qm_all) * 10**(-11))
e = 1.602176634*10**(-19)
print(e/(np.mean(qm_all)))
print(e/(np.std(qm_all)))

coils_charge = coils_charge.round(3)
coils_charge.to_csv("data/coils_charge.csv", index=False)

#### Dif circles ####

def lam(V):
    V = np.multiply(V, 1000)
    h = 6.62607015*10**(-34)
    me = 9.1093837015*10**(-31)
    e = 1.602176634*10**(-19)
    b = np.sqrt( np.multiply(V, 2*e*me) )
    return np.divide(h, b)

def d(lam, d1):
    n = lam
    L = 135
    R = 65
    l = np.add(L-R, np.sqrt(np.subtract(R**2, np.divide( np.power(d1, 2), 4))))
    alpha = np.multiply(1/2, np.arctan(np.divide(d1, np.multiply(2, l))))
    return np.divide(n, np.multiply(2, np.sin(alpha)))

V = np.arange(4, 5.1, 0.2)
dif_circle = pd.DataFrame(
    {
        "voltage":V,
        "d1_v":d(lam(V), d1)*10**12,
        "d2_v":d(lam(V), d2)*10**12,
    }
)
dif_circle = dif_circle.round(3)
dif_circle.to_csv("data/dif_circle.csv", index=False)
#print(np.mean(d(lam(V), d1))*10**12)
#print(np.std(d(lam(V), d1))*10**12)
#print(np.mean(d(lam(V), d2))*10**12)
#print(np.std(d(lam(V), d2))*10**12)
