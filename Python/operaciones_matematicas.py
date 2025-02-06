'''
Realizar un programa que realice una serie de operaciones mátematicas:
menu()->muestra por pantalla las opciones:
            #1-Funciones trigonometricas.
            #2-Logaritmos.
            #3-Raiz.
            #4-Salir.   
trig()->pide el valor de un ángulo entero y positivio e imprime su seno,su coseno y su tangente.
logaritmo()->pide el valor de un número mayor que creo y devuelve su valor,que debera ser impreso fuera de la funcion.
raiz()->pide un numero cualquiera.Si es negativo,el programa indica que la raiz es compleja,sin calcularla.
si es positivo ,imprime el valor de su raiz cuadrada.
'''
import math

def menu():
    print("Menú:")
    print("1. Funciones trigonométricas")
    print("2. Logaritmos")
    print("3. Raíz")
    print("4. Salir")

def trig():
    angulo = int(input("Valor del ángulo entero y positivo: "))
    if angulo < 0:
        print("El ángulo debe ser positivo.")
        return
    radianes = math.radians(angulo)
    seno = math.sin(radianes)
    coseno = math.cos(radianes)
    tangente = math.tan(radianes)
    print(f"Seno de {angulo}°: {seno}")
    print(f"Coseno de {angulo}°: {coseno}")
    print(f"Tangente de {angulo}°: {tangente}")

def logaritmo():
    numero = float(input("Número mayor que 0: "))
    if numero <= 0:
        print("El número debe ser mayor que 0.")
        return
    log = math.log(numero)
    print(f"El logaritmo de {numero} es: {log}")

def raiz():
    numero = float(input("Número cualquiera: "))
    if numero < 0:
        print("La raíz es compleja.")
    else:
        raiz_cuadrada = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            trig()
        elif opcion == '2':
            logaritmo()
        elif opcion == '3':
            raiz()
        elif opcion == '4':
            print("Fin del programa")
            break
        else:
            print("Opción incorrecta. Seleccionar una opción del 1 al 4.")

if __name__ == "__main__":
    main()