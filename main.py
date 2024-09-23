import math


class Figure:
    sides_count = 0
    def __init__(self, color = [], sides = [], filled = False):
        self. __sides = sides
        self. __color = color
        self.filled = filled
    def get_color(self):#Это определение метода get_color() в классе self. Метод возвращает цвет объекта.
        return self.__color
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b])# функция all() возвращает True, если все элементы итерируемого объекта равны True, и False в противном случае
    def __is_valid_sides(self, sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count
#Это функция на языке Python, которая проверяет правильность сторон многоугольника. Функция возвращает True, если все стороны являются целыми числами больше нуля и их количество равно количеству сторон многоугольника.
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return  sum(self. get_sides())
    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = list(sides)
class Circle(Figure):
    sides_count = 1
    def __init__ (self, color = [255], circumference = 0, filled = False):
        super().__init__(color=color, sides=[circumference], filled=filled)
        self. __radius = circumference / (2 * math.pi)#задаем радиус через формулу по длине окружности
    def get_radius(self):
        return self.__radius
    def get_square(self):
        return math.pi * (self.__radius ** 2)
class Triangle(Figure):
    sides_count = 3
    def __init__(self, color = [255, 255, 255], side1 = 0, side2 = 0, side3 = 0, filled = False ):
        super(). __init__(color=color, sides=[side1, side2, side3], filled=filled)
        self.__height = self.__calculator_height()
    def __calculator_height(self):
        s = sum(self.get_sides()) / 2
        area = math.sqrt(s * (self. get_sides()[0]) *(s - self. get_sides()[2]))
        height = 2 * area / self.get_sides()[0]
        return  height
    def get_height(self):
        return self.__height
    def get_square(self):
        s = sum(self. get_sides()) / 2
        return math.sqrt(s * (s - self. get_sides()[0]) * (s - self. get_sides()[1]) * (s - self. get_sides()[2]))
class Cube(Figure):
    sides_count = 12
    def __init__(self, color = [255, 255, 255], sides = 0, filled = False):
        super().__init__(color=color, sides=[sides] * self.sides_count, filled=False)
    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())






