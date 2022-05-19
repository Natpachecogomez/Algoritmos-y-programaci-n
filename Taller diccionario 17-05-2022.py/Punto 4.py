d={}
for i in range (10):
    nombre=input("Nombre estudiante: ")
    nota=int(input("Nota: "))
    d.update({i:{"nombre":nombre,"nota":nota}})

s=[]
a=[]
sum=0
for e in d:
    sum=int(d[e]["nota"])+sum
    if d[e]["nota"]<6:
        s.append(d[e]["nombre"])
    else:
        a.append(d[e]["nombre"])

print("Estudiantes que suspenden:",s)
print("Estudiantes que aprueban:",a)
print("Promedio de la clase:",sum/10)