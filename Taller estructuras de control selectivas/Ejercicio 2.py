s=float(input("Salario bruto en COP: "))
if s<900000:
    print("Aumento: ", s*0.15)
    print("El sueldo total es: ", s*0.15+s)
else:
    print("Aumento: ", s*0.12)
    print("El sueldo total es: ", s*0.12+s)