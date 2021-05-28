def hallar_inversion():
    cant_inv=int(input("ingrese la cantidad a invertir"))
    interes_anual=float(input("ingrese el interes anual"))
    num_años=int(input("ingrese el numero de años"))

    interes_total=interes_anual/100*num_años
    capital_invertido=cant_inv+cant_inv*interes_total

    print(capital_invertido)

hallar_inversion()  