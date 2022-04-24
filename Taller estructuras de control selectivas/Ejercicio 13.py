from datetime import datetime
d=int(input("¿Qué día naciste? "))
m=int(input("¿En qué mes naciste? "))
y=int(input("¿En qué año naciste? "))
if(m==1):
    if(d<=20):
        print("Capricornio")
    elif(d>=21 and d<31):
        print("Acuario")
    else:
        print("El número tiene que ser menor a 31")
if(m==2):
    if(d<=19):
        print("Acuario")
    elif(d>=20 and d<28):
        print("Piscis")
    else:
        print("El número tiene que ser menor a 28")
if(m==3):
    if(d<=21):
        print("Piscis")
    elif(d>=22 and d<31):
        print("Aries")
    else:
        print("El número tiene que ser menor a 31")
if(m==4):
    if(d<=20):
        print("Aries")
    elif(d>=21 and d<30):
        print("Tauro")
    else:
        print("El número tiene que ser menor a 30")
if(m==5):
    if(d<=21):
        print("Tauro")
    elif(d>=22 and d<31):
        print("Géminis")
    else:
        print("El número tiene que ser menor a 31")
if(m==6):
    if(d<=21):
        print("Géminis")
    elif(d>=22 and d<30):
        print("Cáncer")
    else:
        print("El número tiene que ser menor a 30")
if(m==7):
    if(d<=22):
        print("Cáncer")
    elif(d>=23 and d<31):
        print("Leo")
    else:
        print("El número tiene que ser menor a 31")
if(m==8):
    if(d<=23):
        print("Leo")
    elif(d>=24 and d<31):
        print("Virgo")
    else:
        print("El número tiene que ser menor a 31")
if(m==9):
    if(d<=23):
        print("Virgo")
    elif(d>=24 and d<30):
        print("Libra")
    else:
        print("El número tiene que ser menor a 30")
if(m==10):
    if(d<=22):
        print("Libra")
    elif(d>=23 and d<31):
        print("Escorpión")
    else:
        print("El número tiene que ser menor a 31")
if(m==11):
    if(d<=21):
        print("Escorpión")
    elif(d>=22 and d<30):
        print("Sagitario")
    else:
        print("El número tiene que ser menor a 30")        
if(m==12):
    if(d<=21):
        print("Sagitario")
    elif(d>=22 and d<31):
        print("Capricornio")
    else:
        print("El número tiene que ser menor a 31")
if(datetime.now().month>m):
    print("Tu edad es ",datetime.now().year-y)
else:
    print("Tu edad es ",(datetime.now().year-1)-y)