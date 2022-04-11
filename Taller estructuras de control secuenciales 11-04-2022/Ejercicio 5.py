i=1
s=0
while i<=3:
    p=float(input("Parcial: "))
    i=i+1
    s=p+s
s=(s/3)*0.55
ef=float(input("Nota examen final: "))
ef=ef*0.30
tf=float(input("Nota trabajo final: "))
tf=tf*0.15
print("Porcentaje parciales: ",s)
print("Porcentaje examen final: ",ef)
print("Porcentaje trabajo final: ",tf)
print("Calificación final: ",s+ef+tf)