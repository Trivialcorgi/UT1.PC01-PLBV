ano = int(input("Escriba un año para saber si es bisiesto:"))

def es_bisiesto(ano):
	if ano%4 == 0:
			print(f'{ano} Es bisiesto')
	else:
		print(f'{ano} No es bisiesto')

es_bisiesto(ano)