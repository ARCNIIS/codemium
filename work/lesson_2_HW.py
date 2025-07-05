import math

#Задание 1
radius1 = float(input("Введите радиус круга:"))
area1 = math.pi * (radius1 ** 2)
print("Площадь вашего круга:", area1)

#Задание 2
x = int(input("введите глобальную x: "))
def modify_variables():
    x = int(input("введите локальную x: "))
    print("Локальная x:", x)
    globals()['x'] = int(input("введите новую глобальную x: "))
modify_variables()
print("Глобальная x:", x)

#Заданиие 3
def charnum(txt, chr):
    num = 0
    for i in txt:
        if i == chr:
            num += 1
    return num
text = str(input("Введите текст:"))
char = str(input("Введите символ:"))
print("символ появился",charnum(text, char), "раз")