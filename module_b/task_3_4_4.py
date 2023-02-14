
#Запишите условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.

number_a = int(input("Введите A: "))
number_b = int(input("Введите B: "))
number_c = int(input("Введите C: "))

result = False

if (number_a < 45 and number_b >= 45 and number_c >= 45) or \
        (number_a >= 45 and number_b < 45 and number_c >= 45) or \
        (number_a >= 45 and number_b >= 45 and number_c < 45):
    result = True
print(result)
