k=float(input("Kilómetros: "))
if k>300:
    if k<1000:
        print("Valor a pagar: ",round((k-300)*30000+70000,2))
    else:
        print("Valor a pagar: ",round((k-1000)*9000+150000,2))
