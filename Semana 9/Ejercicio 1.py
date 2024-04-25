kilometros_por_dia = [0] * 7 

for dia in range(7): 
    kilometros = float(input(f"Ingrese los kilometros reccoridos por dia {dia + 1}:"))
    kilometros_por_dia[dia] = kilometros 


total_semana = 0 
for dia in range(7):
    total_semana += kilometros_por_dia[dia]
    print(f"Dia {dia +1}: {kilometros_por_dia[dia]} kilometros")

print(f"Total de kilometros recorridos en la semana {total_semana} kilometros")