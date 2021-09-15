inf_weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_inf = []
for i in inf_weather:
    if i.isdigit():
        new_inf.append(f'"{int(i):02}"')
    elif i[0] == '+' or i[0] == '-':
        new_inf.append(f'"{i[0]}{int(i[1:]):02}"')
    else:
        new_inf.append(i)
print(' '.join(new_inf))
