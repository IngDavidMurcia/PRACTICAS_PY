#posicionar con grid y con place
#Ejercicio: vetana con 2 labels y 2 botones que salude y minimice ventana
from tkinter import *

root=Tk()
root.title("posicionar")
root.geometry("400x400")

etiqueta =Label(root,text="Etiqueta")
#etiqueta.grid(row=0,column=0)
etiqueta.place(x=30, y=40)

boton1 = Button(root,text="boton")
#boton1.grid(row=0,column=1)
boton1.place(x=30,y=80)


root.mainloop()