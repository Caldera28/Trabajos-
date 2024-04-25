tipo_figura = input("Ingrese el tipo de figura (C para cuadrado, T para triángulo): ").upper()

if tipo_figura == 'C':
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    area = lado ** 2
    perimetro = 4 * lado
    print("El área del cuadrado es:", area)
    print("El perímetro del cuadrado es:", perimetro)
elif tipo_figura == 'T':
    lado = float(input("Ingrese la longitud del lado del triángulo equilátero: "))
    area = (3 ** 0.5 / 4) * lado ** 2
    perimetro = 3 * lado
    print("El área del triángulo equilátero es:", area)
    print("El perímetro del triángulo equilátero es:", perimetro)
else:
    print("Tipo de figura no reconocido.")
