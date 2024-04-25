palabra = input("Ingrese una palara: ")

palabra_al_reves = ""

for i in range(len(palabra)-1, -1, -1):
    palabra_al_reves += palabra[i]

print("Palabra inversa:", palabra_al_reves)