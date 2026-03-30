import random

from methods import *
from vector import Vector


def print_sep():
    """Печать разделителя для лучшей читаемости вывода"""
    print("=" * 100)


random.seed(42)  # Сид для генерации случайных чисел

# Распределение для треугольника
v1 = Vector(0, 0, 0)
v2 = Vector(1, 1, 0)
v3 = Vector(1, 0, 0)
triangle_dots = triangle_distribution(random, v1, v2, v3, 100_000)
print("Распределение для треугольника")
print("Первые 10 точек:")
for i in range(10):
    print(triangle_dots[i])

print_sep()

# Распределение для круга
n = Vector(0, 0, 1)
center = Vector(0, 0, 0)
radius = 5
circle_dots = circle_distribution(random, n, radius, center, 100_000)
print("Распределение для круга")
print("Первые 10 точек:")
for i in range(10):
    print(circle_dots[i])

print_sep()

# Распределение для сферы
center = Vector(0, 0, 0)
radius = 5
sphere_dots = sphere_distribution(random, radius, center, 100_000)
print("Распределение для сферы")
print("Первые 10 точек:")
for i in range(10):
    print(sphere_dots[i])

print_sep()

# Косинусное распределение
n = Vector(0, 0, 1)
c = Vector(0, 0, 0)
radius = 5
cos_dots = cos_distribution(random, n, c, radius, 100_000)
print("Косинусное распределение")
print("Первые 10 точек:")
for i in range(10):
    print(cos_dots[i])
print_sep()
