# Función para resolver el Ejercicio 15
def ejercicio17(contagiados):
    c=0
    for i in range (len(contagiados)):
        if contagiados[i][3]==False and contagiados[i][1]>=20 and contagiados[i][1]<=30:
            c=c+1
    return c
contagiados=[]
s=int(input("Cantidad de personas a ingresar: "))
for x in range (s):
    r=input("Ingrese género (M para masculino y F para femenino), edad, días contagiado, muerte (si falleció escriba True, sino False): ")
    (g,e,dc,m)=r.split(",")
    g=str(g)
    e=int(e)
    dc=int(dc)
    m=str(m)
    if m=="False":
        m=False
    else:
        m=True
    contagiados.append((g,e,dc,m))
print("Cantidad personas entre 20 y 30 años que no fallecieron:",ejercicio17(contagiados))
# Pruebas de la función anterior
assert (ejercicio17([('M', 23, 12, False), ('M', 45, 3, False), ('M', 72, 6, True), ('F', 81, 11, True), ('M', 11, 12, False), ('M', 17, 8, True),
                   ('F', 77, 3, True), ('M', 67, 4, False), ('F', 61, 5, True), ('M', 14, 28, False), ('M', 44, 11, True), ('M', 6, 3, False),
                    ('M', 28, 19, False), ('F', 91, 10, True), ('F', 72, 6, True), ('F', 26, 5, False)])) == 3
print("Prueba superada 💪🏽")