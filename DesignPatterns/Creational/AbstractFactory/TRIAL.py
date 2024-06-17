from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Circle")


class Square(Shape):
    def draw(self):
        print("Square")


class Rectangle(Shape):
    def draw(self):
        print("Rectangle")


class Color(ABC):
    @abstractmethod
    def fill(self):
        pass


class Red(Color):
    def fill(self):
        print("Red")


class Green(Color):
    def fill(self):
        print("Green")


class Blue(Color):
    def fill(self):
        print("Blue")


class ShapeFactory:

    def get_shape(self):
        return Shape


class AbstractFactory:

    def get_shape(self):
        return Shape

    def get_color(self):
        return Color