#Дано n-значное целое число N. Определите, начинается ли оно с чётной цифры.

number = input("Введите число: ")

if int(number[0]) % 2 == 0:
     print("Цифра четная")
else:
    print("Цифра нечетная")