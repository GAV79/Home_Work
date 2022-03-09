# задача 1 вариант 1
a = input('Введите фамилию: ')
b = input('Введите имя: ')
c = input('введите номер телефона: ')
with open(r'info.txt', 'w', encoding='utf-8') as f:
    vr = [a, b, c]
    for el in vr:
        el += '\n'
        f.write(f'{el}')

# задача 1 вариант 2
a = input('Введите элементы через пробел: ').split()
for i in a:
    k = a.index(i)
    i += "\n"
    a.insert(k, i)
    a.pop(k + 1)
with open(r'info.txt', 'w', encoding='utf-8') as f:
    f.writelines(a)

# задача 2
with open(r'count.txt', 'r', encoding='utf-8') as f:
    k = 0
    for i in f:
        k += 1
        word = i.split()
        x = len(word)
        print(f'Число слов {k} строки = {x}')
print(f'Число строк в файле = {k}')

# задача 3
err = 'оклад введен неверно'
try:
    with open(r'zp.txt', 'r', encoding='utf-8') as f:
        s = 0
        k = 0
        for i in f:
            a = i.split()
            b = float(a[1])
            s += b
            k += 1
            if b < 20000:
                print(i, end='')
    print(f'Средний доход {k} сотр. составляет {round(s / k, 2)} рублей')
except (ValueError, TypeError):
    print(err)

# задача 4
with open(r'eng_rus.txt', 'r', encoding='utf-8') as f:
    b = {"One": "Один", 'Two': "Два", "Three": "Три", "Four": "Четыре"}
    for el in f:
        a = el.split('-')  # в файле данные записаны без пробелов, т.е One-1, поэтому '-' как разделитель
        d = b.get(a[0])
        a.insert(0, d)
        a.pop(1)
        c = '-'.join(a)
        print(c, end="")
        with open(r'eng_rus_2.txt', 'a', encoding='utf-8') as f_2:
            f_2.write(c)

# задача 5
with open(r'numer.txt', 'w+', encoding='utf-8') as f:
    try:
        a = input('Введите набор чисел, разделенных пробелами: ')
        f.write(a)
        f.seek(0)
        b = f.read()
        b = b.split()
        k = 0
        for el in b:
            el = int(el)
            k += el
        print(k)
    except (ValueError, TypeError):
        print("Введено не число")

# Задача 6 вариант 1 (это решение "в лоб", когда дописала, поняла как упростить код(см. ниже))
with open(r'urok.txt', 'r', encoding='utf-8') as f:
    my_dic = {}
    for li in f:
        a = li.split()
        d = []
        for el in a:
            k = ''
            for i in el:
                if 48 <= ord(i) <= 57:
                    k += i
            d.append(k)
            s_1 = 0
            for y in d:
                if y == '':
                    x = d.index(y)
                    d.pop(x)
                else:
                    y = int(y)
                    s_1 += y
        dic = {a[0]: s_1}
        my_dic |= dic
    print(my_dic)

# задача 6 вариант 2
with open(r'urok.txt', 'r', encoding='utf-8') as f:
    my_dic = {}
    for el in f:
        a = el.split()
        c = [a[1], a[2], a[3]]
        for i in c:
            d = c.index(i)
            ff = [i[li] for li in range(0, len(i)) if 48 <= ord(i[li]) <= 57]
            ff_1 = ''.join(ff)
            c.insert(d, ff_1)
            c.pop(d + 1)
        up_c = [vr for vr in c if vr != '']
        new_c = map(int, up_c)
        su = sum(new_c)
        b = {a[0]: su}
        my_dic = my_dic | b
    print(my_dic)

# задача 6 вариант 1 upgrade
with open(r'urok.txt', 'r', encoding='utf-8') as f:
    my_dic = {}
    for li in f:
        a = li.split()
        d = []
        for el in a:
            ff = [el[i] for i in range(0, len(el)) if 48 <= ord(el[i]) <= 57]
            ff_1 = ''.join(ff)
            d.append(ff_1)
        up_d = [el for el in d if el != '']
        upp_d = map(int, up_d)
        new_d = sum(upp_d)
        dic = {a[0]: new_d}
        my_dic |= dic
    print(my_dic)

# задача 7
import json

with open(r'company.txt', 'r', encoding='utf-8') as f:
    mean_prib = 0
    d = []
    for li in f:
        a = li.split()
        prib = int(a[2]) - int(a[3])
        book = {a[0]: prib}
        d.append(book)
        if prib > 0:
            mean_prib += prib
            print(f'{a[0]}, прибыль: {prib}')
        else:
            print(f'{a[0]}, убытки: {prib}')
    print(f'Средняя прибыль: {mean_prib}')
    avv = {'average_profit': mean_prib}
    d.append(avv)
    print(d)

with open(r'company.json', 'w', encoding='utf-8') as write_f:
    json.dump(d, write_f)
