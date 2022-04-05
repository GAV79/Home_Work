# задача 1
class Date:

    def __init__(self, number, month, year):
        self.n = number
        self.m = month
        self.y = year
        Date.exam(self)

    def __str__(self):
        return f'Введено:\nчисло: {self.n}\nмесяц: {self.m}\nгод: {self.y}'

    @classmethod
    def transf(cls, date):
        err = "ошибка ввода"
        try:
            trf_date = date.split('-')
            n = int(trf_date[0])
            m = int(trf_date[1])
            y = int(trf_date[2])
            return Date(n, m, y)
        except ValueError:
            print(err)

    @staticmethod
    def exam(obj):
        if (obj.m in range(1, 9, 2) or obj.m in range(8, 13, 2)) and obj.n in range(1, 32):
            print('Дата ведена корректно')
        elif (obj.m in range(4, 7, 2)) or (obj.m in range(9, 12, 2)) and obj.n in range(1, 31):
            print('Дата введена корректно')
        elif obj.m == 2 and obj.n in range(1, 29):
            print('Дата введена корректно')
        elif obj.m == 2 and obj.n == 29 and (obj.y % 4 == 0 and obj.y % 400 != 0):
            print('Дата введена корректно')
        else:
            print("Дата введена НЕКОРРЕКТНО!")


li = input('внесите дату в формате день-месяц-год: ')
d1 = Date.transf(li)
print(d1)


# Задача 2

class Nul(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input('Числитель: '))
    b = int(input('Знаменатель: '))
    if b == 0:
        raise Nul('делить на ноль нельзя')
except ValueError:
    print('введено не число')
except Nul as err:
    print(err)
else:
    print(f'Результат: {a / b}')


# Задача 3

class Number(Exception):
    def __init__(self, txt):
        self.txt = txt


b = []
while True:
    try:
        a = input('введите элемент списка: ')
        if a == 'end':
            break
        for el in a:
            if el not in "0123456789":
                raise Number('это не число')
        b.append(int(a))
    except Number as num:
        print(num)
        continue
print(b)

# Задача 4, 5, 6
""" Проект "Лаборатория"
                класс Labor: статистический метод, выводящий результирующую информацию по исследованиям
                         /                                            \
              класс Person(Labor)                          класс Biomaterial(Labor)
            параметры: имя и фамилия                          метод "make_dict":
           переопределен метод __str__                 на основе списка создается словарь, где ключ - это
          /                         \                  код биоматериала, который должен ввести пользователь
         /                           \
класс Doctor(Person)                   класс Patient(Person)
имя и фамилия наследуются              дополнительные параметры: number_id и biomaterial
метод "make": врач                     метод "to_give": сдает биоматериал
выполнил исследование                  вид биоматериала выбирает пользователь из словаря
переопределен метод __str__            переопределен метод __str__

класс Date: ввод даты, до тех пор пока не будет введена корректная
"""


class Date:
    running = True

    def __init__(self, number, month, year):
        self.n = number
        self.m = month
        self.y = year
        Date.exam(self)

    @classmethod
    def transf(cls, date):
        err = "ошибка ввода"
        try:
            trf_date = date.split('-')
            n = int(trf_date[0])
            m = int(trf_date[1])
            y = int(trf_date[2])
            return Date(n, m, y)
        except ValueError:
            print(err)

    @staticmethod
    def exam(obj):
        if (((obj.m in range(1, 9, 2)) or (obj.m in range(8, 13, 2))) and obj.n in range(1, 32)) and \
                (2022 <= obj.y < 2050):
            Date.running = False
            return dat
        elif (obj.m in range(4, 7, 2)) or (obj.m in range(9, 12, 2)) and obj.n in range(1, 31) and \
                (2022 <= obj.y < 2050):
            Date.running = False
            return dat
        elif obj.m == 2 and (obj.n in range(1, 29)) and (2022 <= obj.y < 2050):
            Date.running = False
            return dat
        elif obj.m == 2 and obj.n == 29 and obj.y in range(2024, 2050, 4) and (2022 <= obj.y < 2050):
            Date.running = False
            return dat
        else:
            print("Дата введена НЕКОРРЕКТНО!")


while Date.running:
    dat = input('Введите дату в формате день-месяц-год: ')
    d = Date.transf(dat)
    a = dat


class Labor:

    @staticmethod
    def info_labor(obj1, obj2):
        print(f'Результат: {a} исследование биоматериала ({obj1.biomaterial[0]}) пациента ({obj1.name} '
              f'{obj1.surname},'
              f' id {obj1.number_id}) выполнено и валидировано врачом ({obj2.name} {obj2.surname}).')


class Person(Labor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Name: {self.name} Surname: {self.surname}'


class Patient(Person):
    def __init__(self, name, surname, number_id):
        super().__init__(name, surname)
        self.number_id = number_id
        self.biomaterial = []

    def to_give(self):
        running = True
        while running:
            try:
                kod_bio = input(f'Укажите код биоматериал {Biomaterial.biodict}: ')
                if int(kod_bio) in Biomaterial.biodict.keys():
                    biomaterial = Biomaterial.biodict.get(int(kod_bio))
                    self.biomaterial.append(biomaterial)
                    print(f'Пациент {self.name} {self.surname} (id {self.number_id}) сдал {self.biomaterial[0]}.')
                    running = False
                else:
                    print(f'биоматериал выбран некорректно')
            except ValueError:
                print('Введено не число')

    def __str__(self):
        return f'Пациент: {self.name} {self.surname} (id {self.number_id})'


class Doctor(Person):
    @staticmethod
    def make(obj):
        print(f'Врач {obj.name} {obj.surname} выполнил исследования.')

    def __str__(self):
        return f'{a} работает врач КДЛ: {self.name} {self.surname}'


class Biomaterial(Labor):
    biodict = {}

    def __init__(self, *biomaterials):
        self.biomaterials = list(biomaterials)
        Biomaterial.make_biodict(self)

    def make_biodict(self):
        for el in self.biomaterials:
            k = self.biomaterials.index(el)
            f = {k: el}
            Biomaterial.biodict.update(f)
        return Biomaterial.biodict

    def labor_list(self):
        return self.biomaterials


b = Biomaterial('кровь', 'моча', 'ликвор')
d1 = Doctor('Сергей', 'Смирнов')
print(d1)
print()
p1 = Patient('Иван', 'Петров', 436453645)
print(p1)
p1.to_give()
print()
p2 = Patient('Евгений', 'Кузнецов', 6589845654)
print(p2)
p2.to_give()
print()
Doctor.make(d1)
Labor.info_labor(p1, d1)
Labor.info_labor(p2, d1)


# задача 7

class MyComplex:
    def __init__(self, a, b, name):
        self.a = a
        self.b = b
        self.n = name

    def __str__(self):
        return f'комплексное число {self.n}: {self.a} + {self.b}i'

    def __add__(self, other):
        return f'{self.n} + {other.n} = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{self.n} * {other.n} = {(self.a * other.a) + (self.b * other.b * (-1))} + ' \
               f'{(self.a * other.b) + (self.b * other.a)}i'


c1 = MyComplex(5, 4, 'c1')
print(c1)
c2 = MyComplex(-2, 3, 'c2')
print(c2)
print(c1 + c2)
print(c1 * c2)
