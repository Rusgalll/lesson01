# 5

def counter_numbers(n):
    list_number = []
    for _ in range(n):
        numbers = int(input())
        list_number.append(numbers)
    symbol_were = []

    for number in list_number:
        counter = list_number.count(number)
        if counter > 1 or number > n:
            return 'НЕТ'
        else:
            symbol_were.append(number)
    if len(symbol_were) == n:
        return 'ДА'
    else:
        return 'НЕТ'


print(counter_numbers(4))
