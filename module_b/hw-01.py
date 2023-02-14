

print("Cодержит ли число цифры цифры, 5, 7 или 9:")
number = int(input("Введите число: "))

flag = "NO"

while number > 0:
    if number % 10 == 5 or number % 10 == 7 or number % 10 == 9:
       flag = "YES"
    number = number // 10
print(flag)
