def filtrar_palabras(lista, numero):
	array = []
	for palabra in lista:
		if len(palabra) >= numero:
			array.append(palabra)

	if len(array) == 0:
		print("Ninguna palabra :(")
	else:
		print(array)


lista = ["Que pasa", "loquito", "como", "estas?"]

numero = input("Escribe un numero: ")

filtrar_palabras(lista, numero)