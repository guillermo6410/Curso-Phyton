print("Ingrese la figura para determinar su area")
print("1.Triangulo\n2.Cuadrado\n3.Rectangulo\n4.Circulo\n5.Rombo\n")
opcion=int(input("Ingresar opcion deseada"))

if(opcion==1):
    base=int(input("Ingrese la base"))
    altura=int(input("Ingrese la altura"))
    resultado = (base*altura)/2
    print("El area es de:", resultado)

if(opcion==2):
    base=int(input("Ingrese la base"))
    altura=int(input("Ingrese la altura"))
    resultado = (base*altura)
    print("El area es de:", resultado)

if(opcion==3):
    base=int(input("Ingrese la base"))
    altura=int(input("Ingrese la altura"))
    resultado = (base*altura)
    print("El area es de:", resultado)

if(opcion==4):
    radio=int(input("Ingrese el radio"))
    resultado = (radio**2)*3.1416
    print("El area es de:", resultado)


if(opcion==5):
    diagonal_mayor=int(input("Ingrese Diagonal Mayor"))
    diagonal_menor=int(input("Ingrese Diagonal Menor"))
    resultado = (diagonal_mayor*diagonal_menor)/2
    print("El area es de:", resultado)