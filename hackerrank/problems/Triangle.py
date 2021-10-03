import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.sqrt(((self.__x-x)**2)+((self.__y-y)**2))

    def distance_from_point(self, point):
        return math.sqrt(((self.__x - point.__x)**2) + ((self.__y-point.__y)**2))


class Triangle:
    def __init__(self, v1, v2, v3):
        self.__v1 = v1
        self.__v2 = v2
        self.__v3 = v3

    def get_dis(self, v1, v2):
        point = Point(v1.getx(), v1.gety())
        dis = point.distance_from_point(v2)
        return dis

    def perimeter(self):
        side1 = self.get_dis(self.__v1, self.__v2)
        side2 = self.get_dis(self.__v1, self.__v3)
        side3 = self.get_dis(self.__v2, self.__v3)
        return side1 + side2 + side3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())


