m=0
h=0
s=0
n=0
ag=0
ro=0
ce=0
te=0
wh=0
ot=0
e25=0
e245=0
e465=0
e65=0
de="s"
c=0
while de=="s":
    g=input("Digite m=mujer y h=hombre: ")
    if g=="m":
        m=m+1
    else:
        h=h+1
    e=int(input("Ingrese su edad: "))
    if e<=25:
        e25=e25+1
    elif e<=45:
        e245=e245+1
    elif e<=65:
        e465=e465+1
    else:
        e65=e65+1
    t=input("Digite s=si toma y n=si no: ")
    if t=="s":
        q=7
        while q>6:
            q=int(input("1-Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro: "))
    if t=="s":
        s=s+1
        if q==1:
            ag=ag+1
        elif q==2:
            ro=ro+1
        elif q==3:
            ce=ce+1
        elif q==4:
            te=te+1
        elif q==5:
            wh=wh+1
        else:
            ot=ot+1
    else:
        n=n+1
    c=c+1
    de=input("Si desea seguir digite s, sino cualquier letra")
print("Cantidad encuestados: ",c)
print("Mujeres:", m)
print("Hombres:", h)
print("RANGO DE EDAD")
print("Menores de 25:",e25)
print("Entre 26 y 45:",e245)
print("Entre 46 y 65:",e465)
print("Mayores a 66:",e65)
print("¿CUÁNTOS TOMAN, CUÁNTOS NO?")
print("Sí:",s)
print("No:",n)
print("¿QUÉ TOMAN?")
print("Aguardiente:",ag)
print("Ron:",ro)
print("Cerveza:",ce)
print("Tequila:",te)
print("Whisky:",wh)
print("Otro:",ot)