# 1

def positive_numbers():
    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 12, 12, 45, 65, 6554, 4]
    return all(i > 0 for i in list_numbers)


# print(positive_numbers())

# 2

def even_numbers():
    list_numbers = [1, 3, 3, 3, 5, 3, 7, 3, 3, 3, 45, 65, 6553, 3]
    return any(i % 2 == 0 for i in list_numbers)


# print(even_numbers())

# 3 не понял задание

# 4

def unique_numbers():
    list_numbers = [1, 3, 3, 3, 5, 3, 7, 3, 3, 3, 45, 65, 6553, 3]
    result = []
    arr = [result.append(i) for i in list_numbers if i not in result]

    return result


# print(unique_numbers())

# 5

def prime_numbers():
    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    result = [i for i in range(2, max(list_numbers) + 1) if not [n for n in range(2, i) if not i % n]]
    return result


print(prime_numbers())
