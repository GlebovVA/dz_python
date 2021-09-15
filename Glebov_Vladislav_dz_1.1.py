s = 0
m = 0
h = 0
d = 0
duration = int(input('Введите продолжительность времени в секундах: '))
while duration <= 0:
    duration = int(input('Ошибка, повторите ввод: '))
s = duration
if s < 60:
    print(s, 'сек')
elif 60 <= s < 3600:
    m = s // 60
    s = s % 60
    print(m, 'мин', s, 'сек')
elif 3600 <= s < 86400:
    h = s // 3600
    m = (s - h * 3600) // 60
    s = s % 60
    print(h, 'час', m, 'мин', s, 'сек')
else:
    d = s // 86400
    h = (s - d * 86400) // 3600
    m = (s - d * 86400 - h * 3600) // 60
    s = s % 60
    print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
