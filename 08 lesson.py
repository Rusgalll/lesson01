# 1

def even_numbers():
    list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]
    return all(list_numbers[i] % 2 == 0 for i in range(0, len(list_numbers), 2))


# print(even_numbers())

# 2

def vowel_letters(text):
    vowel = 'аиеёоуыэюя'
    return all(i in vowel for i in text.lower()[0::2])


# print(vowel_letters('апааа'))

# 3

def consonant_letters(text):
    vowel = 'аиеёоуыэюя'
    return any(i not in vowel for i in text.lower()[1::2])


# print(consonant_letters('ббаа'))

# 4

def list_length_n():
    list_numbers = [1, 2, 3, 4, 5]
    length_list_numbers = len(list_numbers)
    return all(i in list_numbers for i in range(1, length_list_numbers + 1))


# print(list_length_n())

# 5

def check_prime():
    list_numbers = [2, 3, 5, 7, 11, 13, 17]
    result = [i for i in range(2, max(list_numbers) + 1) if not [n for n in range(2, i) if not i % n]]
    return all(i in result for i in list_numbers)


print(check_prime())
