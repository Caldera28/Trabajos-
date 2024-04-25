tiempo_vuelta_s = [120, 100, 80, 95, 90, 105, 83, 89, 96, 92]
tiempo_pits_s = [15, 20, 16, 25, 30, 27, 29, 32, 22, 36]
 
prom_vuelta = sum(tiempo_vuelta_s) / len(tiempo_vuelta_s)
prom_pits = sum(tiempo_pits_s) / len(tiempo_pits_s)
tpitsvsvuelta = (sum(tiempo_pits_s) / sum(tiempo_vuelta_s)) * 100
 
print('El tiempo promedio por vuelta es de: ', prom_vuelta, 'segundos')
print('El tiempo promedio por pits es de: ', prom_pits, 'segundos')
print('El porcentaje de tiempo utilizado en los pits corresponde: ', tpitsvsvuelta)