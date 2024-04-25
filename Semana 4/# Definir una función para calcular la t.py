
def temperatura_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def temperatura_maxima(temperaturas):
    return max(temperaturas)

def temperatura_minima(temperaturas):
    return min(temperaturas)


temperaturas_por_dia = {
    'Lunes': [],
    'Martes': [],
    'Miércoles': [],
    'Jueves': [],
    'Viernes': []
}

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

        cantidad_personas = int(input(f'Ingrese la cantidad de personas para el día {dia}: '))

        for i in range(cantidad_personas):
            nombre = input(f'Ingrese el nombre de la persona {i+1}: ')
            temperatura = float(input(f'Ingrese la temperatura de {nombre}: '))

            temperaturas_por_dia[dia].append(temperatura)

for dia, temperaturas in temperaturas_por_dia.items():
    if temperaturas:
        print(f'{dia}:')
        print(f'- Temperatura promedio: {temperatura_promedio(temperaturas)}')
        print(f'- Temperatura máxima: {temperatura_maxima(temperaturas)}')
        print(f'- Temperatura mínima: {temperatura_minima(temperaturas)}')
