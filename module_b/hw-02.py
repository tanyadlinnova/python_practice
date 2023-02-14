def print_matrix(matrix_local):
    print("  0 1 2")
    i = 0
    for row in matrix_local:
        print(i,  end=" ")
        i += 1
        for element in row:
            print(element, end=" ")
        print()
    print()

def check_win(matrix_local):
    is_win = False
    for flag in ["X", "O"]:
        #проверка строк
        for i in range(3):
            if matrix_local[0][i] == flag and matrix_local[1][i] == flag and matrix_local[2][i] == flag:
                is_win = True
                print(f"Победили {flag}")

        #проверка столбцов
        for i in range(3):
            if matrix_local[i][0] == flag and matrix_local[i][1] == flag and matrix_local[i][2] == flag:
                is_win = True
                print(f"Победили {flag}")

        #проверка диагоналей
        if matrix_local[0][0] == flag and matrix_local[1][1] == flag and matrix_local[2][2] == flag:
             is_win = True
             print(f"Победили {flag}")
        if matrix_local[2][0] == flag and matrix_local[1][1] == flag and matrix_local[0][2] == flag:
             is_win = True
             print(f"Победили {flag}")

    return is_win

def check_dead_heat(matrix_local):
    dead_heat = True
    for row in matrix_local:
        for element in row:
            if element == "-":
                dead_heat = False
    if dead_heat:
        print("Ничья")
    return dead_heat


matrix = [
    ['-', '-', '-']
   ,['-', '-', '-']
   ,['-', '-', '-']
]

print_matrix(matrix)

flag = "X"

while 1:
    print(f"Ходит {flag}:")
    raw_input = input("Введите координаты: ")

    correct = True
    if raw_input == "":
        correct = False
    if not correct:
        print("Вы ничего не ввели\n")
        continue

    split = raw_input.split()
    if len(split) != 2:
        print("Недопустимое количество координат\n")
        continue


    if not (split[0] in ["0", "1", "2"]):
        correct = False
    if not (split[1] in ["0", "1", "2"]):
        correct = False
    if not correct:
        print("Недопустимые координаты\n")
        continue

    coords = list(map(int, split))

    if matrix[coords[1]][coords[0]] != "-":
        correct = False

    if not correct:
        print("Перезапись хода\n")
        continue

    matrix[coords[1]][coords[0]] = flag

    print_matrix(matrix)

    if check_win(matrix) or check_dead_heat(matrix):
        print("Game over")
        break

    if flag == "X":
        flag = "O"
    else:
        flag = "X"

