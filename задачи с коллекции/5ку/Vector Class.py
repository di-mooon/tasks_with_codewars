from math import sqrt


class Vector:
    def __init__(self, *args):
        if len(args) == 1:
            args = (element for item in args for element in item)
        self.x, self.y, self.z = args

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

    def cross(self, other):
        x = self.y * other.z - other.y * self.z
        y = self.x * other.z - other.x * self.z
        z = self.x * other.y - self.y * other.x
        return Vector(x, -y, z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def to_tuple(self):
        return self.x, self.y, self.z

    @property
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


