s=0
ce=0
wh=0
de="s"
c=0
m18=0
h2a=0
ec=0
while de=="s":
    c=c+1
    print("Encuesta número", c)
    g=input("Digite m=mujer y h=hombre: ")
    e=int(input("Ingrese su edad: "))
    t=input("Digite s=si toma y n=si no: ")
    if t=="s":
        q=7
        while q>6:
            q=int(input("1-Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro: "))
    if g=="m":
        if e<19:
            m18=m18+1
    if g=="h":
        if e>=20 and e<=25:
            if t=="s":
                if q!=1:
                    h2a=h2a+1
    if t=="s":
        s=s+1
        if q==3:
            ce=ce+1
            ec=ec+e
        elif q==5:
            wh=wh+1
    de=input("Si desea seguir digite s, sino cualquier letra: ")
print("Cantidad encuestados: ",c)
print("Personas que consumen licor:",s)
print("Mujeres menores de edad:",m18)
print("Hombres que toman, pero no aguardiente entre 20 y 25:",h2a)
print("Promedio edad personas que consumen cerveza:",round(ec/ce,2))
print("Porcentaje de personas que consumen whisky:",round(wh/c*100,2))