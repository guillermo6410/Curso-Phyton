lista = [27, 33, 11, 22, 81, 3, 8]
menor = None
mayor = None

for numero in lista:
    if menor == None and mayor == None:
        menor = numero
        mayor = numero

    else:
        if numero < menor:
            menor = numero
        if numero > mayor:
            mayor = numero

print(f"El numero mayor es: {mayor}")  
print(f"El numero menor es: {menor} ")     