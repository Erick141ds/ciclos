'''
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador.
'''
suma = 0
cuenta = 0
while True:
    numero = int(input("escribe un numero: "))
    if numero == 0:
        break
    suma = suma + numero
    cuenta = cuenta + 1 
print(f"el promedio final es: ", suma / cuenta)

