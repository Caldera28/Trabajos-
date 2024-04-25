#Ejercicio 9

ingresos_mensuales = float(input("Ingrese sus ingresos mensuales: "))
gastos_alimentacion = float(input("Ingrese sus gastos mensuales en alimentación: "))

porcentaje_gastos_alimentacion = (gastos_alimentacion / ingresos_mensuales) * 100
porcentaje_disponible_otros_rubros = 100 - porcentaje_gastos_alimentacion

print(f"El porcentaje de gastos en alimentación es: {porcentaje_gastos_alimentacion}%")
print(f"El porcentaje disponible para otros rubros es: {porcentaje_disponible_otros_rubros}%")
