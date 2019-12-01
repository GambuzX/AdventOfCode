import re


class Point:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy


points = []

file = open("input.txt")
for line in file:
    x = int(re.search("(position=<)([0-9-\s-]*)(,)", line).group(2))
    y = int(re.search("(,\s)([0-9-\s-]*)(> velocity)", line).group(2))
    vx = int(re.search("(velocity=<)([0-9-\s-]*)(,)", line).group(2))
    vy = int(re.search("(velocity=<)([0-9-\s-]*)(,\s)([0-9-\s-]*)", line).group(4))
    points.append(Point(x,y,vx,vy))
file.close()


def point_in_coord(x,y, points_l):
    for point in points_l:
        if point.x == x and point.y == y:
            return True
    return False


def display_points(points_l):
    max_x = 0
    min_x = 999999
    max_y = 0
    min_y = 999999
    for point in points_l:
        if point.x > max_x:
            max_x = point.x
        if point.x < min_x:
            min_x = point.x
        if point.y > max_y:
            max_y = point.y
        if point.y < min_y:
            min_y = point.y

    display_string = ""
    for row in range(min_y, max_y+1):
        for col in range(min_x, max_x+1):
            if point_in_coord(col, row, points_l):
                display_string += '#'
            else:
                display_string += '.'
        display_string += '\n'
    print(display_string)


def points_distance(points_l):
    total = 0
    for point1 in points_l:
        for point2 in points_l:
            total += abs(point2.y - point1.y) + abs(point1.x - point2.x)
    return total


def pre_iterate(points_l, amount):
    for point in points_l:
        point.x += point.vx*amount
        point.y += point.vy*amount


pre_iterate(points, 10020)
prev_val = -1
current_val = points_distance(points)
while True:
    if prev_val != -1 and current_val > prev_val:
        for i in range(5):
            for point in points:
                point.x -= point.vx
                point.y -= point.vy
        for i in range(10):
            for point in points:
                point.x += point.vx
                point.y += point.vy
            display_points(points)
        break
    prev_val = current_val
    for point in points:
        point.x += point.vx
        point.y += point.vy
    current_val = points_distance(points)
