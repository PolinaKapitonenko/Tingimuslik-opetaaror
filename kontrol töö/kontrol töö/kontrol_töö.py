#Võimalus 3


#1 1 Написать программу, которая по данному числу n от 1 до 9 выводит на экран n скворечников. 
#Между двумя соседними скворечниками также имеется пустой (из пробелов) столбец. 
#Разрешается вывести пустой столбец после последнего скворечника. 
#Для упрощения рисования скопировать скворечник из примера в среду разработк
n = int(input("Sisestage number (1-9): "))

for i in range(n):
    print("   -----")
    print("  |  O  |")
    print("  !  -  !")
    print("   ------   ")




#4 Мой богатый дядюшка подарил мне один доллар в мой первый день рождения. 
#В каждый день рождения он увеличивал свой подарок и прибавлял к нему столько долларов, сколько лет мне исполнилось. 
#Написать программу, указывающую, к какому дню рождения подарок превысит 100$.


kingitus = 1
vana = 1

while kingitus <= 100:
    kingitus += vana
    vana += 1

print("See võtab", vana, "sünnipäevad ületada $100.")





#2 Вывести степени натуральных чисел, не превосходящие данного числа n**3. Пользователь задает показатель степени и число n.
kraad = int(input("Sisesta astme pöördväärtus: "))
n = int(input("Sisesta n: "))

for i in range(1, n+1):
    tulemus = i ** kraad
    if tulemus <= n ** 3:
        print(i, "^", kraad, "=", tulemus)
    else:
        break




#3Известны оценки по физике каждого из  учеников класса. Определить среднюю оценку. (Оценки и количество учеников получаем случайным образом)
import random

õpilanearv = random.randint(5, 30)
grades = ()

for i in range(õpilanearv):
    grade = random.randint(2, 5)
    grades.append(grade)

average_grade = sum(grades) / õpilanearv
print("Keskmine hinne on: ", average_grade)
