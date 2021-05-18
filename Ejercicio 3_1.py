palabra = input ( "Introduce una palabra:")
palabra = palabra.lower()
vocales = ["a","e","i","o","u","á","é","í","ó","ú"]


for x in vocales:
    veces = 0
    for y in palabra:
        if x == y:
            veces+=1

    print("La vocal", x, "aparece", veces, "veces")       