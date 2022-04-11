import math
a=float(input("Lado a: "))
b=float(input("Lado b: "))
c=float(input("Lado c: "))
s=(a+b+c)/2
print("Área del triángulo:",math.sqrt(s*(s-a)*(s-b)*(s-c)))