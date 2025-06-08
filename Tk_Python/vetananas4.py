#entradas de usuario con ENTRY

from tkinter import *

def saludar():
    print("hola "+nombre.get()+" "+apellido.get())
    saludo.set("hola "+nombre.get()+" "+apellido.get())
    
ventana=Tk()
ventana.title("Entradas")
ventana.geometry("300x200")
ventana.config(bg="DarkOliveGreen3")
ventana.resizable(0,0)

nombre = StringVar()
apellido=StringVar()
saludo=StringVar()
nombre.set("nombre aqui")
apellido.set("apellido aqui")

etiqueta1=Label(ventana,text="Nombre:", bd=4, bg="coral",font=("arial"))
etiqueta1.place(x=10,y=10)
entrada1=Entry(ventana,textvariable=nombre)
entrada1.place(x=100,y=10)


etiqueta2=Label(ventana,text="Apellido:",bd=4, bg="coral", font=("arial"))
etiqueta2.place(x=10,y=40)
entrada2=Entry(ventana,textvariable=apellido)
entrada2.place(x=100,y=40)

boton=Button(ventana,text="saludar", command=saludar)
boton.place(x=10,y=100)

entrada3=Entry(ventana,bd=8,font=("arial 10"),textvariable=saludo,state=DISABLED)
entrada3.place(x=70,y=150)

ventana.mainloop()