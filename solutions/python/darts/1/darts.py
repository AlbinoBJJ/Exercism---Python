def score(x, y):
    radius = ((1, 10), (5, 5), (10, 1))
    shoot = (x**2 + y**2)**0.5
    for r, points in radius:
        if shoot <= r:
            return points
    return 0