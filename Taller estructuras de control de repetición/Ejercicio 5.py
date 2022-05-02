sm=0
c=0
for k in range(1,1000):
    sm=round(sm+((k**2)+1)/k,3)
    if(sm<=1000):
        c=c+1
print (c)