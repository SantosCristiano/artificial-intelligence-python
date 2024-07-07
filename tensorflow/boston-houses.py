import tensorflow as tf
from tensorflow.keras import layers, models, datasets
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Carregar dados do conjunto de dados Boston Housing
boston = load_boston()
data = boston.data
targets = boston.target

# Pré-processamento dos dados
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)
targets = np.reshape(targets, (-1, 1)) # reshape targets to match the shape required by TensorFlow

# Dividir dados em conjuntos de treinamento e teste
train_data, test_data, train_targets, test_targets = train_test_split(data_scaled, targets, test_size=0.2, random_state=42)

# Definição do modelo
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(train_data.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)  # saída linear para regressão
])

# Compilação do modelo
model.compile(optimizer='adam',
              loss='mse',  # Mean Squared Error para regressão
              metrics=['mae'])  # Mean Absolute Error como métrica

# Treinamento do modelo
history = model.fit(train_data, train_targets, epochs=100, batch_size=16, validation_data=(test_data, test_targets))

# Avaliação do modelo
test_loss, test_mae = model.evaluate(test_data, test_targets, verbose=2)
print('\nTest Mean Absolute Error:', test_mae)

# Plotar resultados de treinamento
import matplotlib.pyplot as plt

plt.plot(history.history['mae'], label='MAE')
plt.plot(history.history['val_mae'], label = 'val_MAE')
plt.xlabel('Epoch')
plt.ylabel('MAE')
plt.legend(loc='upper right')
plt.show()