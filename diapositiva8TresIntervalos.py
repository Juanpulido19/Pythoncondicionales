x = float(input("Ingrese Su numero: "))

print("Intervalo 1")
min1 = float(input("Minimo: "))
max1 = float(input("Maximo: "))

print("Intervalo 2")
min2 = float(input("Minimo: "))
max2 = float(input("Maximo: "))

print("Intervalo 3")
min3 = float(input("Minimo: "))
max3 = float(input("Maximo: "))

if (x > min1 and x < max1) or (x > min2 and x < max2) or (x > min3 and x < max3):
    print("x esta dentro de alguno de los intervalos")
else:
    print("x esta fuera de los tres intervalos")
