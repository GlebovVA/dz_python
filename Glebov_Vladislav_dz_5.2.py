n = int(input('Введите верхнюю границу диапозона: '))
while n <= 1:
    n = int(input('Ошибка, повторите ввод: '))
my_list = [i for i in range(1, n + 1, 2)]
print(f'Нечетные числа от 1 до {n}:')
print(*my_list)
