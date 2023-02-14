string = input("Введите текст:")

list_of_words = string.split()

unique_words = set(list_of_words)

total = list(unique_words)

counter = len(total)

print(counter)
