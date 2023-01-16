from math import *
from random import *
from winreg import *


#1
while True:
    try:
        nimi=input("Palun siseta oma nimi: ")
        if nimi=="SIIM":
            n=int(input("Palun siseta mitu krda soovin tervitus saada: "))#n=korda
            for i in range(1, n+1): # i=katsete arv
                print(f"Ole tervitatud, {nimi}, {i}. korda. ")
        else:
            break
    except:
        print("!!!")






#------------------------------------------------------------------------
#0===
p=0
while True:
    number = int(input("Sisestage number suurem kui 10: "))
    p+=1
    if number >= 10:
        print("Õigesti")
        break
    else:
        print("Arv on liiga väike!")
print("katsed", p)

#---------------------------------------------------------------
#22.2.0
katsed=0
answer=""
while answer!="komm":
    answer=input("Tahan kommi!")
    katsed+=1
print(f"katsed: {katsed}")
print()




#22
print("Ma tahan kommi")
katsed = 0
while True:
    answer = input("Tahan kommi!")
    katsed += 1
    if answer.lower() == "kommi":
        print(f"Teil kommid kirjutakse kulus {katsed} katse.")
        break

#------------------------------------------------------------------------

#11ülesane
print("arvuti mõistatab nubrit 1-10 ja sina üritab seda ära arvata")
a=randint(1,10)
vastus=int(input("Mis arv on mõistatanud arvutit?: "))
k=p=1 
while vastus!=a:
    print("Ära sa ei arvanud ära, proovi uuesti!: ")
    vastus=int(input("Sisesta vastus: "))
    k+=1
    p+=1
    if k>2:
        print("Püüdlused on lõppenud")
        b=input("Kas roovi veel kord: ")
        if b.upper()=="JAH":
            k=0
            continue
        else:
            break
if vastus==a:
    print("Palju õnne, sa arvasid ära!",p )

print()


#------------------------------------------------------------------------
#0
n = input("Введите целое число: ")
while type(n) != int:
    try:
        n = int(n)
    except:
        n = input("Введите целое число: ")
if n % 2 == 0:
    print("Четное")
else:
    print("Нечетное")


#------------------------------------------------------------------------

#2 ülesanne(6)
n=0
print ("kolmnurga")
for e in range (11,0,-1):
    n = n + 1
    for f in range (1, n+1):
        print ("*", end = "")
    print()
print ("")

#1 ülesanne(6)
for x in range(5):
    print("******") 

#3 ülesanne(6)


print ("kolmnurga")
for g in range (11,0,-1):
    n = n - 1
    for h in range (0, n-1):
        print ("*", end = "")
    print()

#------------------------------------------------------------------------




#-----------------------------
for i in range(1,11):
    print("*"*i,end="")
    print()
#---------------------------------
for i in range(1,5):
    x=str("*"*i).center(14," ")
    print(x, end="")
    print()
for i in range(1,10):
    x=str("*"*(i+2)).center(14," ")
    print(x, end="")
    print()
for i in range(1,15):
    x=str("*"*(i+4)).center(14," ")
    print(x, end="")
    print()





