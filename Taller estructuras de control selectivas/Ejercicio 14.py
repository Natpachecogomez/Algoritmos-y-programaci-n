la=float(input("Lectura anterior: "))
l=float(input("Lectura actual: "))
c=l-la
if c>=0 and c<=100:
    print("Monto a pagar: ", c*4600)
elif c>=101 and c<=300:
    print("Monto a pagar: ", c*80000)
elif c>=301 and c<=500:
    print("Monto a pagar: ", c*100000)
elif c>=501:
    print("Monto a pagar: ", c*120000)