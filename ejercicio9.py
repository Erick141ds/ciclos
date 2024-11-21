'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
    '''
def main():
    while True:
        limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
        limite_superior = int(input("Introduce el límite superior del intervalo: "))
        if limite_inferior < limite_superior:
            break
        print("El límite inferior debe ser menor que el límite superior. Inténtalo de nuevo.")
		suma_dentro_intervalo = 0
    	numeros_fuera_intervalo = 0
    	numero_limite_inferior = False
    	numero_limite_superior = False
	while True:
        numero = int(input("Introduce un número (0 para terminar): "))
        if numero == 0:
            break
        if limite_inferior < numero < limite_superior:
            suma_dentro_intervalo += numero
        else:
            numeros_fuera_intervalo += 1
        if numero == limite_inferior:
            numero_limite_inferior = True
        if numero == limite_superior:
            numero_limite_superior = True
	print("\nResultados:")
    print(f"Suma de los números dentro del intervalo: {suma_dentro_intervalo}")
    print(f"Números fuera del intervalo: {numeros_fuera_intervalo}")
    if numero_limite_inferior or numero_limite_superior:
        print("Se ha introducido algún número igual a los límites del intervalo.")
    else:
        print("No se ha introducido ningún número igual a los límites del intervalo.")
