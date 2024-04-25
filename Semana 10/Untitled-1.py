# Inicializar la matriz de asientos con 20 espacios disponibles (0 representa asiento libre)
asientos = [[0] * 4 for _ in range(5)]  # 5 filas (para 5 asientos) y 4 columnas (para 4 horarios)

# Función para imprimir la matriz de asientos
def imprimir_asientos():
    print("Estado actual de los asientos:")
    for fila in range(len(asientos)):
        for columna in range(len(asientos[0])):
            print(asientos[fila][columna], end=" ")
        print()

# Solicitar al usuario que reserve un asiento
while True:
    imprimir_asientos()
    fila = int(input("Ingrese el número de fila que desea reservar (1-5): "))
    if fila < 1 or fila > 5:
        print("¡Número de fila inválido! Inténtelo de nuevo.")
        continue
    columna = int(input("Ingrese el número de horario que desea reservar (1-4): "))
    if columna < 1 or columna > 4:
        print("¡Número de horario inválido! Inténtelo de nuevo.")
        continue

    # Verificar si el asiento está disponible
    if asientos[fila - 1][columna - 1] == 0:
        asientos[fila - 1][columna - 1] = 1  # Reservar el asiento (1 representa vendido)
        print(f"¡Asiento en la fila {fila}, horario {columna} reservado exitosamente!")
    else:
        print("¡Este asiento ya está reservado! Por favor, elija otro.")

    opcion = input("¿Desea reservar otro asiento? (s/n): ")
    if opcion.lower() != 's':
        break

print("Gracias por utilizar nuestro servicio de reserva de asientos.")
