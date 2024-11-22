'''
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def mostrar_primos(n):
    contador_primos = 0
    numero_actual = 2

    while contador_primos < n:
        if es_primo(numero_actual):
            print(numero_actual)
            contador_primos += 1
        numero_actual += 1

cantidad = int(input("Introduce la cantidad de números primos que quieres mostrar: "))
mostrar_primos(cantidad)
