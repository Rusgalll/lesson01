# 1

def min_abs():
    list_numbers = [5, 10, 100, -100, 56, -1]
    return min(list_numbers, key=abs)


# print(min_abs())


# 2

def sorted_words(text):
    return sorted(text.split(), key=len)


print(sorted_words('сегодня 16 мая'))
