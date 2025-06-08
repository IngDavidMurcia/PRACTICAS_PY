#CENTRO TECNOLOGICO DEL MOBILIARIO 
#SENA REGIONAL ANTIOQUIA
#ANÁLISIS Y DESARROLLO DE SISTEMAS DE INFORMACION - ADSI
#AUTOR: Ing David Murcia - @IngDavidMurcia - davidmurcia001@gmail.com


#EJERCICIO CRUD EN PYTHON --AGENDA DE CONTACTOS--
# Tematicas evaluadas: Programacion estructurada, Poo, funciones lambda, excepciones, librerias tk ttk, conexion a BD
#condicionales, ciclos, funciones, clases, objetos, metodos.


# importando las librerias necesarias:
from tkinter import Button, PhotoImage,Label,LabelFrame,W,E,N,S,Entry,END,StringVar,Scrollbar,Toplevel,Tk, font # se importa solo elementos necesarios para optimizar memoria
from tkinter import ttk  # ttk ofrece widgets similares a tk, pero con una apariencia mas moderna.
import sqlite3  # libreria para realizar la coneccion con la base de datos
from typing import Text  #modulo python para la conexion con sqlit


class Agenda:               # clase principal que genera el contenedor de ventana principal con ttk
    nombreBD="contacts.db"     #asignamos  la variable que representa la base de datos, como se tenga en el archivo fuente. si esta en subcarpetas se coloca toda la ruta
    def __init__(self,menu):        #constructor, recibe como parametro un objeto ventana creado en la funcion main
        self.menu = menu            # asignamos el objeto de ventana como propiedad de la clase
        self.menu.title("Agenda ADSI")  #asigna un titulo a la ventana creada que ahora pertenece a la misma clase
        self.crearGUI()                 # llamamos el metodo crearGUI el cual genera todo el contenido (Widgets) que va tener nuestra aplicacion
        
        # configuramos los estilos para la letra, tipo de fuente y color
        ttk.estilo=ttk.Style()            
        ttk.estilo.configure("Treeview",font=("helvetica",10))
        ttk.estilo.configure("Treeview.Heading",font=("arial",12,"bold"))
    
    #definimos un metodo para realizar la conexion a la BD con la libreria sqlite3. (la BD previamente esta creada - se recomienda revisarla con sqlitebrowser)
    def consultaDB(self, consulta, parametro=()): # la funcion resive 2 argumentos, que son la consulta SQL a realizar y el otro argumento son los parametros para esa consulta
        with sqlite3.connect(self.nombreBD) as conn:  # se establece un alias a la conexion
            print(conn)                               #se imprime por consola el cursos de la conexion                  
            print("la conexion a la base de datos es satisfactoria") 
            #se asigna la respuesta del motor de BD a la variable resConsulta, luego se realiza un commit, este debemos hacerlo acada que se hagan transacciones a la BD
            cursor= conn.cursor()               
            resConsulta=cursor.execute(consulta,parametro)
            conn.commit()
        return resConsulta  #se retorna la respuesta obtenida del motor BD sobre la consulta realizada.

#este metodo llama los demas metodos para instanciar todos los widgets dentro de la ventana principal de la aplicacion, (el logo, los contenedores, areas de mensjaes, botones, etc)
    def crearGUI(self):                     
        self.main_logo()   #metodo que dibuja el logo en la ventana principal
        self.contenedor_texto()   #metodo que crea los widgets del modulo agregar contactos, crea los campos, nombe, numero y correo y sus espacios para las entradas de usuario
        self.canva_datos()          # metodo que genera un contenedor donde se visualizaran los registros de la BD, utiliza la funcion Treeview.
        self.area_mensajes()        #genera un label para mostrar los diferentes mensajes al usuario.
        self.barraNav()             #crea una barra de navegacion lateral en sentido vertial, para desplazarse en caso de que hayan numerosos registros en la vista de datos.
        self.botonesInferiores()       # crea los botones, Editar y Borrar registros. asi mismo se asocian los metodos de las acciones correspondientes
        self.verLista()             # limpia datos previos, realiza la consulta de registros a la BD y los inserta en el espacio canva creado con Treeview

#define un Label que contendra la imagen del logo
    def main_logo(self):
        foto = PhotoImage(file='imagenes/logoSena.png')  #instanciamos un objeto tipo imagen de la libreria tkinter, se asigna la ruta donde esta el logo con extension.
        label = Label(image=foto)                        #creamos un label que sirva como contenedor de la imagen.
        label.image = foto                               # En la propiedad imagen del label asignamos el objeto imagen creado.
        label.grid(row=0, column=1,padx=15)              #Posicionamos en label del logo en la ventana principal. primera linea y segunda columna(1)


