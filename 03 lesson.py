# 1

def amount_symbol(text, symbol):
    text_list = list(text.lower())
    return text_list.count(symbol.lower())


# print(amount_symbol('HeLlllO', 'h'))

# 2

def amount_vowels(text):
    text_list = list(text.lower())
    vowels_letter = 'ауоыэеёиюя'
    total = 0
    for symbol in text_list:
        if symbol in vowels_letter:
            total += 1
    return total


# print(amount_vowels('Пример простого текста'))

# 3

def parentheses(text):
    text_list = list(text)
    total = 0
    for symbol in text_list:
        if symbol == '(':
            total += 1
        if symbol == ')':
            total -= 1
        if total < 0:
            return 'НЕТ'
    if total == 0:
        return 'OK'
    else:
        return 'НЕТ'


# print(parentheses('(a+b)*(c-)'))

# 4

def check_palindrome(text):
    text_replace = text.lower().replace(' ', '')
    if text_replace == text_replace[::-1]:
        return 'Да'
    else:
        return 'Нет'


# print(check_palindrome('А роза упала на лапу Азора'))

# 5

def strip_method(text, crop):
    len_crop = len(crop)
    while text[0: len_crop] == crop or text[len(text) - len_crop::] == crop:
        if text[0: len_crop] == crop:
            text = text[len_crop::]
        if text[len(text) - len_crop::] == crop:
            text = text[0:len(text) - len_crop]
    return text


# print(strip_method('11115 апреля1111', '1'))

# 6

def find_method(text, sub, start_position):
    len_sub = len(sub)
    for i in range(start_position, len(text)):
        if text[i:i + len_sub] == sub:
            return i
    return -1


# print(find_method('питон', '!', 2))

def longest_word(text):
    total = 0
    word = []
    max_word = []
    for symbol in text:
        if symbol != ' ':
            total += 1
            word.append(symbol)

        else:
            if len(word) > len(max_word):
                max_word = word

            total = 0
            word = []
    return ''.join(max_word)


print(longest_word('В тексте найти и напечатать самое длинное слово'))
