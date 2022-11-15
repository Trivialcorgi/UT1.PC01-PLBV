print ("Comparar caracteres de dos listas")

lista1 = []
lista2 = []
n1 = int(input("Introduce numeros de elementos : "))
n2 = int(input("Introduce numeros de elementos : "))

print (lista1,lista2)
def superposicion(lista1,lista2):
	print ("Elementos comunes", set(lista1) & set(lista2))

superposicion(lista1,lista2)

