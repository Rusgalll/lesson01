# 1

def next_row(row):
    row = [1] + row
    for i in range(1, len(row) - 1):
        row[i] += row[i + 1]
    return row


def pascal_triangle(n):
    row = []
    for _ in range(n):
        row = next_row(row)
        print(*row)


# pascal_triangle(10)

# 4


def rotateMatrix():
    n = 3
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    i = n - 1
    while i >= 0:
        j = n - 1
        while j >= 0:
            print(mat[i][j], end=" ")
            j = j - 1
        print()
        i = i - 1


# rotateMatrix()


# 5

def swap_columns(a, b):
    n = 3
    m = 4
    matrix = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]

    change = [a, b]
    a, b = change[0], change[1]

    for i in range(n):
        matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]

    for row in matrix:
        print(*row)


# swap_columns(0, 1)


# 6
def filling_with_snake(n, m):
    matrix = [[0 for i in range(m)] for _ in range(n)]
    count = 1
    for i in range(n):
        for j in range(m):
            matrix[i][j] += count
            count += 1
    for i in range(n):
        if i % 2 == 0:
            print(*matrix[i])
        else:
            matrix[i].reverse()
            print(*matrix[i])


# filling_with_snake(3, 4)


# 7

def matrixTranspose():
    matrix = [[1, 2, 0, 4], [1, 0, 2, 0]]
    print([list(i) for i in zip(*matrix)])


# matrixTranspose()


# 8

# n, m = [int(i) for i in input().split()]
# a = [[int(j) for j in input().split()] for _ in range(n)]
# m, k = [int(i) for i in input().split()]
# b = [[int(j) for j in input().split()] for _ in range(m)]
#
# c = [[0] * k for i in range(n)]
#
# for i in range(n):
#     for j in range(k):
#         el = 0
#         for r in range(m):
#             el += a[i][r] * b[r][j]
#         c[i][j] = el
#
# for row in c:
#     print(*row)


# 9
def filling_with_spiral(n):
    m = n
    mat = [[0] * int(m) for i in range(n)]

    c = 1
    a, b = 0, 0
    rows = n - 1
    cols = m - 1

    while a <= cols and b <= rows:
        for i in range(a, cols + 1):
            mat[a][i] = c
            c += 1
        b += 1
        for i in range(b, rows + 1):
            mat[i][cols] = c
            c += 1
        cols -= 1
        if b <= rows:
            for i in range(cols, a - 1, -1):
                mat[rows][i] = c
                c += 1
            rows -= 1
        if a <= cols:
            for i in range(rows, b - 1, -1):
                mat[i][a] = c
                c += 1
            a += 1

    for s in mat:
        print(*s)


filling_with_spiral(4)
