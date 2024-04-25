
anio_nacimiento = int(input("Ingrese su año de nacimiento (YYYY): "))

if (anio_nacimiento % 4 == 0 and anio_nacimiento % 100 != 0) or (anio_nacimiento % 400 == 0):
    print("El año", anio_nacimiento, "es un año bisiesto.")
else:
    print("El año", anio_nacimiento, "no es un año bisiesto.")
