vhn=float(input("Valor hora (COP): "))
vhe=vhn+vhn*0.25
print("Horas normales trabajadas")
hnt=int(input("Horas: "))
mnt=int(input("Minutos: "))
while mnt>60:
    print("Los minutos deben ser menores a 60")
    mnt=int(input("Minutos: "))
else:
    print("Horas extra trabajadas")
het=int(input("Horas: "))
met=int(input("Minutos: "))
while met>60:
    print("Los minutos deben ser menores a 60")
    met=int(input("Minutos: "))
else:
    hj=int(input("Número de hijos: "))
sh=((hnt+(mnt/60))*vhn)
she=((het+(met/60))*vhe)
sb=sh+she
ah=hj*173000
ta= sh+she+250000+ah+180000
pf=sb*0.05
ph=sb*0.02
ca=sb*0.07
td=pf+ph+ca
print("ASIGNACIONES")
print("     Horas:", round(sh,2), "COP")
print("     Horas extra:",round(she,2), "COP")
print("     Actualización académica: 250000 COP")
print("     Asignación por hijo:",round(ah,2), "COP" )
print("     Prima por hogar: 180000 COP")
print("     Total asignaciones: ",round(ta,2),"COP")
print("DEDUCCIONES")
print("     Paro forzoso:", round(pf,2),"COP")
print("     Política habitacional:", round(ph,2),"COP")
print("     Caja de ahorro: ", round(ca,2),"COP")
print("     Total deducciones: ", round(td,2),"COP")
print("SUELDO NETO", round(ta-td,2),"COP")
