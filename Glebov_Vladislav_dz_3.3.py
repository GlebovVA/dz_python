def thesaurus(my_list):
    my_dict = {}
    for name in my_list:
        key = name[0]
        if key in my_dict:
            my_dict[key].append(name)
        else:
            my_dict.setdefault(key, [])
            my_dict[key].append(name)
    return my_dict


list_name = list(map(str, input('Введите имена сотредников через пробел: ').split()))
print(list_name)
dictionary = thesaurus(list_name)
print('Словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с '
      'соответствующей буквы')
print(dictionary)
