
#Запишите логическое выражение, которое определяет, что число А НЕ
# принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.

number = int(input("Введите число: "))

cond_1 = number > -10 and number < -1
cond_2 = number > 2 and number < 15

if cond_1 or cond_2:
    print("False")

else:
    print("True")




