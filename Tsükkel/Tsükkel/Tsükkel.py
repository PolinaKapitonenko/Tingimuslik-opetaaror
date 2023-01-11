from math import *
from random import *



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