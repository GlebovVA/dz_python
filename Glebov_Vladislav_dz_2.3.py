inf_weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i, el in enumerate(inf_weather):
    if el.isdigit():
        inf_weather[i] = f'"{int(el):02}"'
    if el[0] == '+' or el[0] == '-':
        inf_weather[i] = f'"{el[0]}{int(el[1:]):02}"'
print(' '.join(inf_weather))
