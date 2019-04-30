def calcularmaslarga(lista):
    palabra= ""
    largo= 0
    for i in lista:
        if (len(i) > largo):
            palabra= i
            largo= len(i)
    return palabra
def menu():
    print("1. calcular palabra mas larga")
lista = []
op= input("ingrese su opcion: ")
menu()
if op== "1":
    largo= int(input("agregar largo de la lista: "))
    for i in range(largo):
        lista.append(input("ingrese palabra: "))
    print ("la palabra mas larga es : ", calcularmaslarga(lista))
