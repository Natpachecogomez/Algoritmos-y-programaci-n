P=float(input("Precio de contado: "))
T=float(input("Valor cuota (para 12 cuotas): "))
pc=T*12
r=pc-P
print("Porcentaje recargo: ", round(r*100/P,2), "%")