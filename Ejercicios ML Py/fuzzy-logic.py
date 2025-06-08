import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Definir el universo de variables (rango de valores)
temperatura = np.arange(0, 41, 1)  # de 0°C a 40°C

# 2. Crear las funciones de pertenencia (fuzzy sets)
# Para la temperatura:
fria = fuzz.trimf(temperatura, [0, 0, 20])
templada = fuzz.trimf(temperatura, [10, 20, 30])
caliente = fuzz.trimf(temperatura, [20, 40, 40])

# 3. Visualizar las funciones (opcional)
import matplotlib.pyplot as plt
plt.figure()
plt.plot(temperatura, fria, 'b', label='Fría')
plt.plot(temperatura, templada, 'g', label='Templada')
plt.plot(temperatura, caliente, 'r', label='Caliente')
plt.title('Funciones de pertenencia para la temperatura')
plt.legend()
plt.show()

# 4. Evaluar un valor específico (ej. 15°C)
temp_valor = 15

# Calcular grados de pertenencia
grado_frio = fuzz.interp_membership(temperatura, fria, temp_valor)
grado_templado = fuzz.interp_membership(temperatura, templada, temp_valor)
grado_caliente = fuzz.interp_membership(temperatura, caliente, temp_valor)

print(f"Para {temp_valor}°C:")
print(f"Grado de frío: {grado_frio:.2f}")
print(f"Grado de templado: {grado_templado:.2f}")
print(f"Grado de caliente: {grado_caliente:.2f}")
