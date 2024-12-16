class Point:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        coord = (self.x, self.y)
        return coord

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __eq__(self, other):
        return (self.name, self.x, self.y) == (other.name, other.x, other.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.name, self.x, self.y) < (other.name, other.x, other.y)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)


class ColoredPoint(Point):
    def __init__(self, name: str, x: int, y: int, color=(0, 0, 0)):
        super().__init__(name, x, y)
        self.color = color

    def get_color(self):
        return self.color

    def __repr__(self):
        return f"ColoredPoint('{self.name}', {self.x}, {self.y}, {self.color})"

    def __invert__(self):
        inverted_point = super().__invert__()
        inverted_color = tuple(255 - c for c in self.color)
        return ColoredPoint(inverted_point.name, inverted_point.x, inverted_point.y, inverted_color)

