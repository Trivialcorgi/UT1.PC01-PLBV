print ("Ingrese tres numeros a comparar")

num1 = input()
num2 = input()
num3 = input()

def nmayor (num1,num2,num3):
    if num1>num2>num3:
        print ("el mayor numero es",num1)
    elif num1<num2>num3:
        print ("el mayor numero es",num2)
    else:
        print ("el mayor numero es",num3)

nmayor (num1,num2,num3)