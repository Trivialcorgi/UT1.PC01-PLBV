print ("Introduce las edades de las 10 personas:")
edades = []

for i in range(0, 10):
    ele = int(input())

    edades.append(ele)
cantidad = 0

for elemento in edades:
	if elemento >= 20:
		cantidad = cantidad + 1
	else:
		cantidad = cantidad

print(cantidad)
