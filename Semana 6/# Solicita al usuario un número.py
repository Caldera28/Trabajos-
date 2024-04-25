
numero = int(input('Ingrese un número: '))

cont = 0

for i in range(1, 100):
    if i % numero == 0:
        print(i)
        cont += 1
    if cont == 10:
        break
