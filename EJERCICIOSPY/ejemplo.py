while True:
    try:
        print("digite un numero")
        valor=int(input())
        break
    except ValueError:
        print("por favor digite datos numericos no caracteres de texto")
    except TypeError: 
        print("Ocurrio un Error de tipo de datos, valor invalido")
    finally:
        print("Ocurrio un Error")

#print("la division por cero es: ", valor/0)
print("aqui otra linea de codigo que continua")


