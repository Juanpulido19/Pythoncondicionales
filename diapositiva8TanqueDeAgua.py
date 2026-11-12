nivelDelTanque = float(input("Ingrese el nivel del tanque en litros: "))

if nivelDelTanque < 250:
    print("la llave debe ser abierta")
else:
    if nivelDelTanque > 450:
        print("la llave debe ser cerrada")
    else:
        print("El tanque esta en un nivel bueno!")
