print ("Ingrese la palabra que quiere invertir")

palabra = input()

def inversa(palabra):
   invertida = palabra[::-1] #Con esto hacemos la inversa de la palabra
   print (invertida)

inversa(palabra)