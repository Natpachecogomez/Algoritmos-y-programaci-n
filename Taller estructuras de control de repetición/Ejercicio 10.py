e=int(input("Digite la cantidad de estudiantes: "))
alm=0
for i in range(1,e+1):
    al=float(input("Digite altura: "))
    if(alm<=al):
        alm=al
print(alm)