#agregar comandos a botones con funciones y parametros

import tkinter as tk
from tkinter import ttk



root= tk.Tk()
root.geometry("300x300")


def seleccion(valor_recibido):
    print(valor_recibido)

ttk.Button(root,text="python", command=lambda: seleccion("python")).pack()
ttk.Button(root,text="js", command=lambda:seleccion("js")).pack()
ttk.Button(root,text="java", command=lambda:seleccion("java")).pack()
root.mainloop()
