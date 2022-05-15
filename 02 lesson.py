# 1

def min_max_average_value(n):
    if n <= 0:
        return 'Допускается ввод n > 0'
    list_number = []
    for _ in range(n):
        list_number.append(int(input()))

    min_number = min(list_number)
    max_number = max(list_number)
    average_number = sum(list_number) / len(list_number)
    return f'Минимальное значение {min_number}, максимальное значение {max_number}, средние значение {average_number}'


# print(min_max_average_value(2))

# 2
def positive_number(n):
    if n <= 0:
        return 'Допускается ввод n > 0'
    for _ in range(n):
        number = int(input())
        if number <= 0:
            return 'НЕТ'
    return 'ДА'


# print(positive_number(3))

# 3

def even_numbers(n):
    if n <= 0:
        return 'Допускается ввод n > 0'
    number_list = []
    for _ in range(n):
        number = int(input())
        if number % 2 == 0:
            number_list.append(str(number))
    if len(number_list) > 0:
        return ' '.join(number_list)
    else:
        return 'Четных чисел нет'


# print(even_numbers(3))

# 4

def not_monotone_number(n):
    if n <= 0:
        return 'Допускается ввод n > 0'
    list_number = []
    for _ in range(n):
        number = int(input())
        list_number.append(number)
    sorted_number = sorted(list_number)
    reverse_sorted_number = sorted(list_number, reverse=True)
    if list_number == sorted_number or list_number == reverse_sorted_number:
        return 'ДА'
    else:
        return 'НЕТ'


# print(not_monotone_number(5))

# 5

def arithmetical_progression(n):
    if n <= 0:
        return 'Допускается ввод n > 0'
    number1 = int(input())
    number2 = int(input())
    if number1 == number2:
        return 'НЕТ'
    difference = number2 - number1
    for _ in range(n - 2):
        number = int(input())
        if number == number2 + difference:
            number2 = number
        else:
            return 'НЕТ'
    return 'ДА'


# print(arithmetical_progression(4))

# 6

def increasing_chain(n):
    if n <= 0:
        return 'Допускается ввод n > 0'
    number1 = int(input())
    total = 1
    max_total = []
    for _ in range(n - 1):
        number = int(input())
        if number > number1:
            total += 1
        else:
            total = 0
        number1 = number
        max_total.append(total)
    return max(max_total)


# print(increasing_chain(3))

# 7

def largest_pair(n):
    if n <= 0:
        return 'Допускается ввод n > 0'
    number1 = int(input())
    max_pair = number1
    for _ in range(n - 1):
        number = int(input())
        if number1 + number > max_pair:
            max_pair = number1 + number
        number1 = number
    return max_pair


print(largest_pair(5))
