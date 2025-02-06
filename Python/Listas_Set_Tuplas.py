# Hacer un programa que:
    # Contenga una lista de 6 animales. Cada anaimal debe tener 3 datos: el nombre del animal, su clasificación por reino(mamifero,reptiles...) y por dietas(carnivoro...)Se guardara en tuplas
tigre=("Tigre", "Mamífero", "Carívoro")
leon=("León", "Mamífero", "Carívoro")
serpiente=("Serpiente", "Reptíl", "Carívoro")
perro=("Perro", "Mamífero", "Carívoro")
gato=("Gato", "Mamífero", "Herbívoro")
tortuga=("Tortuga", "Reptíl", "Herbívoro")

lista_animales=[tigre,leon,serpiente,perro,gato,tortuga]

    # Añadir un animal nuevo no repetido
lista_animales.append(("Conejo", "Mamífero", "Herbívoro"))

    # Añadir animal repetido
lista_animales.append(("Perro", "Mamífero", "Carnívoro"))
    # Convertir en un set
conjunto= set(lista_animales)

    # imprimir el set entero
print(conjunto)
    #Imprimir el segundo y cuarto animal del set en este formato:
       # Animal:
       # Tipo:
       # Dieta:

#Añadir un animal nuevo el usuario y que se almacenen en la lista

nombre1 = input("Introduce el nombre del nuevo animal: ")
clasificacion1 = input("Introduce la clasificación del animal (Mamífero, Reptil, Ave, etc.): ")
dieta1 = input("Introduce la dieta del animal (Carnívoro, Herbívoro, Omnívoro, etc.): ")

animal1=(nombre1,clasificacion1,dieta1)
lista_animales.append(animal1)
print(lista_animales)




