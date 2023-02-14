
#Напишите программу, которая получает на вход название книги - title, фамилию автора - author и год выпуска - year.

#Полученные данные должны быть преобразованы в словарь book с ключами: title, author, year. Причем
#year нужно преобразовать в тип int.

#Примечание. Обратите внимание, что для отправки кода на проверку переменные title, author, year объявлять не нужно.
#Не забудьте удалить строку кода с её объявлением перед тем, как отправить код на тестирование.

title = input("title = ")
author = input("author = ")
year = input("year = ")


book = dict()
book["title"] = title
book["author"] = author
book["year"] = int(year)


# book = {'title' : title,
#         'author' : author,
#         'year' : int(year)}

print(book)
