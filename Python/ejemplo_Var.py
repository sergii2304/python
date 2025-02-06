 # Ejercicio 1 
# Crear variables

var1 = 12
var2 = True
var3 = 12.9
var4 = 'c'
var5 = "Hola"
var6 = "7"

# Saber de que tipo son 

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))
print(type(var6))



# Ejercicio 2
# Crear variable

a = 2
b = 4
# Operaciones basicas

c = a + b
d = b - a
e = a * b
f = b / a

print(c,d,e,f)


# Otras operaciones

g = a**b
h = pow(a,b)
i = b % a

import math
j = math.sin(90)
k = math.sqrt(4)

print(g,h,i,j,k)


# Operaciones
a="Hola"
b=""
c="Mundo"

print(a + b + c + "¡")

nombre= "Jose Garcia"
inicial= nombre[0]
ultima= nombre[11]
tres= nombre[:3] # o [0:3]
ultimas= nombre[-3:]
mitad= nombre[5:9]

print(nombre[-3:])

# Ejercicio 3
# Realizar un programa que cree las variables para almacenar vuestro nombre y la de vuestro compañero de mesa
# Mostrar por pantalla la frase que sigue este patron: En esta mesa se sientan  --- y ---.

var1 = "Sergio Mayo"
var2 = "Alvaro Mañoso"

print("En esta mesa se sientan " + var1 + " y " + var2)

# mensaje por pantalla: Compañero: 
#                       Yo:
# Primera letra de cada nombre

print("Compañero: " + var2[0:4])
print("Yo: " + var1[0:4])


# Ejercicio 4
# Operaciones logicas

a=True
b=False

print(a==b)
print(10 < 10)
print(10 <= 10)
print(6 > 4)
print(6 >= 4)
print(a != b)

print(a and b)
print(a or b)
print(not a)


# Ejercicio 5
# LISTAS y SETS

colores=["Rojo","Azul","Verde"]
colores.append("Amarillo")
print(colores)
mas_colores=["Negro","Blanco"]
colores.extend(mas_colores)
print(mas_colores)
otros_colores=["Morado","Beige"]
todos=colores + otros_colores

print(len(todos))

# Set ejercicio
colores=["Rojo",1,"Verde"]
colores.append("Amarillo")
print(colores)
mas_colores=[2,"Blanco","Blanco"]
colores.extend(mas_colores)
print(mas_colores)
otros_colores=["Morado",3]
todos=colores + otros_colores
set_colores=set(todos)
print(set_colores,len(set_colores))

# Ejercicio 6 Listas

mesa = "Sergio Mayo","Alvaro mañoso"


print("En esta mesa se sientan " + mesa[0] + " y " + mesa[1])

# mensaje por pantalla: Compañero: 
#                       Yo:
# Primera letra de cada nombre

print("Compañero: " + mesa[1][0:4])
print("Yo: " + mesa[0][0:4])

# Ejercicio 7 separaciones(Split)
nombre="Maria Rodriguez"
nombre_separado=nombre.split(" ")
print(nombre_separado,type(nombre_separado))
frase="Hola,¿Que tal?"
separada=frase.split(",")
print(separada)

# Ejercicio 8 Tuplas
alumno=("Mario",16)
juego=("Hollow Knigth","Team Cherry",2017,"Metroidvania")
print("Juego: " + juego[0] + 
      "\nDesarrollador: " + juego[1] + 
      "\nAño: " + str(juego[2]) + 
      "\nGenero: " + juego[3])
# Ejercicio 9
alumnos=[
    ("Julio", 12),
    ("Cristina", 13),
    ("Pedro", 15),
    ("Luis", 16)
]
print(alumnos)

#Ejercico 10 Diccionarios
libros={
    "La isla del tesoro": 30,
    "El señor de los Anillos": 20,
    "La casa de Bernarda Alba": 25,
}
print("Precio: ", libros["La isla del tesoro"])

#Ejercicio 11 Añadir parametro a diccionario
libros={
    "La isla del tesoro": 30,
    "El señor de los Anillos": 20,
    "La casa de Bernarda Alba": 25,
}
print("Precio: ", libros["La isla del tesoro"])
libros["Hola mundo"]=30
print(libros)

#Ejercicio 12 if

# pedir a y b
# si a es mayor que b, mostrar un mensaje

# pedir a y b
# si a es mayor que b, mostrar un mensaje

a= input("a=")
b= input("b=")

if a > b:
    print(" a es mayor que b")
else:
    print("b es mayor que a")

#Mostrar un menu
#pedir al usuario la opcion que desea realizar y realizar la operacion con a y b
#realizar la operación correspondiente
#mostrar el resultado
#si el usuariointroduce una opcion que no sea 1,2  o 3 mostrar un mensaje que diga opcion incorrecta y salir del programa


operaciones=int(input("1.Sumar \n2.Restar \n3.Multiplicar \n4.Dividir"))

if operaciones==1:
    a= float(input("Valor a="))
    b= float(input("Valor b="))
    print("El resultado es=",a + b )

elif operaciones==2:
    a= float(input("Valor a="))
    b= float(input("Valor b="))
    print("El resultado es=",a - b )

elif operaciones==3:
    a= float(input("Valor a="))
    b= float(input("Valor b="))
    print("El resultado es=",a * b )

elif operaciones==4:
    a= float(input("Valor a="))
    b= float(input("Valor b="))
    
    if b==0:
        print("ERROR")
    else:
        print("El resultado es=",a / b )

else:
    print("Opción incorrecta")

#try y except
try:
    a= int(input("Introduzca valor= "))
    print(a)
except:
    print("El valor no es un número")

# for
for i in range (0,5):
    print(i)
# for lista colores
colores=["Rojo","Azul","Negro"]
for elementos in colores:
    print(elementos)

# for lista creada por el usuario
colores=[]

for i in range(0,5):
    color=input("Introduce el nombre del color: ")
    colores.append(color)
print("Los colores de la lista son: ")
for color in colores:
        print("Color: " + color)

#contador
import random
contador=0
while contador < 100:
    contador += random.randint(0,5)
print("El bucle ha terminado con", contador)






  