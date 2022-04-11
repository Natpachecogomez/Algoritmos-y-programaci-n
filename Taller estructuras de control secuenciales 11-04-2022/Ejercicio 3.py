s=float(input("Sueldo base: "))
i=1
ad=0
while i<=3:
    v=float(input("Venta: "))
    i=i+1
    ad=v+ad
cm=ad*0.1
print("Comisión:",cm)
print("Sueldo total:",cm+s)