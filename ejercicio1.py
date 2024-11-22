'''
Crea una programa que pida un número y calcule su factorial (El factorial de 
un número es el producto de todos los enteros entre 1 y el propio número y se 
representa por el número seguido de un signo de exclamación. 
Por ejemplo 5! = 1x2x3x4x5=120)
'''
N = int(input("escribe un numero entero para calcular su factorial: "))
if N < 0:
    print("¡ERROR! el factorial solo esta disponible para numeros positivos")
else:
    fa = 1 
    for i in range(1, N + 1):
        fa *= i
    print(f"el factorial de {N} es {fa}")
    