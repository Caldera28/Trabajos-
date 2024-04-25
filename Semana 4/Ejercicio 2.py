# Ejercicio 2 
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

if numero1 < numero2:
    numero1, numero2 = numero2, numero1

if numero1 < numero3:
    numero1, numero3 = numero3, numero1

if numero2 < numero3:
    numero2, numero3 = numero3, numero2

print("Los números ordenados en orden descendente son:", numero1, ",", numero2, ",", numero3)
