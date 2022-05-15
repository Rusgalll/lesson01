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


# print(counter_numbers(4))

# 2 a)

def pangram_check(text):
    enalphabet = list('abcdefghijklmnopqrstuvwxyz')
    for symbol in enalphabet:
        if symbol not in text.lower():
            return 'Нет'
    return 'Да'


# print(pangram_check('The quick brown fox jumps over the lazy dog'))

# 2 b)

def pangram_check_without_repetition(text):
    enalphabet = list('abcdefghijklmnopqrstuvwxyz')
    symbol_were = []
    for symbol in enalphabet:
        if symbol not in text.lower() or symbol in symbol_were:
            return 'Нет'
        symbol_were.append(symbol)
    if len(symbol_were) == 26:
        return 'Да'
    else:
        return 'Нет'


# print(pangram_check_without_repetition('The quick brown fox jumps over the lazy dog'))

# 3

def counter_number_symbols(n):
    number_list = []
    check_number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(1, n + 1):
        number_list.append(str(i))
    number_list = ''.join(number_list)
    for number in check_number_list:
        counter = number_list.count(number)
        print(f'{number} - {counter}')


counter_number_symbols(11)
