while True:
    print("digite las horas trabajadas")
    try:
        totalHoras=int(input())
        break
    except:
        print("por favor digite solo valores numericos")
    

print("digite el valor de la hora")
costoHora=int(input())

if totalHoras >40:
    print("el total a pagar es de:  ", totalHoras*costoHora*1.5)
else:
    print("el total a pagar es de:  ", totalHoras*costoHora)