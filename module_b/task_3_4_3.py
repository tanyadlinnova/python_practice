#В задании ниже вам нужно написать код, который выводит на экран обозначение ветра
#в зависимости от его характера

speed = 0

if speed >= 1 and speed <= 4:
    print("Weak")
elif speed >= 5 and speed <= 10:
    print("Moderate")
elif speed >= 11 and speed <= 18:
    print("Strong")
elif speed >= 19:
    print("Hurricane")
else:
    print("error")
