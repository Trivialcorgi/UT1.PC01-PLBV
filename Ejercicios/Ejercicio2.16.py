nombres = []
n = int(input("Ingresa un numero de personas:"))

for i in range(0, n):
    ele = str(input())

    nombres.append(ele)


letra_buscada = input("Qué letra buscas?: ")
cantidad = 0

for nombre in nombres:
	for letra in nombre:
		if letra == letra_buscada:
			cantidad = cantidad + 1
			break
		else:
			cantidad = cantidad

print (cantidad)