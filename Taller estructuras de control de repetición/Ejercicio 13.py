ce=int(input("Cantidad de estudiantes: "))
pfmax=0
sumpf=0
epfin=0
epfsp=0
npfmax=" "
npfmin=" "
pfmin=0
puntaje=[None]*ce
pmmin=0
pmmax=0
for i in range (1,ce+1):
    n=input("Nombre del estudiante: ")
    pf=float(input("Puntaje final: "))
    puntaje[i-1]=pf
    sumpf=pf+sumpf
    if(pfmax<=pf):
        pfmax=pf
        npfmax=n
    if(pfmax>pf):
        pfmin=pf
        npfmin=n
print("Estudiante con mayor puntaje final:",npfmax)
print("Estudiante con menor puntaje final:",npfmin)
print("Máximo puntaje obtenido:",pfmax)
print("Mímimo puntaje obtenido:",pfmin)
print("Promedio puntajes:",round(sumpf/ce,2))
for i in range (1,ce+1):
    if puntaje[i-1]<sumpf/ce:
        pmmin=pmmin+1
    elif puntaje[i-1]>sumpf/ce:
        pmmax=pmmax+1
print("Porcentaje estudiantes con puntaje final menor al promedio:",round(pmmin/ce,2))
print("Porcentaje estudiantes con puntaje final mayor al promedio:",round(pmmax/ce,2))