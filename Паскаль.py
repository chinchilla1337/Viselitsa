# функция возвращает строку треугольника паскаля с номером n(нумерация с нуля)
def pascal(n):
    li = [[1] * i for i in range(1, n + 2)]
    for j in range(len(li)):
        for m in range(1, len(li[j]) - 1):
            li[j][m] = li[j - 1][m - 1] + li[j - 1][m]
    return li[n]
