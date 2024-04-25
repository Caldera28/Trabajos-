
Mapa=[[0,0,0],

       [0,0,0],

       [0,0,0]]
 
def cambiar_elemento(Mapa):

    fila = int(input("Introduce la fila del mapa donde quiere esconder el tesoro: "))

    columna = int(input("Introduce la columna del mapa donde quiere esconder el tesoro: "))

    nuevo_valor = int(input("Introduce tesoro(1): "))

    Mapa[fila][columna] = nuevo_valor
 
def adivinar_posicion(Tablero):

    while True:

        fila = int(input("Adivina la fila del mapa: "))

        columna = int(input("Adivina la columna del mapa: "))

        valor = int(input("Adivina el valor(1): "))

        if Mapa[fila][columna] == valor:

            print(f"Encontro el tesoro tenia {1} monedas en su interior")

            return True

        else:

            print("Sigue intentando")

 
 
cambiar_elemento(Mapa)

adivinar_posicion(Mapa)