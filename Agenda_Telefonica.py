agenda = {}

while True:

    print("\n--- MENÚ ---")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Listar contactos")
    print("4. Borrar contacto")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:

        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agenda[nombre] = telefono
        print("Contacto añadido.")

    elif opcion == 2:

        nombre = input("Nombre del contacto que quieres buscar: ")

        if nombre in agenda:
            print(f"El número de teléfono de {nombre} es {agenda[nombre]}.")
        else:
            print(f"No se encontró ningún contacto con el nombre {nombre}.")

    elif opcion == 3:

        print("\nLista de contactos:")
        for nombre, telefono in agenda.items():
            print(f"- {nombre}: {telefono}")

    elif opcion == 4:

        nombre = input("Nombre del contacto que quieres borrar: ")

        if nombre in agenda:
            del agenda[nombre]
            print(f"El contacto {nombre} ha sido borrado.")


    elif opcion == 5:
        break

    else:
        print("Opción no válida. Por favor, elige una opción válida.")
