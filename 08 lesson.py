# 1

def even_numbers():
    list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]
    return all(list_numbers[i] % 2 == 0 for i in range(0, len(list_numbers), 2))


print(even_numbers())
