
datos = input("Introduce lista de numeros: ")
def procedimiento(datos):

	listado = list(datos)
	for i in listado:
		print ("*"*int(i))


procedimiento(datos)