def is_triangle(sides):
    sorted_sides = sorted(sides)
    return sorted_sides[0] > 0 and sum(sorted_sides[:2]) >= sorted_sides[2]

def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3