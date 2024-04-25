#Ejercicio 8

horas_semanales = float(input("Ingrese la cantidad de horas semanales:"))
precio_por_hora = float(input("Ingrese el precio por hora:"))

salario_semanal = horas_semanales * precio_por_hora
salario_mensual = salario_semanal * 4.2

deduccion_cargas_sociales = salario_mensual * 0.105  
deduccion_asociacion_solidarista = salario_mensual * 0.05

salario_mensual_despues_deducciones = salario_mensual - deduccion_cargas_sociales - deduccion_asociacion_solidarista

print(f"El salario mensual después de las deducciones es: {salario_mensual_despues_deducciones}")
