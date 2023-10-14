import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import Button, Slider

#Voltage is 5V
#at 30 deg it was 0,3 V
#at 0 deg it was 0.8 V
#
t = np.concatenate((np.repeat(100, 7), np.repeat(200, 2), np.repeat(600, 2), np.repeat(900, 2)))
ang = np.array([0, 5, -5, 10, -10, 15, -15, 20, -20, 25, -25, 30, -30])
angl = np.linspace(0, 10, 300)
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
#plt.scatter(ang, N)
plt.plot(angl, np.divide(1, np.sin(angl)))
plt.show()
