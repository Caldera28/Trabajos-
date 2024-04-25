
fila_de_teatro = [""] * 10

for i in range(10):
    nombre = input("Ingrese el nombre del ocupante: ")
    butaca = int(input("Ingrese el número de butaca (1 a 10): "))
    
    if 1 <= butaca <= 10:
        fila_de_teatro[butaca - 1] = nombre
    else:
        print("Número de butaca inválido. Debe ser entre 1 y 10.")

print("\nEstado de la fila de teatro:")
for i in range(10):
    print("Butaca {}: {}".format(i + 1, fila_de_teatro[i]))

