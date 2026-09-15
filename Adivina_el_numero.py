import random as r

print("He pensado un número del 1 al 10. Adivina cual es.")
numero = r.randint(1,10)

while True:
    numero_usuario = int(input("Escribe un número: "))

    if numero_usuario == numero:
        print("¡INCREÍBLE! ¡Has acertado!")
        break

    elif numero_usuario > numero:
        print("El número que buscas es menor.")

    else:
        print("El número que buscas es mayor.")
