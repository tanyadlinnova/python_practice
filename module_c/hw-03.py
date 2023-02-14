
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
    ['-', '-', '-', '-', '-', '-']
   ,['-', '-', '-', '-', '-', '-']
   ,['-', '-', '-', '-', '-', '-']
   ,['-', '-', '-', '-', '-', '-']
   ,['-', '-', '-', '-', '-', '-']
   ,['-', '-', '-', '-', '-', '-']]
        self.ships = []

    def add_ship(self, x, y, angle, type_of_ship):
        ship = Ship(x, y, angle, type_of_ship)
        self.ships.append(ship)

        for point in ship.points:
            x = point[0]
            y = point[1]
            self.matrix[y][x] = "O"


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

    raw_input = input("Введите координаты: ")
    split = raw_input.split()
    x, y, angle = list(map(int, split))

    board_1.add_ship(x, y, angle, size_of_ship)


