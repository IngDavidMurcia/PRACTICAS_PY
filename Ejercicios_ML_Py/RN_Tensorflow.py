import tensorflow as tf
from tensorflow.keras import layers

#crear un modelo secuencial con una capa oculta
modelo = tf.keras.Sequential([
    layers.Dense(10, input_shape=(5,), activation='relu'),layers.Dense(1)  
])
# Compilar el modelo
modelo.compile(optimizer='adam', loss='mse')
# Datos de ejemplo
import numpy as np
X = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
y = np.array([2, 4, 6])
# Ajustar el modelo a los datos
modelo.fit(X, y, epochs=100, verbose=0)
# Hacer una predicción
prediccion = modelo.predict(np.array([[16, 17, 18, 19, 20]]))
print("Predicción:", prediccion[0][0])

