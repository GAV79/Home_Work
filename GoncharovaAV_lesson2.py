# задача 1
# так как в задании к первому уроку не использовала форматирование через f-строки,
# то потренировалась в этом уроке, ответ к задаче: значение элемента; его индекс; тип.
coagulogram = ['АЧТВ', 80, 'МНО', 1.89, 'фибриноген', 4.0, 'Norma?', False]
for i in coagulogram:
    print(f'{coagulogram.index(i)+1}й элемент списка: {i}; индекс = {coagulogram.index(i)}; {type(i)}')

# задача 2
a = list(input('Введите элементы для списка: '))  # создаю список
b = len(a)  # количество элементов в списке
d = a[-1]  # сохраняю последний элемент в переменную
if b % 2 != 0:  # количество элементов нечетное
    a.pop(-1)  # удаляю последний элемент из списка
for i in a[::2]:  # для каждого элемента из списка с шагом 2
    k = a.index(i)  # k - индекс i-го элемента (является числом)
    a[k], a[k + 1] = a[k + 1], a[k]  # перестановка соседних элементов
if b % 2 != 0:
    a.append(d)  # добавляю последний элемент в список
print(a)

# задача 3 вариант через list
a = int(input('Введите номер месяца (от 1 до 12): '))
c = ['зима', 'весна', 'лето', 'осень']
if a == 1 or a == 2 or a == 12:
    print(c[0])
elif a == 3 or a == 4 or a == 5:
    print(c[1])
elif a == 6 or a == 7 or a == 8:
    print(c[2])
elif a == 9 or a == 10 or a == 11:
    print(c[3])
else:
    print("Номер месяца введен некорректно!")

# задача 3 вариант через dict
a = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}  # создаю словарь
err = 'Номер месяца введен некорректно!'
try:
    b = int(input('Введите номер месяца (от 1 до 12): '))
    if 0 < b <= 12:  # цикл для обработки ошибки ввода пользователем
        for i in a:  # поиск значений по элементам словаря
            if b in a[i]:
                print(f'Время года: {i}')
    else:
        print(err)
except ValueError as d:
    print(err)

# задача 4
a = input('Введите несколько слов, разделённых пробелами: ').split(' ')
print(a)
for i, y in enumerate(a, 1):
    k = a.index(y)
    a[k] = str(a[k])
    b = len(a[k])
    if b > 10:
        print(i, y[0:10])
    else:
        print(i, y)

# задача 5
a = [11, 5, 2, 2, 1]
err = "Введено некорректное значение"
try:
    b = int(input('Ведите новый элемент рейтинга (натуральное число): '))
    if b <= 0:
        print(err)
    else:
        for i in a:
            k = a.index(i)
            if b > i:
                a.insert(k, b)
                break
            if b == i:
                a.insert(k+1, b)
                break
        print(a)
except ValueError as d:
    print(err)

# задача 6
y = []
z = {}
was = []
cost = []
wieviel = []
wie = []
err = "Введено некорректное значение"
for i in range(1, 3):
    try:
        a = input('Ведите название товара: ')
        b = float(input(f'Цена товара {a}: '))
        if b < 0:
            print(err)
            exit()
        c = int(input(f'Количество в наличие товара {a}: '))
        if c < 0:
            print(err)
            exit()
        d = input(f'Единицы измерения товара {a}: ')
        x = (i, {'название': a, 'цена': b, 'количество': c, 'ед': d})
        y.append(x)
        was.append(a)
        cost.append(b)
        wieviel.append(c)
        wie.append(d)
        z = {'название': was, 'цена': cost, 'количество': wieviel, 'ед': wie}
    except ValueError as d:
        print(err)
print(y)
print(z)