from vector import Vector
from math import sqrt, sin, cos, pi


def triangle_distribution(random, v1, v2, v3, dots_count):
    """Равномерное распределение случайных точек внутри треугольника"""
    v = (v2 - v1).normalize()
    u = (v3 - v1).normalize()

    v_r = (v2 - v1).length()
    u_r = (v3 - v1).length()

    dots = []
    for i in range(dots_count):
        xi1 = random.random()
        xi2 = random.random()
        if xi1 + xi2 > 1:
            xi1 = 1 - xi1
            xi2 = 1 - xi2
        p = v1 + v * v_r * xi1 + u * u_r * xi2
        dots.append(p)
    return dots


def circle_distribution(random, n, radius, center, dots_count):
    """Равномерное распределение случайных точек внутри круга"""
    if n.x != 0 and n.y != 0:
        v = Vector(-n.y / sqrt(n.y ** 2 + n.x ** 2), n.x / sqrt(n.y ** 2 + n.x ** 2), 0)
    else:
        v = Vector(1, 0, 0)

    u = n.vec_mul(v)

    m = [[v.x, v.y, v.z],
         [u.x, u.y, u.z],
         [n.x, n.y, n.z]]

    dots = []
    for i in range(dots_count):
        xi_r = random.random()
        xi_phi = random.random()

        phi = 2 * pi * xi_phi
        r = radius * sqrt(xi_r)

        p_vun = Vector(r * cos(phi), r * sin(phi), 0)
        p = center + p_vun.matrix_mul(m)
        dots.append(p)

    return dots
