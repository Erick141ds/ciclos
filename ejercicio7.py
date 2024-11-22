'''
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''

while True:
    caracteres = input("ingrese un caracter(o espacio pa terminar):").lower()
    if caracteres == " ":
        break

    if caracteres in "aeiou":
        print("¡VOCAL!")
    else:
        print("¡no vocal!")
        
