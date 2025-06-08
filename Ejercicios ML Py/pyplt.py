"""import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
"""
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración del estilo
sns.set_theme(style="whitegrid")  # Fondo con cuadrícula
sns.set_palette("dark")  # Paleta de colores profesional

# Datos
x = [1, 2, 3]
y = [1, 4, 9]
labels = ["A", "B", "C"]

# Crear figura
plt.figure(figsize=(8, 5))  # Tamaño personalizado

# Gráfico de línea con marcadores
line_plot = sns.lineplot(
    x=x, 
    y=y, 
    marker="*",  # Marcadores circulares
    markersize=10,  # Tamaño de marcadores
    linewidth=2,  # Grosor de línea
    label="Crecimiento exponencial"
)

# Añadir etiquetas a los puntos
for i, (xi, yi, lbl) in enumerate(zip(x, y, labels)):
    plt.text(xi + 0.1, yi - 0.3, lbl, fontsize=10)  # Desplazamiento para mejor visibilidad

# Personalización adicional
plt.title("Relación X vs Y - Crecimiento Exponencial", fontsize=14, pad=20)
plt.xlabel("Valores del Eje X (unidades)", fontsize=12)
plt.ylabel("Valores al Cuadrado (unidades²)", fontsize=12)
plt.xticks(x)  # Fuerza a mostrar todos los valores de X
plt.legend(loc="upper left", frameon=True)  # Leyenda con marco

# Ajustes finales
plt.tight_layout()  # Evita cortes en etiquetas
plt.show()