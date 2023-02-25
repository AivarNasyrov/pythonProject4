import emoji
print(emoji.emojize('Python is :thumbs_up:'))
Python is 👍
class Figure:
    unit = "mm"
    def __init__(self):
        passi
    def calculate_area(self):
        pass
    def info(self):
        pass


class Circle(Figure):
    pi= 'π'
    super.__init__(self, radius):
        self.__radius__ = radius

    def calculate_area(self):
        return self.__radius__**2 * 3.14

    def info(self):
        return f'Circle radius: {self.__radius} {Figure.unit}, ' \
               f'area: {self.calculate_area()}{Circle.pi} {Figures.unit}'


class RightTriangle(Figures):
    def __init(self, side_a, side_b):
        super(RightTriangle, self).init()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return round((self.__side_a * self.__side_b) / 2, 1)

    def info(self):
        return f'RightTriangle side a: {self.__side_a}{Figures.unit}, ' \
               f'side b: {self.__side_b}{Figures.unit}, ' \
               f'area: {self.calculate_area()}{Figures.unit}'


figure2_list = [Circle(5), Circle(4), RightTriangle(3, 5), RightTriangle(5, 9), RightTriangle(5, 7)]

for i in figure2_list:
    print(i.info())



