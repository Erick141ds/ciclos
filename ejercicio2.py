 '''
# Crea un programa que permita adivinar un número. La aplicación genera un 
# número aleatorio del 1 al 100. A continuación va pidiendo números y va 
# respondiendo si el número a adivinar es mayor o menor que el introducido,
# a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
# El p.rograma termina cuando se acierta el número (además te dice en cuantos 
# intentos lo has acertado), si se llega al limite de intentos te muestra el 
# número que había generado.
# Para genear un número entero aleatorio se utiliza la función randint
# del paquete random

# import random
# aleatorio = random.randint(limite_inf, limite_sup)
''' 
import random
numero_escondido = random.randint(1, 100)
intentos = 0
while True :
    numero = int(input("adivina un numero: "))
    intentos = intentos + 1
    if numero_escondido == numero:
        print("lo adivinaste")
        print(f"en {intentos} intentos")
        break 
    elif numero_escondido > numero:
        print("escribe uno mas grande")
    else:
        print("escribe uno mas pequeño")

    if intentos == 10:
        print(f"fallaste")
        break