#Ejercicio 5

Base = int(input("Ingrese un numero:"))
Altura = int(input("Ingrese un numero:"))

Area = Base * Altura
Perimetro = Base + Altura

print(f"El área del rectángulo es: {Area}")
print(f"El perímetro del rectángulo es: {Perimetro}")

#Ejercicio 6

distancia_casa_universidad = float(input("Ingrese la distancia de su casa a la universidad en kilometros:"))
costo_por_kilometro = float(input("Ingrese el costo por kilometro en su transporte:"))
dias_por_semana = int(input("Ingrese la cantidad de dias que va por semana a la universidad:"))

costo_total_por_viaje = (distancia_casa_universidad * 2) * costo_por_kilometro
costo_total_por_semana = costo_total_por_viaje * dias_por_semana
costo_total_por_cuatrimestre = costo_total_por_semana * 15

print(f"El costo total de trasladarse por cuatrimestre es: {costo_total_por_cuatrimestre} pesos.")
