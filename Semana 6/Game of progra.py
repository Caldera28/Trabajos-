
n = int(input('Ingrese el número de estudiantes: '))

enero = 0
febrero = 0
marzo = 0
abril = 0
mayo = 0
junio = 0
julio = 0
agosto = 0
septiembre = 0
octubre = 0
noviembre = 0
diciembre = 0
suma_edades = 0

for i in range(1, n+1):
    print(f'Estudiante {i}')
    mes = input('Ingrese el mes de nacimiento: ').lower()
    edad = int(input('Ingrese la edad del estudiante: '))
 
    if mes == 'enero':
        enero += 1
    elif mes == 'febrero':
        febrero += 1
    elif mes == 'marzo':
        marzo += 1
    elif mes == 'abril':
        abril += 1
    elif mes == 'mayo':
        mayo += 1
    elif mes == 'junio':
        junio += 1
    elif mes == 'julio':
        julio += 1
    elif mes == 'agosto':
        agosto += 1
    elif mes == 'septiembre':
        septiembre += 1
    elif mes == 'octubre':
        octubre += 1
    elif mes == 'noviembre':
        noviembre += 1
    elif mes == 'diciembre':
        diciembre += 1

    suma_edades += edad

print('\nCantidad de estudiantes que cumplen años en cada mes:')
print(f'Enero: {enero}')
print(f'Febrero: {febrero}')
print(f'Marzo: {marzo}')
print(f'Abril: {abril}')
print(f'Mayo: {mayo}')
print(f'Junio: {junio}')
print(f'Julio: {julio}')
print(f'Agosto: {agosto}')
print(f'Septiembre: {septiembre}')
print(f'Octubre: {octubre}')
print(f'Noviembre: {noviembre}')
print(f'Diciembre: {diciembre}')

promedio_edades = suma_edades / n
print(f'El promedio de las edades de los estudiantes es: {promedio_edades:}')
