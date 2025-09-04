# вывод квадратной матрицы размерности n
def print_matrix(matrix, n, width):
    for i in range(n):
        for j in range(n):
            print(str(matrix[i][j]).ljust(width), end=" ")
            n = int(input())


# считывание матрицы с n строками
n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
    print()

matrix = [[277, -930, 11, 0], [9, 43, 6, 87], [4456, 8, 290, 7], [56, 89, 4, 23]]
