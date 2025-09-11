from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.fc = FigureColor()
        self.fc.colorproperty = color

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return f'{Rectangle.get_figure_type()} {self.fc.colorproperty} цвета шириной {self.width} и высотой {self.height} площадью {self.square()}.'
