import sys
import os

# Python 3.13
python313 = r"C:\Users\maryo\AppData\Local\Programs\Python\Python313\python.exe"
if sys.version_info[:2] != (3, 13):
    os.execv(python313, [python313] + sys.argv)

# Librerías
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam

plt.style.use("ggplot")

# Cargar MNIST
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Dimensiones
print("Datos de entrenamiento:", X_train.shape, y_train.shape)
print("Datos de prueba:", X_test.shape, y_test.shape)

# Pruebas
print(X_train[8])
print(y_train[8])
print(X_train[20])
print(y_train[20])

# Gráfico entrenamiento
values_train, count_train = np.unique(y_train, return_counts=True)

plt.figure(figsize=(7, 4))
plt.bar(values_train, count_train)
plt.title("Training label distribution")
plt.xlabel("Labels")
plt.ylabel("Frequency")
plt.xticks(values_train)
plt.show()

# Gráfico prueba
values_test, count_test = np.unique(y_test, return_counts=True)

plt.figure(figsize=(7, 4))
plt.bar(values_test, count_test, color="royalblue")
plt.title("Testing label distribution")
plt.xlabel("Labels")
plt.ylabel("Frequency")
plt.xticks(values_test)
plt.show()

# Preparar imágenes
train_images = X_train.reshape((60000, 28 * 28))
train_images = train_images.astype("float32") / 255

test_images = X_test.reshape((10000, 28 * 28))
test_images = test_images.astype("float32") / 255

# Pruebas
print(train_images.shape)
print(train_images[20])

# Preparar etiquetas
train_labels = to_categorical(y_train)
test_labels = to_categorical(y_test)

# Prueba
print(train_labels[20])

# Crear modelo
model = Sequential([
    Input(shape=(28 * 28,)),
    Dense(64, activation="relu"),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])

# Resumen
model.summary()

# Compilar
model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# Entrenar
history = model.fit(
    train_images,
    train_labels,
    validation_split=0.2,
    epochs=15,
    batch_size=64
)

# Historial
print(history.history.keys())

# Gráfico pérdida
plt.figure(figsize=(6, 4))
plt.plot(
    np.arange(0, len(history.history["loss"])),
    history.history["loss"],
    label="train_loss"
)
plt.plot(
    np.arange(0, len(history.history["val_loss"])),
    history.history["val_loss"],
    label="val_loss"
)
plt.title("Train and Test Loss")
plt.xlabel("Epoch #")
plt.ylabel("Loss")
plt.legend()
plt.show()

# Gráfico precisión
plt.figure(figsize=(6, 4))
plt.plot(
    np.arange(0, len(history.history["accuracy"])),
    history.history["accuracy"],
    label="train_accuracy"
)
plt.plot(
    np.arange(0, len(history.history["val_accuracy"])),
    history.history["val_accuracy"],
    label="val_accuracy"
)
plt.title("Train and Test Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

# Evaluar
resultado = model.evaluate(test_images, test_labels)
print("Loss:", resultado[0])
print("Accuracy:", resultado[1])

# Guardar
model.save("mnist_model.keras")

# Forma de imagen
print(test_images[0].shape)
print(test_images[0].reshape(1, 28 * 28).shape)

# Predicción
pred = model.predict(test_images[0].reshape(1, 28 * 28))
pred_label = np.argmax(pred)

print("Predicción:", pred_label)
print("Etiqueta real:", test_labels[0])

# Mostrar resultado
plt.imshow(test_images[0].reshape(28, 28), cmap="gray")
plt.title(f"Predicción: {pred_label}")
plt.axis("off")
plt.show()
