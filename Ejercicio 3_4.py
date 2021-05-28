def APLICAR_DESCUENTO(opc):
    precioManzana = 25
    precioPapa = 36
    precioCilantro = 22
    precioElote = 15
    precioJamon = 33
    precioQueso = 75
    descuentoManzana = .15
    descuentoPapa = .25
    descuentoCilantro = .12
    descuentoElote = .14
    if opc == 1:
        precioProducto = precioManzana - (precioManzana * descuentoManzana)
    elif opc == 2:
        precioProducto = precioPapa - (precioPapa * descuentoPapa)  
    elif opc == 3:
        precioProducto = precioCilantro - (precioCilantro * descuentoCilantro) 
    elif opc ==4:
        precioProducto = precioElote - (precioElote * descuentoElote)  
    elif opc == 5:
        precioProducto = precioJamon
    elif opc == 6:
        precioProducto = precioQueso
    return precioProducto

def APLICAR_IVA(precioProducto):
    precioTotal = precioProducto * 1.16
    return precioTotal

opc = int(input("Indica el producto deseas agregar al carrito. 1.-Manzana, 2.- Papa, 3.- Cilantro, 4.- Elote, 5.- Jamon, 6.- Queso: ")) 
subtotalProducto = APLICAR_DESCUENTO(opc) 
totalProducto = APLICAR_IVA(subtotalProducto)   
print ("El subtotal es de:" + str (subtotalProducto)) 
print ("El total es de:" + str(totalProducto))   
                   