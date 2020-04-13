import sys


def create_matrix_sumizh():
    file = open('File.one.txt')
    info = file.readline()
    info_size = info.split(" ")
    if ((int(info_size[0]) == 0) and (int(info_size[1]) == 0)) or (int(info_size[0]) == 0):
        sys.exit("Помилка! Оскільки кількість вершин дорівнює нулю!")
    else:
        matrix_sumizh = [[0] * int(info_size[0]) for x in range(int(info_size[0]))]
        for i in range(int(info_size[1])):
            info_versh = file.readline()
            info_versh_arr = info_versh.split(" ")
            matrix_sumizh[int(info_versh_arr[0]) - 1][int(info_versh_arr[1]) - 1] = 1
            matrix_sumizh[int(info_versh_arr[1]) - 1][int(info_versh_arr[0]) - 1] = 1
        file.close()
        return matrix_sumizh


def output(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("%3d" % matrix[i][j], end=' ')
        print()


def step(matrix):
    array = []
    for i in range(len(matrix)):
        counter = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                counter += 1
        array.append(counter)
    print(array)
    return array


def check_on_cicl(array):
    global count
    for i in range(len(array)):
        if array[i] % 2 == 0:
            continue
        else:
            count += 1
            print("Граф не має Ейлеревого циклу!")
            break


def Eyler_1(matrix):
    array_1 = []
    j = 0
    array_1.append(1)
    for i in range(len(matrix)):
        while j < len(matrix):
            if matrix[i][j] == 1:
                for x in range(len(matrix)):
                    matrix[x][i]=0
                matrix[i][j] = 0
                array_1.append(j + 1)
                i = j
                j = 0
            elif matrix[i][j] == 0:
                j += 1
    print(array_1)


count = 0
sumizh_matrix = create_matrix_sumizh()
output(sumizh_matrix)
array = step(sumizh_matrix)
check_on_cicl(array)
if count == 0:
    Eyler_1(sumizh_matrix)
