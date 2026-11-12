a = float(input("ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

if a == 0:
    print("No es una ecuacion cuadratica")
else:
    descriminante = b ** 2 - 4 * a * c

    if descriminante < 0:
        print("No tiene soluciones")
    else:
        if descriminante == 0:
            print("Tiene una solucion")
        else:
            print("Tiene dos soluciones")
