#Funciones
def diHola():
    print("Hola")
diHola()

#Ejemplo 1

def calcula_media(lista): #definir funcion
    suma=0
    for n in lista:
        suma += n
    return suma /len(lista)

lista=[1,2,5,7] #Crear lista
print(calcula_media(lista))

calcula_media(lista) #llamar funcion

