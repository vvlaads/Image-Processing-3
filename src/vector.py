from math import sqrt


class Vector:
    def __init__(self, x, y, z):
        """Конструктор"""
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """Сложение векторов"""
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Вычитание векторов"""
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """Умножение вектора на число"""
        return Vector(self.x * other, self.y * other, self.z * other)

    def __imul__(self, other):
        """Умножение числа на вектор"""
        self.x *= other

    def __truediv__(self, other):
        """Деление вектора на число"""
        return Vector(self.x / other, self.y / other, self.z / other)

    def __str__(self):
        """Представление вектора в виде строки"""
        return f'({self.x}, {self.y}, {self.z})'

    def vec_mul(self, other):
        """Векторное умножение"""
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)

    def dot(self, other):
        """Скалярное умножение векторов"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def matrix_mul(self, matrix):
        """Умножение вектора на матрицу 3x3"""
        x = matrix[0][0] * self.x + matrix[0][1] * self.y + matrix[0][2] * self.z
        y = matrix[1][0] * self.x + matrix[1][1] * self.y + matrix[1][2] * self.z
        z = matrix[2][0] * self.x + matrix[2][1] * self.y + matrix[2][2] * self.z
        return Vector(x, y, z)

    def length(self):
        """Модуль вектора"""
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        """Нормализованный вектор"""
        return self / self.length()
