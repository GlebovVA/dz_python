def num_translate(word):
    dictionary = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять',
                  'null': 'нолевой', 'first': 'первый', 'second': 'второй', 'third': 'третий', 'fourth': 'четвертый',
                  'fifth': 'пятый', 'sixth': 'шестой', 'seventh': 'седьмой', 'eighth': 'восьмой', 'ninth': 'девятый',
                  'tenth': 'десятый'}
    for key in dictionary.keys():
        if word == key:
            return dictionary[key]
    return None


an_word = input('Введите числительное от 0 до 10 на английском: ')
print(f'Перевод: {num_translate(an_word)}')
