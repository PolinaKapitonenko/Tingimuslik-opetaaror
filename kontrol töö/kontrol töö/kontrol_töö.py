#Võimalus 3


#1
n = int(input("Sisestage number (1-9): "))

for i in range(n):
    print("   -----")
    print("  |  O  |")
    print("  !  -  !")
    print("   ------   ")

#4


kingitus = 1
vana = 1

while kingitus <= 100:
    kingitus += vana
    vana += 1

print("See võtab", vana, "sünnipäevad ületada $100.")


#2
kraad = int(input("Sisesta astme pöördväärtus: "))
n = int(input("Sisesta n: "))

for i in range(1, n+1):
    tulemus = i ** kraad
    if tulemus <= n ** 3:
        print(i, "^", kraad, "=", tulemus)
    else:
        break

#3
import random

õpilanearv = random.randint(5, 30)
grades = ()

for i in range(õpilanearv):
    grade = random.randint(2, 5)
    grades.append(grade)

average_grade = sum(grades) / õpilanearv
print("Keskmine hinne on: ", average_grade)
