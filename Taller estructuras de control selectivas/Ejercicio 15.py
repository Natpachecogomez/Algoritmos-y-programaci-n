e=input("Si la edad es en meses escriba M, si es en años escriba A : ")
ed=int(input("Ingrese la edad: "))
s=input("Esrciba W si es mujer, si es hombre escriba H: ")
h=float(input("Nivel de hemoglobina: "))
if e=="M" and ed==0 or ed==1:
    if h<13:
        print("El paciente tiene anemia")
    else:
        print("El paciente no tiene anemia")
elif e=="M" and ed>1 or ed<=6:
    if h<11:
        print("El paciente tiene anemia")
    else:
        print("El paciente no tiene anemia")
elif e=="M" and ed>6 or ed<=12:
    if h<11:
        print("El paciente tiene anemia")
    else:
        print("El paciente no tiene anemia")
elif e=="A" and ed>1 or ed<=5:
    if h<11.5:
        print("El paciente tiene anemia")
    else:
        print("El paciente no tiene anemia")
elif e=="A" and ed>5 or ed<=10:
    if h<12.6:
        print("El paciente tiene anemia")
    else:
        print("El paciente no tiene anemia")
elif e=="A" and ed>10 or ed<=15:
    if h<13:
        print("El paciente tiene anemia")
    else:
        print("El paciente no tiene anemia")
elif e=="A" and ed>15 and s=="W":
    if h<12:
        print("El paciente tiene anemia")
    else:
        print("El paciente no tiene anemia")
elif e=="A" and ed>15 and s=="H":
    if h<14:
        print("El paciente tiene anemia")
    else:
        print("El paciente no tiene anemia")