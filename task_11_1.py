# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
# умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные.
    def __init__(self, name, model, year, speed):
        self.name = name
        self.model = model
        self.year = year
        self.speed = speed

    def moving(self, *args):
        if args == ('+'):
            self.speed += 5
        if args == ('-'):
            self.speed -= 5
        elif args == ('stop'):
            self.speed = 0

bmw = Car('BMW', 'e35', 1997, 0)

print(Car.moving())

class Car:
