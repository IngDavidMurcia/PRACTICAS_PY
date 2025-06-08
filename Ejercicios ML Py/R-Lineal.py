from sklearn.linear_model import LinearRegression
import numpy as np
# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4,6,8,10])

# Crear el modelo de regresión lineal
modelo = LinearRegression()
# Ajustar el modelo a los datos
modelo.fit(X, y)
# Hacer una predicción
prediccion = modelo.predict(np.array([[6]]))
print("Coeficiente:", modelo.coef_[0])
print(prediccion[0])