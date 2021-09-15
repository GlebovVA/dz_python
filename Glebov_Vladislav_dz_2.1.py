my_list = ['15 * 3', '15 / 3', '15 // 2', '15 ** 2']
for vr in my_list:
    rez = eval(vr)
    print(f'{vr} = {rez}, тип результата выражения {type(rez)}')
