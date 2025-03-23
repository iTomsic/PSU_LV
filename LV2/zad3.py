# Na temelju primjera 2.5. učitajte sliku 'tiger.png'. Manipulacijom odgovarajuće numpy matrice pokušajte:
# a) posvijetliti sliku (povećati brightness),
# b) zarotirati sliku za 90 stupnjeva u smjeru kazaljke na satu,
# c) zrcaliti sliku,
# d) smanjiti rezoluciju slike x puta (npr. 10 puta),
# e) prikazati samo drugu četvrtinu slike po širini, a prikazati sliku cijelu po visini; ostali dijelovi slike trebaju biti
# crni.

import numpy as np 
import matplotlib.pyplot as plt 
 
img = plt.imread("tiger.png") 
img = img[:,:, 0].copy() 
print(img.shape) 
print(img.dtype) 

# a)
osvjetljeniImg = img * 2
osvjetljeniImg = np.clip(osvjetljeniImg, 0.0, 1.0)

# b)
rotiraniImg = np.rot90(img, 3)

# c)
zrcalniImg = np.fliplr(img)

# d)

x = 10
smanjeniImg = img[::x, ::x]

# e)
visina, sirina = img.shape
zadnjiImg = img 
zadnjiImg[:,sirina//2:] = 0
zadnjiImg[:,sirina//4] = 0

odabir = int(input("Unesite odabir slike (1 - 6): "))

match odabir:
    case 1: 
        plt.figure() 
        plt.imshow(img, cmap="gray") 
        plt.title("Originalna slika")
        plt.show() 
    case 2:
        plt.figure() 
        plt.imshow(osvjetljeniImg, cmap="gray") 
        plt.title("Osvijetljena slika")
        plt.show() 
    case 3: 
        plt.figure() 
        plt.imshow(rotiraniImg, cmap="gray") 
        plt.title("Rotirana slika")
        plt.show() 
    case 4: 
        plt.figure() 
        plt.imshow(zrcalniImg, cmap="gray") 
        plt.title("Zrcalna slika")
        plt.show() 
    case 5:
        plt.figure() 
        plt.imshow(smanjeniImg, cmap="gray") 
        plt.title("Slika smanjene rezolucije")
        plt.show() 
    case 6:
        plt.figure() 
        plt.imshow(zadnjiImg, cmap="gray") 
        plt.title("Zadnja slika")
        plt.show() 
