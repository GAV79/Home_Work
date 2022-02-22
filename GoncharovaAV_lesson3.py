# задача 1
"""Калькулятор для расчета ИМТ(индекса массы тела)"""
err = "Введено некорректное значение"
while True:  # если ошибка, то запрос на ввод цифр опять, пока не будет правильно введено
    try:  # обработка ошибок
        a = float(input('Введите вес в кг: '))
        if a < 40 or a > 150:  # ограничение для веса
            print(err)
        else:
            b = float(input('Введите рост в м: '))
            if 1 < b < 2.5:  # ограничение для роста
                def f1(weight, height):  # объявляю функцию с двумя аргументами
                    bmi = round(weight / pow(height, 2), 1)  # расчет индекса массы тела
                    print(f'Индекс массы тела равен {bmi} кг/м2')
                    exit()  # если расчет произведен, выход из кода


                f1(a, b)  # запуск функции со значениями аргументов от пользователя
            else:
                print(err)
    except (TypeError, ValueError, ZeroDivisionError) as d:
        print(err)

# задача 2
a = input('Введите имя: ')
b = input('Введите фамилию: ')
c = input('Введите год рождения: ')
d = input('Введите город проживания; ')
e = input("Введите email: ")
f = input("Введите телефон: ")


def info_book(name, surname, date, city, email, tel):
    print(f'Имя: {name}; Фамилия: {surname}; Год рождения: {date}; Город: {city}; email: {email}; телефон: {tel}')


info_book(name=a, surname=b, date=c, city=d, email=e, tel=f)

# задача 3
err = "некорректные данные"
try:
    a = float(input('1ое число: '))
    b = float(input('2ое число: '))
    c = float(input('3ое число: '))

    if a != b and a != c and b != c:
        def my_func(first, second, third):
            small = min(first, second, third)
            return first + second + third - small


        print(f'Сумма двух наибольших аргументов: {my_func(a, b, c)}')
    else:
        print(err)
except (TypeError, ValueError):
    print(err)

# задача 4 вариант 1
err = "некорректные данные"
try:
    x = int(input('Введите целое положительное число: '))
    y = int(input('Введите целое отрицательное число: '))
    if x > 0 > y:
        def my_func(var1, var2):
            return var1 ** var2


        print(my_func(x, y))
    else:
        print(err)
except (TypeError, ValueError):
    print(err)

# задача 4 вариант 2
err = "некорректные данные"
try:
    x = int(input('Введите целое положительное число: '))
    y = int(input('Введите целое отрицательное число: '))
    if x > 0 > y:
        def my_func(var1, var2):
            k = 1
            for i in range(abs(var2)):
                k = var1 * k
            return 1 / k


        print(my_func(x, y))
    else:
        print(err)
except (TypeError, ValueError):
    print(err)

# Задача 5
err = "некорректные данные"
res = 0
try:
    while True:
        def f1():
            b = input("Введите последовательность чисел через пробел: ").split()
            summ_1 = 0
            for i in b:
                if i == "stop":
                    return summ_1
                else:
                    i = int(i)
                    summ_1 += i
            return summ_1


        r = f1()
        res += r
        print(res)
except (ValueError, TypeError):
    print(err)

# задача 6, 7
err = "некорректные данные"


def int_func():
    b = input('слова через пробел: ').split()
    for i in b:
        if i.isalpha() is True:
            continue
        else:
            print(err)
            exit()
    c = " ".join(b)
    return c.title()


print(int_func())