#define los widgets para agregar contacto, labels, entradas de usuario y boton que dispara el evento SQL para agregar en la BD
    def contenedor_texto(self):
        Labelframe = LabelFrame(self.menu, bg="sky blue",text="crear nuevo contacto", font="arial 12")  # este es el contenedor para los campos de nuevo contacto se incorpora a la ventana principal
        Labelframe.grid(row=0, column=0, padx=15, pady=20, sticky="S")                                  # se esta posicionando el contenedor dentro de la ventana principal con grid.
        Label(Labelframe, text="Nombre: ",bg="sky blue", fg="black").grid(row=1, column=1, sticky=W, pady=2,padx=15)    #primer label de campo nombre creado dentro del contenedor y posicionado de una vez.
        self.campoNombre =Entry(Labelframe)                                                                             #se genera un campo de entrada de datos. 
        self.campoNombre.grid(row=1, column=2, sticky=W,padx=5,pady=2)                                                  #se posiciona el entry con grid. similar como se hizo con el label
        Label(Labelframe, text="Correo: ",bg="sky blue", fg="black").grid(row=2, column=1, sticky=W, pady=2,padx=15)    #repetimos creacion de label para los campos correo y numero
        self.campoCorreo =Entry(Labelframe)
        self.campoCorreo.grid(row=2, column=2, sticky=W,padx=5,pady=2)
        Label(Labelframe, text="Numero: ",bg="sky blue", fg="black").grid(row=3, column=1, sticky=W, pady=2,padx=15)
        self.campoNumero =Entry(Labelframe)
        self.campoNumero.grid(row=3, column=2, sticky=W,padx=5,pady=2)
            #este boton se incorpora dentro del contenedor en la ventana principal, llama el metodo eventoAgregarContacto
        Button(Labelframe, text="AGREGAR", command=self.eventoAgregarContacto,bg="SteelBlue", fg="white").grid(row=4, column=2, sticky=W, padx=5, pady=5)  

#este metodo recibe como parametro un string, y lo presenta como mensaje en un label dentro de la ventana, se le da una posicion especifica con grid.
    def area_mensajes(self):
        self.mensajes=Label(text="",fg="sienna3",font=("arial",10,"bold"))
        self.mensajes.grid(row=3, column=1,sticky=W)

##este metodo genera un arbol (Treeview) de datos, una especia de tabla grillada para mostrar los datos de la BD, se nombras los encabezados de fila.
    def canva_datos(self):
        self.arbol = ttk.Treeview(height=8, columns=("email","numero"),style="Treeview")
        self.arbol.grid(row=6,column=0,columnspan=3)
        self.arbol.heading("#0",text="Nombre",anchor=W)
        self.arbol.heading("email", text="Direccion de Correo", anchor=W)
        self.arbol.heading("numero",text="Numero contacto", anchor=W)

# este metodo crea un widget de barra de desplazamiento lateral en la ventana principal
    def barraNav(self):
        self.barra=Scrollbar(orient="vertical", command=self.arbol.yview)
        self.barra.grid(row=6, column=3, rowspan=10, sticky="sn")

#en este metodo se estan creando los botones editar y borrar, los cuales disparan las consultas SQL correspondientes.
    def botonesInferiores(self):
        Button(text="BORRAR SELECCIONADO",command="",bg="SteelBLue",fg="white").grid(row=8, column=0,sticky=W, pady=10,padx=20)
        Button(text="EDITAR SELECCIONADO", command=self.eventoEditarElemento,bg="SteelBlue",fg="white").grid(row=8,column=1,sticky=W)

#este es el evento asignado al boton Agregar, el cual llama a su vez a la funcion agregarcontacto.
    def eventoAgregarContacto(self):
        self.agregarContacto()

#este es el metodo asignado al boton Editar. 
    def eventoEditarElemento(self):
        self.mensajes['text']=''     #deja en blanco el campo de mensajes.
        try: 
            self.arbol.item(self.arbol.selection())['text'][0]          #valida si hay seleccionado algun registro
        except:
            self.mensajes['text'] = 'No ha seleccionado reigstros para Editar'   # si no hay seleccion de registros lanza la excepcion y retorna sin hacer nada mas.
            return
        self.abrirVetanaEdicion()                                                #si no se ejecuta el Except, se llama el metodo abrir ventana de edicion, una ventana emergente.

