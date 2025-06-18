from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg
import numpy as np
import joblib

filename = 'example.png'

img = mpimg.imread(filename)[:,:,:3]
img = color.rgb2gray(img)
img = resize(img, (28, 28))

plt.figure()
plt.imshow(img, cmap=plt.get_cmap('gray'))


# TO DO: prebacite sliku u vektor odgovarajuce velicine
img = np.asarray(img)
img = np.reshape(img, (-1, 784))

img = img.astype('float32')

filename = "NN_model.sav"
mlp_mnist = joblib.load(filename)

# TODO: napravi predikciju i spremi u varijablu digit kao string

label = mlp_mnist.predict(img)
plt.show()
print("------------------------")
print("Slika sadrzi znamenku: ", label)