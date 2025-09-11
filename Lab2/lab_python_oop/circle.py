from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):
    """
    Класс «Круг» наследуется от класса «Геометрическая фигура».
    """
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, r, color):
        self.r = r
        self.fc = FigureColor()
        self.fc.colorproperty = color

    def square(self):
        return math.pi * self.r**2

    def __repr__(self):
        return f'{Circle.get_figure_type()} {self.fc.colorproperty} цвета радиусом {self.r} площадью {self.square()}.'
