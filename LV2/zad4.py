# Napišite funkciju koja kao povratnu vrijednost daje sliku (polje) sa crno bijelim kvadratima jednake dimenzije koji se
# naizmjenično pojavljuju (vidi primjer slike ispod). Funkcija kao argumente prima veličinu kvadrata u pikselima, broj
# kvadrata po visini i broj kvadrata po širini slike. Za realizaciju ove funkcije koristite numpy funkcije zeros i ones
# kako biste kreirali crna i bijela polja. Kako bise ih složili u odgovarajući oblik koristite numpy funkcije hstack i
# vstack. Za prikaz grayscale slike koristite naredbu:

# plt.imshow(img, cmap='gray', vmin=0, vmax=255)

import numpy as np
import matplotlib.pyplot as plt

def poljeKvadrata(kvadrat, redak, stupac):

    crna = np.zeros((kvadrat, kvadrat))
    bijela = np.ones((kvadrat, kvadrat)) * 255
    redak1 = np.hstack([crna, bijela] * (stupac//2))

    if stupac % 2 != 0:
        redak1 = np.hstack([redak1, crna])

    redak2 = np.hstack([bijela, crna] * (stupac//2))

    if stupac % 2 != 0:
        redak2 = np.hstack([redak2, bijela])

    matrica = np.vstack([redak1, redak2] * (redak//2))

    if redak % 2 != 0:
        matrica = np.vstack([matrica, redak1])

    return matrica

img = poljeKvadrata(50, 4, 5)
plt.imshow(img, cmap='gray', vmin = 0, vmax = 255)
plt.show()
