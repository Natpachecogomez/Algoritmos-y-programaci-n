d={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5}
l=[]
c=0
j=""
for i in d:
    a=d[i]
    for g in range(0,c):
        if a==l[g]:
            j="igual"
            break
        else:
            j=""
    if j!="igual":
        l.append(d[i])
        c=c+1
print(l)