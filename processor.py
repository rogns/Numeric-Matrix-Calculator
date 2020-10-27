import numpy as np


class Matrix:
    count = 0

    def __init__(self):
        self.arr = [] # Cria a lista (para futura matriz)
        self.line, self.colum = [int(x) for x in input().split()]  # Atribui o numero de linhas e colunas

    def make_mtx(self):
        while self.count < self.line:
            self.arr.append(list(map(float, input().split()))) # Insere as linhas(e colunas) na lista (tonando-a matriz)
            self.count += 1


def obj_make_mtx(option):
    lst = []
    if option == "1":
        print("Enter size of first matrix:")
        mtx_A = Matrix()
        print("Enter first matrix:")
        mtx_A.make_mtx()
        print("Enter size of second matrix:")
        mtx_B = Matrix()
        print("Enter second matrix:")
        mtx_B.make_mtx()
        lst.append(mtx_A)
        lst.append(mtx_B)
    elif option == "2":
        print("Enter size of matrix: ")
        mtx_A = Matrix()
        print("Enter matrix:")
        mtx_A.make_mtx()
        lst.append(mtx_A)
    elif option == "3":
        print("Enter size of first matrix:")
        mtx_A = Matrix()
        print("Enter first matrix:")
        mtx_A.make_mtx()
        print("Enter size of second matrix:")
        mtx_B = Matrix()
        print("Enter second matrix:")
        mtx_B.make_mtx()
        lst.append(mtx_A)
        lst.append(mtx_B)
    elif option == "4" or "5" or "6":
        print("Enter matrix size: ")
        mtx_A = Matrix()
        print("Enter matrix:")
        mtx_A.make_mtx()
        print("The result is:")
        lst.append(mtx_A)

    return lst

def add_mtx(option):
    mtx = obj_make_mtx(option)
    mtx_A = mtx[0]
    mtx_B = mtx[1]

    if mtx_A.line == mtx_B.line and mtx_A.colum == mtx_B.colum:
        print("The result is:")
        mtx_c = np.add(mtx_A.arr, mtx_B.arr)
        lst = 0
        #mtx_c = mtx_c.astype(int)
        while lst < mtx_A.line:
            print(*mtx_c[lst], sep=" ")
            lst += 1
    else:
        print("The operation cannot be performed.")
    menu()


def const_mtx(option):
    mtx = obj_make_mtx(option)
    mtx_A = mtx[0]

    print("Enter constant:")
    x = float(input())
    print("The result is:")

    def multiply(n):
        return n * x
    lst = 0
    while lst < mtx_A.line:
        result = map(multiply, mtx_A.arr[lst])
        print(*result, sep=" ")
        lst += 1
    menu()


def multi_mtx(option):
    mtx = obj_make_mtx(option)
    mtx_A = mtx[0]
    mtx_B = mtx[1]

    print("The result is:")
    res = np.dot(mtx_A.arr, mtx_B.arr)
    #res = res.astype(int)
    lst = 0
    while lst < mtx_A.line:
        print(*res[lst], sep=" ")
        lst += 1
    menu()

def transpose_mtx(option, option2):
    mtx = obj_make_mtx(option)
    mtx_A = mtx[0]
    count = 0
    if option2 == "1":
        mtx_A.arr = np.array(mtx_A.arr)
        mtx_A.arr = mtx_A.arr.transpose()
        while count < mtx_A.line:
            print(*mtx_A.arr[count], sep=" ")
            count += 1
    elif option2 == "2":
        lst = []
        for x in range(mtx_A.colum):
            lst.append([])
            for y in range(mtx_A.line):
                lst[x].append(mtx_A.arr[-1 - y][-1 - x])
        while count < mtx_A.line:
            print(*lst[count], sep=" ")
            count += 1
    elif option2 == "3":
        lst = []
        for x in range(mtx_A.line):
            lst.append([])
            for y in range(mtx_A.colum):
                lst[x].append(mtx_A.arr[x][mtx_A.colum - 1 - y])
        while count < mtx_A.line:
            print(*lst[count], sep=" ")
            count += 1
    elif option2 == "4":
        lst = []
        for x in range(mtx_A.line):
            lst.append([])
            for y in range(mtx_A.colum):
                lst[x].append(mtx_A.arr[mtx_A.line - 1 - x][y])
        while count < mtx_A.line:
            print(*lst[count], sep=" ")
            count += 1

def calc_determinant(option):
    mtx = obj_make_mtx(option)
    mtx_A = mtx[0]

    det = np.linalg.det(mtx_A.arr)

    print(det)

def calc_inverse(option):
    mtx = obj_make_mtx(option)
    mtx_A = mtx[0]

    det = np.linalg.inv(mtx_A.arr)

    lst = 0
    while lst < mtx_A.line:
        #result = map(det, mtx_A.arr[lst])
        print(*det[lst], sep=" ")
        lst += 1
    menu()

def menu():
    print("1. Add matrices\n""2. Multiply matrix by a constant\n"
          "3. Multiply matrices\n""4. Transpose matrix\n"
          "5. Calculate a determinant\n""6. Inverse Matrix\n""0. Exit")
    option = input("Your choice: ")
    if option == "1":
        add_mtx(option)
    elif option == "2":
        const_mtx(option)
    elif option == "3":
        multi_mtx(option)
    elif option == "4":
        print("1. Main diagonal\n""2. Side diagonal\n"
              "3. Vertical line\n""4. Horizontal line\n")
        option2 = input("Your choice: ")
        transpose_mtx(option, option2)
    elif option == "5":
        calc_determinant(option)
    elif option == "6":
        calc_inverse(option)
    else:
        return 0


menu()
