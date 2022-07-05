import math


class Circle:

    def __init__(self, coord=(), radius=1):
        self.cord = coord
        self.radius = radius

    def bigger(self, k):
        self.radius *= k

    def square(self):
        return math.pi * self.radius ** 2

    def perimetr(self):
        return 2 * math.pi * self.radius

    def intersection(self, circle):
        if self.cord == circle.cord and self.radius == circle.radius:
            return True
        else:
            cen_dist = math.sqrt(
                (self.cord[0] - circle.cord[0]) ** 2 +
                (self.cord[1] - circle.cord[1]) ** 2
            )
        if not cen_dist:
            return False if self.radius != circle.radius else True
        else:
            return False if cen_dist > self.radius + circle.radius else True


circle_1 = Circle((3, 4))
circle_2 = Circle((2, 3))

print(circle_1.square())
print(circle_2.perimetr())
circle_1.bigger(3)
print(circle_1.square())
print(circle_1.intersection(circle_2))
