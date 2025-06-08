
# Programa de ejemplo para condicionales y funcionales
def menu():
    print("1. SUMAR ")
    print("2. RESTAR ")
    print("3. MULTIPLICAR ")
    print("4. DIVIDIR ")
    print("5. salir")
    print("")
    print("")

def saludo():
    print("HOLA")
    print("BIENVENIDOS A MI CALCULADORA")  # esta funcion imprime por pantalla.  

def suma(num1,num2):
    return num1+num2

def resta(a,b): # funcion en construccion
    return a-b

def multiplica(a,b):
    return a*b

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return("la division con cero no es posible")
    except ValueError:
        return("Valor no valido, error en el calculo")
    except TypeError:
        return("tipo de datos no valido para una division")
    finally:
        print("este calculo ha terminado")
        
def lectura_datos():
    num1 = int(input("digite un numero: "))
    num2 = int(input("digite un segundo numero: ")) 
    valores=(num1,num2)
    return valores

if __name__ == '__main__':
    saludo()
    valores=lectura_datos()
    opc = 0
    while opc != "5":
        menu()
        opc = input("digite una opcion: ")

        if opc == "1":
            resultado=suma(valores[0],valores[1])
            print(resultado)
            print("")

        elif opc == "2":
            print(resta(valores[0],valores[1]))
            print("")

        elif opc == "3":
            print(multiplica(valores[0],valores[1]))
            print("")

        elif opc == "4":
            print(division(valores[0],valores[1]))
            print("")

        elif opc == "5":
            print("el programa ha finalizado")
            print("")

        else:
            print("Esta opcion no es valida")
            print("")




