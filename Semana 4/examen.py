
temperaturas_por_dia = {
    'Lunes': [],
    'Martes': [],
    'Miércoles': [],
    'Jueves': [],
    'Viernes': []
}

def promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas) if len(temperaturas) > 0 else 0

def maximo(temperaturas):
    return max(temperaturas) if len(temperaturas) > 0 else 0

def minimo(temperaturas):
    return min(temperaturas) if len(temperaturas) > 0 else 0

while True:
    print("Seleccione el día que desea ingresar (6 para mostrar resultados y salir):")
    print("[1] Lunes")
    print("[2] Martes")
    print("[3] Miércoles")
    print("[4] Jueves")
    print("[5] Viernes")
    print("[6] Mostrar resultados y salir")

    opcion = input("Opción: ")

    if opcion == '6':
        break
    elif opcion in ['1', '2', '3', '4', '5']:
        dia = ''
        if opcion == '1':
            dia = 'Lunes'
        elif opcion == '2':
            dia = 'Martes'
        elif opcion == '3':
            dia = 'Miércoles'
        elif opcion == '4':
            dia = 'Jueves'
        elif opcion == '5':
            dia = 'Viernes'

        cant_personas = int(input(f'Ingrese la cantidad de personas para el día {dia}: '))

        temperaturas = []

        for i in range(cant_personas):
            nombre = input(f'Ingrese el nombre de la persona {i + 1}: ')
            temp = float(input(f'Ingrese la temperatura de {nombre}: '))
            temperaturas.append(temp)

        temperaturas_por_dia[dia] = temperaturas

# Mostrar resultados
for dia, temps in temperaturas_por_dia.items():
    print(f'{dia}:')
    print(f'- Temperatura promedio: {promedio(temps)}')
    print(f'- Temperatura máxima: {maximo(temps)}')
    print(f'- Temperatura mínima: {minimo(temps)}')
