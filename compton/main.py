import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/Co60.csv", comment='#')
x = df[" Energy (keV)"]
y = df[" Counts"]
plt.xlim(800, 1600)
plt.plot(x, y)
plt.show()
