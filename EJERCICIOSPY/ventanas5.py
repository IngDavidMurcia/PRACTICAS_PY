from tkinter import *

root= Tk()
root.title("radiobuttons")
root.geometry("400x300")
root.config(bg="DarkSlateGray1")
root.resizable(0,0)



def operacion():
    numero=num.get()
    if opc.get()==1:
        total =numero*5
    elif opc.get()==2:
        total=numero*10
    elif opc.get()==3:
        total=numero*20
    elif opc.get()==4:
        total=numero*30
    elif opc.get()==5:
        total=numero*40
    else:
        total=numero*numero
    print("el total de la operacion es: ", total)

opc=IntVar()
num=IntVar()



etiqueta1=Label(root,text="Escriba un numero")
etiqueta1.place(x=20,y=20)

entrada1=Entry(root,bd=7,font="Helvetica 12")
entrada1.place(x=150,y=20)

etiqueta2=Label(root,text="Elija la cantidad")
etiqueta2.place(x=20,y=50)

x5=Radiobutton(root,text="x5",value=1,bg="DarkSlateGray1",variable=opc)
x5.place(x=20, y=80)
x10=Radiobutton(root,text="x10",value=2,bg="DarkSlateGray1",variable=opc)
x10.place(x=70, y=80)
x20=Radiobutton(root,text="x20",value=3,bg="DarkSlateGray1",variable=opc)
x20.place(x=120, y=80)
x30=Radiobutton(root,text="x30",value=4,bg="DarkSlateGray1",variable=opc)
x30.place(x=20, y=110)
x40=Radiobutton(root,text="x40",value=5,bg="DarkSlateGray1",variable=opc)
x40.place(x=70, y=110)

boton1=Button(root,text="calcular",command=operacion)
boton1.place(x=20,y=140)



root.mainloop()
