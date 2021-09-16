def odd_to_n(nx):
    for i in range(1, nx + 1, 2):
        yield i


n = int(input('Введите верхнюю границу диапозона: '))
while n <= 1:
    n = int(input('Ошибка, повторите ввод: '))
print(f'Нечетные числа от 1 до {n}: ')
for i in odd_to_n(n):
    print(i, end=' ')
