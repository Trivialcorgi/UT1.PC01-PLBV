print("Ingrese 10 numeros que desea comprobar si es divisible entre 3: ")
numeros = []

for i in range(0, 10):
    ele = int(input())

    numeros.append(ele)

for numeros in range(10):
    if numeros % 3 == 0:
        print (numeros)