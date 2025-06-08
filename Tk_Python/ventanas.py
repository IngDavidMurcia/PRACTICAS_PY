#hola mundo con ventanas y texto
#titulo y tamaño ventana
# botones y comandos de funciones
#label


from tkinter import *

def imprimir():
    print("imprimiendo----")
    label1=Label(root,text="Imprimiendo")
    label1.pack(side=RIGHT)

root = Tk()
root.title("mi primer ventana")
root.geometry("1000x500")

boton1=Button(root, text="Minimizar", command=root.iconify,bg="blue")
boton1.pack()

boton2=Button(root, text="imprimir", command=imprimir)
boton2.pack()



root.mainloop()

