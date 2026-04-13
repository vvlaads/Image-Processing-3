import random

from methods import *
from proofs import *
from vector import Vector


def print_sep():
    """Печать разделителя для лучшей читаемости вывода"""
    print("=" * 100)


random.seed(42)  # Сид для генерации случайных чисел

# Распределение для треугольника
v1 = Vector(0, 0, 0)
v2 = Vector(100, 100, 0)
v3 = Vector(100, 0, 0)
triangle_dots = triangle_distribution(random, v1, v2, v3, 100_000)
triangle_test(v1, v2, v3, triangle_dots)
print_sep()

# Распределение для круга
n = Vector(0, 0, 1)
center = Vector(0, 0, 0)
radius = 5
circle_dots = circle_distribution(random, n, radius, center, 100_000)
circle_test(n, radius, center, circle_dots)
print_sep()

# Распределение для сферы
center = Vector(0, 0, 0)
radius = 5
sphere_dots = sphere_distribution(random, radius, center, 100_000)
print_sep()

# Косинусное распределение
n = Vector(0, 0, 1)
c = Vector(0, 0, 0)
radius = 5
cos_dots = cos_distribution(random, n, c, radius, 100_000)
print_sep()
