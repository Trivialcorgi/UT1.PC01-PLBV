print ("Introduce el numero binario que quieres convertir a entero")

numero_bin = input()
numero_decimal = 0
valor_string = str(numero_bin)

posicion = len(numero_bin) - 1

for posicion, digito_string in enumerate (numero_bin[::-1]):
    digito = int(digito_string)
    print (f'digito: {digito}, posicion:{posicion}')

for posicion, digito_string in enumerate (numero_bin[::-1]):
    numero_decimal += int(digito_string) * 2 ** posicion

print (f'El número decimal que buscamos es {numero_decimal}')
