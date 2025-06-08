"""
import numpy as np
import matplotlib.pyplot as plt

# Función sigmoide
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Parámetros ajustados
w0 = -3.895
w1 = 0.849

# Rango de horas de estudio (0 a 15)
x = np.linspace(0, 15, 300)  # más puntos para suavizar la curva
z = w0 + w1 * x
probabilidad = sigmoid(z)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, probabilidad, label='Probabilidad de aprobar', color='blue')
plt.axvline(x=10, color='green', linestyle='--', label='10 horas (P ≈ 0.99)')
plt.axvline(x=2, color='red', linestyle='--', label='2 horas (P ≈ 0.10)')
plt.scatter([2, 10], [sigmoid(w0 + w1 * 2), sigmoid(w0 + w1 * 10)], color='black')
plt.title('Regresión logística: Probabilidad de aprobar según horas de estudio')
plt.xlabel('Horas de estudio')
plt.ylabel('Probabilidad de aprobar')
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True)
plt.show()

    """
    
import tkinter as tk
from tkinter import messagebox
import numpy as np
import plotly.graph_objs as go
from dash import Dash, dcc, html
import threading
import webbrowser

# Modelo logístico: parámetros ajustados
w0 = -3.895
w1 = 0.849

# Función sigmoide
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Función para generar la gráfica con Dash
def lanzar_dash(horas_usuario):
    # Generar datos para la curva
    x_vals = np.linspace(0, 15, 300)
    z_vals = w0 + w1 * x_vals
    y_vals = sigmoid(z_vals)

    # Punto del usuario
    z_user = w0 + w1 * horas_usuario
    y_user = sigmoid(z_user)

    # Crear app Dash
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1('Regresión Logística - Probabilidad de Aprobar', style={'textAlign': 'center'}),
        dcc.Graph(
            id='sigmoid-plot',
            figure={
                'data': [
                    go.Scatter(x=x_vals, y=y_vals, mode='lines', name='Curva Sigmoide', line=dict(color='royalblue')),
                    go.Scatter(x=[horas_usuario], y=[y_user], mode='markers+text',
                               marker=dict(size=10, color='red'),
                               text=[f"{y_user:.2%} probabilidad"],
                               textposition="top center",
                               name='Tu resultado')
                ],
                'layout': go.Layout(
                    xaxis={'title': 'Horas de estudio'},
                    yaxis={'title': 'Probabilidad de aprobar', 'range': [0, 1.05]},
                    title='Modelo logístico ajustado',
                    plot_bgcolor='white',
                    paper_bgcolor='whitesmoke',
                    font=dict(family="Arial", size=14),
                )
            }
        )
    ])

    # Abrir navegador
    def run_dash():
        app.run(debug=False, port=8050, use_reloader=False)

    threading.Thread(target=run_dash).start()
    webbrowser.open("http://127.0.0.1:8050")

# Función de botón "Calcular"
def calcular_probabilidad():
    try:
        horas = float(entry.get())
        if horas < 0:
            raise ValueError
        lanzar_dash(horas)
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingresa un número válido de horas (>= 0).")

# Crear interfaz Tkinter
ventana = tk.Tk()
ventana.title("Calculadora de Probabilidad de Aprobación")
ventana.geometry("400x200")
ventana.configure(bg='white')

titulo = tk.Label(ventana, text="Horas de estudio:", font=("Arial", 14), bg='white')
titulo.pack(pady=10)

entry = tk.Entry(ventana, font=("Arial", 14), justify="center")
entry.pack(pady=5)

boton = tk.Button(ventana, text="Calcular", font=("Arial", 12), bg="lightblue", command=calcular_probabilidad)
boton.pack(pady=20)

ventana.mainloop()
