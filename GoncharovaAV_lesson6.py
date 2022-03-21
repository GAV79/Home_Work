# задача 1
from time import sleep


class TrafficLight:
    def __init__(self, red_time, yellow_time, green_time):
        self.__color = {'красный': red_time, 'желтый': yellow_time, 'зеленый': green_time}

    def running(self, light_cycle):
        count = 0
        while count < light_cycle:
            for el in self.__color:
                count += 1
                for i in range(0, self.__color[el] + 1):
                    print(f'горит', el, i, end='')
                    sleep(1)
                    print('\r', end='')
        print('Светофор завершил работу. Обратитесь в службу поддержки светофоров.')


go = TrafficLight(7, 2, 5)
go.running(9)

# задача 2
class Road:
    def __init__(self, length, width):
        self.mass_asf_kg = 25
        self.tol_pol_metr = 0.05
        self._l_metr = length
        self._w_metr = width

    def result(self):
        res = self.mass_asf_kg * self.tol_pol_metr * self._l_metr * self._w_metr
        print(f'Масса асфальта = {res/1000} тонн')


a = Road(5000, 20)
a.result()

# задача 3
err = "Введены некорректные данные"
try:

    class Worker:
        def __init__(self, name, surname, position, wage, bonus):
            self.n = name
            self.s = surname
            self.p = position
            self._income = {"wage": float(wage), "bonus": float(bonus)}


    class Position(Worker):
        v = input("Введите должность: ")

        def pos(self):
            if self.p == Position.v:
                get_full_name = self.n.title() + ' ' + self.s.title()
                get_total_income = self._income.get('wage') + self._income.get('bonus')
                print(f'{self.p.title()} {get_full_name} имеет доход с учётом премии: {get_total_income} рублей.')


    a1 = Position('Василий', 'Иванов', 'менеджер', 50000, 300)
    a1.pos()

    a2 = Position('екатерина', 'сидорова', 'секретарь', 35000, 5000)
    a2.pos()

    a3 = Position("сергей", 'смирнов', 'водитель', 15000, 300)
    a3.pos()

    a4 = Position('Игорь', 'петров', 'водитель', 19000, 1500)
    a4.pos()

    a5 = Position('Елена', 'Красавина', 'менеджер', 43500, 2500)
    a5.pos()

except (ValueError, TypeError):
    print(err)

# задача 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.sp = speed
        self.c = color
        self.n = name
        self.police = is_police

    def go(self):
        if self.police is False:
            print(f'{self.n}, цвет {self.c}, едет со скоростью {self.sp} км/час.')
        else:
            print(f'Полицейская машина, {self.n}, цвет {self.c}, едет со скоростью {self.sp} км/час.')

    def stop(self):
        if self.police is False:
            print(f'{self.n}, цвет {self.c}, остановилась.')
        else:
            print(f'Полицейская машина, {self.n}, цвет {self.c}, остановилась.')

    def turn(self):
        if self.police is False:
            print(f'{self.n}, цвет {self.c}, повернула направо.')
        else:
            print(f'Полицейская машина, {self.n}, цвет {self.c}, повернула направо.')

    def show_speed(self):
        if self.police is False:
            print(f'Текущая скорость {self.n}, цвет {self.c}, составляет {self.sp} км/час.')
        else:
            print(f'Текущая скорость полицейской машины, {self.n}, цвет {self.c}, составляет {self.sp} км/час.')


class TownCar(Car):
    def show_speed(self):
        if self.sp > 60:
            print(f'{self.n}, цвет {self.c}, превысила допустимую скорость.')
        else:
            print(f'Текущая скорость {self.n}, цвет {self.c}, составляет {self.sp} км/час.')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.sp > 40:
            print(f'{self.n}, цвет {self.c}, превысила допустимую скорость.')
        else:
            print(f'Текущая скорость {self.n}, цвет {self.c}, составляет {self.sp} км/час.')


class PoliceCar(Car):
    pass


towncar_1 = TownCar(50, 'green', 'Lada', False)
towncar_1.go()
towncar_1.show_speed()
towncar_1.stop()

towncar_2 = TownCar(100, 'red', 'Oka', False)
towncar_2.go()
towncar_2.show_speed()
towncar_2.turn()

sportcar_1 = SportCar(150, 'blue', 'Bolid', False)
sportcar_1.show_speed()

workcar_1 = WorkCar(50, 'black', 'Tarantul', False)
workcar_1.go()
workcar_1.show_speed()

policecar_1 = PoliceCar(90, 'white', 'Nissan', True)
policecar_1.show_speed()
policecar_1.turn()
policecar_1.stop()

# задача 5
class Stationery:
    def __init__(self, title):
        self.t = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.t.title()} рисует круг.')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.t.title()} рисует квадрат.')


class Handle(Stationery):
    def draw(self):
        print(f'{self.t.title()} рисует треугольник.')


stationery1 = Stationery('канцелярская принадлежность')
stationery1.draw()

pen1 = Pen('ручка')
pen1.draw()

pencil1 = Pencil('карандаш')
pencil1.draw()


handle1 = Handle('маркер')
handle1.draw()
