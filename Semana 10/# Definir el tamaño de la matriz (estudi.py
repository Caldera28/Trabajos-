# Definir el tamaño de la matriz (estudiantes x actividades)
num_estudiantes = 5
num_actividades = 4

# Inicializar la matriz de calificaciones con ceros
calificaciones = []

# Solicitar al usuario que ingrese las calificaciones para cada estudiante y actividad
for i in range(num_estudiantes):
    fila_calificaciones = []
    print(f"Ingrese las calificaciones del estudiante {i + 1}:")
    for j in range(num_actividades):
        calificacion = float(input(f"Calificación de la actividad {j + 1}: "))
        fila_calificaciones.append(calificacion)
    calificaciones.append(fila_calificaciones)

# Sumar todas las calificaciones en la matriz
suma_total = 0
for fila in calificaciones:
    for calificacion in fila:
        suma_total += calificacion

# Imprimir el resultado
print(f"La suma total de todas las calificaciones es: {suma_total}")
