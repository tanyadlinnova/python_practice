
import random

def print_two_matrix(matrix_local_1, matrix_local_2):
    print("  1 2 3 4 5 6     1 2 3 4 5 6")
    for i in range(len(matrix_local_1)):
        print(i,  end=" ")
        for element in matrix_local_1[i]:
            print(element, end=" ")
        print(' ', i,  end=" ")
        for element in matrix_local_2[i]:
            print(element, end=" ")
        print()
    print()

class Board:
    def __init__(self):
        self.matrix = [
     ['~', '~', '~', '~', '~', '~']
    ,['~', '~', '~', '~', '~', '~']
    ,['~', '~', '~', '~', '~', '~']
    ,['~', '~', '~', '~', '~', '~']
    ,['~', '~', '~', '~', '~', '~']
    ,['~', '~', '~', '~', '~', '~']]
        self.ships = []

    def add_ship(self, x, y, angle, type_of_ship):
        ship = Ship(x, y, angle, type_of_ship)


        intersection = False
        #Ставим ли мы корабль в корректное место?
        for point in ship.points:
            x = point[0]
            y = point[1]

            if not (x >= 0 and x < 6 and y >= 0 and y < 6): #не выходим ли мы за границы поля?
                intersection = True
                break
            if self.matrix[y][x] == "O" or self.matrix[y][x] == "-":
                intersection = True
                break

        if not intersection:
            self.ships.append(ship)
            for point in ship.points:
                x = point[0]
                y = point[1]

                self.matrix[y][x] = "O"

            for shift_x in [-1, 0, 1]:
                for shift_y in [-1, 0, 1]:
                    for point in ship.points:
                        x = point[0] + shift_x
                        y = point[1] + shift_y

                        if x >= 0 and x < 6 and y >= 0 and y < 6:
                            if self.matrix[y][x] != "O":
                                self.matrix[y][x] = "-"

        return intersection

    def print_matrix(self):
        print("  1 2 3 4 5 6")
        i = 1
        for row in self.matrix:
            print(i,  end=" ")
            i += 1
            for element in row:
                print(element, end=" ")
            print()
        print()

class Ship:
    def __init__(self, x, y, angle, type_of_ship):
        self.x = x
        self.y = y
        self.angle = angle
        self.type_of_ship = type_of_ship

        self.points = []

        if angle == 0:
            for i in range(type_of_ship):
                self.points.append([x + i, y])
        else:
            for i in range(type_of_ship):
                self.points.append([x, y + i])

board_1 = Board()
list_of_ships_types = [3, 2, 2, 1, 1, 1, 1]
if 0:
    for size_of_ship in list_of_ships_types:
        #Расстановка кораблей
        #Вывести поле, спросить у пользователя, куда ставить корабль

        board_1.print_matrix()
        print(f"Куда ставить корабль {size_of_ship}-палубный? Три переменные, x, y и угол поворота(0 или 90)")

        while 1:
            raw_input = input("Введите координаты: ")
            split = raw_input.split()
            x, y, angle = list(map(int, split))
            error = board_1.add_ship(x - 1, y - 1, angle, size_of_ship)
            if error == False:
                break
else:
    while 1:
        board_1 = Board()
        trial_counter = 150

        for size_of_ship in list_of_ships_types:
            #Расстановка кораблей ботом

            while 1:
                x = random.randint(1, 6)
                y = random.randint(1, 6)
                angle = random.randint(0, 1)

                trial_counter -= 1
                if trial_counter <= 0:
                    break
                error = board_1.add_ship(x - 1, y - 1, angle, size_of_ship)
                if error == False:
                    break

            if trial_counter <= 0:
                break

        if len(list_of_ships_types) == len(board_1.ships):
            break
        board_1.print_matrix()

while 1:
    board_2 = Board()
    trial_counter = 150

    for size_of_ship in list_of_ships_types:
        #Расстановка кораблей ботом

        while 1:
            x = random.randint(1, 6)
            y = random.randint(1, 6)
            angle = random.randint(0, 1)

            trial_counter -= 1
            if trial_counter <= 0:
                break
            error = board_2.add_ship(x - 1, y - 1, angle, size_of_ship)
            if error == False:
                break

        if trial_counter <= 0:
            break

    if len(list_of_ships_types) == len(board_2.ships):
        break

#board_2.print_matrix()

#ФАЗА СТРЕЛЬБЫ
current_player = 1

boards_targets = [board_2, board_1] # мишень игрока первого и мишень игрока второго
while 1:
    print_two_matrix(board_1.matrix, board_2.matrix)
    print(f"Выстрел {current_player}-го игрока")
    raw_input = input("Введите координаты выстрела: ")
    split = raw_input.split()
    x, y = list(map(int, split))
    if boards_targets[current_player - 1].matrix[y][x] == "-" or boards_targets[current_player - 1].matrix[y][x] == "~":
        boards_targets[current_player - 1].matrix[y][x] = "T"
        current_player = 3 - current_player #смена хода
    elif boards_targets[current_player - 1].matrix[y][x] == "O":
        boards_targets[current_player - 1].matrix[y][x] = "X" #смена хода не требуется
        #Проверка на то не потоплен ли корабль
        for ship in boards_targets[current_player - 1].ships:
            ship_alive = False
            for point in ship.points:
                x, y = point
                if boards_targets[current_player - 1].matrix[y][x] == "O":
                    ship_alive = True
            if ship_alive == False:
                #Красим, что корабль мертв
                for point in ship.points:
                    x, y = point
                    boards_targets[current_player - 1].matrix[y][x] = "K" #Kill
                #Расставляем промахи вокруг корабля
                for shift_x in [-1, 0, 1]:
                    for shift_y in [-1, 0, 1]:
                        for point in ship.points:
                            x = point[0] + shift_x
                            y = point[1] + shift_y

                            if x >= 0 and x < 6 and y >= 0 and y < 6:
                                if boards_targets[current_player - 1].matrix[y][x] != "K":
                                    boards_targets[current_player - 1].matrix[y][x] = "T"

    #Проверка на то не закончилась ли игра
    any_ship_alive = False
    for ship in boards_targets[current_player - 1].ships:
        for point in ship.points:
            x, y = point
            if boards_targets[current_player - 1].matrix[y][x] == "O":
                any_ship_alive = True

    if any_ship_alive == False:
        print(f"Победа {current_player}-го игрока")
        break
print_two_matrix(board_1.matrix, board_2.matrix)