#este metodo genera una ventana emergente transitoria a la principal, en donde se hara la edicion del registro seleccionado.
    def abrirVetanaEdicion(self):
        nombre = self.arbol.item(self.arbol.selection())['text']            # en la variable nombre, se captura el nombre que se ha seleccionado en el treviw para su edicion
        numeroActual = self.arbol.item(self.arbol.selection())['values'][1]   # en la variable nnumeroActual, se captura el numero del registro seleccionado en el treviw para su edicion
        self.ventanaTemporal = Toplevel()                                       #genera una ventana transitoria
        self.ventanaTemporal.title('Edicion de contacto')                       #asigan titulo a la nueva ventana
        Label(self.ventanaTemporal, text='Nombre: ').grid(row=0,column=1)       # Un label Nombre dentro de la nueva ventana
        Entry(self.ventanaTemporal, textvariable=StringVar(                     
            self.ventanaTemporal,value=nombre), state='readonly').grid(row=0,column=2)      # una entrada de datos, sin edicion solo visualizacion del dato actual que se va editar
        Label(self.ventanaTemporal, text="numero actual").grid(row=1,column=1)        # Un label numero actual dentro de la nueva ventana
        Entry(self.ventanaTemporal,textvariable=StringVar(                                   
            self.ventanaTemporal, value=numeroActual),state='readonly').grid(row=1,column=2)   # una entrada de datos, sin edicion solo visualizacion del dato actual que se va editar
    # aqui se genera un nuevo label y entrada de dato en la nueva ventana para que el usuario coloque el nuevo dato a editar del registro seleccionado.
        Label(self.ventanaTemporal, text='nuevo numero: ').grid(row=2,column=1)
        nuevoNumeroContactoWidget = Entry(self.ventanaTemporal)
        nuevoNumeroContactoWidget.grid(row=2, column=2)                 # se posiciona el campo de entrada.

        Button(self.ventanaTemporal, text='Editar contacto', command=lambda: self.editarElemento(
            nuevoNumeroContactoWidget.get(),numeroActual, nombre)).grid(row=3,column=2,sticky=E)    #se crea un boton para confirmar la edicion y disparar el metodo editar elemento
        
        self.ventanaTemporal.mainloop()                 # la nueva ventana de edicion tambien reuqiere el meotodo mainloop para que este persistente y pueda visualizarse

# este metodo es llamado por el boton editar elemento, genera la consulta SQL a la base de dato scon la nueva informacion agregada
    def editarElemento(self,nuevoNumero,numeroActual,nombre):
        consulta= 'UPDATE contacts_list SET number=? WHERE number =? AND name= ?'
        parametros=(nuevoNumero,numeroActual,nombre)
        self.consultaDB(consulta,parametros)
        self.ventanaTemporal.destroy()                  #una vez realizada la consulta de actualizacin de dato, se elmimina la ventanta transitoria.
        self.mensajes["text"]="Numero de {} ha sido modificado".format(nombre)      #se envia el mensaje de cofirmacion al usuario
        self.verLista()                             # se actualiza la vista del Treview en el canva de datos.

#este metodo genera la consulta SQL donde se agrega registros nuevos a la BD
    def agregarContacto(self):
        if self.validarNuevoContacto():     # se llama el metodo validacionnuevocontacto para revisar que los campos en los entry no esten vacios. 
            consulta= 'INSERT INTO contacts_list VALUES (NULL,?,?,?)'               #si la validacion es verdadera, se ejecuta todo el if, con la consulta SQL
            parametro= (self.campoNombre.get(),self.campoCorreo.get(),self.campoNumero.get())
            self.consultaDB(consulta,parametro)    # se envia la conuslta con los parametros.
            self.mensajes["text"] = 'Nuevo contacto {} agregado'.format(self.campoNombre.get())         #se confirma con mensjae al usuario
            self.campoNombre.delete(0,END)
            self.campoCorreo.delete(0,END)
            self.campoNumero.delete(0,END)                                                                 # se borran todos los datos agregados de los campos (entry) en la ventana. 
        else:
            self.mensajes['text'] = 'campos nombres, correo y numero no deben estar vacios'             #si la validacion (campos vacios) es falsa, se envia mensaje al usuario y no se hacen consultas SQL.
        self.verLista()                                                                                 # se actualiza la vista de los datos del Treview

#debes construir el metodo borrar registro, no olvides validar si el usuario a seleccionado previamente algun registro.
    def borrarElemento(self):
        pass

#este metodo valida que los campos no esten vacios, debes agregar la funcionalidad de que valide si elcorreo tiene un formato correcto y que el campo numero sea efectivamente numeros y no caracteres.
    def validarNuevoContacto(self):
        return len(self.campoNombre.get()) != 0 and len(self.campoNumero.get()) !=0 and len(self.campoCorreo.get()) != 0 

#con este metodo se realiza la consulta de los registros a la BD y se muestran en el Treview en el contenedor generado para esto. 
    def verLista(self):
        valores = self.arbol.get_children()         # se obtienen todo los valores actuales de la vista de arbol (Treeview)
        for valor in valores:                       #se recorren todos los valores y se borran de la vista
            self.arbol.delete(valor)
        consulta= 'SELECT * FROM contacts_list ORDER BY name desc'              
        entradasContactos = self.consultaDB(consulta)       #se realiza la consulta a la BD de los registros actualizados
        for fila in entradasContactos:
            self.arbol.insert('',0,text=fila[1], values=(fila[2],fila[3]))          #se recorre cada registro y se va insertando en la vista Treeview


if __name__ == '__main__':   #funcion main, aqui inicia nuestra aplicacion
    menu=Tk()               #estamos instanciando un nuevo objeto de tipo TK (ventana)
    aplicacion =  Agenda(menu)  #instanciamos un nuevo objeto de tipo "Agenda"y pasamos como parametro el objeto tk creado ( menu)
    menu.mainloop()             #hacemos persistente la ventana para que pueda visualizarse.
