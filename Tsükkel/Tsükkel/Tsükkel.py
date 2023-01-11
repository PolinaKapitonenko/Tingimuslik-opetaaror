from math import *
from random import *




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




















#2ülesanne(6)
n=0
print ("*kolmnurga")
for e in range (11,0,-1):
    n = n + 1
    for f in range (0, n+1):
        print ("*", end = "")
    print()
print ("")



#1 ülesanne(6)
for x in range(5):
    print("******") 

#ülesanne(6)
#3

print ("kolmnurga")
for g in range (11,0,-1):
    n = n - 1
    for h in range (0, n-1):
        print ("*", end = "")
    print()


#0