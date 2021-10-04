from sys import argv

with open('bl.txt', 'a', encoding='utf-8') as wr:
    with open('bl.txt', 'r', encoding='utf-8') as rd:

        # Вывод значений на экран
        if len(argv) == 1:
            print('Журнал о суммах продаж:')
            print(rd.read())

        if not (',' in argv[1] or '.' in argv[1]):

            if len(argv) > 1 and (i for i in argv[1:] if i.isdigit()) and len(argv) == 3:
                st = int(argv[1])
                fn = int(argv[2])
                if fn <= st:
                    print('Ошибка, повторите ввод диапозона значений')
                else:
                    print(f'Записи о продажах с {st} до {fn}:')
                    print(*(val for k, val in enumerate(rd) if st - 2 < k < fn), sep='')

            if len(argv) > 1 and (i for i in argv[1:] if i.isdigit()) and len(argv) == 2:
                print(f'Записи о продажах с {int(argv[1])} до конца журнала:')
                print(*(val for k, val in enumerate(rd) if int(argv[1]) - 1 <= k), sep='')

        # Добавление записей в журнал
        if len(argv) > 1 and (',' in argv[1] or '.' in argv[1]):
            val = float(argv[1].replace(',', '.'))
            if val > 9999999.99:
                print('Ошибка, число превышает допустимое значение')
            else:
                print('{0:9.2f}'.format(val))
                print('{0:9.2f}'.format(val), file=wr, sep='')
