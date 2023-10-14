import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def mes(name):
    mess = pd.read_csv(name + ".csv")
    print(mess)
    print(mess['Input_A [V]']*10)

