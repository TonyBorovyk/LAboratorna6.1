import sys


def create_array_sumizh():
    file = open('File.one.txt')
    info = file.readline()
    info_size = info.split(" ")
    matrix_sumizh = []
    for i in range(int(info_size[1])):
        matrix_sumizh_1 = []
        info_versh = file.readline()
        info_versh_arr = info_versh.split(" ")
        matrix_sumizh_1.append(int(info_versh_arr[0]))
        matrix_sumizh_1.append(int(info_versh_arr[1]))
        matrix_sumizh.append(matrix_sumizh_1)
    file.close()
    return matrix_sumizh


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


def check_on_cicl(array):
    global count
    for i in range(len(array)):
        if array[i] % 2 == 0:
            continue
        else:
            count += 1
            print("Граф не має Ейлеревого циклу!")
            break


def step(matrix):
    array = []
    for i in range(len(matrix)):
        counter = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                counter += 1
        array.append(counter)
    return array


def Eyler_Algoritm(matrix,start_point):
    way = []
    new_matrix = matrix
    way.append(start_point)
    i = len(matrix) - 1
    while i >= 0 and new_matrix != None:
        if new_matrix[i][0] == start_point:
            new_point = new_matrix[i][1]
            way.append(new_point)
            del new_matrix[i]
            start_point = new_point
            i = len(matrix) - 1
        elif new_matrix[i][1] == start_point:
            new_point = new_matrix[i][0]
            way.append(new_point)
            del new_matrix[i]
            start_point = new_point
            i = len(matrix) - 1
        elif new_matrix[i][0] != start_point:
            i -= 1
    return way


def check_for_error(arr, matrix):
    array = []
    for i in range(len(matrix)):
        if matrix[i][0] not in array:
            array.append(matrix[i][0])
        if matrix[i][1] not in array:
            array.append(matrix[i][1])
        if len(matrix) + 1 == arr:
            sys.exit("Не існує Ейлеревого шляху та цикла!")
    return array


def output(arr):
    for i in arr:
        print("-", i, end=' ')


def check_on_cycle_Hamillton(array, matrix):
    global count
    if len(matrix) > 3:
        for i in range(len(array)):
            if array[i] >= len(matrix) // (len(matrix) // 2):
                continue
            elif array[i] < len(matrix) // 2:
                count = 1
                print("Граф не має Гамільтонового циклу!")
                break


def Hamillton(matrix):
    j = 0
    array_1 = []
    array_1.append(j + 1)
    for i in range(len(matrix)):
        while j < len(matrix):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                matrix[j][i] = 0
                for x in range(len(matrix)):
                    matrix[x][i] = 0
                array_1.append(j + 1)
                i = j
                j = 0
            elif matrix[i][j] == 0:
                j += 1
    if count != 1:
        array_1.append(1)

    return array_1


def check_Humillton(array_1, matrix):
    arr1 = sorted(array_1)
    for i in range(len(matrix)):
        if i + 1 != arr1[i] or len(array_1) != len(matrix):
            sys.exit("Не має цикла та маршрута")


result = int(input("Натисніть (1) для виконання першої частини (Ейлер) або (2) для (Гамільтон): "))

if result == 1:
    count = 0
    sumizh_matrix = create_matrix_sumizh()
    array_sumizh = create_array_sumizh()
    array1 = step(sumizh_matrix)
    check_on_cicl(array1)
    if count == 0:
        arr = Eyler_Algoritm(array_sumizh, 1)
        check_for_error(arr, create_array_sumizh())
        print("Ейлеровий цикл:")
        output(arr)
    elif count == 1:
        arr = Eyler_Algoritm(array_sumizh, 1)
        check_for_error(arr, create_array_sumizh())
        print("Ейлеровий шлях: ")
        output(arr)
elif result == 2:
    count = 0
    sumizh_matrix = create_matrix_sumizh()
    array_sumizh = create_array_sumizh()
    array1 = step(sumizh_matrix)
    check_on_cycle_Hamillton(array1, sumizh_matrix)
    if count == 0:
        print("Гамільтовий цикл:")
        array_h = Hamillton(sumizh_matrix)
        output(array_h)
    elif count == 1:
        print("Гамільтоновий шлях: ")
        array_h = Hamillton(sumizh_matrix)
        output(array_h)
