from random import choice


def get_jokes(dictionary, n):
    for i in range(n):
        jokes_list = []
        for key in dictionary.keys():
            jokes_list.append(choice(dictionary[key]))
        print(jokes_list)


jokes_dict = {'nouns': ["автомобиль", "лес", "огонь", "город", "дом"],
              'adverbs': ["сегодня", "вчера", "завтра", "позавчера", "ночью"],
              'adjectives': ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]}
n_jokes = int(input('Количество шуток: '))
while n_jokes <= 0:
    n_jokes = int(input('Ошибка, повторите ввод: '))
get_jokes(jokes_dict, n_jokes)
