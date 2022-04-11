C=float(input("Costo por kilovatio (kW): "))
LA=int(input("Lectura actual: "))
LP=int(input("Lectura anterior: "))
while LP>LA:
    print("La lectura anterior debe ser menor o igual a la actual")
    LP=int(input("Lectura anterior: "))
else:
    print("Monto total: ",(LA-LP)*C)