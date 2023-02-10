"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    is_police = "нет"

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print("машина поехала ")

    def stop(self):
        print("машина остановилась ")

    def turn(self, direction):
        print("машина повернула ", direction)

    def show_speed(self):
        print(f'текущая скорость = {self.speed}')

class TownCar(Car):
    def show_speed(self):
        print(f'текущая скорость = {self.speed}')
        if self.speed > 60:
            print("СКОРОСТЬ ПРЕВЫШЕНА")



class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'текущая скорость = {self.speed}')
        if self.speed > 40:
            print("СКОРОСТЬ ПРЕВЫШЕНА")


class PoliceCar(Car):
    is_police = "да"


car_1 = TownCar(35, 'зеленый ', 'лада')

print(f'МАШИНА-1  скорость: {car_1.speed}, цвет: {car_1.color}, название: {car_1.name}, полиция: {car_1.is_police}')
car_1.go()
car_1.show_speed()
car_1.turn('налево')
car_1.stop()

car_2 = WorkCar(50, 'желтый ', 'газель')
print(f'МАШИНА-2  скорость: {car_2.speed}, цвет: {car_2.color}, название: {car_2.name}, полиция: {car_2.is_police}')
car_2.go()
car_2.show_speed()
car_2.turn('направо')
car_2.stop()


car_3 = PoliceCar(100, 'белый', 'шкода')
print(f'МАШИНА-3  скорость: {car_3.speed}, цвет: {car_3.color}, название: {car_3.name}, полиция: {car_3.is_police}')
car_3.go()
car_3.show_speed()
car_3.stop()