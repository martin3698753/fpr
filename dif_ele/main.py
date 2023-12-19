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

rings = pd.DataFrame(
    {
        "Napeti":np.arange(4, 5.1, 0.2),
        "d1":np.array([2.6, 2.5, 2.5, 2.6, 2.5, 2.3]),
        "d2":np.array([4.4, 4.2, 4.2, 4, 3.9, 3.8]),
    }
)

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


coils_charge = pd.DataFrame(
    {
        "qm1":qm(proud[0], ohyb, 2000),
        "qm2":qm(proud[1], ohyb, 3000),
        "qm3":qm(proud[2], ohyb, 4000),
        "qm4":qm(proud[3], ohyb, 5000),
    }
)

#### Dif circles ####
dif_circle = pd.DataFrame(
    {
        "voltage":np.arange(4, 5.1, 0.2),
        "d1":np.array(26, 25, 25, 26, 25, 23),
        "d2":np.array(44, 42, 42, 40, 39, 38),
    }
)
