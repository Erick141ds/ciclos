'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total 
de lo que pagó después de los 20 meses.
'''
meses = 20
pago_inicial = 10
total_pagado = 0

print("Mes\tPago mensual (EUR)")

for mes in range(1, meses + 1):
    pago_mensual = pago_inicial * (2 ** (mes - 1))  # El pago se duplica cada mes
    total_pagado += pago_mensual
    print(f"{mes}\t{pago_mensual:.2f}")

print(f"\nEl total pagado después de {meses} meses es: {total_pagado:.2f} EUR")