# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
#  area, height,

from math import sqrt


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)


class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = a.distance(b)
        self.bc = b.distance(c)
        self.ca = c.distance(a)

    def perimeter(self):
        return self.ab + self.bc + self.ca

    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self.ab) * (p - self.bc) * (p - self.ca))

    def height(self):
        return 2 * self.area() / self.ca


a = Point(0, 0)
b = Point(5, 0)
c = Point(5, 3)
t = Triangle(a, b, c)
print("Perimeter: {}, Area: {}, Height: {}.".format(t.perimeter(), t.area(), t.height()))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezoid(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.ab = a.distance(b)
        self.bc = b.distance(c)
        self.cd = c.distance(d)
        self.da = d.distance(a)

    def correct(self):
        return a.distance(c) == b.distance(d)

    def AB(self):
        return self.ab

    def BC(self):
        return self.bc

    def CD(self):
        return self.cd

    def DA(self):
        return self.da

    def perimeter(self):
        return self.ab + self.bc + self.cd + self.da

    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self.ab) * (p - self.bc) * (p - self.cd) * (p - self.da))


a = Point(0, 0)
b = Point(3, 5)
c = Point(8, 5)
d = Point(11, 0)
t = Trapezoid(a, b, c, d)
if t.correct():
    print("AB = {}, BC = {}, CD = {}, DA = {}, Perimeter: {}, Area: {}.".format(
        t.AB(), t.BC(), t.CD(), t.DA(), t.perimeter(), t.area()))
else:
    print("Incorrect trapezoid!")
