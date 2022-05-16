from random import randint


# 1 a)

def check_palindrome(text):
    text = text.replace(' ', '').lower()
    if text == text[::-1]:
        return 'Да'
    else:
        return 'Нет'


# print(check_palindrome('А роза упала на лапу Азора'))

# 1 b)

def check_palindrome_reverse(text):
    text = text.replace(' ', '').lower()
    if len(text) % 2 == 0:
        if text[0:int(len(text) / 2)] == text[-1:int(len(text) / 2) - 1:-1]:
            return 'Да'
        else:
            return 'Нет'
    else:
        if text[0:int(len(text) / 2)] == text[-1:int(len(text) / 2):-1]:
            return 'Да'
        else:
            return 'Нет'


# print(check_palindrome_reverse('А роза упала на лапу Азора'))

# 2

def even_index(text):
    return text[0::2]


# print(even_index('0123456789'))


# 3 a)

def reverse_list(n):
    numbers_list = list(range(1, n + 1))
    result = []
    for i in range(len(numbers_list), 0, -1):
        result.append(i)

    return result


# print(reverse_list(8))

# 3 b)

def reverse_list_slice(n):
    numbers_list = list(range(1, n + 1))
    return numbers_list[::-1]


# print(reverse_list_slice(8))


# 4 a)

def reverse_elements(n, k1, k2):
    if k2 < k1:
        return 'k2 должен быть >= k1'
    numbers_list = list(range(1, n + 1))
    result = []
    j = 1
    for i in range(1, len(numbers_list) + 1):
        if i >= k1 and i <= k2:
            result.append(numbers_list[k2 - j])
            j += 1
        else:
            result.append(i)

    return result


# print(reverse_elements(8, 3, 5))


# 4 b)

def reverse_elements_slice(n, k1, k2):
    if k2 < k1:
        return 'k2 должен быть >= k1'
    numbers_list = list(range(1, n + 1))
    result = numbers_list[0:k1 - 1] + numbers_list[k2 - 1:k1 - 2:-1] + numbers_list[k2::]

    return result


# print(reverse_elements_slice(8, 3, 6))

# 5 a)

def reverse_half(n):
    if n % 2 != 0:
        return 'Допускается только четное n'
    numbers_list = list(range(1, n + 1))
    result = []
    j = 0
    for i in range(len(numbers_list) - 1, -1, -1):
        if i >= len(numbers_list) / 2:
            result.append(numbers_list[i])
        else:
            result.append(numbers_list[j])
            j += 1

    return result


# print(reverse_half(12))


# 5 b)

def reverse_half_slice(n):
    if n % 2 != 0:
        return 'Допускается только четное n'
    numbers_list = list(range(1, n + 1))
    result = numbers_list[-1:int(len(numbers_list) / 2) - 1:-1] + numbers_list[0:int(len(numbers_list) / 2)]

    return result


# print(reverse_half_slice(8))

# 6 a)

def shift_for(n):
    numbers_list = list(range(1, n + 1))
    result = []
    result.append(numbers_list[-1])
    for i in range(len(numbers_list) - 1):
        result.append(numbers_list[i])

    return result


# print(shift_for(4))


# 6 b)

def shift_list(n):
    numbers_list = list(range(1, n + 1))
    result = numbers_list[-1:] + numbers_list[:-1]
    return result


# print(shift_list(4))

# 7 как и 6 a), b) только вместо -1, введенное k, если k > размера списка , то k % len(number_list)

# 8 a)

def end_zero(n):
    list_numbers = [0] * n
    random_amount = randint(1, n)
    for i in range(random_amount):
        list_numbers[randint(0, len(list_numbers)) - 1] = randint(0, 9)

    j = 0

    for i in range(len(list_numbers)):
        list_numbers[j] = list_numbers[i]
        j += 1 if list_numbers[i] else 0

    list_numbers[j:] = [0] * (n - j)

    return list_numbers


# print(end_zero(4))


# 8 b)

def end_zero_list(n):
    list_numbers = [0] * n
    random_amount = randint(1, n)
    for i in range(random_amount):
        list_numbers[randint(0, len(list_numbers)) - 1] = randint(0, 9)

    list_without_0 = [x for x in list_numbers if x != 0]
    list_0 = [x for x in list_numbers if x == 0]

    lst_0s_at_end = list_without_0 + list_0

    return lst_0s_at_end


# print(end_zero_list(4))

# 9

def compression_list(n):
    # list_numbers = [0] * n
    # for i in range(len(list_numbers)):
    #     list_numbers[i] = randint(0, 9)
    list_numbers = [1, 3, 3, 3, 5, 6, 6, 6, 6, 7, 8]
    symbol_were = []
    len_list_numbers = len(list_numbers)

    for numbers in list_numbers:
        if numbers not in symbol_were:
            symbol_were.append(numbers)

    len_symbol_were = len(symbol_were)
    count_zero = len_list_numbers - len_symbol_were

    for i in range(count_zero):
        symbol_were.append(0)

    return symbol_were


print(compression_list(5))
