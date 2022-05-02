while True:
    d=input()
    x,m=d.split(" ")
    x=int(x)
    m=int(m)
    if x==0 and m==0:
        break
    print(x*m)
