from itertools import islice

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Арсений', 'Николай', 'Григорий']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
inf_list = ((tutors[i], klasses[i]) if len(klasses) > i else (tutors[i], None) for i in range(len(tutors)))
print(*islice(inf_list, 11))
print(type(inf_list))
