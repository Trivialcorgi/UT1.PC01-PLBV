print ("Ingrese el caracter a verificar")

caracter = input()

def verificar(caracter):
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        print ("True")
    elif caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
        print ("True")
    else:
        print ("False")

verificar(caracter)