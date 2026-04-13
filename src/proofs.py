import math


def triangle_test(v1, v2, v3, dots, parts=10):
    """Численный тест равномерности точек по полоскам внутри треугольника"""

    v = v2 - v1
    u = v3 - v1

    v_dir = v.normalize()
    u_dir = u.normalize()

    v_len = v.length()
    u_len = u.length()

    slices = [0] * parts
    for p in dots:
        for i in range(1, parts + 1):
            v_part = v1 + v_dir * (v_len * i / parts)
            u_part = v1 + u_dir * (u_len * i / parts)
            if in_triangle(v1, v_part, u_part, p):
                slices[i - 1] += 1
                break

    # площадь всего треугольника
    s_total = triangle_area(v1, v2, v3)
    squares = []
    for i in range(1, parts + 1):
        a0 = (i - 1) / parts
        a1 = i / parts
        strip_area = s_total * (a1 ** 2 - a0 ** 2)
        squares.append(strip_area)

    for i in range(parts):
        print(
            f"Полоска {i + 1}: {slices[i]} точек; Площадь: {squares[i]: .4f}; Отношение: {slices[i] / squares[i] : .4f}")


def triangle_area(a, b, c):
    return abs((b - a).vec_mul(c - a).length()) / 2


def in_triangle(v1, v2, v3, p):
    """Проверка точки внутри треугольника через площади"""

    s = triangle_area(v1, v2, v3)
    s_sum = triangle_area(p, v1, v2) + triangle_area(p, v2, v3) + triangle_area(p, v3, v1)

    return abs(s - s_sum) < 1e-9


def circle_test(n, radius, center, dots, parts=10):
    """Численный тест равномерности точек внутри круга"""

    slices = [0] * parts
    for p in dots:
        for i in range(1, parts + 1):
            r_outer = i * radius / parts
            r_inner = (i - 1) * radius / parts

            if in_circle(n, r_outer, center, p) and not in_circle(n, r_inner, center, p):
                slices[i - 1] += 1
                break

    # площадь всего круга
    s_total = circle_area(radius)

    squares = []
    for i in range(1, parts + 1):
        r_outer = i / parts
        r_inner = (i - 1) / parts

        # площадь кольца
        strip_area = s_total * (r_outer ** 2 - r_inner ** 2)
        squares.append(strip_area)

    for i in range(parts):
        print(
            f"Кольцо {i + 1}: {slices[i]} точек; "
            f"Площадь: {squares[i]: .4f}; "
            f"Отношение: {slices[i] / squares[i]: .4f}"
        )


def in_circle(n, r, center, dot, eps=1e-6):
    v = dot - center
    if abs(v.dot(n)) > eps:
        return False
    return v.length() <= r


def circle_area(r):
    return math.pi * r ** 2
