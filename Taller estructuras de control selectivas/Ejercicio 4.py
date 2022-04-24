m=float(input("Monto compra COP: "))
if m<5000000:
    print("Inversión de la empresa:",round(m*0.55,2))
    print("Prestamo al banco:",round(m*0.30,2))
    print("Crédito fabricante:",round(m*0.15,2))
    print("Interés del fabricante:",round((m*0.15)*0.20,2))
else:
    print("Inversión de la empresa:",round(m*0.70,2))
    print("Crédito fabricante:",round(m*0.30,2))
    print("Interés del fabricante:",round((m*0.30)*0.20,2))