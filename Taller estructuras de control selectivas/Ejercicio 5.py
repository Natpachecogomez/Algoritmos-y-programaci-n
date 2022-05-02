s=float(input("Salario bruto mensual: "))
v1=float(input("Ventas departamento 1: "))
v2=float(input("Ventas departamento 2: "))
v3=float(input("Ventas departamento 3: "))
p=(v1+v2+v3)*0.33
if v1>p:
    if v2>p:
        if v3>p:
            print("Ningún departamento recibe bonificación")  
        else:
            print("Los departamentos 1 y 2 reciben la bonificación")
            print("Salario total")
            print("Departamento 1: ",s+s*0.20,"\n"+"Departamento 2: ",s+s*0.20,"\n"+"Departamento 3: ",s)
    else:
        print("El departamento 1 recibe la bonificación")
        print("Salario total")
        print("Departamento 1: ",s+s*0.20,"\n"+"Departamento 2: ", s,"\n"+"Departamento 3: ", s)
elif v2>p:
    if v3>p:
        print("Los departamentos 2 y 3 reciben la bonificación")
        print("Salario total")
        print("Departamento 1: ",s,"\n"+"Departamento 2: ",s+s*0.20,"\n"+"Departamento 3: ",s+s*0.20)
    else:
        print("El departamento 2 recibe la bonificación")
        print("Salario total")
        print("Departamento 1: ",s,"\n"+"Departamento 2: ",s+s*0.20,"\n"+"Departamento 3: ",s)
elif v3>p:
    print("El departamento 3 recibe la bonificación")
    print("Salario total")
    print("Departamento 1: ",s,"\n"+"Departamento 2: ",s,"\n"+"Departamento 3: ",s+s*0.20)