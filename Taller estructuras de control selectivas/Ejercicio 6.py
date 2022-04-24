A=int(input("Primer dígito: "))
B=int(input("Segundo dígito: "))
C=int(input("Tercer dígito: "))
D=int(input("Cuarto dígito: "))
if A>9 and B>9 and C>9 and D>9:
    print("El dígito debe ser menor que 9")
    A=int(input("Primer dígito: "))
    B=int(input("Segundo dígito: "))
    C=int(input("Tercer dígito: "))
    D=int(input("Cuarto dígito: "))
print("Número: ", str(A)+str(B)+str(C)+str(D))
if C>=5:
    if B<9:
        print("Redondeado: ",str(A)+str(B+1)+str(0)+str(0))
    else:
        print("Redondeado: ",str(A+1)+str(0)+str(0)+str(0))
else:
    print("Redondeado: ",str(A)+str(B)+str(0)+str(0))