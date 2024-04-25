def decimal_a_binario(numero):
    return bin(numero)

def decimal_a_octal(numero):
    return oct(numero)

def decimal_a_hexadecimal(numero):
    return hex(numero)

def mostrar_numero_en_base(numero, base):
    if base == "binario":
        resultado = decimal_a_binario(numero)
        print("El número en base binaria es:", resultado)
    elif base == "octal":
        resultado = decimal_a_octal(numero)
        return resultado
    elif base == "hexadecimal":
        resultado = decimal_a_hexadecimal(numero)
        return resultado
    else:
        return "Base no válida"

numero = int(input("Ingrese un número decimal: "))

resultado_binario = decimal_a_binario(numero)
print("El número en base binaria es:", resultado_binario)

resultado_octal = decimal_a_octal(numero)
print("El número en base octal es:", resultado_octal)

resultado_hexadecimal = decimal_a_hexadecimal(numero)
print("El número en base hexadecimal es:", resultado_hexadecimal)

base = input("Ingrese la base a la que desea convertir el número (binario, octal o hexadecimal): ")
numero_convertido = mostrar_numero_en_base(numero, base)
if numero_convertido:
    print("El número en la base especificada es:", numero_convertido)
else:
    print("Base no válida.")
