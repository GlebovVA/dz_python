max_zn = int(input('Введите верхнюю границу диапозона (значение от 1 до 100): '))
while max_zn < 1 or max_zn > 100:
    max_zn = int(input('Ошибка, повторите ввод: '))
sr = 0
for i in range(1, max_zn + 1):
    sr = i % 10
    if sr == 1 and i != 11:
        print(i, 'процент')
    elif 5 <= sr <= 9 or sr == 0 or i == 12 or i == 13 or i == 14 or i == 11:
        print(i, 'процентов')
    else:
        print(i, 'процента')
