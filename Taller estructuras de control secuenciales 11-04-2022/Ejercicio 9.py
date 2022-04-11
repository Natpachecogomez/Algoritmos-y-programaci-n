v=float(input("Valor hora: "))
h=int(input("Horas trabajadas: "))
min=int(input("Minutos trabajados: "))
while min>60:
    print("Los minutos deben ser menores a 60")
    min=int(input("Minutos trabajados: "))
else:
    sb=((h+(min/60))*v)
print("El salario neto es: ", sb-sb*0.20)