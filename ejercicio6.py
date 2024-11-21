'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
'''
mayores = 0
menores = 0
iguales = 0


cantidad = int(input("ingrese la cantidad de numeros que desea introducir: "))
for i in range(cantidad):
    numero = float(input("escribe un numero: "))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1
    
print(f"numeros mayores a 0: {mayores}")
print(f"numeros menores a 0: {menores}")
print(f"numeros iguales: {iguales}")
    
