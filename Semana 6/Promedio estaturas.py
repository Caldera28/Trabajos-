
estaturas = []
menos_de_100 = 0
entre_100_120 = 0
entre_121_130 = 0
entre_131_140 = 0
mas_de_140 = 0

n = int(input('Ingrese la cantidad de niños: '))
for i in range(n):
    print(f'Ingrese la estatura del niño {i+1} en cm:')
    estatura = float(input())
    estaturas.append(estatura)

    if estatura < 100:
        menos_de_100 += 1
    elif estatura <= 120:
        entre_100_120 += 1
    elif estatura <= 130:
        entre_121_130 += 1
    elif estatura <= 140:
        entre_131_140 += 1
    else:
        mas_de_140 += 1

promedio = sum(estaturas) / n

print(f'Cantidad de niños que miden menos de 100 cm: {menos_de_100}')
print(f'Cantidad de niños que miden entre 100 y 120 cm: {entre_100_120}')
print(f'Cantidad de niños que miden entre 121 y 130 cm: {entre_121_130}')
print(f'Cantidad de niños que miden entre 131 y 140 cm: {entre_131_140}')
print(f'Cantidad de niños que miden más de 140 cm: {mas_de_140}')
print(f'El promedio de estaturas es: {promedio} cm')
