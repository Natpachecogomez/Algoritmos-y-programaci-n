archivo = open('paises.txt', 'r')
#imprima la posicion de colombia
'''
list=[]
for i in archivo:
  list.append(i)
  if (i=="Colombia: Bogotá\n"):
    a=list.index(i)+1
print(a)
'''
#Imprima todos los paises
'''
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
'''
#Imprima todas las Capitales
'''
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
'''  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la letra M  
'''
lista=[]
ciudades=[]
c=0
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudades.append(a)
  lista=[]
for i in ciudades:
  if (i[0]=="M"):
    c=c+1
    print(i)
print("Cantidad de ciudades con M:",c)
'''
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
'''
for i in archivo:
  if i[0]=="U":
    a=i.index(":")
    if i[a+2]=="U":
      print(i)
    elif i[a+2]=="U":
      print("En el archivo no hay paises que tanto su nombre como capital empiecen con U")
      break
'''
#En caso de que el ejercicio sea generar dos listas, una de paises y otra de capitales que empiezan con U:
'''
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  if a[0]=="U":
    paises.append(a)
  lista=[]
print("Países que empiezan con U")
print(paises)
archivo = open('paises.txt', 'r')
list=[]
ciudad=[]
for e in archivo:
  a=e.index(":")
  for r in range(a+2,len(e)-1):
    list.append(e[r])
  a="".join(list)
  if a[0]=="U":
    ciudad.append(a)
  list=[]
print("Capitales que empiezan con U")
print(ciudad)
'''
#Cuente e imprima cuantos paises que hay en el archivo
'''
list=[]
for i in archivo:
  list.append(i)
print(len(list))
'''
#Busque e imprima la ciudad de Singapur
"""
lista=[]
ciudades=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudades.append(a)
  lista=[]
for i in ciudades:
  if (i=='Singapur\n'):
    print(i)
"""
#Busque e imprima el pais de Venezuela y su capital
'''
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  if a=="Venezuela":
    break
  lista=[]
print(i)
'''
#Cuente e imprima las ciudades que su pais inicie con la letra E
'''
c=0
cap=[]
for i in archivo:
  if i[0]=="E":    
    c=c+1
    a=i.index(":")
    for r in range(a+2,len(i)):
      cap.append(i[r])
    a="".join(cap)
    print(a)
    cap=[]
print("Cantidad de capitales con paises que empiezan con E",c)
'''
#Busque e imprima la Capiltal de Colombia
'''
lista=[]
cap=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  if a=="Colombia":
    a=i.index(":")
    for r in range(a+2,len(i)):
      cap.append(i[r])
    a="".join(cap)
    print(a)
    break
  lista=[]
'''
#imprima la posicion del pais de Uganda
'''
list=[]
for i in archivo:
  list.append(i)
  if (i=="Uganda: Kampala\n"):
    a=list.index(i)+1
print(a)
'''
#imprima la posicion del pais de México
'''
list=[]
for i in archivo:
  list.append(i)
  if (i=="México: Ciudad de México\n"):
    a=list.index(i)+1
print(a)
'''
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
'''
archivo = open('paises.txt', 'r+')
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  if a=="Madagascar":
    texto=i.replace("Madagascar: rey julien","Madagascar: Antananarivo")
    print(texto)
    break
  lista=[]
'''
#Agregue un país que no esté en la lista 
'''
archivo = open('paises.txt', 'r+')
lista=[]
d=""
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  if a=="Natalia":
    d='Encontrado'
    break
  lista=[]
if d=='Encontrado':
  print("Existe el país")
else:
    archivo.write("\nNatalia: Pacheco Gómez")
'''
archivo.close()