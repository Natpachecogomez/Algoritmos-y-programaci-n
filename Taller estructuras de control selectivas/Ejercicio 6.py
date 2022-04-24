A=int(input("Primer dígito: "))
if A>9:
    print("El dígito debe ser menor que 9")
    A=int(input("Primer dígito: "))
B=int(input("Segundo dígito: "))
if B>9:
    print("El dígito debe ser menor que 9")
    B=int(input("Segundo dígito: "))
C=int(input("Tercer dígito: "))
if C>9:
    print("El dígito debe ser menor que 9")
    C=int(input("Tercer dígito: "))
D=int(input("Cuarto dígito: "))
if D>9:
    print("El dígito debe ser menor que 9")
    D=int(input("Cuarto dígito: "))
print("Número: ", str(A)+str(B)+str(C)+str(D))
if D>=5:
    if C<9:
        print("Redondeado: ",str(A)+str(B)+str(C+1)+str(0))
    else:
        print("Redondeado: ",str(A)+str(B+1)+str(0)+str(0))
elif C>=5:
    if B<9:
        print("Redondeado: ",str(A)+str(B+1)+str(0)+str(0))
    else:
        print("Redondeado: ",str(A+1)+str(0)+str(0)+str(0))
elif B>=5:
    print("Redondeado: ",str(A+1)+str(0)+str(0)+str(0))
if D<5 and C<5 and B<5:
    print("Redondeado: ",str(A)+str(B)+str(0)+str(0))
