import numpy as np
import matplotlib.pyplot as plt
import pandas
import seaborn as sns

plt.rcParams['text.usetex'] = True

num = np.arange(1, 16, 1)
voltage = np.array([323, 425, 424, 64, 112, 168, 173, 78, 116, 130, 150, 80, 36, 120, 42])
time = np.array([4.362, 1.588, 4.579, 21.303, 21.303, 2.128, 2.04, 6.738, 13.675, 9.521, 7.563, 11.318, 11.456, 18.594, 11.659])
dilek = np.array([1, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
ds = np.multiply(dilek, 0.0005)

# 1, 8, 13
temp_c = np.array([21.6, 22, 22.1])
temp = np.add(temp_c, 273.15)
phi = np.array([40, 40, 39])
p = np.array([964.7, 965, 965.2])
e = 1.602176*10**(-19)

def make_array(org):
    a = np.zeros(time.size, dtype=object)
    for i in range(a.size):
        if(i == 0):
            a[i] = org[0]
        elif(i == 7):
            a[i] = org[1]
        elif(i == 12):
            a[i] = org[2]
        else:
            a[i] = "-"

    return a

teplota = make_array(temp_c)
tlak = make_array(p)
vlhkost = make_array(phi)
def vis(): #uPa
    n0 = 18.27
    T0 = 291.15
    C = 120
    fr = ((T0+C)/(np.mean(temp)+C))
    sec = (np.mean(temp)/T0)**(3/2)
    return (n0*fr*sec * 10**(-6))

psat = 6.1078*10**(7.5*temp_c/(temp_c+237.3)) #hPa
pv = 0.01*phi*psat #hPa
pd = p-pv #hPa
p1 = (pd*100/(287.058*temp)) + (pv*100/(461.495*temp)) #kg/m^3

#print("vis", vis()*10**(6))
#print("psat", np.mean(psat))
#print("pv", np.mean(pv))
#print("pd", np.mean(pd))
#print("p1", np.mean(p1))

def r(): #m
    g = 9.81
    p2 = 873
    up = vis()*(ds/time)*(9/2)
    down = (p2-np.mean(p1))*g
    return np.sqrt(up/down)

def q(): #C
    p2 = 873
    d = 0.006
    g = 9.81
    out = 9*np.pi*(d/voltage)
    up = 2 * (vis())**3 * (ds/time)**3
    down = (p2-np.mean(p1))*g
    return (out*np.sqrt(up/down))

def qc(): #C
    A = 0.07776 * 10**(-6)
    up = q()
    down = (1+(A/r()))**3
    return (up/np.sqrt(down))

n = qc()/e
n = np.round(n)
n = n.astype(int)

en = qc()/n

df1 = pandas.DataFrame(
    {
        "U":voltage,
        "s":ds*1000,
        "t":time,
        "teplota":teplota,
        "tlak":tlak,
        "vlhkost":vlhkost,

    }
)
df1.to_csv("data/df1.csv", index=False)

df2 = pandas.DataFrame(
    {
        "r":r()*10**6,
        "q":q()*10**(19),
        "qc":qc()*10**(19),
        "n":n,
        "e":en*10**(19),
    }
)
df2 = df2.round(3)
df2.to_csv("data/df2.csv", index=False)

#print(df1)
plt.scatter(r(), q())
plt.xlabel(r"Poloměr kapky $r[m]$")
plt.ylabel(r"Náboj kapky $q[C]$")
plt.savefig("data/graph1.pdf")
plt.cla()

print(n)
sns.histplot(n, kde=True, binwidth=0.5, edgecolor="black")
plt.xticks([1,2,3,4,7,9,26,84])
plt.ylabel("Počet nábojů")
plt.xlabel("Četnost")
plt.savefig("data/hist.pdf")
