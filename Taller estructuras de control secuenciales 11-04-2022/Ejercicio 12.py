print("Matemáticas")
i=1
s=0
while i<=3:
    t=float(input("Tarea: "))
    i=i+1
    s=t+s
em=float(input("Examen: "))
pm=round(((s/3)*0.10)+(em*0.90),1)
print("Física")
i=1
s=0
while i<=3:
    t=float(input("Tarea: "))
    i=i+1
    s=t+s
ef=float(input("Examen: "))
pf=round(((s/3)*0.20)+(ef*0.80),1)
print("Química")
i=1
s=0
while i<=3:
    t=float(input("Tarea: "))
    i=i+1
    s=t+s
eq=float(input("Examen: "))
pq=round(((s/3)*0.15)+(eq*0.85),1)
print("El promedio de matemáticas es:",pm)
print("El promedio de física es:",pf)
print("El promedio de química es:",pq)
print("El promedio de las tres materias es: ",round(((pq+pf+pm)/3),2))
