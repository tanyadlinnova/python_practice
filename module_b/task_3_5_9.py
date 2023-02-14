
print("Что надеть?")
temperature = int(input("Температура выше 20 градусов и меньше 30? \n1 - YES, 2 - NO \n"))

if temperature == 1:
    isRain = int(input("Есть осадки? \n1 - YES, 2 - NO\n"))
    if isRain == 1:
        print("Футболку, шорты и дождевик")
    else:
        print("Футболку и шорты")
else:
    temperature = int(input("Температура выше 0 градусов? \n1 - YES, 2 - NO\n"))
    if temperature == 2:
        print("Пуховик")
    else:
        isRain = int(input("Есть осадки? \n1 - YES, 2 - NO\n"))
        if isRain == 2:
            print("Пальто")
        else:
            isRain = int(input("Осадки сильные? \n1 - YES, 2 - NO\n"))
            if isRain == 1:
                print("Пальто,резиновые сапоги и зонт")
            else:
                print("Пальто и дождевик")



