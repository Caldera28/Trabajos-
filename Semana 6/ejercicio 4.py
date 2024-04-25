
dinero_adicional = 0


for i in range(1, 16):
    salario = float(input(f'Ingrese el salario del empleado {i}: '))

    if salario < 500:
        dinero_adicional += 500 - salario

print(f'Se necesita un total de {dinero_adicional} para que todos al menos ganen 500')