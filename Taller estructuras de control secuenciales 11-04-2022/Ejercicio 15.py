pf=float(input("Precio final: "))
pvp=float(input("Precio de venta al público: "))
print("Descuento: ", round(((pvp-pf)/pvp)*100,1), "%")