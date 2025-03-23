# U direktoriju PSU_LV/LV2/ nalazi se datoteka mtcars.csv koja sadrži različita mjerenja provedena na 32
# automobila (modeli 1973-74). Opis pojedinih varijabli nalazi se u datoteci mtcars_info.txt.
#
# a) Učitajte datoteku mtcars.csv pomoću:
# data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
# delimiter=",", skiprows=1)
#
# b) Prikažite ovisnost potrošnje automobila (mpg) o konjskim snagama (hp) pomoću naredbe
# matplotlib.pyplot.scatter.
#
# c) Na istom grafu prikažite i informaciju o težini pojedinog vozila (npr. veličina točkice neka bude u skladu sa
# težinom wt).
#
# d) Izračunajte minimalne, maksimalne i srednje vrijednosti potrošnje (mpg) automobila.
#
# e) Ponovite zadatak pod d), ali samo za automobile sa 6 cilindara (cyl).

import numpy as np
import matplotlib.pyplot as plt

# a)
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
hp = data[:, 3]
mpg = data[:, 0]
wt = data[:, 5]

# b) i c)
plt.scatter(hp, mpg, color="red", s = wt*10, edgecolors="black") 
plt.axis([0, 400, 0, 50])
plt.xlabel('Konjske snage (hp)') 
plt.ylabel('Potrošnja (mpg)') 
plt.title('Ovisnost potrošnje o konjskim snagama') 
plt.show()

# d)
minMpg = np.min(mpg)
maxMpg = np.max(mpg)
srednjiMpg = np.mean(mpg)
print("Najmanji mpg: ", minMpg)
print("Najveci mpg: ", maxMpg)
print("Srednji mpg: ", srednjiMpg)
print("")

# e)
cyl6 = data[data[:,1] == 6, 0] 
minMpg6 = np.min(cyl6)
maxMpg6 = np.max(cyl6)
srednjiMpg6 = np.mean(cyl6)
print("Najmanji mpg od automobila sa 6 cilindara: ", minMpg6)
print("Najveći mpg od automobila sa 6 cilindara:", maxMpg6)
print("Srednji mpg od automobila sa 6 cilindara:", srednjiMpg6)
print("")
