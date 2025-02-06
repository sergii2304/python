lista=[]

def menu():
    print("Menú:")
    print("1. Introduce artículo")
    print("2. Saca precio total")
    print("3. Fín")

def articulo(lista):
    nombre = input("Introduce el nombre del producto: ")
    cantidad = int(input("Introduce la cantidad: "))
    precio = float(input("Introduce el precio: "))
    lista.append((nombre, cantidad, precio))

def total(lista):
    precio_total = 0
    for producto in lista:
        nombre, cantidad, precio = producto
        precio_total += cantidad * precio
    print(f"El precio total es: {precio_total}")

def guardar_articulos(lista):
    f=open("C:/Users/Sergio/Documents/ASIR-2024/ASO/2ºTrimestre/Python/prueba.txt", "a")
    for producto in lista:
        nombre, cantidad, precio = producto
        f.write(f"{nombre},{cantidad},{precio}\n")

def fin():
    print("FIN")

def main():
    lista = []
    while True:
        menu()
        opcion = input("Selecciona una opción (1-3): ")
        if opcion == '1':
            articulo(lista)
        elif opcion == '2':
            total(lista)
        elif opcion == '3':
            guardar_articulos(lista)
            fin()
            break
        else:
            print("Opción incorrecta. Seleccionar una opción del 1 al 3.")

if __name__ == "__main__":
    main()
