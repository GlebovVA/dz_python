prices = [10.14, 37, 75.97, 11.83, 84, 52.71, 23.05, 36.03, 91.04, 22.22, 55.03, 65.88, 99.01, 81.44, 58.14]
print('Пункт A')
for i in prices:
    print('{}руб {:02.0f}коп,'.format(int(i), (100 * (i % 1))), end=' ')
print('/n')

print('Пункт B')
before = id(prices)
prices = sorted(prices, reverse=False)
after = id(prices)
for i in prices:
    print('{}руб {:02.0f}коп,'.format(int(i), (100 * (i % 1))), end=' ')
print('/n')
if before == after:
    print('id до и после сортировки равны, следовательно объект списка после сортировки остался то же')
else:
    print('id до и после сортировки не равны, следовательно объект списка после сортировки изменился')
print('/n')

print('Пункт C')
prices = sorted(prices, reverse=True)
for i in prices:
    print('{}руб {:02.0f}коп,'.format(int(i), (100 * (i % 1))), end=' ')
print('/n')

print('Пункт D')
prices = sorted(prices, reverse=True)
for i in range(5):
    print('{}руб {:02.0f}коп,'.format(int(prices[i]), (100 * (prices[i] % 1))), end=' ')
