
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
board_2 = Board()
list_of_ships_types = [3, 2, 2, 1, 1, 1, 1]
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


