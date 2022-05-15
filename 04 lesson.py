from random import randint


# 1

def counter_number(number):
    list_numbers = [1, 2, 3, 4, 1]
    total = 0
    for i in list_numbers:
        if i == number:
            total += 1
    return total


# print(counter_number(1))

# 2

def common_number():
    list_numbers = [1, 2, 3, 4, 1]
    counter1 = 0
    result = 0
    for i in list_numbers:
        counter = list_numbers.count(i)
        if counter > counter1:
            counter1 = counter
            result = i
    return result


# print(common_number())

# 3

def common_symbol(text):
    counter1 = 0
    result = 0
    for i in text.lower():
        counter = text.count(i)
        if counter > counter1:
            counter1 = counter
            result = i
    return result


# print(common_symbol('hello'))

# 4 b)

def counter_numbers():
    list_numbers = []
    for i in range(10):
        list_numbers.append(randint(-1000, 1000))
    number_were = []
    for number in list_numbers:
        if number not in number_were:
            counter = list_numbers.count(number)
            print(f'{number} - {counter}')
            number_were.append(number)


# counter_numbers()

# 5 a)

def counter_symbols_enalphabet(text):
    enalphabet = list('abcdefghijklmnopqrstuvwxyz')
    symbol_were = []
    for symbol in text.lower():
        if symbol not in symbol_were and symbol in enalphabet:
            counter = text.count(symbol)
            print(f'{symbol} - {counter}')
            symbol_were.append(symbol)


# counter_symbols_enalphabet('hello')

# 5 b)

def counter_symbols_enalphabet_ord(text):
    symbol_were = []
    for symbol in text.lower():
        if ord(symbol) >= 97 and ord(symbol) <= 122 and symbol not in symbol_were:
            counter = text.count(symbol)
            print(f'{symbol} - {counter}')
            symbol_were.append(symbol)


# counter_symbols_enalphabet_ord('hello')

# 6

def counter_symbols_in_text(text):
    symbol_were = []
    for symbol in text.lower():
        if symbol not in symbol_were and symbol != ' ':
            counter = text.count(symbol)
            print(f'{symbol} - {counter}')
            symbol_were.append(symbol)


counter_symbols_in_text('hello ;')
