tipo = input("Ingrese el tipo de articulo: ")

if tipo == "Textil":
    print("Descuento: 0 %")
else:
    if tipo == "Electrodomestico":
        print("Descuento: 3.7 %")
    else:
        if tipo == "Elementos de cocina":
            print("Descuento: 4.2 %")
        else:
            if tipo == "Video juego":
                print("Descuento: 7.8 %")
            else:
                print("Tipo de articulo no valido o no aplica para descuento")
