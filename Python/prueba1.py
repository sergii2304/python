# Ejercicio 1

Alumnos = []
nombres_apellidos_set = set()
while True: # Bucle infinito que recorre el menú hasta el break especificado (fin de bucle)
    opciones = int(input("1. Introducir datos de alumno nuevo. \n2. Imprimir los alumnos de la clase. \n3. Salir \nElige una opcion: "))

    if opciones == 1:
        nombre = input("Introduce el Nombre: ")
        apellidos = input("Introduce los Apellidos: ")
        nombre_apellido = (nombre, apellidos)
         # Verificar si el alumno ya existe
        if nombre_apellido in nombres_apellidos_set:
            print("El alumno ya existe en la lista. No se puede agregar.")
            continue  # Volver al inicio del bucle

        while True: # Bucle que recorre el input hasta que se asigne la letra correcta ("S" o N" o "s" o "n")para continuar al input nota
            repetidor = input("Introduce si es Repetidor (S/N): ").upper()
            if repetidor == 'S':
                repetidor_bool = "Es Repetidor"
                break
            elif repetidor == 'N':
                repetidor_bool = "No es Repetidor"
                break
            else:
                print("Por favor, introduce 'S' para sí o 'N' para no.")
        
        nota = float(input("Introduce la nota media: "))
        alumno = (nombre, apellidos, repetidor_bool, nota)
        Alumnos.append(alumno) # Agregar el alumno a la lista de alumnos
        nombres_apellidos_set.add(nombre_apellido)
        print("Nombre:", alumno[0],
              "\nApellidos:", alumno[1],
              "\nRepetidor:", alumno[2],
              "\nNota:", alumno[3])

    elif opciones == 2:  
        print("Lista de alumnos:") 
        for alumno in Alumnos: # Bucle para ir mostrando los alumnos que se vayan añadiendo
            print("Nombre:", alumno[0],
                  "\nApellidos:", alumno[1],
                  "\nRepetidor:", alumno[2],
                  "\nNota:", alumno[3],
                  "\n")   

    elif opciones == 3:
        print("Fin del programa")
        break  # Terminar el bucle de opciones

    else:
        print("No seleccionó la opción correcta, seleccione opción 1, 2 o 3.")