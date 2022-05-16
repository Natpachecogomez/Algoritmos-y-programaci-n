import random
word=["vaca", "tortuga", "cerdo", "ardilla", "foca", "serpiente"]
rand=random.choice(word)
tries=len(rand)
list=[]
print(rand)

for i in rand:
    list.append(i)
aux=[]
lcopy=list.copy()

for x in range (len(list)):
    aux.append("-")

while tries!=0:
    tries-=1
    let=input("Letra: ")
    try:
        for i in range(len(list)):
            p=lcopy.index(let)
            aux.pop(p)
            aux.insert(p,let)
            lcopy.pop(p)
            lcopy.insert(p, '-')
    except:
        pass
    print(aux)
    try:
        p=list.index(let)
    except:
        print("La letra no está en la palabra")

if tries==0:
    if aux==list:
        print("\nYou've won (✿ ◡ ‿ ◡ )")
    else:
        print("      -----\n      |   |\n      O   |\n     /|\  |   You've lost (┬┬﹏┬┬)\n     / \  |\n          |")