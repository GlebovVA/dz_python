my_list = []
all_summa = 0
n_sum = 0
print('Пункт A')
for i in range(1, 1001):
    if i % 2 != 0:
        my_list.append(i ** 3)
print('Список кубов нечетных чисел от 1 до 1000: ', my_list)
for n in my_list:
    el_list = n
    while n:
        remainder = n % 10
        n_sum += remainder
        n = n // 10
    if n_sum % 7 == 0:
        all_summa += el_list
    n_sum = 0
print('Сумма чисел списка, сумма цифр которых делится нацело на 7: ', all_summa)
print('/n')

print('Пункт B')
all_summa = 0
new_list = []
for i in range(len(my_list)):
    new_list.append(my_list[i] + 17)
print('Список кубов нечетных чисел от 1 до 1000, увеличенных на 17: ', new_list)
for n in new_list:
    el_list = n
    while n:
        remainder = n % 10
        n_sum += remainder
        n = n // 10
    if n_sum % 7 == 0:
        all_summa += el_list
    n_sum = 0
print('Сумма чисел списка(+17), сумма цифр которых делится нацело на 7: ', all_summa)
print('/n')

print('Пункт C')
all_summa = 0
for n in my_list:
    n = n + 17
    el_list = n
    while n:
        remainder = n % 10
        n_sum += remainder
        n = n // 10
    if n_sum % 7 == 0:
        all_summa += el_list
    n_sum = 0
print('Сумма чисел списка(+17), сумма цифр которых делится нацело на 7(без создания нового списка): ', all_summa)
