P=int(input("- "))
Q=int(input("- "))
r=P**3+Q**4-2*P**2
if r>680:
    print("P y Q satisfacen la expresión: ", r, "> 680")
else:
    print("P y Q no Satisfacen la expresión: ", r, "no es mayor a 680")