num1 = float(input("Ingresa tu primer numero: "))
num2 = float(input("Ingresa tu Segundo numero: "))
num3 = float(input("Ingresa tu Tercer numero: "))
num4 = float(input("Ingresa tu Cuarto numero: "))

if num1 < num2 and num2 < num3 and num3 < num4:
    print(num1, "Es mayor broski")
else:
    if num2 > num1 and num2 > num3 and num3 > num4:
        print(num2, "Es mayor broski")
    else:
        if num3 > num1 and num3 > num2 and num3 > num4:
            print(num3, "Es mayor")
        else:
            print(num4, "Es el mayor de todos los mayores")
