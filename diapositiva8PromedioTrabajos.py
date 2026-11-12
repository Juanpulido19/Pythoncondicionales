nota1 = float(input("ingrese la nota de su primer trabajo: "))
nota2 = float(input("ingrese la nota de su segundo trabajo: "))
nota3 = float(input("ingrese la nota de su tercer trabajo: "))
nota4 = float(input("ingrese la nota de su cuarto trabajo: "))
nota5 = float(input("ingrese la nota de su quinto trabajo: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("Su promedio fue =", promedio)

if promedio < 3.5:
    print("Felicidades podras repetir el curso")
else:
    print("Lo lograste pasaste chaval")
