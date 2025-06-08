from tkinter import *


ventana=Tk()
ventana.title("posicionamiento widgets")
ventana.geometry("300x100")


def saludar():
    print("Hola te saludo")

def minimizar():
    ventana.iconify()



etiqueta1=Label(ventana,text="Saluda desde aqui")
etiqueta2=Label(ventana,text="minimiza desde aqui")

etiqueta1.place(x=10,y=10)
etiqueta2.place(x=10,y=40)

boton1=Button(ventana,text="Saludar", command=saludar)
boton2=Button(ventana,text="Minimiza", command=minimizar)

boton1.place(x=200, y=10)
boton2.place(x=200, y=50)





ventana.mainloop()
