ganancias_por_dia = []

for dia in range(1, 8):
    ganancia = float(input(f"Ingrese las ganancias del día {dia}: "))
    ganancias_por_dia.append(ganancia)

total_ganado = sum(ganancias_por_dia)
dia_menos_ganancia = ganancias_por_dia.index(min(ganancias_por_dia)) + 1

print("\nTotal ganado en la semana:", total_ganado)
print("El día con menos ganancias fue el día", dia_menos_ganancia, "con", ganancias_por_dia[dia_menos_ganancia - 1])
