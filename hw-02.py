matrix = [
    ['-', '-', '-']
   ,['-', '-', '-']
   ,['-', '-', '-']
]
def print_matrix(matrix_local):
    print("  0 1 2")
    i = 0
    for row in matrix_local:
        print(i,  end = " ")
        i += 1
        for element in row:
            print(element, end = " ")
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

print_matrix(matrix)

flag = "X"
while 1:
    print(f"Ходит {flag}:")
    raw_input = input("Введите координаты: ")
    coords = list(map(int, raw_input.split()))

    matrix[coords[1]][coords[0]] = flag

    print_matrix(matrix)

    if check_win(matrix):
        print("Game over")
        break

    if flag == "X":
        flag = "O"
    else:
        flag = "X"

