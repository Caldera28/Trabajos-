N = int(input("Ingrese el número de estudiantes: "))
 
estaturas = []
 
for x in range(N):
    while True:
        estatura = float(input("Ingrese la estatura del estudiante (entre 100 y 140 cm): "))
        if estatura >= 100 and estatura <= 140:
            estaturas.append(estatura)
            break
        else:
            print("La estatura debe estar en el rango entre 100 y 140 cm.")
 
if len(estaturas) > 0:
    promedio = sum(estaturas) / len(estaturas)
    print("El promedio de las estaturas de los estudiantes es: ", promedio)
else:
    print("No se ingresaron estaturas válidas.")
 
print("Las estaturas ingresadas son ",estaturas)