'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''
def convertir_a_binario_con_ciclos(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    return binario

numero = int(input("Introduce un número entero: "))
binario = convertir_a_binario_con_ciclos(numero)
print(f"El número {numero} en binario es: {binario}")
