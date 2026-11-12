numeroVerificacion = int(input("Ingrese un número entero entre 0 y 20: "))

if numeroVerificacion < 0 or numeroVerificacion > 20:
    print("Error: El número debe estar entre 0 y 20.")
else:
    if numeroVerificacion in (2, 3, 5, 7, 11, 13, 17, 19):
        print(numeroVerificacion, "es primo.")
    else:
        print(numeroVerificacion, "NO es primo.")
