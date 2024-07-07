import os
import ssl
import certifi

import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

os.environ['SSL_CERT_FILE'] = certifi.where()



# Passo 1: Importar bibliotecas necessárias
import numpy as np

# Passo 2: Carregar e pré-processar o conjunto de dados CIFAR-10
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Normalizar os valores dos pixels para ficarem entre 0 e 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Passo 3: Construir a arquitetura do modelo
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Passo 4: Compilar o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Passo 5: Treinar o modelo
history = model.fit(x_train, y_train, epochs=10,
                    validation_data=(x_test, y_test))

# Passo 6: Avaliar o modelo
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nTest accuracy: {test_acc}')

# Plotar a acurácia e a perda do treinamento e validação
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Acurácia de Treinamento')
plt.plot(history.history['val_accuracy'], label='Acurácia de Validação')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.legend(loc='lower right')
plt.title('Acurácia de Treinamento e Validação')

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Perda de Treinamento')
plt.plot(history.history['val_loss'], label='Perda de Validação')
plt.xlabel('Época')
plt.ylabel('Perda')
plt.legend(loc='upper right')
plt.title('Perda de Treinamento e Validação')

plt.show()
