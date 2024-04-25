#Ejercicio 4

edad_luis = int(input("Ingrese la edad de Luis: "))
edad_pedro = int(input("Ingrese la edad de Pedro: "))

temp = edad_luis
edad_luis = edad_pedro
edad_pedro = temp

print("Después del intercambio:")
print("Edad de Luis:", edad_luis)
print("Edad de Pedro:", edad_pedro)
