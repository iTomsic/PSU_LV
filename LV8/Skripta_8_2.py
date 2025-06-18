import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize
from skimage import color
from tensorflow.keras import models
import numpy as np

filename = 'test.png'

# Ucitaj sliku, MNIST slike su crno-bijele, veličine 28x28 piksela – zato moraš konvertirati boju i promijeniti dimenzije.
img_original = mpimg.imread(filename)
img = color.rgb2gray(img_original)
img = resize(img, (28, 28))


# Prikazi sliku, Prikazuje pripremljenu sliku bez koordinatne mreže, korisno za provjeru je li slika ispravno učitana i izgleda kao znamenka.
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.axis('off')  
plt.show()

# Pripremi sliku - ulaz u mrezu, reshape: model očekuje ulaz u obliku (broj_uzoraka, visina, širina, kanali), a imamo samo 1 sliku.
astype / 255.0

img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')

# Normalizacija piksela (pretpostavka je da je model treniran na vrijednostima 0-1)
img = img / 255.0

# TODO: ucitaj izgradenu mrezu, Učitava najbolji model (spremljen pomoću ModelCheckpoint tijekom treniranja).
model = models.load_model("najbolji_model.h5")

# TODO: napravi predikciju za ucitanu sliku pomocu mreze, predict(img): model daje niz vjerojatnosti za svaku znamenku od 0 do 9.
np.argmax()

predikcija = model.predict(img)
oznaka = np.argmax(predikcija)

# TODO: ispis rezultat u terminal, Prikazuje rezultat klasifikacije u terminalu.
print(f"Predviđena znamenka: {oznaka}")
