import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dc = 0.0575

rings = pd.DataFrame(
    {
        "Napeti":np.arange(4, 5.1, 0.2),
        "d1":np.array([2.6, 2.5, 2.5, 2.6, 2.5, 2.3]),
        "d2":np.array([4.4, 4.2, 4.2, 4, 3.9, 3.8]),
    }
)

ohyb = np.arange(0.04, 0.081, 0.01)
proud = np.array([
    [0.47, 0.67, 0.87, 1.08, 1.24],
    [0.58, 0.82, 1.08, 1.33, 1.56],
    [0.69, 0.97, 1.24, 1.54, 1.79],
    [0.73, 1.03, 1.34, 1.66, 1.93]
])

coils = pd.DataFrame(
    {

    }
)

print(ohyb[0])
