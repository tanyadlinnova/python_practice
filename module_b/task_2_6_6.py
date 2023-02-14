
#Напишите программу, которая на вход получает последовательность чисел, а выводит модифицированный список:

    #  Первое и последнее числа последовательности должны поменяться местами.
   #     В конец списка нужно добавить сумму всех чисел.


string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # cписок чисел

list_of_numbers[0],list_of_numbers[-1] = list_of_numbers[-1],list_of_numbers[0]

total = sum(list_of_numbers)
list_of_numbers.append(total)

print(list_of_numbers)
