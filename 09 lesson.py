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

# 2

