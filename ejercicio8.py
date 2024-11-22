'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''
numero1 = int(input("escribe un numero: "))
numero2 = int(input("escribe un numero: "))

inicio = min(numero1, numero2)
fin = max(numero1, numero2)

print(f"numeros pares entre {inicio}  y  {fin}")

for num in range(inicio, fin + 1):
    if num % 2 == 0:
        print(num)
        