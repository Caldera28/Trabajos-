salario = input("Ingrese su salario")
salario = float(salario)

if salario > 1000:
    salario = salario * 1.15
    print("Su salario aplicando un 15%:", salario)
else:
    salario = salario * 1.20
    print("Su salario aplicando un20%:", salario) 
    
