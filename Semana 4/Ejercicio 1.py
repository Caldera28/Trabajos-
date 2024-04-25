
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
numero4 = float(input("Ingrese el cuarto número: "))

if numero1 > numero2:
    mayor_numero = numero1
else:
    mayor_numero = numero2

if numero3 > mayor_numero:
    mayor_numero = numero3

if numero4 > mayor_numero:
    mayor_numero = numero4

print("El número más grande es:", mayor_numero)
