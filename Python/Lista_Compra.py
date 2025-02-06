# Crear un programa que sirva de lista de la compra introducido por el usuario
# La lista debe contener 5 elementos de compra
# Cada elemnto de la compra debe incluir el nombre, la cantidad y el precio
# Al final debe imprimirse una lista con los nombres de los elemntos a comprar y su correspondiente cantidad
# Se debe imprimir alm fianl el precio total,incluyendo el iva(%16)
lista_compra=[]

nombre1 = input("Introduce el nombre del producto: ")
cantidad1 = input("Introduce la cantidad: ")
precio1 = float(input("Introduce el precio: "))

nombre2 = input("Introduce el nombre del producto: ")
cantidad2 = input("Introduce la cantidad: ")
precio2 = float(input("Introduce el precio: "))

nombre3 = input("Introduce el nombre del producto: ")
cantidad3 = input("Introduce la cantidad: ")
precio3 = float(input("Introduce el precio: "))

nombre4 = input("Introduce el nombre del producto: ")
cantidad4 = input("Introduce la cantidad: ")
precio4 = float(input("Introduce el precio: "))

nombre5 = input("Introduce el nombre del producto: ")
cantidad5 = input("Introduce la cantidad: ")
precio5 = float(input("Introduce el precio: "))

producto1=(nombre1,cantidad1,precio1)
producto2=(nombre2,cantidad2,precio2)
producto3=(nombre3,cantidad3,precio3)
producto4=(nombre4,cantidad4,precio4)
producto5=(nombre5,cantidad5,precio5)

producto1=(nombre1,cantidad1)
lista_compra.append(producto1)
producto2=(nombre2,cantidad2)
lista_compra.append(producto2)
producto3=(nombre3,cantidad3)
lista_compra.append(producto3)
producto4=(nombre4,cantidad4)
lista_compra.append(producto4)
producto5=(nombre5,cantidad5)
lista_compra.append(producto5)

precio_total= precio1 + precio2 + precio3 + precio4 + precio5
iva= precio_total * 0.16
preciototal_iva= str(precio_total + iva)
print(lista_compra)
print("Precio total con IVA: " + preciototal_iva)

