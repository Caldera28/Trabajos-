#Ejercicio 3

categoria = int(input("Ingrese la categoría del colaborador (1-4): "))
salario_base = float(input("Ingrese el salario base del colaborador: "))

if categoria == 1:
    aumento = 0.10
elif categoria == 2:
    aumento = 0.12
elif categoria == 3:
    aumento = 0.15
elif categoria == 4:
    aumento = 0.20
else:
    print("Categoría no válida")
    exit()

salario_total = salario_base * (1 + aumento)

print("El salario total del colaborador es:", salario_total)
