from math import sqrt


def equation(a, b, c):
    if a == 0 and b != 0:
        x1 = 0
        x2 = c / b
        return x1, x2
    if b == 0 and ((a > 0 and c < 0) or (a < 0 and c > 0)):
        x2 = 0
        x1 = sqrt(-c / a)
        return x1, x2
    if c == 0 and a != 0:
        x1 = 0
        x2 = -b / a
        return x1, x2

    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = x2 = -b / (2 * a)
        return x1, x2
    if d > 0:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        return x1, x2

    else:
        return 'Нет вещественных корней'


print(equation(451, 45, 14))
