from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)

# 1) Konvolucijska neuronska mreža (slika 8.1. je standardna CNN arhitektura)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 2) Kompajliranje modela
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 3) Callbacks
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

tensorboard_cb = callbacks.TensorBoard(log_dir=log_dir)
checkpoint_cb = callbacks.ModelCheckpoint("najbolji_model.h5", 
                                          save_best_only=True, 
                                          monitor='val_accuracy', 
                                          mode='max')

# 4) Treniranje modela
history = model.fit(
    x_train_s, y_train_s,
    epochs=10,
    validation_split=0.1,
    callbacks=[tensorboard_cb, checkpoint_cb]
)

# 5) Učitavanje najboljeg modela
najbolji_model = keras.models.load_model("najbolji_model.h5")

# Točnost na skupu za učenje
y_pred_train = np.argmax(najbolji_model.predict(x_train_s), axis=1)
acc_train = accuracy_score(y_train, y_pred_train)
print(f"Točnost na skupu za učenje: {acc_train:.4f}")

# Točnost na skupu za testiranje
y_pred_test = np.argmax(najbolji_model.predict(x_test_s), axis=1)
acc_test = accuracy_score(y_test, y_pred_test)
print(f"Točnost na skupu za testiranje: {acc_test:.4f}")

# 6) Matrica zabune
def prikazi_matricu_zabune(y_true, y_pred, naziv_skupa):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'Matrica zabune - {naziv_skupa}')
    plt.xlabel('Predviđeno')
    plt.ylabel('Stvarno')
    plt.show()

prikazi_matricu_zabune(y_train, y_pred_train, 'Skup za učenje')
prikazi_matricu_zabune(y_test, y_pred_test, 'Skup za testiranje')
