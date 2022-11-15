print ("Ingrese la palabra que desea contar")

palabra = input()


def longCadena(palabra):
    c = 0

    for letra in palabra:
        c += 1

    print('La cadena tiene %d caracteres' % c)

longCadena(palabra)