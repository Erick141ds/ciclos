'''
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''
ahorros_totales = 0

for mes in range(1, 13):
    deposito = float(input(f"Introduce la cantidad a depositar en el mes {mes}: "))
    ahorros_totales += deposito
    print(f"Ahorro acumulado al final del mes {mes}: {ahorros_totales:.2f} USD")

print(f"\nEl ahorro total al final del año es: {ahorros_totales:.2f} USD")